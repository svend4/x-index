<!-- Выдержки первоисточников для карточки agent-discussion. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "agent-discussion", "kind": "plugin", "cluster": "19-agents-orchestration", "group": "дебаты и ревью агентов", "name": "agent-discussion", "vendor": "уточнить", "state": "enabled", "platform_description": "1 скилл: agent-discussion", "source": "список скиллов сессии"},
````

## [2] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "agent-discussion",
  "description": "Coordinate multi-agent debates across different AI platforms (Claude Code, Antigravity, Copilot, Gemini CLI, etc.) using a shared file protocol. Each agent reads one skill and handles everything autonomously — intros, turn-taking, and consensus.",
  "author": {
    "name": "Cyrus Liu"
  },
  "homepage": "https://github.com/cyrusxyl/agent-discussion",
  "version": "0.1.0"
}
````
