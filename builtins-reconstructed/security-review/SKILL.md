---
name: security-review
description: Complete a security review of the pending changes on the current branch
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `/security-review`, not the official text.

# security-review

Security-focused review of the pending diff on the current branch.

## Look for
- Injection (SQL/command/template), unsafe deserialization, SSRF.
- AuthN/AuthZ gaps, missing access checks, IDOR.
- Secrets in code, weak crypto, insecure randomness.
- Path traversal, unsafe file ops, XXE.
- XSS/CSRF and unsafe HTML rendering.
- Dependency and supply-chain risks introduced by the diff.

## Output
Rank by severity with concrete exploit scenario and a fix suggestion for each. Distinguish confirmed from speculative.
