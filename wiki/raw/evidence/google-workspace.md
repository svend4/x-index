<!-- Выдержки первоисточников для карточки google-workspace. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "google-workspace", "kind": "skill", "cluster": "03-docs-knowledge", "group": "совместное редактирование документов", "name": "google-workspace", "vendor": "уточнить", "state": "enabled", "platform_description": "Правила создания и изменения файлов Google Docs, Sheets, Slides и Drive; вспомогательные скрипты", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: google-workspace
description: "Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file. Use this skill whenever the user wants to create or change a Google Doc, Sheet or Slides file in their Google Drive. Triggers include: a request that names Google Docs, Sheets, Slides or Drive and asks to make, edit, format, copy or rename a file; a docs.google.com link with a request to change that file, even a one-line fix or suggested edits; and any follow-up change to a Google file from earlier in the chat, even \"change it\" or \"add a tab\". Includes helper scripts for document positions, cell ranges and slide layout. However, if the user asks for a doc, deck or spreadsheet without naming Google, or gives a Google file only as source material for something new, use Claude's own output type instead. Do NOT use for read-only questions about a Google file, or for Word, Excel, PowerPoint or PDF files."
---

# Google Docs, Sheets, and Slides

The Google connectors are thin wrappers over Google's raw APIs, with almost no guidance of their own. This skill supplies that guidance: which connector does what, the rules that keep edits in the user's file, and, in one reference file per app, how each API really behaves. Most of the app-specific rules in the references were tested against Google's Docs, Sheets and Slides APIs; the rest were seen through the connectors, and a few have not been checked yet.

## Read the reference before you touch the file

| Working on | Read first | Why it matters |
|---|---|---|
| A Google Doc | `references/docs.md` | Docs edits address UTF-16 positions that shift after every insert and go stale after every write. Tabs and pending suggestions change the positions too. |
| A Google Sheet | `references/sheets.md` | Both write tools parse input like the Sheets UI, so text can silently become numbers or dates. Formatting needs numeric sheet IDs, 0-based ranges, and field masks without parentheses. |
| A Google Slides deck | `references/slides.md` | Positions are in EMU, an element's real size is its size times its scale, and an unmasked read can exceed 150 KB for three slides. Slides never shrinks text to fit. |

Read the reference for every app the task touches before the first edit. Embedding a Sheets chart in a deck means reading both. The references are short, and skipping one is how edits land in the wrong place.

## 1. Check the connectors before you start

| Connector | What it can do |
|---|---|
| Google Drive | Create files, upload and convert content, rename, read a file as text, export (PDF and other formats), search, trash |
| Google Docs | Read a doc's full structure and edit it in place, directly or as suggestions |
| Google Sheets | Read values and structure, write values and formulas, format, add tabs and charts |
| Google Slides | Read a deck, add and edit slides, shapes, text, tables, and linked charts |

Drive can create all three file types. It can't edit a file after that. Without the matching editor connector, every change means a new file and a new link, and the user loses the link they already have.

1. Check which Google tools are available in this conversation. On surfaces where tools are deferred, search for and load the tools you need first, such as "google sheets update". Tool names differ by surface, so use the names your surface lists. If a search returns nothing, list all available tools before deciding the connector is missing, because the tool may exist under a different name.
2. If the editor tools are missing, tell the user. When you can list the conversation's connectors, say which case it is: a connector that is set up but turned off in this chat (ask them to turn it on in the chat's connector settings, then continue), or one that isn't connected at all (tell them which connector to add and what it enables).
3. With an editor connector missing, a request to create a new file continues with Drive. A change to an existing file stops and asks. See the missing-connector rule in section 2.
4. If the user asks only for a new file, create it with Drive. If the editor connector is off, add one line saying edits will need it.

Example: "I can create the sheet now. If you want changes later, turn on the Google Sheets connector in this chat first. Then I can edit this file, and the link will stay the same."

## 2. Rules for every file

- **A change goes in the same file.** "Change", "update", "fix", "add", and "switch it to" all mean the user wants the same file and link. Do not recreate the file to skip an edit.
````
