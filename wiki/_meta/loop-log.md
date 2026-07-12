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

## Quectel boss-pitch — 2026-07-05 (directed; Opus synthesis + Sonnet research)
Built the Quectel (移远通信) opportunity-fit analysis (pitch/quectel.md,
verified) and a Chinese-first executive pitch deck (pitch/quectel-pitch.html
+ Artifact). Research (Sonnet, 3 parallel) → synthesis + verify (Opus).
KEY REFRAME: Quectel has ALREADY entered robotics 2+ yrs — SG885G(48
TOPS)/SH602HA-AP(CES2026)/SP895BD-AP(77 TOPS) compute-module ladder, Robrain
brain co-launched with LimX on TRON1 biped (MWC Shanghai 2025-06), Unitree
quadruped module in mass production (secondary), ¥411M AI-robotics line in
the 2025 ≤¥2.3B placement — so the pitch is "scale, not enter". Arms-dealer
thesis (Intel Inside + 高德, not Foxconn). Honest 3-tier sizing ($40-50T wage
TAM ≠ ~$20 億 hardware ≠ $3-8億/yr module SAM). FOMO scoreboard: 美格/
Thundercomm/高通/NVIDIA/广和通 all moved in past 18 months. Verify killed a
decision-grade error: Fibocom's 珞博 investment is AI-companion-TOY (Fuzozo),
not humanoid. Deck design: instrument-panel/oscilloscope identity (slate ink
+ signal-teal + heat-orange, mono data readouts, canvas signal waveform).
Pitch target recorded in memory. Loop paused.

## GitHub push — 2026-07-05
Pushed the full repo to https://github.com/kingwonn/physicalAI (master →
main, 25 commits) via an SSH deploy key (added by user with write access).
Contents: 38-page bilingual wiki (wiki/ + wiki-zh/) + pitch/ (Quectel
analysis, HTML briefing, .pptx deck) + protocol/meta. Remote is now the
canonical mirror; future work can push incrementally (git push). Loop
remains paused.

## funding-timeline — 2026-07-05 (directed; Opus verify + Sonnet collect)
Built a Physical-AI funding timeline: harvested every funding/valuation/IPO/
M&A event from the verified wiki + gap-filled by era via 4 parallel Sonnet
collectors (2015-2022 / 2023-2024 / 2025 / 2026-H1), deduped in code
(157 events after merge, 2013→2026-07), Opus verified the 30 largest and
applied 8 corrections: PI ~$1B@$11B and 1X ~$1B@$10B marked NOT-CLOSED
(reported/in-talks, excluded from totals); Scale AI / AMI Labs / World Labs
double-counts removed; Mind Robotics recategorized (Rivian industrial spin-
out, amount fixed to $500M); BD Hyundai rights offering ~$870M. Result:
~$90B disclosed-closed across 157 events, clear hockey stick (2024:25 →
2025:42 → 2026-H1:31). Deliverable: viz/funding-timeline.html (interactive,
filter by category/region/mega, source-quality chips, not-closed flags) +
dataset wiki/_meta/funding-events.json. Loop paused.

## odm-competitors — 2026-07-05 (directed; 5 Sonnet collectors + Opus synth/verify)
Built a deep ODM/EMS/module-maker competitor page (9 agents, ~0.67M tokens):
16 companies across Taiwan EMS (Foxconn, Quanta/Techman, Wistron, Compal,
Pegatron, Inventec), China ODM/EMS (Luxshare, BYD Electronics, Huaqin,
Longcheer, Wingtech, Lens), module makers (Quectel[ref], Fibocom, MeiG,
Thundercomm) — commitment-ranked scoreboard + per-company profiles across
4 dimensions (product-line / investment / design-win / deployment) + a
synthesis (committed-vs-announcement, own-brand-vs-arms-dealer) + Quectel-
specific read. HEADLINE FIND: the steel-in-the-ground leaders are China
A-share ODMs assembling domestic champions, NOT the Taiwan giants —
Longcheer runs AgiBot 精灵 G2 on a live Nanchang 3C line (~1,000-unit
framework order, scaling 4→~100 by Q3 2026); Lens holds 70% of the AgiBot
JV. Foxconn is the arms-dealer's arms-dealer (Agility PIPE, no own brand).
Luxshare is the own-brand/channel-conflict case (~3,000 self-robots 2025).
Verify (Opus) applied 7 corrections incl. Lens 70% stake, MeiG partner =
AidLux (not Airha), Foxconn LH-L02 hand claim flagged unverified,
Wistron≠上纬 entity-separation source added; re-confirmed Luxshare did NOT
win the China Mobile tender (AgiBot+Unitree did). EN verified + zh synced.
HOME/llms.txt at 38 pages, zh synced, both readers rebuilt (40 EN / 39 zh).
Loop paused.

## docs/ HTML site — 2026-07-05
Consolidated all HTML deliverables into the repo under docs/ (GitHub-Pages-
ready): index.html hub + reader-en.html + reader-zh.html + console.html +
funding-timeline.html + quectel-pitch.html. Previously only pitch/quectel-
pitch.html and viz/funding-timeline.html were in the repo; the readers and
console existed only as Artifacts. Now the whole bilingual wiki (incl.
odm-competitors) is browsable as HTML from the repo. Prepended doctype+utf-8
to the Artifact-fragment files for standalone/Pages serving. Enable Pages
(Settings → Pages → main /docs) to serve the portal live. Loop paused.

