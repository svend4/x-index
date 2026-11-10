<!-- Выдержки первоисточников для карточки court-document-analyzer. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "court-document-analyzer", "kind": "skill", "cluster": "11-law-de-eu", "group": "процессы по делу", "name": "court-document-analyzer", "vendor": "уточнить", "state": "enabled", "platform_description": "Анализ судебных документов и Bescheid: факты, сроки, аргументы, слабые места, контрстратегии", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: court-document-analyzer
description: "Intelligent analysis of German court documents, administrative decisions (Bescheid), and legal correspondence. Extracts key facts, deadlines, legal arguments, identifies weaknesses, and suggests counter-strategies. Specialized for Sozialgericht cases. Triggers: 'analyze court document', 'проанализируй Bescheid', 'extract deadlines from', 'find legal arguments in', 'check Widerspruchsbescheid', 'review Urteil', 'identify weaknesses'."
---

# Court Document Analyzer

## Core Purpose
Systematically analyze German legal documents to extract critical information, identify arguments, detect weaknesses, and recommend legal strategies.

## Capabilities

### 1. Document Types Supported

**Court Documents:**
- Bescheid (administrative decision)
- Widerspruchsbescheid (objection decision)
- Urteil (judgment)
- Beschluss (court order)
- Ladung (summons)
- Verfügung (directive)

**Correspondence:**
- Letters from Sozialamt
- Attorney communications
- Expert opinions (Gutachten)
- Medical assessments (MDK reports)

### 2. Extraction Engine

**Automatic Extraction:**

**A. Critical Dates**
```
Pattern recognition:
- "vom [Datum]" → document date
- "Widerspruch bis [Datum]" → deadline
- "rechtskräftig am [Datum]" → final date
- "Zustellung am [Datum]" → notification date
````
