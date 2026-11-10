<!-- Выдержки первоисточников для карточки sozialrecht-sachsen. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "sozialrecht-sachsen", "kind": "plugin", "cluster": "11-law-de-eu", "group": "процессы по делу", "name": "sozialrecht-sachsen", "vendor": "уточнить", "state": "enabled", "platform_description": "7 скиллов по социальному праву Саксонии: анализ Bescheid, сроки, Widerspruch, Klage, персональный бюджет, проверка цитат", "source": "список скиллов сессии"},
````

## [2] манифест плагина: название, версия, описание (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "sozialrecht-sachsen",
  "displayName": "Sozialrecht Sachsen",
  "version": "0.1.1",
  "description": "Sozialrechtliche Praxis in Sachsen (SGB IX/XII, Persönliches Budget, Eingliederungshilfe, Hilfe zur Pflege): deterministischer Fristenrechner mit sächsischen Feiertagen, Bescheid-Analyse, Widerspruch- und Klage-Entwürfe, Kostenrechner Arbeitgebermodell und ein Zitate-Gate, das jede Norm und Entscheidung vor dem Versand über die Konnektoren nu:legal und Zitierfest prüft. Quellen kommen aus Konnektoren, nie aus dem Gedächtnis.",
````

## [3] описания скиллов плагина (поле description из файлов скиллов)
- Снимок: 2026-11-10
- Фрагмент:

````text
sozialrecht-sachsen:bescheid-analyse: Bescheid, Widerspruchsbescheid oder Schreiben eines Leistungsträgers (SGB IX/XII, Eingliederungshilfe, Persönliches Budget, Hilfe zur Pflege) strukturiert auswerten – Verfügungssatz, Rechtsgrundlagen, Fristen, Begründungslücken, fehlende Unterlagen, Angriffspunkte, nächste Schritte. Pseudonymisierung zuerst. Use when a Bescheid is pasted or attached, or on "analysiere den Bescheid", "was steht da drin", "worauf kann ich mich stützen", "разбери решение ведомства", "analyze this decision".
sozialrecht-sachsen:fristen: Fristen im sozialrechtlichen Verfahren deterministisch berechnen (Widerspruch § 84 SGG, Klage § 87 SGG, Berufung § 151 SGG, Jahresfrist § 66 Abs. 2 SGG) mit Bekanntgabefiktion § 37 Abs. 2 SGB X (vierter Tag), § 64 SGG und den gesetzlichen Feiertagen Sachsens (Buß- und Bettag, Reformationsfest). Immer das Skript scripts/fristen.py ausführen, nie im Kopf rechnen. Use when the user asks about a Frist, Fristende, Widerspruchsfrist, Klagefrist, Bekanntgabe, Zustellung, "bis wann", "срок обжалования", "рассчитай срок", "deadline for Widerspruch".
sozialrecht-sachsen:klage: Klage zum Sozialgericht (Anfechtungs-, Verpflichtungs-, Leistungsklage, §§ 54, 56 SGG) gegen einen Widerspruchsbescheid entwerfen – fristwahrende Klageschrift und Begründung aus references/vorlagen/klage.md, Prozessstation SG Dresden / Sächsisches LSG, Pflichtdurchlauf zitate-gate. Use on "Klage erheben", "Klageschrift", "zum Sozialgericht", "подать иск в социальный суд", "file a claim with the Sozialgericht".
sozialrecht-sachsen:persoenliches-budget: Persönliches Budget (§ 29 SGB IX) vorbereiten – Bedarfsermittlung strukturieren (§ 13 SGB IX, Lebensbereiche, Stundenplan), Arbeitgebermodell-Kosten mit scripts/budget.py rechnen (Lohn, Arbeitgeberanteile, Vertretung, Nebenkosten), Gegenüberstellung zum bewilligten Budget, Zielvereinbarung (§ 29 Abs. 4 SGB IX) prüfen. Ergebnisse sind vorläufig. Use on "Persönliches Budget", "Arbeitgebermodell", "Assistenzstunden", "Budget zu niedrig", "Zielvereinbarung", "персональный бюджет", "personal budget calculation".
sozialrecht-sachsen:sozialrecht-manager: Einstieg und Lotse des Plugins sozialrecht-sachsen – ordnet ein Anliegen (Bescheid erhalten, Frist, Widerspruch, Klage, Persönliches Budget, Zitate prüfen) dem passenden Skill zu, prüft zuerst die verbundenen Rechtsquellen-Konnektoren und hält die Reihenfolge ein (Frist → Analyse → Entwurf → Zitate-Gate → Freigabe). Use on general requests like "ich habe einen Bescheid bekommen", "was tun", "Hilfe mit SGB IX", "wie gehe ich vor", "что делать с решением", "help with a German social law decision", or when unsure which skill fits.
sozialrecht-sachsen:widerspruch: Widerspruch gegen einen Bescheid im Sozialrecht (SGB IX/XII) entwerfen – fristwahrende Kurzfassung und begründete Fassung aus der Vorlage references/vorlagen/widerspruch.md, mit Pflichtdurchlauf durch zitate-gate vor dem Versand. Use on "Widerspruch schreiben", "Widerspruch einlegen", "Entwurf Widerspruch", "составь возражение", "draft an objection against the Bescheid".
sozialrecht-sachsen:zitate-gate: Citation-Gate für ausgehende Schriftsätze im Sozialrecht – jede Norm und Entscheidung vor dem Versand in drei Schritten prüfen (Existenz über Zitierfest, Inhalt und Stand über nu:legal, Aktualität), dann Angriff der Gegenseite und Scorecard. Use before any Widerspruch, Klage, Antrag or Stellungnahme leaves the practice; on "prüfe die Zitate", "Fundstellen prüfen", "stimmen die Paragraphen", "проверь ссылки на нормы", "citation check", "ist das versandfertig".
````
