---
name: loop
description: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo, defaults to 10m). Use for recurring tasks, polling status, or running something repeatedly on an interval.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/loop`, not the official text.

# loop

Repeat a prompt or slash command on an interval until told to stop.

## Usage
- `/loop 5m /some-command` — run every 5 minutes.
- `/loop <prompt>` — defaults to ~10m cadence.

## Behavior
1. Execute the target each tick; report only meaningful changes.
2. Choose cadence by what's being watched (fast-changing external state → shorter; idle → longer).
3. Stop when the terminal condition is met or the user says stop. Do not busy-wait with `sleep`.
