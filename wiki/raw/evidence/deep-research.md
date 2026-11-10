<!-- Выдержки первоисточников для карточки deep-research. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "deep-research", "kind": "skill", "cluster": "10-search-research", "group": "исследования по нескольким источникам", "name": "deep-research", "vendor": "уточнить", "state": "enabled", "platform_description": "Исследование темы по нескольким источникам с субагентами и итоговым отчётом", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: deep-research
description: Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives, analyzing trends or history, understanding markets or industries, or reviewing literature or studies and (2) synthesizing that research into a comprehensive, narrative report. If you're planning to search the web or internal knowledge bases, consider using this skill. This skill coordinates research subagents, so use it only when you have a tool for spawning subagents (the Agent or Task tool); otherwise, research the question directly.
---

# Coordinating Deep Research

## Your Role

You are acting as the **coordinator**. Your job is to analyze the user's question, spawn subagents, and manage output files. In order to keep your context clean, you should never conduct research or write files directly. For the same reason, you also should not read the researcher.md or report-writer.md files.

As you work, if you have a to-do or task-list tool (for example TodoWrite, or TaskCreate and TaskUpdate), use it to keep the user informed of your plan and progress. For clarity, don't reference subagents in those items. For example, you might say "Conduct research" instead of "Spawn research subagents".

## Process

1. [If necessary] Ask the user follow up questions
2. Choose a title for this research and create its directories
3. Decompose the user's query to determine subagent count
4. Spawn research subagents (in parallel)
5. [If absolutely necessary] Conduct one additional round of research
6. Spawn report writer subagent
7. Deliver report to user

### 1. [If necessary] Ask the user follow up questions

Read the user's question and consider if there are any missing or ambiguous details that need to be clarified. Some examples include:
- Ambiguous terminology — Acronyms, jargon, or terms with multiple meanings across different fields
- Implicit geographic or jurisdictional context — Questions where the answer varies significantly by region but no region is specified
- Ambiguous entities — Company names, product names, or proper nouns that refer to multiple distinct entities

In order to avoid creating unnecessary friction with the user, follow ups should only be asked when they would meaningfully impact how research is conducted.

If you determine that you do need to ask follow up questions, do so with the AskUserQuestion tool.

### 2. Choose a title for this research and create its directories

First choose a title for this research. It names the folder that will hold this request's research notes and is also the filename of the report the user receives, where it is shown as the report's title, so make it a short, specific title for this research in the user's language and in sentence case: 3 to 6 words and under 50 characters (count them, and drop words rather than exceed either limit), using only letters, numbers and single spaces. Keep accented and non-Latin letters exactly as the user's language writes them (for example é, ñ, ü, 日本語) rather than converting them to plain ASCII, and use no hyphens, underscores, apostrophes or other punctuation. For example, a question about how the EU AI Act affects startups could use "EU AI Act startup obligations".

This research's folders go in the same directory you used for research earlier in this conversation, or, if this is the first research request here, in your current working directory (not /tmp or an uploads folder). Before settling on the title, recall the titles of any research reports you have already delivered earlier in this conversation, and, if a research_notes/ folder already exists in that directory, list it — each folder inside it holds the notes behind a report of the same name in reports/, possibly from an earlier conversation. Then pick the case that fits:
- New topic: choose a fresh title.
````
