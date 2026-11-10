<!-- Выдержки первоисточников для карточки german-legal-deadline-calculator. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "german-legal-deadline-calculator", "kind": "skill", "cluster": "11-law-de-eu", "group": "сроки и расчёты", "name": "german-legal-deadline-calculator", "vendor": "уточнить", "state": "enabled", "platform_description": "Расчёт сроков в немецких процессах (Widerspruch, Klage, Verjährung) с учётом выходных и праздников", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: german-legal-deadline-calculator
description: "Precise deadline calculations for German legal proceedings (Widerspruch, Klage, Verjährung) with automatic exclusion of weekends/holidays, Fristwahrung rules, and safety margin recommendations. Specialized for German social law (SGG, SGB, BGB). Triggers: 'calculate deadline', 'Widerspruchsfrist berechnen', 'when is Klage deadline', 'Verjährung check', 'count days until', 'working days calculation', 'is this deadline valid'."
---

# German Legal Deadline Calculator

## Core Purpose
Calculate legally accurate deadlines for German court and administrative proceedings, accounting for weekend/holiday rules, different deadline types, and providing safety margins.

## Legal Framework

### 1. Key Deadline Rules

**A. General Principles (§187-193 BGB)**
```
Start of deadline:
- Event occurs on Day X
- Deadline starts Day X+1 (§187 Abs. 1 BGB)
- Exception: Midnight events start same day

End of deadline:
- Month deadlines → same day number next month (§188 Abs. 2 BGB)
- Week deadlines → same weekday next week
- If end day = Sunday/holiday → next workday (§193 BGB)
```

**B. Court Proceedings (§64 SGG, §222 ZPO)**
```
Widerspruch: 1 month from Bekanntgabe (notification)
Klage: 1 month from Widerspruchsbescheid
Berufung: 1 month from Urteil (if allowed)
Revision: 1 month from Berufungsurteil
```

**C. Verjährung (Statute of Limitations)**
```
Social benefits: 4 years (§45 SGB I)
Start: December 31 of year when claim arose
Example: Claim 2020 → Verjährung 31.12.2024
````
