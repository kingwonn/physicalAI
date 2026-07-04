# Loop log (append-only, newest last)

## loop(0) — 2026-07-03
Scaffolded the repo: README, CLAUDE.md (page protocol), LOOP.md (loop
engineering), wiki/_meta state files, llms.txt skeleton. Next: loop(1) initial
deep-research build — 15 pages via multi-agent research + adversarial verify.

## loop(1) — 2026-07-03
Initial deep-research build: 18 pages via a 36-agent workflow (one web-research
agent + one adversarial fact-checker per page; ~2.4M tokens, 1034 tool calls,
~2h wall clock, one mid-run process restart resumed from the journal). All 18
pages passed verification; fact-checkers applied ~150 corrections (examples:
BMW-Leipzig pilot is Hexagon AEON not Figure; Counterpoint vs TrendForce
forecast conflation; Unitree IPO timeline/raise precision; Gemini Robotics
benchmark claim reattributed to ER 1.5). Dropped 2 uncommitted agent
intermediates (sota-foundation-models, world-models-simulation) superseded by
vla-models/state-of-the-art/world-models/simulation. Wrote HOME.md, refreshed
llms.txt + README + LOOP.md (added Publish step + console URL), distilled 54
research leads into the queue. Published HTML console v2 (build-complete state).
Next: loop(2) light pass — news sweep + 1-3 queue picks.

## loop(2) — 2026-07-03
Light pass (6 agents, ~0.4M tokens, ~20 min): global news sweep + 2 queue
pages. New pages safety-regulation (9 verify corrections) and glossary (5),
both verified. News sweep patched 5 spots across landscape-china,
landscape-usa, humanoid-robots, state-of-the-art: UBTech UWORLD U1 consumer
launch (2026-06-30, from ~$16.7k), Unitree CSRC approval (2026-07-02, not
07-03 as first reported), Apptronik Apollo 2 + Robot Park, Tesla Fremont
Optimus line delivered/installing. News verify pass corrected 4 details
(photo-not-video walkthrough, line delivered-not-installed, approval date).
Six watch items checked, no news (PI round close, AgiBot HK, Agility SPAC,
policy, frontier models, EU/JP/KR). HOME/llms.txt now list 20 pages; queue
pruned + 3 new watch items. Next: loop(3) light pass — news sweep + queue
picks (tactile/dexterous-hands page or evaluation-crisis page).

## loop(3) — 2026-07-03
Light pass (5 agents, ~0.4M tokens, ~18 min): 2 queue pages + narrow news
check. New pages tactile-hands (10 verify corrections — notably Unitree
Dex5-1 price refuted from ~$7-8k to $25-27k reseller pricing; silicone-skin
durability claim reattributed to the ORCA study) and evaluation (7
corrections), both verified. News check: ZERO changes needed — all watch
items (Unitree IPO details, Tesla Fremont line, Hyundai-SoftBank BD stake,
Figure BotQ ramp, NVIDIA stack) already on the pages; wiki is current with
the news cycle. HOME/llms.txt at 22 pages; queue: 2 done, 2 watch items
added. Next: loop(4) — news sweep + queue picks (per-company deep pages or
data-foundry economics or academic lab map).

## loop(4) — 2026-07-04
Company deep pages + first full-stack news sweep (6 agents, ~0.5M tokens,
~23 min). New pages company-figure (6 verify corrections — BMW pilot
provenance precision, Hark upgraded to multi-source verified) and
company-unitree (5 — GUARD Act date 2026-06-04, overseas revenue >55%
2022-24), both verified. News sweep NOW USES community+media signals
(last30days engine: Reddit/HN/Polymarket; RSS watchlist: Robot Report, IEEE
Spectrum, BD/Unitree YouTube, Lex Fridman): patched the same-day 2026-06-29
Shenzhen "model-first" funding pair (X Square Robot >$2.8B, AI² Robotics
~$735M at ~RMB 20B) into landscape-china/vla-models/investment; verify pass
corrected 4 details (IDG participated-not-led etc.). Resolved Unitree YouTube
channel RSS into feeds.md. Fixed cross-page contradiction: Unitree was
already profitable in 2024 (humanoid-robots.md said "first profitable year"
2025). Community signals logged as leads only (New Yorker deployment-
readiness feature queued). Unitree IPO pricing: still pending, watch is hot.
HOME/llms.txt at 24 pages. Next: loop(5) — news sweep (IPO watch) + queue
picks (PI / NVIDIA-stack / Optimus company pages, or academic lab map).

