---
name: init
description: Initialize a new CLAUDE.md file with codebase documentation
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/init`, not the official text.

# init

Generate a `CLAUDE.md` at the repo root that gives future sessions the context they need.

## Steps
1. Survey the repo: build/test/lint commands (package.json, Makefile, pyproject, etc.), directory layout, and dominant conventions.
2. Read existing docs (README, CONTRIBUTING) and any current CLAUDE.md — merge, don't clobber.
3. Write a concise CLAUDE.md covering: how to build/test/run, project structure, code style/conventions, and any non-obvious gotchas.
4. Keep it short and high-signal — it is prepended to context every session, so avoid bloat.
