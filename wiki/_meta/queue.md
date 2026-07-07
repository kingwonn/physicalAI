# Research queue / backlog

Items the loop should pick up in future iterations. Add freely; remove when done.
Distilled from loop(1)'s 54 research leads (2026-07-03) plus the original backlog.

## New pages (candidates)

- [x] ~~Safety & regulation deep page~~ — done loop(2): [safety-regulation.md](../safety-regulation.md)
- [x] ~~Glossary page~~ — done loop(2): [glossary.md](../glossary.md); append candidates for later: affordance, VLM-vs-VLA distinction, RECAP/RLHF-for-robotics, end-effector taxonomy (parallel-jaw vs suction)
- [x] ~~Tactile sensing & dexterous hands deep page~~ — done loop(3): [tactile-hands.md](../tactile-hands.md)
- [x] ~~Evaluation crisis / benchmarks page~~ — done loop(3): [evaluation.md](../evaluation.md)
- [x] ~~Per-company deep pages~~ — series complete: Figure ✅ + Unitree ✅ loop(4); PI ✅ + NVIDIA ✅ loop(5); Optimus ✅ loop(6): [company-optimus.md](../company-optimus.md).
- [x] ~~Data-foundry economics page~~ — done loop(7): [data-foundry.md](../data-foundry.md); follow-ups: Forbes 2026-05-14 Scale-post-Meta piece (paywalled) for robotics-segment revenue; retry CNBC China-centers article (403) for per-center economics; Genesis AI (~$105M seed 2025) not yet covered anywhere in wiki.
- [x] ~~Academic lab map~~ — done loop(6): [academic-labs.md](../academic-labs.md); follow-ups: verify Sangbae Kim→Meta and Karl Pertsch→PI moves; pin down Hutter-NVIDIA relationship; second-tier labs (Georgia Tech/Danfei Xu, UCSD/Xiaolong Wang, CMU LeCAR/Guanya Shi).
- [ ] Optimus follow-ups from loop(6): Tesla vs Proception hand-IP suit settlement (single source); reconcile ">1,000 Gen 3 on Fremont floor" claim across company-optimus + humanoid-robots; find primary Elluswamy CVPR 2026 transcript ("Digital Optimus").

## Watch items (news-sweep targets)

