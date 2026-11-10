---
id: "claude-code-bundled"
title: "Встроенные скиллы Claude Code"
kind: "plugin"
vendor: "уточнить"
cluster: "06-dev-code"
group: "IDE и агенты для кода"
summary: "Набор из 12 встроенных скиллов Claude Code для работы с кодом, включённых в сессии 2026-11-10, например code-review и security-review."
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
tags: ["Claude Code", "встроенные скиллы", "скиллы", "code-review", "security-review", "update-config", "plugin-authoring"]
---

# Встроенные скиллы Claude Code

## Суть
- Пакет из 12 скиллов, встроенных в Claude Code, включён в сессии 2026-11-10 [1].
- Состав пакета: `update-config`, `keybindings-help`, `code-review`, `simplify`, `fewer-permission-prompts`, `loop`, `claude-api`, `workflow-authoring`, `run`, `plugin-authoring`, `init`, `security-review` [1].

## Для чего
- Работа с кодом и агентами: так группа записи инвентаря называет набор [1].
- нет данных о задачах каждого скилла: в выдержках только имена [1].

## Возможности
- По названиям часть скиллов относится к настройкам: `update-config`, `keybindings-help`, `fewer-permission-prompts` [1].
- По названиям часть скиллов относится к коду: `code-review`, `security-review`, `simplify` [1].
- По названиям часть скиллов относится к созданию расширений и инициализации: `plugin-authoring`, `workflow-authoring`, `init` [1].
- нет данных о действиях каждого скилла, их лимитах и правах доступа.

## Чем выделяется
- Мнение: набор уже включён в сессии, поэтому отдельная установка скиллов не нужна [1].

## Ограничения и риски
- Класс данных не определён: описаний отдельных скиллов в выдержках нет [1].
- Скилл `update-config` по названию меняет настройки; подтверждения в выдержках нет [1].
- Поставщик в инвентаре не определён [1].
- нет данных о цене, способе входа и месте обработки данных.

## Когда не подходит
- Мнение: если нельзя менять настройки Claude Code, набор со скиллом `update-config` не подходит [1].
- Мнение: задачи вне разработки кода набор не закрывает, судя по группе записи инвентаря: IDE и агенты для кода [1].

## Альтернативы
- [[skill-creator]] — создание и улучшение собственных скиллов, если встроенных недостаточно.

## Источники
1. инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления) — raw://session/2026-11-10/inventory.json

## Заявлено автором
> 12 скиллов: update-config, keybindings-help, code-review, simplify, fewer-permission-prompts, loop, claude-api, workflow-authoring, run, plugin-authoring, init, security-review
