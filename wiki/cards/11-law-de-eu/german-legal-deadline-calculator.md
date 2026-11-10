---
id: "german-legal-deadline-calculator"
title: "german-legal-deadline-calculator"
kind: "skill"
vendor: "уточнить"
cluster: "11-law-de-eu"
group: "сроки и расчёты"
summary: "Скилл расчёта сроков немецких процессов (Widerspruch, Klage, Verjährung) с учётом выходных и праздников; сверка с текстом норм нашла ошибки в примерах и в части правил."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: ["de", "en"]
jurisdiction: "DE"
source_urls: ["raw://session/2026-11-10/inventory.json", "raw://evidence/german-legal-deadline-calculator.md", "raw://session/2026-11-10/evidence/nulegal-normtexte.txt", "https://recht.nulegal.eu"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["сроки", "Fristen", "Frist", "Widerspruchsfrist", "Klagefrist", "Verjährung", "Fristwahrung", "выходные и праздники", "Sonnabend", "Zustellung", "Bekanntgabe", "Wiedereinsetzung", "BGB", "SGG", "SGB X", "SGB I"]
---

# german-legal-deadline-calculator

## Суть
- Скилл рассчитывает сроки немецких процессов (Widerspruch, Klage, Verjährung) с учётом выходных и праздников и даёт рекомендации по запасу времени [2].
- Заявлена специализация на немецком социальном праве (SGG, SGB, BGB) [2].
- В сессии скилл включён [1].
- Сверка с текстом норм (nu:legal, снимок 2026-11-10) нашла в примерах скилла и в части правил расхождения; см. раздел Ограничения и риски [2][8][9][11][18][19].

## Для чего
- Расчёт сроков Widerspruch, Klage и Verjährung [1][2].
- Проверка соблюдения срока (Fristwahrung) и запас времени до его окончания [2].
- Группа инвентаря: сроки и расчёты [1].
- нет данных о целевой аудитории скилла.

## Возможности
- Начало срока: день события не засчитывается [2]. По тексту §187 Abs. 1 BGB день события не засчитывается [8]; если начало дня является моментом начала срока, этот день засчитывается (§187 Abs. 2 BGB) [8]. Исключение для событий в полночь скилл называет [2].
- Месячный срок: конец приходится на тот же номер дня следующего месяца, со ссылкой на §188 Abs. 2 BGB [2]. По тексту номер дня берётся от дня, в который пришлось событие [9]; для сроков SGG то же правило в §64 Abs. 2 SGG [11].
- Перенос срока с выходного или праздничного дня: скилл ссылается на §193 BGB [2][3]. По тексту §193 BGB относится к Willenserklärung und Leistung и учитывает праздник по месту совершения действия [10]. Для сроков SGG перенос дан в §64 Abs. 3 SGG: Sonntag, gesetzlicher Feiertag или Sonnabend переносят конец срока на следующий Werktag [11].
- Сроки судебного процесса: скилл приводит Widerspruch — месяц от Bekanntgabe, Klage — месяц от Widerspruchsbescheid, Berufung — месяц, если она допустима, Revision — месяц [2]. По тексту: Widerspruch — месяц после Bekanntgabe Verwaltungsakt (§84 Abs. 1 SGG) [12]; Klage — месяц после Bekanntgabe Verwaltungsakt, а при Vorverfahren от Bekanntgabe Widerspruchsbescheid (§87 Abs. 1–2 SGG) [13]; Berufung — месяц после Zustellung Urteils (§151 Abs. 1 SGG) [14]; Revision — месяц после Zustellung Urteils или Beschlusses über die Zulassung (§164 Abs. 1 SGG) [15]. §222 ZPO, названный скиллом [2], в выдержках не приведён: нет данных.
- Праздники: перечень федеральных праздников и две записи для Саксонии, Fronleichnam отмечен как региональный [3]. Полнота перечня и закон о праздниках земли в выдержках не проверялись: нет данных.
- Расчёт по месяцам и по дням: два алгоритма, второй с примером по §569 BGB [4]. Текста §569 BGB в выдержках нет: нет данных.
- Verjährung социальных пособий: четыре года, §45 SGB I [2][7]. По тексту: четыре года после окончания календарного года, в котором требование возникло [21].
- Способы соблюдения срока (Fristwahrung): личная подача, почта, Einschreiben, факс до 24:00, DE-Mail, почтовый ящик суда [6]. Эти способы по текстам снимка не проверены: нет данных.
- Правила Bekanntgabe по почте и Wiedereinsetzung описаны со ссылками, которые сверены ниже в разделе Ограничения и риски [6][7].
- нет данных о разделах скилла (многоэтапная шкала, система предупреждений, шаблон отчёта): в выдержках они не приведены.

## Чем выделяется
- Описание скилла заявляет точные расчёты с учётом выходных и праздников [2].
- Мнение: полезна пошаговая структура расчёта (событие, начало, конец, перенос, запас), но результаты без сверки с текстом норм использовать нельзя: сверка дала расхождения.
- Мнение: ссылки на §187, §188 и §193 BGB в каждом шаге полезны для проверки, если сами нормы сверяются с текстом.

## Ограничения и риски
- Месячный срок в примере скилла: событие 15.01.2026 и срок до 16.02.2026 [4]. Вычисление: 15.01.2026 — по календарю четверг, в примере названа среда. По §188 Abs. 2 BGB [9] и §64 Abs. 2 SGG [11] срок истекает с окончанием 15.02.2026. Это воскресенье, поэтому по §64 Abs. 3 SGG срок переходит на понедельник 16.02.2026 [11]. Итог совпадает, а обоснование в примере другое.
- Метод скилла считает номер дня от дня после события [4]. Вычисление по тексту: событие в понедельник 19.01.2026 даёт срок до четверга 19.02.2026 [9][11]; по методу скилла — до пятницы 20.02.2026, то есть на день позже.
- Почтовый пример скилла [6]: отправка 10.01.2026, доставка 13.01.2026 со ссылкой на §41 Abs. 2 SGB X. §41 SGB X называется «Heilung von Verfahrens- und Formfehlern» [19]; почтовая фикция содержится в §37 Abs. 2 SGB X: письмо считается доставленным на четвёртый день после сдачи на почту [18], то есть 14.01.2026. Фикция не действует, если письмо не дошло или дошло позже; в сомнении доказывает получение орган [18]. Конец срока 14.02.2026 — суббота; по §64 Abs. 3 SGG срок переходит на понедельник 16.02.2026 [11] (вычисление). Скилл даёт 14.02.2026 и не применяет собственное правило выходных [3][6].
- Начало срока от Bekanntgabe: §64 Abs. 1 SGG называет день после Zustellung, Eröffnung или Verkündung [11]; норма о первом дне срока от Bekanntgabe (§84 Abs. 1, §87 Abs. 1 SGG) в выдержках не приведена. Скилл берёт §187 Abs. 1 BGB [2][8]; применимость этой нормы к срокам SGG в выдержках не проверена: нет данных.
- Berufung и Revision: скилл пишет from Urteil и from Berufungsurteil [2]. По тексту срок Berufung идёт от Zustellung Urteils (§151 Abs. 1 SGG) [14]. Для Revision срок идёт от Zustellung Urteils или Beschlusses über die Zulassung (§164 Abs. 1 SGG) [15]; Begründungsfrist — два месяца (§164 Abs. 2 SGG) [15], которую скилл не называет.
- Klage: скилл пишет from Widerspruchsbescheid [2]; по §87 Abs. 2 SGG срок идёт от Bekanntgabe des Widerspruchsbescheids [13]. При Bekanntgabe im Ausland срок составляет три месяца, при öffentlicher Bekanntgabe — ein Jahr [13]; этих случаев скилл не описывает.
- Таблица кратких сроков [7] ссылается на §160 SGG для Revision; срок Revision задан в §164 Abs. 1 SGG [15]. Для Berufung указаны §143 SGG и условие If >750€ dispute: по выдержкам не проверено, нет данных.
- Verjährung [2][5][21]: начало с 31.12 года возникновения совпадает с §45 Abs. 1 SGB I [21]; пример 2020 → 31.12.2024 [2] тоже совпадает. Вариант «4 years from knowledge» (пример 2023 → 2027-12-31) [5] в тексте §45 Abs. 1–2 SGB I опоры не находит [21]. Фраза «If Bescheid issued, clock resets» [2] описывает не сброс срока: по §45 Abs. 3 SGB I срок приостанавливается (Hemmung) подачей Antrag или Widerspruch и продолжается через шесть месяцев после Bekanntgabe решения [21]. Neubeginn — по BGB sinngemäß (§45 Abs. 2 SGB I) [21]; норм BGB о Neubeginn в выдержках нет: нет данных.
- Wiedereinsetzung [6][7]: скилл ссылается на §67 SGB X, два недели и максимум шесть месяцев. §67 SGB X называется «Begriffsbestimmungen» [20], Wiedereinsetzung в нём не регулируется. Wiedereinsetzung в SGB X — §27: два недели после устранения препятствия и предельный срок один год [17]. В SGG — §67: один месяц после устранения препятствия и предельный срок один год [16]. Срок в шесть месяцев в текстах не найден. Оценка успешности около 20 % в выдержках не подтверждена: нет данных.
- Праздники: §193 BGB учитывает праздник по месту совершения действия [10]; §64 Abs. 3 SGG говорит о gesetzlichem Feiertag [11]. В перечне скилла Reformationstag не назван [3]; закон о праздниках Саксонии в выдержках не приведён: нет данных. Даты перечня записаны в порядке месяц.день (например, Tag der Arbeit: 05.01), а даты примеров — день.месяц.год [3][4]: это легко перепутать.
- Скилл называет §193 BGB общим правилом переноса срока [2][3]. По тексту §193 BGB касается Willenserklärung und Leistung [10]. Мнение: для сроков SGG ориентироваться на перенос по §64 Abs. 3 SGG [11].
- Способы подачи и рекомендация трёхдневного запаса [6] по выдержкам не проверены: нет данных; запас — рекомендация скилла.
- Версии норм: nu:legal показывает дату первого наблюдения, а не дату вступления в силу: §84 SGG — 2024-01-03 [12]; §37 SGB X — 2025-12-31 [18]; для большинства норм дата начала архива 2019-06-10 [8]. Сверка с Bundesgesetzblatt не проводилась, статус draft.
- Выдержка не описывает, какие данные передаются при расчёте; класс данных не подтверждён [2]. Нет данных о цене, лимитах и поставщике.

## Когда не подходит
- Мнение: если дата события (Zustellung, Bekanntgabe, Verkündung) неясна по документам, расчёт не заменяет проверку документов [11][12].
- Мнение: если Bekanntgabe была за границей или публичной, пример скилла таких случаев не охватывает [13][18].
- Мнение: если срок связан с праздником другой земли, перечень скилла не подходит без закона этой земли [3][10].
- Процессы вне Германии: выдержка описывает только немецкие процессы [2].

## Альтернативы
- [[lulius]] — калькуляторы сроков и расходов в коннекторе федерального права; описание см. в карточке.
- [[sozialrecht-sachsen]] — плагин из семи скиллов по социальному праву Саксонии, в состав которого входит расчёт сроков с саксонскими праздниками; состав см. в карточке.
- [[court-document-analyzer]] — скилл для немецких судебных документов и Bescheid: по описанию карточки извлекает факты и сроки из текста документа.

## Источники
1. Инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления), снимок 2026-11-10, сверка не проводилась — raw://session/2026-11-10/inventory.json
2. Локальный файл скилла SKILL.md, начало (раздел 1: общие правила, сроки судебного процесса, Verjährung), снимок 2026-11-10, сверка не проводилась — raw://evidence/german-legal-deadline-calculator.md
3. Локальный файл скилла, раздел 2: праздники и правило выходных, снимок 2026-11-10 — raw://evidence/german-legal-deadline-calculator.md
4. Локальный файл скилла, раздел 3, A–B: расчёт по месяцам и по дням, с примерами — raw://evidence/german-legal-deadline-calculator.md
5. Локальный файл скилла, раздел 3, C: долгосрочная Verjährung — raw://evidence/german-legal-deadline-calculator.md
6. Локальный файл скилла, раздел 4: Fristwahrung, Bekanntgabe, Wiedereinsetzung — raw://evidence/german-legal-deadline-calculator.md
7. Локальный файл скилла, раздел 8: сводная таблица сроков — raw://evidence/german-legal-deadline-calculator.md
8. § 187 BGB, текст nu:legal, снимок 2026-11-10 — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
9. § 188 BGB, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
10. § 193 BGB, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
11. § 64 SGG, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
12. § 84 SGG, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
13. § 87 SGG, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
14. § 151 SGG, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
15. § 164 SGG, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
16. § 67 SGG, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
17. § 27 SGB X, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
18. § 37 SGB X, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
19. § 41 SGB X, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
20. § 67 SGB X, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt
21. § 45 SGB I, текст nu:legal — raw://session/2026-11-10/evidence/nulegal-normtexte.txt

Пункты 8–21: источник nu:legal – recht.nulegal.eu (CC BY 4.0), https://recht.nulegal.eu; тексты неофициальные (nicht-amtliche Lesefassung), сверка с Bundesgesetzblatt не проводилась.

## Заявлено автором
Поле platform_description записи инвентаря [1], дословно (заявление автора, не проверенный факт):
> Расчёт сроков в немецких процессах (Widerspruch, Klage, Verjährung) с учётом выходных и праздников

Первое предложение описания в файле скилла [2], дословно (заявление автора):
> Precise deadline calculations for German legal proceedings (Widerspruch, Klage, Verjährung) with automatic exclusion of weekends/holidays, Fristwahrung rules, and safety margin recommendations.
