# skill-library

A reference dump of Anthropic's example Agent Skills, copied verbatim from
`/mnt/skills/examples/` in the Claude environment. These are **not** auto-loaded
by Claude Code (they live here, not under `.claude/skills/`). To activate any of
them, move or copy its folder into `.claude/skills/<name>/`.

They can also be uploaded to claude.ai as custom skills.

## examples/ (23 skills)

| Skill | What it does |
|---|---|
| `mcp-builder` | Build MCP servers |
| `canvas-design` | Design work on a canvas |
| `web-artifacts-builder` | Build rich web artifacts |
| `algorithmic-art` | Generative / algorithmic art |
| `theme-factory` | Generate visual themes |
| `brand-guidelines` | Apply brand guidelines |
| `doc-coauthoring` | Co-author documents |
| `internal-comms` | Draft internal communications |
| `setup-writing-style` | Establish a writing style |
| `slack-gif-creator` | Create GIFs for Slack |
| `learn` | Learning / tutoring flows |
| `financial-calculator` | Financial calculations |
| `event-planning` | Plan events |
| `file-expenses` | File expense reports |
| `file-form` | Fill out forms |
| `benepass-reimbursement` | Benepass reimbursements |
| `call-to-book` | Booking via calls |
| `cancel-unsubscribe` | Cancel / unsubscribe flows |
| `grocery-shopping` | Grocery shopping |
| `hire-help` | Hiring help |
| `meal-delivery` | Meal delivery ordering |
| `prescription-refill` | Prescription refills |
| `return-refund` | Returns and refunds |

> `skill-creator` was also in `/mnt/skills/examples/` but is already installed at
> `.claude/skills/skill-creator`, so it is not duplicated here.
