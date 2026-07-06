## 主要玩家的方案与批判性评价 (Players Solutions & a Critical Read)

> 本节依据 §K 评分标准(要求为每个 Hz/TOPS 数字给出 SoC SKU 与占空比;要求给出分任务类别的分布外(OOD)成功率与第三方成对评测;将未公开的 MTBF 本身视为一项发现)以及 §L 参考架构(S2 7–10 Hz VLM / S1 100–200 Hz 策略 / S0 500 Hz–1 kHz 反射岛)对端侧大脑玩家进行打分。坦率地说:**这一梯队里几乎每一个"完全自主端侧"的头条声明都是公司口径,而营销声量最大的两个玩家(Tesla、Figure)恰恰拥有最薄弱的独立证据。** 真实、可验证的端侧推理确实存在——Figure Helix、Gemini Robotics On-Device,以及(通过 Jetson Thor 实现的)GR00T/π0——但这属于*推理本地化、遥操作训练*,而非*自主发现*。全部信息截至 **2026-07**;行内标注:`(company-reported)`(公司口径) = 厂商自述/直播,无第三方审计;`(teleop-assisted)`(遥操作辅助) = 已确认或已报道的人在环操作;`(marketing)`(营销口径) = 新闻稿/发布会话术;`(unverified)`(未证实) = 单一信源或未在一手资料中找到。交叉引用:[VLA models](vla-models.md), [Figure](company-figure.md), [NVIDIA](company-nvidia.md), [PI](company-pi.md), [Optimus](company-optimus.md), [AgiBot](company-agibot.md), [UBTech](company-ubtech.md), [Unitree](company-unitree.md), [ODM competitors](odm-competitors.md)。

### 1. 对照记分牌 (The scoreboard)

三大阵营。"真端侧?"= 推理是否真正在机器人自身芯片上本地运行(而不是"某处存在一个蒸馏模型")。评分反映的是*证据质量*,而非雄心。

