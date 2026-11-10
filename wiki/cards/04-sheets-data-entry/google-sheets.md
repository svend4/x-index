---
id: "google-sheets"
title: "Google Sheets"
kind: "connector"
vendor: "Google"
cluster: "04-sheets-data-entry"
group: "таблицы"
summary: "Коннектор для чтения и изменения таблиц Google Sheets: значения, формулы, строки и листы; в сессии 2026-11-10 подключён."
status: "draft"
data_class: "C"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: []
source_urls: ["raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Google Sheets", "Google Таблицы", "таблицы", "spreadsheets", "Tabellen", "формулы", "google-sheets"]
---

# Google Sheets

## Суть
- Коннектор читает, анализирует и обновляет таблицы Google Sheets [1].
- В сессии 2026-11-10 коннектор подключён, его инструменты загружены [1][2].
- Системная инструкция сервера: это MCP-сервер, который предоставляет инструменты для работы с Google Sheets [3].

## Для чего
- Чтение и анализ таблиц [1].
- Добавление строк и изменение значений в таблицах [2].
- нет данных о целевой аудитории и сценариях сверх описания.

## Возможности
- Чтение таблиц и значений: `get_spreadsheet`, `get_values` [2].
- Запись значений: `append_values`, `update_values`, `batch_clear_values` [2].
- Структура, формулы и свойства таблицы: `insert_dimension`, `update_formulas`, `update_spreadsheet` [2].
- Копирование листа в другую таблицу: `copy_sheet_to_another_spreadsheet` [2].
- нет данных о лимитах API и параметрах инструментов.

## Чем выделяется
- Мнение: в одном коннекторе есть и чтение, и запись значений, и изменение структуры таблицы [2].

## Ограничения и риски
- Класс данных C: инструменты меняют данные владельца, включая значения и структуру таблицы: `update_values`, `insert_dimension`, `update_formulas` [2].
- `batch_clear_values` очищает значения, поэтому ошибочный вызов может стереть данные таблицы [2].
- нет данных о цене, способе входа и месте обработки данных.

## Когда не подходит
- Мнение: для больших объёмов данных и аналитики лучше подходит хранилище данных, см. [[bigquery]].
- Мнение: записи, которые нельзя менять задним числом, например журналы аудита: инструменты `update_values` и `batch_clear_values` позволяют менять значения [2].

## Альтернативы
- [[google-drive]] — поиск и чтение файлов Google Drive, если нужна работа с файлом целиком, а не с ячейками.
- [[xlsx]] — файлы .xlsx, .csv и .tsv, если таблица хранится в файле, а не в Google Таблицах.

## Источники
1. инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления) — raw://session/2026-11-10/inventory.json
2. список инструментов, загруженных в сессию — raw://session/2026-11-10/tools-by-server.txt
3. системные инструкции MCP-сервера (сессия 2026-11-10) — raw://session/2026-11-10/evidence/mcp-instructions.txt

## Заявлено автором
> Read, analyze, and update your spreadsheets
> This is an MCP server which provides tools to interact with Google Sheets.
