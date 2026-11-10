<!-- Выдержки первоисточников для карточки google-calendar. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "google-calendar", "kind": "connector", "cluster": "02-calendar-tasks", "group": "календарь и встречи", "name": "Google Calendar", "vendor": "Google", "state": "connected", "platform_description": "Manage your schedule and coordinate meetings effortlessly", "source": "ListConnectors"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[google-calendar] инструменты (префикс mcp__Google_Calendar__): list_calendars, list_events, get_event, search_events, create_event, update_event, delete_event, respond_to_event, suggest_time
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### Google Calendar
This is an MCP server provided by Google Calendar API. The server provides tools for developers to build LLM applications on top of Calendar.
````