| 玩家 (Player) | 方案:架构 / 芯片 / 云边 / 开闭 | 真端侧? | 一句话批判 (one-line critical read) |
|---|---|---|---|
| **— 西方前沿 (Western frontier) —** | | | |
| **Figure** (Helix / Helix-02) | S2 7B VLM @7–9 Hz + S1 80M 策略 @200 Hz(35 自由度),+ Helix-02 "S0" 全身网络;双嵌入式 GPU 板载(约 60 W,Jetson 级 **(未证实)**);约 500 小时遥操作数据;**S1 闭源**,S2 开源衍生但部署闭源 | **是**(推理确实在板载运行,无云端回路) | 真实的端侧推理——但训练数据 100% 来自遥操作,且每一个"24/7 全自主"数字都是 Figure 自己的直播,**并非**经过审计的 **(公司口径)** |
| **NVIDIA** (GR00T N1.6 + Jetson Thor + Isaac) | 开放基础模型 + Isaac Lab/Cosmos 仿真 + CUDA-X 运行时;Jetson Thor 2,070 FP4 TFLOPS,128 GB,40–130 W;**开放权重**(HF) | **平台方**——取决于集成商 | 真正做到开放+全栈,但作为卖铲子的供应商**没有任何端到端自主性声明需要为之负责**("机器人界的安卓") |
| **Physical Intelligence** (π0 / π0.5, openpi) | 流匹配(flow-matching)VLA,π0.5 预训练超 1 万小时;**完全开放权重**(openpi);默认部署 = **策略服务器通过 websocket 流式输出动作** | **默认为否**——依赖服务器;仅通过 Jetson Thor+NVFP4(NVIDIA 撰写的教程)可实现本地化 | 全队中最透明/最可复现——但 PI *自己的* README 提供的就是边缘-服务器混合方案,因此"端侧 π0"并非默认产品形态 |
| **Google DeepMind** (Gemini Robotics On-Device) | 专为本地运行构建的独立蒸馏 VLA,无网络依赖;50–100 个演示即可微调;ALOHA→Franka→Apollo;**闭源,"内测预览"/受信测试者阶段**| **设计上是**——但尚未 GA,规模化未证实 | 对*本意*的最干净实现(专门构建的小型本地模型)——但仍锁定在预览阶段,未公布芯片,也无与自家云端版本的基准对比 |
| **Tesla** (Optimus, AI5 芯片) | 仅视觉、源自 FSD 的堆栈(约 48 个网络 + 移动/操作/平衡 + Grok);**AI5 于 2026 年流片**,2027 年中量产;**完全闭源**,无架构论文 | **尚未**——芯片未量产;演示为遥操作 | 全队中"蒸汽件/遥操作"证据最充分:2024 年 We-Robot 与 2025 年 Diner 活动**已确认为远程操作**;Musk(2026 年 1 月)称 Optimus"用于学习,而非生产性任务" **(遥操作辅助)** |
| **Skild AI** (Skild Brain, 全身型通用) | 一个模型适配任意具身形态;交付形式 = **SaaS:Skild Cloud** 将机器人规格编译为 API/自然语言调用;在 Isaac Lab/Cosmos 中训练;运行于 4,000–1.5 万美元级的低成本硬件;**2026 年 1 月 14 亿美元 C 轮融资,估值超 140 亿美元,软银领投** | **否——按设计即为云端 API** | "全身型通用大脑"其实是**云端推理 SaaS**,恰是端侧的反面;规模化/可靠性声明是部署前的叙事 **(营销口径)** |
| **— 中国人形机器人阵营 —** | | | |
| **AgiBot**(智元,GO-1 → GO-2) | ViLLA(InternVL2.5-2B + 潜在动作规划器 + 扩散头),GO-1 开放权重(HF);GO-2 统一了推理与动作;板载芯片/板载 Hz **未披露**;基于开放的 AgiBot World 数据集训练(超 100 万条轨迹) | **不明确**——GO-1 的 30 Hz 是训练/评测速率,没有板载 Hz 数据 **(未证实)** | 中国团队中最好的开放*数据+模型*故事,但"端侧"数字(30 Hz)其实是采集速率而非已证实的板载性能;工厂 99.99% 直播运行在 **G2 硬件而非 GO-1 上**(已核实),且是合作伙伴主导的公司直播 **(公司口径)** |
| **UBTech**(优必选,Walker S2 / Co-Agent) | **分体式大脑:Intel i7(运动/平衡)+ Jetson AGX Orin(视觉/AI)**;BrainNet 2.0 多机协同;**Co-Agent 在本地运行 LLM+技能模型,无需云端往返**;闭源 | **是(本地 Co-Agent)**——真正的板载 NLP/规划 | 全队中最具体的量产分体式大脑(§L 三层架构的现实化);但自主率/MTBF 未公布,订单(8 亿元人民币)≠ 经审计的可用性数据 **(公司口径)** |
| **Unitree**(宇树,G1 + UnifoLM-VLA-0) | UnifoLM-VLA-0 基于 **Qwen2.5-VL-7B**,单一策略覆盖 12 类任务;**开放权重**(HF/GitHub);运行于 **板载 Jetson Orin**(G1 EDU);最大的开放遥操作数据集(WBT) | **是**(板载 Jetson Orin)——但开箱即用的 G1 并非自主 | 开放权重+板载 Jetson 是一条真实的端侧路径;Unitree 自己也表示,标准版 G1"不能自主"完成新任务——自主性来自遥操作数据管线,而非出厂即有 **(公司口径)** |
| **— 模组/芯片供应商(平台层) —** | | | |
| **Qualcomm**(Dragonwing IQ10) | 稀疏算力约 700 TOPS,18 核 Oryon + NPU + GPU,64 GB;**片上安全岛(SAIL)** + EtherCAT/8×CAN-FD;2026 年 9 月 GA | **赋能者**——非运营方 | 全队中 S0 片上化+现场总线集成度最好的方案,但 2026 年 6 月才早期开放/9 月才 GA——**作为机器人大脑尚未经现场验证** |
| **Quectel**(移远,SH602HA-AP) | **地平线 Sunrise5(X5M),BPU 算力 ≤10 TOPS**(八核 A55)+ Ubuntu;40.5×40.5 mm;支持 VSLAM/深度/BEV-占据栅格;**搭配自家 LTE/5G/Wi-Fi6 模组**;CES 2026 亮相 | **感知/S1-lite 层级**——真实、已出货 | 真正的"军火商"式模组(计算芯片+连接性+操作系统预集成),但 **10 TOPS 远不及 Thor/IQ10 旗舰水平**——它是低端感知切入点,而非完整的 VLA 大脑 |

### 2. 各阵营批判性档案 (Critical profiles by camp)

#### 西方前沿 (Western frontier)

