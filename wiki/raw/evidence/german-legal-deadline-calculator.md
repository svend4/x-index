<!-- Выдержки первоисточников для карточки german-legal-deadline-calculator. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "german-legal-deadline-calculator", "kind": "skill", "cluster": "11-law-de-eu", "group": "сроки и расчёты", "name": "german-legal-deadline-calculator", "vendor": "уточнить", "state": "enabled", "platform_description": "Расчёт сроков в немецких процессах (Widerspruch, Klage, Verjährung) с учётом выходных и праздников", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало): общие правила, сроки судебного процесса, Verjährung (раздел 1)
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
Special: If Bescheid issued, clock resets
```
````

## [3] локальный файл скилла: праздники и правило выходных (раздел 2)
- Снимок: 2026-11-10
- Фрагмент:

````text
### 2. Holiday Calendar

**German Public Holidays (Bundesweit):**
```python
FEDERAL_HOLIDAYS = {
    "Neujahr": "01.01",
    "Karfreitag": "[Easter-2]",  # Good Friday
    "Ostermontag": "[Easter+1]",
    "Tag der Arbeit": "05.01",
    "Christi Himmelfahrt": "[Easter+39]",
    "Pfingstmontag": "[Easter+50]",
    "Tag der Deutschen Einheit": "10.03",
    "1. Weihnachtstag": "12.25",
    "2. Weihnachtstag": "12.26"
}

# Saxony-specific (Dresden)
SAXONY_HOLIDAYS = {
    "Fronleichnam": "[Easter+60]",  # Some regions
    "Buß- und Bettag": "[November, Wednesday before -22]"
}
```

**Weekend Rule:**
```
Saturday = not a workday (§193 BGB)
Sunday = not a workday (§193 BGB)

If deadline ends on Sat/Sun/Holiday:
→ Deadline moves to next workday
```
````

## [4] локальный файл скилла: расчёт сроков по месяцам и по дням (раздел 3, A–B)
- Снимок: 2026-11-10
- Фрагмент:

````text
### 3. Calculation Types

**A. Month-Based Deadlines**
```python
def calculate_month_deadline(start_date, months=1):
    # Example: Bescheid received 15.01.2026
    # Start: 16.01.2026 (next day per §187 BGB)
    # End: 16.02.2026 (same day next month per §188 BGB)
    
    if end_date.is_weekend_or_holiday():
        end_date = next_workday(end_date)
    
    return end_date
```

**Example:**
```
Bescheid received: 15.01.2026 (Wednesday)
Deadline starts: 16.01.2026 (Thursday)
1 month later: 16.02.2026 (Monday)
Check: 16.02.2026 = workday ✓
DEADLINE: 16.02.2026

Safety margin: 13.02.2026 (3 days before)
Einschreiben send: 10.02.2026 (6 days before)
```

**B. Day-Based Deadlines**
```python
def calculate_day_deadline(start_date, days):
    # Only for specific provisions
    # Example: §569 BGB (rental termination)
    
    current = start_date + 1 day  # §187 Abs. 1
    count = 0
    
    while count < days:
        current += 1 day
        count += 1
    
    if current.is_weekend_or_holiday():
        current = next_workday(current)
    
    return current
```
````

## [5] локальный файл скилла: долгосрочная Verjährung (раздел 3, C)
- Снимок: 2026-11-10
- Фрагмент:

````text
**C. Verjährung (Long-Term)**
```python
def calculate_verjährung(claim_year, knowledge_year=None):
    # Standard: 4 years from end of year claim arose
    # Special: 4 years from knowledge
    
    if knowledge_year:
        start = f"{knowledge_year}-12-31"
    else:
        start = f"{claim_year}-12-31"
    
    end = start + 4 years
    
    return end

# Example
claim_year = 2020
verjährung = 2024-12-31

# If discovered later
knowledge_year = 2023
verjährung = 2027-12-31
```
````

## [6] локальный файл скилла: особые случаи — Fristwahrung, Bekanntgabe, Wiedereinsetzung (раздел 4)
- Снимок: 2026-11-10
- Фрагмент:

````text
### 4. Special Cases

**A. Fristwahrung (Preserving Deadline)**
```
Definition: Action must REACH authority before end of last day

Methods:
1. Personal delivery (Abgabe) - SAFEST
2. Regular mail (Brief) - Count 3+ days
3. Registered mail (Einschreiben) - Postmark counts if delivered
4. Fax (before 24:00 last day) - Still accepted by many courts
5. Electronic (DE-Mail) - If court supports it
6. Court mailbox (Gerichtsbriefkasten) - Before midnight

