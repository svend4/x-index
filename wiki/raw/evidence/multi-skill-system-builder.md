<!-- Выдержки первоисточников для карточки multi-skill-system-builder. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "multi-skill-system-builder", "kind": "skill", "cluster": "00-meta", "group": "управление skills и плагинами", "name": "multi-skill-system-builder", "vendor": "уточнить", "state": "enabled", "platform_description": "Мета-скилл для систем из нескольких skills (Core/Extended/Companion) при лимите описания 1024 знака", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: multi-skill-system-builder
description: "Meta-skill for creating large multi-skill systems and domain orchestrators. Helps split complex skills into 2-3 interconnected skills (Core/Extended/Companion pattern) when hitting 1024-char description limit. Provides: architecture patterns, splitting methodology, templates for different domains (legal, social, business, restaurant, healthcare, education, etc), description optimization strategies, skill coordination patterns, testing frameworks. TRIGGERS: create skill system|build domain manager|split large skill|multi-skill architecture|domain orchestrator|skill ecosystem|description too long|1024 limit. OUTPUTS: skill structures, YAML templates, coordination logic, installation guides. USE CASES: large domain managers, professional skill suites, business vertical skills, complex workflow orchestrators. v1.0"
---

# Multi-Skill System Builder

## 🎯 Core Purpose

**Meta-skill для создания больших skill-систем** когда один skill не вмещается в лимит 1024 символов или требует сложной архитектуры.

## 🏗️ Architecture Patterns

### Pattern 1: Dual-Skill (Core + Extended)

**Когда использовать:**
- Description >1024 символов
- Много документации и примеров
- Основная функциональность отделяется от обучающих материалов

**Структура:**
```
┌─────────────────────────────────┐
│  DOMAIN-MANAGER (Core)          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Active orchestration          │
│  • Auto-activation               │
│  • Workflow execution            │
│  • Skill coordination            │
│  • <1024 chars ✓                 │
│  ROLE: Functionality             │
└─────────────────────────────────┘
            ↕
┌─────────────────────────────────┐
│  DOMAIN-MANAGER-EXTENDED        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Detailed documentation        │
│  • Examples & use cases          │
│  • Best practices                │
│  • Troubleshooting               │
````
