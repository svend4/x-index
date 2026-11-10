---
id: "zitierfest"
title: "Zitierfest"
kind: "connector"
vendor: "уточнить"
cluster: "11-law-de-eu"
group: "проверка цитат"
summary: "Коннектор Zitierfest: официальный текст немецких норм и решений с Fundstelle, проверка цитат и расчёт гебюр."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "unknown"
hosting: "unknown"
hosted: true
languages: ["de"]
jurisdiction: "DE"
source_urls: ["raw://session/2026-11-10/inventory.json", "raw://session/2026-11-10/tools-by-server.txt", "raw://session/2026-11-10/evidence/mcp-instructions.txt"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Zitierfest", "цитаты", "Zitat", "Fundstelle", "Stand der Fassung", "RVG", "GKG", "Gebühren", "гебюры", "Германия"]
curator_hint: "test"
---

# Zitierfest

## Суть
- Коннектор Zitierfest отдаёт официальный текст немецких норм и решений с Fundstelle и датой состояния редакции [3].
- Есть проверка цитат и расчёт гебюр по RVG, GKG, FamGKG, GNotKG и JVEG [2][3].
- В сессии коннектор подключён [1]; hosted: true выведено по [2]: инструменты MCP-сервера (префикс mcp__Zitierfest__).

## Для чего
- Проверка цитаты (инструмент `zitate_pruefen`) [2].
- Получение текста нормы или решения с Fundstelle для ссылки [3].
- Расчёт гебюр и судебных расходов по тарифам (`gebuehr_berechnen`, `gebuehren_verzeichnis`) [2][3].
- Группа инвентаря: «проверка цитат» [1].
- нет данных о целевой аудитории инструмента.

## Возможности
- Инструменты в сессии: `gesetze_finden`, `gesetz`, `normen`, `stand`, `suche`, `urteile`, `verweise`, `zitate_pruefen`, `gebuehr_berechnen`, `gebuehren_verzeichnis` [2].
- Охват 30 622 законов и постановлений: федеральное право, право земель (в том числе баварское), право ЕС, международные договоры, BRAK-Berufsrecht, тарифные договоры öD (неофициальные), муниципальное право (München, Regensburg, Beratzhausen) [3].
- Решения BGH и GmS-OGB с 2000 года; BAG, BFH, BSG, BPatG и BVerfG с 2010 года; EuGH с 1954 года [3].
- Гебюры по RVG, GKG, FamGKG, GNotKG и JVEG [3].

## Чем выделяется
- Мнение: проверка цитат удобна, когда нужно сверить цитату с официальным текстом нормы или решения с Fundstelle [3].
- Охват решений начинается с 1954 года для EuGH и с 2000 года для BGH и GmS-OGB [3].

## Ограничения и риски
- Охват решений зависит от суда и периода: Eingangsgerichte Bayern с 2021 года, Eingangsgerichte Brandenburg с 2001 года, а раздел «Eingangsgerichte NRW im Aufbau (urteile)» находится в стадии создания [3].
- Комментариев к нормам нет: в описании сервиса указано «keine Kommentierung» [3].
- Выдержки не описывают, какие данные уходят при вызове инструментов; класс данных не подтверждён [2][3].

## Когда не подходит
- Толкование норм и комментарии: сервис их не даёт [3].
- Мнение: если нужного суда или земли нет в перечне охвата, сверяйтесь с другим сервисом, например [[nu-legal]].

## Альтернативы
- [[nu-legal]] — право земель, история редакций норм и граф ссылок от решений к нормам.
- [[lulius]] — федеральное право, федеральные суды и калькуляторы сроков и расходов.
- [[verification-foundation]] — набор скиллов для проверки цитат в ответах ИИ.

## Источники
1. Инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/inventory.json
2. Список инструментов, загруженных в сессию, снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/tools-by-server.txt
3. Системные инструкции MCP-сервера (сессия 2026-11-10), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/evidence/mcp-instructions.txt

## Заявлено автором
> В каталоге описание отсутствует.
> Инструкции сервера: «Zitierfest liefert den amtlichen Wortlaut deutscher Normen und Entscheidungen mit Fundstelle und Stand der Fassung.»

Пометка: вторая строка — инструкции MCP-сервера [3], не проверены по первоисточнику; поле platform_description инвентаря [1] пустое.
