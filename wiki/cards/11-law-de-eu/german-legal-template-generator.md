---
id: "german-legal-template-generator"
title: "german-legal-template-generator"
kind: "skill"
vendor: "уточнить"
cluster: "11-law-de-eu"
group: "процессы по делу"
summary: "Скилл шаблонов по немецкому социальному праву: Widerspruch, Klage и заявления на персональный бюджет на DE, RU и EN."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: ["de", "en", "ru"]
jurisdiction: "DE"
source_urls: ["raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["шаблоны", "Vorlagen", "template", "Widerspruch", "Klage", "персональный бюджет", "persönliches Budget", "SGB IX", "SGB XII", "Eilantrag"]
---

# german-legal-template-generator

## Суть
- Скилл генерирует шаблоны документов по немецкому социальному праву (SGB IX, SGB XII): заявления, возражения, иски и расчёты компенсаций [2].
- Работает на DE, RU и EN и формирует ссылки на нормы автоматически [2].
- В сессии скилл в состоянии enabled [1].

## Для чего
- Заявления: персональный бюджет (§29 SGB IX), Teilhabeleistungen, повышение уровня ухода (Pflegegraderhöhung), Wohngeld, Kindergeld [2].
- Возражения и иски: Widerspruch, Klage vor Sozialgericht, Eilantrag (einstweilige Anordnung), Berufung [2].
- Расчёты: ретроактивные выплаты, сроки Verjährung и проценты по §44 SGB I [2].
- нет данных о целевой аудитории инструмента.

## Возможности
- Шаблон заявления на персональный бюджет по §29 SGB IX [2].
- Для Widerspruch указан срок один месяц [2].
- Срок Verjährung для социальных пособий — 4 года [2].
- Расчёт процентов по §44 SGB I [2].
- Ссылки на SGB IX, SGB XII, SGB I, BGB и SGB X [2].

## Чем выделяется
- Объединяет заявления, возражения, иски и расчёты в одном скилле [2].
- Мнение: многоязычные шаблоны удобны для работы с немецкими ведомствами, но ссылки на нормы перед отправкой стоит сверить с первоисточником.

## Ограничения и риски
- Шаблоны описаны для немецкого социального права; другие отрасли выдержка не описывает [2].
- Ссылки на нормы формируются автоматически; выдержка не описывает, как они проверяются [2].
- Выдержка не описывает, куда передаются введённые данные заявителя; класс данных не подтверждён [2].

## Когда не подходит
- Мнение: шаблон не заменяет оценку конкретного случая юристом.
- Документы вне перечисленных видов: выдержка их не описывает [2].

## Альтернативы
- [[german-legal-deadline-calculator]] — расчёт сроков Widerspruch и Klage по правилам.
- [[court-document-analyzer]] — разбор полученного решения, а не составление ответа.
- [[sozialrecht-sachsen]] — плагин для Саксонии с черновиками Widerspruch и Klage.

## Источники
1. Инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/inventory.json
2. Локальный файл скилла (начало), снимок 2026-11-10, сверка не проводилась — raw://evidence/german-legal-template-generator.md

## Заявлено автором
> Шаблоны по социальному праву: Widerspruch, Klage, заявления на персональный бюджет (DE, RU, EN)