- [ ] IPO wave: Unitree STAR-market listing pricing/pop (CSRC registration approved 2026-07-02; debut possibly late July, unverified), AgiBot HK backdoor listing (HK$40-50B target), Galbot/EngineAI filings, Agility-Churchill Capital XI SPAC outcome.
- [ ] UBTech UWORLD U1 consumer humanoid: deliveries from mid-Sept 2026; verify order book (company claims 13,361 at launch vs TechNode ~11,000+).
- [ ] Standards track: ISO 25785-1 CD → DIS progression (expected late 2026/2027), possible Part 2 work item; EU delegated acts folding AI requirements into Machinery Regulation Annex III (due 2028-08-02); what certification 1X actually obtains for NEO before home deliveries (UL 3300 listing or none).
- [ ] World-model-as-policy convergence: DreamZero/GR00T N2, π0.7 visual-subgoal world model; Cosmos 3 technical report details; SIMA 2 + Genie 3 transfer-to-physical evidence.
- [ ] Tesla: Optimus V3 Fremont production start (slated late-July/Aug 2026), official V3 actuator/DoF specs, AI5 robot silicon (mass production mid-2027) vs Jetson Thor.
- [x] ~~Meta ARI / OpenAI robotics verification~~ — done loop(11): ARI closed 2026-05-01 (Pinto + Xiaolong Wang → Meta Superintelligence Labs); Ramesh VP-of-Robotics confirmed; Kalinowski departure OpenAI-confirmed (stale marker fixed); Sangbae Kim → Meta Robotics Architect (2025-03, "Metabot") and Pertsch → PI both confirmed. Remaining watch: Meta Robotics Studio org placement conflicting (Reality Labs per Kim's LinkedIn vs Superintelligence Labs per ARI coverage).
- [ ] SoftBank ~$5.4B ABB robotics acquisition (announced 2025-10) integration; K-Humanoid Alliance (verify KRW 1T-by-2030); Japan ¥1T foundation-model JV against METI/NEDO primary documents.
- [ ] Non-Chinese rare-earth magnet buildout (MP Materials et al.) vs the humanoid actuator chokepoint.
- [ ] State Grid RMB 6.8B / 8,500-robot 2026 procurement (added to landscape-china.md 2026-07-04, found as a coverage gap dating to 2026-04): all figures trace to one Jiemian-leaked internal plan — watch for actual public tender/award notices (ecp.sgcc.com.cn bidding portal) confirming the 500-humanoid line item and which vendors win; also whether China Southern Power Grid follows with its own plan.
- [ ] Events: CoRL 2026, ICRA/IROS 2026 results, CES 2027 announcements.
- [ ] Tactile fork to track: SharpaWave field reliability + ~$50k price audit once early-customer reports appear (VBT-in-production bet vs Figure's anti-gel durability bet); whether any frontier VLA (π-successor, Helix, GR00T) adds tactile as a first-class modality in H2 2026; Daimon-Infinity scaling claims; LinkerBot 50k-100k unit 2026 target (single-source Gasgoo).
- [ ] Evaluation watch: RoboChallenge Table30 v2 launch (v1 retired 2026-05-27); whether closed frontier models (Helix, Gemini Robotics, π0.7) appear on any public leaderboard; verify GR00T N2 #1 claims against actual RoboArena/MolmoSpaces boards at GA (late 2026); GM-100 SOTA trajectory (~17% avg = best single indicator of real generalist progress).

- [ ] **Unitree IPO pricing imminent (days)**: when offer price / subscription / listing date land (expected late 2026-07), refresh company-unitree.md, humanoid-robots.md, landscape-china.md, investment.md in one pass. Status 2026-07-04 ~19:45 CST (rechecked; Saturday, markets closed): still no 发行安排/初步询价公告; Eastmoney 新股日历 API has no Unitree entry (latest scheduled STAR subscription: 泰诺麦博 688806/申购代码787806 on 07-10); SSE audit record for auditId=2178 unchanged since 06-02 (currStatus 4, CITIC sponsor team listed). Next realistic announcement window: trading week of 2026-07-06. After the 07-02 registration, CITIC files the issuance/underwriting plan with the SSE, which has 5 working days to raise no objection → earliest formal launch week of 2026-07-06. Monitor the SSE disclosure page (sse.com.cn auditId=2178; announcement PDFs under static.sse.com.cn code 002178 — working JSON probe: query.sse.com.cn/statusAction.do?sqlId=SH_XM_LB&keyword=宇树 with Referer kcb.sse.com.cn; the GP_GPZCZ_SHXXPL doc-list sqlId returns empty) and 新股日历 aggregators (Eastmoney JSON: datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPTA_APP_IPOAPPLY) for the 申购代码/申购日.
- [ ] **Unitree 2025 profit-measure reconciliation** — resolved 2026-07-04 (fact-check pass): GAAP series confirmed from two STCN pieces + Hangzhou News: 2022 −2,210.05万 / 2023 −1,114.51万 / 2024 9,450.18万 (stcn.com 3688950, filing-stage) / 2025 ~2.88亿 +204.29% ("净利润近3亿" per stcn.com 3735182; "2.88亿" per hznews.hangzhou.com.cn). The ~¥600M measure is **扣非净利润** (excl. non-recurring items, CSRC-standardized) — stcn 3688950 headline: "扣非净利润暴增674.29%", "超6亿" — NOT a loosely-defined non-GAAP adjusted figure; it exceeds GAAP because 2025 non-recurring items were net losses (~¥3.1亿 implied). Earlier state-of-the-art relabeling away from 扣非 was an over-correction, reverted 2026-07-04. Remaining: (a) exact 2025 decimals + composition of the non-recurring net losses (share-based payment?) from the offering-stage 招股意向书; (b) why SCMP says "adjusted RMB 591M" vs STCN's "超6亿" (measure nuance or rounding).
- [x] ~~New Yorker Witt feature~~ — done loop(9)+(10): full text retrieved, digested into open-problems + evaluation, remaining leads applied across 5 more pages; residual watch: post-publication reactions/rebuttals from 1X or Figure once the 07-06 print issue circulates.
- [ ] X Square Robot / AI² Robotics follow-up: WALL model family details, AlphaBot deployments, whether the RMB 20B valuations hold in next rounds.
- [ ] Foxconn Houston plant: primary confirmation that GR00T-powered humanoids are actually in production (Q1 2026 target, unconfirmed as of 2026-07).
- [ ] Figure-Qualcomm compute collaboration: if Figure 04-gen drops NVIDIA onboard silicon, update company-nvidia + company-figure skeptic sections.
- [ ] Dated refresh triggers: GR00T N2 GA (late 2026); first Halos AI Systems Inspection Lab certification outcomes (Agility Digit vs IEC 61508/ISO 13849).
- [ ] PI unnamed pilot partners (logistics, grocery, chocolate mfg per TechCrunch 2026-01) — watch for names; would fill company-pi business-model void.
- [x] ~~Japan Airlines × GMO AI & Robotics humanoid trial at Haneda~~ — done 2026-07-04: written into [landscape-row.md](../landscape-row.md) Japan section (2026-05→2028 trial, Unitree G1-based, baggage/GSE/cabin-cleaning tasks, "Japan's first" per JAL; cost conflict kept with explicit attribution: ~$13.5K New Atlas vs ~$15.4K CNBC).
- [ ] MIIT+SASAC real-scene-training special action follow-through: end-June implementation plans and November progress reports (which provinces/SOEs, which vendors win the "consortium" slots) — added to landscape-china.md 2026-07-04.
- [x] ~~Korea ">$1T triple axis" primary verification~~ — done loop(11): MOTIE 2026-06-29 release fetched directly; chip conflict = scope difference (W800T fabs alone vs W881T incl. packaging; USD conversions are outlets' own); Hyundai "$5.8B" decoded as W9T Saemangeum hub breakdown; K-Humanoid Alliance KRW 1T primary-verified (MOTIE 2025-04-10); fab sites explicitly undecided as of 2026-07; MSIT's separate W50.4B K-AI consortium disambiguated.
- [ ] Korea follow-ups: investment.md fold-in of primary-verified program numbers (W881T chips / W550T AI DC / robot axis); Hyundai W42T Yeongnam hub (2026-07-03 briefing, ZDNet — new figure to verify); MSIT 3-year physical-AI export push; which vendors win robot data-factory slots.
- [ ] Weave Robotics "Isaac 1" $7,999 home robot, Fall 2026 deliveries (HN 232pts, 2026-07-01, weaverobotics.com/isaac-1) — assess for home-robot coverage in humanoid-robots.md/landscape-usa.md (wheeled non-humanoid; relevant as 1X NEO price counterpoint).
- [ ] Witt/New Yorker leads batch (piece digested into open-problems + evaluation loop(9); remaining material): 1X Neo fresh data (10,000+ deposits at $20K, ~800 staff, 66 lb, 22 dB locomotion, Oakland-area factory) → humanoid-robots.md; "every robot ran on an Nvidia chip" + edge-chips-drain-up-to-60%-battery → company-nvidia.md skeptic/hardware; Neura 1,000+ mocap-suit worker program + Waymo 500K+ teleop-hours framing → data.md/data-foundry.md; Unitree G1 BT botnet (Makris/Finisterre) + home-robot jailbreak/privacy (child coaxing Neo; 1X operators seeing homes) → safety-regulation.md; Stanford cross-country adoption-attitude poll → open-problems culture note.
- [ ] ByteDance Seed GR-3 VLA has no entry in vla-models.md (verified from paper arXiv:2507.15493 in loop(8)) — add entry + Fourier GR-3 name-collision note.
- [ ] FITEE 2025 CoT paper erratum (doi 10.1631/FITEE.24e1070) — check whether it corrects the Table 6 CoT values cited in locomotion/glossary.

## Claims to re-verify (single-source or conflicting)

Most of this list was resolved by the loop(8) re-verification batch (2026-07-04):
H2 price tiering, MirrorMe Bolt (real, multi-source), Honor Flash (independently
confirmed incl. Scientific American/CBS/NPR), GR-3/GO-1/"100+ VLAs" (attributed
to ResearchInChina), shipment + funding-total methodology notes written, Figure
03 height (official 1.73 m), robots-outnumber-employees (primary post found,
headcount trajectory corrected), Meituan 9.65% combined / A2 2025-08 / UniPwn
confirmed, CoT numbers added to locomotion. Remaining:

- [ ] Figure-BMW commercial terms (~$25/robot-hour, 40-unit fleet claim) — 40-unit claim traces to one aggregator; Leipzig pilot is Hexagon AEON, not Figure.
- [ ] Still-open round watch: PI ~$1B @ >$11B and 1X ~$1B @ ~$10B — both NOT closed as of 2026-07-04 (rechecked); World Labs/AMI/Wayve confirmed CLOSED and written into investment.md; "Shihang $1B" REFUTED (actual: Seahi >¥1B RMB ≈ $140M, Crunchbase currency error).
- [ ] Cross-page propagation batch from loop(8) leads: world-models.md lacks the 2026 world-model funding wave (World Labs/AMI/Wayve closed rounds); landscape-row.md check Neura milestone-contingency + Wayve/AMI closed status; locomotion.md + tech-tree.md attribute "Unitree 5,500+ 2025" as prospectus self-reported; data.md upgrade AgiBot World to verified paper figures (>1M trajectories, 2,976.4 h, 217 tasks, 100 robots); organizations.md fix AgiBot "backdoor listing" (company denied — landscape-china has the denial); check GR-3 name collision (ByteDance VLA vs Fourier robot) on remaining pages; glossary.md CoT entry could cite learned-gait numbers; MirrorMe Black Panther II quadruped 13.4 m/s claim; verify FITEE 2025 CoT 0.4306 datapoint from primary.

## ODM-pitch track (audience: user's boss, 2026-07-05)

- [ ] **NEXT: ODM opportunity analysis page** (odm-opportunity): market sizing with tracker attribution, where the value chain opens for ODMs/EMS (assembly, actuators, hands, harnesses, sensors, test), who moved already (Foxconn: Agility PIPE + Houston GR00T plant; Lens Tech: AgiBot JV 智启未来; Wistron/Quanta/Pegatron/BYDE/Luxshare/Goertek status check), capturable-share scenarios, response options, FOMO evidence chain. Research: Sonnet for company-move fact-gathering; Fable for sizing synthesis + verify.
- [ ] **THEN: boss pitch deck** (Chinese-first HTML artifact): 蛋糕多大 / 机会在哪 / 怎么切能切多少 / 友商在做什么优劣如何 / 如何应对 — built from odm-opportunity + visions + company pages.
- [ ] Lens Technology 智启未来 humanoid assembly JV — first real humanoid-EMS test, deserves tracking (from company-agibot leads).
- [ ] AgiBot data-ops subsidiary 觅蜂 (10M-hours-by-end-2026 target, exec claim) — barely documented in English; Chinese-language sweep.
- [ ] Visions-page leads: Wang Xingxing's VLA-as-"simpleton-architecture" critique → vla-models/world-models named-dissent; Hassabis 18-month clock (expires ~2027-08) → open-problems timeline table; SoftBank "Roze" US robotics vehicle (~$100B IPO target, aggregator-only) — watch filings.
- [ ] Company-page watches: BD permanent CEO / 30K-yr factory site / NASDAQ IPO float (single-source); Agility S-4 (H2 2026, real revenue disclosure); 1X end-2026 first verified home delivery; Skild post-Fetch revenue mix; UBTech H1 2026 interims (~2026-08/09) + Walker S3 unveil + Fenglong tender completion.

## ODM opportunity — leads (2026-07-05)
- [x] ~~ODM opportunity page~~ — done: [odm-opportunity.md](../odm-opportunity.md), verified (14 corrections; killed the circulated "Luxshare won China Mobile ¥124M order" claim — actually AgiBot ¥78M + Unitree ¥46M; fixed Wistron/Shangwei 上纬 conflation).
- [ ] 友商 ledger churns fast — dated freshness passes: Agility SPAC close (Foxconn PIPE → manufacturing role?); Foxconn Houston GB300 line actual humanoid count once Q1-2026 results reported; Luxshare "Manufacturing 2.0" + mid-2026 robot prototype + who got its 3,000 units; State Grid Q3 2026 procurement winners (best datapoint on CM demand conversion); Techman/Quanta TM Xplore I production start.
- [ ] Consider a dedicated supply-chain / EMS-tracking page if the 友商 ledger keeps growing.

- [ ] company-agibot.md: add spin-off structure note (觅蜂 Maniformer 75%, 智鼎/擎天租/临界点 AGILINK/智元酷拓 batch; IPO-driven incubation model) — from case-mifeng research 2026-07-07
- [ ] Watch (case-mifeng): MEgo Gripper shutter type + 1mm claim teardown (2026-Q4); first collector/buyer community posts (2026-08+); 10M-hour delivery via marketplace dataset count (baseline 467 @2026-07-07, /api/data re-queryable)
