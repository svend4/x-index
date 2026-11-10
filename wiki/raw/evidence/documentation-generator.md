<!-- Выдержки первоисточников для карточки documentation-generator. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "documentation-generator", "kind": "skill", "cluster": "03-docs-knowledge", "group": "заметки и wiki", "name": "documentation-generator", "vendor": "уточнить", "state": "enabled", "platform_description": "Генерация документации: API-доки, README, changelog, шаблоны wiki-страниц", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: documentation-generator
description: "Automated documentation generation: API docs, README creation, changelog generation, wiki templates. Use when: (1) generating API documentation, (2) creating README files, (3) building changelogs, (4) wiki page generation, (5) code documentation, (6) project documentation. Triggers: 'generate documentation', 'create readme', 'api docs', 'generate changelog', 'documentation template', 'auto document code'."
---

# Documentation Generator

Automated generation of API docs, READMEs, changelogs, and wikis.

## README Generator

```python
def generate_readme(project_name, description, **sections):
    """Generate README.md file"""
    
    readme = f"""# {project_name}

{description}

## Installation

```bash
pip install {project_name.lower().replace(' ', '-')}
```

## Quick Start

```python
import {project_name.lower().replace(' ', '_')}

# Your code here
```

## Features

{sections.get('features', '- Feature 1\n- Feature 2\n- Feature 3')}

## Usage

{sections.get('usage', 'Coming soon...')}
````
