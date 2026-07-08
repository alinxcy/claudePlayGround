# `.claude` directory

Project-level configuration for [Claude Code](https://code.claude.com/docs).

## Layout

```
.claude/
├── settings.json              # Permissions, env vars, hooks (shared, committed)
├── skills/
│   └── hello-world/
│       └── SKILL.md           # Example skill — invoke with /hello-world
└── agents/
    └── code-explorer.md       # Example read-only sub agent
```

## Skills

Skills are reusable, model-invoked capabilities. Each lives in
`skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`). The
`description` tells Claude *when* to use it. Users can also invoke one directly
with `/<name>`.

## Sub Agents

Sub agents run in their own context with a restricted toolset. Each is a single
markdown file in `agents/<name>.md` with frontmatter:

- `name` — the agent identifier
- `description` — when the agent should be used
- `tools` — comma-separated allowed tools (omit to inherit all)
- `model` — optional model override (`sonnet`, `opus`, `haiku`)

The `code-explorer` agent here is read-only (Glob, Grep, Read only) and is a good
template for building your own.

## Notes

- `settings.json` is committed and shared with everyone on the repo.
- For personal, uncommitted overrides use `settings.local.json` (gitignored).
