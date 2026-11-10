# Замер поиска по карточкам

Дата: 2026-11-10. Вопросов: 93. Глубина выдачи: 10. Карточек в индексе: 1607.

## Сводка

| режим | вопросов | hit@k | recall@k | MRR | запрещённые в топ-3 |
|---|---:|---:|---:|---:|---:|
| and | 93 | 0.11 | 0.08 | 0.10 | 0.00 |
| or | 93 | 0.80 | 0.72 | 0.66 | 0.18 |
| fallback | 93 | 0.80 | 0.72 | 0.66 | 0.18 |

## По доменам (режим fallback)

| домен | вопросов | hit@k | MRR |
|---|---:|---:|---:|
| автоматизация | 12 | 0.75 | 0.62 |
| документы-таблицы | 12 | 1.00 | 0.89 |
| комплаенс-медицина-данные | 11 | 0.91 | 0.76 |
| память-знания | 12 | 0.75 | 0.65 |
| почта-календарь-встречи | 12 | 0.75 | 0.62 |
| право-фрг-еэс | 10 | 0.70 | 0.52 |
| право-фрг-социальное | 12 | 0.92 | 0.72 |
| счета-бухгалтерия | 12 | 0.58 | 0.46 |

## Промахи (режим fallback): ожидаемой карточки нет в выдаче

| qid | вопрос | ожидалось | в выдаче (топ-5) |
|---|---|---|---|
| Q008 | § 84 SGG Wortlaut nachschlagen | lulius, mcp-io-github-pipeworx-io-de-gesetze, nu-legal | german-legal-deadline-calculator, sozialrecht-sachsen, mcp-dev-infranode-infranode, legal-domain-manager, zitierfest |
| Q014 | Как найти федеральный закон по официальной аббревиатуре вроде SGB IX — есть ли поиск по Kürzel? | mcp-io-github-pipeworx-io-de-gesetze, zitierfest | midpage-legal-research, sozialrecht-sachsen, german-legal-template-generator, nu-legal, harvey |
| Q016 | Где искать решения EuGH по Vorabentscheidungsersuchen, а не только тексты регламентов? | mcp-io-github-cyanheads-eur-lex-mcp-server, mcp-io-github-lex-api-lexapi-mcp | zitierfest, lulius, nu-legal, ecosystem-curator, eu-ai-act-mcp |
| Q022 | EU regulation, Fassung am Stichtag | mcp-io-github-lex-api-lexapi-mcp, mcp-io-github-sfhajji-lex | mcp-eu-ansvar-eu-regulations, mcp-eu-ansvar-gateway, amplitude-eu, mcp-io-github-evidinvest-aether-developer, zitierfest |
| Q029 | Wie lese ich Lieferantenrechnungen aus PDF-Dateien für die Buchhaltung aus? | mcp-io-github-antondrakon-duebuddy-invoices, mcp-io-github-fashionmascherine-svg-document-to-json-mcp | mcp-io-github-pipeworx-io-ip-australia, mcp-io-github-mastalier1997-austria-property, mcp-io-github-cyanheads-ris-austria-mcp-server, mcp-io-github-mcp-dir-sancoes-australia-mcp, mcp-au-com-aiframework-australian-ai-governance-framework |
| Q030 | Bankauszug in Buchungssätze umwandeln | mcp-io-github-arceedev-contabridge-mcp | — |
| Q031 | Welche Software taugt für Buchhaltung und Steuern in europäischen Kleinunternehmen? | mcp-finance-norman-mcp-server | mcp-com-shaftware-componecat, mcp-co-chinaready-search, mcp-io-github-cognitive-emergence-prooftask, mcp-io-github-mcp-dir-astrea-mcp, mcp-com-thedailyworkflow-thedailyworkflow-mcp |
| Q032 | Verzugszinsen Mahnung offene Rechnungen | mcp-com-pagofix-pagofix | mcp-de-zugferd-validator-validator, mcp-app-apiguru-amazon-data, mcp-io-github-diogoup26-mcp-x402, mcp-com-compsapi-ebay-sold-listings, german-legal-deadline-calculator |
| Q033 | Rechnungen und Beiträge eines e.V. verwalten | mcp-io-github-ki-klub-werder-e-v-openverein | mcp-de-zugferd-validator-validator, german-legal-deadline-calculator |
| Q050 | Какой инструмент делает E-Mail-Entwürfe с подтверждением владельца? | mcp-com-cooperemail-cooper-email, mcp-com-lockally-email | ecosystem-curator, google-calendar, midpage-legal-research, google-drive, google-slides |
| Q053 | overlapping recurring meetings, skip weekends | mcp-com-moltlinestudio-timeops | mcp-com-operatornest-tools, mcp-com-skipshit-mcp, mcp-com-autocontentapi-platform, mcp-io-github-noriget-agentcron, mcp-ai-contentsweep-supplier-feeds |
| Q057 | Как поставить напоминание, которое придёт на почту или в календарь? | mcp-com-pingfyr-pingfyr, mcp-io-github-noriget-agentcron | morning, productivity, notion, google-calendar, gmail |
| Q062 | Какой сервис с открытым кодом можно использовать вместо Zapier? | mcp-io-github-blinkboxhq-blinkbox | icd-10-codes, clickup, linear, monday, guru |
| Q065 | вебхук-триггер, который будит AI-агента | mcp-ai-wakeshift-webhooks | ifttt, agent-discussion, agent-handoff, multi-chat-orchestrator, vault-anything |
| Q068 | Verfahrensanweisung in Flussdiagramm umwandeln | mcp-io-github-eyeinthesky6-unseen-workflow-compiler | — |
| Q079 | заметки и закладки в чате | mcp-app-sensefold-sensefold, mcp-cn-moonlybox-moonlink, mcp-com-hjarni-hjarni | notion, granola, memory-toolkit, pptx, docs |
| Q080 | Как сделать, чтобы каждая новая сессия Claude не начиналась с нуля? | mcp-com-deerdawn-deerdawn, memory-toolkit | claude-code-bundled, context-handoff, claude-docs-mcp, session-status-sweep, chrome-browser |
| Q081 | Übergabe zwischen mehreren Agenten | mcp-com-llm-bus-llm-bus, mcp-io-github-josephibra-handoff-mcp-server | mcp-com-a2awire-agent-inbox, mcp-com-agentpmt-agentpmt, mcp-com-clauxel-agentmemorymcp-agentmemorymcp-mcp, mcp-com-agentemaillist-ai-free-transactional-email-smtp-relay, mcp-dev-agenttool-agenttool |
| Q084 | Какие сроки AI Act уже действуют сейчас и где за ними следить? | mcp-com-aiactradar-ai-act-radar, mcp-com-lunarasociety-intelligence | eu-ai-act-mcp, data-protection, lulius, atlassian-2, legal-domain-manager |
