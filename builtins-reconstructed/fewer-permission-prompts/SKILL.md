---
name: fewer-permission-prompts
description: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `fewer-permission-prompts`, not the official text.

# fewer-permission-prompts

Reduce repetitive approval prompts by allowlisting safe, frequent calls.

## Steps
1. Scan recent session transcripts for commonly-approved, read-only commands (e.g. `git status`, `ls`, `git diff`, safe MCP reads).
2. Rank by frequency and safety — only include genuinely read-only / non-destructive patterns.
3. Add them to `.claude/settings.json` `permissions.allow`, using precise matchers (e.g. `"Bash(git log:*)"`).
4. Never allowlist destructive or outward-facing commands.
