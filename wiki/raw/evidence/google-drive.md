<!-- Выдержки первоисточников для карточки google-drive. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "google-drive", "kind": "connector", "cluster": "21-files-storage", "group": "облачные диски", "name": "Google Drive", "vendor": "Google", "state": "connected", "platform_description": "Search, read, and upload files instantly", "source": "ListConnectors"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[google-drive] инструменты (префикс mcp__Google_Drive__): search_files, list_recent_files, get_file_metadata, read_file_content, download_file_content, create_file, update_file, copy_file, trash_file, share_file, get_file_permissions, list_shared_drives, get_shared_drive_metadata
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### Google Drive
This is an MCP server provided by Drive API. The server provides tools for developers to build LLM applications on top of Drive.
````
