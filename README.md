# x-index — Вики по инструментам экосистемы Claude и MCP-серверам

Вики и индексный инструмент по коннекторам, скиллам, плагинам, MCP-серверам и приложениям автоматизации: знания хранятся в Markdown-карточках с YAML-заголовком, а поиск работает поверх SQLite FTS5.

> **Состояние ветки `main`:** в основной ветке `main` на данный момент содержатся только `README.md` и `LICENSE`. Полная реализация вики, документации, карточек и CLI-инструментов находится в неслитой ветке [`claude/clever-bohr-5h86es`](../../tree/claude/clever-bohr-5h86es).

## Возможности (по ветке `claude/clever-bohr-5h86es`)

- **Двухуровневая модель данных**:
  1. **Уровень 1 (`wiki/cards/<кластер>/<id>.md`)** — карточки-README с фактами, классами данных (`A/B/C/unknown`), источниками и цитатами по схеме `wiki/SCHEMA.md`.
  2. **Уровень 2 (`wiki/.index/wiki.sqlite`, таблица `entries`)** — строки каталога для записей официального реестра MCP без создания отдельных файлов.
- **Таксономия из 26 кластеров (`wiki/taxonomy.json`, `wiki/TAXONOMY.md`)** — от мета-инструментов и коммуникаций до права Германии/ЕС, медицины, бухгалтерии и комплаенса ИИ.
- **CLI-утилита `tools/wiki.py`** (только стандартная библиотека Python 3.10+, без сторонних пакетов):
  - `harvest-mcp` — выгрузка публичного реестра MCP (`https://registry.modelcontextprotocol.io/v0/servers`) в сжатый снимок `servers.ndjson.gz`;
  - `build` — генерация заготовок карточек, индексов `wiki/INDEX.md`, `wiki/clusters/`, `wiki/catalog.json`;
  - `lint` — проверка карточек по `wiki/SCHEMA.md` и поиск случайных токенов/секретов;
  - `index` — пересборка полнотекстового индекса `wiki/.index/wiki.sqlite` (SQLite FTS5);
  - `ask` — поиск по карточкам и каталогу с фильтрами (`--cluster`, `--kind`, `--status`, `--data-class`, `--price`, `--json`);
  - `queue` — формирование очереди заданий для обогащения (`wiki/queue/enrich-queue.jsonl`);
  - `evidence` / `verify` — сбор выдержек первоисточников и сверка ссылок `[n]` и цитат;
  - `eval` — замер качества поиска (`hit@k`, `recall@k`, `MRR`) по эталонному набору вопросов (`wiki/eval/`).
- **Рабочие процессы агентов (`tools/workflows/`)**: скрипты `enrich-inventory.js`, `repair-inventory.js`, `review-inventory-r1.js`, `review-inventory-r2.js`.

## Структура проекта

### Ветка `main`

- `LICENSE` — текст лицензии GNU Affero General Public License v3.
- `README.md` — описание проекта.

### Ветка `claude/clever-bohr-5h86es`

```text
├── .gitignore
├── LICENSE
├── README.md                  # Основная документация ветки
├── docs/
│   ├── ANALYSIS.md            # Разбор источников, вики, RAG и рекомендации
│   └── PIPELINE.md            # Конвейер стадий сборки, проверки и поиска
├── tools/
│   ├── wiki.py                # Единый CLI-инструмент вики (Python 3.10+ stdlib)
│   └── workflows/             # JS-скрипты обогащения и состязательных проверок
│       ├── enrich-inventory.js
│       ├── repair-inventory.js
│       ├── review-inventory-r1.js
│       └── review-inventory-r2.js
└── wiki/
    ├── SCHEMA.md              # Схема карточки, классы данных и статусы
    ├── taxonomy.json          # Таксономия кластеров и групп
    ├── TAXONOMY.md            # Оглавление таксономии
    ├── INDEX.md               # Сводное оглавление вики
    ├── catalog.json           # Машиночитаемый каталог карточек
    ├── log.md                 # Журнал изменений
    ├── cards/                 # Карточки инструментов по кластерам
    ├── clusters/              # Страницы кластеров
    ├── eval/                  # Вопросы и отчёты замера поиска
    ├── queue/                 # Очередь и промпт обогащения
    └── raw/                   # Снимки реестра MCP и инвентаря сессии
```

## Состояние данных и проверенные команды (ветка `claude/clever-bohr-5h86es`)

- **Карточки и реестр (на 2026-11-10):** 1 607 карточек по 26 кластерам (в `wiki/INDEX.md`: 1 584 `stub`, 23 `draft`; в `README.md` и `docs/ANALYSIS.md` ветки отмечены 107 карточек инвентаря сессии, прошедших 5 кругов проверки, и 1 500 заготовок реестра); в снимке официального реестра MCP — 61 245 серверов.
- **Качество поиска:** на 93 вопросах в режиме `fallback` достигнуты `hit@10` 0.80 и `MRR` 0.66.
- **Замечание по качеству одного скилла:** в `README.md` ветки отдельно отмечено, что карточка `wiki/cards/11-law-de-eu/german-legal-deadline-calculator.md` зафиксировала ошибки самого скилла в расчёте сроков.

Запуск (после переключения на ветку `claude/clever-bohr-5h86es`, требуется Python 3.10+):

```bash
git checkout claude/clever-bohr-5h86es
python3 tools/wiki.py build
python3 tools/wiki.py lint
python3 tools/wiki.py index
python3 tools/wiki.py ask "счета XRechnung"
python3 tools/wiki.py queue --batch 20
python3 tools/wiki.py verify wiki/cards/11-law-de-eu/german-legal-deadline-calculator.md
python3 tools/wiki.py eval --mode all
python3 tools/wiki.py harvest-mcp
# При необходимости указать CA-бандл для TLS:
# SSL_CERT_FILE=/путь/к/ca-bundle.crt python3 tools/wiki.py harvest-mcp
```

## Ветки репозитория

- `main` — защищённая основная ветка (`LICENSE`, `README.md`).
- `claude/clever-bohr-5h86es` — неслитая ветка с полной реализацией вики, CLI `tools/wiki.py`, документацией (`docs/ANALYSIS.md`, `docs/PIPELINE.md`) и базой карточек (`wiki/`). Pull Request для этой ветки пока не открывался.

## Лицензия

Проект распространяется под лицензией **GNU Affero General Public License v3** (см. файл `LICENSE`).
