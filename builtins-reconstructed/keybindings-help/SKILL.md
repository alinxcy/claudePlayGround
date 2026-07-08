---
name: keybindings-help
description: Customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `keybindings-help`, not the official text.

# keybindings-help

Edit `~/.claude/keybindings.json` to remap Claude Code shortcuts.

## Steps
1. Read the current keybindings file (create if absent).
2. Map the requested action to its command id; set the desired key or chord (e.g. `ctrl+k ctrl+s`).
3. Watch for conflicts with existing bindings and terminal-reserved keys.
4. Write valid JSON and tell the user which binding changed.