**Figure(Helix / Helix-02)** — [company-figure.md](company-figure.md)
- **方案(截至 2026-01):** 双系统 VLA——System 2 为 7B 互联网预训练 VLM,@7–9 Hz,负责场景/语言理解;System 1 为 8000 万参数视觉运动 Transformer,@**200 Hz**,覆盖 35 自由度(手指/手腕/躯干/头部)。Helix-02 增加了统一移动+操作+平衡的"System 0"全身网络。运行于**双低功耗嵌入式 GPU 板载**,功耗约 60 W,采用 4-bit 量化与模型并行切分。训练数据约 500 小时遥操作演示(经 VLM 自动标注)。
- **是否真的端侧?** **推理层面是**——没有声称或报告任何针对控制回路的云端往返,这相较于 π0 依赖服务器的默认方案是一个真正的差异化优势。这与 §L 参考架构(S2 7–9 Hz / S1 200 Hz / Helix-02 S0)高度吻合。**但有三点需要标注:** (1) 200 Hz 是在 8000 万参数规模下实现的,而非完整 VLA(§K 锚点 1)——令人印象深刻,但并非魔法;(2)**芯片型号(Jetson Orin)信息来自二手博客,并非 Figure 官方发布 (未证实)**;(3) 2026 年 5 月的 24/7 仓库直播(3–4 台机器人,24–81 小时内分拣 5 万至逾 10 万件包裹,Adcock 称"无遥操作")是 **Figure 自身未经第三方佐证的直播**——TechRadar 等媒体指出,并非所有人都相信这"完全是真实的",也没有第三方核实过失败率或环境控制情况 **(公司口径)**。
- **优势:** 真实的边缘推理,在无云端依赖下实现了实用的 200 Hz 控制回路;单一权重集策略即可覆盖多种操作任务,且声称无需针对具体任务微调;公开发布节奏快(Helix→Helix-02 用时不到一年)。
- **批判性解读:** 训练数据谱系**100% 来自遥操作**,因此其"自主性"实为对遥操作轨迹的自主*模仿*,而非独立发现的策略。对照 §K:没有分任务类别的 OOD 成功率表,没有 MTBF,没有第三方(类 RoboArena)评测——每一项长时程声明都是自我报告。这是典型的自报基准风险模式;板载 200 Hz 的工程实现是真实的,但"自主性"叙事未经审计。

**NVIDIA(GR00T N1.6 + Jetson Thor + Isaac)** — [company-nvidia.md](company-nvidia.md)
- **方案:** 明确定位为**平台,而非机器人本身**:开放基础模型(GR00T N1.5→N1.6,权重在 HF 上开放)+ 数据/仿真管线(Isaac Lab、Cosmos 世界模型)+ CUDA-X 运行时 + Jetson AGX Thor T5000(Blackwell 架构,2,070 FP4 TFLOPS,128 GB,40–130 W)。2026 年 6 月推出开放的"Isaac GR00T 参考人形机器人"设计(由 Unitree 制造,2026 年末量产)。授权合作伙伴包括 Boston Dynamics、Caterpillar、Franka、NEURA、Skild。
- **是否真的端侧?** Jetson Thor 确实支持本地推理(这正是该产品的卖点),且 GR00T 权重开放,因此任何部署*都可以*完全本地化(§I 中给出 GR00T-N1.6 在 Thor 上的基准:TensorRT 10.9 Hz / 手写 CUDA 22–24 Hz)。**但 NVIDIA 自身并不运营任何可供审计的旗舰机器人**——端侧还是云端的现实取决于具体集成商如何部署,这使得 NVIDIA 自身的端侧声明*作为单一产品无法被证伪*。
- **优势:** 真正开放的权重加上异常完整的全栈方案降低了初创公司无需自建芯片或基础模型即可获得可用 VLA 的门槛——真实的采纳情况(具名 OEM、HF 下载量)证明这*作为基础设施*而言不仅仅是空谈。
- **批判性解读:** 卖铲子的供应商**在任何自主性声明上都没有切身利益**——"机器人界的安卓"这一框架意味着即便建立在 GR00T 之上的机器人大脑存在遥操作、不可靠或功能狭窄的问题,NVIDIA 依然是赢家。2026 年 6 月的参考人形机器人是第三方制造的规格设计,尚未量产出货。应将其评为基础设施(强)而非自主大脑(不适用)。

**Physical Intelligence(π0 / π0.5, openpi)** — [company-pi.md](company-pi.md)
- **方案:** 流匹配 VLA(π0、π0-FAST、π0.5);π0.5 预训练超 1 万小时,采用"知识隔离"以实现开放世界泛化。通过 openpi(JAX/Flax + PyTorch)**完全开放权重**,提供公开的 GCS 检查点——是本梯队中最真正开放的发布。文档记录的 GPU 最低要求:推理需 >8 GB 显存(RTX 4090),LoRA 需 >22.5 GB,全量微调需 >70 GB(A100/H100)。
- **是否真的端侧?这是核心的怀疑论发现。** PI **自己文档记录的默认方案是策略*服务器*,而非端侧**——openpi README 中的参考工作流(`serve_policy.py` 运行于 8000 端口,机器人通过 websocket 查询)意味着 PI 自家示例中的真实机器人依赖同址部署/联网 GPU。独立的 VLA-Perf 基准量化了其局限:π0 在 RTX 4090 上约 73 毫秒/次推理,在 Thor 上的最佳估计约为 53 毫秒(§L/§I:π0 在 Thor 上为 19.0 Hz)。真正的端侧路径(Jetson Thor + TensorRT NVFP4)**存在,但那是 NVIDIA 撰写的教程,并非 PI 出货的默认方案**。
- **优势:** 全队中最透明、最可复现、完全开放权重的方案——实际的检查点+训练代码+文档化的硬件最低要求让外部人员能够独立验证延迟/质量(不同于 Figure/Tesla)。通过 Thor+量化的边缘迁移路径也可信可行。
- **批判性解读:** "VLA 需要 GPU"这一陷阱**是真实存在且被自己文档记录下来的**——许多实际的 π0 演示是边缘-服务器混合方案,而非手机级的端侧算力。只有在叠加了额外的 NVIDIA 侧量化处理后,才能称之为"端侧"。诚实的评价是:*可评估性*最佳,但并非开箱即用的端侧大脑。

