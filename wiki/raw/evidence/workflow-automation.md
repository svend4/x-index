<!-- Выдержки первоисточников для карточки workflow-automation. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "workflow-automation", "kind": "skill", "cluster": "08-automation-ipaas", "group": "сценарии (make, zapier, n8n)", "name": "workflow-automation", "vendor": "уточнить", "state": "enabled", "platform_description": "Оркестрация задач: цепочки, условия, параллельное выполнение, обработка ошибок, шаблоны", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: workflow-automation
description: "Workflow automation and orchestration: task chains, conditional logic, parallel execution, error handling, workflow templates. Use when: (1) automating workflows, (2) orchestrating tasks, (3) building task chains, (4) conditional workflows, (5) parallel task execution, (6) workflow error handling. Triggers: 'automate workflow', 'task orchestration', 'workflow automation', 'task chain', 'parallel tasks', 'workflow template'."
---

# Workflow Automation

Task orchestration and workflow automation with conditional logic.

## Basic Workflow

```python
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'
    FAILED = 'failed'
    SKIPPED = 'skipped'

class Task:
    def __init__(self, name, action, depends_on=None):
        self.name = name
        self.action = action
        self.depends_on = depends_on or []
        self.status = TaskStatus.PENDING
        self.result = None
        self.error = None
        self.start_time = None
        self.end_time = None
    
    def run(self, context):
        """Execute task"""
        
        self.status = TaskStatus.RUNNING
        self.start_time = datetime.now()
        
        try:
````
