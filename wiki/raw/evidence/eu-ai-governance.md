<!-- Выдержки первоисточников для карточки eu-ai-governance. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "eu-ai-governance", "kind": "plugin", "cluster": "20-compliance-ai-act", "group": "AI Act", "name": "eu-ai-governance", "vendor": "уточнить", "state": "enabled", "platform_description": "Скиллы AI Act: классификация риска, соответствие, оценка вендора, DPIA, политика, управление рисками, документация", "source": "список скиллов сессии"},
````

## [2] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "eu-ai-governance",
  "displayName": "Lexbeam EU AI Governance",
  "version": "1.1.3",
  "description": "Source-grounded EU AI Act governance for European legal, compliance, privacy, security, and AI governance teams: classification, DPIA and FRIA workflows, vendor review, policy review, and evidence packs.",
  "author": {
    "name": "Lexbeam Software",
    "url": "https://lexbeam.com"
  },
  "homepage": "https://lexbeam-software.github.io/eu-ai-governance-plugin/",
  "privacyPolicyUrl": "https://github.com/lexbeam-software/eu-ai-act-mcp/blob/main/PRIVACY.md",
  "documentationUrl": "https://github.com/lexbeam-software/eu-ai-governance-plugin#readme",
  "termsOfServiceUrl": "https://github.com/lexbeam-software/eu-ai-governance-plugin/blob/main/LEGAL-DISCLAIMER.md",
  "repository": "https://github.com/lexbeam-software/eu-ai-governance-plugin",
  "license": "Apache-2.0",
  "keywords": [
    "eu-ai-act",
    "ai-governance",
    "compliance",
    "dpia",
    "fria",
    "ai-risk-classification",
    "evidence-pack",
    "dach"
  ]
}
````

## [3] список инструментов сессии: строка сервера eu-ai-act-mcp и префикс инструментов
- Снимок: 2026-11-10
- Фрагмент:

````text
[eu-ai-act-mcp] инструменты (префикс mcp__plugin_eu-ai-governance_eu-ai-act__): euaiact_annex_iv_checklist, euaiact_answer_question, euaiact_assess_art6_3_exception, euaiact_assess_system, euaiact_calculate_penalty, euaiact_check_deadlines, euaiact_check_gpai_systemic_risk, euaiact_classify_system, euaiact_get_article, euaiact_get_obligations
````
