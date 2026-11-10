<!-- Выдержки первоисточников для карточки gmail. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "gmail", "kind": "connector", "cluster": "01-communication", "group": "почта", "name": "Gmail", "vendor": "Google", "state": "connected", "platform_description": "Draft replies, summarize threads, & search your inbox", "source": "ListConnectors"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[gmail] инструменты (префикс mcp__Gmail__): search_threads, get_thread, get_message, create_draft, get_draft, list_drafts, update_draft, delete_draft, reply, forward, send_message, list_labels, create_label, update_label, delete_label, label_message, label_thread, unlabel_message, unlabel_thread, update_message_labels, trash_message, trash_thread, untrash_message, untrash_thread, mark_message_spam, mark_thread_spam, unmark_message_spam, unmark_thread_spam, apply_sensitive_message_label, apply_sensitive_thread_label, download_gmail_attachment
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### Gmail
This is an MCP server provided by Gmail API. The server provides tools for developers to build LLM applications on top of Gmail.
````
