<!-- Выдержки первоисточников для карточки sozialrecht-sachsen. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "sozialrecht-sachsen", "kind": "plugin", "cluster": "11-law-de-eu", "group": "процессы по делу", "name": "sozialrecht-sachsen", "vendor": "уточнить", "state": "enabled", "platform_description": "7 скиллов по социальному праву Саксонии: анализ Bescheid, сроки, Widerspruch, Klage, персональный бюджет, проверка цитат", "source": "список скиллов сессии"},
````

## [2] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "sozialrecht-sachsen",
  "displayName": "Sozialrecht Sachsen",
  "version": "0.1.1",
  "description": "Sozialrechtliche Praxis in Sachsen (SGB IX/XII, Persönliches Budget, Eingliederungshilfe, Hilfe zur Pflege): deterministischer Fristenrechner mit sächsischen Feiertagen, Bescheid-Analyse, Widerspruch- und Klage-Entwürfe, Kostenrechner Arbeitgebermodell und ein Zitate-Gate, das jede Norm und Entscheidung vor dem Versand über die Konnektoren nu:legal und Zitierfest prüft. Quellen kommen aus Konnektoren, nie aus dem Gedächtnis.",
  "author": {
    "name": "Max (svend4)",
    "url": "https://github.com/svend4"
  },
  "homepage": "https://github.com/svend4/sozialrecht-sachsen",
  "repository": "https://github.com/svend4/sozialrecht-sachsen",
  "license": "Apache-2.0",
  "keywords": [
    "sozialrecht",
    "sgb-ix",
    "sgb-xii",
    "persoenliches-budget",
    "eingliederungshilfe",
    "sozialgericht",
    "fristen",
    "widerspruch",
    "sachsen",
    "zitate-gate"
  ],
  "privacyPolicyUrl": "https://github.com/svend4/sozialrecht-sachsen/blob/main/DATENSCHUTZ.md",
  "icon": "./.claude-plugin/icon.png"
}
````