**Google DeepMind(Gemini Robotics On-Device)**
- **方案(公布于 2025-06-25):** 分两个层级——云端版"Gemini Robotics"(完整 Gemini 规模)+ **"Gemini Robotics On-Device",一个专为本地运行、无网络依赖而蒸馏出的独立 VLA**。基于 ALOHA 双臂系统训练,适配到 Franka FR3 + Apptronik Apollo;仅需**50–100 个演示**即可适配。状态为**"内测预览"/"受信测试者"**——尚未 GA。未公布芯片/SoC;无开放权重声明(闭源)。合作伙伴 Apptronik 于 2026 年 2 月获得 5.2 亿美元 A 轮追加融资。
- **是否真的端侧?** **本梯队中最坦诚的端侧设计理念**——DeepMind 构建了一个*专门用于本地推理的独立、更小的模型*(而非对旗舰云端 Gemini 做事后包装),其框架围绕延迟/带宽受限场景展开。**但**它仍停留在闭源内测阶段;没有大规模现场验证,没有与云端版本的基准对比,没有芯片规格,没有故障率数据。在*意图/设计*层面可信,但在 Google 受信测试者圈子之外的有意义规模上尚未得到证实(§I:"7 项任务 OOD 成功率超过 60%"这一数字在原始博客中无法核实——标记为 **(未证实)**)。
- **优势:** 概念上是最干净的端侧实现——发布的是一个专门构建的小型模型,而非对旗舰模型的事后量化;有文档记录的低样本微调+跨具身可移植性(ALOHA→Franka→Apollo)作为公开的证明点。
- **批判性解读:** 典型的资源雄厚实验室模式——在大规模出货前数年就预览端侧能力。真实的可靠性、硬件范围以及与云端旗舰版本的真正对等性仍未披露,实际上也无法从外部核实。设计可信度高,独立现场数据为零。

**Tesla(Optimus,AI5 芯片)** — [company-optimus.md](company-optimus.md)
- **方案:** 仅视觉、与 FSD 共享的端到端神经网络堆栈(无激光雷达/毫米波雷达)——据副总裁 Ashok Elluswamy(2026 年 2 月 ScaledML 大会)介绍,在约 48 个 FSD 网络基础上扩展了移动/操作/平衡网络以及 Grok 语音层,感知表征在汽车与机器人之间共享。**自研芯片:AI5 已于 2026 年流片**(相对 AI4 有效算力约提升 5 倍/原始算力约提升 8 倍,由台积电亚利桑那工厂与三星德州工厂双源代工;2026 年末出首批样品,2027 年中量产)。Optimus V3(22 自由度双手、AI5、Grok)计划于 2026 年夏季在 Fremont 小批量投产。**完全闭源**——无开放权重,没有类似 Helix/GR00T/openpi 的技术论文。
- **是否真的端侧?这是六大前沿玩家中怀疑论证据最充分、最详实的一例。** 2024 年 We-Robot 活动:Optimus 机组**已确认为远程操控**(TechCrunch、Bloomberg 报道)——其中一台在镜头前告诉一位嘉宾自己是"由人类辅助"的;摩根士丹利分析师 Adam Jonas 称其"并非完全自主运行"。2025 年 7 月 Tesla-Diner 爆米花演示:**已确认为遥控操作**,Musk 本人未予否认。2025 年 10 月的一段"功夫"视频,Musk *声称*为 AI 驱动——**这是他本人未经核实的说法**,并未经过审计 **(遥操作辅助/未证实)**。在 2026 年 1 月 28 日的 Q4-2025 财报电话会上,**Musk 本人称当前的 Optimus 机组"主要用于学习,而非生产性任务"**——即仍处于研发阶段。来自中国供应链的信息也印证了其对远程操作的依赖。
- **优势:** 真实的、独一无二的垂直整合自研芯片项目——**AI5 流片是一项具体、可验证的硬件里程碑**(在采购通用 GPU 之外,少数几家真正流片定制端侧 AI 芯片的公司之一);在汽车与机器人之间复用仅视觉的 FSD 堆栈是其他竞争者所不具备的真实效率优势。
- **批判性解读:** **本梯队中直接证据显示的蒸汽件/遥操作风险最高**——旗舰演示已被证实为遥操作,且*未主动披露*,只是通过媒体报道/镜头前的当场承认才浮出水面;Musk 本人在 2026 年 1 月的"用于学习而非生产性任务"言论,削弱了此前多年在舞台上的生产力宣称;本应支撑真正端侧大脑的芯片(AI5)**要到 2027 年中才能量产**,因此当前的 Optimus 必然运行在算力较弱的芯片上,或依赖遥操作。Rodney Brooks(2025 年)评价:Musk 对 Optimus 的构想是"纯粹的幻想"。

