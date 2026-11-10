---
id: "github-mcp"
title: "GitHub (MCP-инструменты сессии)"
kind: "mcp-server"
vendor: "GitHub"
cluster: "06-dev-code"
group: "репозитории и ревью"
summary: "Инструменты GitHub в сессии: около 60 функций для pull request, issues, файлов, веток, Actions и релизов. Доступ ограничен репозиторием, подключённым к сессии."
status: "draft"
data_class: "C"
price: "freemium"
auth: "oauth"
hosting: "US"
hosted: true
languages: ["en"]
source_urls: ["https://github.com", "raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["GitHub", "pull request", "issues", "код-ревью", "Actions", "ветки", "релизы"]
curator_hint: "test"
---

# GitHub (MCP-инструменты сессии)

## Суть
Набор инструментов для работы с GitHub через MCP: pull request, issues, файлы и ветки, Actions, релизы, отзывы на ревью и секретное сканирование. В сессии доступно около 60 инструментов. Доступ ограничен репозиторием, который подключён к сессии.

## Для чего
- Просмотр и ревью pull request, ответы на комментарии, разрешение обсуждений.
- Создание веток, изменение файлов, pull request по явной команде.
- Просмотр Actions, логов сборок, релизов и тегов.

## Возможности
По списку инструментов сессии (префикс `mcp__github__`):
- **Pull request:** `pull_request_read`, `list_pull_requests`, `create_pull_request`, `update_pull_request`, `merge_pull_request`, `pull_request_review_write`, `add_comment_to_pending_review`, `resolve_review_thread`, `request_copilot_review`, `enable_pr_auto_merge`, `disable_pr_auto_merge`.
- **Issues:** `issue_read`, `issue_write`, `list_issues`, `add_issue_comment`, `sub_issue_write`, `list_issue_types`.
- **Файлы и ветки:** `get_file_contents`, `create_or_update_file`, `delete_file`, `push_files`, `create_branch`, `list_branches`, `list_commits`, `get_commit`.
- **Actions и релизы:** `actions_list`, `actions_get`, `actions_run_trigger`, `get_job_logs`, `get_check_run`, `list_releases`, `get_latest_release`, `get_release_by_tag`.
- **Безопасность:** `run_secret_scanning`.

## Чем выделяется
- Мнение: инструменты разделены на чтение (`*_read`, `list_*`, `get_*`) и запись (`*_write`, `create_*`, `update_*`). Это удобно для правила «сначала чтение, потом запись».

## Ограничения и риски
- Инструменты записи меняют репозиторий. `merge_pull_request`, `delete_file`, `push_files` требуют подтверждения владельца.
- В системных инструкциях сессии поиск через `search_*` недоступен, поэтому поиск по коду и issues делается через `gh api search/...`.
- По правилам сессии не использовать `create_repository` и `list_notifications`, потому что они выходят за пределы разрешённого репозитория.

## Когда не подходит
- Работа с репозиториями вне списка разрешённых в сессии без отдельного подключения.
- Массовые изменения без ветки и ревью.

## Альтернативы
- Локальный `git` и `gh` в терминале сессии — для команд, которые не нужны через MCP.
- [[claude-code-bundled]] — встроенные скиллы Claude Code: code-review (ревью изменений без обращения к GitHub) и security-review (проверка безопасности).

## Источники
1. Список инструментов сессии (префикс `mcp__github__`), 2026-11-10.
2. Системные инструкции сессии: область доступа GitHub и правила поиска, 2026-11-10.
3. Сайт поставщика: https://github.com (тарифы и лимиты проверить при сверке).

## Заявлено автором
> Нет описания в каталоге: инструменты загружены как часть сессии.
