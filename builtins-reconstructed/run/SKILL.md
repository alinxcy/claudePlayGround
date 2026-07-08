---
name: run
description: Launch and drive this project's app to see a change working. Use when asked to run/start/screenshot the app, or to confirm a change works in the real app (not just tests).
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/run`, not the official text.

# run

Start the project's app and drive it to confirm a change works for real.

## Steps
1. Detect project type (CLI, web server, TUI, Electron, browser-driven, library) and its start command.
2. Launch it (background long-running servers; foreground short commands).
3. Drive the affected flow — hit the route, click through the UI (Playwright/Chromium is preinstalled), run the command.
4. Capture output/screenshot and report what you observed. Tear down background processes when done.
