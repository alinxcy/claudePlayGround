---
name: verify
description: Verify that a code change actually does what it's supposed to by exercising it end-to-end and observing behavior — drive the affected flow, not just tests or typecheck.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/verify`, not the official text.

# verify

Confirm a change works by observing real behavior, before committing nontrivial work.

## Steps
1. Identify the runtime surface the change affects (endpoint, CLI command, UI flow, function).
2. Actually drive it — run the command, hit the endpoint, render the page — don't rely on tests/typecheck alone.
3. Observe the output and compare against expected behavior.
4. Report what you exercised and what you saw. Skip only for pure test/doc changes with no runtime surface.
