<!-- Выдержки первоисточников для карточки nu-legal. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "nu-legal", "kind": "connector", "cluster": "11-law-de-eu", "group": "нормы и история редакций", "name": "nu:legal Deutsches Recht", "vendor": "nu:legal", "state": "connected", "platform_description": "", "source": "ListConnectors"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[nu-legal] инструменты (префикс mcp__nu_legal_Deutsches_Recht__): getChanges, getCoverage, getNorm, get_lawyer, listCasePassages, listCitedAuthorities, listCitingDecisions, listNormVersions, resolveIdentifiers, search, search_lawyers
````

## [3] системные инструкции MCP-сервера (сессия 2026-11-10)
- Снимок: 2026-11-10
- Фрагмент:

````text
### nu:legal
nu:legal Deutsches Recht (recht.nulegal.eu): German federal statutes and case law, EU law (520 acts in force, plus 5 international treaties) and the Landesrecht of Bayern, Brandenburg, Hessen, Nordrhein-Westfalen and Sachsen (laws per Land: Bayern 935 laws; Brandenburg 1,882 laws; Hessen 509 laws; Nordrhein-Westfalen 1,505 laws; Sachsen 1,024 laws; `getCoverage` has every count; Hessen: in part, the laws whose text the site publishes, rebuilt from the gazette). Read-only, free, no key.
Two limits: a version date is often the day a text was first seen here (the archive starts 2019-06-10), not its Inkrafttreten; each version's `date_basis` says which.
The decision-to-norm citation graph is built over every decision held, federal, Land and EU courts alike (5,976,204 edges). It links federal, EU and Land provisions (Bayern, Brandenburg, Nordrhein-Westfalen and Sachsen). It does not link Hessen provisions, so a zero there means not indexed, not that no court has cited it; `coverage` says which.
A miss says what to try next under `next`. Please name the source when you quote: "Source: nu:legal – recht.nulegal.eu" (CC BY 4.0). Use for AI training is reserved (Section 44b UrhG).
- a lawyer in Germany: search_lawyers {"city": "München", "area": "Arbeitsrecht"} (English works too: "Munich", "employment law", "Turkish"), then get_lawyer {"id": ...}. Report only values present in the result; never fill a null.
````
