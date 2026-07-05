---
title: HOME — physicalAI 知识库索引
slug: HOME
updated: 2026-07-03
confidence: verified
lang: zh
source: ../wiki/HOME.md
---
> physicalAI 知识库的带注释索引:共 37 个专题页面,覆盖全球具身智能(Physical AI)领域,
> 每页均由网络研究智能体调研并通过对抗式事实核查(`confidence: verified`)。
> 建议先读三个核心页面,再按技术、人物/机构、地区或资本方向深入。

## 领域概览(截至 2026-07)

Physical AI 在 2025-26 年从演示阶段跨入首批商业部署。通用视觉-语言-动作模型(VLA)
(π0.7、Gemini Robotics 1.5、GR00T N2、Helix 02)定义了模型前沿;世界模型(world model)
正与策略融合,成为 2026 年最具决定性的架构押注。中国以深厚的零部件供应链和低于 6000 美元
的价格颠覆出货了约 90% 的人形机器人;美国实验室则握有前沿模型优势和创纪录的资本
(Figure 估值 $39B、Skild 估值 $14B)。按[技术树](tech-tree.md)的判断,当前的关键约束是:
机器人数据规模、灵巧手(dexterous hand)/触觉感知,以及部署可靠性。领域内的活跃争论
汇总在[开放问题](open-problems.md)中。

## 核心(优先阅读)

| 页面 | 内容 |
|---|---|
| [Physical AI 简史](history.md) | Unimate(1961)与 Shakey → 深度强化学习/模拟到现实(sim2real)时代 → 2022-26 机器人基础模型转折与人形机器人量产浪潮 |
| [技术前沿(2026-07)](state-of-the-art.md) | 前沿全景快照:领先 VLA、首批商用人形机器人车队(BMW/GXO/Toyota)、出货份额、创纪录资本 |
| [Physical AI 技术树](tech-tree.md) | 分层依赖图(硬件 → 感知 → 控制 → 学习 → 基础模型 → 部署)及各分支瓶颈 |
| [愿景与论点](visions.md) | 领军者如何构建 Physical AI 叙事 — 黄仁勋、Musk、Hassabis、李飞飞、LeCun、孙正义、王兴兴的带日期一手引语 + 怀疑派制衡;共识/分歧矩阵 |

## 技术

| 页面 | 内容 |
|---|---|
| [视觉-语言-动作模型](vla-models.md) | RT-1/RT-2 → π0/π0.5/π*0.6、GR00T N1-N2、Gemini Robotics 1.x、Helix 02:架构、动作解码、训练数据、开源与闭源之争、基准测试 |
| [机器人世界模型](world-models.md) | Cosmos、Genie 3、1X 世界模型、V-JEPA 2、Tesla 的神经模拟器——可学习模拟器、规划器、策略评估器、数据引擎 |
| [灵巧操作](manipulation.md) | 夹爪与灵巧手之争、触觉感知、ALOHA/Diffusion-Policy/UMI 谱系、2026 年能力前沿 |
| [足式运动](locomotion.md) | ZMP/MPC → 大规模并行模拟到现实强化学习:标准训练配方、跑酷里程碑、野外鲁棒性 |
| [仿真与 Sim2Real](simulation.md) | GPU 并行模拟器、域随机化(domain randomization)、合成数据管线——数据战略中可规模化的中间层 |
| [硬件底座](hardware.md) | 执行器、灵巧手、触觉/力感知、机载算力、电池、BOM 成本曲线、中国主导的供应链 |
| [机器人数据难题](data.md) | 遥操作(teleoperation)、第一人称人类视频、仿真数据、开放数据集、商业数据工厂、首批规模定律证据 |
| [触觉感知与灵巧手](tactile-hands.md) | 灵巧手全景与价格、GelSight 谱系 vs 触觉单元(taxel)阵列、触觉数据集/模型、中国灵巧手量产经济学、为何灵巧硬件仍是短板 |
| [数据工厂经济学](data-foundry.md) | 机器人数据制造生意:Meta 交易后的 Scale、Generalist 的可穿戴数据工厂、中国的国家补贴数据工厂、遥操作每小时成本经济学、数据交易市场 |
| [评测与基准](evaluation.md) | 已饱和的仿真套件 vs 真机竞技场(RoboArena、RoboChallenge、GM-100)、具身推理考试、工业吞吐量指标、自报基准的可信度问题 |

## 人物与机构

| 页面 | 内容 |
|---|---|
| [关键人物](key-people.md) | 研究者、美国/欧洲创始人与高管、中国人形机器人创始人;2024-26 年的人事变动与人才流向 |
| [机构:全球名录](organizations.md) | 公司、大厂事业部、学术实验室、国家级项目的参考总表——融资、代表性成果、规模 |
| [学术实验室地图](academic-labs.md) | 全球实验室地图:PI、代表性数据集/基准、实验室→创业公司管线、Google 系人才流散 |

