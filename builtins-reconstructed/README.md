# Claude Code Built-in Skills — reconstructions

These are the skills that ship **inside the Claude Code CLI** in this environment.

⚠️ **Important:** Except where noted, the CLI built-ins are compiled into the
Claude Code package and are **not** available as copyable `SKILL.md` files on
disk. The files here are **best-effort reconstructions** written from each
skill's official one-line description plus general knowledge of how they behave.
They are *approximations*, not the real bundled prompts. Treat them as a
reference/starting point, not an authoritative copy.

## List of built-ins

| Skill | Invoke | This file is | Notes |
|---|---|---|---|
| `init` | `/init` | reconstruction | Generate CLAUDE.md |
| `code-review` | `/code-review` | reconstruction | Review local working diff |
| `review` | `/review` | reconstruction | Review a remote GitHub PR |
| `security-review` | `/security-review` | reconstruction | Security review of pending diff |
| `verify` | `/verify` | reconstruction | Exercise a change end-to-end |
| `simplify` | `/simplify` | reconstruction | Quality cleanups (not bug hunt) |
| `dataviz` | (auto) | reconstruction | Chart/visualization design system |
| `artifact-design` | (auto) | reconstruction | Artifact design fundamentals |
| `update-config` | (auto) | reconstruction | Edit settings.json (perms/env/hooks) |
| `keybindings-help` | (auto) | reconstruction | Edit ~/.claude/keybindings.json |
| `fewer-permission-prompts` | (auto) | reconstruction | Allowlist safe repeated calls |
| `loop` | `/loop` | reconstruction | Run a prompt/command on an interval |
| `claude-api` | (auto) | reconstruction | Claude API/SDK reference |
| `run` | `/run` | reconstruction | Launch & drive the project's app |
| `session-start-hook` | (auto) | **REAL COPY** | Copied verbatim from `~/.claude/skills/session-start-hook` — the one built-in that exists as a real file on disk |

## Why only `session-start-hook` is real

A filesystem scan for `SKILL.md` found the docx/pdf/etc. skills under
`/mnt/skills/` (those are the same ones claude.ai uses), but the CLI slash-command
skills above had no standalone files — only `session-start-hook` existed at
`/root/.claude/skills/session-start-hook/SKILL.md`, so that one is a faithful copy.

## Using these in claude.ai

The reconstructions can be uploaded to claude.ai as custom skills, but note many
are **Claude Code-specific** (`init`, `update-config`, `keybindings-help`,
`fewer-permission-prompts`, `run`, `loop`) and reference concepts —
`settings.json`, permission prompts, the CLI harness — that don't exist in
claude.ai, so they won't be useful there. The generally portable ones are
`dataviz`, `artifact-design`, `claude-api`, and (loosely) `code-review` /
`security-review` / `simplify`.