## loop(5) — 2026-07-04
Company deep pages round 2 (6 agents, ~0.56M tokens, ~22 min). New pages
company-pi (6 verify corrections — "Jasmine Hsu" co-founder claim killed,
pre-revenue framing precisioned) and company-nvidia (6 — GR00T reference
humanoid date 2026-05-31, CoRL vs CES release URL misattribution fixed),
both verified. News sweep (full stack): Unitree GD01 manned mecha
(2026-05-12, ~$574K) + WVLA 2.0 demo added to company-unitree; Figure
200-hour livestreamed endurance run (~249,560 packages, 2026-05-13→22)
added to company-figure; news-verify tightened 7 details (San Jose vs
Sunnyvale conflict flagged, "zero crashes" precisioned to system-halting).
Figure YouTube RSS resolved into feeds.md. Cross-page fix: landscape-usa
espresso demo 13h → ~18h per PI blog. Unitree IPO pricing STILL pending.
HOME/llms.txt at 26 pages. Next: loop(6) — IPO watch + Tesla Optimus page
and/or academic lab map; consider lengthening interval if news stays dry.

## loop(6) — 2026-07-04
Company series finale + academia (6 agents, ~0.53M tokens, ~24 min). New
pages company-optimus (7 verify corrections — V3 reveal guided "mid-2026"
not late-July; hand-patent mechanism abandoned per Musk; Tesla Diner
teleop softened to "reported") and academic-labs (2 — Spirit AI and Sunday
Robotics founding years corrected to 2024), both verified. News sweep:
MIIT+SASAC "2026 real-scene training special action" (launched 2026-06-09;
primary-sourced official notice 工信厅联科函〔2026〕256号: ten provinces +
central SOEs, 100+ scenarios, 10,000-unit-scale deployment capacity by
end-2026) added to landscape-china policy timeline; verify pass upgraded
deadlines to primary-sourced and completed the province list. NVIDIA blog
RSS resolved into feeds.md; JAL×GMO Haneda humanoid trial queued with JAL
primary source. Unitree IPO pricing STILL pending (US July-4 holiday, quiet
cycle). HOME/llms.txt at 28 pages. Company deep-page series COMPLETE
(Figure, Unitree, PI, NVIDIA, Optimus). Next: loop(7) — IPO watch +
data-foundry economics page or JAL/landscape-row refresh; consider
lengthening interval through the US holiday weekend.

## loop(7) — 2026-07-04
Data-foundry page + assigned refresh (4 agents, ~0.34M tokens, ~19 min).
New page data-foundry verified after 11 corrections — the fact-check pass
was unusually productive: payment-direction reversal on the Rest of World
in-home data-collection anecdote, Eric Jang's 1X departure (2026-01), Aria
partner-count fix, AgiBot Lingang 4,000m² vs 3,000m² conflict flagged from
the primary paper, multiple citation-URL repairs. News agent completed the
assigned JAL Haneda write-in (landscape-row Japan, cost conflict kept with
explicit attribution) and added Korea's ">$1T triple axis" national AI
strategy (2026-06-29, humanoids as national strategic industry) — verify
pass added JAL Ground Service attribution and initial two-unit test-phase
detail. Community signals: Weave Robotics Isaac 1 ($7,999 home robot, HN
232pts) queued. Unitree IPO pricing STILL pending. HOME/llms.txt at 29
pages. Next: loop(8) — IPO watch + queue picks (Optimus follow-ups,
shipment-methodology reconciliation, or New Yorker read once published).
