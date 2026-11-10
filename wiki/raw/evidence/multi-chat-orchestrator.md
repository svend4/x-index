<!-- Выдержки первоисточников для карточки multi-chat-orchestrator. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "multi-chat-orchestrator", "kind": "skill", "cluster": "19-agents-orchestration", "group": "оркестраторы", "name": "multi-chat-orchestrator", "vendor": "уточнить", "state": "enabled", "platform_description": "Parallel processing system for massive tasks through multiple chat sessions; MASTER-WORKER; описание начинается словом «Revolutionary»", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: multi-chat-orchestrator
description: "Revolutionary parallel processing system for massive tasks through multiple chat sessions. MASTER-WORKER architecture: splits large jobs (5000+ lines templates, complex analyses, multi-topic research) into chunks, generates worker instructions, coordinates 10-20 parallel chats, aggregates results. CONTROL PANEL in master chat shows real-time status dashboard. WORKFLOW: [1]Chunk-large-task(auto-split by topics/sections) [2]Generate-worker-instructions(indexed chunks+prompts) [3]Parallel-execution(10-20 worker chats) [4]Result-aggregation(collect+merge). TRIGGERS: large-template|parallel-processing|multi-chat|chunk-task|split-work|orchestrate|5000-lines|massive-task. FEATURES: intelligent-chunking, worker-instruction-gen, index-management, status-tracking, result-assembly. USE CASES: massive templates, multi-topic research, parallel document generation, distributed analysis. v1.0"
---

# Multi-Chat Orchestrator

## 🎯 Revolutionary Concept

**Parallel processing через множество Claude чатов!**

Обходим лимит контекста одного чата, распределяя работу на 10-20 worker чатов которые работают параллельно.

## 🏗️ Master-Worker Architecture

### Компоненты системы:

```
┌─────────────────────────────────────────────────┐
│         MASTER CHAT (Control Panel)             │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Multi-Chat Orchestrator активирован          │
│  • Анализирует большое задание                  │
│  • Разбивает на chunks (10-20 частей)           │
│  • Генерирует инструкции для workers            │
│  • Управляет координацией                       │
│  • Собирает результаты                          │
│  • РОЛЬ: Координатор + Dashboard                │
└─────────────────────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │    Parallel Distribution  │
        │                           │
┌───────▼────────┐  ┌───────▼────────┐  ┌───────▼────────┐
│  WORKER CHAT 1 │  │  WORKER CHAT 2 │  │  WORKER CHAT 3 │
│  ════════════  │  │  ════════════  │  │  ════════════  │
│  Chunk 1       │  │  Chunk 2       │  │  Chunk 3       │
│  Topic: [A]    │  │  Topic: [B]    │  │  Topic: [C]    │
│  Lines: 500    │  │  Lines: 500    │  │  Lines: 500    │
│  Status: ✅    │  │  Status: ✅    │  │  Status: ✅    │
````
