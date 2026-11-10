<!-- Выдержки первоисточников для карточки batch-file-renamer. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "batch-file-renamer", "kind": "skill", "cluster": "21-files-storage", "group": "порядок в файлах", "name": "batch-file-renamer", "vendor": "уточнить", "state": "enabled", "platform_description": "Пакетное переименование файлов: шаблоны, регулярные выражения, метаданные, предпросмотр", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: batch-file-renamer
description: "Advanced batch file renaming with patterns, regex, metadata extraction, and preview. Use when: (1) need to rename multiple files at once, (2) standardize filenames across project, (3) add sequential numbers or dates to files, (4) extract metadata into filenames (EXIF, ID3, document properties), (5) clean up messy filenames with special characters, (6) rename files based on content or folder structure. Triggers: 'rename files', 'batch rename', 'rename all files', 'standardize filenames', 'add numbers to filenames', 'clean up filenames'."
---

# Batch File Renamer

Advanced batch file renaming with patterns, regex, metadata extraction, and intelligent preview.

## Core Capabilities

### 1. Pattern-Based Renaming
Use patterns with placeholders:
```
Pattern: "Photo_{num:03d}_{date}"
Input:   IMG_1234.jpg, IMG_1235.jpg
Output:  Photo_001_2024-01-27.jpg, Photo_002_2024-01-27.jpg
```

Available placeholders:
- `{num}` - Sequential number (with optional padding)
- `{date}` - Current date (customizable format)
- `{time}` - Current time
- `{original}` - Original filename
- `{parent}` - Parent folder name
- `{ext}` - File extension
- `{size}` - File size
- `{created}` - Creation date
- `{modified}` - Modification date

### 2. Find & Replace
Simple or regex-based replacement:
```bash
# Simple
Find: "IMG_"
Replace: "Photo_"

# Regex
Find: "(\d{4})-(\d{2})-(\d{2})"
Replace: "\1\2\3"  # 2024-01-27 → 20240127
````
