---
title: Academic Lab Map
slug: academic-labs
updated: 2026-07-04
confidence: verified
---
> A few dozen university labs supply most of Physical AI's ideas, datasets, benchmarks, and founders. The US pipeline runs through Stanford (IRIS/Finn, SVL/Fei-Fei Li, REAL/Shuran Song), Berkeley (RAIL/Levine, BAIR), CMU (Pathak & Gupta → Skild AI), MIT (Tedrake ↔ Toyota Research Institute), UT Austin (Zhu ↔ NVIDIA GEAR; Sentis → Apptronik) and UW (Fox → NVIDIA → Ai2); China's runs through Tsinghua's IIIS — which by 2026 had incubated three robotics unicorns (Robotera, Galaxea, Spirit AI) — Peking University (Galbot, PsiBot), Shanghai AI Lab, HIT (Leju) and Zhejiang (DEEP Robotics); Europe's flagship is ETH Zurich's RSL (Hutter), whose spinoffs span ANYbotics to Amazon-acquired RIVR; Korea's KAIST seeded Rainbow Robotics (now Samsung-controlled) and Raion; Japan's UTokyo JSK begat SCHAFT (bought by Google, 2013). Nearly every foundational artifact of the field — ALOHA, Diffusion Policy, UMI, DROID, Open X-Embodiment, LIBERO, BEHAVIOR, legged_gym — originated in academia, and the dominant staffing pattern is the "dual-hat" professor who runs a startup or corporate lab without giving up the faculty post.

## Why the academic map matters

- **Academia is the upstream of the Google diaspora.** The Google Brain/DeepMind robotics group that later seeded Physical Intelligence, Figure's Helix team, and 1X's AI team ([Key people](key-people.md)) was itself staffed from Berkeley, Stanford, and CMU PhD programs — the labs below are the regenerating source of the field's talent tree.
- **Datasets and benchmarks are academia's main lever.** Companies hoard robot data ([Data](data.md)); universities publish it. Every widely used open corpus (OXE, DROID), teleop rig (ALOHA, UMI), sim benchmark (LIBERO, BEHAVIOR-1K, RoboCasa), and locomotion toolchain (legged_gym/rsl_rl, RaiSim) has a university of origin.
- **The "dual-hat" professor is the field's defining employment structure** (as of 2026-07): Levine (Berkeley + Pi), Finn (Stanford + Pi), Zhu (UT Austin + NVIDIA), Pathak & Gupta (CMU + Skild), Tedrake (MIT + TRI), Wang He (PKU + Galbot), Chen Jianyu (Tsinghua + Robotera), Zhu Qiuguo (ZJU + DEEP Robotics), Hwangbo (KAIST + Raion). The talent pool is thin enough that neither side forces a choice.
- **Corporate capture of academic lineages is accelerating**: Google–SCHAFT (2013), Hyundai–Boston Dynamics (2021), Samsung–Rainbow Robotics (control approved 2025-03), Amazon–Covariant team (2024-08), Amazon–RIVR (2026-03).

## United States