## 地区版图

| 页面 | 内容 |
|---|---|
| [版图:美国与加拿大](landscape-usa.md) | 逐公司梳理:人形机器人厂商、机器人大脑实验室、NVIDIA 的平台打法、大型科技公司、学术界、融资环境 |
| [版图:中国](landscape-china.md) | 占 2025 年人形机器人出货量约 90%:Unitree/AgiBot/UBTech、供应链、五年规划政策、价格颠覆、IPO 浪潮 |
| [版图:欧洲、日本、韩国及其他地区](landscape-row.md) | 欧洲的风投明星、日本的老牌厂商与主权基础模型合资、韩国财阀的押注、以色列/印度/海湾地区 |

## 资本与前沿

| 页面 | 内容 |
|---|---|
| [投资与市场](investment.md) | 标注时点的巨额融资、估值、IPO、国家基金、市场预测台账——附泡沫观察的审慎视角 |
| [ODM 机会地图](odm-opportunity.md) | 代工厂的切入点在哪:诚实的市场边界(2026 全球硬件盘约 $2B)、价值链切入图、ODM/EMS 友商记分牌(Jabil/富士康/蓝思/立讯…)、时机与战略选项矩阵 |
| [开放问题与争论](open-problems.md) | 数据稀缺、sim2real 局限、灵巧性差距、可靠性、安全认证、评测危机、形态与时间线之争 |
| [安全与监管](safety-regulation.md) | ISO 25785-1 / 10218:2025 / UL 3300、欧盟机械法规 + AI 法案、中国 HEIS、工厂与家庭部署的认证关口、事故与保险 |

## 公司深度研究

| 页面 | 内容 |
|---|---|
| [Figure AI](company-figure.md) | 创立历程、$2.6B→$39B 融资曲线、Helix 架构、BotQ 制造、与 BMW 的合作(已证实内容 vs 聚合媒体说法)、与 OpenAI 分道扬镳、看空理由 |
| [Unitree](company-unitree.md) | 从 XDog 到 IPO 之路、完整价格阶梯、招股书财务数据、科创板 IPO 进展、垂直整合、爆红里程碑、安全事故、美国审查 |
| [Physical Intelligence](company-pi.md) | Google 系创始团队、累计融资约 $1.07B、π0→π0.7 模型演进、openpi 生态、未产生营收的姿态、看空理由 |
| [NVIDIA 机器人技术栈](company-nvidia.md) | 三计算机论、Isaac/GR00T/Cosmos/Jetson/Halos、合作伙伴图谱、约占营收 1% 的现实 vs $40T TAM 的说辞、平台押注的挑战者 |
| [Tesla Optimus](company-optimus.md) | 世代时间线、Musk 承诺 vs 交付台账、Fremont 产线状态、AI5 芯片、供应链卡点、演示质疑记录 |
| [Boston Dynamics](company-bostondynamics.md) | 现代 100% 控股、从研究表演转向量产 Atlas、"借脑"路线(RAI/TRI/DeepMind)、25,000+ 台内部订单、Spot/Stretch 经济账 |
| [Agility Robotics](company-agility.md) | "先干无聊仓库活"论、$2.5B SPAC(Foxconn 领投 PIPE)、行业最扎实部署记录、RaaS 经济学 |
| [1X Technologies](company-1x.md) | 家庭优先消费级押注、腱绳驱动安全硬件、遥操作数据飞轮、$20K NEO、交付风险检验点 |
| [Skild AI](company-skild.md) | ">$14B 估值的全形态机器人大脑"、与 PI 相反的营收优先姿态、In-Q-Tel/国防角度、SoftBank 汇聚 |
| [智元机器人 AgiBot](company-agibot.md) | 中国出货量领跑者、开放数据/模型生态(AgiBot World、GO-1)、ODM/EMS 代工路线(蓝思合资)、港股 IPO 路径 |
| [优必选 UBTech](company-ubtech.md) | 首家上市人形厂商、Walker S2 工业爬坡、U1 消费级发布、亏损 vs 订单簿的财务现实 |

## 参考

| 页面 | 内容 |
|---|---|
| [术语表](glossary.md) | 约 35 个核心术语(模型、学习方法、数据机制、执行器、控制、商业黑话),每条均交叉链接到对应页面 |

## 元信息

- [循环日志](_meta/loop-log.md) — 每次循环迭代的变更记录
- [研究队列](_meta/queue.md) — 后续迭代的待办清单
- [LOOP.md](../LOOP.md) — 维护循环的运行方式;实时 HTML 控制台见 [README](../README.md)
