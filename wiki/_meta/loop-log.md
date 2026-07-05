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

## loop(8) — 2026-07-04
Re-verification batch mode (7 agents, ~0.51M tokens, ~27 min): news-first
then 6 claim groups in parallel with disjoint page ownership. News: zero
changes, IPO still pending, all feeds quiet. Batch resolved ~13 backlog
claims: Figure 03 height corrected to official 1.73 m; ">1,000 Gen 3 at
Fremont" REFUTED (aggregator-only; both pages now say "several hundred,
primarily for learning" per Musk Q4'25 call); H2 price conflict resolved as
channel tiering ($29.9K direct standard / $40.9K distributor Commercial /
$68.9K EDU / H2 Plus $100K); Tesla-Proception settlement multi-source
confirmed; Meituan stake corrected to 9.65% combined (largest external);
UniPwn confirmed (Bin4ry/Finisterre, 2025-09-20 disclosure); Honor Flash
half-marathon independently confirmed (SciAm/CBS/NPR); "100+ Chinese VLAs"
attributed to ResearchInChina report; investment.md: World Labs/AMI/Wayve
rounds confirmed CLOSED (stale "in talks"), "Shihang $1B" refuted as
Crunchbase yuan/dollar error (~$140M actual), tracker-divergence note
added; MirrorMe Bolt verified real (ZJU spinout); CoT got real numbers
(Hwangbo 2019 et al.); shipment-count reconciliation table added to
state-of-the-art. Orchestrator applied 5 cross-page propagation edits
(H2 row on company-unitree, World Labs on key-people/academic-labs,
shipment attribution on history/humanoid-robots); remaining propagation
queued. Next: loop(9) — IPO watch + propagation batch + New Yorker piece
(2026-07-06 issue) if published.

## loop(9) — 2026-07-04
Three-track pass (5 agents, ~0.47M tokens, ~20 min), disjoint page
ownership. NEWS/IPO: no pricing yet (confirmed via SSE trail + Chinese
searches ~15:30 CST); enriched company-unitree + investment with verified
post-registration mechanics (SSE 5-working-day window → offering could
launch week of 2026-07-06; retail eligibility rules) and flagged a
2025-profit-measure conflict (GAAP ~RMB 278-300M vs adjusted ~RMB 591-600M)
for resolution from the offering prospectus. PROPAGATION: all 9 items
landed (world-model funding-wave section on world-models.md; Neura
milestone-contingency; Unitree 5,500-attribution on locomotion/tech-tree;
AgiBot World verified paper figures on data.md; AgiBot backdoor-listing
denial on organizations.md; GR-3 disambiguation; glossary CoT datapoints;
Black Panther II 13.17s televised 100m + company-video-only 13.4 m/s peak).
NEW YORKER: full Witt text retrieved; verified surgical additions to
open-problems (field-reported data-gap color, hand-as-missing-link hedge)
and evaluation ("crisis gone mainstream" bullet); verify pass fixed 2
attribution overstatements; 7 rich leads queued (1X Neo data, NVIDIA
ubiquity quote, Neura mocap program, G1 BT botnet → safety page, etc.).
Next: loop(10) — IPO watch (inquiry announcement could land w/o 07-06),
Witt-leads batch, ByteDance GR-3 into vla-models.

## loop(10) — 2026-07-04
Witt-leads batch + IPO forensics (5 agents, ~0.48M tokens, ~21 min).
IPO: still no pricing at China market close; recorded working SSE/Eastmoney
JSON probe endpoints in the queue for future sweeps; earliest formal launch
week of 2026-07-06. RESOLVED the Unitree 2025 profit-measure conflict with
primary STCN quotes: GAAP net profit 2022 −¥22.1M / 2023 −¥11.1M / 2024
¥94.5M / 2025 ~¥288M; the ~¥600M figure is 扣非净利润 (CSRC-standardized,
+674%) — news-verify even reverted an earlier over-correction on
state-of-the-art. Documented the A-share proxy mania (limit-up wave
2026-07-03, 首开股份 ~0.3% indirect stake repeat mania) in investment.
WITT BATCH: all 5 leads applied (1X NEO data incl. 10k deposits marked
company-reported; NVIDIA ubiquity quote + 60%-battery-drain datapoint; Neura
mocap program + Waymo 500k-h precedent into data/data-foundry; G1 BT botnet
into safety-regulation; Stanford adoption survey into open-problems) —
verify pass corrected 3 attribution nuances (survey is 2025 AI Index ch.8 /
Ipsos 2024; deposits not independently verified). GR-3 found already
covered (dedup held); FITEE erratum checked from full PDF — affiliation-only,
CoT numbers stand. Next: loop(11) — IPO inquiry announcement (SSE window),
routine sweep; queue is mostly event-driven watch items now.

