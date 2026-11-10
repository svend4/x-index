<!-- Выдержки первоисточников для карточки tinyfish. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "tinyfish", "kind": "connector", "cluster": "09-browser-web-data", "group": "облачные браузеры", "name": "TinyFish", "vendor": "TinyFish", "state": "connected", "platform_description": "Browser automation, web scraping, web search and fetch via a cloud browser agent: automate websites, log in to portals, submit forms, scrape social media, listings, prices, reviews, monitor changes.", "source": "ListConnectors"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[tinyfish] инструменты (префикс mcp__TinyFish__): batch_cancel, batch_status, cancel_dataset_run, cancel_deep_research, cancel_monitor, cancel_run, close_browser_session, create_browser_session, create_dataset, create_monitor, delete_dataset, fetch_content, get_dataset, get_dataset_rows, get_deep_research, get_monitor, get_run, get_search_usage, get_wallet, guide_next_step, list_browser_sessions, list_datasets, list_deep_research, list_fetch_usage, list_monitors, list_runs, pause_monitor, plan_dataset, populate_dataset, resume_monitor, run_monitor, run_web_automation, run_web_automation_async, search, start_deep_research, top_up_wallet, update_monitor, wait_for_run
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### TinyFish
TinyFish provides tools for user-requested web search, page-content extraction, research, monitoring, and browser automation. run_web_automation_async starts a background run when the user explicitly requests background execution. An automation call that times out may still be running; its status can be checked before retrying. Datasets are slow, billed per row, and opt-in: use create_dataset only when the user asks for a table or list of many entities with the same fields, never for a single fact. Users can start TinyFish prompts from the client prompt menu: the + menu in claude.ai, or / in Claude Code. This TinyFish account includes web automation (up to 2 concurrent).
````
