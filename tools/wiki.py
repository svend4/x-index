#!/usr/bin/env python3
"""Инструменты вики x-index. Только стандартная библиотека Python 3.10+.

Подкоманды:
  harvest-mcp  выгрузить реестр MCP (публичный API, пагинация, version=latest) в wiki/raw/mcp-registry/<дата>/
               и записать компактный снимок servers.ndjson.gz (он попадает в git; постраничные файлы — нет)
  build        создать карточки-заготовки для кандидатов из снимков, индекс покрытия coverage.json,
               пересобрать INDEX.md, кластеры и catalog.json
  lint         проверить карточки по wiki/SCHEMA.md (код выхода 1, если есть ошибки)
  index        пересобрать SQLite FTS5 индекс wiki/.index/wiki.sqlite: карточки (уровень 1)
               и все записи реестра (уровень 2, без отдельных файлов)
  ask          поиск: карточки с фильтрами плюс записи каталога реестра
  queue        очередь заданий для агентов-обогатителей: wiki/queue/enrich-queue.jsonl

Типичный проход:
  python3 tools/wiki.py harvest-mcp
  python3 tools/wiki.py build && python3 tools/wiki.py lint && python3 tools/wiki.py index
  python3 tools/wiki.py ask "счета XRechnung" --cluster 14-accounting-einvoice
  python3 tools/wiki.py queue --batch 25

Если TLS через прокси не проходит, укажите путь к CA-бандлу:
  SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 tools/wiki.py harvest-mcp
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import sqlite3
import ssl
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CARDS = WIKI / "cards"
CLUSTERS_DIR = WIKI / "clusters"
RAW_MCP = WIKI / "raw" / "mcp-registry"
RAW_SESSION = WIKI / "raw" / "session"
QUEUE_DIR = WIKI / "queue"
INDEX_DIR = WIKI / ".index"
INDEX_DB = INDEX_DIR / "wiki.sqlite"
TAXONOMY_FILE = WIKI / "taxonomy.json"

MCP_API = "https://registry.modelcontextprotocol.io/v0/servers"
OFFICIAL_META = "io.modelcontextprotocol.registry/official"
USER_AGENT = "x-index-wiki-harvester/0.1"
SNAPSHOT_NAME = "servers.ndjson.gz"

GEN_NOTE = "<!-- Создано tools/wiki.py. Не править вручную: файл перезаписывается при сборке. -->"
PENDING = "_Ожидает заполнения (стадия enrich)._"
STALE_DAYS = 180
SUMMARY_MAX = 240
MIN_DESC = 20

KINDS = {"connector", "mcp-server", "skill", "plugin", "app", "api", "package", "other"}
STATUSES = {"stub", "draft", "verified", "retired"}
DATA_CLASSES = {"A", "B", "C", "unknown"}
PRICES = {"free", "freemium", "trial", "paid", "enterprise", "unknown"}
AUTHS = {"none", "api-key", "oauth", "account", "unknown"}
HOSTINGS = {"EU", "US", "global", "unknown"}
HINTS = {"test", "later", "no", "none"}

REQUIRED_FIELDS = [
    "id", "title", "kind", "vendor", "cluster", "summary", "status", "data_class",
    "price", "auth", "hosting", "languages", "source_urls", "snapshot", "verified_on", "updated",
]
OPTIONAL_FIELDS = ["group", "tags", "hosted", "curator_hint", "jurisdiction"]
REQUIRED_SECTIONS = [
    "## Суть", "## Для чего", "## Возможности", "## Чем выделяется", "## Ограничения и риски",
    "## Когда не подходит", "## Альтернативы", "## Источники", "## Заявлено автором",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SECRET_RE = re.compile(r"\b(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[bp]-[A-Za-z0-9-]{10,})")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
STATUS_ORDER = {"verified": 0, "draft": 1, "stub": 2, "retired": 3}
STOPWORDS = {
    "и", "в", "во", "на", "для", "что", "как", "или", "по", "с", "со", "к", "о", "об", "от", "до",
    "из", "за", "не", "да", "это", "какой", "какие", "какая", "какое", "нужен", "нужна", "есть",
    "мне", "мой", "the", "a", "an", "of", "and", "or", "to", "for", "with", "in", "on", "is",
    "are", "which", "what", "how", "der", "die", "das", "und", "oder", "für", "mit", "ein", "eine",
}

# Первичная классификация по ключевым словам. Порядок важен: побеждает первое совпадение.
# Это эвристика. Результат — гипотеза; агенты уточняют её на стадии enrich.
RULES: list[tuple[str, tuple[str, ...]]] = [
    ("13-medical-care", ("medical", "medicine", "clinical", "fhir", "patient", "icd", "pharma", "hospital")),
    ("14-accounting-einvoice", ("invoice", "accounting", "bookkeeping", "xrechnung", "zugferd", "datev", "quickbooks", "xero")),
    ("15-commerce-finance", ("shopify", "e-commerce", "ecommerce", "woocommerce", "stripe", "payment", "plaid", "banking", "paypal", "checkout")),
    ("16-crm-sales", ("crm", "salesforce", "hubspot", "pipedrive")),
    ("17-pm-agile", ("jira", "linear", "asana", "clickup", "monday.com", "trello", "project management", "kanban", "issue tracker")),
    ("22-meetings-speech", ("meeting", "transcript", "speech-to-text", "transcription", "whisper", "podcast", "zoom")),
    ("20-compliance-ai-act", ("compliance", "gdpr", "dsgvo", "ai act", "privacy", "soc 2", "iso 27001", "dpia")),
    ("11-law-de-eu", ("german", "deutsch", "gesetz", "bundes", "eur-lex", "eu law", "sozial", "urteil")),
    ("12-law-other", ("legal", "law ", "court", "statute", "lawyer", "attorney", "case law")),
    ("08-automation-ipaas", ("zapier", "make.com", "n8n", "ifttt", "workflow", "automation", "webhook", "pipedream")),
    ("06-dev-code", ("github", "gitlab", "bitbucket", "pull request", "docker", "kubernetes", "sentry", "code review", "ci/cd")),
    ("07-data-analytics", ("bigquery", "snowflake", "postgres", "mysql", "sqlite", "database", "sql", "analytics", "amplitude", "mixpanel", "warehouse", "clickhouse", "duckdb")),
    ("09-browser-web-data", ("browser", "playwright", "puppeteer", "scrap", "crawl", "selenium", "web automation")),
    ("01-communication", ("gmail", "email", "e-mail", "outlook", "slack", "discord", "telegram", "whatsapp", "teams", "imap", "smtp", "inbox")),
    ("02-calendar-tasks", ("calendar", "reminder", "todoist", "google tasks")),
    ("04-sheets-data-entry", ("spreadsheet", "google sheets", "excel", "airtable", "csv")),
    ("05-slides-design", ("slide", "presentation", "powerpoint", "canva", "figma", "design tool", "graphic")),
    ("24-office-documents", ("pdf", "docx", "xlsx", "pptx", "word document", "ocr")),
    ("21-files-storage", ("google drive", "dropbox", "onedrive", "sharepoint", "box.com", " s3", "bucket", "file storage", "filesystem")),
    ("03-docs-knowledge", ("notion", "confluence", "obsidian", "wiki", "knowledge base", "markdown", "google docs")),
    ("18-memory-sessions", ("memory", "knowledge graph", "handoff", "checkpoint")),
    ("19-agents-orchestration", ("agent", "orchestrat", "subagent")),
    ("23-ai-models-media", ("image generation", "video generation", "text-to-speech", "llm", "inference", "openai", "anthropic", "gemini", "stable diffusion", "hugging face")),
    ("10-search-research", ("research", "arxiv", "pubmed", "wikipedia", "scholar", "literature", "citation")),
    ("00-meta", ("ecosystem", "marketplace", "plugin", "skill manager", "catalog")),
]

STATE_TEXT = {
    "connected": "подключён",
    "connected_tools_loaded": "подключён, инструменты загружены в сессию",
    "not_connected": "не подключён",
    "connect_incomplete": "подключение не завершено",
    "disconnected": "отключён",
    "enabled": "включён",
    "available": "доступен в сессии",
    "auth_required": "нужна авторизация (системное уведомление сессии)",
    "failed": "не удалось подключить (системное уведомление сессии)",
}

Card = tuple[Path, dict, str]


# ---------------------------------------------------------------- утилиты

def today() -> str:
    return dt.date.today().isoformat()


def txt(value: object) -> str:
    return "" if value is None else str(value)


def clip(text: str, limit: int = SUMMARY_MAX) -> str:
    flat = " ".join(text.split())
    return flat if len(flat) <= limit else flat[: limit - 1] + "…"


def md_text(value: object) -> str:
    return " ".join(txt(value).split()).replace("[", "(").replace("]", ")")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slugify(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", norm.lower()).strip("-")
    return slug or "item"


def classify(text: str) -> str:
    low = text.lower()
    for code, words in RULES:
        if any(word in low for word in words):
            return code
    return "99-other"


def load_taxonomy() -> dict[str, dict]:
    data = json.loads(TAXONOMY_FILE.read_text(encoding="utf-8"))
    return {c["code"]: c for c in data["clusters"]}


def fm_value(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (list, tuple)):
        return json.dumps(list(value), ensure_ascii=False)
    return json.dumps(str(value), ensure_ascii=False)


def render_card(meta: dict, body: str) -> str:
    known = REQUIRED_FIELDS + OPTIONAL_FIELDS
    keys = [k for k in known if k in meta] + sorted(k for k in meta if k not in known)
    front = ["---"] + [f"{k}: {fm_value(meta[k])}" for k in keys] + ["---"]
    return "\n".join(front) + "\n" + body.rstrip() + "\n"


def parse_card(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("нет блока frontmatter в начале файла")
    end = text.find("\n---\n", 3)
    if end == -1:
        raise ValueError("frontmatter не закрыт строкой ---")
    meta: dict = {}
    for lineno, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, raw = line.partition(":")
        if not sep or not key.strip():
            raise ValueError(f"строка {lineno} frontmatter без вида «ключ: значение»")
        raw = raw.strip()
        try:
            meta[key.strip()] = json.loads(raw)
        except json.JSONDecodeError:
            meta[key.strip()] = raw
    return meta, text[end + 5:]


def load_cards() -> tuple[list[Card], list[str]]:
    cards: list[Card] = []
    problems: list[str] = []
    for path in sorted(CARDS.rglob("*.md")):
        try:
            meta, body = parse_card(path)
        except ValueError as exc:
            problems.append(f"{path.relative_to(ROOT).as_posix()}: {exc}")
            continue
        cards.append((path, meta, body))
    return cards, problems


def latest_snapshot(base: Path, marker: str) -> Path | None:
    if not base.exists():
        return None
    dirs = sorted(d for d in base.iterdir() if d.is_dir() and (d / marker).exists())
    return dirs[-1] if dirs else None


def http_get(url: str, tries: int = 5, timeout: int = 60) -> bytes:
    cafile = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    ctx = ssl.create_default_context(cafile=cafile) if cafile else ssl.create_default_context()
    delay = 2.0
    for attempt in range(1, tries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if not (exc.code == 429 or exc.code >= 500) or attempt == tries:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == tries:
                raise
        time.sleep(delay)
        delay *= 2
    raise RuntimeError("недостижимо")


# ---------------------------------------------------------------- реестр MCP: выгрузка и компактный снимок

def compact(entry: dict) -> dict | None:
    """Одна запись реестра -> компактная строка снимка. Поля, которые не нужны вики, отбрасываются."""
    server = entry.get("server") or {}
    name = server.get("name")
    if not name:
        return None
    official = (entry.get("_meta") or {}).get(OFFICIAL_META) or {}
    remotes = []
    for remote in server.get("remotes") or []:
        host = urllib.parse.urlparse(txt(remote.get("url"))).hostname or ""
        remotes.append({"type": txt(remote.get("type")) or "?", "host": host})
    repo = server.get("repository")
    return {
        "name": name,
        "title": txt(server.get("title")) or name,
        "version": txt(server.get("version")),
        "description": " ".join(txt(server.get("description")).split()),
        "status": txt(official.get("status")) or "active",
        "published": txt(official.get("publishedAt"))[:10],
        "updated": txt(official.get("updatedAt"))[:10],
        "is_latest": bool(official.get("isLatest")),
        "remotes": remotes,
        "repository": txt(repo.get("url")) if isinstance(repo, dict) else "",
    }


def harvest_mcp(args: argparse.Namespace) -> int:
    date = args.date or today()
    out_dir = RAW_MCP / date
    if (out_dir / "manifest.json").exists() and not args.force:
        print(f"снимок {date} уже есть: {out_dir.relative_to(ROOT).as_posix()} (нужен --force или другая --date)", file=sys.stderr)
        return 2
    pages_dir = out_dir / "pages"  # рабочие постраничные файлы; в git не попадают (см. .gitignore)
    pages_dir.mkdir(parents=True, exist_ok=True)

    base_params = {"limit": str(args.limit)}
    if not args.all_versions:
        base_params["version"] = "latest"
    cursor: str | None = None
    seen: set[str] = set()
    raw_total = 0
    pages = 0
    complete = False
    t0 = time.time()
    for number in range(1, args.max_pages + 1):
        params = dict(base_params)
        if cursor:
            params["cursor"] = cursor
        raw = http_get(f"{MCP_API}?{urllib.parse.urlencode(params)}")
        data = json.loads(raw)
        servers = data.get("servers") or []
        with gzip.open(pages_dir / f"page-{number:05d}.json.gz", "wb") as fh:
            fh.write(raw)
        pages = number
        raw_total += len(servers)
        if number == 1 or number % 25 == 0:
            print(f"стр. {number}: записей {raw_total}", flush=True)
        nxt = (data.get("metadata") or {}).get("nextCursor")
        if not nxt or not servers:
            complete = True
            break
        if nxt in seen:
            print("курсор повторился, останавливаюсь", file=sys.stderr)
            complete = True
            break
        seen.add(nxt)
        cursor = nxt
        time.sleep(args.sleep)
    if not complete:
        print(f"внимание: достигнут --max-pages={args.max_pages}, выгрузка неполная", file=sys.stderr)

    best: dict[str, dict] = {}
    for page in sorted(pages_dir.glob("page-*.json.gz")):
        with gzip.open(page, "rb") as fh:
            data = json.loads(fh.read())
        for entry in data.get("servers") or []:
            rec = compact(entry)
            if rec is None:
                continue
            current = best.get(rec["name"])
            if current is None or (rec["is_latest"], rec["published"]) > (current["is_latest"], current["published"]):
                best[rec["name"]] = rec

    snapshot_path = out_dir / SNAPSHOT_NAME
    with gzip.open(snapshot_path, "wt", encoding="utf-8") as fh:
        for name in sorted(best):
            fh.write(json.dumps(best[name], ensure_ascii=False) + "\n")
    manifest = {
        "source": MCP_API,
        "query": base_params,
        "snapshot": date,
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "pages": pages,
        "raw_entries": raw_total,
        "unique_servers": len(best),
        "complete": complete,
        "snapshot_file": SNAPSHOT_NAME,
        "snapshot_sha256": sha256_bytes(snapshot_path.read_bytes()),
        "note": "Публичный API реестра MCP, без авторизации. Запросы не содержат данных пользователя; User-Agent общий. Постраничные файлы pages/ не коммитятся.",
        "tool": "tools/wiki.py harvest-mcp",
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"готово: страниц {pages}, записей {raw_total}, уникальных серверов {len(best)}, "
          f"за {time.time() - t0:.0f} с → {out_dir.relative_to(ROOT).as_posix()}")
    return 0 if complete else 1


def load_mcp_snapshot(snapshot_dir: Path) -> list[dict]:
    with gzip.open(snapshot_dir / SNAPSHOT_NAME, "rt", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def mcp_id(name: str, owner: dict[str, str]) -> str:
    base = "mcp-" + slugify(name)
    if owner.get(base, f"mcp:{name}") == f"mcp:{name}":
        return base
    return f"{base}-{hashlib.sha1(name.encode('utf-8')).hexdigest()[:6]}"


def candidate_score(rec: dict, recent_cutoff: str) -> int:
    """Кандидат в карточки: чем больше признаков зрелости, тем выше. Не оценка качества, а порядок очереди."""
    score = 0
    if rec.get("repository"):
        score += 2
    if rec.get("remotes"):
        score += 2
    if len(rec.get("description", "")) >= 80:
        score += 1
    if rec.get("published", "") >= recent_cutoff:
        score += 1
    return score


# ---------------------------------------------------------------- карточки-заготовки

def stub_body(title: str, claim: str, sources: list[str], points: list[str] | None = None,
              points_title: str = "Точки подключения (как заявлено)") -> str:
    parts = [f"# {title}", ""]
    for section in REQUIRED_SECTIONS:
        parts += [section, ""]
        if section == "## Источники":
            parts += [f"- {src}" for src in sources] + [""]
        elif section == "## Заявлено автором":
            quoted = (claim or "Описание в источнике отсутствует.").strip().splitlines() or [""]
            parts += [("> " + line) if line.strip() else ">" for line in quoted] + [""]
        else:
            parts += [PENDING, ""]
    if points:
        parts += [f"## {points_title}", ""] + [f"- {p}" for p in points] + [""]
    return "\n".join(parts)


def inventory_card(row: dict, snapshot: str) -> tuple[dict, str]:
    state = STATE_TEXT.get(row["state"], row["state"])
    claim = " ".join(txt(row.get("platform_description")).split())
    summary = clip(f"Состояние: {state}. Описание платформы: {claim}" if claim
                   else f"Состояние: {state}. Описание в каталоге отсутствует.")
    meta = {
        "id": row["id"], "title": row["name"], "kind": row["kind"], "vendor": row.get("vendor") or "уточнить",
        "cluster": row["cluster"], "summary": summary, "status": "stub", "data_class": "unknown",
        "price": "unknown", "auth": "unknown", "hosting": "unknown", "languages": [],
        "source_urls": [f"raw://session/{snapshot}/inventory.json"], "snapshot": snapshot,
        "verified_on": None, "updated": today(),
    }
    if row.get("group"):
        meta["group"] = row["group"]
    body = stub_body(
        row["name"], claim,
        sources=[f"Инвентарь сессии `raw://session/{snapshot}/inventory.json` (источник: {row.get('source', 'сессия')})"],
        points=[f"Состояние в сессии: {state}"],
        points_title="Состояние в сессии",
    )
    return meta, body


def mcp_card(rec: dict, snapshot: str, cid: str, cluster: str) -> tuple[dict, str]:
    name = rec["name"]
    desc = SECRET_RE.sub("[редактировано: токен-подобная строка]", rec["description"])
    search_url = f"{MCP_API}?search={urllib.parse.quote(name)}"
    summary = clip(f"[заявлено реестром, EN] {desc}" if desc else f"[заявлено реестром] {rec['title']}, описания нет")
    hosts = [f"{r['type']}: `{r['host'] or '?'}`" for r in rec["remotes"]]
    meta = {
        "id": cid, "title": rec["title"], "kind": "mcp-server",
        "vendor": name.split("/", 1)[0] if "/" in name else name,
        "cluster": cluster, "summary": summary, "status": "stub", "data_class": "unknown",
        "price": "unknown", "auth": "unknown", "hosting": "unknown", "languages": [],
        "source_urls": [search_url], "snapshot": snapshot, "verified_on": None, "updated": today(),
        "hosted": bool(rec["remotes"]),
    }
    sources = [
        f"Реестр MCP, запись `{name}`, версия {rec['version'] or '?'}: {search_url}",
        f"Снимок `raw://mcp-registry/{snapshot}/{SNAPSHOT_NAME}`",
    ]
    if rec.get("published"):
        sources.append(f"Опубликовано в реестре: {rec['published']}")
    if rec.get("repository"):
        sources.append(f"Репозиторий, как заявлено в реестре: {rec['repository']}")
    body = stub_body(rec["title"], desc, sources=sources, points=hosts)
    return meta, body


def build(args: argparse.Namespace) -> int:
    tax = load_taxonomy()
    cards, problems = load_cards()
    for msg in problems:
        print(f"пропуск (не читается): {msg}", file=sys.stderr)
    existing: dict[str, tuple[Path, str]] = {}
    for path, meta, _ in cards:
        existing[txt(meta.get("id", path.stem))] = (path, txt(meta.get("status")))
    owner: dict[str, str] = {}
    placed: set[str] = set()
    stats: Counter[str] = Counter()

    def place(cid: str, cluster: str, meta: dict, body: str, owner_key: str) -> None:
        if cluster not in tax:
            stats["ошибки кластера"] += 1
            print(f"ошибка: кластер {cluster!r} отсутствует в taxonomy.json (карточка {cid})", file=sys.stderr)
            return
        if owner.get(cid, owner_key) != owner_key:
            stats["коллизии id"] += 1
            return
        owner[cid] = owner_key
        target = CARDS / cluster / f"{cid}.md"
        if cid in existing:
            old_path, old_status = existing[cid]
            if old_status != "stub":
                stats["сохранено рукописных"] += 1
                return
            stats["заготовок обновлено"] += 1
            if old_path != target and old_path.exists():
                old_path.unlink()
                stats["перенесено"] += 1
        else:
            stats["заготовок создано"] += 1
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_card(meta, body), encoding="utf-8")
        existing[cid] = (target, "stub")
        placed.add(cid)

    inv_dir = latest_snapshot(RAW_SESSION, "inventory.json")
    if inv_dir:
        inventory = json.loads((inv_dir / "inventory.json").read_text(encoding="utf-8"))
        for row in inventory["items"]:
            meta, body = inventory_card(row, inv_dir.name)
            place(row["id"], row["cluster"], meta, body, f"inv:{row['id']}")
        stats["позиций в инвентаре сессии"] = len(inventory["items"])

    mcp_dir = latest_snapshot(RAW_MCP, "manifest.json")
    if mcp_dir:
        records = load_mcp_snapshot(mcp_dir)
        recent_cutoff = (dt.date.today() - dt.timedelta(days=365)).isoformat()
        active = [r for r in records if r["status"] == "active"]
        priority_codes = {code for code, c in tax.items() if c.get("priority")}
        candidates = [r for r in active if len(r["description"]) >= MIN_DESC]

        def rank(r: dict) -> tuple:
            cluster_guess = classify(f"{r['title']} {r['name']} {r['description']}")
            return (0 if cluster_guess in priority_codes else 1, -candidate_score(r, recent_cutoff), r["name"])

        candidates.sort(key=rank)
        chosen = candidates[: args.cards_limit]
        for rec in chosen:
            cid = mcp_id(rec["name"], owner)
            cluster = classify(f"{rec['title']} {rec['name']} {rec['description']}")
            meta, body = mcp_card(rec, mcp_dir.name, cid, cluster)
            place(cid, cluster, meta, body, f"mcp:{rec['name']}")
        coverage = {
            "snapshot": mcp_dir.name,
            "unique_servers": len(records),
            "active": len(active),
            "deprecated": len(records) - len(active),
            "active_with_description_20plus": len(candidates),
            "active_with_remotes": sum(1 for r in active if r["remotes"]),
            "active_with_repository": sum(1 for r in active if r["repository"]),
            "active_published_last_365_days": sum(1 for r in active if r["published"] >= recent_cutoff),
            "card_candidates_selected": len(chosen),
            "cards_limit": args.cards_limit,
            "active_by_keyword_cluster": dict(sorted(Counter(
                classify(f"{r['title']} {r['name']} {r['description']}") for r in active).items())),
        }
        (mcp_dir / "coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        pruned = 0
        for cid, (path, status) in list(existing.items()):
            if status != "stub" or cid in placed or not path.exists():
                continue
            old_meta, _ = parse_card(path)
            if any("registry.modelcontextprotocol.io" in txt(u) for u in (old_meta.get("source_urls") or [])):
                path.unlink()
                del existing[cid]
                pruned += 1
        stats["устаревших заготовок реестра удалено"] = pruned
        stats["серверов реестра уникальных"] = len(records)
        stats["активных"] = len(active)
        stats["кандидатов в карточки (выбрано)"] = len(chosen)

    write_generated(tax)
    print("Сборка завершена:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    return 0


def write_generated(tax: dict[str, dict]) -> None:
    cards, _ = load_cards()
    by_cluster: dict[str, list[tuple[Path, dict]]] = defaultdict(list)
    for path, meta, _ in cards:
        by_cluster[txt(meta.get("cluster")) or "99-other"].append((path, meta))

    CLUSTERS_DIR.mkdir(parents=True, exist_ok=True)
    for code, cluster in tax.items():
        items = by_cluster.get(code, [])
        counts = Counter(txt(m.get("status")) for _, m in items)
        lines = [GEN_NOTE, "", f"# {code} · {cluster['title']}", "", cluster["description"], "",
                 f"Карточек: {len(items)} · " + (", ".join(f"{k}: {v}" for k, v in sorted(counts.items())) or "пусто"), ""]
        groups: dict[str, list[tuple[Path, dict]]] = defaultdict(list)
        for path, meta in items:
            groups[txt(meta.get("group"))].append((path, meta))
        order = list(cluster.get("groups", [])) + [""]
        order += [g for g in groups if g not in order]
        for group in order:
            members = sorted(groups.get(group, []),
                             key=lambda pm: (STATUS_ORDER.get(txt(pm[1].get("status")), 9), txt(pm[1].get("title")).lower()))
            if not members:
                continue
            lines += [f"## {group or 'Без группы'} ({len(members)})", ""]
            for path, meta in members:
                rel = os.path.relpath(path, CLUSTERS_DIR).replace(os.sep, "/")
                lines.append(f"- [{md_text(meta.get('title'))}]({rel}) · `{txt(meta.get('kind'))}` · "
                             f"{txt(meta.get('status'))} · класс {txt(meta.get('data_class'))} — {md_text(meta.get('summary'))}")
            lines.append("")
        (CLUSTERS_DIR / f"{code}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    status_totals = Counter(txt(m.get("status")) for _, m, _ in cards)
    lines = [GEN_NOTE, "", "# Вики x-index — оглавление", "",
             f"Обновлено: {today()} · карточек: {len(cards)} · "
             + " · ".join(f"{k}: {status_totals.get(k, 0)}" for k in ["stub", "draft", "verified", "retired"]), "",
             "| Кластер | Карточек | stub | draft | verified |", "|---|---:|---:|---:|---:|"]
    for code, cluster in tax.items():
        items = by_cluster.get(code, [])
        counts = Counter(txt(m.get("status")) for _, m in items)
        lines.append(f"| [{code} · {md_text(cluster['title'])}](clusters/{code}.md) | {len(items)} | "
                     f"{counts.get('stub', 0)} | {counts.get('draft', 0)} | {counts.get('verified', 0)} |")
    lines += ["", "## Навигация", "",
              "- Правила карточек: [SCHEMA.md](SCHEMA.md)",
              "- Таксономия: [TAXONOMY.md](TAXONOMY.md)",
              "- Журнал изменений: [log.md](log.md)",
              "- Машиночитаемый каталог карточек: [catalog.json](catalog.json)",
              "- Очередь заданий для агентов: [queue/](queue/)",
              "- Поиск из терминала: `python3 tools/wiki.py ask \"запрос\"` (карточки и каталог реестра)", ""]
    (WIKI / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    tax_lines = [GEN_NOTE, "", "# Таксономия вики", "",
                 "Источник правды — `wiki/taxonomy.json`. Этот файл — читаемая версия.", ""]
    for code, cluster in tax.items():
        tax_lines += [f"## {code} · {cluster['title']}", "", cluster["description"], ""]
        tax_lines += [f"- {g}" for g in cluster.get("groups", [])] + [""]
    (WIKI / "TAXONOMY.md").write_text("\n".join(tax_lines), encoding="utf-8")

    records = []
    for path, meta, _ in cards:
        record = {k: meta[k] for k in REQUIRED_FIELDS + OPTIONAL_FIELDS if k in meta}
        record["path"] = path.relative_to(ROOT).as_posix()
        records.append(record)
    (WIKI / "catalog.json").write_text(json.dumps(records, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- lint

def lint(args: argparse.Namespace) -> int:
    tax = load_taxonomy()
    cards, problems = load_cards()
    errors: list[str] = list(problems)
    warnings: list[str] = []
    seen: dict[str, str] = {}
    today_d = dt.date.today()

    for path, meta, body in cards:
        rel = path.relative_to(ROOT).as_posix()
        cid = meta.get("id")
        if not isinstance(cid, str) or not cid:
            errors.append(f"{rel}: нет поля id")
            continue
        if cid in seen:
            errors.append(f"{rel}: повтор id «{cid}» (уже в {seen[cid]})")
        seen[cid] = rel
        if path.stem != cid:
            errors.append(f"{rel}: id «{cid}» не совпадает с именем файла")
        missing = [f for f in REQUIRED_FIELDS if f not in meta]
        if missing:
            errors.append(f"{rel}: нет полей: {', '.join(missing)}")
        for field, allowed in (("kind", KINDS), ("status", STATUSES), ("data_class", DATA_CLASSES),
                               ("price", PRICES), ("auth", AUTHS), ("hosting", HOSTINGS)):
            if field in meta and meta[field] not in allowed:
                errors.append(f"{rel}: {field}={meta[field]!r}; допустимо: {', '.join(sorted(allowed))}")
        if "curator_hint" in meta and meta["curator_hint"] not in HINTS:
            errors.append(f"{rel}: curator_hint={meta['curator_hint']!r}; допустимо: test, later, no, none")
        cluster = meta.get("cluster")
        if cluster not in tax:
            errors.append(f"{rel}: неизвестный кластер {cluster!r}")
        elif path.parent.name != cluster:
            warnings.append(f"{rel}: папка «{path.parent.name}» не совпадает с кластером «{cluster}»")
        summary = txt(meta.get("summary"))
        if not summary:
            errors.append(f"{rel}: пустой summary")
        elif len(summary) > SUMMARY_MAX:
            errors.append(f"{rel}: summary длиннее {SUMMARY_MAX} знаков ({len(summary)})")
        for field in ("snapshot", "updated", "verified_on"):
            value = meta.get(field)
            if value is not None and not (isinstance(value, str) and DATE_RE.match(value)):
                errors.append(f"{rel}: {field} должно быть датой ГГГГ-ММ-ДД или null")
        urls = meta.get("source_urls")
        if not isinstance(urls, list):
            errors.append(f"{rel}: source_urls должен быть списком")
        else:
            for url in urls:
                if not (isinstance(url, str) and (url.startswith("https://") or url.startswith("raw://"))):
                    errors.append(f"{rel}: источник должен начинаться с https:// или raw://, получено {url!r}")
        for section in REQUIRED_SECTIONS:
            if section not in body:
                errors.append(f"{rel}: нет раздела «{section}»")
        status = meta.get("status")
        if status != "stub" and PENDING in body:
            errors.append(f"{rel}: статус {status}, но остались заглушки")
        if status == "verified":
            if not meta.get("verified_on"):
                errors.append(f"{rel}: verified требует verified_on")
            if not meta.get("source_urls"):
                errors.append(f"{rel}: verified требует source_urls")
            if meta.get("data_class") == "unknown":
                errors.append(f"{rel}: verified требует класс данных A, B или C")
        vdate = meta.get("verified_on")
        if isinstance(vdate, str) and DATE_RE.match(vdate):
            try:
                age = (today_d - dt.date.fromisoformat(vdate)).days
            except ValueError:
                errors.append(f"{rel}: verified_on не существует в календаре: {vdate}")
            else:
                if age > STALE_DAYS:
                    warnings.append(f"{rel}: проверка устарела ({age} дн.), нужна повторная сверка")
        if SECRET_RE.search(body) or SECRET_RE.search(json.dumps(meta, ensure_ascii=False)):
            errors.append(f"{rel}: найден токен-подобный фрагмент; проверьте и удалите")

    for path, _, body in cards:
        rel = path.relative_to(ROOT).as_posix()
        for link in WIKILINK_RE.findall(body):
            if link.strip() not in seen:
                warnings.append(f"{rel}: ссылка [[{link.strip()}]] не ведёт на карточку")

    print(f"карточек: {len(cards)} · ошибок: {len(errors)} · предупреждений: {len(warnings)}")
    for item in errors[: args.limit]:
        print(f"ОШИБКА {item}")
    for item in warnings[: args.limit]:
        print(f"внимание {item}")
    if len(errors) > args.limit or len(warnings) > args.limit:
        print(f"показаны первые {args.limit}; полный список: --limit N")
    return 1 if errors else 0


# ---------------------------------------------------------------- индекс и поиск

def index(args: argparse.Namespace) -> int:
    cards, problems = load_cards()
    for msg in problems:
        print(f"пропуск: {msg}", file=sys.stderr)
    snap = latest_snapshot(RAW_MCP, "manifest.json")
    records = load_mcp_snapshot(snap) if snap else []
    card_ids = {txt(m.get("id")) for _, m, _ in cards}

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    if INDEX_DB.exists():
        INDEX_DB.unlink()
    con = sqlite3.connect(INDEX_DB)
    con.executescript(
        """
        CREATE TABLE cards (
            id TEXT PRIMARY KEY, title TEXT, kind TEXT, vendor TEXT, cluster TEXT, grp TEXT,
            status TEXT, data_class TEXT, price TEXT, auth TEXT, hosting TEXT, updated TEXT,
            path TEXT, summary TEXT
        );
        CREATE VIRTUAL TABLE cards_fts USING fts5(
            id UNINDEXED, title, tags, summary, body, tokenize = 'unicode61 remove_diacritics 2'
        );
        CREATE TABLE entries (
            name TEXT PRIMARY KEY, title TEXT, version TEXT, status TEXT, published TEXT,
            cluster TEXT, hosted INTEGER, has_repo INTEGER, description TEXT, card_id TEXT
        );
        CREATE VIRTUAL TABLE entries_fts USING fts5(
            name UNINDEXED, title, description, tokenize = 'unicode61 remove_diacritics 2'
        );
        """
    )
    rows, fts = [], []
    for path, meta, body in cards:
        cid = txt(meta["id"])
        rows.append((cid, txt(meta.get("title")), txt(meta.get("kind")), txt(meta.get("vendor")),
                     txt(meta.get("cluster")), txt(meta.get("group")), txt(meta.get("status")),
                     txt(meta.get("data_class")), txt(meta.get("price")), txt(meta.get("auth")),
                     txt(meta.get("hosting")), txt(meta.get("updated")),
                     path.relative_to(ROOT).as_posix(), txt(meta.get("summary"))))
        tags = " ".join(txt(t) for t in (meta.get("tags") or []))
        fts.append((cid, txt(meta.get("title")), tags, txt(meta.get("summary")), body))
    con.executemany("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    con.executemany("INSERT INTO cards_fts (id, title, tags, summary, body) VALUES (?,?,?,?,?)", fts)

    entry_rows, entry_fts = [], []
    for rec in records:
        base = "mcp-" + slugify(rec["name"])
        card_id = base if base in card_ids else ""
        cluster = classify(f"{rec['title']} {rec['name']} {rec['description']}")
        entry_rows.append((rec["name"], rec["title"], rec["version"], rec["status"], rec["published"],
                           cluster, int(bool(rec["remotes"])), int(bool(rec["repository"])),
                           rec["description"], card_id))
        entry_fts.append((rec["name"], rec["title"], rec["description"]))
    con.executemany("INSERT INTO entries VALUES (?,?,?,?,?,?,?,?,?,?)", entry_rows)
    con.executemany("INSERT INTO entries_fts (name, title, description) VALUES (?,?,?)", entry_fts)
    con.commit()
    con.close()
    print(f"индекс: {INDEX_DB.relative_to(ROOT).as_posix()} · карточек: {len(rows)} · записей каталога реестра: {len(entry_rows)}")
    return 0


def fts_terms(query: str) -> list[str]:
    out = []
    for token in re.findall(r"\w+", query.lower()):
        if len(token) < 2 or token in STOPWORDS:
            continue
        stem = token if len(token) <= 4 else token[: max(4, len(token) - 2)]
        out.append(f'"{stem}"*')
    return out


def ask(args: argparse.Namespace) -> int:
    if not INDEX_DB.exists():
        print("индекс не найден, строю…", file=sys.stderr)
        index(args)
    terms = fts_terms(args.query)
    if not terms:
        print("запрос пуст или состоит из служебных слов", file=sys.stderr)
        return 2

    base: dict[str, object] = {}
    card_filters = []
    for field, value in (("cluster", args.cluster), ("kind", args.kind), ("status", args.status),
                         ("data_class", args.data_class), ("price", args.price)):
        if value:
            card_filters.append(f"AND c.{field} = :{field}")
            base[field] = value
    card_sql = f"""
        SELECT c.id, c.title, c.kind, c.cluster, c.grp, c.status, c.data_class, c.price, c.path, c.summary,
               bm25(cards_fts, 0.0, 6.0, 3.0, 3.0, 1.0) AS score,
               snippet(cards_fts, 4, '«', '»', ' … ', 16) AS snip
        FROM cards_fts JOIN cards c ON c.id = cards_fts.id
        WHERE cards_fts MATCH :q {' '.join(card_filters)}
        ORDER BY score
        LIMIT :k
    """
    entry_base: dict[str, object] = {}
    entry_filters = [] if args.include_deprecated else ["AND e.status = 'active'"]
    if args.cluster:
        entry_filters.append("AND e.cluster = :cluster")
        entry_base["cluster"] = args.cluster
    entry_sql = f"""
        SELECT e.name, e.title, e.cluster, e.status, e.published, e.hosted, e.has_repo, e.card_id, e.description,
               bm25(entries_fts, 0.0, 5.0, 1.0) AS score
        FROM entries_fts JOIN entries e ON e.name = entries_fts.name
        WHERE entries_fts MATCH :q {' '.join(entry_filters)}
        ORDER BY score
        LIMIT :k
    """

    con = sqlite3.connect(INDEX_DB)
    con.row_factory = sqlite3.Row

    def search(sql: str, key: str, limit: int, extra: dict) -> list[dict]:
        # сначала совпадение по всем словам (И); если результатов мало, добавляем совпадение по любому слову (ИЛИ)
        found: list[dict] = []
        seen: set[str] = set()
        for joiner in (" AND ", " OR "):
            params = {**extra, "q": joiner.join(terms), "k": limit}
            for row in con.execute(sql, params).fetchall():
                record = dict(row)
                record["match"] = "все слова" if joiner == " AND " else "часть слов"
                if record[key] not in seen:
                    seen.add(record[key])
                    found.append(record)
            if len(found) >= limit:
                break
        return found[:limit]

    try:
        cards_hits = search(card_sql, "id", args.k, base)
        catalog_hits: list[dict] = []
        if not args.cards_only and args.k_catalog > 0:
            catalog_hits = search(entry_sql, "name", args.k_catalog, entry_base)
    finally:
        con.close()

    if args.json:
        print(json.dumps({"cards": cards_hits, "catalog": catalog_hits}, ensure_ascii=False, indent=1))
        return 0
    print(f"Карточки вики ({len(cards_hits)}):")
    if not cards_hits:
        print("  ничего не найдено; попробуйте синонимы или другой язык (RU, EN, DE)")
    for number, r in enumerate(cards_hits, 1):
        print(f"  {number}. {r['title']}  [{r['id']}]")
        print(f"     {r['cluster']} · {r['grp'] or 'без группы'} · {r['kind']} · {r['status']} · класс {r['data_class']} · {r['price']} · совпадение: {r['match']}")
        print(f"     {r['summary']}")
        print(f"     {r['path']}")
        if r["snip"]:
            print(f"     …{r['snip']}…")
    if catalog_hits:
        print(f"\nКаталог реестра MCP ({len(catalog_hits)}):")
        for number, r in enumerate(catalog_hits, 1):
            where = f"карточка: {r['card_id']}" if r["card_id"] else "только строка каталога"
            print(f"  {number}. {r['title']}  [{r['name']}]")
            print(f"     {r['cluster']} · {r['status']} · опубликовано {r['published']} · "
                  f"удалённый сервер: {'да' if r['hosted'] else 'нет'} · репозиторий: {'да' if r['has_repo'] else 'нет'} · {where} · совпадение: {r['match']}")
            print(f"     {clip(r['description'], 200)}")
    return 0


# ---------------------------------------------------------------- очередь для агентов

def queue(args: argparse.Namespace) -> int:
    cards, _ = load_cards()
    rows = []
    for path, meta, _ in cards:
        if meta.get("status") != "stub":
            continue
        sources = [txt(u) for u in (meta.get("source_urls") or [])]
        if any(u.startswith("raw://session") for u in sources):
            priority = 1
        elif meta.get("kind") == "mcp-server" and meta.get("hosted"):
            priority = 2
        elif meta.get("kind") == "mcp-server":
            priority = 3
        else:
            priority = 4
        rows.append((priority, txt(meta["id"]), path, meta))
    rows.sort(key=lambda r: (r[0], r[1]))
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    out = QUEUE_DIR / "enrich-queue.jsonl"
    with out.open("w", encoding="utf-8") as fh:
        for n, (priority, cid, path, meta) in enumerate(rows, start=1):
            record = {
                "n": n, "batch": (n - 1) // args.batch + 1, "priority": priority, "id": cid,
                "path": path.relative_to(ROOT).as_posix(), "cluster": meta.get("cluster"),
                "kind": meta.get("kind"), "task": "enrich", "prompt": "wiki/queue/ENRICH_PROMPT.md",
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    batches = (len(rows) + args.batch - 1) // args.batch
    by_priority = dict(sorted(Counter(r[0] for r in rows).items()))
    print(f"очередь: {len(rows)} заданий · батчей по {args.batch}: {batches} · приоритеты: {by_priority}")
    print(f"файл: {out.relative_to(ROOT).as_posix()}")
    return 0


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Инструменты вики x-index")
    sub = parser.add_subparsers(dest="cmd", required=True)

    h = sub.add_parser("harvest-mcp", help="выгрузить реестр MCP и записать компактный снимок")
    h.add_argument("--date", help="дата снимка ГГГГ-ММ-ДД (по умолчанию сегодня)")
    h.add_argument("--limit", type=int, default=100, help="записей на страницу")
    h.add_argument("--sleep", type=float, default=0.3, help="пауза между страницами, с")
    h.add_argument("--max-pages", type=int, default=2000)
    h.add_argument("--all-versions", action="store_true", help="все версии, а не только последние")
    h.add_argument("--force", action="store_true", help="перезаписать снимок этой даты")
    h.set_defaults(func=harvest_mcp)

    b = sub.add_parser("build", help="создать заготовки карточек и индексы")
    b.add_argument("--cards-limit", type=int, default=1500, help="сколько кандидатов из реестра превращать в карточки")
    b.set_defaults(func=build)

    lt = sub.add_parser("lint", help="проверить карточки по SCHEMA.md")
    lt.add_argument("--limit", type=int, default=50)
    lt.set_defaults(func=lint)

    ix = sub.add_parser("index", help="пересобрать SQLite FTS5 индекс")
    ix.set_defaults(func=index)

    a = sub.add_parser("ask", help="поиск по карточкам и каталогу реестра")
    a.add_argument("query")
    a.add_argument("-k", type=int, default=10, help="сколько карточек вывести")
    a.add_argument("--k-catalog", dest="k_catalog", type=int, default=5, help="сколько строк каталога вывести")
    a.add_argument("--cards-only", action="store_true", help="не искать в каталоге реестра")
    a.add_argument("--include-deprecated", action="store_true", help="учитывать устаревшие записи каталога")
    a.add_argument("--cluster")
    a.add_argument("--kind")
    a.add_argument("--status")
    a.add_argument("--data-class", dest="data_class")
    a.add_argument("--price")
    a.add_argument("--json", action="store_true")
    a.set_defaults(func=ask)

    q = sub.add_parser("queue", help="очередь заданий для агентов-обогатителей")
    q.add_argument("--batch", type=int, default=20)
    q.set_defaults(func=queue)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
