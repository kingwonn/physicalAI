# physicalAI wiki — maintenance protocol

This repo is an **LLM-wiki**: markdown pages optimized for LLM (and human)
consumption, maintained by an autonomous research loop. Any session working
here follows this protocol.

## Repo layout

```
README.md            what this repo is
LOOP.md              loop engineering: how iterations run, pacing, freshness policy
llms.txt             llms.txt-convention index (keep in sync with wiki/)
wiki/HOME.md         annotated index + field overview
wiki/<slug>.md       one topic per page, stable kebab-case slugs
wiki/_meta/loop-log.md   append-only iteration log (one entry per loop pass)
wiki/_meta/queue.md      research backlog (topics to add / claims to re-check)
```

## Page format

```markdown
---
title: <Title>
slug: <kebab-slug>            # must equal filename
updated: YYYY-MM-DD           # date of last research/verify pass
confidence: verified | draft  # verified = passed an adversarial fact-check
---
> One-paragraph summary readable in isolation.

<sections: bullet-dense, factual, tables where apt>

## Sources
- <url> — one-line note on what it supports
```

Rules:
- Cross-link sibling pages with relative links: `[Humanoids](humanoid-robots.md)`.
- Stamp volatile facts (funding, model SOTA, headcounts) "as of YYYY-MM".
- Uncertain or single-source claims get an explicit `(unverified)` marker.
- Never delete a page; supersede content in place and let git keep history.
- Prefer primary sources (papers, company posts) over aggregator articles.

## Change discipline

- Every loop iteration = one commit: `loop(N): <what changed>` on `master`.
- Append an entry to `wiki/_meta/loop-log.md` in the same commit.
- Update `wiki/HOME.md` and `llms.txt` whenever pages are added/renamed.
- Freshness: any page whose `updated:` is >14 days old is due for a refresh
  pass; a news sweep runs every iteration regardless (see LOOP.md).