**Skild AI(Skild Brain,全身型通用)** — [company-skild.md](company-skild.md)
- **方案:** 为任意具身形态(四足、人形、机械臂、移动操作平台)构建一个无需预先具身知识的基础模型。**交付方式明确为 SaaS/云端 API:** 制造商将机器人规格上传至 **Skild Cloud**,由编译器自动生成控制接口,用户调用高层级 API 端点或下达自然语言指令。在 NVIDIA Isaac Lab(仿真)+ Cosmos(合成数据)中大规模训练。部署于 4,000–1.5 万美元级的低成本硬件。合作伙伴包括 ABB、Universal Robots、MiR、NVIDIA、富士康;收购了 Zebra 的机器人业务部门;**2026 年 1 月 C 轮融资 14 亿美元,估值超 140 亿美元(软银领投)**。
- **是否真的端侧?否——按设计即为云端推理 SaaS。** 这是对端侧理念*架构上的反转*:大脑存在于 Skild Cloud 中,通过 API 流式传输给机器人。任何延迟敏感的 S1/S0 控制(§L)仍必须本地化,而 SaaS 框架并未解决这一点。
- **优势:** 跨具身"编译规格→API"这一抽象层确实新颖,资本与合作伙伴信号均属顶级;这是成为*云端*大脑供应商的一条可信路径。
- **批判性解读:** "更稳健的自主运行"等可靠性声明是**部署前的叙事(营销口径)**——2026 年是"部署叙事"之年,而非经审计的部署之年。就*端侧*大脑评价而言,Skild 得分最低:它恰恰是证明云端与端侧分野存在的反例。

#### 中国人形机器人阵营(成本下探+开放)

**AgiBot(智元,GO-1 → GO-2)** — [company-agibot.md](company-agibot.md)
- **方案:** GO-1(Genie Operator-1,2025-03)——ViLLA(InternVL2.5-2B VLM + 潜在动作规划器 + 扩散动作专家),**在 HF 上开放权重**;GO-2(2026-04)在单一架构中统一了推理与动作。基于**开放的 AgiBot World** 数据集训练(超 100 万条轨迹,30 Hz 采集)。
- **是否真的端侧?** **不明确——未公布板载 Hz。** GO-1 所引用的 **30 Hz 是 AgiBot-World 数据采集/评测速率,而非已证实的板载推理性能**(§I 明确将其标注为**(未证实)**——训练速率不等于真机性能)。没有披露专用端侧 SoC 或板载延迟数据。
- **优势:** 中国团队中最好的开放*数据+模型+仿真+操作系统*故事(即"安卓打法")——GO-1 开放权重加上超 100 万条开放轨迹是外部可用/可验证的真实资产。
- **批判性解读:** 该端侧数字是**将采集速率伪装成性能**——恰是 §K 所警示的陷阱("训练率冒充板载率")。2026 年 6 月 23–28 日在龙旗(南昌)工厂的直播——约 64 小时内完成"64,828 项任务,成功率 99.99%"——运行于 **G2 轮式移动操作平台硬件,而非 GO-1**(据 AgiBot/媒体报道,已核实),因此该数据*并非*专门针对 GO-1 板载 30 Hz 的证据;而且龙旗是 AgiBot 自身的制造合作伙伴兼客户(AgiBot 第 15,000 台设备正是交付给龙旗的),即这是一场**由公司主导、且与商业关联方绑定的直播 (公司口径)**——比实验室演示更进一步,但仍非第三方审计。

