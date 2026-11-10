<!-- Выдержки первоисточников для карточки agent-handoff. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "agent-handoff", "kind": "plugin", "cluster": "18-memory-sessions", "group": "handoff и чекпоинты", "name": "agent-handoff", "vendor": "уточнить", "state": "enabled", "platform_description": "4 скилла: plan, execute, verify, setup-handoff", "source": "список скиллов сессии"},
````

## [2] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "agent-handoff",
  "version": "0.4.2",
  "description": "Strict 3-stage handoff workflow (plan → execute → verify) for coding agents. Disk-backed state enables fresh-context code review and multi-stage verification across chat contexts. Supports multi-phase plans and parallel subagent execution.",
  "keywords": [
    "handoff",
    "workflow",
    "plan",
    "execute",
    "verify",
    "verification",
    "multi-stage",
    "context-handoff",
    "code-review",
    "coding-agent"
  ],
  "author": {
    "name": "WillowRyu",
    "url": "https://github.com/WillowRyu"
  },
  "homepage": "https://github.com/WillowRyu/agent-handoff",
  "repository": "https://github.com/WillowRyu/agent-handoff",
  "license": "MIT",
  "skills": [
    "./skills/setup-handoff",
    "./skills/plan",
    "./skills/execute",
    "./skills/verify"
  ]
}
````
