<!-- Выдержки первоисточников для карточки duplicate-hunter. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "duplicate-hunter", "kind": "skill", "cluster": "21-files-storage", "group": "архивы и дубликаты", "name": "duplicate-hunter", "vendor": "уточнить", "state": "enabled", "platform_description": "Поиск дубликатов: точные (хеш), похожие (нечёткое сравнение), почти одинаковые изображения", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: duplicate-hunter
description: "Intelligent duplicate file detection using multiple methods: exact matches (hash), similar content (fuzzy), near-duplicates (perceptual for images), and metadata comparison. Use when: (1) cleaning up disk space by finding duplicate files, (2) organizing photo collections with similar shots, (3) deduplicating Downloads folder, (4) finding duplicate documents across folders, (5) identifying redundant backups, (6) consolidating file libraries. Triggers: 'find duplicates', 'detect duplicate files', 'remove duplicates', 'find similar images', 'deduplicate', 'clean up duplicate files'."
---

# Duplicate Hunter

Intelligent multi-method duplicate file detection system with fuzzy matching and perceptual hashing for images.

## Detection Methods

### 1. Exact Duplicates (Hash-based)
Fastest and most reliable - compares file hashes (MD5/SHA256):
```python
import hashlib

def hash_file(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# Files with same hash = exact duplicates
```

### 2. Similar Images (Perceptual Hash)
Finds near-duplicate photos (same scene, different exposure/crop):
```python
from PIL import Image
import imagehash

def perceptual_hash(image_path):
    img = Image.open(image_path)
    return imagehash.average_hash(img)

# Hash distance < 5 = similar images
```

### 3. Similar Documents (Fuzzy Matching)
````
