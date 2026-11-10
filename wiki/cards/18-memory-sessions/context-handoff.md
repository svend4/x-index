---
id: "context-handoff"
title: "context-handoff"
kind: "plugin"
vendor: "уточнить"
cluster: "18-memory-sessions"
summary: "Плагин context-handoff версии 0.1.2 с двумя скиллами (handoff, handoff-writing): сводка сессии для переноса контекста из Claude Code в чат Claude Desktop или Claude.ai."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: []
source_urls: ["raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
group: "handoff и чекпоинты"
tags: ["сводка сессии", "перенос контекста", "handoff", "handoff-writing", "Claude Desktop"]
---
# context-handoff

## Суть
Плагин context-handoff версии 0.1.2, в сессии включён; содержит два скилла: handoff и handoff-writing [1][2].
По описанию автора плагин формирует сводку сессии с решениями, отвергнутыми вариантами и открытыми блокерами, чтобы перенести контекст из Claude Code в чат Claude Desktop или Claude.ai [2].

## Для чего
- По описанию автора: перенос контекста из Claude Code в чат Claude Desktop или Claude.ai без повторного объяснения проекта [2].
- нет данных о целевой аудитории сверх этого описания.

## Возможности
- Сводка сессии с решениями, отвергнутыми альтернативами и открытыми блокерами [2].
- Два скилла: handoff и handoff-writing [1].
- нет данных о формате сводки, её объёме и способе запуска скиллов.

## Чем выделяется
- Мнение: узкая задача, только перенос контекста в другой чат, отличает плагин от многоэтапных процессов передачи работы; это мнение по описанию [2].

## Ограничения и риски
- Сводка переносится в чат Claude Desktop или Claude.ai, то есть её содержимое попадает в другой чат [2].
- Версия манифеста 0.1.2; по выдержкам зрелость не оценена [2].
- В сессии плагин включён [1].
- нет данных о том, что помимо решений, отвергнутых вариантов и блокеров попадает в сводку.
- нет данных о цене, модели оплаты, способе подключения, месте обработки данных и классе данных.

## Когда не подходит
- Мнение: если нужен многоэтапный процесс с планом и отдельной проверкой, одной сводки недостаточно; см. [[agent-handoff]].
- Мнение: если контекст нужно передать внутри того же чата, инструмент не нужен.
- Мнение: если сводка может содержать данные, которые нельзя переносить в другой чат, её переносить не стоит; состав сводки в выдержке описан только категориями [2].

## Альтернативы
- [[agent-handoff]] — многоэтапный процесс plan, execute, verify по описанию автора.
- [[chat-migration-assistant]] — перенос работы в новый чат через пакет checkpoint-файлов.
- [[chat-migration-pro]] — расширенный вариант переноса с автоматизацией и Git-интеграцией по описанию.

## Источники
1. инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления), снимок 2026-11-10 — raw://session/2026-11-10/inventory.json
2. манифест плагина (начало файла), снимок 2026-11-10 — raw://evidence/context-handoff.md

## Заявлено автором
> Generates a curated session handoff summary (decisions, rejected alternatives, open blockers) so you can bring context from Claude Code into a Claude Desktop/Claude.ai chat without re-explaining your project from scratch.
