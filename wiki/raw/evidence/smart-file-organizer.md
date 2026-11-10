<!-- Выдержки первоисточников для карточки smart-file-organizer. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "smart-file-organizer", "kind": "skill", "cluster": "21-files-storage", "group": "порядок в файлах", "name": "smart-file-organizer", "vendor": "уточнить", "state": "enabled", "platform_description": "Организация файлов по содержимому: папки, категории, фото по EXIF и событиям", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: smart-file-organizer
description: "Intelligent file organization with content understanding and semantic categorization. Use this skill when users need to: (1) Organize messy Downloads folders or file collections, (2) Sort files by content rather than just extension, (3) Handle mixed file types that need contextual organization, (4) Create meaningful folder structures automatically, (5) Organize photos by EXIF data and events, (6) Clean up workspace with hundreds of unsorted files. Triggers include phrases like 'organize my files', 'sort these documents', 'clean up Downloads', 'group files by project', 'organize photos by date/event', or any request involving file organization beyond simple renaming."
---

# Smart File Organizer

Intelligent file organization with semantic understanding of file content, metadata, and context.

## Core Capabilities

This skill enables Claude to:

1. **Analyze file content** - Read inside documents (PDF, DOCX, TXT) to understand what they contain
2. **Extract metadata** - Use EXIF data from photos, document properties, timestamps
3. **Semantic categorization** - Group files by meaning, not just extension
4. **Create intelligent folder structures** - Build hierarchies that make sense for the content
5. **Handle mixed file types** - Photos, documents, code, archives in one operation

## Usage Patterns

### Basic Organization

```
User: "Organize my Downloads folder"

Process:
1. Scan all files in Downloads
2. For each file:
   - Determine file type
   - Extract content/metadata
   - Categorize semantically
3. Create folder structure
4. Move files with confirmation
```

### Project-Based Organization

```
User: "Group all files by project"
````