| Lab (institution) | PI(s) | Signature contributions | Industry pipeline |
|---|---|---|---|
| **IRIS, Stanford** | Chelsea Finn | MAML; ALOHA/ACT + Mobile ALOHA teleop rigs; DROID (13-institution corpus); OpenVLA (with Berkeley/TRI) | Finn co-founded **Physical Intelligence** (2024); students Tony Zhao & (REAL-lab) Cheng Chi founded **Sunday Robotics**; alumni throughout Pi and Google DeepMind |
| **SVL / HAI, Stanford** | Fei-Fei Li, Jiajun Wu | ImageNet legacy; **BEHAVIOR-1K** benchmark + OmniGibson (1,000 household activities; NeurIPS challenge series, 2026 edition: 100 tasks/20k demos) | Li founded **World Labs** (2024, Marble world model); PhD lineage includes Jim Fan (NVIDIA GEAR co-lead) and Yuke Zhu |
| **REAL, Stanford (ex-Columbia)** | Shuran Song | **Diffusion Policy** (with TRI, RSS 2023), **UMI** handheld gripper — both field-standard | Song moved Columbia→Stanford 2023, student Cheng Chi followed; Chi co-founded **Sunday Robotics** (CTO); heavy TRI collaboration |
| **RAIL / BAIR, UC Berkeley** | Sergey Levine (RAIL); Pieter Abbeel; Ken Goldberg | SAC, offline RL, Open X-Embodiment/RT-X co-lead, OpenVLA; Dex-Net grasping (Goldberg) | Levine co-founded **Pi**; Abbeel co-founded **Covariant** (→ Amazon 2024-08); Goldberg co-founded **Ambi Robotics** + **Jacobi Robotics**; PhD/postdoc diaspora staffs faculty everywhere (Finn→Stanford, Pathak→CMU, A. Gupta→UW, Kumar→CMU, Yang Gao→Tsinghua) |
| **Robotics Institute, CMU** | Deepak Pathak, Abhinav Gupta (both on leave/dual-hat) | Curiosity-driven RL, rapid motor adaptation for legged robots, self-supervised robot learning; RI is the oldest US robotics department (1979) + NREC contract lab | Pathak & Gupta founded **Skild AI** (2023, Pittsburgh) — $14B+ valuation (2026-01); DARPA Urban Challenge (Boss, 2007) lineage fed the AV industry ([History](history.md)) |
| **CSAIL / Leg Lab legacy, MIT** | Russ Tedrake; Pulkit Agrawal; Sangbae Kim (biomimetics); Daniela Rus (CSAIL director) | Underactuated robotics course/canon; TRI **Large Behavior Models**; Mini Cheetah (first backflipping quadruped); Improbable AI dexterity + locomotion RL | Tedrake is SVP at **Toyota Research Institute** (MIT–TRI is the deepest US lab–corporate marriage); Marc Raibert's Leg Lab → **Boston Dynamics** (1992); Sangbae Kim reported to have joined **Meta's** humanoid effort (2025, unverified); Rus co-founded Liquid AI |
| **RSE / WEIRD, U. Washington** | Dieter Fox; Abhishek Gupta | State estimation → robot learning; Fox built **NVIDIA's Seattle Robotics Lab** (2017–2025) adjacent to campus | Fox left NVIDIA for **Ai2** (2025-07) to lead its robotics foundation-model initiative (MolmoAct open embodied models); Ai2 is a 2026 NVIDIA GR00T reference-robot partner |
| **RPL / LARG / HCRL, UT Austin** | Yuke Zhu; Peter Stone; Luis Sentis | robosuite, **LIBERO** (with Stone), **RoboCasa** kitchen-scale sim; RoboCup legacy; whole-body control | Zhu co-leads **NVIDIA GEAR** (GR00T line, [NVIDIA](company-nvidia.md)); Stone is Chief Scientist at Sony AI; Sentis's HCRL spun out **Apptronik** (2016, ~$5.3B as of 2026-02) |
| **USC (RESL/ICAROS)** | Gaurav Sukhatme; Stefanos Nikolaidis; Erdem Bıyık; Maja Matarić (socially assistive legacy) | Multi-robot systems, human-robot interaction, RLHF-for-robots strands | Steady feeder of PhDs to NVIDIA/Amazon; no marquee spinout (as of 2026-07) |

- Georgia Tech (Danfei Xu, a Stanford SVL alum) contributed **EgoMimic** human-video co-training; UCSD's ARC Lab is a GR00T reference-robot partner — the map's second tier is dense and growing.
- NVIDIA formalized the academia channel on 2026-06-01: the **Isaac GR00T reference humanoid** (Unitree H2 Plus chassis, Sharpa Wave tactile hands, Jetson Thor) ships to Ai2, ETH Zurich, Stanford Robotics Center, and UCSD ARCLab first, available from [Unitree](company-unitree.md) late 2026.

## China

