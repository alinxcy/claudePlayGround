---
name: review
description: Review a GitHub pull request; for your working diff use /code-review
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/review`, not the official text.

# review

Review a remote GitHub PR (use `/code-review` for the local working diff).

## Steps
1. Fetch the PR: title, description, changed files, and diff (via the GitHub MCP tools).
2. Assess correctness, design, tests, and adherence to repo conventions.
3. Note blocking issues vs. nits separately.
4. Post a review or summarize inline, most-important first. Be frugal with comments — only what's genuinely useful.