**UBTech(优必选,Walker S2 / Co-Agent / BrainNet)** — [company-ubtech.md](company-ubtech.md)
- **方案(截至 2026 年):** **明确的分体式大脑——Intel Core i7 负责实时运动/平衡,NVIDIA Jetson AGX Orin 并行负责视觉/导航/AI 推理。** BrainNet 2.0 = 多机器人共享环境协同;**Co-Agent = 在本地运行大语言模型+更小技能模型的边缘智能体,无需远程服务器往返**(多语言 NLP/规划/异常检测均在板载完成)。Walker S2 已量产,订单超 8 亿元人民币;已部署于比亚迪、吉利、富士康、顺丰速运、空客(2026 年 1 月边境海关试点项目)。
- **是否真的端侧?** **就 Co-Agent/NLP + Orin AI 这一层而言是**——UBTech 明确表示语言/任务决策在机器人本地运行,而非云端。这可以说是 **§L 三层架构最字面意义上的量产实现**:i7 对应 S0/S1 确定性回路,Jetson Orin 对应 S1/S2 AI 层,Co-Agent 对应 S2 深思层,全部本地化。
- **优势:** 具体、具名的分体式大脑硬件方案(而非"未指明型号的嵌入式 GPU");真实的工厂客户与支持 24/7 作业的电池热插拔方案;在所有玩家中对参考架构的硬件实现最为清晰。
- **批判性解读:** 未公布自主率、未公布 MTBF/干预率、未公布分任务类别成功率——订单量(8 亿元人民币)与工厂部署案例是**商业信号,而非经审计的可用性数据(公司口径)**。分体式大脑执行到位,但*可靠性*这一维度(§K 锚点 3)仍是空白,与其他所有玩家相同。

**Unitree(宇树,G1 + UnifoLM-VLA-0)** — [company-unitree.md](company-unitree.md)
- **方案(2026-03):** **开源发布 UnifoLM-VLA-0**(HF/GitHub)——基于 **Qwen2.5-VL-7B** 构建,单一策略网络覆盖 12 类操作任务(抽屉、连接件、拾取放置)。运行于 **G1 EDU 板载的 Jetson Orin**(完整 Python/C++/ROS2 SDK)。基于 Unitree 的 **WBT 遥操作数据集**训练(号称最大的开放人形机器人遥操作数据集)。
- **是否真的端侧?** **是——在板载 Jetson Orin 上运行开放权重,是一条真实、可复现的端侧路径**(§I 名单)。但 Unitree 自己也表示,标准版 G1 **"不能自主"**行走陌生空间或完成新颖的多步骤任务——自主性来自遥操作数据到策略的转化管线,而非出厂即具备的行为。
- **优势:** 开放权重+板载 Jetson+低成本硬件(基础版 G1 售价 1.6 万美元,R1 售价 4,900 美元)= 全队中*可及性*最高的可验证端侧大脑;任何人都可以下载 UnifoLM-VLA-0 并复现。
- **批判性解读:** 与 Figure 存在同样的遥操作数据谱系问题,但*诚实披露*——Unitree 并未过度宣称自主性。差距在于能力而非诚信:在板载 Orin 上用一个 7B 模型覆盖 12 类任务是一个演示基线,而非通用工人 **(任务覆盖范围为公司口径)**。

#### 模组/芯片供应商——平台层

**Qualcomm(Dragonwing IQ10)** — [odm-competitors.md](odm-competitors.md)
- **方案:** 稀疏算力约 700 TOPS(18 核 Oryon CPU + NPU + GPU),64 GB LPDDR5x,**片上安全岛(SAIL,2.5G Base-T 安全域)** + EtherCAT(4×1G)+ 8×CAN-FD + 最多 12 路 GMSL2 摄像头 + Wi-Fi 7;2026 年 6 月早期开放,2026 年 9 月 GA。
- **批判性解读:** **在单一封装内对 §L 架构集成度最好的实现**——S0 安全岛+现场总线为原生集成,而非外挂的 FPGA 方案。但它仍是*赋能者*,而非运营方,截至 2026-07,**作为机器人大脑尚未经现场验证**(目前仅早期开放阶段)。应像评估 GR00T 一样,逐一部署评估。

**Quectel(移远,SH602HA-AP)** — [odm-competitors.md](odm-competitors.md),以及 [ODM opportunity](odm-opportunity.md) 中的推介目标
- **方案(CES 2026):** **地平线 Sunrise5(X5M),BPU 算力 ≤10 TOPS**(八核 Cortex-A55 @1.5 GHz,据 Quectel 介绍)+ Ubuntu 22.04,尺寸 40.5×40.5×2.9 mm,工作温度 −25→+85 °C;支持 Transformer/BEV/占据栅格、VSLAM、双目深度、三维点云、激光雷达融合;**搭配 Quectel 自家的 LTE Cat1/Cat4/5G/Wi-Fi6/GNSS 模组**以提供连接性。(内存/存储配置**(未证实)**——Quectel 官方产品页列出了尺寸/温度参数,但未列出内存;二手信源之间存在分歧,例如"4 GB + 32 GB"对"4 GB + 64 GB"。)
- **批判性解读:** 一款**真实、已出货的"军火商"式模组**——计算芯片+连接性+操作系统预集成,正是 §L 所述模组制造商切入点(拼的是集成能力,而非 TOPS 数字)。**但 10 TOPS 远不及 Thor(2,070 TFLOPS)/IQ10(700 TOPS)**——它处于**感知/S1-lite 层级**,而非完整的 S2 级 VLA 大脑。它证明了这一打法在今天确实存在;但尚未承载一个前沿端侧大脑。