## component supply-chain integration — 2026-07-05
Component page zh mirror confirmed (wiki-zh/component-supply-chain.md, from
the workflow Sync phase), added to zh HOME + both readers. Built interactive
HTML (docs/component-supply-chain.html + Artifact): BOM value-chain map
(9 subsystems, cost% + chokepoint color) + 5 sub-chain supplier scoreboards
(~28 suppliers, filter by commitment/region) + Quectel read. Added to docs/
portal. Readers rebuilt (41 EN / 40 zh). EN page kept confidence:draft
(many single-source Chinese-media rows) — flagged in HTML + queue for a
future adversarial verify pass.

## on-device-brain deep-research loop — COMPLETE 2026-07-05
7 iterations (6 planned A-L + 1 gap-fill M-N) over a sustained research loop:
each sub-topic Sonnet-collected → Opus-written → Opus-adversarially-verified,
all load-bearing numbers checked vs arXiv/vendor primaries. Assembled into
wiki/on-device-brain.md (14 sections, ~1248 lines, confidence: verified) +
zh mirror + reference-architecture HTML (docs/on-device-brain.html, v2 with
security block). Completeness critic confirmed zero cross-section numeric
contradiction, fixed 15 dead links, flagged 4 gaps (2 closed by M/N).
Thesis: on-device the binding constraint is memory-bandwidth + reliability/
generalization, not TOPS; the win is the S2/S1/S0 tiered split; for a module
maker the on-device brain is the defensible arms-dealer lane. Notable finds:
Jetson Thor has NO confidential-compute/TDISP (dGPU-only); RoboPAIR 100%
robot-jailbreak; MPS has no priority preemption. HOME/llms/readers at 42 EN /
41 zh; portal 专题深度报告 section. Loop paused (news-freshness loop still off).

## on-device-brain §O players critical eval — 2026-07-06
Added Section O (主要玩家方案与批判性评价): 12 players across 3 camps
(Western frontier / Chinese humanoid / module-chip suppliers), each graded
against the §K rubric + §L reference stack. Verdict verified. Key findings:
inference-local is genuinely shipped by Figure/UBTech Walker S2(i7+Orin)/
Unitree UnifoLM-VLA-0/Gemini-On-Device/GR00T·pi0-on-Thor; NOT on-device by
default (self-documented) = PI openpi (policy server over websocket) + Skild
(cloud SaaS); Tesla Optimus = strongest teleop/vaporware evidence (We-Robot
+ Diner remote-op, Musk "for learning", AI5 volume mid-2027). Open players
most trustworthy (reproducible). Verify caught the AgiBot GO-1/G2 conflation
(factory livestream was G2 not GO-1) + Quectel SH602 memory unverified. Page
now 15 sections A-O bilingual; HTML v3 adds a players-critical table.

## data-collection-devices — 2026-07-06 (loop; 8 agents ~0.6M tokens)
New page data-collection-devices.md (verified, bilingual): 60 data-collection
devices/rigs across 3 families + a critical comparative evaluation. 5 Sonnet
collectors (UMI-family / egocentric-video+gloves / teleop-leader-follower /
teleop-VR-haptic-mocap / player-programs) -> Opus synthesis + verify ->
Sonnet zh. Core: a 3-family tradeoff MATRIX (cost/throughput/embodiment-gap/
action-fidelity/force/scalability) with per-axis verdicts — you can't have
cheap-scalable AND clean-zero-gap from one device. Verify corrections: ALOHA
2 cost fixed to ~$22k stationary (not $32k, which needs a mobile base),
FastUMI tracking error -> range (10.5-24mm), AgiBot daily rate + Generalist
corpus/rate marked unverified, iDP3 quote fixed, DROID 13-institution
consistency, Dobb-E iPhone-odometry precision. Read: embodiment-free wins
pretraining scale, teleop wins the last mile; field converged on
pretrain-cheap+fine-tune-clean hybrids; the rig-hardware business is a
low-margin volume niche, not a moat. Interactive comparison HTML +
portal. HOME/llms/readers at 43 EN / 42 zh.

