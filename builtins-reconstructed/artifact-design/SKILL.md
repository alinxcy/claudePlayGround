---
name: artifact-design
description: Design guidance and fundamentals for Artifacts (self-contained HTML/Markdown pages hosted for the user).
---

> **RECONSTRUCTION** — approximation of the Claude Code built-in `artifact-design`, not the official text.

# artifact-design

Calibrate design investment to the request, then build a polished, self-contained page.

## Guidance
1. **Right-size effort**: a quick utility ≠ a showcase landing page. Don't over-design a throwaway.
2. **Self-contained**: inline all CSS/JS; embed assets as data URIs (strict CSP blocks external hosts).
3. **Responsive**: relative units, flex/grid, `max-width:100%` media; wide content scrolls in its own container — the body never scrolls horizontally.
4. **Theme-aware**: style light and dark; honor the viewer's theme toggle.
5. **Typography & hierarchy**: intentional type scale, spacing, and restraint over templated defaults.
