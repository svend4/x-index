<!-- Выдержки первоисточников для карточки legal-domain-manager. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "legal-domain-manager", "kind": "skill", "cluster": "11-law-de-eu", "group": "процессы по делу", "name": "legal-domain-manager", "vendor": "уточнить", "state": "enabled", "platform_description": "Оркестратор для немецкого социального права (SGG, SGB IX/XII, Sozialgericht): Bescheid, Widerspruch, Klage, сроки", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: legal-domain-manager
description: "Meta-orchestrator for German legal work (SGG/SGB IX/XII, Sozialgericht). MANAGES: german-legal-deadline-calculator (deadlines+Fristwahrung), court-document-analyzer (doc analysis+arguments), german-legal-template-generator (Widerspruch/Klage templates). SUPPORTS: docx/pdf/xlsx. WORKFLOWS: [1]Bescheid-Response(6min): analyzer→deadline-calc→template→docx [2]Klage-Prep(10min): analyzer→deadline-calc→template→evidence→docx [3]Case-Management: Antrag→Bescheid→Widerspruch→Klage→Urteil with timeline tracking. TRIGGERS: Bescheid|Widerspruch|Klage|Urteil|Sozialgericht|Aktenzeichen|Frist|deadline|SGB|SGG|Sozialamt|analyze|проанализируй. AUTO: context-detect, sequential-activation, deadline-tracking(🔴≤3d|🟠≤7d|🟡≤14d|🟢≤21d|⚪>21d), state-persistence. INTEGRATION: Claude Projects, chat-migration-v5. LANG: DE/RU/EN. COMPANION: legal-domain-manager-extended for advanced features. v1.0"
---

# Legal Domain Manager (Core)

## 🎯 Core Purpose

**Meta-orchestrator** для всей юридической работы по немецкому праву. Автоматически активирует нужные legal skills, координирует их работу, управляет workflows от получения Bescheid до подачи Klage.

**💡 NOTE:** This is the CORE skill. For advanced features, examples, and detailed documentation, activate companion skill: **legal-domain-manager-extended**

## 🧬 Architecture

### Domain Scope
```
LEGAL DOMAIN (Core Orchestration)
├─ Managed Skills (3)
│  ├─ german-legal-deadline-calculator
│  ├─ court-document-analyzer
│  └─ german-legal-template-generator
│
├─ Support Skills (3)
│  ├─ docx (document generation)
│  ├─ pdf (document processing)
│  └─ xlsx (data tables, calculations)
│
└─ Integration (2)
   ├─ Claude Projects (state persistence)
   └─ chat-migration (continuity)
```

### Activation Logic
```python
# Core activation triggers

TRIGGERS = {
    "high_priority": [
        "Bescheid", "Widerspruch", "Klage", "Urteil",
````