## data-collection-devices +system-designs +china-ecosystem — 2026-07-06 (loop; 2 parallel workflows, 12 agents ~0.8M tokens)
Two parallel Workflow runs deepened data-collection-devices.md (both verified,
bilingual). (1) Detailed SYSTEM DESIGNS: a new "系统方案设计详解" section — a
shared 3-block architecture (sensing rig -> pose/action-recovery -> data format)
+ a design-pattern comparison table + 10 per-system engineering breakdowns
(UMI/FastUMI/DexUMI/Dobb·E/DexCap/ALOHA 2/GELLO/DROID/Open-TeleVision-VR/
Aria-egocentric), each with composition/sensors/mechanical/pipeline/software/
BOM/design-read. Verify fixed UMI tracking label (6.1mm/3.5° per-gripper ATE
vs 10.1mm/0.8° inter-gripper RPE — NOT inter-frame), AgileX Tracer spelling,
+ (unverified) on the DexUMI Alps encoder part#. (2) CHINA ECOSYSTEM: a new
"中国数据采集生态" section — a 16-player scoreboard (星海图 Galaxea / 智元 /
银河通用 / 千寻 / 自变量 / 逐际 / 穹彻 / ByteDance Seed / 松灵 Cobot Magic /
帕西尼 PaXini / GenRobot / 它石 Morphic / 光轮 LightWheel / 张江+亦庄 训练场 /
京东 Suqian) + genrobot RESOLVED (= GenRobot 简智新创 Beijing, NOT AgiBot's
Genie Studio). Verify: PiPER reach 626mm (not 610), removed unverified
Zhangjiang welding/3C scenario triad, JD gig wage $3/h confirmed but "$5-20/h"
marked unverified, Galaxea "400k downloads" flagged (HF shows ~13k/mo), PaXini
DexH13 sourced to mall.paxini.com. Read: China's edge is cost-structure +
state coordination + buyable hardware (vertically-integrated stack), NOT data
quality/verifiability. HTML deliverable gains ④ 系统方案设计详解 (10 design
cards) + ⑤ 中国数据采集生态 (16-player table w/ type badges + genrobot callout
+ China verdict box). Readers rebuilt 43 EN / 42 zh; portal card + counts updated.

## data-engine-roadmap — 2026-07-06 (design workflow; 10 agents ~0.64M tokens)
NEW page data-engine-roadmap.md (verified, bilingual): our own SOTA
data-collection-system DESIGN PROPOSAL + 18-24mo 3-gen roadmap, derived from
brain-scaling needs (S2/S1/S0 ladder). Judge-panel competition: 3 theses
(A-wearable fidelity-climb / B-convergence collection=deployment sensor head /
C-fleet W/L/R tiered family) x 3 judge lenses (engineering / data-science /
strategy) — each lens picked a DIFFERENT winner; totals C 140 > B 131 > A 125.
Final: C spine (W/L/R mix shifting 80/15/5 -> 60/25/15 -> 30/25/45) + grafts
(A error-budget engineering + native $21 force channel from day 1 + fidelity
SLA certificates; B isomorphic sensor head + no-software-timestamps axiom +
3-layer endgame). Gen-1 COTS ($520 W1 / $726 GELLO L1 / $1,400 R1), Gen-2
custom sensor-head module (2mm/200Hz gate at month 9 + precision-value
ablation), Gen-3 C1 SoC (1us on-chip timestamps, 40 TOPS, $15-25M NRE) +
future sensors (event cam, 1k taxel/fingertip, e-skin). Dated falsifiable
endgame: 2028 category-merge, 2030 inversion (robots collect for robots),
terminal = spine survives as module+SoC+certification-cloud. Verify fixed 8
factual errors (Hero9 discontinued -> Hero13 2nd source, Q-8750 80 TOPS,
ICM-42688 ODR, TAL220 swap, Landot attribution, Aria gaze spec, JD/Shandong
labor case, teleop price timeline) -> confidence: verified. Readers 44 EN /
43 zh. HTML deliverable pending (next iteration, post LeCun-rethink).

## lecun-worldmodels-rethink — 2026-07-07 (research workflow; 6 agents ~0.47M tokens)
NEW page lecun-worldmodels-rethink.md (verified, bilingual): LeCun's ETH
Zurich 2026-05-29 talk "World Models: Enabling the next AI revolution"
investigated (talk PRIMARY-confirmed via LeCun's own post + ETH EFCL event
page + video; no verbatim transcript parsed — in-talk content rests on two
independent secondaries with podcast quotes firewalled from ETH-stage
attribution). Content: (1) faithful reconstruction of the argument chain
(LLM critique / data-efficiency / latent JEPA + MPC / VLA "dead end" [podcast]
/ AMI Labs $1.03B @ $3.5B pre context); (2) claim-by-claim collision with our
verified scaling evidence (GEN-0 unsaturated, EgoScale, V-JEPA 2-AC itself
needs 62h action data; honest "layered both-right" mapping to S2/S1/S0);
(3) critique (steelman + dated track record + fundraising context + 3 blind
spots: force-not-in-video, last-mile reliability, his own 62h close-out);
(4) ROADMAP RETHINK: spine survives; passive ego-video upgraded from
defensive SKU to co-primary product line (W-active/W-passive/L/R quaternary
mix), new pretrain-vs-label gate ablation, force data gains 3rd buyer
(world-model physics calibration), ego-pose ATE certificate = world-model
action-conditioning fidelity certificate; 8 dated watch items. Verify fixed
11 items (departure date, RoboChallenge variance, de-quoted paraphrases,
removed fabricated slide filename, AMI investor roster, Schmidhuber quote
downgrade). data-engine-roadmap.md got a revision pointer. NEW HTML
deliverable data-engine-roadmap.html (roadmap 3-gen cards + requirements
ladder + LeCun collision table + endgame panel + judges/risks). NOTE:
scratchpad build scripts were wiped by tmp cleanup; recovered from transcript
Write/Edit replay — consider committing build scripts to repo. Readers 45 EN
/ 44 zh; portal card + counts updated.

