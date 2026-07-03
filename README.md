# physicalAI — a self-updating LLM-wiki on Physical AI

A git-versioned, LLM-maintained knowledge base covering **Physical AI worldwide**:
history, state of the art, the technology tree, key people and organizations,
regional landscapes (US, China, Europe, Japan/Korea, rest of world), hardware,
data/benchmarks, investment, and open problems.

## How it works (the loop)

This repo is maintained by an autonomous research loop (see [LOOP.md](LOOP.md)):

```
Orient → Research (multi-agent web fan-out) → Verify (adversarial fact-check)
       → Integrate (write/refresh wiki pages) → Commit → Sleep → repeat
```

Every change is a git commit (`loop(N): ...`), so `git log` **is** the audit
trail of what the wiki learned and when.

## Reading the wiki

- Start at [wiki/HOME.md](wiki/HOME.md) — annotated index and reading order.
- [llms.txt](llms.txt) — machine-readable index (llms.txt convention).
- Every page carries frontmatter with `updated:` (last research pass) and a
  `Sources` section with URLs. Volatile claims are stamped "as of YYYY-MM".

## Conventions

See [CLAUDE.md](CLAUDE.md) for the page format and maintenance protocol.
