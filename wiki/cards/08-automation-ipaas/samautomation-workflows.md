---
id: "samautomation-workflows"
title: "samautomation-workflows"
kind: "plugin"
vendor: "Samautomation"
cluster: "08-automation-ipaas"
group: "сценарии (make, zapier, n8n)"
summary: "Плагин Samautomation версии 1.0.2 с одним скиллом n8n-workflow-check: сборка, ремонт и проверка импортируемого JSON-workflow для n8n."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "none"
hosting: "unknown"
languages: []
source_urls: ["https://samautomation.work", "raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["n8n", "workflow", "JSON", "n8n-workflow-check", "автоматизация"]
---
# samautomation-workflows

## Суть

Плагин в инвентаре относится к группе «сценарии (make, zapier, n8n)» [1] и содержит один скилл n8n-workflow-check [1]. По описанию автора, плагин собирает или исправляет импортируемый JSON-workflow для n8n и проверяет его структуру [2]. Версия манифеста — 1.0.2 [2].

## Для чего

- Сборка и исправление импортируемого JSON-workflow для n8n [2].
- Проверка событий в изоляции: допустимых, повторных и недопустимых, по описанию автора [2].
- Группа в инвентаре сессии: «сценарии (make, zapier, n8n)» [1].

## Возможности

- Скилл n8n-workflow-check в составе плагина [1].
- Проверочный скрипт работает только на чтение и не активирует workflow, по заявлению автора [2].
- Ручная тестовая фикстура, протестированная на n8n 2.23.4 [2].
нет данных: подробный перечень действий скилла в выдержках не приведён [1][2].

## Чем выделяется

- Мнение: узкая специализация на n8n и отдельная проверка JSON отличают плагин от общих инструментов оркестрации [2].
- Мнение: заявление, что проверка идёт без сетевых запросов и учётной записи, упрощает безопасное тестирование; это слова автора, не проверенный факт [2].

## Ограничения и риски

- По заявлению автора, проверочный скрипт не подключается к учётной записи, не делает сетевых запросов и не активирует workflow [2].
- Заявление относится к проверочному скрипту; о том, какие файлы меняет сборка и ремонт JSON, в описании ничего не сказано [2].
- Лицензия MIT, как указано в манифесте [2].
нет данных: класс данных, цена, поддержка и зрелость проекта в выдержках не указаны.

## Когда не подходит

- Когда нужны сценарии Make или Zapier, а не n8n: скилл рассчитан на JSON n8n [1][2].
- Мнение: если workflow нужно запускать и проверять в живой системе, проверочный скрипт этого не делает; по заявлению он не активирует workflow [2].

## Альтернативы

- [[workflow-automation]] — общий скилл оркестрации задач (цепочки, условия, обработка ошибок), не привязанный к n8n.
- [[make-com]] — коннектор сценариев Make из той же группы; другая платформа.
- [[zapier]] — коннектор Zapier из той же группы; другая платформа.

## Источники
1. инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления) — raw://session/2026-11-10/inventory.json
2. манифест плагина (начало файла), адрес автора из манифеста — https://samautomation.work

## Заявлено автором

> Build or repair importable n8n workflow JSON, check its structure and test valid, duplicate and invalid events in isolation. Includes a read-only checker and a manual fixture tested on n8n 2.23.4. No account connection, network requests or activation by the bundled checker.