## data-scaling-strategy — 2026-07-07 (red-team + panel workflow; 10 agents ~0.9M tokens)
NEW page data-scaling-strategy.md (verified, bilingual) answering the owner's
three questions. (1) RE-REVIEW: 3-lens red-team of our own data-engine-roadmap
— no lens voted kill; 4 FATAL fixes applied as v1.1 (C1 downgraded to 12/16nm
sensor-hub die at month 30+ w/ >=500k-unit hard gate; revenue gate added
alongside precision gate; R-series restructured as white-label data infra —
customers own data, we own clock/QC/cert SaaS + BOM slot; ladder arithmetic
rebuilt — fully-loaded ~$55/h not $6/h, throughput re-based to 60-70 demos/h
eff.); 15-item change list; roadmap page annotated in place (banner + 2 inline
fatal notes, EN+zh). (2) SCALING-CHANNEL ASSESSMENT: channel defined as
C1 predictability ∧ C2 economic flywheel ∧ C3 transferability; 4-precondition
LLM scorecard (unified substrate PARTIAL, single arch PARTIAL, near-zero
marginal data cost FAIL — the decisive gap, smooth loss-capability PARTIAL);
bull/bear/referee panel P(full@2030) = 0.55/0.17/0.35, our synthesis
0.25-0.35 (point 0.30). KEY INSIGHT: all observed laws are shallow-exponent
(10x hours per capability step) while $/h only falls 2-3x per OOM — the
channel is an economics inequality; the 3-5x gap closes only via deployment
exhaust or passive-video substitution — exactly what our two gate ablations
measure (the gates double as a private measurement instrument for the
industry-wide channel question). (3) STRATEGY: 3-world ownership map (channel
opens ~0.30 / stalls ~0.45-0.50 / paradigm shift ~0.20-0.25 — force/contact
+ correction/failure data + metrology stack valuable in ALL three); 7
principles (barbell, dual gates, sell-picks-own-the-ruler, force-sells-3x,
failure-data-is-product, R-as-white-label, the not-do list); ODM translation:
3 steps smallest-regret first (sensor-head module $3-8M -> certified
collection-instrument SKU $2-5M -> corpus layer ~$25M+ as OPTION, default
unfunded) — "sell the scale first, then decide on the granary." Verify fixed
6 misattributions (LWD-not-RECAP, Figure 8h source, AgiBot theme label,
Landot +510% scope, bipedal claim, BMW fleet count). HTML gains ⑤ red-team
+ probability panel, ⑥ 7-principle strategy + ODM 3-step, renumbered ⑦/⑧.
Readers 46 EN / 45 zh; HOME/llms/portal updated.

## data-engine-blueprint — 2026-07-07 (architect+implement workflow; 7 agents ~0.46M tokens)
NEW page data-engine-blueprint.md (verified, bilingual): the ENGINEERING layer
under the roadmap — chief-architect top-down design of the whole thing as ONE
closed-loop machine. (1) SYSTEM: 5 planes (device / clock / data / QC-cert /
brain) each with a design invariant (e.g. no stream without a traceable
timestamp chain; raw shards immutable append-only with hash lineage; only
sensor-rejects get deleted — task-failure clips are product); 9-boundary
interface-contract table with rates/volumes/owners; 3 budget tables with
arithmetic (data GB/h, power->battery-life W1 10.8h / W1e 7.4h, timing chain
280-300us < 0.5ms chirp budget). (2) IMPLEMENTATION: W1 electrical (part-level
power tree, buses) / firmware (RTOS task table, ISR timestamp discipline,
QC-triple math) / mechanical (strain-beam load path, 711g weight budget) +
W1e delta; L1 metrology kit (XL330 4Mbps Fast-Sync-Read 215us math, URDF->twin
design rules, audit protocol); R1 white-label box (read-only isolated bus tap
— CAN capacitive-isolated listen-only + EtherCAT magnetic winding tap, crypto
boundary so we never hold raw customer data); QC dock honest throughput; spine
software (LeRobot v2 shard layout, cert JSON schema, 6-stage ingest with
compute sizing, bounty scheduler, buyer dataloader pseudocode); Gen-2
dual-source carrier (RDK S100 ∥ Quectel SP895BD-AP one-PCB strategy) with
month-6-11 bring-up + month-11 gate procedure. Six inline INTEGRATION
ARBITRATIONS (R1: RK3588 has NO AV1 hw-encode -> site transcode node RTX 4060;
R2: dock copy honest 1.6h/shift; R4: D405 has no GMSL -> USB-only + active
optical cable; etc). Verify: 12 fixes (stale XL330/U2D2 prices, 164GB volume
typo, L1 servo power 1W->3W, W1 weight 694->711g, ISO1042 is capacitive not
transformer isolation, S3 storage tier mislabel, ingest cost closure, PGA
full-scale overstatement, RDK S100 price marked unverified) -> verified.
Roadmap page gained engineering-layer pointer; HTML gained a ⓪ 5-plane SVG
architecture diagram section. Readers 47 EN / 46 zh; portal updated.

