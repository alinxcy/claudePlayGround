---
name: update-config
description: Configure the Claude Code harness via settings.json — permissions ("allow X"), env vars, and hooks (automated "when/whenever X" behaviors the harness runs). Also for hook troubleshooting.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `update-config`, not the official text.

# update-config

Edit `.claude/settings.json` / `settings.local.json` (or user-level `~/.claude/settings.json`).

## Common tasks
- **Permissions**: add to `permissions.allow` / `permissions.deny` (e.g. `"Bash(npm run test:*)"`).
- **Env vars**: `env: { "KEY": "value" }`.
- **Hooks**: automated behaviors ("after Claude stops, run X") go under `hooks` (PreToolUse, PostToolUse, Stop, SessionStart, …) — the harness executes these, not the model.
- Pick the right scope: project (shared, committed) vs. local (gitignored) vs. user (global).
- Validate JSON and confirm hook command exit-code semantics.
