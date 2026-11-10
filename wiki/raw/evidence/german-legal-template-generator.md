<!-- Выдержки первоисточников для карточки german-legal-template-generator. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "german-legal-template-generator", "kind": "skill", "cluster": "11-law-de-eu", "group": "процессы по делу", "name": "german-legal-template-generator", "vendor": "уточнить", "state": "enabled", "platform_description": "Шаблоны по социальному праву: Widerspruch, Klage, заявления на персональный бюджет (DE, RU, EN)", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: german-legal-template-generator
description: "Professional legal document templates for German social law (SGB IX, XII), personal budget applications, Widerspruch, Klage, and compensation calculations. Multilingual support (DE/RU/EN) with automatic legal citations and formatting. Triggers: 'создай шаблон заявления', 'generate Widerspruch', 'template for Klage', 'persönliches Budget Antrag', 'compensation calculation', 'social law template', 'SGB IX template'."
---

# German Legal Template Generator

## Core Purpose
Generate professional, legally sound templates for German social law proceedings with automatic legal citations, proper formatting, and multilingual support.

## Capabilities

### 1. Document Types
**Applications (Anträge):**
- Persönliches Budget (§29 SGB IX)
- Teilhabeleistungen (participation benefits)
- Pflegegraderhöhung (care level increase)
- Wohngeld (housing allowance)
- Kindergeld (child benefits)

**Objections & Lawsuits:**
- Widerspruch (objection - 1 month deadline)
- Klage vor Sozialgericht (lawsuit)
- Eilantrag/einstweilige Anordnung (emergency motion)
- Berufung (appeal)

**Compensation Claims:**
- Retroactive payments (rückwirkende Zahlungen)
- Verjährungsfristen calculations (4 years for social benefits)
- Interest calculations (§44 SGB I)

### 2. Legal Citation Engine
**Automatic References:**
- SGB IX (Rehabilitation und Teilhabe)
- SGB XII (Sozialhilfe)
- SGB I (Allgemeiner Teil)
- BGB (Bürgerliches Gesetzbuch)
- SGB X (Verwaltungsverfahren)

**Example Output:**
````