## data-engine-first-principles — 2026-07-07 (clean-room workflow; 6 agents ~0.53M tokens)
NEW page data-engine-first-principles.md (verified, bilingual): the CONTROL
EXPERIMENT — strip all vendor constraints (Quectel modules, SP895BD-AP
mandated 2nd source, module-maker GTM) and commercial constraints (90-day
ship, calendar generations, fundraising-narrative milestones), re-derive
products + 3 generations from 12 axioms via two independent designers
(info-completeness-first vs scale-physics-first). New axioms of note:
measurement back-action (a rig that alters the demo poisons data invisibly),
measured-relative label class (in-jaw ChArUco opens the 2-10mm band without
global 2mm SLAM), utilization-inversion economics ($500-class devices are
forgiving at 10% utilization; the $55/h trap belongs to $20k rigs),
certify-the-certifier (fleet must own a measured-truth instrument). RESULT:
product family re-cast as Cicada 蝉 (passive worn, GoPro HERO 2024 $199/86g)
/ Mantis 螳 (handheld, AR0234 GS stereo Day-1, STM32G474+TCXO single-clock
island <=50us constructive — CHIRP ARCHITECTURE ELIMINATED as commercial
residue of keeping GoPro on the label path) / Anvil 砧 (metrology instrument,
single-digit units, paired recovered-vs-measured streams) + Gen-2 CORE shared
board (Mantis-2 head = robot wrist head CORE-R). Compute downgraded 80 TOPS
-> $60-80 RK3588-class (-$310/unit); generations gate-defined not
calendar-defined; silicon zero-scheduled (FPGA IP first, die only behind the
500k-unit/2-OEM gate). 18-row delta attribution: ~6.5 equivalent (physics
core independently reproduced — robustness evidence) / ~4.5 first-principles
fixes / ~4.5 commercial residue / ~1.5 vendor residue (SP895BD-AP, Landot
naming) / 1 not-judged (GTM). 12-item invariant core = paradigm-proof,
vendor-proof, build-first list. Verify: 10 parts web-checked (ICM-42688 8kHz
ODR fix, AR0234 $50-65, PiPER $2,499 pinned), BOM/economics re-summed, 2
delta-table strawmen fixed, attribution arithmetic made to sum. Canonical
adjudication per the delta table; roadmap page gained clean-room pointer.
HTML gained ⑥.5 clean-room panel (Cicada/Mantis/Anvil cards + attribution
readbox). Readers 48 EN / 47 zh; portal updated.

## case-mifeng — 2026-07-07 (case-study workflow; 6 agents ~0.43M tokens)
NEW page case-mifeng.md (verified, bilingual): reality-collision case study.
IDENTITY RESOLVED: "觅蜂智能" = 上海觅蜂具身智能科技有限公司 (觅蜂科技,
official English brand Maniformer, maniformer.ai) — AgiBot spin-out (75%
equity, registered 2026-02-03, ¥5M capital), CEO 姚卯青 (Tsinghua BS + USC
PhD, Waymo/Google/NIO, AgiBot data-factory head since 2023), Sequoia-led
seed+angel "数亿元" announced 10 DAYS after founding, 国方创投 angel+ 2026-06.
PRODUCTS: MEgo View (7-cam passive headset, sub-ms wireless sync claim) +
MEgo Gripper (480g UMI-class, Day-1 tactile array, 1mm claim, isomorphic
with 智元精灵 G2 Air) + MEgo Engine pipeline + 467-dataset marketplace
(LIVE-VERIFIED via maniformer.ai/api/data query, 2026-07-07). Founder thesis
verbatim-verified (100M-hour GPT-3.5 threshold, 8h->5h wearable vs 8h->2-3h
real-robot yield, Meituan-rider labor model, closed-source-majority view).
Zero customer/community evidence (5-month-old company); GitHub orgs
NONEXISTENT (negative finding); "29k stars" marketing claim REFUTED (real
AgiBot-World: 3,089 via API). AXIOM COLLISION: 5.5/12 converge (force Day-1,
diversity-first, byproduct labor, yield numbers interlock with ours,
isomorphism = textbook validation -> axiom 10 upgraded "market-validated");
metrology band (axioms 4/9/11) wholesale violated/undisclosed — 1mm claim
with zero error distribution, no certify-the-certifier, no SDK/format —
CONFIRMING our metrology/certificate lane is the only vacant differentiation
lane in the category. FIRST REAL PRICE ANCHOR: real-robot data ¥500-1,000/h
(证券时报 + Yao verbatim, dual-source) ≈ 5-10x our Anvil cost — written into
strategy pricing assumptions. 11 revision instructions written back: axiom-6
threshold gets new G-M mass-matching ablation (their 480g vs our 700-900g),
COTS discipline contextualized (spin-outs inherit amortized NRE), buyer-side
fatal #3 partially resolved by anchor-buyer structure, supply-shock sentinel
added (10M h/yr claim), multi-body replay scoring absorbed as cert-field
candidate. Verify: identity chain independently re-verified, brand conflict
resolved (Maniformer confirmed via site+registry match), quote misattribution
fixed (rider quote is 36kr not 甲子光年), G2 Air attribution corrected.
China-ecosystem table gained Maniformer row (EN+zh); first-principles page +
strategy page gained collision notes; queue gained company-agibot spin-off
item. Readers 49 EN / 48 zh; portal updated.

