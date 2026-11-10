---
id: "notion"
title: "Notion (коннектор)"
kind: "connector"
vendor: "Notion"
cluster: "03-docs-knowledge"
group: "заметки и wiki"
summary: "Коннектор Notion: поиск и чтение страниц, создание и изменение страниц и баз данных, комментарии, календарь, память и сессии. Подключён."
status: "draft"
data_class: "C"
price: "freemium"
auth: "oauth"
hosting: "unknown"
hosted: true
languages: ["en", "ru", "de"]
source_urls: ["https://www.notion.so", "raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Notion", "wiki", "базы данных", "заметки", "страницы", "память", "календарь"]
curator_hint: "test"
---

# Notion (коннектор)

## Суть
Коннектор даёт Claude доступ к рабочему пространству Notion: страницам, базам данных, комментариям, календарю и памяти. Список инструментов в сессии большой (несколько десятков). Коннектор подключён.

## Для чего
- Поиск по рабочему пространству и чтение страниц.
- Создание страниц и баз данных, обновление записей, перенос страниц.
- Запрос данных баз, работа с комментариями и представлениями.
- Работа с заметками о встречах и календарём Notion.

## Возможности
По списку инструментов сессии (выборка):
- **Страницы:** `notion-search`, `notion-fetch`, `notion-create-pages`, `notion-update-page`, `notion-move-pages`, `notion-duplicate-page`, `notion-delete-pages`.
- **Базы:** `notion-create-database`, `notion-query-data-sources`, `notion-query-multiple-data-sources`, `notion-update-data-source`, `notion-create-view`, `notion-update-view`.
- **Комментарии:** `notion-create-comment`, `notion-get-comments`, `notion-update-comment`, `notion-delete-comment`.
- **Календарь:** `notion-calendar-*` (список, создание, изменение и отмена событий).
- **Память:** `notion-memory-search`.
- **Сессии:** `notion-spawn-session`, `notion-send-message-to-session`, `notion-wait-session`, `notion-stop-session`.
- **Навыки:** `notion-upload-skill`, `notion-download-skill`, `notion-convert-page-to-skill`.

## Чем выделяется
- Мнение: коннектор объединяет документы, базы, память и сессии в одном месте. Это позволяет использовать Notion как рабочую память команды, а не только как хранилище страниц.

## Ограничения и риски
- Создание и изменение страниц, баз и календаря меняют данные, которые видят другие участники. Нужно подтверждение владельца.
- Инструменты сессий могут запускать другие сессии. Такие действия требуют отдельного согласования.
- Доступ ограничен правами интеграции в рабочем пространстве. Видимость страниц нужно проверить до массовых операций.

## Когда не подходит
- Большие таблицы с аналитикой: для них лучше [[google-sheets]] или хранилище данных.
- Конфиденциальные данные без проверки прав доступа в рабочем пространстве.

## Альтернативы
- [[google-docs]] — документы в Google.
- [[documentation-generator]] — генерация документации в файлах.
- [[enterprise-search]] — поиск по внутренним источникам, включая Notion.

## Источники
1. Список инструментов сессии (префикс `mcp__Notion__`), 2026-11-10.
2. ListConnectors, 2026-11-10: состояние «подключён».
3. Сайт поставщика: https://www.notion.so (тарифы и лимиты проверить при сверке).

## Заявлено автором
> Connect your Notion workspace to search, update, and power workflows across tools
