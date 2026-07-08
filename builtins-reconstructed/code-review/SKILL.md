---
name: code-review
description: Review the current diff for correctness bugs and reuse/simplification/efficiency cleanups at the given effort level (low/medium/high/max). Pass --comment to post inline PR comments, or --fix to apply findings.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/code-review`, not the official text.

# code-review

Review the working-tree diff (not a remote PR — that's `/review`).

## Steps
1. Get the diff: `git diff` (unstaged+staged) or against the base branch.
2. Hunt for: correctness bugs, edge cases, unhandled errors, then reuse/simplification/efficiency cleanups.
3. Calibrate by effort level: low/medium = few high-confidence findings; high/max = broader, may include uncertain ones.
4. Verify each finding against the code before reporting; give a concrete failure scenario.
5. Report most-severe first. `--comment` posts inline PR comments; `--fix` applies fixes to the working tree.
