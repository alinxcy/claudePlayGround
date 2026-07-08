---
name: claude-api
description: Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. Consult instead of answering LLM questions from memory.
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `claude-api`, not the official text.

# claude-api

Authoritative reference to consult before answering Anthropic API / SDK questions — do not rely on memory (training data may be stale).

## Covers
- **Models & ids**: current Claude family and exact model ids; pick the latest capable model for new apps.
- **Messages API**: params, system prompts, multi-turn, stop reasons.
- **Streaming**: SSE event types and assembly.
- **Tool use**: tool definitions, tool_use/tool_result loop, parallel tools.
- **MCP, agents, prompt caching, token counting, batch, migration.**

When a task is LLM-shaped and the provider is Anthropic, verify specifics here rather than guessing.
