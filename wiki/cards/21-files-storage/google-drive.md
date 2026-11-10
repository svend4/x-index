---
id: "google-drive"
title: "Google Drive (коннектор)"
kind: "connector"
vendor: "Google"
cluster: "21-files-storage"
group: "облачные диски"
summary: "Коннектор Google Drive: поиск и чтение файлов, создание и изменение, копирование, доступ и общие диски. Подключён."
status: "draft"
data_class: "C"
price: "free"
auth: "oauth"
hosting: "global"
hosted: true
languages: ["en", "ru", "de"]
source_urls: ["https://workspace.google.com", "raw://session/2026-11-10/inventory.json"]
snapshot: "2026-11-10"
verified_on: null
updated: "2026-11-10"
tags: ["Google Drive", "файлы", "хранилище", "общие диски", "права доступа", "дубликаты"]
curator_hint: "test"
---

# Google Drive (коннектор)

## Суть
Коннектор даёт доступ к файлам Google Drive владельца, включая общие диски. В сессии загружено 13 инструментов. Коннектор подключён.

## Для чего
- Поиск файлов, чтение содержимого, выгрузка в диалог.
- Создание и изменение файлов, копирование, перенос в корзину.
- Проверка и изменение прав доступа.

## Возможности
По списку инструментов сессии: `search_files`, `list_recent_files`, `get_file_metadata`, `read_file_content`, `download_file_content`, `create_file`, `update_file`, `copy_file`, `trash_file`, `share_file`, `get_file_permissions`, `list_shared_drives`, `get_shared_drive_metadata`.

## Чем выделяется
- Мнение: есть инструменты прав доступа (`share_file`, `get_file_permissions`). Это редкость для файловых коннекторов и полезно для аудита общих папок.

## Ограничения и риски
- `share_file` и `trash_file` меняют доступ и состояние файлов. Нужно подтверждение владельца.
- Файлы могут содержать персональные данные. Передача модели требует осторожности.
- Для очистки дубликатов Google Takeout есть отдельный скилл [[takeout-drive-cleanup]], который работает по контрольным суммам.

## Когда не подходит
- Массовая очистка без предварительного списка и подтверждения.
- Архивы с чужими данными без согласования с их владельцами.

## Альтернативы
- [[google-docs]] и [[google-sheets]] — редактирование конкретных типов файлов.
- [[microsoft-365]] — SharePoint и OneDrive, в сессии не подключён.

## Источники
1. Список инструментов сессии (префикс `mcp__Google_Drive__`), 2026-11-10.
2. ListConnectors, 2026-11-10: состояние «подключён».
3. Сайт поставщика: https://workspace.google.com (проверить при сверке).

## Заявлено автором
> Search, read, and upload files instantly