## case-mifeng full dossier + data-engine-v2 — 2026-07-08 (2-session workflow, resumed after limit; 9+9 agents ~0.92M tokens)
Run hit the session usage cap mid-flight (3/4 collectors done), resumed next
morning via resumeFromRunId — cached collectors returned instantly, 6 failed
stages re-ran. TWO deliverables, both verified:
(1) case-mifeng.md SUPERSEDED IN PLACE into the definitive Maniformer
dossier: 资料全录 sections (per-interview digests incl. full 甲子光年/东财
re-reads; launch event 2026-04-16 张江科学会堂 reconstruction; full site read
incl. hidden /api/news endpoint (12 items) + marketplace metadata schema +
the reproducible id=341 NULL defect (re-confirmed live twice); patents/
hiring/open-source incl. NEGATIVE findings — zero patents, zero HF/GitHub;
claim-propagation map: one press release echoed ~25 outlets, 29k-stars
number refuted, single-source claims downgraded) + critical synthesis
(claims-density vs disclosure-density ratio as the core signal; audience-
stratified messaging documented) + updated axiom collision + sentinels with
programmatic monthly API polling. Verify fixed 13 items (mis-sourced quotes
downgraded, "12-week zero growth" made conditional, 涌现 quote corrected to
1亿小时 threshold, 灵初 paid-pilot claim downgraded).
(2) NEW page data-engine-v2.md — direction + Maniformer-aware 3-gen plan:
honest no-go list (anchor buyer / capital / volume / brand-blitz — forfeit);
three structural voids GRADED BY DEFENSIBILITY (metrology = mid-term
defensible via real instrument work; neutrality = structural vs Maniformer
[75% AgiBot equity makes every rival body-maker our natural customer] but
not vs third parties; open-auditable = first-mover only, defensible via
open-format+signed-cert+Merkle coupling); POSITIONING: 不与觅蜂争数据货架,
做具身数据的度量衡. 10 targeted principles (disclosure-as-weapon spec sheet
listing exactly the fields they hide; multi-body jaw CARTRIDGES vs their
G2-Air single-body equity lock; error-distribution report as shipping
feature; per-claim bench-cert traceability). 3-gen deltas ON the clean-room
canonical (base untouched): Gen-1 adds cartridge kit (+G-J gate, Mantis cap
<=$570), open shard spec published BEFORE first hardware ships, legal+crypto
in-box pack (their site has zero legal text); Gen-2 adds neutrality audit
service (any-vendor data) + absorbs their multi-body replay scoring as an
auditable cert field; Gen-3 unchanged options + "Maniformer wins China
volume" pivot-weight branch. They-close-the-gap scenario: response window
<=4 weeks (weekly reports + cross-vendor comparative), fallback to neutral-
auditor position. Readers 50 EN / 49 zh; portal updated.

## company dossiers x6 + category scoreboard — 2026-07-12 (pipeline workflow; 26 agents ~1.95M tokens, 606 tool uses)
SIX new dossier pages (all verified, bilingual, novice-friendly per owner
request: 说人话 openers, jargon glossed on first use, explicit unknowns
sections with where-we-searched) + capstone comparison page:
- case-genrobot.md: 简智新创(北京) resolved fully — CEO 陈建兴 (矿大/
  RoboMaster/小鹏→Momenta), reg. 2025-05-29; DAS 5-device lineup; the most
  open-source of the Chinese pack (real GitHub genrobot-ai + HF genrobot2025).
- case-luming.md: 鹿明 = Lumos Robotics 深圳 (founder 喻超, Tsinghua +
  ex-Dreame humanoid lead, reg. 2024-09-06); robots+collectors+data-mart
  triple line; ~¥1B cumulative, A1/A2 led by Mitsubishi Electric.
- case-morphic.md: 它石智航 brand = TARS; our prior "Morphic" label was OUR
  OWN ERROR (zero external sources) — corrected across the wiki (device pages
  fixed; loop-log history left intact); founders 陈亦伦/李震宇/丁文超/陈同庆;
  GitHub org tars-robotics real; industrial-robot GTM, collection self-used.
- case-lingchu.md: 灵初智能 = PsiBot (CEO Viktor Wang 王启斌, chief scientist
  杨耀东; distinct from BeingBeyond/卢宗青); ¥2.0B angel+Pre-A (2026-03,
  华兴-confirmed); data-glove/dexterous-first bet.
- case-jd-data.md: JD = 探索研究院 Joy Future Academy (何晓冬) + LIVE data-
  trading platform robotdata.jdcloud.com; 2 arXiv papers (JoyAI-RA 62
  authors, EgoLive); HF org exists with ZERO public datasets;
  internalize-vs-sell unresolved — recorded as the central unknown.
- case-generalist.md: Generalist AI, Inc. — Pete Florence/Andy Zeng/Andy
  Barry; $400M led by Radical Ventures 2026-06-04, >$500M total, ~$2B
  valuation; devices strictly self-used: sells capability, not data/hardware.
- data-companies-compare.md (capstone, facts only from the 7 dossiers): one
  table across vision/products/tech-disclosure grades/GTM/funding/biggest
  unknown; 2x2 grid placement; claims-density vs disclosure-density ranking;
  CATEGORY-LEVEL INFORMATION VOIDS (nobody publishes error distributions /
  shutter types / measured sync / real labor rates) — our metrology lane
  confirmed vacant across all 7; three-lane threat/customer mapping checked
  against data-engine-v2 positioning, no contradictions found.
