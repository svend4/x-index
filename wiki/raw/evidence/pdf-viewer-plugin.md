<!-- Выдержки первоисточников для карточки pdf-viewer-plugin. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "pdf-viewer-plugin", "kind": "plugin", "cluster": "24-office-documents", "group": "PDF", "name": "PDF viewer (плагин)", "vendor": "уточнить", "state": "connected_tools_loaded", "platform_description": "Инструменты display_pdf, interact, list_pdfs; скиллы pdf-viewer: open, annotate, fill-form, sign, view-pdf", "source": "список инструментов сессии"},
````

## [2] список инструментов, загруженных в сессию
- Снимок: 2026-11-10
- Фрагмент:

````text
[pdf-viewer-plugin] инструменты (префикс mcp__plugin_pdf-viewer_pdf__): display_pdf, interact, list_pdfs
````

## [3] системное уведомление о статусе сервера
- Снимок: 2026-11-10
- Фрагмент:

````text
[pdf-viewer-plugin] plugin:pdf-viewer:pdf — в уведомлении «The following MCP servers are still connecting»; позже инструменты появились в списке сессии.
````

## [4] манифест плагина (начало файла)
- Снимок: 2026-11-10
- Фрагмент:

````text
{
  "name": "pdf-viewer",
  "version": "0.2.0",
  "description": "View, annotate, and sign PDFs in a live interactive viewer. Mark up contracts, fill forms with visual feedback, stamp approvals, and place signatures — then download the annotated copy.",
  "author": {
    "name": "Anthropic"
  }
}
````
