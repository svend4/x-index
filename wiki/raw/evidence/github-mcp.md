<!-- Выдержки первоисточников для карточки github-mcp. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "github-mcp", "kind": "mcp-server", "cluster": "06-dev-code", "group": "репозитории и ревью", "name": "GitHub (инструменты mcp__github__* в сессии)", "vendor": "GitHub", "state": "available", "platform_description": "Инструменты для pull request, issues, файлов, веток, Actions, релизов, отзывов на ревью", "source": "список инструментов сессии"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[github-mcp] инструменты (префикс mcp__github__): actions_get, actions_list, actions_run_trigger, add_comment_to_pending_review, add_issue_comment, add_reply_to_pull_request_comment, assign_copilot_to_issue, create_branch, create_or_update_file, create_pull_request, create_pull_request_with_copilot, create_repository, delete_file, disable_pr_auto_merge, enable_pr_auto_merge, fork_repository, get_check_run, get_commit, get_copilot_job_status, get_file_contents, get_job_logs, get_label, get_latest_release, get_me, get_release_by_tag, get_tag, get_team_members, get_teams, issue_read, issue_write, list_branches, list_commits, list_issue_fields, list_issue_types, list_issues, list_pull_requests, list_releases, list_repository_collaborators, list_tags, merge_pull_request, pull_request_read, pull_request_review_write, push_files, request_copilot_review, resolve_review_thread, run_secret_scanning, sub_issue_write, unresolve_review_thread, update_issue_comment, update_pull_request, update_pull_request_branch
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### GitHub
The GitHub MCP Server provides tools to interact with GitHub platform.
GitHub access for this session is currently scoped to:
- `svend4/x-index`
Search is the one exception: the GitHub MCP `search_*` tools are not available in this session.
`create_repository` and `list_notifications` take no repository argument and can reach beyond this scope, so do not use them at all in this session.
````
