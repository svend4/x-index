<!-- Выдержки первоисточников для карточки smart-backup-assistant. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "smart-backup-assistant", "kind": "skill", "cluster": "21-files-storage", "group": "архивы и дубликаты", "name": "smart-backup-assistant", "vendor": "уточнить", "state": "enabled", "platform_description": "Стратегии резервного копирования: инкрементальные копии, ротация, проверка восстановления, правило 3-2-1", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: smart-backup-assistant
description: "Intelligent backup management with automated strategies, version control, and recovery planning. Use when: (1) setting up backup strategies for projects or systems, (2) creating incremental or differential backups, (3) scheduling automated backups, (4) managing backup rotation and retention, (5) testing backup integrity and recovery, (6) syncing important files across locations, (7) implementing 3-2-1 backup rule. Triggers: 'create backup', 'backup strategy', 'schedule backups', 'incremental backup', 'test backup recovery', 'sync files to backup'."
---

# Smart Backup Assistant

Intelligent backup orchestration with automated strategies, versioning, encryption, and disaster recovery planning.

## Backup Strategies

### 1. Full Backup

```python
import shutil
from datetime import datetime

def full_backup(source_dir, backup_dir):
    """Complete copy of all files"""
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'full_backup_{timestamp}')
    
    # Copy entire directory
    shutil.copytree(source_dir, backup_path)
    
    return backup_path
```

### 2. Incremental Backup

```python
def incremental_backup(source_dir, backup_dir, last_backup):
    """Backup only files changed since last backup"""
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'incremental_{timestamp}')
    os.makedirs(backup_path)
    
    for root, dirs, files in os.walk(source_dir):
````
