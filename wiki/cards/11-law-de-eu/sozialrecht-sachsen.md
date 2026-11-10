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
source_urls: ["https://github.com/svend4/sozialrecht-sachsen", "raw://session/2026-11-10/inventory.json"]
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
- нет данных о целевой аудитории инструмента.

## Возможности
- Детерминированный расчёт сроков с саксонскими праздниками [2].
- Анализ Bescheid [2].
- Черновики Widerspruch и Klage [2].
- Калькулятор расходов модели работодателя (Arbeitgebermodell) [2].
- Zitate-Gate: каждая норма и решение проверяются через коннекторы nu:legal и Zitierfest перед отправкой [2].
- Источники для проверок берутся из подключённых коннекторов, а не из памяти модели [2].

## Чем выделяется
- Заявляет, что источники берутся из коннекторов, а не из памяти модели [2].
- Мнение: связка расчёта сроков по саксонским праздникам с проверкой цитат через внешние базы снижает риск ошибок в сроках и ссылках.

## Ограничения и риски
- Версия 0.1.1 по манифесту; лицензия Apache-2.0 [2].
- Качество проверки цитат зависит от подключённых коннекторов nu:legal и Zitierfest [2].
- Выдержка не описывает, какие данные уходят наружу при анализе Bescheid; класс данных не подтверждён [2].
- Ориентирован на Саксонию и социальное право (SGB IX и XII); другие отрасли выдержка не описывает [2].

## Когда не подходит
- Мнение: если дело относится к другой федеральной земле, саксонские праздники и практика не подойдут.
- Вопросы вне социального права (вне SGB IX и XII) выдержка не описывает [2].

## Альтернативы
- [[legal-domain-manager]] — общий оркестратор для немецкого социального права (SGG, SGB IX/XII).
- [[court-document-analyzer]] — анализ судебных документов и Bescheid как отдельный скилл.
- [[zitierfest]] — официальный текст норм и решений для проверки цитат.

## Источники
1. Инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/inventory.json
2. Манифест плагина (начало файла), снимок 2026-11-10, сверка не проводилась — https://github.com/svend4/sozialrecht-sachsen

## Заявлено автором
> Манифест: «Sozialrechtliche Praxis in Sachsen (SGB IX/XII, Persönliches Budget, Eingliederungshilfe, Hilfe zur Pflege)»
> 7 скиллов по социальному праву Саксонии: анализ Bescheid, сроки, Widerspruch, Klage, персональный бюджет, проверка цитат
