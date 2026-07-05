## 安全与对抗鲁棒性 (Security & Adversarial Robustness)

> An on-device embodied brain is an **actuation-capable** attack surface: a jailbroken planner or a spoofed perception input does not leak data, it *moves motors*. Two threat classes must be defended separately — **classical device security** (secure boot, TEE, signed OTA, root-of-trust) where the flagship SoCs are already strong, and **AI-native adversarial robustness** (VLM jailbreaks, adversarial patches, supply-chain model backdoors) where **there is no shipping mitigation with published field efficacy as of 2026-07**. The 2025 UniPwn worm against Unitree — root, wormable, from a hardcoded key — is the canonical proof that shipping an unsecured connectivity stack on a field robot is not hypothetical (primary). The module-maker (模组厂) takeaway: hardware security is a *procurement* problem (pick the SoC), adversarial robustness is an *open research* problem you must architect around, not buy.

### 1. Silicon-level device security — what the flagship SoCs actually give you

| Capability | Jetson Thor / AGX Thor (NVIDIA) | Qualcomm robotics (SPU-class, incl. Dragonwing IQ10) |
|---|---|---|
| Hardware root of trust | On-die **BootROM** authenticates BCT/bootloader/warm-boot vector via **PKC**; **Thor supports up to 16 OEM PKC keys** (RSA-3K, ECDSA P-256, ECDSA P-521, XMSS — 4 slots each) whose hashes burn into write-once `PublicKeyHash` fuses, with a **revocation policy** fuse if a key is compromised post-ship (primary — the older 2-hash / FUSE_PK_H1-H2 scheme was Orin/Xavier-era; corrected to Thor's 16-key design) | **SPU**: physically separate security subsystem, own boot-loader/boot-chain, dedicated clocks, HW anti-replay, key-mgmt + crypto-mgmt units (primary) |
| TEE | **OP-TEE** (Arm TrustZone-based); OP-TEE derives root key **EKB_RK** from a 256-bit fuse key (OEM_K1) via the Security Engine, chaining secure boot → TEE key hierarchy (primary) | SPU-hosted TEE; **Common Criteria EAL4+ certifiable**, **StrongBox-compliant** (primary) |
| Confidential compute | **NVIDIA Confidential Computing** (protected GPU enclave, no code changes) is a **Blackwell *dGPU* feature (H100/B200-class), NOT available on Jetson AGX Thor** — an AGX Thor dev-forum request to enable CC + **TDISP** was answered by NVIDIA staff "not supported on Jetson Thor, dGPU only" (2025-09) (**correction**: earlier draft wrongly listed Thor CC/TDISP as shipping — Thor confidential compute is *unavailable as of 2026-07*) | Inline crypto accelerators; masking/blinding + operating-condition sensors to resist power/side-channel attacks (primary) |
| Signed OTA | **PV-key-signed UEFI capsule** authentication; update images must chain back to the fused RoT — network access alone **cannot** push an accepted model/firmware update without the OEM private key (primary) | Platform security services for "secure field deployment" via IQ10 RRD (primary) |
| Safety/security isolation | GPU partitionable into up to **7 HW-isolated instances** (compute/mem/cache), explicitly framed as separating "fast-reaction" safety tasks from "slow-thinking" VLM/planning (primary) | **Dedicated safety island certifiable to SIL-3** (IQ10); RRD combines it with OS + security services for "functional safety, system integrity, secure field deployment" (primary) |
| Peak AI / power (context) | **2,070 FP4 / 1,035 FP8 TFLOPS @ 40–130 W**; 7.5× compute, 3.5× efficiency vs AGX Orin (primary) | IQ10: **up to 700 TOPS**, 18 Oryon CPU cores; early access 2026-06, GA target 2026-09 (primary) |

- **Key architectural point for the brain:** the same isolation boundary that runs multi-tenant workloads doubles as a **security domain wall** — a compromised S2 VLM planner in one GPU instance / on the AI-compute domain **should not be able to reach actuation-critical S0 code** on the safety island. Thor's 7-way GPU partitioning and IQ10's SIL-3 safety island are the two shipping mechanisms to enforce this (primary). This maps directly onto the S2/S1 vs S0 split from [Reference architecture](#).
- **The isolation is necessary but not sufficient:** none of the above stops an *adversarial input* that the VLM itself mis-processes — the model runs inside the TEE faithfully executing a poisoned instruction. Device security ≠ AI robustness.

### 2. The cautionary tale — UniPwn (Unitree, disclosed 2025-09-20)

- **Wormable, root, network-adjacent takeover** of Unitree **Go2 / G1 / H1 / B2** via BLE (primary):
  - The "security handshake" only checks whether a decrypted BLE packet contains the literal string **`unitree`** before setting an authenticated flag.
  - **Every unit ships the identical** AES-CFB128 key `df98b715d5c6ed2b25817b6f2554124a` and IV `2841ae97419c2973296a0d4bdfe19a4f` — one key breaks the whole fleet.
  - Shell commands built by **unsanitized concatenation** of attacker-controlled Wi-Fi SSID/password (e.g. `";$(reboot -f);#`) → **root**.
  - A compromised unit **scans BLE for nearby Unitree robots and auto-infects** — a genuine robot botnet, first publicly disclosed of its kind against humanoids.
  - CVEs: **CVE-2025-35027, CVE-2025-60017, CVE-2025-60250, CVE-2025-60251** (primary).
- **5-month vendor-response failure (primary):** found 2025-04-14 → reported ~2025-05-14 → Unitree said fixes would take "quarters or years" (2025-07-18/20) → public disclosure 2025-09-20. Unitree's 2025-09-29 LinkedIn claim of "majority of fixes" complete has **no published independent security audit** of its humanoids as of 2026-07 (primary).
- **Not a one-off:** Unitree **Go1** shipped a pre-installed remote-access backdoor (**"CloudSail", CVE-2025-2894**), found Mar/Apr 2025; units at **MIT, Princeton, CMU** were potentially exposed before Unitree deactivated the service (primary). IP-theft / tamper risk on the exact robot class a module-maker brain would ship on is *already realized*, not theoretical.

### 3. AI-native adversarial threats — the open problem

| Attack | Target layer | Reported efficacy | Threat-model realism | Source |
|---|---|---|---|---|
| **RoboPAIR** jailbreak | S2 VLM planner | **100% attack success** on 3 systems (Go2 black-box, Clearpath Jackal grey-box, NVIDIA Dolphins white-box) within days | Iterative attacker-LLM; induced driving off bridges, weapon-seeking, bomb-site hunting | primary — IEEE Spectrum; arXiv (ICRA 2025) |
| **BadRobot** | Embodied-LLM (S2) | Formalizes 3 vuln classes; **voice interaction alone** suffices to break safety constraints | First paradigm specific to *embodied* LLM agents | primary — arXiv 2407.20242 |
| **VLA adversarial patch** (UADA / UPA / TMA) | S1 VLA policy (perception) | **100% failure** in LIBERO sim for UADA/TMA (UPA 89.7%; benign baseline ~23.5%); physical world: UADA **43%** ASR, TMA **88.6%** avg failure. Patch = 3–10% of a 224×224 image; Normalized Action Discrepancy for UADA ~21% (sim) → 32.6% (physical) | Patches visually mimic robot-arm structures for real-world plausibility (OpenVLA-7B / -LIBERO) | primary — arXiv 2411.13587v3 |
| **Partially-observable patch** (2026) | S1 VLA policy | One **fixed** patch from a short observed **prefix** works on all later frames — drops the full-trajectory-access assumption | Materially more realistic: attacker need not watch the whole task | primary — arXiv 2606.03556 |
| **Universal / transferable patch** ("When Robots Obey the Patch", UPA-RFAS) | S1 VLA policy | Effective across **unknown VLA architectures, fine-tuned variants, sim-to-real** — no per-robot/per-model tuning | Raises severity: one patch, many robots | primary — arXiv 2511.21192 (posted 2025-11-30; "CVPR 2026" venue *unverified* — no acceptance record found) |
| **TrojanRobot / "Robot Collapse"** | Supply chain (VLM module) | Backdoor-finetuned VLM as drop-in module; **LVLM-as-a-backdoor** variant needs *only* a backdoored system prompt (no fine-tuning). 4 VLMs × 18 real-world tasks, physical + sim | Concrete evidence for the compromised-third-party-model risk | primary — arXiv 2411.11683 (v7, 2026-04-02) |

- **Why this layer is uniquely hard:** the attacks succeed *because the model behaves as trained* — there is no memory-corruption bug to patch. A TEE-resident, signed, correctly-booted VLA policy is fully vulnerable to an adversarial patch on a physical object in its field of view.
- **The threat model is getting worse, not better:** the 2025→2026 progression (full-trajectory → prefix-only → architecture-agnostic universal patches) removes exactly the assumptions that made these attacks feel like lab curiosities. A deployed robot's camera *will* see attacker-chosen scenery.
- **Practical mitigations (all partial, none with published field efficacy on VLA robots as of 2026-07):** input sanitization / semantic guardrails on the S2 planner; adversarial training and input preprocessing on S1 perception; **out-of-band S0 safety envelope** (geofence, torque/velocity limits, e-stop on the SIL-3 island) so that *even a fully jailbroken S2* cannot command an unsafe motion — the safety island is the last line of defense precisely because it does not trust the AI stack (unverified as a complete defense; it bounds harm, it does not prevent misbehavior).

### 4. Regulatory overlay (module-maker / procurement risk)

- **GUARD Act (H.R.9129, "Guarding the U.S. against Adversarial Robotics Dominance Act of 2026", introduced 2026-06-03** by Moolenaar/Obernolte/McClellan; dronelife coverage dated 2026-06-04): mandates national-security review of adversary-state humanoid/quadruped robots, with **automatic FCC Covered List addition** if the appropriate agency makes no determination within one year of enactment; explicitly aimed at Unitree ("six little dragons") via companion Senate legislation (primary — congress.gov / House Select Committee on the CCP; see [company-unitree.md](company-unitree.md)).
- **Read for a module-maker:** shipping the brain on a robot flagged as insecure (UniPwn-class) is now a **market-access** risk, not just a reputational one. A demonstrable secure-boot + signed-OTA + isolated-safety-domain story is becoming table stakes for Western procurement — and is a differentiator the flagship SoCs (Thor 16-key PKC RoT + OP-TEE + 7-way GPU isolation; Qualcomm SPU EAL4+/SIL-3) let you *buy* rather than build. (Note: Blackwell GPU Confidential Computing / TDISP is a *dGPU* feature, not available on Jetson Thor — do not cite it for a Thor-based brain.)

**Bottom line (要点):** device security is solved at the silicon tier — pick Thor (OP-TEE + 16-key PKC RoT + 7-way GPU isolation; note Blackwell Confidential Computing/TDISP is dGPU-only, not on Thor) or a Qualcomm SPU/IQ10 platform (EAL4+ TEE + SIL-3 safety island) and wire up secure boot + signed OTA. **Adversarial robustness is unsolved** — no patch-defense or jailbreak-defense with published VLA-robot field efficacy exists as of 2026-07, so the only load-bearing mitigation is an **AI-independent S0 safety envelope** on the safety island that bounds the physical harm a compromised brain can do.

来源:
- https://docs.nvidia.com/jetson/ — Jetson Linux Developer Guide: OP-TEE, Secure Boot (PKC/FSKP), signed OTA / UEFI capsule, Firmware TPM
- https://forums.developer.nvidia.com/t/enabling-nvidia-confidential-computing-cc-and-tdisp-on-jetson-agx-thor-blackwell-gpu/344837 — Jetson AGX Thor CC/TDISP request; NVIDIA staff reply: NOT supported on Jetson Thor, dGPU-only (2025-09)
- https://docs.nvidia.com/jetson/archives/r39.2/DeveloperGuide/SD/Security/SecureBoot/QuickStartThor.html — Thor secure boot: up to 16 PKC keys (RSA-3K / ECDSA P-256 / P-521 / XMSS), PublicKeyHash fuses, revocation policy
- https://www.nvidia.com/en-gb/data-center/solutions/confidential-computing/ — Blackwell GPU confidential computing (enclave, no code change)
- https://developer.ridgerun.com/wiki/index.php/NVIDIA_Jetson_Thor — Thor SoC features: 7-way GPU isolation, fast/slow task separation
- https://developer.nvidia.com/blog/ — Jetson Thor introduction (2,070 FP4 TFLOPS, 7.5×/3.5× vs Orin, adopters)
- https://csrc.nist.gov/ — NIST CMVP security policy, Qualcomm SPU HW v3.1
- https://www.qualcomm.com/ — "Guard Your Data" SPU whitepaper; Dragonwing IQ10 press release (Jan 2026, SIL-3 safety island, ~700 TOPS)
- https://docs.qualcomm.com/ — IQ10 Robotics Reference Design product brief
- https://github.com/Bin4ry/UniPwn — UniPwn PoC: hardcoded key/IV, "unitree" handshake bypass, root command injection, wormability, disclosure timeline
- https://spectrum.ieee.org/unitree-robot-exploit — UniPwn disclosure and vendor-response timeline
- https://spectrum.ieee.org/jailbreak-llm — RoboPAIR 100% jailbreak success across 3 robotic systems
- https://www.axios.com/2025/04/01/threat-spotlight-backdoor-in-chinese-robots-future-of-cybersecurity — Go1 CloudSail backdoor (CVE-2025-2894)
- https://arxiv.org/html/2407.20242 — BadRobot embodied-LLM jailbreak paradigm
- https://arxiv.org/html/2411.13587v3 — adversarial patch attacks on VLA (UADA/TMA, sim 100% / physical 86.6%)
- https://arxiv.org/pdf/2606.03556 — partially-observable adversarial patch attacks on VLA (2026)
- https://arxiv.org/abs/2511.21192 — "When Robots Obey the Patch": universal transferable patches (CVPR 2026)
- https://arxiv.org/abs/2411.11683 — "Robot Collapse": supply-chain backdoor attacks against VLM-based manipulation (v7, 2026-04-02)
- https://dronelife.com/2026/06/04/congress-introduces-guard-act-extending-fcc-covered-list-framework-to-robotics/ — GUARD Act (H.R.9129) FCC Covered List mechanism
