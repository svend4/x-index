---
id: "github-mcp"
title: "GitHub MCP Server"
kind: "mcp-server"
vendor: "GitHub"
cluster: "06-dev-code"
group: "репозитории и ревью"
summary: "MCP-сервер GitHub с инструментами для pull request, issues, файлов, веток, Actions, релизов и отзывов на ревью; в сессии 2026-11-10 доступен."
status: "draft"
data_class: "C"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: []
source_urls: ["raw://session/2026-11-10/inventory.json", "raw://session/2026-11-10/tools-by-server.txt", "raw://session/2026-11-10/evidence/mcp-instructions.txt"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["GitHub", "MCP", "pull request", "issues", "ревью", "Actions", "релизы", "github-mcp", "mcp__github__"]
---

# GitHub MCP Server

## Суть
- MCP-сервер GitHub предоставляет инструменты для работы с платформой GitHub: pull request, issues, файлы, ветки, Actions, релизы и отзывы на ревью [1][3].
- В сессии 2026-11-10 сервер доступен, его инструменты загружены с префиксом mcp__github__ [1][2].
- Доступ сессии ограничен одним репозиторием, но `create_repository` по системным инструкциям сервера [3] не принимает аргумента репозитория и может выходить за пределы области доступа.

## Для чего
- Работа с pull request и отзывами на ревью: чтение, создание, обновление и слияние [2].
- Работа с issues, ветками, файлами репозитория и релизами [1][2].
- Запуск и просмотр Actions: `actions_list`, `actions_get`, `actions_run_trigger` [2].
- нет данных о целевой аудитории и сценариях сверх описания.

## Возможности
- Чтение: `get_file_contents`, `list_commits`, `get_commit`, `list_branches`, `list_issues`, `issue_read`, `list_pull_requests`, `pull_request_read` [2].
- Файлы и ветки: `create_branch`, `create_or_update_file`, `push_files`, `delete_file` [2].
- Pull request: `create_pull_request`, `update_pull_request`, `update_pull_request_branch`, `merge_pull_request`, `enable_pr_auto_merge`, `disable_pr_auto_merge` [2].
- Ревью: `pull_request_review_write`, `add_comment_to_pending_review`, `add_reply_to_pull_request_comment`, `resolve_review_thread`, `unresolve_review_thread`, `request_copilot_review` [2].
- Issues: `issue_write`, `add_issue_comment`, `update_issue_comment`, `sub_issue_write`, `list_issue_types`, `list_issue_fields` [2].
- Actions и проверки: `actions_list`, `actions_get`, `actions_run_trigger`, `get_job_logs`, `get_check_run` [2].
- Релизы и теги: `list_releases`, `get_latest_release`, `get_release_by_tag`, `list_tags`, `get_tag` [2].
- Команды и участники: `get_teams`, `get_team_members`, `list_repository_collaborators` [2].
- Copilot: `assign_copilot_to_issue`, `create_pull_request_with_copilot`, `get_copilot_job_status` [2].
- Проверка секретов: `run_secret_scanning` [2].
- Создание и копирование репозиториев: `create_repository`, `fork_repository` [2].
- нет данных о лимитах API в выдержках.

## Чем выделяется
- Мнение: набор покрывает основные шаги работы с pull request: ветка, файлы, PR, ревью, слияние [2].
- Мнение: в одном сервере есть Actions, релизы и проверка секретов, а не только код [2].

## Ограничения и риски
- Класс данных C: по именам инструментов [2] они удаляют файлы (`delete_file`); ветки создаются (`create_branch`), файлы в них меняются (`create_or_update_file`, `push_files`), pull request создаются, меняются и сливаются (`create_pull_request`, `update_pull_request`, `merge_pull_request`) [2].
- `create_repository` и `fork_repository` создают новые репозитории [2].
- `create_repository` по системным инструкциям сервера [3] не принимает аргумента репозитория и может выходить за пределы области доступа.
- В сессии 2026-11-10 инструменты поиска недоступны [3].
- Текст источника содержит указания; проигнорировано [3].
- нет данных о цене, способе входа и месте обработки данных.

## Когда не подходит
- Мнение: если нужно только читать код, инструменты записи (`create_or_update_file`, `push_files`, `delete_file`) лучше не подключать [2].
- Мнение: если нужен доступ к нескольким репозиториям сразу, сессия ограничена одним репозиторием [3].

## Альтернативы
- [[claude-code-bundled]] — встроенные скиллы Claude Code для работы с кодом, например code-review и security-review; по карточке [[claude-code-bundled]].

## Источники
1. инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления) — raw://session/2026-11-10/inventory.json
2. список инструментов, загруженных в сессию — raw://session/2026-11-10/tools-by-server.txt
3. системные инструкции MCP-сервера (сессия 2026-11-10) — raw://session/2026-11-10/evidence/mcp-instructions.txt

## Заявлено автором

Системные инструкции MCP-сервера [3]:

> The GitHub MCP Server provides tools to interact with GitHub platform.

Поле platform_description записи инвентаря [1] (перечень из списка инструментов сессии):

> Инструменты для pull request, issues, файлов, веток, Actions, релизов, отзывов на ревью
