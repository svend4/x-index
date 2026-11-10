<!-- Выдержки первоисточников для карточки memory-toolkit. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "memory-toolkit", "kind": "plugin", "cluster": "18-memory-sessions", "group": "заметки о сессиях", "name": "memory-toolkit", "vendor": "уточнить", "state": "enabled", "platform_description": "11 скиллов: память проекта, workstreams, заметки, решения, сессии (start, end, continue, restore, insights), park, reflect, task-template", "source": "список скиллов сессии"},
````

## [2] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "memory-toolkit",
  "description": "Session memory lifecycle for developers — structured markdown memory, workstreams, handoff, auto-save hooks. No vector DB, no external dependencies.",
  "version": "1.9.13",
  "author": {
    "name": "Ilya Gorsky"
  },
  "license": "MIT",
  "keywords": ["memory", "session", "workstream", "handoff", "lifecycle"],
  "commandsMetadata": {
    "session-start": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "session-continue": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "session-end": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "memory": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "memory-setup": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "reflect": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "docs-reflect": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "park": { "allowedTools": ["Bash", "Read", "Write", "Glob", "Grep"] },
    "session-restore": { "allowedTools": ["Bash", "Read", "Glob", "Grep"] },
    "session-insights": { "allowedTools": ["Bash", "Read", "Glob", "Grep"] }
  }
}
````
