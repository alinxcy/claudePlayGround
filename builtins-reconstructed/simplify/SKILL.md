---
name: simplify
description: Review the changed code for reuse, simplification, efficiency, and altitude cleanups, then apply the fixes. Quality only — it does not hunt for bugs; use /code-review for that.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/simplify`, not the official text.

# simplify

Improve the quality of the changed code (not a bug hunt — use `/code-review` for correctness).

## Focus
- **Reuse**: replace ad-hoc code with existing helpers/utilities.
- **Simplification**: cut needless branches, dead code, over-abstraction.
- **Efficiency**: obvious wins (avoid re-computation, needless allocation/IO).
- **Altitude**: right level of abstraction; match surrounding idioms.

Apply the fixes to the working tree, matching the codebase's existing style.
