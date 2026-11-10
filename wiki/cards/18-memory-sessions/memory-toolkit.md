---
id: "memory-toolkit"
title: "memory-toolkit"
kind: "plugin"
vendor: "уточнить"
cluster: "18-memory-sessions"
summary: "Плагин ведения памяти сессий для разработчиков: память проекта в Markdown, workstreams, передача контекста и автосохранение; 11 скиллов."
status: "draft"
data_class: "C"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: ["en"]
source_urls: ["raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
group: "заметки о сессиях"
tags: ["память проекта", "project memory", "workstreams", "handoff", "заметки", "решения", "сессии"]
---
# memory-toolkit

## Суть
- Плагин ведёт память сессий для разработчиков: структурированные Markdown-заметки, workstreams, передача контекста (handoff) и автосохранение через хуки [2].
- Описание платформы: «11 скиллов: память проекта, workstreams, заметки, решения, сессии (start, end, continue, restore, insights), park, reflect, task-template» [1].

## Для чего
- Ведение памяти проекта и решений между сессиями [1][2].
- Продолжение работы по workstream и передача контекста в следующую сессию (handoff) [2].
- Для разработчиков [2].

## Возможности
- Команды в манифесте: `session-start`, `session-continue`, `session-end`, `memory`, `memory-setup`, `reflect`, `docs-reflect`, `park`, `session-restore`, `session-insights` [2].
- Большинству команд разрешены `Bash`, `Read`, `Write`, `Glob` и `Grep`; `session-restore` и `session-insights` работают без `Write` [2].
- Структурированная память в Markdown, workstreams и решения [1][2].
- Автосохранение через хуки (auto-save hooks) [2].

## Чем выделяется
- Заявлено автором: плагин работает без векторной базы и внешних зависимостей: «No vector DB, no external dependencies.» [2]
- Мнение: память в обычных Markdown-файлах проще проверить вручную, чем содержимое векторной базы.

## Ограничения и риски
- Класс C основан на записи файлов (`Write`) и хуках автосохранения [2].
- Команды, которым разрешён `Bash`, могут запускать команды оболочки [2].
- Какие события запускают хуки автосохранения, в выдержках не описано: нет данных [2].
- Версия 1.9.13, лицензия MIT [2].
- Число скиллов расходится: в описании платформы 11 [1], в манифесте перечислено 10 команд [2].
- нет данных: цена, лимиты и место хранения памяти.

## Когда не подходит
- Мнение: если нужны поиск по смыслу или векторная база, плагин не подходит: автор заявляет, что её нет [2].
- Мнение: для личных заметок вне проектной работы плагин избыточен: описание адресовано разработчикам [2].

## Альтернативы
- [[import-memory]] — импорт экспорта памяти из другого ассистента, а не ведение заметок сессий.
- [[context-handoff]] — сводка сессии для переноса контекста из Claude Code в чат Claude Desktop или Claude.ai.
- [[obsidian-notes]] — хранилище заметок Obsidian из папки Markdown.

## Источники
1. Инвентарь сессии: запись позиции (список скиллов сессии), снимок 2026-11-10 — raw://session/2026-11-10/inventory.json
2. Манифест плагина (начало файла), снимок 2026-11-10 — адреса нет (локальный файл плагина).
Сверка с первоисточником не проводилась (verified_on: null).

## Заявлено автором
> «Session memory lifecycle for developers — structured markdown memory, workstreams, handoff, auto-save hooks. No vector DB, no external dependencies.» [2]
> «11 скиллов: память проекта, workstreams, заметки, решения, сессии (start, end, continue, restore, insights), park, reflect, task-template» [1]
