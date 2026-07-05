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

## Model tiering (user directive, 2026-07-04/05)

Workflow agents run on tiered models to control cost:
- **Sonnet** (`model: 'sonnet'`, usually `effort: 'low'`): translation + zh QC,
  routine research (news sweeps, feed scans, IPO/API probes, fact-gathering on
  well-documented topics), propagation/index maintenance.
- **Fable** (session default): adversarial verification, precise-quote research
  (executive statements for the pitch), synthesis/SWOT/judgment pages,
  orchestration.

## Unknowns discipline (added 2026-07-04 after a self-review)

Lessons from loops 0-12, framed per "map vs territory":
- **Interview first.** Before any major new build, ask the user 2-3 questions
  whose answers change the architecture (output language, delivery format,
  cost tier). Every mid-project pivot so far (HTML views, source audit,
  Sonnet tiering, Chinese edition) was an *unknown known* — obvious to the
  user, never asked by the loop.
- **Blind-spot pass.** When entering a new domain/page area, spend one agent
  on "what are the unknown unknowns here" before fanning out researchers.
- **Aggregators are systematically unreliable** (fabricated counts, currency
  misreads, misattributions). The verify layer exists because of this; never
  weaken it. Secondary sources are leads; only primaries are facts.
- **Territory lessons already encoded**: inline workflow params (args can
  fail), resumeFromRunId + fallback heartbeats (processes die), one-file-only
  agent scoping (agents drift), disjoint page ownership (edit races).

## Invariants

- The repo is always in a committed, self-consistent state at the end of an
  iteration (no half-written pages left uncommitted).
- Every factual change traces to a URL in the page's `Sources`.
- Iteration numbering is monotonic; the counter lives in the loop log.
- The loop never deletes history — corrections supersede, git remembers.

## Chinese mirror (wiki-zh/)

- Full Simplified-Chinese translation of every wiki page lives in `wiki-zh/`
  (same slugs; frontmatter adds `lang: zh` + `source:`). Built 2026-07-04 by a
  30-page translate+QC workflow (translation on Sonnet-class agents).
- **Sync rule:** when a loop iteration changes English pages, the Publish step
  should re-translate the *changed pages only* into `wiki-zh/` (Sonnet-class
  agents) and redeploy the Chinese reader below.

## Loop status

- **PAUSED by user 2026-07-04 after loop(12)** (commit 678e0fe). Do not start
  new iterations until the user asks to resume. Watch items remain queued in
  `wiki/_meta/queue.md` (hot: Unitree IPO pricing, week of 2026-07-06).

## State

- **Iteration counter + narrative log:** `wiki/_meta/loop-log.md`
- **Backlog:** `wiki/_meta/queue.md`
- **Per-page freshness:** `updated:` frontmatter on each page
- **HTML dashboard (redeploy to this exact URL every iteration):**
  https://claude.ai/code/artifact/821047d4-fdd2-44a8-b26e-0034119ae56f
- **English full-text reader:**
  https://claude.ai/code/artifact/68ac0327-eba9-4992-b59e-f0a842129433
- **Chinese full-text reader (wiki-zh/):**
  https://claude.ai/code/artifact/4fe05af7-9241-4177-b7b5-296486977015
