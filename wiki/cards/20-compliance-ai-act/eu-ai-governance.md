---
id: "eu-ai-governance"
title: "Lexbeam EU AI Governance"
kind: "plugin"
vendor: "Lexbeam Software"
cluster: "20-compliance-ai-act"
summary: "Плагин Lexbeam EU AI Governance: скиллы по классификации риска, соответствию, DPIA, оценке вендоров, политике и управлению рисками по AI Act."
status: "draft"
data_class: "unknown"
price: "unknown"
auth: "unknown"
hosting: "unknown"
languages: ["en"]
source_urls: ["raw://session/2026-11-10/inventory.json", "https://lexbeam-software.github.io/eu-ai-governance-plugin/", "raw://evidence/eu-ai-governance.md", "raw://session/2026-11-10/tools-by-server.txt"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
group: "AI Act"
tags: ["AI Act", "EU AI Act", "eu-ai-governance", "DPIA", "FRIA", "оценка вендоров", "evidence pack"]
jurisdiction: "EU"
---
# Lexbeam EU AI Governance

## Суть
- По описанию поставщика [2], плагин предназначен для юридических, комплаенс-, privacy-, security- и AI-governance-команд в Европе: классификация, DPIA и FRIA, проверка вендоров и политик, пакеты доказательств. Юрисдикция — EU (выведен по [2]: название плагина в манифесте содержит EU AI Act governance).
- В описании платформы: скиллы по классификации риска, соответствию, оценке вендора, DPIA, политике, управлению рисками и документации [1].

## Для чего
- Классификация ИИ-системы по риску по AI Act [1].
- Оценка вендоров ИИ и проверка политик [1][2].
- Оценка воздействия: DPIA и FRIA [2].
- Сбор пакетов доказательств (evidence packs) [2].

## Возможности
- Скиллы: классификация риска, соответствие, оценка вендора, DPIA, политика, управление рисками, документация [1].
- Рабочие процессы DPIA и FRIA [2].
- Проверка вендоров и политик; пакеты доказательств (evidence packs) [2].
- Инструменты MCP-сервера [[eu-ai-act-mcp]] по списку инструментов сессии [3]: классификация (euaiact_classify_system, euaiact_assess_system), исключение по статье 6(3) (euaiact_assess_art6_3_exception), порог GPAI (euaiact_check_gpai_systemic_risk), статьи и обязательства (euaiact_get_article, euaiact_get_obligations), сроки и штрафы (euaiact_check_deadlines, euaiact_calculate_penalty), чек-лист приложения IV (euaiact_annex_iv_checklist), вопросы (euaiact_answer_question) [3]. Префикс имён инструментов — mcp__plugin_eu-ai-governance_eu-ai-act__ [3]: по нему сервер загружен как часть плагина (вывод по префиксу имён).
- Полный перечень скиллов плагина в выдержках не подтверждён: нет данных; в platform_description [1] перечислены темы.

## Чем выделяется
- Заявлено автором: подход назван «Source-grounded EU AI Act governance» [2].
- Мнение: классификация, DPIA и FRIA и пакеты доказательств в одном плагине дают единый процесс для команды.

## Ограничения и риски
- Манифест указывает на юридическое предупреждение (LEGAL-DISCLAIMER) [2].
- Слово «Source-grounded» — заявление поставщика; как именно проверяются первоисточники, в выдержках не описано: нет данных [2].
- Версия 1.1.3, лицензия Apache-2.0 [2].
- Политика конфиденциальности плагина (privacyPolicyUrl в манифесте) ведёт в репозиторий eu-ai-act-mcp [2]; её содержание в выдержках не описано: нет данных.
- нет данных: цена, лимиты, способ подключения, место обработки данных и класс данных.

## Когда не подходит
- Мнение: окончательная классификация и решения о соответствии без юриста; в манифесте есть юридическое предупреждение [2].
- Мнение: команды вне Европы, так как описание адресовано европейским командам [2].

## Альтернативы
- [[data-protection]] — DPIA есть и в этом плагине [1][2]; см. карточку [[data-protection]].

## Источники
1. Инвентарь сессии: запись позиции (список скиллов сессии), снимок 2026-11-10 — raw://session/2026-11-10/inventory.json; список инструментов сессии по серверам, снимок 2026-11-10 — raw://session/2026-11-10/tools-by-server.txt (сверка не проводилась).
2. Манифест плагина (начало файла), снимок 2026-11-10 — raw://evidence/eu-ai-governance.md; адрес homepage из манифеста — https://lexbeam-software.github.io/eu-ai-governance-plugin/.
3. Список инструментов сессии, строка сервера eu-ai-act-mcp, снимок 2026-11-10 — raw://session/2026-11-10/tools-by-server.txt
Сверка с первоисточником не проводилась (verified_on: null).

## Заявлено автором
> «Source-grounded EU AI Act governance for European legal, compliance, privacy, security, and AI governance teams: classification, DPIA and FRIA workflows, vendor review, policy review, and evidence packs.» [2]

Поле platform_description записи инвентаря [1], дословно (заявление записи, не проверенный факт):
> «Скиллы AI Act: классификация риска, соответствие, оценка вендора, DPIA, политика, управление рисками, документация» [1]