Readers gained a 数采公司档案 group: 57 EN / 56 zh. China-ecosystem rows got
dossier cross-links. Portal updated. NOTE: run took ~73 min wall, no session-
limit incident this time.

## case-galaxea — 2026-07-12 (targeted data-business dossier)
NEW page case-galaxea.md — 星海图 Galaxea AI, focused on the data-business
angle per commission brief. Five-dimension sweep: (1) vision/mission verbatim
("具身智能体服务世界" / "部署100亿台AI机器人,服务100亿全球人口", primary
site); (2) founders fully verified — CEO 高继扬 (Tsinghua+USC CV PhD,
Waymo/Momenta), co-founders 赵行 (MIT PhD, ex-Waymo research scientist,
Tsinghua MARS Lab) + 许华哲 (UC Berkeley PhD, Stanford postdoc, Tsinghua
embodied-AI lab) + COO 李天威 — no unresolved rumor, all four cross-confirmed
Forbes+多源zh; (3) full SKU lineup (R1/R1 Lite/R1 Pro $44.5-64k/A1 family/
新增 Kengo双足人形 2026-06首发) + complete funding chain reconstructed
(angel 2024-01 → Pre-A → A轮 → A4/A5 2025-08 $100M+/$700M valuation Forbes →
B轮 2026-02 ¥10亿/百亿估值 → B+轮 2026-04 ¥20亿/估值破200亿) — cumulative-
total figures explicitly NOT reconciled (Tencent "近10轮近20亿" vs Forbes
"~$210M" conflict recorded, not forced); (4) tech stack — isomorphic teleop
(GitHub OpenA1Z-T actually open to hardware-protocol level, strongest in the
group), Real2Sim2Real engine (赵行, consumer-camera cm-level 3D recon,
tension with "we don't trust sim data" stance flagged as unresolved not
contradiction), zero patents found (negative finding, notable gap vs
technical-sophistication claims), arXiv 2509.00576 independently confirmed
via 5 cross-indexes; (5) GTM — named international customers (Huawei Cloud/
VW/Haier/Samsung/ByteDance/Physical Intelligence/Stanford/MIT, Forbes+
Benzinga cross-confirmed) but data-vs-hardware revenue split undisclosed;
2024 revenue = zero (Forbes primary). CORE DATA-BUSINESS FINDING: new
Galaxea Data Hub (launched 2026-06-16 WDC) claims 1.27M hours + token-based
data-asset settlement — 1.27M figure is SINGLE-SOURCED (aimaoxian.com only,
not corroborated by stcn/qbitai coverage of the same event) and the cited
"ISO/IEC 23053:2024 embodied-data compliance certification" is a MISAPPLIED
STANDARD NUMBER (that ISO number is actually the AI-system-explainability
framework, unrelated) — same genre of failure as Maniformer's fabricated
29k-stars, flagged per house discipline. Reconciled the wiki's prior "400k
downloads unverified" flag: HF steady-state is now 16,610/mo (up from ~13k),
and press "400k in 2 months" (2025-10) is arithmetically plausible as a
launch-spike total, not a fabrication — downgraded from "likely inflated" to
"reconciled, no longer flagged." SPIN-OUT ANGLE (commissioned question):
Galaxea's data business is organized as 亦数智能, a government JV with
Beijing Yizhuang (亦庄机器人+亦庄国投, ¥1亿注册资本) — explicitly NOT a
controlled spin-out like Maniformer's 75%-AgiBot-owned carve-out; company
itself denies "spin-off" framing. Judged low probability of Maniformer-style
independent-fundraise spin-out short-term given govt-platform co-ownership.
9-item explicit-unknowns list (equity split unconfirmed, patents absent,
Data Hub hour-count uncorroborated, ISO claim status, EDP platform specs
inaccessible — docs page 503'd, no community/practitioner technical reviews
found). Cross-linked into data-collection-devices.md (2 passages updated,
prior "unverified/inflated" download flag corrected), HOME.md, llms.txt.

