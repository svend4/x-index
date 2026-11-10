---
id: "google-sheets"
title: "Google Sheets (коннектор)"
kind: "connector"
vendor: "Google"
cluster: "04-sheets-data-entry"
group: "таблицы"
summary: "Коннектор Google Sheets: чтение таблиц, добавление строк, обновление значений и формул, копирование листов. Подключён."
status: "draft"
data_class: "C"
price: "free"
auth: "oauth"
hosting: "global"
hosted: true
languages: ["en", "ru", "de"]
source_urls: ["https://workspace.google.com", "raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Google Sheets", "таблицы", "формулы", "записи", "данные"]
curator_hint: "test"
---

# Google Sheets (коннектор)

## Суть
Коннектор даёт Claude доступ к таблицам Google Sheets: чтение, анализ и изменение значений. В сессии 9 инструментов. Коннектор подключён.

## Для чего
- Чтение таблиц и анализ данных в диалоге.
- Добавление записей в журналы, обновление статусов, правка формул.

## Возможности
По списку инструментов сессии: `get_spreadsheet`, `get_values`, `append_values`, `update_values`, `batch_clear_values`, `insert_dimension`, `update_formulas`, `update_spreadsheet`, `copy_sheet_to_another_spreadsheet`.

## Чем выделяется
- Мнение: отдельный `update_formulas` и `insert_dimension` позволяют менять структуру таблицы, а не только значения. Это удобно для журналов, но требует осторожности.

## Ограничения и риски
- `batch_clear_values` и `update_*` могут стереть данные. Нужна копия или подтверждение владельца.
- Таблицы часто содержат персональные данные. Передача модели требует осторожности.

## Когда не подходит
- Большие объёмы данных и аналитика: для них лучше хранилище данных, например BigQuery. В сессии BigQuery не подключился: см. [[bigquery]].
- Записи, которые нельзя менять задним числом (журналы аудита): без отдельной защиты.

## Альтернативы
- [[google-drive]] — поиск таблицы по имени.
- [[xlsx]] — работа с локальными файлами .xlsx и .csv.
- Airtable — базы записей без кода, в сессии не подключён.

## Источники
1. Список инструментов сессии (префикс `mcp__Google_Sheets__`), 2026-11-10.
2. ListConnectors, 2026-11-10: состояние «подключён».
3. Сайт поставщика: https://workspace.google.com (проверить при сверке).

## Заявлено автором
> Read, analyze, and update your spreadsheets