| Lab (institution) | PI(s) | Signature contributions | Industry pipeline |
|---|---|---|---|
| **IIIS, Tsinghua** (Andrew Yao's institute) | Chen Jianyu; Yang Gao; Hang Zhao (MARS Lab); Huazhe Xu (TEA Lab) | Data Scaling Laws in Imitation Learning (ICLR 2025 oral); RL + VLA research; IIIS runs an explicit incubation model | **Robotera** (Chen, 2023, Tsinghua holds equity — company claim); **Galaxea AI** (Hang Zhao co-founder/chief scientist, ex-Waymo); **Spirit AI** (Yang Gao co-founder/chief scientist, Berkeley PhD) — three unicorns from one institute by 2026 |
| **EPIC Lab, Peking University** | Wang He (王鹤) | Category-level pose estimation, GAPartNet-line perception; directs BAAI's embodied-AI center | **Galbot** (2023): wheeled dual-arm G1, >$2.8B valuation, ~¥5B raised (as of 2026-03), HK IPO prep ([Landscape: China](landscape-china.md)) |
| **Institute for AI, Peking University** | Yaodong Yang | Multi-agent RL; NeurIPS 2022 dexterous-manipulation challenge winner; PKU–PsiBot joint lab | **PsiBot** (灵初智能): chief scientist Yang; ¥2B raised across angel/Pre-A (as of 2025); Psi R0/R1 pitched as first end-to-end RL-based embodied models (company claim) |
| **Shanghai AI Lab — Embodied AI Center / OpenRobotLab** | Jiangmiao Pang (research lead) | InternRobotics stack, GRUtopia city-scale sim, learned locomotion (Hybrid Internal Model); state-backed EIbench evaluation ([Evaluation](evaluation.md)) | State lab rather than spinout factory; supplies open models/benchmarks to Chinese ecosystem; partners with OpenDriveLab (HKU) |
| **Shanghai Qi Zhi Institute** | Founded by Andrew Yao (2020) | Bridge institute hosting Tsinghua-affiliated embodied-AI researchers (Yang Gao, Huazhe Xu circles) | Feeder into the same Tsinghua startup cluster (Spirit AI et al.) |
| **HIT (Harbin Institute of Technology)** | State Key Lab of Robotics & System (est. 1986) | One of China's first robotics labs; space manipulators (Tiangong program); on US entity list since 2020 | **Leju Robotics** (2016, Leng Xiaokun): Kuavo — first HarmonyOS open-source humanoid (2023-12); $207M pre-IPO (led by Greenwoods); co-built Beijing Shijingshan data-collection center ([Data](data.md)) |
| **Zhejiang University** | Zhu Qiuguo (Control College) | Jueying quadrupeds, Wukong humanoid; ZJUDancer student robot-soccer team as talent funnel | **DEEP Robotics** (2017, Zhu still associate professor) — quadruped #2 to Unitree in China; ZJU claims cultivation of Hangzhou's "six little dragons" cluster (DeepSeek, Unitree, DEEP Robotics...) though Unitree's Wang Xingxing is not a ZJU alum |

- The Chinese pattern differs structurally from the US: professor-founders keep posts **and** universities/state funds take equity (Tsinghua in Robotera; "Big Fund" in Galbot; CDB Capital in PsiBot), with IPO paths (STAR Market, HK) rather than perpetual venture rounds ([Investment](investment.md)).
- BAAI (Beijing) acts as a cross-university embodied-AI coordinator (Wang He directs its embodied center while running Galbot).

## Europe

| Lab (institution) | PI(s) | Signature contributions | Industry pipeline |
|---|---|---|---|
| **RSL, ETH Zurich** | Marco Hutter | ANYmal quadruped; actuator networks (Hwangbo, Science Robotics 2019); teacher–student sim-to-real; **legged_gym + rsl_rl** (community-standard RL locomotion stack); Isaac Lab co-development with NVIDIA; DARPA SubT-winning robots ([Locomotion](locomotion.md)) | **ANYbotics** (2016, >$150M raised as of 2024-12); **RIVR**/ex-Swiss-Mile (Bjelonic, 2023; Bezos-backed; **acquired by Amazon 2026-03**); **Ascento**; **Flexion Robotics**; PhD alumni: Hwangbo (KAIST), Mittal (dual ETH/NVIDIA); NVIDIA runs Zurich robotics research nearby |
| **LASA / BioRob, EPFL** | Aude Billard; Auke Ijspeert | Learning-from-demonstration canon (Billard); CPG-based locomotion, salamander robot (Ijspeert) | Talent exporter more than spinout factory; alumni across European faculty and DeepMind |
| **IAS, TU Darmstadt** | Jan Peters | Policy search, movement primitives; heads DFKI's SAIROL robot-learning department (since 2022) | Europe's robot-learning PhD schoolhouse — alumni hold chairs across the continent (e.g., Gerhard Neumann at KIT) |
| **H2T, KIT** | Tamim Asfour | ARMAR humanoid family (continuous development since ~1998, ARMAR-6/7) — Europe's longest-running humanoid platform | Research platform lineage; feeds German industrial robotics ecosystem |
| **Imperial / Oxford** | Edward Johns (Robot Learning Lab); Oxford Robotics Institute (Posner, Newman et al.) | Few-shot imitation (Imperial); field robotics + AV autonomy (ORI) | ORI spun out **Oxa** (née Oxbotica, AV software); Google DeepMind's London robotics group is the gravitational sink for UK robot-learning talent |

- Europe's structural problem (as of 2026-07): it produces world-class locomotion/hardware talent but its spinoffs either stay niche (ANYbotics = industrial inspection) or sell to US acquirers (Amazon–RIVR); no European robot-foundation-model lab has raised at US/China scale. Google DeepMind launched a European robotics accelerator in 2026 partly in response ([Landscape: RoW](landscape-row.md)).

## Korea and Japan

| Lab (institution) | PI(s) | Signature contributions | Industry pipeline |
|---|---|---|---|
| **Hubo Lab, KAIST** | Jun Ho Oh (emeritus) → lab continuation | HUBO (2005, Korea's first biped); **DRC-HUBO won the DARPA Robotics Challenge Finals (2015, $2M)** ([History](history.md)) | **Rainbow Robotics** (2011 spinout); Samsung raised stake 14.7%→35% (announced 2024-12, approved 2025-03) making it controlling shareholder; Oh now heads Samsung's Future Robotics Office |
| **RaiLab, KAIST** | Jemin Hwangbo (ETH RSL PhD) | RaiSim physics engine; actuator-network sim-to-real; Raibo quadruped (first robot to finish a full marathon, 2024-11) | **Raion Robotics** (2023, Hwangbo as CEO): commercializing Raibo-line quadrupeds |
| **JSK Lab, UTokyo** | Masayuki Inaba (lineage of Hirochika Inoue, lab est. ~1970s) | Musculoskeletal humanoids (Kotaro, Kojiro, Kenshiro), JAXON; deep ROS contributions | **SCHAFT** (2012, Nakanishi & Urata): left the university to accept DARPA funding, won DRC Trials 2013, acquired by Google (2013), shut down 2018 after the SoftBank sale collapsed — the cautionary tale of corporate capture |
| **Waseda (Takanishi Lab legacy)** | Atsuo Takanishi lineage | **WABOT-1 (1973)** — first full-scale anthropomorphic robot; WABIAN bipeds | Historic root of all humanoid programs (Honda's P2/ASIMO era drew on this milieu); today more legacy than pipeline |

- Japan's 2026 academic-industrial vehicle is **AIRoA** (~10,000 h open mobile-manipulator dataset + ICRA 2026 competition, Toyota HSR platform — see [Data](data.md)); Korea's is Samsung–Rainbow plus KAIST's continuing locomotion strength.

## Lab → startup pipeline

| Lab (PI) | Company | Founded | Focus | Status (as of 2026-07) |
|---|---|---|---|---|
| MIT Leg Lab (Raibert) | Boston Dynamics | 1992 | Legged robots | Hyundai 100%-owned (2026-06) |
| KAIST Hubo Lab (Oh) | Rainbow Robotics | 2011 | Humanoids/cobots | Samsung-controlled (35%) |
| UTokyo JSK (Inaba students) | SCHAFT | 2012 | DRC humanoid | Google 2013 → shut down 2018 |
| ETH RSL (Hutter) | ANYbotics | 2016 | ANYmal inspection | >$150M raised (2024-12) |
| UT Austin HCRL (Sentis) | Apptronik | 2016 | Apollo humanoid | ~$5.3B (2026-02) |
| Berkeley (Abbeel/Chen/Duan) | Covariant | 2017 | Warehouse manipulation FM | Team+license absorbed by Amazon (2024-08) |
| ZJU (Zhu Qiuguo) | DEEP Robotics | 2017 | Quadrupeds, humanoids | China quadruped #2 |
| Berkeley Dex-Net (Goldberg/Mahler) | Ambi Robotics | 2018 | Parcel sorting | Operating; Goldberg also co-founded Jacobi (2022) |
| HIT (alumni, Leng Xiaokun) | Leju Robotics | 2016 | Kuavo humanoid | $207M pre-IPO |
| CMU (Pathak & A. Gupta) | **Skild AI** | 2023 | Omni-bodied robot FM | **>$14B** (2026-01; SoftBank, NVentures, Bezos, Samsung, LG) |
| Tsinghua IIIS (Chen Jianyu) | Robotera | 2023 | STAR/L7 humanoids | >¥10B val (2026-03); >$200M round (2026-05); thousand-unit deliveries + SF Express logistics (2026-Q2, as reported) |
| Tsinghua MARS (Hang Zhao co-f.) | Galaxea AI | 2023 | R1 robots + VLA | ~$291M Series B+ at >¥20B (~$2.8B) (2026-04) |
| Tsinghua (Yang Gao) | Spirit AI | 2024 | "Dirty data" embodied FM | $280M raised (2026-02), unicorn; 200k+ h interaction data (company claim) |
| PKU EPIC (Wang He) | Galbot | 2023 | Retail wheeled humanoid | >$2.8B; HK IPO prep |
| ETH RSL (Bjelonic) | RIVR (ex-Swiss-Mile) | 2023 | Wheeled-legged delivery | **Acquired by Amazon (2026-03)** |
| KAIST RaiLab (Hwangbo) | Raion Robotics | 2023 | Raibo quadrupeds | Seed stage |
| Stanford IRIS (Finn) + Berkeley RAIL (Levine) | **Physical Intelligence** | 2024 | π VLA models | $5.6B (2025-11); see [Pi](company-pi.md) |
| Stanford SVL (Fei-Fei Li) | World Labs | 2024 | Generative world models | Marble shipped 2025-11; $1B round closed 2026-02-18 (Autodesk-led, ~$5.4B post reported) |
| PKU (Yaodong Yang, chief sci.) | PsiBot | 2024 (unverified) | Dexterous RL VLA | ¥2B raised (state-backed investors) |
| Stanford IRIS/REAL alumni (Zhao & Chi) | Sunday Robotics | 2024 | Memo home robot, Skill Capture Glove | Out of stealth 2025-11 ($35M, Benchmark/Conviction); reported ~$165M follow-on at ~$1.15B (2026, as reported) |

## Datasets, benchmarks, and tools that originate in academia

| Artifact | Origin lab | Why it matters |
|---|---|---|
| **ALOHA / ACT / Mobile ALOHA** (2023–24) | Stanford IRIS (Tony Zhao, Zipeng Fu; ALOHA 2 with Google DeepMind) | $20–30k open teleop rig — the template for global data collection, incl. Chinese data centers ([Data](data.md)) |
| **Diffusion Policy** (RSS 2023) | Columbia REAL (Cheng Chi, Song) + TRI | Default visuomotor policy class before/alongside VLAs ([Manipulation](manipulation.md)) |
| **UMI** (2024) | Stanford/Columbia REAL | Handheld robot-free data capture, ~3× teleop throughput |
| **DROID** (2024) | Stanford-led, 13 institutions | Standardized-rig diversity corpus; substrate for RoboArena eval |
| **Open X-Embodiment / RT-X** (2023) | 21-institution collaboration with Google DeepMind | Default VLA pretraining corpus; cross-embodiment transfer proof |
| **OpenVLA** (2024) | Stanford + Berkeley + TRI et al. | Most-cited open VLA baseline ([VLA models](vla-models.md)) |
| **LIBERO** (2023) | UT Austin (Liu, Zhu, Stone) | De-facto (now saturated) VLA scorecard ([Evaluation](evaluation.md)) |
| **RoboCasa / robosuite** | UT Austin RPL (Zhu) | Kitchen-scale sim + the underlying framework of much manipulation research |
| **BEHAVIOR-1K + OmniGibson** (2024→) | Stanford SVL (Li, Wu) | 1,000-activity long-horizon benchmark; annual NeurIPS challenge; "ImageNet for robotics" aspiration |
| **Dex-Net** (2017–19) | Berkeley (Goldberg, Mahler) | Grasping-at-scale lineage → Ambi Robotics |
| **legged_gym / rsl_rl / RaiSim** | ETH RSL (Rudin; Hwangbo) | The recipe stack that made RL locomotion the industry default ([Locomotion](locomotion.md), [Simulation](simulation.md)) |
| **EgoMimic** (2024) | Georgia Tech (Danfei Xu) | Human-video co-training evidence feeding the egocentric-data wave |

## Talent-flow patterns

- **Academia → Google → startup → (sometimes) back.** Berkeley/Stanford PhDs staffed Google Brain robotics; its 2023–24 diaspora founded Pi and staffed Figure/1X; the founders' academic co-authors and students now flow directly to those startups, skipping the Google step (Tony Zhao: Stanford → Sunday; Karl Pertsch: Berkeley/Stanford postdoc, DROID/OpenVLA/RoboArena → Physical Intelligence (unverified)).
- **NVIDIA is the connective tissue of the map** (as of 2026-07): GEAR co-led by a UT Austin professor, Isaac Lab co-developed with ETH RSL, the Seattle lab built by a UW professor (until Fox's 2025 Ai2 move), NVentures in Skild, and the GR00T reference humanoid shipped to four academic labs in 2026. No other company embeds in this many universities ([NVIDIA](company-nvidia.md)).
- **China compresses the pipeline.** US pattern: PhD (5 yr) → industry lab → startup. Tsinghua/PKU pattern: assistant professor founds the company directly, university takes equity, state funds follow, IPO within ~3 years of founding (Robotera, Galbot). Result: China's academic labs and its [humanoid industry](humanoid-robots.md) are effectively the same org chart.
- **Locomotion talent is genealogically concentrated**: Raibert (MIT) → Boston Dynamics; Hutter (ETH) → ANYbotics/RIVR + the legged_gym recipe; Hwangbo (ETH PhD) → KAIST → Raion. Most of the world's learned-locomotion stacks trace to two labs (ETH RSL and its descendants; MIT's Cheetah line) — see [Locomotion](locomotion.md).
- **Acquisition beats competition for corporates**: Google (SCHAFT), Amazon (Covariant team, RIVR), Samsung (Rainbow), Hyundai (Boston Dynamics) all bought academic lineages rather than growing them; OpenAI and Meta instead hired individual academics (Kalinowski era; Sangbae Kim report) with mixed results ([Organizations](organizations.md)).
- **Benchmark power is soft power**: whoever maintains the scorecard (Stanford's BEHAVIOR challenge, UT Austin's LIBERO, Fudan's LIBERO-Plus, Shanghai AI Lab's EIbench) frames what "state of the art" means — see [State of the art](state-of-the-art.md) and [Evaluation](evaluation.md).

## Open questions

- Can universities still do frontier work as training runs move beyond academic compute budgets? The 2026 hedge is infrastructure gifts (NVIDIA GR00T reference robots, cloud credits) — which also deepens vendor lock-in.
- Does the dual-hat model survive conflicts of interest at scale (professor-founders reviewing competitors' papers, students as de-facto startup employees)? No institution has published a clear policy (as of 2026-07).
- Will Europe/Japan convert research excellence into domestic companies, or continue exporting labs' output to US/China acquirers (RIVR, SCHAFT precedents)?
- Entity-list dynamics: HIT and other Chinese defense-linked universities are cut off from US collaboration, yet their spinoffs (Leju) commercialize freely — an asymmetry with no US policy answer yet ([Safety & regulation](safety-regulation.md)).

## Sources
- https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B — Skild $1.4B at >$14B (2026-01); CMU founders Pathak & Gupta
- https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/ — Skild investor list (SoftBank, NVentures, Bezos, Samsung, LG), omni-bodied thesis
- https://shurans.github.io/ — Shuran Song: Stanford REAL lab, Columbia → Stanford move
- https://github.com/real-stanford/diffusion_policy — Diffusion Policy origin (Columbia/REAL + TRI)
- https://umi-gripper.github.io/ — UMI handheld capture, throughput vs teleop
- https://behavior.stanford.edu/challenge/index.html — BEHAVIOR-1K 2025/2026 challenge scale (Stanford SVL)
- https://the-decoder.com/behavior-1k-is-set-to-become-for-robotics-what-imagenet-was-for-computer-vision/ — "ImageNet for robotics" framing (aspirational)
- https://rpl.cs.utexas.edu/ — UT Austin RPL: Zhu dual-hat with NVIDIA GEAR; RoboCasa, robosuite
- https://rpl.cs.utexas.edu/publications/2024/07/15/nasiriany-rss24-robocasa/ — RoboCasa (RSS 2024)
- https://goldberg.berkeley.edu/bio.html — Goldberg: Ambi + Jacobi co-founder, BAIR co-founder
- https://ipira.berkeley.edu/ambi-robotics — Ambi Robotics from Dex-Net (Mahler PhD '18)
- https://rail.eecs.berkeley.edu/people.html — RAIL lab (Levine) within BAIR
- https://rsl.ethz.ch/partnership/spinoff.html — ETH RSL spinoff roster (ANYbotics, RIVR, Ascento, Flexion)
- https://www.swissinfo.ch/eng/workplace/amazon-acquires-swiss-delivery-robot-start-up-rivr/91144826 — Amazon–RIVR acquisition (confirmed 2026-03-19)
- https://deeptechnation.ch/dtn-news/amazon-acquires-rivr-how-an-eth-zurich-lab-built-the-robot-that-delivers-your-packages/ — RIVR/Swiss-Mile founding (2023), Bezos-led seed, RSL origin
- https://ethz.ch/en/news-and-events/eth-news/news/2025/12/getting-a-grip-ai-and-robotic.html — RSL–NVIDIA relationship; ANYbotics lineage
- https://news.samsung.com/global/samsung-electronics-to-become-largest-shareholder-in-rainbow-robotics-accelerating-future-robot-development — Samsung 14.7%→35%; Jun Ho Oh to Future Robotics Office
- https://www.koreatimes.co.kr/business/companies/20250305/south-koreas-regulator-approves-samsungs-purchase-of-robotics-startup — regulator approval (2025-03)
- https://en.wowtale.net/2024/04/03/74664/ — Raion Robotics founded 2023 by Hwangbo (KAIST), Raibo tech
- https://www.koreatimes.co.kr/business/tech-science/20241118/kaists-4-legged-robot-becomes-1st-in-the-world-to-finish-full-marathon — Raibo full marathon (2024-11)
- https://spectrum.ieee.org/schaft-robot-company-bought-by-google-darpa-robotics-challenge-winner — SCHAFT: JSK origin, DARPA funding constraint, Google acquisition
- https://www.caixinglobal.com/2026-03-05/chinas-robot-era-valued-at-over-10-billion-yuan-102419832.html — Robotera >¥10B valuation; Tsinghua IIIS incubation
- https://pandaily.com/star-dynasty-humanoid-robot-sf-express-20260622 — Robotera >¥4B cumulative raise, SF Express logistics deployment (2026-06)
- https://www.forbes.com/sites/ywang/2025/08/25/the-700-million-chinese-robot-startup-that-wants-to-take-on-tesla/ — Galaxea AI: Tsinghua/Stanford founding team, Hang Zhao (ex-Waymo) chief science role
- https://www.caixinglobal.com/2026-04-02/robot-startup-galaxea-ai-raises-291-million-102430297.html — Galaxea ¥2B (~$291M) at >¥20B valuation (2026-04)
- https://www.prnewswire.com/news-releases/spirit-ai-lands-280m-to-scale-embodied-ai-through-dirty-data-302697085.html — Spirit AI $280M (2026-02); Yang Gao (Tsinghua AP, Berkeley PhD); 200k+ h data claim
- https://baike.baidu.com/en/item/Spirit%20AI%20(Hangzhou)%20Technology%20Co.,%20Ltd./33601 — Spirit AI founded 2024-01 (Hangzhou); Han Fengtao + Yang Gao co-founders
- https://www.psibot.ai/en/about-us/ — PsiBot: Yaodong Yang chief scientist, PKU joint lab, Psi R0/R1
- https://autonews.gasgoo.com/articles/icv/seeds-psibot-announces-completion-of-2-billion-yuan-financing-2031589417448222721 — PsiBot ¥2B financing, state-backed investors
- https://en.wikipedia.org/wiki/Leju_Robot — Leju: HIT spinout (2016), Leng Xiaokun, Kuavo/HarmonyOS
- https://www.therobotreport.com/leju-raises-200m-humanoid-production-unitree-unveils-h2-robot/ — Leju $207M pre-IPO round
- https://www.thewirechina.com/whos_who/zhu-qiuguo-%E6%9C%B1%E7%A7%8B%E5%9B%BD/ — Zhu Qiuguo: ZJU associate professor + DEEP Robotics founder/CEO
- https://www.zju.edu.cn/english/2025/0313/c75270a3026836/page.htm — ZJU "six little dragons" cultivation narrative, ZJUDancer origin
- https://github.com/InternRobotics — Shanghai AI Lab OpenRobotLab/InternRobotics open stack
- https://oceanpang.github.io/ — Jiangmiao Pang: Shanghai AI Lab Embodied AI Center lead
- https://www.geekwire.com/2025/nvidia-leader-uw-prof-dieter-fox-joins-allen-institute-for-ai-to-lead-new-robotics-initiative/ — Fox: NVIDIA Seattle lab → Ai2 robotics initiative (2025-07)
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — GR00T reference humanoid (2026-06-01): Unitree H2 Plus + Sharpa hands; partners Ai2, ETH, Stanford Robotics Center, UCSD ARCLab
- https://theaiinsider.tech/2025/11/20/sunday-emerges-from-stealth-with-35m-for-household-robot-called-memo/ — Sunday Robotics: Zhao (CEO) & Chi (CTO), $35M Benchmark/Conviction, Memo + Skill Capture Glove
- https://www.founded.com/sunday-memo-robot-chores-founders/ — Sunday founded 2024, reported ~$1.15B valuation, founders' ALOHA/Diffusion Policy lineage
- https://h2t.iar.kit.edu/tamim-asfour.php — Asfour: ARMAR family since 1998, KIT H2T
- https://www.ias.informatik.tu-darmstadt.de/Team/JanPeters — Peters: TU Darmstadt IAS + DFKI SAIROL (since 2022)
- https://www.tri.global/about-us/dr-russ-tedrake — Tedrake MIT + TRI SVP dual role
- https://droid-dataset.github.io/ — DROID: 13 institutions, Stanford-led
- https://robotics-transformer-x.github.io/ — Open X-Embodiment: 21-institution collaboration
