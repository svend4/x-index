<!-- Выдержки первоисточников для карточки pptx. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "pptx", "kind": "skill", "cluster": "24-office-documents", "group": "презентации PowerPoint", "name": "pptx", "vendor": "уточнить", "state": "enabled", "platform_description": "Создание, чтение и правка .pptx: слайды, шаблоны, заметки докладчика", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: pptx
description: "Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations as PowerPoint (.pptx) files; reading, parsing, or extracting text from any .pptx or .potx file (even if the extracted content will be used elsewhere, like in an email, summary, or creating a different type of slide deck); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates (.potx), layouts, speaker notes, or comments. Trigger whenever the user asks for a PowerPoint or .pptx file, or references a .pptx or .potx filename, regardless of what they plan to do with the content afterward. However, when the user asks for a deck, slides, a slide deck, or a presentation without naming a file format, default to using a dedicated slide-deck artifact type or a separate slides skill if this session offers one; otherwise, use this skill."
license: Complete terms in LICENSE.txt
---

# PPTX creation, editing, and analysis

If this session offers a dedicated slide-deck artifact type or a separate slides skill, and the user has neither asked for a PowerPoint/.pptx file nor supplied a .pptx/.potx file to edit, fill in, or convert, build the deck with that type or skill instead. A .pptx/.potx file given only as source material or as an example for a new deck ("make another deck like this one") does not count as supplied: read it with this skill, then build the new deck with that type or skill. This skill remains the right tool for producing .pptx files and for reading, editing, templating, or converting existing .pptx/.potx files.

A `.pptx` is a ZIP archive of XML files. Choose your approach by task:

| Task | Approach |
|---|---|
| **Create** a new deck | Write a `pptxgenjs` script — see gotchas below — and build it as a [structured deck](#structured-decks) unless the user asks for a quick throwaway |
| **Edit** an existing deck, or build from a template | unzip → edit `ppt/slides/slideN.xml` → zip |
| **Read** content | `python scripts/slide_text.py deck.pptx` (one block per slide under `<!-- Slide number: N -->` markers); visual grid: `python scripts/thumbnail.py deck.pptx` |

## Scripts

Paths are relative to this skill's directory. Everything else is plain Python, `node`, or shell.

| Script | What it does |
|---|---|
| `scripts/slide_text.py deck.pptx` | Every slide's title, text, tables, chart data (scatter and bubble charts: series names only), picture alt text and speaker notes, as markdown. Reads `.potx` too |
| `scripts/thumbnail.py deck.pptx [prefix]` | Labeled grid of every slide, for picking template layouts. `.pptx` only. Pass `prefix` — it defaults to `thumbnails`, which overwrites the grids of any other deck done in the same directory |
| `scripts/add_slide.py unpacked/ slide2.xml [--after slideN.xml]` | Duplicate a slide (or a `slideLayoutN.xml`) with all the package bookkeeping. Also takes a `.pptx` directly with `-o out.pptx` |
| `scripts/clean.py unpacked/` | Delete slides, media, and rels no longer referenced. Run **after** `<p:sldIdLst>` is final |
| `scripts/apply_theme.js` | Node module: `const { applyTheme } = require("<this skill's directory>/scripts/apply_theme.js")`. `await applyTheme("deck.pptx", THEME)` after `pres.writeFile()` writes `THEME`'s colors and name (escaped for XML) into the deck's theme, for [structured decks](#structured-decks). Also a CLI: `node scripts/apply_theme.js deck.pptx theme.json` |
| `scripts/office/validate.py deck.pptx [--original src.pptx]` | Schema, relationship, content-type, chart and slide checks; each failure names its fix. Pass `--original` for any template-derived deck — it baselines the schema checks against the template, so the template's own XSD errors don't read as yours |
| `scripts/office/soffice.py --headless --convert-to pdf deck.pptx` | LibreOffice wrapper — bare `soffice` hangs in this sandbox |

## Creating with pptxgenjs — gotchas

`pptxgenjs` is preinstalled — do not run `npm install` first; write the script and `require('pptxgenjs')` directly. Only if that require fails: `npm install pptxgenjs`. The model knows the API; these are the footguns:

- **Set `pres.layout` before adding slides.** The default canvas is `LAYOUT_16x9` = **10" × 5.625"**, not 13.3" wide. Coordinates past the edge are written, not clamped — the shape just isn't on the slide. (`LAYOUT_WIDE` is 13.3" × 7.5".)
- **Hex colors: never `#`, never 8 digits.** `color: "FF0000"`. Both `"#FF0000"` and alpha baked into the hex (`"00000020"`) **corrupt the file**. For translucency: `transparency: 0-100` on fills and images, `opacity: 0.0-1.0` on shadows — each is silently ignored on the other.
- **pptxgenjs mutates option objects in place** (converts values to EMU on first use). Never share one `shadow`/options object across two `add*` calls — build a fresh object each time.
- **Shadow `offset` must be ≥ 0** — a negative offset corrupts the file. To cast a shadow upward, use `angle: 270` with a positive offset.
````
