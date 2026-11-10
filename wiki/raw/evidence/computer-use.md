<!-- Выдержки первоисточников для карточки computer-use. Фрагменты дословные. Файл создаёт tools/wiki.py evidence; не править вручную. -->

## [1] инвентарь сессии: запись позиции (ListConnectors, ListSkills, системные уведомления)
- Снимок: 2026-11-10
- Фрагмент:

````text
    {"id": "computer-use", "kind": "skill", "cluster": "09-browser-web-data", "group": "управление интерфейсом", "name": "computer-use", "vendor": "уточнить", "state": "enabled", "platform_description": "Управление рабочим столом пользователя: скриншоты, клики, ввод через приложение Claude Desktop", "source": "ListSkills"},
````

## [2] локальный файл скилла (начало)
- Снимок: 2026-11-10
- Фрагмент:

````text
---
name: computer-use
description: "Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their screen, or for \"computer use\". Computer use (desktop control) lets Claude take screenshots of the person's desktop and control it with clicks, typing and scrolling through the Claude desktop app; its tools are named mcp__computer-use__* when the session runs in the desktop app and mcp__remote-devices__computer_* when a cloud session is linked to the person's computer; before computer use is turned on for a conversation there may be no such tools, only an enable__mcp__remote-devices__computer tool, which turns it on. It covers turning it on, picking the right tool, the access flow, and the safety rules for tiered apps, links and financial actions. It is not for websites, which go through Claude in Chrome or the built-in browser and their own skills."
compatibility: "Cowork in the Claude desktop app, and Cowork Remote or upgraded claude.ai sessions linked to a computer running the desktop app (macOS or Windows) with Computer use turned on"
license: Proprietary. LICENSE.txt has complete terms
---

# Computer use (desktop control)

Computer use lets Claude take screenshots of the person's desktop and control it with mouse clicks, keyboard input, and scrolling, through the Claude desktop app. Its tools are named `mcp__computer-use__*` (for example `request_access`, `screenshot`) when the session runs inside the desktop app, and `mcp__remote-devices__computer_*` (for example `computer_request_access`, `computer_screenshot`) when the session runs in the cloud and is linked to the person's computer. Computer use works only while Computer use is turned on in the Claude desktop app (Settings → This computer → Computer use; it is off by default).

## Turning computer use on from a chat

What Claude does first depends on which tools are present (loaded or deferred):

1. **Computer-use tools are present.** Claude goes straight to the access flow below.
2. **No computer-use tools, but an `enable__mcp__remote-devices__computer` tool is present.** Claude calls that tool once, before any other step of the task, with the task in its `task` field. When the call goes through, the `mcp__remote-devices__computer_*` tools arrive with it and Claude starts with the access flow below; there is no second enable step. If it does not go through, Claude relays the reason in one line and carries on with what it can do in the conversation.
3. **Neither.** Computer use is not available in this conversation as it stands, and Claude says so plainly without diagnosing why: in general Claude can use apps on a computer where the Claude desktop app is installed and signed in with Computer use turned on, and on claude.ai in a web browser, if the composer's + menu offers Devices, the person can pick their computer there before sending a new message. Claude does not pretend to act.

## Separate filesystems

Computer-use actions (clicks, typing, clipboard writes) happen on the person's real computer, a different system from wherever Claude's own shell and files are, when it has them. Files Claude creates on its side do not exist on the person's machine. If Claude puts a command or file path in the person's clipboard, or types into one of their apps, the path must exist on their computer, not a path on Claude's side that they can't reach.

## Pick the right tool for the app

Each tier trades speed/precision against coverage:

1. **Dedicated MCP for the app**: if the task is in an app that has its own MCP (Slack, Gmail, Calendar, Linear, etc.) and that MCP is connected, Claude uses it. API-backed tools are fast and precise.
2. **Browser tools**: if the target is a web app and there's no dedicated MCP for it, Claude uses a browser: Claude in Chrome (tools named `mcp__claude-in-chrome__*`) or the built-in browser (tools named `mcp__Claude_Browser__*` in the desktop app, `mcp__remote-devices__Claude_Browser__*` when a cloud session is linked to the person's computer). Both are DOM-aware, much faster than clicking pixels. If this prompt has a `<browsers>` section, Claude follows it on which browser to use; otherwise it uses whichever one is connected. If neither is connected, Claude asks the person to connect one rather than falling through to computer use.
3. **Computer use**: for native desktop apps (Maps, Notes, Finder, Photos, System Settings, any third-party native app) and cross-app workflows. Computer use is the right tool here; Claude does not decline a native-app task just because there's no dedicated MCP for it.

This is about what's available, not error handling: if a dedicated MCP tool errors, Claude debugs or reports it rather than silently retrying via a slower tier.

## Background tools and full-screen tools

On a Mac the computer-use toolkit usually has two kinds of tool:

- **Background tools** have `app_` in the name: `app_screenshot`, `app_click`, `app_type`, `app_menu` (an app's menu bar) and so on, or `computer_app_screenshot` and so on in a cloud session. They work in granted apps without taking the screen from the person. A call says which app it acts on, by the bundle identifier the access response returned, so a task across several granted apps stays in the background.
- **Full-screen tools** take the screen away from the person: `computer_batch`, the clipboard tools, and `screenshot`, `left_click`, `type` and the like where listed (`computer_screenshot` and so on in a cloud session).
````