## batch-2 dossiers x5 + data-business-patterns — 2026-07-12 (pipeline+miners workflow; 26 agents ~2.36M tokens, 613 tool uses)
FIVE new dossiers (all verified, bilingual, novice-friendly): case-agilex
(松灵 Dongguan 2017, 魏基栋 ex-DJI; nine years hardware cash flow, no
funding since 2021 — the sell-shovels archetype; open item: ICP footer names
a different entity), case-paxini (许晋诚 Waseda/Sugano lab, Taiwan-born
confirmed via CommonWealth; sensor 10万→¥199 ~500× collapse;
customer-shareholder overlap BYD/JD/TCL/商汤; HK-IPO pipeline = category
forced-disclosure event), case-lightwheel (谢晨 ex-Cruise/NVIDIA; Santa
Clara US entity confirmed; GitHub/HF orgs real+active; CN/EN order books do
not reconcile), case-galaxea (CEO 高继扬 Waymo→Momenta + 赵行/许华哲;
gov-JV holds data platform; "127万 h"+wrong-ISO single-source flagged),
case-scale (Physical AI unit 2025-09, GM Ben Levin since POACHED BY NVIDIA
no successor; UR/Teradyne AI Trainer; 150k+ delivered hours; the only
named-external-buyer business; Meta 49%/$14.3B, Droege CEO).
NEW page data-business-patterns.md (verified): the answer to the owner's
"find the pattern" question — 8 patterns across 12 companies, each with
evidence/counterexample/dated falsifiable prediction: P1 AV-sequel (6/12
founder teams from AV data-closed-loop; playbook breaks at no-free-fleet),
P2 two-layer convergence (form = truth, independently converged CN/US;
script = imitation, same AV alumni same lines), P3 parent+state-pays (real
named external data buyers ≈ one company category-wide: Scale), P4
shovels-priced-gold-unpriced (only verified unit economics is hardware
retail; hours floor is wages not BOM), P5 lemon equilibrium
(claims/disclosure inversely ranked; hours-as-fundraising-collateral;
inflation correlates with funding dependence), P6 open≠metrology (open-source
density zero-correlated with error disclosure), P7 annexation endgame
(AgiBot 75%+suspected Lingchu seed / JD 6 investments+PaXini / Meta-Scale /
NVIDIA everywhere — AV endgame pre-positioning), P8 pulse+fracture-order
(4 founding waves 3-9mo after policy/model events; fracture order scripted,
MIIT 2026-11-30 = first clearing event). CENTERPIECE: why-metrology-empty
adjudication H2 (no paying buyer exists) > H3 ≈ H4 > H1 — Scale "borrows"
UR metrology rather than building = heaviest evidence; VERDICT DOWNGRADES
OUR OWN LANE-1 from revenue line to instrument-backed OPTION with 3
exogenous exercise triggers (first named external data deal / regulatory
forcing e.g. PaXini prospectus / performative-certification blowup). 4
revision verdicts + H4 "performative certification squatting" risk written
into data-engine-v2; P8 cash discipline into strategy; 2 fixed actions into
LOOP.md (check shareholder overlap before any customer announcement; tag
hours-numbers with funding dependence). Verify: ~25 evidence rows re-sourced,
12 fixed (它石 order misattribution, 星海图 single-sources, quote reuse).
History-analogy adjudication: AV-sequel main frame, labeling+shanzhai
sub-layers, gold-rush rhetoric only ("everyone sells shovels = shovel-selling
is the new gold rush"). Readers 63 EN / 62 zh; portal updated.

## physical-ai-essence — 2026-07-12 (4-lens essence mining; 7 agents ~0.98M tokens)
NEW capstone page physical-ai-essence.md (verified, bilingual): the complete
portrait of the field + the essential patterns BENEATH the business layer.
Part I portrait: stack pyramid silicon->deployment with per-layer players/
numbers/chokepoints, load-bearing snapshot (as-of dated), three running plots.
Part II: 8 X-patterns, each evidence/counterexample/dated-falsifiable:
X1 skill-capitalization engine (skills become capital: train once, $0 copy,
fleet amortization — the ONE new economic property vs all prior automation;
the industry's equity wars are fights over the amortization curve),
X2 embodiment-tax contact gradient (info cheapest on human bodies, action
must execute on robot bodies; tax heaviest at contact — locomotion tax-free
via sim RL, manipulation pays full; the bitter lesson meets its first
non-Moore cost term: wages), X3 three atomic irreversibilities (serial
wall-clock floor / irreversible errors / 1kHz safety loop bans cloud —
graded physical vs engineering), X4 clock-layering law (S2/S1/S0 shape
emerges everywhere incl. LeCun because three incommensurable clocks are
physically pinned; route-wars end in layer-annexation not victory),
X5 dual-clock phase lag (capability on research time, deployment on
industrial time; 2-4yr lag; compression only upstream; US dark-clearing via
private marks, China open-clearing via public markets+state absorption —
AgiBot rental ¥15k->¥4-5k/day = first cleared submarket), X6 metrology-lemon
unification (bottlenecks become markets only with units+third-party rulers;
compute standardized->NVIDIA captured, data/reliability lemon; capital
currently PRICES unverifiability at a premium — $39B undisclosed vs $5.9B
audited; leader-prediction inflation same law), X7 factor-endowment mirror
(CN monetizes supply chain+state demand, US monetizes capital+model talent —
one pattern, two halves; interface vs blockade can't both live), X8
pricing-power topology pre-dominant-design (physical chokepoints / ecosystem
lock-in / integrated cost leadership; everything else deflates to Shenzhen
floor; every money-making entity in corpus is integrated). Part 2.3: X1
adjudicated deepest by parsimony with EXPLICIT generation chain down to
X2-X8 and P1-P8, chain strength honestly graded (X2/X5/X6 tight, X3/X4
"made binding not generated", X8 loosest w/ corpus-外 premise marked), plus
a dethrone clause: if no cross-embodiment OTA skill push w/ third-party
verification by 2027-12, X2 takes the throne, TAM collapses to traditional
automation scale — and that world is BETTER for our instrument business
(pressure-test, not flattery). Verify: ~40 evidence rows re-sourced, 10
fixes (π0 span 18mo, BMW claim de-upgraded, GM-100 reattributed, phantom
labels removed, 绿的 discount 五至七折, Unitree valuation unified). Field-
level watchlist deduped vs existing pages. Readers 64 EN / 63 zh.
