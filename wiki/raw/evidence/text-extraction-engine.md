<!-- Выдержки первоисточников для карточки text-extraction-engine. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "text-extraction-engine", "kind": "skill", "cluster": "24-office-documents", "group": "OCR и извлечение текста", "name": "text-extraction-engine", "vendor": "уточнить", "state": "enabled", "platform_description": "Извлечение текста из PDF, DOCX, XLSX, PPTX, изображений (OCR), HTML, ePub, RTF", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: text-extraction-engine
description: "Extract text from any document format (PDF, DOCX, XLSX, PPTX, images OCR, HTML, ePub, RTF). Use when: (1) need to extract text from PDFs for analysis, (2) OCR scanned documents or images, (3) extract data from Office documents, (4) convert documents to plain text, (5) extract text from web pages (clean HTML), (6) batch text extraction from multiple files, (7) extract structured data from documents. Triggers: 'extract text from PDF', 'OCR this image', 'get text from document', 'convert PDF to text', 'extract data from Excel', 'read text from image'."
---

# Text Extraction Engine

Universal text extraction from any document format with OCR, structure preservation, and batch processing.

## Supported Formats

**Documents:**
- PDF (.pdf) - All types including scanned
- Word (.docx, .doc)
- Excel (.xlsx, .xls) - Text and data
- PowerPoint (.pptx, .ppt)
- RTF (.rtf)
- ODT, ODS, ODP (OpenOffice)

**Images (OCR):**
- PNG, JPEG, GIF, BMP, TIFF
- Screenshots
- Scanned documents
- Photos of text

**Web:**
- HTML - Clean text extraction
- EPUB - E-books
- Markdown

**Other:**
- Text files with encoding detection
- CSV data extraction
- JSON/XML data to text

## PDF Text Extraction

### Simple Text Extraction

```python
````
