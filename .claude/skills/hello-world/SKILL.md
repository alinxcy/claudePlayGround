---
name: hello-world
description: A minimal example skill. Use when the user wants to test that skills are working, or asks for a greeting demo. Prints a friendly greeting and explains how skills are structured.
---

# Hello World Skill

This is a starter skill for the claudePlayGround repository. It demonstrates the
minimal structure a skill needs so you can copy it to build real ones.

## What to do when invoked

1. Greet the user warmly.
2. Briefly explain that this greeting came from a project-level skill located at
   `.claude/skills/hello-world/SKILL.md`.
3. If the user asks how to make their own skill, point them at the structure below.

## Skill structure reference

A skill is a directory under `.claude/skills/` containing a `SKILL.md` file with
YAML frontmatter:

- `name`: the skill's identifier (invoked as `/hello-world`).
- `description`: tells Claude *when* to use the skill. Be specific about trigger
  conditions — this is how the skill gets selected automatically.

The body (this markdown) is the instructions Claude follows once the skill runs.
You can also add supporting files (scripts, references, templates) in the same
directory and reference them by relative path.