### 3. 模式/读数 (synthesis)

**A. 真正端侧(推理本地化)vs 云端/遥操作依赖——真实的分野:**
- **真正推理本地化(可验证):** Figure Helix、DeepMind Gemini-On-Device(设计层面)、UBTech Co-Agent、运行于 Jetson Orin 的 Unitree UnifoLM-VLA,以及*任何*量化部署于 Jetson Thor 上的 GR00T/π0。这些方案都在机器人自身的芯片上运行大脑。
- **默认依赖云端或服务器:** **π0(PI 自己默认的 websocket 服务器方案)、Skild(云端 API SaaS)**——两个最典型的"非默认端侧"案例,且均由厂商自己文档记录。
- **实际自主性依赖遥操作:** **Tesla Optimus**(旗舰演示已确认遥操作)是极端案例;但更深层的模式是,**这里的每一个 VLA 都由遥操作数据训练而来**(Figure 约 500 小时、Unitree WBT、AgiBot World、Gemini 的 ALOHA 演示)——因此"自主"普遍意味着"对遥操作轨迹的自主模仿"。诚实的区分应是**推理本地化(数量较多)vs 自主发现而非模仿(基本上公开层面尚不存在)**。

**B. 开源 vs 闭源:**
- **开放权重:** GR00T(N1.6,HF)、openpi(π0/π0.5)、AgiBot GO-1、Unitree UnifoLM-VLA-0,以及端侧原生的 SmolVLA/TinyVLA/BitVLA(§I)。开放≈*可评估*——外部人员可以验证延迟/质量。
- **闭源:** Figure Helix(S1 权重)、Gemini Robotics、Tesla Optimus、Skild Brain。闭源≈*不可验证*——你只能得到营销数字,而没有任何东西可供复现。**这一相关性十分显著:闭源的玩家(Tesla、Figure、Skild)恰恰是自主性声明得到独立支持最少的那些。**

**C. 平台方 vs 终端方案:**
- **平台方(无论任何单一机器人的自主性如何,都能获益):** NVIDIA(GR00T+Thor+Isaac)、Qualcomm(IQ10),以及模组层面的 Quectel/地平线。应将这些评为基础设施——在被采用的地方表现强劲,但**没有任何自主性声明需要为之负责**。
- **终端方案(拥有自主性声明):** Figure、Tesla、Gemini、AgiBot、UBTech、Unitree、Skild。这些正是 §K 评分标准真正起作用的对象——也是 MTBF/第三方评测空白真正要紧的地方。

**D. 西方前沿 vs 中国成本下探路线的分野:**
- **西方前沿**在*模型能力+叙事*上竞争(最大的 VLM、最长的直播、自研芯片),且大多**闭源**(Figure/Tesla/Gemini),仅有两个开源例外(NVIDIA、PI)。营销声量最高,而独立证据在头部玩家(Tesla、Figure)那里恰恰最薄弱。
- **中国人形机器人阵营**在*成本+部署规模+开放性*上竞争(AgiBot/Unitree 开放权重、UBTech 的 8 亿元订单、4,900–1.6 万美元级的硬件),并出货**具体、具名的分体式大脑硬件**(UBTech 的 i7+Orin),而非"未指明型号的嵌入式 GPU"。中国阵营在**遥操作数据谱系上更为诚实**(Unitree 明确否认标准版具备自主性),但同样依赖**公司主导的工厂直播**(AgiBot 龙旗、UBTech)而非第三方审计——证据缺口相同,只是表述方式不同。

**E. 对端侧大脑技术现状的诚实判断(截至 2026-07):**
1. **推理本地化已基本得到解决;自主性尚未解决。** 在板载实现双系统 VLA,S1 达到 200 Hz(Figure)/ S2 达到 7–11 Hz(GR00T/π0.5 在 Thor 上)是一项**真实的、已出货的能力**——但这是通过压缩 S1(8000 万参数)并将推理放逐到较慢的 S2 层才实现的。完整的 VLA 在最好的边缘芯片上仍然只能以 3–19 Hz 的速度蹒跚运行(§K/§L)。
2. **评测空白才是真正的故事。** 没有一家玩家公布在 8 小时×5 天占空比下的 MTBF/干预率(§K 锚点 3);没有一家展示第三方成对(类 RoboArena)评测结果;几乎没有一家给出针对*量产*SoC 的分任务类别 OOD 成功率。每一个头条数字都缺少 SKU、缺少占空比——按 §K 规则应予以拒绝。
3. **营销声量最大的恰恰是验证最薄弱的。** Tesla 和 Figure 制造了最多的自主性头条新闻,却拥有最薄弱的独立证据(Tesla:已确认遥操作;Figure:未经佐证的直播)。最*可信*的反而是那些开放、可复现的方案(PI、Unitree、GR00T)——恰恰因为你可以下载并亲自核查它们。

