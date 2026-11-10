---
id: "vault-anything"
title: "Vault Anything"
kind: "plugin"
vendor: "уточнить"
cluster: "03-docs-knowledge"
group: "заметки и wiki"
summary: "Плагин, который строит Obsidian-вики из исходного кода и файлов raw/ через скиллы vault и vault-update и агенты file-analyzer и page-writer."
status: "draft"
data_class: "B"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: []
source_urls: ["https://github.com/burakolgun/vault-anything", "https://burakolgun.github.io/vault-anything/", "raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Obsidian", "вики", "wiki", "vault-anything", "vault-update", "llm-context", "knowledge-vault", "codebase-analysis", "документация"]
---

# Vault Anything

## Суть
- Плагин генерирует Obsidian-вики из исходного кода и файлов каталога raw/ [1].
- По манифесту это генератор LLM-вики в стиле Karpathy из исходного кода и статических документов; лицензия MIT [2].

## Для чего
- Создание Obsidian-вики из исходного кода проекта [1][2].
- Создание вики из статических документов в каталоге raw/ [1].
- нет данных о целевой аудитории и типичных сценариях сверх описания.
- Группа инвентаря: «заметки и wiki» [1].

## Возможности
- Скиллы vault и vault-update [1].
- Агенты file-analyzer и page-writer [1].
- нет данных о порядке работы скиллов, аргументах запуска и проверке качества: в выдержках только состав [1][2].

## Чем выделяется
- Мнение: плагин работает с исходным кодом и файлами raw/ в одном конвейере, поэтому он ближе к документации проекта, чем к каталогу инструментов [1][2].
- Мнение: открытая лицензия MIT [2] позволяет проверить код плагина до подключения.

## Ограничения и риски
- Агенты file-analyzer и page-writer работают с исходным кодом и файлами raw/ [1].
- Класс данных B выведен по [1]: агенты обрабатывают содержимое файлов; куда оно передаётся, в выдержках нет данных [1].
- Выдержки не описывают, какие файлы попадают в пакеты для агентов [1].
- В инвентаре поставщик не определён, в манифесте указан автор [1][2].
- Версия манифеста 0.1.0 [2]; зрелость и история изменений по выдержкам не оценены.
- нет данных о цене, способе входа и месте обработки данных.

## Когда не подходит
- Мнение: большие каталоги без исходного кода и с нестабильной структурой: плагин рассчитан на код и файлы raw/ [1].
- Мнение: проекты, где содержимое файлов нельзя передавать агентам: класс данных B [1].

## Альтернативы
- [[obsidian-notes]] — работа с папкой Markdown как хранилищем Obsidian без генерации вики.
- [[documentation-generator]] — генерация API-документации, README и changelog, если нужна документация, а не вики.

## Источники
1. инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления) — raw://session/2026-11-10/inventory.json
2. манифест плагина (начало файла) — https://github.com/burakolgun/vault-anything

## Заявлено автором
> Скиллы vault и vault-update: генерация Obsidian-вики из исходного кода и файлов raw/; агенты file-analyzer и page-writer

Поле platform_description записи инвентаря [1].

Описание в манифесте [2]:
> Generate Karpathy-style Obsidian LLM wikis from source code and static documents