RECOMMENDATION: Always 3-day safety margin minimum!
```

**B. Bekanntgabe (Notification) Rules**
```
Document considered "known" (§41 SGB X):
- Personal delivery: same day
- Regular mail: 3rd day after posting (legal fiction)
- If delivery proof shows earlier: that date
- If no delivery proof: authority must prove

Example:
Letter posted: 10.01.2026
Assumed delivery: 13.01.2026 (§41 Abs. 2 SGB X)
Deadline starts: 14.01.2026
Deadline ends: 14.02.2026
```

**C. Wiedereinsetzung (Restoration of Deadline)**
```
If deadline missed without fault (§67 SGB X):
- Apply within 2 weeks of obstacle removal
- Max 6 months after missed deadline (absolute)
- Explain reasons
- Submit missing action immediately

Requirements:
✓ No fault (unverschuldet)
✓ Explanation convincing
✓ Quick action after discovery

Success rate: ~20% (difficult!)
```
````

## [7] локальный файл скилла: сводная таблица сроков (раздел 8)
- Снимок: 2026-11-10
- Фрагмент:

````text
### 8. Quick Reference Table

| Deadline Type | Duration | Law | Notes |
|--------------|----------|-----|-------|
| Widerspruch | 1 month | §84 SGG | From Bekanntgabe |
| Klage | 1 month | §87 SGG | From Widerspruchsbescheid |
| Berufung | 1 month | §143 SGG | If >750€ dispute |
| Revision | 1 month | §160 SGG | If allowed |
| Verjährung | 4 years | §45 SGB I | Social benefits |
| Wiedereinsetzung | 2 weeks | §67 SGB X | Max 6 months absolute |
````

## [8] § 187 BGB (Fristbeginn): абзацы (1)–(2), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 187 BGB — Fristbeginn
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Ist für den Anfang einer Frist ein Ereignis oder ein in den Lauf eines Tages fallender Zeitpunkt maßgebend, so wird bei der Berechnung der Frist der Tag nicht mitgerechnet, in welchen das Ereignis oder der Zeitpunkt fällt.
(2) Ist der Beginn eines Tages der für den Anfang einer Frist maßgebende Zeitpunkt, so wird dieser Tag bei der Berechnung der Frist mitgerechnet. Das Gleiche gilt von dem Tage der Geburt bei der Berechnung des Lebensalters.
````

## [9] § 188 BGB (Fristende): абзацы (1)–(3), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 188 BGB — Fristende
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Eine nach Tagen bestimmte Frist endigt mit dem Ablauf des letzten Tages der Frist.
(2) Eine Frist, die nach Wochen, nach Monaten oder nach einem mehrere Monate umfassenden Zeitraum - Jahr, halbes Jahr, Vierteljahr - bestimmt ist, endigt im Falle des § 187 Abs. 1 mit dem Ablauf desjenigen Tages der letzten Woche oder des letzten Monats, welcher durch seine Benennung oder seine Zahl dem Tage entspricht, in den das Ereignis oder der Zeitpunkt fällt, im Falle des § 187 Abs. 2 mit dem Ablauf desjenigen Tages der letzten Woche oder des letzten Monats, welcher dem Tage vorhergeht, der durch seine Benennung oder seine Zahl dem Anfangstag der Frist entspricht.
(3) Fehlt bei einer nach Monaten bestimmten Frist in dem letzten Monat der für ihren Ablauf maßgebende Tag, so endigt die Frist mit dem Ablauf des letzten Tages dieses Monats.
````

## [10] § 193 BGB (Sonn- und Feiertag; Sonnabend), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 193 BGB — Sonn- und Feiertag; Sonnabend
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
Ist an einem bestimmten Tage oder innerhalb einer Frist eine Willenserklärung abzugeben oder eine Leistung zu bewirken und fällt der bestimmte Tag oder der letzte Tag der Frist auf einen Sonntag, einen am Erklärungs- oder Leistungsort staatlich anerkannten allgemeinen Feiertag oder einen Sonnabend, so tritt an die Stelle eines solchen Tages der nächste Werktag.
````

## [11] § 64 SGG: абзацы (1)–(3), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 64 SGG
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Der Lauf einer Frist beginnt, soweit nichts anderes bestimmt ist, mit dem Tag nach der Zustellung oder, wenn diese nicht vorgeschrieben ist, mit dem Tag nach der Eröffnung oder Verkündung.
(2) Eine nach Tagen bestimmte Frist endet mit dem Ablauf ihres letzten Tages, eine nach Wochen oder Monaten bestimmte Frist mit dem Ablauf desjenigen Tages der letzten Woche oder des letzten Monats, welcher nach Benennung oder Zahl dem Tag entspricht, in den das Ereignis oder der Zeitpunkt fällt. Fehlt dem letzten Monat der entsprechende Tag, so endet die Frist mit dem Monat.
(3) Fällt das Ende einer Frist auf einen Sonntag, einen gesetzlichen Feiertag oder einen Sonnabend, so endet die Frist mit Ablauf des nächsten Werktags.
````

## [12] § 84 SGG: абзац (1), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 84 SGG
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diese Fassung haben wir zuerst am 03.01.2024 gesehen; das ist ein Beobachtungsdatum, kein amtliches Inkrafttretensdatum.
(1) Der Widerspruch ist binnen eines Monats, nachdem der Verwaltungsakt dem Beschwerten bekanntgegeben worden ist, schriftlich, in elektronischer Form nach § 36a Absatz 2 des Ersten Buches Sozialgesetzbuch, schriftformersetzend nach § 36a Absatz 2a des Ersten Buches Sozialgesetzbuch und § 9a Absatz 5 des Onlinezugangsgesetzes oder zur Niederschrift bei der Stelle einzureichen, die den Verwaltungsakt erlassen hat. Die Frist beträgt bei Bekanntgabe im Ausland drei Monate.
````

## [13] § 87 SGG: абзацы (1)–(2), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 87 SGG
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Die Klage ist binnen eines Monats nach Bekanntgabe des Verwaltungsakts zu erheben. Die Frist beträgt bei Bekanntgabe im Ausland drei Monate. Bei einer öffentlichen Bekanntgabe nach § 85 Abs. 4 beträgt die Frist ein Jahr. Die Frist beginnt mit dem Tag zu laufen, an dem seit dem Tag der letzten Veröffentlichung zwei Wochen verstrichen sind.
(2) Hat ein Vorverfahren stattgefunden, so beginnt die Frist mit der Bekanntgabe des Widerspruchsbescheids.
````

## [14] § 151 SGG: абзац (1), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 151 SGG
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Die Berufung ist bei dem Landessozialgericht innerhalb eines Monats nach Zustellung des Urteils schriftlich oder zu Protokoll des Urkundsbeamten der Geschäftsstelle einzulegen.
````

## [15] § 164 SGG: абзацы (1)–(2), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 164 SGG
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Die Revision ist bei dem Bundessozialgericht innerhalb eines Monats nach Zustellung des Urteils oder des Beschlusses über die Zulassung der Revision (§ 160a Absatz 4 Satz 1 oder § 161 Abs. 3 Satz 2) schriftlich einzulegen. Die Revision muß das angefochtene Urteil angeben; eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils soll beigefügt werden, sofern dies nicht schon nach § 160a Abs. 1 Satz 3 geschehen ist. Satz 2 zweiter Halbsatz gilt nicht, soweit nach § 65a elektronische Dokumente übermittelt werden.
(2) Die Revision ist innerhalb von zwei Monaten nach Zustellung des Urteils oder des Beschlusses über die Zulassung der Revision zu begründen. Die Begründungsfrist kann auf einen vor ihrem Ablauf gestellten Antrag von dem Vorsitzenden verlängert werden. Die Begründung muß einen bestimmten Antrag enthalten, die verletzte Rechtsnorm und, soweit Verfahrensmängel gerügt werden, die Tatsachen bezeichnen, die den Mangel ergeben.
````

## [16] § 67 SGG: абзацы (1)–(3), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 67 SGG
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Wenn jemand ohne Verschulden verhindert war, eine gesetzliche Verfahrensfrist einzuhalten, so ist ihm auf Antrag Wiedereinsetzung in den vorigen Stand zu gewähren.
(2) Der Antrag ist binnen eines Monats nach Wegfall des Hindernisses zu stellen. Die Tatsachen zur Begründung des Antrags sollen glaubhaft gemacht werden. Innerhalb der Antragsfrist ist die versäumte Rechtshandlung nachzuholen. Ist dies geschehen, so kann die Wiedereinsetzung auch ohne Antrag gewährt werden.
(3) Nach einem Jahr seit dem Ende der versäumten Frist ist der Antrag unzulässig, außer wenn der Antrag vor Ablauf der Jahresfrist infolge höherer Gewalt unmöglich war.
````

## [17] § 27 SGB X (Wiedereinsetzung): абзацы (1)–(3), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 27 SGB X — Wiedereinsetzung in den vorigen Stand
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) War jemand ohne Verschulden verhindert, eine gesetzliche Frist einzuhalten, ist ihm auf Antrag Wiedereinsetzung in den vorigen Stand zu gewähren. Das Verschulden eines Vertreters ist dem Vertretenen zuzurechnen.
(2) Der Antrag ist innerhalb von zwei Wochen nach Wegfall des Hindernisses zu stellen. Die Tatsachen zur Begründung des Antrages sind bei der Antragstellung oder im Verfahren über den Antrag glaubhaft zu machen. Innerhalb der Antragsfrist ist die versäumte Handlung nachzuholen. Ist dies geschehen, kann Wiedereinsetzung auch ohne Antrag gewährt werden.
(3) Nach einem Jahr seit dem Ende der versäumten Frist kann die Wiedereinsetzung nicht mehr beantragt oder die versäumte Handlung nicht mehr nachgeholt werden, außer wenn dies vor Ablauf der Jahresfrist infolge höherer Gewalt unmöglich war.
````

## [18] § 37 SGB X (Bekanntgabe): абзацы (2) и (4), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 37 SGB X — Bekanntgabe des Verwaltungsaktes
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diese Fassung haben wir zuerst am 31.12.2025 gesehen; das ist ein Beobachtungsdatum, kein amtliches Inkrafttretensdatum.
(2) Ein schriftlicher Verwaltungsakt, der im Inland durch die Post übermittelt wird, gilt am vierten Tag nach der Aufgabe zur Post als bekannt gegeben. Ein Verwaltungsakt, der im Inland oder Ausland elektronisch übermittelt wird, gilt am vierten Tag nach der Absendung als bekannt gegeben. Dies gilt nicht, wenn der Verwaltungsakt nicht oder zu einem späteren Zeitpunkt zugegangen ist; im Zweifel hat die Behörde den Zugang des Verwaltungsaktes und den Zeitpunkt des Zugangs nachzuweisen.
(4) Die öffentliche Bekanntgabe eines schriftlichen oder elektronischen Verwaltungsaktes wird dadurch bewirkt, dass sein verfügender Teil in der jeweils vorgeschriebenen Weise entweder ortsüblich oder in der sonst für amtliche Veröffentlichungen vorgeschriebenen Art bekannt gemacht wird. In der Bekanntmachung ist anzugeben, wo der Verwaltungsakt und seine Begründung eingesehen werden können. Der Verwaltungsakt gilt zwei Wochen nach der Bekanntmachung als bekannt gegeben. In einer Allgemeinverfügung kann ein hiervon abweichender Tag, jedoch frühestens der auf die Bekanntmachung folgende Tag bestimmt werden.
````

## [19] § 41 SGB X (Heilung von Verfahrens- und Formfehlern): начало абзаца (1), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 41 SGB X — Heilung von Verfahrens- und Formfehlern
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Eine Verletzung von Verfahrens- oder Formvorschriften, die nicht den Verwaltungsakt nach § 40 nichtig macht, ist unbeachtlich, wenn
````

## [20] § 67 SGB X (Begriffsbestimmungen): абзац (1), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 67 SGB X — Begriffsbestimmungen
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diese Fassung haben wir zuerst am 02.12.2019 gesehen; das ist ein Beobachtungsdatum, kein amtliches Inkrafttretensdatum.
(1) Die nachfolgenden Begriffsbestimmungen gelten ergänzend zu Artikel 4 der Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016 zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung) (ABl. L 119 vom 4.5.2016, S. 1; L 314 vom 22.11.2016, S. 72; L 127 vom 23.5.2018, S. 2) in der jeweils geltenden Fassung.
````

## [21] § 45 SGB I (Verjährung): абзацы (1)–(3), текст nu:legal
- Снимок: 2026-11-10
- Фрагмент:

````text
## § 45 SGB I — Verjährung
Stand: 10.11.2026 (zuletzt mit der konsolidierten Fassung abgeglichen). Diesen Text führen wir unverändert seit mindestens 10.06.2019, dem Beginn unseres Archivs.
(1) Ansprüche auf Sozialleistungen verjähren in vier Jahren nach Ablauf des Kalenderjahrs, in dem sie entstanden sind.
(2) Für die Hemmung, die Ablaufhemmung, den Neubeginn und die Wirkung der Verjährung gelten die Vorschriften des Bürgerlichen Gesetzbuchs sinngemäß.
(3) Die Verjährung wird auch durch schriftlichen Antrag auf die Sozialleistung oder durch Erhebung eines Widerspruchs gehemmt. Die Hemmung endet sechs Monate nach Bekanntgabe der Entscheidung über den Antrag oder den Widerspruch.
````
