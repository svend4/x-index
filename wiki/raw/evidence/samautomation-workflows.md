<!-- Выдержки первоисточников для карточки samautomation-workflows. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "samautomation-workflows", "kind": "plugin", "cluster": "08-automation-ipaas", "group": "сценарии (make, zapier, n8n)", "name": "samautomation-workflows", "vendor": "уточнить", "state": "enabled", "platform_description": "1 скилл: n8n-workflow-check", "source": "список скиллов сессии"},
````

## [2] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "samautomation-workflows",
  "version": "1.0.2",
  "description": "Build or repair importable n8n workflow JSON, check its structure and test valid, duplicate and invalid events in isolation. Includes a read-only checker and a manual fixture tested on n8n 2.23.4. No account connection, network requests or activation by the bundled checker.",
  "author": {
    "name": "Samautomation",
    "url": "https://samautomation.work"
  },
  "homepage": "https://github.com/smrht/samautomation-workflows",
  "repository": "https://github.com/smrht/samautomation-workflows",
  "license": "MIT",
  "skills": "./skills/",
  "keywords": [
    "n8n",
    "n8n workflow",
    "workflow automation",
    "webhook",
    "automation",
    "n8n json",
    "workflow automatisering"
  ],
  "icon": "assets/icon.png"
}
````
