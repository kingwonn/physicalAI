# LOOP.md — loop engineering for the physicalAI wiki

Design notes for the autonomous maintenance loop ("boris loop" style: a small,
verifiable unit of work, executed forever, with the plan and the state living
in the repo itself so any fresh session can pick it up cold).

## The loop

Each iteration is one pass of:

1. **Orient** — read this file, `wiki/_meta/loop-log.md` (last entry), and
   `wiki/_meta/queue.md`. Decide the iteration's scope: refresh stale pages,
   pull items off the queue, and always do a news sweep.
2. **Research** — fan out web-research agents (one per topic/page). Agents
   search, read primary sources, and write/update the page directly.
   *Community signals:* news-sweep agents may additionally run the
   `last30days` engine (`python3 ~/.claude/skills/last30days/scripts/last30days.py
   <topic> --quick --search reddit,hackernews,polymarket --emit compact`) to
   surface Reddit/HN/Polymarket discussion from the last 30 days. Treat
   community content as *leads and sentiment*, never as verifiable facts —
   anything promoted to a page still needs a primary source. (X/YouTube/TikTok
   in that engine need API keys we don't have; 小红书/微信公号/知乎 are not
   supported by it at all and remain a known blind spot.)
   *Media feeds:* sweep agents should also scan the RSS watchlist in
   `wiki/_meta/feeds.md` (blogs, YouTube channel feeds, podcast feeds — all
   zero-config; connectivity verified 2026-07-04). Same rule: leads/sentiment
   only, facts need primary sources.
3. **Verify** — adversarial fact-check agents re-derive the highest-stakes
   claims (dates, dollar amounts, model names, SOTA assertions) from
   independent sources and fix errors in place. Pages that pass get
   `confidence: verified`.
4. **Integrate** — fix cross-links, refresh `wiki/HOME.md` + `llms.txt`,
   append to the loop log, push new leads onto the queue.
5. **Publish** — regenerate the HTML console dashboard (single self-contained
   file, Chinese chrome: status chips, page pipeline, log, queue) and redeploy
   it to the SAME Artifact URL recorded under State below (pass it as the
   `url` param; keep favicon 🤖 stable). The user reads loop output here.
6. **Commit** — single commit `loop(N): <summary>` on `master`.
7. **Sleep** — self-paced wake-up (see pacing), then go to 1.

## Pacing policy (self-paced)

- News moves on ~hours-to-days timescales for this field; the loop wakes every
  **~30–60 min** for a light pass (news sweep + 1–3 stale/queued pages) rather
  than rebuilding everything each time.
- A **full refresh** (all pages re-verified) is due when the oldest page's
  `updated:` exceeds 14 days.
- If two consecutive iterations produce no meaningful change, lengthen the
  interval; shorten it again when a sweep finds real news.

## Invariants

- The repo is always in a committed, self-consistent state at the end of an
  iteration (no half-written pages left uncommitted).
- Every factual change traces to a URL in the page's `Sources`.
- Iteration numbering is monotonic; the counter lives in the loop log.
- The loop never deletes history — corrections supersede, git remembers.

## State

- **Iteration counter + narrative log:** `wiki/_meta/loop-log.md`
- **Backlog:** `wiki/_meta/queue.md`
- **Per-page freshness:** `updated:` frontmatter on each page
- **HTML dashboard (redeploy to this exact URL every iteration):**
  https://claude.ai/code/artifact/821047d4-fdd2-44a8-b26e-0034119ae56f
