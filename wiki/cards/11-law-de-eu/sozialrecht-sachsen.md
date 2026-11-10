---
id: "sozialrecht-sachsen"
title: "Sozialrecht Sachsen"
kind: "plugin"
vendor: "уточнить"
cluster: "11-law-de-eu"
group: "процессы по делу"
summary: "Плагин из семи скиллов по социальному праву Саксонии: Bescheid, сроки, Widerspruch, Klage, персональный бюджет и проверка цитат."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: ["de"]
jurisdiction: "DE"
source_urls: ["raw://session/2026-11-10/inventory.json", "raw://evidence/sozialrecht-sachsen.md", "raw://session/2026-11-10/evidence/plugin-sozialrecht-sachsen-skills.txt"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Саксония", "Sachsen", "SGB IX", "SGB XII", "персональный бюджет", "Persönliches Budget", "Eingliederungshilfe", "Hilfe zur Pflege", "Zitate-Gate", "Bescheid", "Widerspruch", "Klage"]
---

# Sozialrecht Sachsen

## Суть
- Плагин по социальному праву Саксонии: SGB IX и XII, персональный бюджет, Eingliederungshilfe и Hilfe zur Pflege [2].
- В составе расчёт сроков с саксонскими праздниками, анализ Bescheid, черновики Widerspruch и Klage, калькулятор расходов модели работодателя (Arbeitgebermodell) и Zitate-Gate [2].
- В сессии плагин включён, состав — семь скиллов [1].

## Для чего
- Подготовка к процессам по социальным делам в Саксонии: Bescheid, Widerspruch, Klage, персональный бюджет [1][2].
- Расчёт сроков с учётом саксонских праздников [2].
- Проверка норм и решений перед отправкой [2].
- Группа инвентаря: процессы по делу [1].
- нет данных о целевой аудитории инструмента.

## Возможности
- Детерминированный расчёт сроков с саксонскими праздниками [2].
- Анализ Bescheid [2].
- Черновики Widerspruch и Klage [2].
- Калькулятор расходов модели работодателя (Arbeitgebermodell) [2].
- Zitate-Gate: каждая норма и решение проверяются через коннекторы nu:legal и Zitierfest перед отправкой [2].
- Источники берутся из коннекторов, а не из памяти модели [2].
- Семь скиллов плагина (префикс `sozialrecht-sachsen:`) [3]:
  - `bescheid-analyse`: структурированный разбор Bescheid, Widerspruchsbescheid или письма Leistungsträger (Verfügungssatz, Rechtsgrundlagen, Fristen, Begründungslücken, fehlende Unterlagen, Angriffspunkte, nächste Schritte); сначала псевдонимизация [3];
  - `fristen`: детерминированный расчёт сроков: Widerspruch (§ 84 SGG), Klage (§ 87 SGG), Berufung (§ 151 SGG), Jahresfrist (§ 66 Abs. 2 SGG), Bekanntgabefiktion (§ 37 Abs. 2 SGB X), § 64 SGG и саксонские праздники; расчёт выполняется скриптом, а не по памяти [3];
  - `klage`: черновик Klage zum Sozialgericht против Widerspruchsbescheid (Anfechtungs-, Verpflichtungs-, Leistungsklage, §§ 54, 56 SGG): fristwahrende Klageschrift и Begründung, станции SG Dresden / Sächsisches LSG, обязательная проверка через zitate-gate [3];
  - `persoenliches-budget`: подготовка Persönliches Budget (§ 29 SGB IX): структура Bedarfsermittlung (§ 13 SGB IX), расчёт расходов модели работодателя (зарплата, взносы работодателя, замещение, сопутствующие расходы), сопоставление с бюджетом, проверка Zielvereinbarung (§ 29 Abs. 4 SGB IX); результаты предварительные [3];
  - `sozialrecht-manager`: точка входа плагина: относит запрос к подходящему скиллу, сначала проверяет связанные коннекторы правовых источников и соблюдает порядок Frist → Analyse → Entwurf → Zitate-Gate → Freigabe [3];
  - `widerspruch`: черновик Widerspruch против Bescheid (SGB IX/XII): fristwahrende Kurzfassung и begründete Fassung по шаблону плагина; обязательная проверка через zitate-gate перед отправкой [3];
  - `zitate-gate`: проверка цитат перед отправкой: существование норм и решений через Zitierfest, содержание и редакция через nu:legal, актуальность; затем атака со стороны противной стороны и scorecard [3].

## Чем выделяется
- Заявляет, что источники берутся из коннекторов, а не из памяти модели [2].
- Мнение: связка расчёта сроков по саксонским праздникам с проверкой цитат через внешние базы снижает риск ошибок в сроках и ссылках.

## Ограничения и риски
- Версия 0.1.1 по манифесту [2].
- Zitate-Gate проверяет нормы и решения через коннекторы nu:legal и Zitierfest [2].
- нет данных о поведении плагина при недоступном коннекторе.
- Выдержка не описывает, какие данные уходят наружу при анализе Bescheid; класс данных не подтверждён [2].
- Ориентирован на Саксонию и социальное право (SGB IX и XII); другие отрасли выдержка не описывает [2].

## Когда не подходит
- Мнение: если дело относится к другой федеральной земле, саксонские праздники и ориентация на саксонскую практику не подойдут.
- Вопросы вне социального права (вне SGB IX и XII): описание плагина их не охватывает [2].

## Альтернативы
- [[legal-domain-manager]] — оркестратор для немецкого социального права: по описанию карточки ведёт дело от Bescheid до Klage и координирует скиллы сроков, анализа документов и шаблонов.
- [[court-document-analyzer]] — скилл для анализа немецких судебных документов и Bescheid: факты, сроки, аргументы, слабые места и контрстратегии, по описанию карточки.
- [[zitierfest]] — коннектор с официальным текстом немецких норм и решений с Fundstelle и проверкой цитат, по описанию карточки.

## Источники
1. Инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/inventory.json
2. Манифест плагина: название, версия, описание (начало файла), снимок 2026-11-10, сверка не проводилась — raw://evidence/sozialrecht-sachsen.md
3. Описания скиллов плагина (поле description из файлов скиллов, дословно), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/evidence/plugin-sozialrecht-sachsen-skills.txt

## Заявлено автором
Описание из манифеста [2] (фрагмент, дословно):
> Sozialrechtliche Praxis in Sachsen (SGB IX/XII, Persönliches Budget, Eingliederungshilfe, Hilfe zur Pflege)

Поле platform_description записи инвентаря [1], дословно:
> 7 скиллов по социальному праву Саксонии: анализ Bescheid, сроки, Widerspruch, Klage, персональный бюджет, проверка цитат

Пометка: обе цитаты — описание поставщика и каталога, а не проверенный факт; сверка не проводилась.