## loop(11) — 2026-07-04
Light pass (5 agents, ~0.35M tokens, ~21 min). IPO probe via recorded
SSE/Eastmoney JSON endpoints: no announcement (Saturday, markets closed);
next window is the 07-06 trading week. PEOPLE FLOWS all verified and
upgraded: Sangbae Kim → Meta Robotics Architect (2025-03, MIT on-leave,
"Metabot" program under Marc Whitten w/ ex-Apple Jian Zhang), Pertsch → PI
(own site), Aditya Ramesh VP-of-Robotics confirmed, Kalinowski departure
OpenAI-confirmed (stale "(no OpenAI confirmation)" marker removed), Meta
ARI acquisition enriched (Pinto + Xiaolong Wang → Superintelligence Labs).
KOREA section rebuilt on primary MOTIE releases: chip-figure conflict
resolved as scope difference (W800T fabs vs W881T incl. packaging; USD
conversions are outlets' own), Hyundai "$5.8B" decoded as W9T Saemangeum
hub breakdown, K-Humanoid Alliance KRW 1T primary-verified, fab sites
explicitly undecided, MSIT's separate W50.4B consortium disambiguated —
verify pass then fixed 8 more nuances (venue 迎宾馆 not Blue House, etc.).
Orchestrator fixed Jasmine Hsu residue on key-people (aligned with
company-pi refutation). Queue: 2 items closed, Korea follow-ups queued.

Next: loop(12) — Monday IPO window opens; investment.md Korea fold-in;
routine sweep.

## loop(12) — 2026-07-04
Weekend light pass (4 agents, ~0.25M tokens, ~10 min). Sweep found a real
COVERAGE GAP dating to April: State Grid's leaked 2026 Embodied
Intelligence Development Plan — RMB 6.8B for ~8,500 robots (5,000
quadrupeds / 3,000 dual-arm / 500 humanoids at ~RMB 5M/unit) — added to
landscape-china with single-leaked-document caveats; it is the landmark
order Morgan Stanley cited when raising its 2026 China forecast to 50K;
verify pass added the primary Jiemian exclusive and flagged 36Kr's
Zhipu/AgiBot mistranslation. Korea fold-in to investment.md completed and
verified (fab-siting nuance: Samsung's Lee publicly named Gwangju at the
briefing — "undecided" was overstated; state-led vs chaebol-capex framing
fixed for internal consistency). IPO: zero movement (Saturday); Monday
07-06 window armed. Queue: New Yorker item closed (done loops 9-10); State
Grid tender-watch added. Next: loop(13) — Sunday quiet cycle expected;
Monday brings the IPO window + Chinese trading week.

## zh-mirror — 2026-07-04 (loop paused)
User paused the loop after loop(12) and requested a full Chinese edition.
Built wiki-zh/: all 30 pages translated to Simplified Chinese (same slugs,
lang: zh + source: frontmatter, cross-links preserved, source URLs intact,
"(unverified)" → "(未证实)" etc. mappings). Pipeline: per-page translate →
per-page QC; first 21 pages translated on Fable-5-low, then switched to
Sonnet-5 per user request (remaining 9 translate + all 30 QC on Sonnet).
QC fixed 5 issues (tool-call artifact leak in glossary, "headline"
leftovers, a translator's bracketed self-note in company-unitree corrected
to ~$300M). Published the Chinese reader artifact (see LOOP.md State) and
recorded the zh sync rule + PAUSED status in LOOP.md. Loop resumes only on
user request; hot watch item remains Unitree IPO pricing (week of 07-06).

## tier2-visions batch — 2026-07-05 (loop still paused; directed build)
User set new direction: companies = top priority (tech route/bets/SWOT per
player), leader theses next, and the endgame is an ODM boss-pitch (market
size, entry points, 友商 moves, FOMO). Built 7 pages via 4-stage pipeline
(research Fable → verify Fable → translate Sonnet → QC Sonnet), 28 agents,
~2.3M tokens, ~1h42m: visions (13 corrections — Musk composite quotes
restored to verbatim transcripts, Brooks attribution fixed, Huang CES line
is video narration not spoken), company-bostondynamics (13 — official spec
sheet 1.9m/90kg, 100% Hyundai ownership verified, DHL is MoU not order),
company-agility (13), company-1x (9), company-skild (10), company-agibot
(8), company-ubtech (13). All EN verified; all zh synced. Cross-page fixes
applied (landscape-usa BD ownership, locomotion Atlas date). ODM gold:
Lens Tech × AgiBot assembly JV = first real humanoid-EMS test; Foxconn ×
Agility PIPE + manufacturing. HOME/llms.txt at 36 pages, zh HOME synced.
Queue: ODM-pitch track added (odm-opportunity page next, then Chinese-first
boss deck). GitHub push still blocked on deploy key.

## odm-opportunity — 2026-07-05 (directed build; main model now Opus 4.8)
Built the ODM opportunity map (5 agents: Sonnet fact-gathered 15 ODM/EMS
moves, high-tier synthesized + verified, Sonnet translated + QC'd). Verify
caught the key aggregator-pollution items for the pitch: the circulated
"Luxshare won China Mobile ¥124M humanoid order" is FALSE (won by AgiBot
¥78M + Unitree ¥46M per guancha primary; only leaderobot syndicated the
Luxshare version); Wistron ≠ 上纬/Shangwei (AgiBot's STAR vehicle launching
Qiyuan Q1). 14 corrections total incl. date fixes and the Figure-BMW
skeptic bullet corrected to match company-figure. Honest core: 2026 global
humanoid hardware pool ~$2B (Morgan Stanley China ~$2B, IDC 2025 ~$440M) —
tiny vs Goldman $38B/2035 and Huang's $40-50T wage rhetoric — but 2026-27
is the design-win window (Jabil-Apptronik, Lens-AgiBot JV, Foxconn-Agility
PIPE). HOME/llms.txt at 37 pages, zh synced, both readers rebuilt (39 EN /
38 zh incl. meta). Next: Chinese-first boss pitch deck (needs user's ODM
profile answers). Loop paused; GitHub push still awaiting deploy key.