**F. 模组制造商(Quectel)视角下的空白所在:**
- **前沿玩家留下了一个具体的空缺:** 计算/模型层(NVIDIA、PI、DeepMind)与机器人大脑层(Figure、UBTech、Unitree)都默认*由其他人*来交付那个**预集成、具备连接能力、功能安全达标的模组**——将 S2+S1(大型 SoC)与 S0(确定性 MCU/安全岛)、现场总线(EtherCAT/CAN-FD)、蜂窝网络(供 S2 云辅助层使用的 5G/Wi-Fi)拼接在一起,并且已经完成了各厂商专有、不可移植的运行时移植工作(§L 模组制造商视角)。**这种集成能力——而非 TOPS 数字——才是稀缺资源。**
- **Quectel 的 SH602HA-AP 证明了这一切入点确实存在,但定位偏低:** 以 ≤10 TOPS 而言,它是一个*感知/S1-lite* 模组,而非完整的 VLA S2 大脑。一个真正的大脑模组本可以填补的空缺是**Thor/IQ10 级别的计算芯片+Quectel 的蜂窝网络技术栈+确定性 S0 安全岛+已移植的运行时**,作为一个通过功能安全认证的模组整体出售——即"军火商"打法(参见 [ODM competitors](odm-competitors.md)、[ODM opportunity](odm-opportunity.md))。目前没有任何一家在旗舰层级提供这样的产品:NVIDIA 出售芯片,但不提供蜂窝网络/功能安全集成;Qualcomm 的 IQ10 捆绑了 S0+现场总线,但尚未经现场验证,也不是模组制造商可用的 SKU;各机器人 OEM 都在各自内部重新做集成。**一家能够将旗舰级算力+连接性+S0+移植层作为单一模组出货的蜂窝模组供应商,恰恰能出售前沿玩家尚未构建的那样东西。**

来源:
- https://www.figure.ai/news/helix ; https://www.figure.ai/news/helix-02
- https://www.techradar.com/ai-platforms-assistants/figure-ai-streamed-humanoid-robots-sorting-packages-for-8-hours-straight-and-not-everyone-is-convinced-it-was-fully-real
- https://interestingengineering.com/ai-robotics/figure-ai-humanoids-24-hour-autonomous-run ; https://en.sedaily.com/international/2026/05/17/figure-ai-robot-sorts-100000-packages-in-81-hours-without
- https://developer.nvidia.com/isaac/gr00t ; https://github.com/Nvidia/Isaac-GR00T ; https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
- https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/
- https://github.com/Physical-Intelligence/openpi/blob/main/README.md ; https://www.jetson-ai-lab.com/tutorials/openpi_on_thor/ ; https://github.com/NVlabs/vla-perf
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/ ; https://deepmind.google/models/gemini-robotics/gemini-robotics-on-device/
- https://siliconangle.com/2026/02/11/apptronik-raises-520m-ramp-humanoid-apollo-robot-commercial-deployments/
- https://techcrunch.com/2024/10/14/tesla-optimus-bots-were-controlled-by-humans-during-the-we-robot-event/ ; https://www.bloomberg.com/news/articles/2024-10-14/tesla-s-optimus-robots-were-remotely-operated-at-cybercab-event
- https://eletric-vehicles.com/tesla/tesla-tapes-out-ai5-chip-for-next-generation-self-driving-and-robotics/ ; https://www.nextbigfuture.com/2025/10/tesla-vp-describes-technology-of-fsd.html
- https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/ ; https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain ; https://www.skild.ai/blogs/skild-zebra
- https://arxiv.org/abs/2503.06669 (AgiBot GO-1 / AgiBot World)
- https://www.ubtrobot.com/en/humanoid/products/walker-s2 ; https://www.prnewswire.com/news-releases/ubtech-humanoid-robot-walker-s2-begins-mass-production-and-delivery-with-orders-exceeding-800-million-yuan-302616924.html ; https://www.techtimes.com/articles/319749/20260705/china-deploys-humanoid-robots-vietnam-border-walker-s2-begins-live-customs-work.htm
- https://github.com/unitreerobotics/unifolm-vla ; https://unigen-x.github.io/unifolm-vla.github.io/ ; https://huggingface.co/unitreerobotics/UnifoLM-VLA-Base
- https://www.quectel.com/product/sh602ha-ap-smart-module/ ; https://iotbusinessnews.com/2026/01/08/quectel-unveils-sh602ha-ap-smart-robotic-module/
- https://docs.qualcomm.com/doc/87-A0789-1/87-A0789-1_REV_A_Qualcomm_Dragonwing_IQ10_Robotics_Reference_Design_Product_Brief.pdf
