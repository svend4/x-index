<!-- Выдержки первоисточников для карточки archive-manager. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "archive-manager", "kind": "skill", "cluster": "21-files-storage", "group": "архивы и дубликаты", "name": "archive-manager", "vendor": "уточнить", "state": "enabled", "platform_description": "Создание, распаковка и проверка архивов ZIP, RAR, TAR, 7z, GZ, BZ2; шифрование, ремонт", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: archive-manager
description: "Universal archive management for creating, extracting, and inspecting compressed files (ZIP, RAR, TAR, 7z, GZ, BZ2). Use when: (1) need to create archives with specific compression, (2) extract files from any archive format, (3) inspect archive contents without extracting, (4) convert between archive formats, (5) split large archives or merge split archives, (6) repair corrupted archives, (7) encrypt/decrypt archives. Triggers: 'create zip', 'extract archive', 'compress files', 'unzip', 'list archive contents', 'convert tar to zip'."
---

# Archive Manager

Universal archive management supporting all major formats with compression control, encryption, and batch operations.

## Supported Formats

**Full support (create/extract):**
- ZIP (.zip) - Universal
- TAR (.tar, .tar.gz, .tar.bz2, .tar.xz) - Unix standard
- GZIP (.gz) - Single file compression
- BZIP2 (.bz2) - Better compression
- XZ (.xz) - Best compression

**Extract only:**
- RAR (.rar) - Popular Windows format
- 7z (.7z) - High compression
- ISO (.iso) - Disc images
- CAB (.cab) - Windows cabinet files

## Basic Operations

### 1. Create Archive

```python
# ZIP archive
import zipfile

with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('file1.txt')
    zf.write('file2.txt')

# TAR.GZ archive
import tarfile

with tarfile.open('archive.tar.gz', 'w:gz') as tf:
````
