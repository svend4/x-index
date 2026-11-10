---
id: "google-slides"
title: "Google Slides (коннектор)"
kind: "connector"
vendor: "Google"
cluster: "05-slides-design"
group: "презентации"
summary: "Коннектор Google Slides: чтение презентаций, страниц и миниатюр, изменение слайдов. Подключён."
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
tags: ["Google Slides", "презентации", "слайды", "миниатюры", "дизайн"]
curator_hint: "test"
---

# Google Slides (коннектор)

## Суть
Коннектор даёт Claude чтение презентаций Google Slides, отдельных страниц и их миниатюр, а также изменение слайдов. В сессии 4 инструмента. Коннектор подключён.

## Для чего
- Разбор чужих презентаций: текст, структура, миниатюры слайдов.
- Правка и добавление слайдов по команде владельца.

## Возможности
По списку инструментов сессии: `read_presentation`, `read_slide_page`, `read_slide_page_thumbnail`, `update_presentation`.

## Чем выделяется
- Мнение: возможность читать миниатюры слайдов позволяет проверять визуальный результат, а не только текст. Это полезно для проверки дизайна.

## Ограничения и риски
- `update_presentation` меняет презентацию, которую могут видеть другие. Нужно подтверждение владельца.
- Презентации могут содержать конфиденциальные данные клиентов.

## Когда не подходит
- Сложная вёрстка и анимации: для них нужны инструменты дизайна или скилл [[pptx]] для файлов .pptx.

## Альтернативы
- [[pptx]] — работа с файлами PowerPoint.
- [[google-drive]] — поиск презентаций по имени.
- [[canva]] — дизайн и шаблоны, в сессии не подключён.

## Источники
1. Список инструментов сессии (префикс `mcp__Google_Slides__`), 2026-11-10.
2. ListConnectors, 2026-11-10: состояние «подключён».
3. Сайт поставщика: https://workspace.google.com (проверить при сверке).

## Заявлено автором
> Read, edit, and add slides to your presentations
