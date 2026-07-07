---
title: 数据引擎全系统蓝图与硬件实现方案 (Data-Engine Full-System Blueprint & Hardware Implementation)
slug: data-engine-blueprint
updated: 2026-07-07
confidence: verified
---
> 本页是 [数据引擎路线图 v1.1](data-engine-roadmap.md) 之下的**工程层**:把已定案的 [Scaling 策略](data-scaling-strategy.md)、[LeCun 再思考](lecun-worldmodels-rethink.md)、[端侧大脑](on-device-brain.md) 收束为一台闭环机器的系统规格(五平面 + 边界契约 + 三张预算表),并给出可开工的硬件实现:W1/W1e 手持与头戴采集器、L1 计量套件、R1 白标改装盒、QC 坞站、数据脊柱软件,以及 Gen-2 传感头板级方案 (设计目标)。本页由总架构规格与三份子系统实现整合而成;子系统对总架构的每处修正已由总架构师**裁决并内联标注(⚖ 整合裁决 R1–R6)**。凡现货件带实价,前瞻规格标 (设计目标),单源价标 (unverified)。全文遵守 v1.1:吞吐按 60–70 demos/h 有效口径、传感废 15–20% 规划容量;啁啾 <0.5 ms 未过月 1 台架前,一切 SLA 字段按 LED 帧级填写。

## 1. 系统总览:一台闭环机器

整机是一条单向数据流加一条反向修正流:**设备舰队产生带时戳的原始流 → 时钟平面给每个字节一条可追溯的时间链 → 数据平面把它变成不可变 shard → QC/认证平面把 shard 变成带证书的商品 → 大脑平面消费证书化语料训练 S2/S1/S0 → R 系部署盒在客户机器人上捕获干预/结果标签,回注脊柱**。飞轮的每一圈都让下一圈的边际数据更便宜(修正数据是部署副产品)、更值钱(失败/力/修正是三个世界通吃的稀缺 SKU)。

```
P1 设备平面                P3 数据平面              P5 训练/部署平面
┌──────────────┐          ┌──────────────┐        ┌──────────────┐
│ W1  夹爪采集  │─shard──▶│ 坞站(RK3588) │        │ S2 VLM 7–10Hz │
│ W1e 被动头戴  │─shard──▶│  ↓ 转码+QC   │─cert─▶│ S1 50–200Hz  │
│ L1  主从计量  │─shard──▶│ 云存储(热/冷)│ shard  │ S0 0.5–1kHz  │
│ R1  在机改装  │─shard──▶│ LeRobot v2   │        │ 世界模型买家  │
│ Gen2 传感头   │          └──────┬───────┘        └──────┬───────┘
└──────▲───────┘                 │                        │
       │        P2 时钟平面(贯穿):GPMF 单钟→啁啾/LED→PTP→gPTP
       │        P4 QC/认证平面(贯穿):端上三件套→坞站门禁→云证书
       │                                                  │
       └────────── R 系修正飞轮:干预 flag + 结果标签 ◀────┘
                   (白标契约:数据归客户,证书/SaaS 归脊柱)
```

**每平面一条设计不变量:**

- **P1 设备平面:** 任何 SKU 的输出必须是合法 LeRobot v2 shard + QC manifest,设备异构性不得越过坞站泄漏到下游——三 SKU 一条脊柱。
- **P2 时钟平面:** 任何一路数据流不得存在无法追溯到命名时钟域的时间戳;软件时间戳只在 L1 一处豁免(书面例外),Gen-2 起硬件公理化(锁步 R52 时间戳岛)。
- **P3 数据平面:** 原始 shard 一经落盘不可变(append-only),一切派生物(转码、标注、证书)以哈希引用原件——git 式血统,坏管线可重放,不可污染。
- **P4 QC/认证平面:** 判决在采集现场做出、在云端固化为证书;无证书字段不齐的 shard 不进训练池、不进货架。废片三分类:**只有传感废真删**,任务失败片是产品([复审 #11](data-scaling-strategy.md))。
- **P5 大脑平面:** 大脑只吃证书化语料;每个部署修正事件必须在 24h 内回到脊柱(飞轮 SLA)——采集与部署不是两个系统,是同一个环的两段。

**⚖ 整合裁决 R1(转码职责重分配,本页唯一的架构级修正):** 原架构把"AV1 转码"放在坞站 RK3588。子系统实现查明 **RK3588 VPU 只有 AV1 硬解、无 AV1 硬编**(编码仅 H.264/HEVC);SVT-AV1 软编 2.7K 在 8×A76 上仅 ~0.15–0.3× 实时,6 h 素材需 20–40 h——正是 v1.1 警告的 3–5× 低估的藏身处。裁决:**AV1 转码移至站点转码节点(RTX 4060,第 8 代 NVENC AV1 硬编,~6–8× 实时),坞站保留哈希校验/SLAM/QC/证书字段/上行**;无转码节点的微型站点降级为 RK3588 HEVC 硬编(H.265 CRF 23,LeRobot 兼容),证书 `codec` 字段如实记录。架构页"AV1+QC"的意图(≥2:1 归档压缩)不变,只是执行位置变了。下文预算与配比全部按此重算。

## 2. 接口契约

| 边界 | 过界物 | 速率/体积 | 格式 | 错误处理 | 两侧所有者 |
|---|---|---|---|---|---|
| 传感器→MCU(W1) | AS5600 开度、ADS131M04 4ch 24-bit 力、ICM-42688-P 6 轴 | 各 1 kSPS;合计 ~40 B/ms ≈ 0.32 Mbps | SPI/I²C,DRDY 硬中断打戳 | CRC 逐帧;DRDY 缺失计数 >0.1% 判传感废 | 传感器件商 / 固件组 |
| MCU→本地存储 | 单晶振时戳二进制流 | 40 KB/s ≈ 0.14 GB/h | 自定义帧→坞站转 parquet | 双写环形缓冲;掉电保留最后 4 MB | 固件组 / 数据平面组 |
| GoPro 域↔MCU 域 | 时钟对齐信号(**唯一过界物是时间本身**) | 啁啾 20 ms 编码/2 s 注入 48 kHz 音轨;LED 时码 60 fps 入画 | 声学啁啾经 Media Mod 3.5mm;LED 二进制时码 | 啁啾丢失→QC 自动重采;互相关方差超限→整段降级 LED 帧级 | 时钟平面组独占(双侧固件不得私自对时) |
| 设备→坞站 | 原始 shard + 自检报告 | W1 ~164 GB/6h 班;USB 3.0 实测持续 ~30 MB/s → **单机拷贝 ~1.6 h**(⚖ R2,见下) | GoPro MP4(GPMF)+ MCU 流 + manifest 草稿 | 哈希校验失败重传;坞站 72h 本地缓存 | 设备组 / 坞站(数据平面) |
| 坞站→站点转码节点(⚖ R1 新增边界) | 已验证 raw 视频段 | 站点千兆内网($30 交换机),节点主动抓取 | MP4 原件 + 哈希清单 | 转码产物回写坞站哈希核对;节点宕机→坞站 HEVC 硬编降级 | 数据平面组(两侧同主) |
| 坞站→云 | 转码 shard + QC 判决 + 离线 SLAM 位姿 | 10 台站点 ~0.75 TB/天(见预算 a);持续 ~70 Mbps | LeRobot v2(Zarr 分块)+ manifest JSON | 幂等断点续传;云不可达→坞站持有 72h 后报警 | 数据平面 / 云脊柱 |
| 云→买家 dataloader | 证书化 episode | 按订单;RLDS 导出一键 | LeRobot v2 主格式,RLDS 副格式,`load_dataset` 即训 | 版本 pin + 哈希;负迁移投诉→训练价值化验仲裁 | 云脊柱 / 买家 |
| R1↔机器人总线 | **只读**侦听 EtherCAT(100 Mbps)/CAN-FD(≤5 Mbps)本体感知 500 Hz–1 kHz + 干预按钮事件 | 总线镜像 ~0.23 GB/h;按钮事件异步 | 隔离 tap(CAN:电容隔离收发器;EtherCAT:磁隔离监听绕组),硬件禁 TX;帧到达硬时戳 | tap 故障=零侵入(总线不受扰);侦听中断只丢数据不停机器人 | R1 盒(我方)/ 机器人主控(客户)——**白标契约:原始数据产权归客户** |
| 认证服务→买家 | per-episode 证书:ATE 上界、同步残差、力标定日期、训练价值化验分、本体对齐元数据 | 每 episode 一份,~2 KB | 签名 JSON,挂 CAICT/LeRobot manifest 参考实现 | 年度高校第三方审计;抽检不符→整批召回重验 | 认证主体(独立辖区)/ 买家 |

**⚖ 整合裁决 R2(入坞时间口径):** 原契约"单机 <20 min"按 USB3 峰值 ≥150 MB/s 写;实测持续吞吐 ~30 MB/s,164 GB 班产实际拷贝 **~1.6 h**。裁决采用诚实口径:入坞拷贝按 1.6 h/班/机预算,MCU 流(0.86 GB,USB FS MSC ~15 min)与 GoPro 卸载并行不占关键路径;坞站日程算术(§6)按 1.6 h 版成立,1:3 配比不受影响。

**⚖ 整合裁决 R4(R1 相机链路):** D405 无 GMSL 变体(RealSense GMSL 仅 D457),R1 相机链路实施为 **USB-only**;线长 >2 m 处用有源光纤 USB3 线(~$40)。原架构表述照此修正。

## 3. 预算表

### (a) 数据预算(每设备类型)

| 设备 | 模态×速率 | 原始 MB/h | 压缩后 MB/h(站点 AV1 / 无损) | 日存储(6h 班) |
|---|---|---|---|---|
| **W1** | 视频 HEVC ~60 Mbps + GPMF IMU 200 Hz + 音频 AAC 256 kbps + MCU 流 40 KB/s | ≈ **27.3 GB/h** | AV1 ~2:1 → **~14 GB/h**;MCU→parquet ~50 MB/h | 原始 164 GB;归档 ~85 GB |
| **W1e** | 同 GoPro,**不剪切长片段**(世界模型规格,像素保留) | **27 GB/h** | 归档保原始码率或 AV1 高档(CRF 24)~18 GB/h | ~110–164 GB(分层上行:语义摘要走蜂窝,原始按订单批量回传,[复审 #5](data-scaling-strategy.md)) |
| **L1** | 2× D405 848×480@30:RGB H.264 ~5 Mbps + 深度 z16 raw 24.4 MB/s,无损 RVL ~4:1;关节 100 Hz×14 DoF 忽略不计 | ~180 GB/h raw | **~50 GB/h** | ~150–200 GB(按有效记录 ~3–4h;整班连录上限 300 GB) |
| **R1** | 2× D405 同上 + 总线镜像 64 B×1 kHz=0.23 GB/h | ~180 GB/h raw | **~50 GB/h**(CPU x264 ultrafast + RVL,Orin Nano 无 NVENC) | 按部署班次,~200–400 GB |
| **Gen-2 传感头** (设计目标) | 2× AR0234 2.3MP@60 全局快门 + 2 kHz IMU + 1 kHz 力/触觉 | ~40 GB/h(板载编码后;传感器裸流 ~1.2 TB/h 不落盘) | 端侧 AV1 + 蒸馏分割 → ~15 GB/h | ~90 GB |

**10 台站点(8 W1 + 2 W1e)上行:** 10×27 GB/h×6h ≈ **1.64 TB/天原始** → 站点转码 + 15–20% 传感废剔除 → **~0.75 TB/天上云** = 24h 摊 8.7 MB/s ≈ **70 Mbps 持续**;工程配置 200 Mbps 专线或夜间 500 Mbps 窗口,断网退路为磁盘摆渡。坞站按 [复审 #18](data-scaling-strategy.md) **1 带 3**:10 台站点配 3–4 台 Orange Pi 5 Plus 坞站(~$150/台 (unverified))+ **1 台转码节点**(二手 x86 + RTX 4060,~$700 整机 (unverified)):60 h 素材 ÷ ~7× 实时 ≈ 8.6 h/天,单卡吃下全站,夜间窗口完成(⚖ R1)。

### (b) 功耗预算(每设备)

| 设备 | 分项 W(占空比) | 系统 W | 电池 | 续航 |
|---|---|---|---|---|
| **W1** | GoPro 录制 ~4.5(100%,去内电池 USB 直供)+ STM32H743 ~0.4 + ADS131M04/双 IMU/AS5600 ~0.05 + LED 时码 0.1 + SD 突发 + DC-DC 损耗 ~0.9 | **~5.8–6.2 W**(measured-class 估算) | 20,000 mAh USB-PD 72 Wh(Anker 535 类,~$50,腰挂) | 72×0.9/6.0 ≈ **10.8 h ✓(6 h 班余量 80%)** |
| **W1e** | GoPro 录制 ~4.5(100%) | **~4.5 W** | 10,000 mAh 37 Wh(~$22,后仓配重) | 37×0.9/4.5 ≈ **7.4 h,过 6h 班留 23% 余量** ✓ |
| **L1** | 主机 NUC ~30 W + XL330×14 编码器态 ~3 W(14×40 mA@5V) + 2× D405 ~4 W | ~37 W | **市电**(计量站固定工位) | n/a |
| **R1** | Orin Nano Super 25 W 模式 + 2× D405 4 W + NVMe 2 W | **~31 W** | 机器人 48V 母线经隔离 DC-DC(Mean Well DDR-60L-12);契约 ≤35 W 带保险 | 随机器人 |
| **Gen-2 W2** (设计目标) | RDK S100 8–12(BPU 占空比控制:VIO 仅在线 QC)+ 传感头 2 + 杂项 2 | ~10–14 W | 99 Wh(民航上限) | 99×0.9/12 ≈ **7.4 h** ✓ |

### (c) 时序预算(误差链,逐项分配)

**路径 1:W1 啁啾路径,总预算 <0.5 ms(未过月 1 台架前不得进 SLA):**

| 环节 | 分配 |
|---|---|
| ADS131M04/ICM DRDY→定时器输入捕获锁存(与 ISR 延迟无关) | <5 µs(实现达 ±1 µs) |
| STM32 晶振 ±20 ppm × 2 s 啁啾间隔漂移 | ±40 µs |
| 啁啾 DAC 输出确定性延迟(逐台产测标定后残差) | <10 µs |
| **GoPro 音频管线方差**(ADC+DSP+AAC 21.3 ms 帧粒度;均值可标定移除,方差是成败项) | **≤200 µs(月 1 台架实测项;>200 µs 即啁啾降级为漂移监测)** |
| 48 kHz 互相关亚采样分辨率 | ±10–21 µs |
| GPMF 域内视频↔音频(同晶振) | 0 |
| **合计(最坏)** | **~280–300 µs < 500 µs ✓(条件成立时)** |

**路径 2:LED 时码回退:** LED 驱动 <1 µs + 帧量化 ±8.3 ms @60 fps → **帧级**,只支撑 ≤10 Hz 语义标签与 S2 用途。
**路径 3:R1:** PTP offset <100 µs + CAN-FD 帧到达硬时戳 ~1 µs → **<100 µs 域**。
**路径 4:Gen-2 传感头 (设计目标):** 硬触发线抖动 <1 µs + 快门中点估计 <5 µs + IMU ODR 对齐 <5 µs → **<10 µs**。

## 4. 时钟平面详设

时间层级(从器件到舰队):**单器件晶振 → 设备内单钟域 → 跨域对齐信号 → 站点/机器人时间 → 舰队 gPTP (设计目标)**。绝对 UTC 只做溯源(坞站对时),永不做标签。

| 需对齐的域对 | 机制 | 期望精度 | 测量方法 | 失效模式 + 检测 |
|---|---|---|---|---|
| GoPro GPMF 内部(视频/IMU/音频) | 单硬件时钟,UMI 公理 | 0 融合误差 | n/a(构造保证) | 固件异常极罕见;GPMF 解析校验 |
| GoPro ↔ STM32 | 声学啁啾每 2 s 经 Media Mod($80)入音轨,离线互相关 | <0.5 ms(**待月 1 台架,全案最便宜实验**) | 100 会话啁啾 vs LED 双通道对拍,给出每设备管线延迟均值/方差 | Media Mod 接触不良/音轨削波→啁啾丢失计数触发自动重采;方差 >0.2 ms→整型号降级 LED |
| GoPro ↔ STM32(备份) | 视野角 LED 二进制时码(曼彻斯特 @30 bit/s,抗滚快门) | 帧级 ±8.3 ms | 帧解码直读 | 视野遮挡→该段仅供 S2;双通道同失→episode 报废 |
| STM32 ↔ 坞站 UTC | 回坞 USB 对时 | ms 级(仅溯源) | 每次入坞记录偏移 | 偏移跳变→晶振老化告警(>±5 ppm/月),设备召回标定 |
| **L1 主机单调钟(全线唯一软件时戳豁免)** | USB 设备统一打主机 monotonic;D405 无硬件同步引脚,librealsense global timestamp 映射,实测抖动 <1 ms | <1 ms(100 Hz 标签预算 10 ms,余量 10×) | episode 内时间戳单调性 + 间隔方差自检 | USB 调度尖峰→方差超限段打标;豁免自 Gen-2 传感头起废止 |
| R1 ↔ 机器人主控 | IEEE 1588 PTP over Ethernet(Orin 原生 RGMII 硬时戳,linuxptp) | <100 µs | PTP offset 遥测入 manifest | 主控无 PTP→退化为总线帧硬时戳 + 周期等距校验;offset 漂移→侦听段降级 |
| Gen-2 传感头内 (设计目标) | 锁步 Cortex-R52 时间戳岛(RDK S100,¥2,799 (unverified))+ 单触发线快门中点打戳 | <10 µs | 台架:LED 闪光同拍多传感器 | 触发线断→无戳即无数据(公理),设备自报下线 |
| 舰队跨设备 (设计目标,Gen-2 先 ms 级软同步,Gen-3 gPTP) | 802.1AS | <1 µs | pdelay 残差遥测 | 交换机不支持→双人协作任务退化为啁啾软同步 ms 级 |

## 5. W 系实现(W1 手持夹爪 + W1e 被动头戴)

90 天内用命名现货件建成 EVT→PVT。所有输出遵守脊柱契约:合法 LeRobot v2 shard + QC manifest,时戳全部可追溯至命名时钟域。

### 5.1 W1 电气架构

**拓扑:** 两个时钟域,一块自研板。GoPro 域(视频+200 Hz IMU+48 kHz 音频,GPMF 单晶振)与 MCU 域(力/开度/副 IMU,STM32 单晶振)之间**唯一过界物是时间**(啁啾+LED)。自研板"W1-MB"为 6 层 80×45 mm PCB,挂夹爪柄内。

| # | 器件 | 型号 | 街价 | 总线 | 选型理由 |
|---|---|---|---|---|---|
| U1 | MCU | STM32H743VIT6 | ~$10 (unverified,LCSC ~¥60) | — | 480 MHz、双 bank flash(A/B OTA)、1 MB SRAM(大环形缓冲)、SDMMC、双 12-bit DAC(啁啾)、32-bit 定时器输入捕获(硬件打戳) |
| U2 | 力 ADC | TI ADS131M04 | ~$6 | SPI1 @ 8 MHz,DRDY→TIM2_CH1 | 4ch 24-bit ΔΣ 同步采样 @ 1 kSPS;PGA=128 直连应变桥,免仪表放大器 |
| B1/B2 | 应变梁 | TAL220(10 kg,1 mV/V)×2 | ~$7/支 | 全桥模拟→U2 | 3.3 V 激励×1 mV/V=3.3 mV FS,PGA128 输入满量程 ±9.4 mV,桥 FS 占 ~35%(过载余量即由此来);噪声 <1 µV RMS → 分辨力 ~0.03 N,0.5 N 系统指标由机械/温漂主导,余量 >10× |
| U3 | 主副 IMU | ICM-42688-P @ 1 kHz ODR | ~$3 | SPI2 @ 24 MHz,INT1→TIM2_CH2 | 路线图钦点;Gen-2 同件延续 |
| U4 | 第二副 IMU | ST LSM6DSO32 @ 833 Hz | ~$3 (unverified) | SPI2 片选 2,INT→TIM2_CH3 | 见 ⚖ R3 |
| U5 | 开度编码器 | AS5600(手指转轴卫星小板) | ~$5 | I²C1 @ 400 kHz,TIM17 触发 1 kHz 轮询 | 12-bit/0.088°;单次读角 ~125 µs,1 kHz 轮询余量 8× |
| U6 | 存储 | SanDisk Industrial 32 GB microSD | ~$10 | SDMMC1 4-bit @ 50 MHz | 40 KB/s 流零负载;工业卡保写入延迟尾部 |
| U7 | PD 受电 | WCH CH224K | ~$0.4 | 独立 | 向充电宝申请 9 V,避免 1.5 m 线缆压降致 GoPro 掉电复位 |
| U8 | 5.2 V 主 buck | MPS MP2338(3 A) | ~$0.5 (unverified) | — | GoPro 供电 + LED + 振动马达 |
| U9 | 3.3 VD buck | TI TPS62823 | ~$0.6 | — | MCU/SD/IMU/AS5600 数字轨 |
| U10 | 3.3 VA LDO | TI TPS7A2033(低噪) | ~$0.7 | — | ADS131M04 AVDD + 应变桥激励,与数字轨隔离,桥激励与 ADC 同源近比例 |
| U11 | 振动马达驱动 | 2N7002 + 10 mm ERM | ~$0.8 | GPIO PWM | 漂移告警触觉提醒(QC 三件套 #1) |
| D1 | LED 时码 | OSRAM LUW 型 0.5 W 白光 + 恒流 MOSFET | ~$1 | TIM3 PWM+DMA | 入画二进制时码,帧级回退通道 |
| — | 啁啾链路 | DAC1_OUT→RC 低通(fc 12 kHz)→100:1 分压至 mic 电平→交流耦合→3.5 mm TRRS | ~$1 | DAC+DMA,TIM15 触发 | 进 Media Mod(ADFMD-001,$80)mic 口;分压中点回抽 ADC1 做**电气自环检测**(啁啾确实发出) |

**⚖ 整合裁决 R3(端上双 IMU 的实现细化):** 原 QC 三件套把"双 IMU 漂移告警"写为 GoPro IMU vs MCU IMU。物理事实:GoPro IMU 数据在 GPMF 内**仅离线可读**,无法实时参与端上告警。裁决:端上实时告警由两颗异厂家 MCU 侧 IMU(U3 ICM-42688-P + U4 LSM6DSO32,+$3,误差去相关)承担;**权威残差(GoPro↔MCU)仍按契约由坞站在 20 min 回灌内离线复算**,超限整段判传感废。判据不变,执行分层。

**功率树:** 充电宝 → USB-C 1.5 m → CH224K@9 V → MP2338 5.2 V(GoPro ~870 mA avg、LED 30 mA avg、ERM 80 mA 突发)+ TPS62823 3.3 VD(H743 @240 MHz ~120 mA、SD 均值 15 mA、双 IMU 2 mA、AS5600 7 mA)+ TPS7A2033 3.3 VA(双桥 ~19 mA、ADC 3 mA)。合计 ≈5.6 W + 转换损耗 ≈ **5.8–6.2 W**(预算表 b)。

**接插件:** J1 USB-C(PD 入电 + 坞站数据,MCU 走 USB 2.0 FS MSC);J2 3.5 mm TRRS(啁啾);J3/J4 JST-SH 4-pin(左右应变桥);J5 JST-SH 5-pin(AS5600 卫星板);J6 JST-SH 6-pin(SWD 产测/烧录);J7 2-pin(ERM)。GoPro 供电走 Media Mod 直通 USB-C。

### 5.2 W1 固件架构

**RTOS:FreeRTOS 10(CMSIS-RTOS2),但打戳一律不经任务**——时间纪律在硬件定时器层闭合,任务只搬运已带戳的数据。

**时戳纪律(P2 平面在设备内的落地):** TIM2 配 32-bit 自由计数 @ 1 MHz(溢出 ISR 扩至 64-bit,全程单调);三路 DRDY/INT 物理接 TIM2 输入捕获通道——**采样时刻由捕获寄存器锁存,与 ISR 延迟无关**,打戳抖动 = ±1 µs,优于契约 <5 µs 分配。ISR 只做:读捕获值→读 FIFO→组帧压入无锁 SPSC 队列。AS5600 由 TIM17 精确触发 I²C DMA 事务,戳取事务启动沿。啁啾发生:TIM15 触发 DAC1+DMA 播 20 ms 线性扫频(2→8 kHz @48 kHz),触发沿同锁 TIM2 得 t_chirp;8 种签名波形轮换编码序号,坞站互相关后建立"啁啾序号↔MCU 64-bit 戳↔音轨样点"三元组。DAC 链路确定性延迟产测标定,残差 <10 µs 入预算。

| 任务 | 周期 | 优先级 | 截止期 | 职责 |
|---|---|---|---|---|
| (ISR/捕获) | 事件 | HW | <5 µs | 锁存时戳、组帧入队 |
| tSense | 1 ms | 5 | 1 ms | 排空队列→环形缓冲,逐帧 CRC16,DRDY 缺失计数(>0.1% 判传感废,契约项) |
| tChirp | 2 s | 4 | 5 ms | 排程啁啾 + ADC 自环验证,失败计数入 manifest |
| tLED | 33.3 ms | 4 | 2 ms | 20-bit 计数器曼彻斯特编码 @ 30 bit/s(60 fps 每比特 2 帧,抗滚快门) |
| tLog | 10 ms | 3 | 500 ms | 512 KB SRAM 双写环形缓冲→64 KB 块写 SD;耐受 >10 s SD 卡顿(40 KB/s×10 s=400 KB) |
| tQC | 100 ms | 2 | 100 ms | 双 IMU 积分残差、力通道饱和/零漂监测 |
| tUI | 50 ms | 2 | 50 ms | 按键(录制/事件标记)、状态灯、振动告警 |
| tHealth | 1 s | 1 | 1 s | 看门狗、轨电压/温度、f_sync |
| tUSB | 坞内 | 3 | — | MSC 暴露 + 对时 + OTA |

**存储路径:** 帧格式 `[magic|type|t64|payload|CRC16]` 追加写入预分配 exFAT 文件(FatFs,4 MB 段滚动,每 1 s f_sync)——满足"掉电保留最后 4 MB"。6 h 班 ≈0.86 GB,入坞 USB FS MSC ~15 min,与 GoPro USB3 卸载并行(总入坞时间口径见 ⚖ R2)。设备端布局:`/W1-<SN>/<session>/mcu.bin + manifest_draft.json + selftest.json`,坞站负责转 parquet 与 LeRobot v2 组装(异构性不越坞站,P1 不变量)。

**QC 三件套实现:**
1. **漂移告警数学:** 两 MCU 侧 IMU 各自跑重力对齐捷联双积分,静持段(‖ω‖<0.5°/s 且 ‖a−g‖<0.05 g 持续 300 ms)做 ZUPT 复位;30 s 滑窗内位置残差 ‖Δp₁₂‖>2 cm → ERM 振动 3 短脉冲,episode 打 `drift_suspect`。共模真运动相消,残差是传感误差包络的实时代理;权威判决由坞站复算(⚖ R3)。
2. **自动重采触发(端上/坞站分工):** 端上可判:啁啾电气自环失败 ≥2 次/min、力通道满幅 >1% 时长、DRDY 缺失、SD 写失败——即时振动+屏灯要求重拍。需视觉的判据(锚板可见率 <50%、过曝 >5%、特征数低)由坞站在回灌内判出,同班次重拍。
3. **标定健康自检:** 开班"8 字绕锚板"30 s(固件振动节拍引导)→ 入坞后坞站跑离线 VIO,ATE 自测 >8 mm 判下线;CharUco 重投影 >0.3 px 拒采;力零漂 >0.2 N 或 500 g 检重块偏 >0.3 N → 返厂标定标志。

**OTA + 产权初始化:** H743 双 bank A/B 镜像,Ed25519 签名,坞站 USB DFU 推送,失败自动回滚;provisioning 写入:SN、密钥、逐台标定 blob(相机内参、IMU-cam 外参、力增益/偏置、啁啾管线延迟均值)——标定 blob 哈希进每份 QC manifest,证书可溯源到台架。

### 5.3 W1 机械

- **打印结构:** 主体 PAHT-CF(拓竹 X1C),壁厚 3 mm、gyroid 40%;力路径件(梁座、指座)实心打印或 6061 CNC 小件。手柄为 UMI 式扳机构型:扳机经连杆驱双指平行开合,转轴端埋 AS5600 磁铁(径向磁化,气隙 1.0±0.5 mm)。
- **应变梁载荷路径(力读真):** 每指一支 TAL220 悬臂——固定端 2×M5 锁底盘,自由端经 6061 转接块挂指托;载荷路径唯一:物体→TPU 指垫→指托→梁自由端→底盘,**无并联旁路**(走线 30 mm 服务环、零预紧)。过载止挡:底盘限位销,间隙设为 120 N 对应挠度(TAL220 极限 150% FS),跌落/夹硬物时销先受力,梁不塑变。
- **GoPro 笼 + 鱼眼禁区:** Hero9 + Max Lens Mod(155°)顶置笼架,禁区为镜头前 155° 锥体——结构件全部退出锥外,仅两件**故意入画**:视野下缘角 LED 时码窗(D1)与 25×25 mm 前表面亚克力反射镜(UMI 式隐式立体,安装角产测标定)。指尖外侧贴 12 mm ArUco 码,做开度视觉交叉验证与遮挡判据。
- **TPU 指接口 + 维护性:** 指垫 95A TPU 燕尾滑槽+卡扣,徒手 <1 min 换;凝胶垫(触觉选配位)为耗材,班检更换。SD 卡与 TRRS 免拆壳可达。
- **重量预算(目标 ≤750 g 手持,充电宝腰挂不计):** Hero9(去电池)126 g+Max Lens Mod 49 g ≈ 175 g、Media Mod 76 g、2×TAL220+转接 75 g、W1-MB+SD+走线 38 g、打印底盘+手柄+连杆 190 g、笼+镜+LED 窗 65 g、指托+TPU 垫 45 g、AS5600 卫星板 12 g、紧固件/减振垫 35 g → **合计 ~711 g ✓(余量 ~39 g)**。

### 5.4 W1e 被动头戴(delta 单)

**移除:** W1-MB 整板、力/开度/Media Mod/啁啾/LED——单 GoPro 域内视频+IMU+音频同晶振,**无跨域对齐问题,时钟平面构造性满足**。**保留/新增:** Hero9 + Max Lens Mod、头带、顶置散热铝板、后脑勺电池仓。BOM 对齐路线图 $350。

- **度量深度(世界模型契约字段):** 主路线**纯标定路线,零加件**——逐台 CharUco 内参(Kannala-Brandt)+ Kalibr IMU-cam 外参入 provisioning blob,坞站离线 VI-SLAM(GPMF 200 Hz IMU 提供度量尺度)输出帧级 ego-pose + 尺度化深度(单目稠密 MASt3R 类以 VIO 尺度约束);ATE 证书照锚板审计抽检。硬件选项 (设计目标):Gen-1.5 夹扣式 60 mm 基线 AR0234 全局快门立体头,与 Gen-2 传感头同件系,不进 90 天范围。
- **不剪切长片段的工程后果:** 27 GB/h×6 h=164 GB → SanDisk Extreme 512 GB(~$45)单卡整班;GoPro 4 GB 章节化不破"时间轴无剪切"声明(同一晶振,章节拼接零缝)。热:Hero9 连录过热是已知失效——对策三件:去内电池 USB 直供(内热源 −30%)、4K30 8-bit 档(非 5K)、机背 40×60 mm 铝板经导热垫开框散热;EVT 必测 35 ℃ 环温 6 h 连录不热停。
- **佩戴性:** 前部 ≤290 g,后仓电池 ~190 g 配重,**头戴总重 ≤480 g**,前后力矩近平衡;三点织带+顶带,镜头额前眉心上 3 cm,俯角 25°(桌面操作视野)。隐私指示灯常亮(录制状态外显,采集合规)。

### 5.5 标定与产测

**工厂标定序列(每台,顺序执行):**
1. **相机内参:** 12×9 CharUco(6 mm 格),电动转台 30 位姿自动采,Kannala-Brandt 4 参鱼眼拟合,通过限 RMS <0.3 px。
2. **IMU:** 10 min 静置 Allan 方差(零偏不稳定性建档)→ 6 面翻转标 accel 零偏/标度。
3. **IMU-cam 外参:** Kalibr,机械臂/治具摇台带板扫 60 s 激励全轴,通过限:重投影 <0.5 px、外参协方差收敛。
4. **力梁标定:** 挂码 0/0.5/1/2/5/10 kg 三循环升降,拟合逐梁增益/偏置,通过限:非线性+迟滞 <0.3% FS(0.3 N),温漂系数抽 10% 台份做 10–40 ℃ 箱。
5. **啁啾管线延迟逐台标定:** 治具内本机录 30 发啁啾 + LED 双通道对拍,互相关得逐台延迟均值(入 provisioning)与方差;**通过限:方差 ≤200 µs**(时序预算成败项)。注意:逐台产测不替代月 1 舰队级 100 会话台架门禁。

**EOL 工站:** 暗罩工位(LED 时码判读)+ 锚板墙 + 挂码架 + 摇台 + 坞站脚本一键跑完 1–5 项 + 电测(轨电压、待机/录制电流、DRDY 计数、SD 写速)+ 8 字仪式 ATE 自测 <6 mm。判据全部机读,报告哈希入 provisioning。**节拍 12 min/台**(内参 4 + 外参 3 + 力 3 + 啁啾/电测 2),单工站 40 台/班,PVT 两工站够 ramp。

**现场重标节奏:** 每班 8 字仪式(ATE 自测);每周 500 g 检重块 30 s 力核查;力标定有效期 **90 天**入证书字段(过期该 episode 证书降级);内参/外参年检或跌落/换镜后立即返厂。

## 6. L1 / R1 / 坞站实现

### 6.1 L1 计量套件

**编码器链。** 14× DYNAMIXEL XL330-M288-T($27.49/只,ROBOTIS 官方价 as of 2026-07),纯编码器态(torque off 或重力补偿电流态),12-bit/0.088°。总线:TTL 半双工 3-pin JST,**每臂一条独立菊花链(7 只)**,两链各接一只 U2D2($36.92)走 USB——不并链是为把总线时延减半并隔离单链故障。4 Mbps、Return Delay Time=0、Protocol 2.0 **Fast Sync Read** 读 Present Position(4 B):指令包 ≈21 B + 状态包 ≈65 B ≈ 860 bit → **215 µs/链/帧**;瓶颈在 USB 往返:U2D2 的 FT232H(USB 2.0 HS)latency timer 置 1 ms,轮询往返最坏 ~2.5 ms;100 Hz 周期 10 ms → 占空 25%,**100 Hz × 14 关节余量 4×**,500 Hz 可达但不承诺。

**供电。** XL330 空载 ~40 mA@5V ×14 ≈ 0.6 A;U2D2 不供电,独立 5V/3A 桌面电源经 SMPS2DYNAMIXEL 类转接($8)注入每链;重力补偿电流态峰值按 2A/链保险。主机 NUC 类 x86(~$450 (unverified))市电,系统 ~37 W(预算表 b)。

**D405 对。** 关键事实:**D405 无硬件同步引脚**(inter-cam sync 连接器不存在,官方不支持多机硬同步),两只 D405($272/只)自由跑 30 fps,靠 librealsense global timestamp 打戳,实测抖动 <1 ms——恰落在 L1 的**全线唯一软件时戳豁免**内(100 Hz 标签预算 10 ms,余量 10×)。带宽:深度 z16 raw 24.4 MB/s/只,**两只必须挂不同 USB 3.0 root hub**,否则丢帧判传感废。安装:一只顶视(工位横梁打印云台)、一只 45° 斜视;外参 CharUco 标定,重投影 >0.3 px 拒采。

**机械(运动学孪生设计规则):**
1. **从目标 URDF 导几何:** 解析 `<joint>` 轴向量与 `<origin>`,只保留旋转轴相对方位与连杆比例,整机线性缩放 0.5–0.7×(GELLO 惯例)至人手臂舒适包络;**轴方位 1:1 保留、连杆长度可缩放**——关节空间记录(DROID 论据)只要求轴拓扑同构,不要求笛卡尔同尺。
2. **公差策略:** PETG 打印孔位预留 0.2 mm 后铰刀精铰;轴承座压入 683ZZ 微型轴承(¥1/只),**不让舵机输出轴承受弯矩**;XL330 花键盘直连,回差主要来自打印件蠕变——设计规则:承载梁 ≥3 mm 壁厚 + 15% gyroid,关节零位靠**钢销定位孔**而非止口面。
3. **零位夹具:** 每臂一块打印"归位梳",开机把 7 关节卡入已知角度,消除 XL330 多圈计数不确定。
4. **重力平衡两档:** 默认橡皮筋/恒力弹簧被动配重(零功耗、零固件);选配 XL330 电流模式主动补偿(GELLO 已证),代价是供电按 2A/链走线。

**计量角色实施(审计协议硬件 + 真值计算):**
- **锚板套件(~$180/套):** 6 mm 铝塑板热贴 CharUco(A2,12×9,40 mm 格)+ 板面 3 只淬硬钻套(位置 CMM 单次溯源标定,证书随套件);运输箱 + 三点磁座可重复安装。
- **L1 自身标定:** 打印件 DH 参数不可信,做**触点辨识**:持末端标定尖依次触 3 钻套 × 25 姿态,最小二乘辨识 DH+零位偏置;验收残差 RMS <1 mm。此后 FK 输出即 measured EEF 真值(±1 mm)。
- **审计会话真值:** 野外审计时,W1 夹爪刚性夹持 L1 末端适配销(或装在被 L1 遥操的跟随臂上)同场录制;真值 = L1 FK@100 Hz,被审对象 = W1 SLAM recovered 轨迹;时间对齐用 W1 自己的啁啾/LED 链(比对用相对轨迹 ATE,绝对钟差不入误差)。输出 per-session ATE 上界,直接写入该批次 W1 证书抽检字段。
- **EOL 三项:** (1) 全关节扫摆,编码器单调性与丢步计数为零;(2) 三钻套复触,FK 重复性 <0.5 mm;(3) 24 h 上电漂移 <1 LSB。整臂 BOM ~$390/臂(GELLO 基线 $363;XL330 2026-07 涨价至 $27.49、U2D2 至 $36.92 后重算)、双臂全配 ~$2,650(路线图 $2,600 基线 +$50 价差)。

### 6.2 R1 改装盒

**核心板。** Jetson Orin Nano Super 8GB 模组 + 第三方载板(Seeed reComputer J401 类,~$199 (unverified)),不用开发套件(无外壳/温度域)。**Orin Nano 无 NVENC**:视频压缩走 CPU x264 ultrafast(2× 848×480@30 占 6 核 A78AE ~10%)+ 深度 RVL 无损(~4:1)。存储:2 TB NVMe(致态 TiPlus7100,~¥750)作**环形缓冲**:~50 GB/h → **~40 h 环深**,覆盖"云不可达 72 h"契约的移动折衷(客户侧 NAS 分流后实际 >72 h)。相机 2× D405 USB-only(⚖ R4),双相机分 root hub。

**总线侦听(只读 tap,为何扰动不了机器人):**
- **CAN-FD 路径:** ISO1042(隔离收发器,5 kVrms,~$2.5)+ MCP2518FD(SPI 控制器,~$2.5)挂 Orin 40-pin SPI。三重不可扰保证:(1) **Listen-Only Mode**——不发 ACK、不发错误帧;(2) **TXD 引脚硬件上拉焊死至 VCC**(永久隐性,物理不可能拉显性);(3) ISO1042 SiO₂ 电容隔离栅(5 kVrms),tap 掉电=高阻,总线端接不变。帧到达在 MCP2518FD 本地时基打硬时戳(µs 级),经 PTP 换算入 manifest。
- **EtherCAT 路径:** EtherCAT 是切通式菊花链,**不得插入存储转发设备**(破坏 DC 分布时钟测距)。实施为**只收铜缆 tap**:段间跳线处并出两对监听绕组,各接只收 PHY(监听板 TX 差分对**物理不布线**),磁隔离 1.5 kV——无发射路径、无协议栈,电气上等同一段略长走线;若客户要求零信号衰减,改用再生 tap 并要求在 EtherCAT 主站 DC 测距**之前**上电(传播时延被测距吸收)。两监听口进 Orin:M.2 E-key 双口 i226/i210 采集卡(~$35 (unverified)),**RX 全包硬件时戳**。
- **解析目标:** CiA-402 循环 PDO——Statusword 0x6041 状态机、0x6064 实际位置、0x606C 速度、0x6077 力矩,500 Hz–1 kHz;PDO 映射需客户提供 ENI/EDS(部署 checklist 第一项)。

**干预按钮。** 22 mm 工业蘑菇头瞬动钮,RC 硬件去抖(10 kΩ/100 nF)+ 固件 5 ms 确认;GPIO 中断按 PTP 驯化的 CLOCK_MONOTONIC 打戳,对齐总线帧 <1 ms(<1 帧契约,余量足,无需独立 MCU)。双击=失败标记,长按=损坏标记(结果标签三值)。

**PTP。** Orin 原生 RGMII MAC 支持 IEEE 1588 硬时戳;linuxptp(ptp4l+phc2sys)作 slave 追机器人主控,offset 遥测入 manifest;主控无 PTP 时退化为总线帧硬时戳+周期等距校验。

**白标边界(密码学实施)。** 原则:**原始数据我方不可读,证书我方可签。** (1) NVMe 全盘 LUKS,数据密钥用**客户 KMS 公钥**信封加密——盒子丢了我方也解不开;(2) 盒内计算 QC 指标/同步残差/ATE 代理后,**只有签名证书 JSON(~2 KB/episode)+ 脱敏元数据**经我方 SaaS 通道出盒;(3) 原始 shard 走客户内网直传客户 NAS;(4) 签名 Ed25519,私钥封在 NXP SE050 安全元件(~$2)内不可导出,证书链根在认证主体(独立辖区)。审计接口:客户可授权我方对**哈希指定的** episode 做一次性远程复验,密钥仍由客户释放。

**供电/安装/散热。** 机器人 48V 母线 → Mean Well DDR-60L-12(DIN 导轨隔离 DC-DC,18–75V 入,60 W,~$25)→ 12V 载板;48V 入口 3A 保险 + TVS;系统实测目标 ~31 W,契约 ≤35 W。压铸铝外壳 IP54,模组导热垫贴壳无风扇(25 W 模式壳温 <60 ℃ 台架验证项);DIN 导轨或躯干板 + 硅胶减振垫。**BOM 合计 ~$1,400**(含相机 $544、Orin+载板 ~$450、NVMe/电源/壳体/tap 板 ~$400)。

**固件。** 单一 Rust/C++ 守护进程,四线程:sniffer 解析(CiA-402 状态解码 + 帧时戳重排)→ 环形写入(parquet 分块,append-only)→ 事件通道(干预/结果标签)→ 证书预计算。修正 flag 事件 schema(LeRobot v2 扩展字段):`{event_id, episode_hash, t_bus_frame, t_ptp, type: takeover|release, outcome: success|failure|damage, operator_id, sw_state_0x6041}`——24 h 内回注脊柱(飞轮 SLA)。

### 6.3 QC 坞站(职责按 ⚖ R1 重分配)

| 节点 | 硬件 | 职责 |
|---|---|---|
| 坞站(1 带 3) | Orange Pi 5 Plus 16 GB(RK3588,~$150 (unverified))+ 2×4 TB HDD + USB3 hub | 入坞哈希校验、离线 ORB-SLAM3、QC 三件套判决、manifest/证书字段、隐私模糊(NPU)、断点续传上行、72 h 缓存;降级模式 HEVC 硬编 |
| 站点转码节点(每站 1 台) | 二手 x86 + RTX 4060(第 8 代 NVENC AV1 硬编,~$280 (unverified),整机 ~$700) | 全站 AV1 转码,10×6 h=60 h 素材 ÷ ~7× ≈ 8.6 h/天,夜间窗口完成 |

**吞吐算术(每坞每天,诚实版,单台 W1 一个 6 h 班):**
- 入坞拷贝:164 GB ÷ 30 MB/s 实测持续 ≈ **1.6 h**(⚖ R2 口径);
- ORB-SLAM3 单目-惯性(4K 降采 960p):RK3588 4×A76 单实例 ~1.0–1.2× 实时,8 核 2 实例 → 6 h 素材 ≈ **3 h 墙钟**;
- QC 判决 + 啁啾互相关 + manifest:**~0.5 h**;
- 上行与计算重叠不占预算。

单班合计 ~5 h 墙钟/设备 → 24 h 坞站吃 4.8 班,取 3 台 = 15 h,**余量 1.6×——1:3 配比成立,但前提是 AV1 已外移**;若强行 RK3588 软编则余量为负,这正是把 v1.1 的低估警告变成显式架构决策(⚖ R1)的原因。10 台站点 = 3–4 坞 + 1 转码节点,与预算表 (a) 一致。站点网络:200 Mbps 专线 + 夜间 500 Mbps 窗口 + 磁盘摆渡退路;坞站间千兆内网交换机($30)供转码节点抓取。

**视频编码参数(转码节点执行):** AV1 10-bit,CRF 30 / preset 8 等效档,keyint=60(2 s,帧级 seek),film-grain 合成关(伪纹理污染 SLAM 重放);W1e 世界模型档 CRF 24、**不剪切**、时间轴零删帧声明入证书。降级 HEVC 时证书 `codec` 字段如实记录,1:3 配比重算。

## 7. 数据脊柱实现

### 7.1 Shard 布局(LeRobot v2 兼容,一字不多)

```
<dataset_repo>/
  meta/info.json            # fps=30, robot_type="umi-w1", codebase_version="v2.1"
  meta/episodes.jsonl       # 每行: episode_index, tasks, length, qc_manifest_hash
  meta/tasks.jsonl, meta/stats.json
  data/chunk-XXX/episode_XXXXXX.parquet      # 30 Hz 帧对齐主表
  data_hf/chunk-XXX/episode_XXXXXX.parquet   # 1 kSPS 原生高频表(扩展目录,不破坏 load_dataset)
  videos/chunk-XXX/observation.images.wrist/episode_XXXXXX.mp4
  audio/chunk-XXX/episode_XXXXXX.m4a         # 含啁啾的原始 GPMF 音轨(证据链,不删)
  qc/chunk-XXX/episode_XXXXXX.cert.json      # 签名证书
```

- **主表列(30 Hz):** `timestamp`(GPMF 域,float64 s)、`observation.state`(EEF 位姿 7 维 + 开度 1 维,float32)、`action`(下一帧 EEF 目标)、`observation.force_n`(帧内 1 kSPS 力降采样均值+峰值 2 列)、`episode_index/frame_index/task_index`、`pose_source`(recovered/measured)。
- **高频表(1 kSPS,MCU 域原生):** `t_device_ns`(int64,STM32 单晶振)、`t_gpmf_ns`(int64,经啁啾偏移样条映射;LED 回退时置 null 并在证书降标)、`force_raw[4]`(int32 原码)、`force_n[2]`(标定后)、`gripper_rad`、`accel[3]/gyro[3]`、`drdy_gap_flag`。R1 另有 `bus_mirror` 表:`t_hw_ns`、`joint_pos/vel/tau[N]`、`intervention_flag`、`outcome_label`。触觉垫(Gen-2)同表加 `taxel[100+]`(uint16)@500 Hz。

### 7.2 Per-episode QC manifest / 证书 JSON(证书=manifest 的签名超集)

```json
{ "schema": "spine-cert/1.2", "episode_id": "uuid", "device_id": "w1-0042",
  "fw": {"mcu": "1.4.2", "gopro": "H9.01.02.10"},
  "clock": { "sync_method": "chirp|led|host|ptp",
    "chirp": {"offset_us_mean": 1234.5, "offset_us_var": 0.021,
              "loss_count": 0, "bench_cert_id": "M1-BENCH-…|null"},
    "sync_residual_us": 180, "residual_class": "sub-ms|frame|10ms" },
  "pose": { "ate_upper_mm": 5.8, "method": "orbslam3-mi+anchor-pg",
    "anchor_visible_frac": 0.83, "label_rate_hz": 60,
    "pose_provenance": "recovered|measured", "no_interp_spectrum_pass": true },
  "force": { "calib_date": "2026-06-28", "calib_cert": "FC-…",
    "shunt_check_pass": true, "valid_until": "2026-07-28" },
  "codec": "av1-crf30|av1-crf24|hevc-crf23",
  "taxonomy": "success|task_failure|sensor_reject",
  "failure": {"labels": ["slip","drop"], "recovery_present": true},
  "intervention_events": [{"t_ns":"…", "outcome":"success|failure|damage"}],
  "worldmodel": {"uncut": true, "metric_depth": false, "ego_pose_framewise": true},
  "privacy": {"blur_stage": "dock|module", "model": "yolov8face-1.3", "screen_blur": true},
  "assay": {"benchmark": "spine-bench-v1", "co_train_delta_pp": 2.1, "batch_id": "…"},
  "embodiment": {"eef_frame": "tcp-relative", "gripper_geom_hash": "…", "mix_advice_ref": "…"},
  "diversity": {"scene_emb_cluster": 1187, "near_dup_score": 0.06, "operator_id_hash": "…"},
  "sig": {"alg": "ed25519", "key_id": "cert-2026a", "merkle_leaf": "…"} }
```

`taxonomy=sensor_reject` 不建 shard,只留 manifest 尸检行;`task_failure` 完整入库并进失败-恢复 SKU 目录(P4 三分类)。**⚖ R6(啁啾 SLA 的字段级落地):** 月 1 台架通过前,`residual_class` 一律填 `frame`、`bench_cert_id` 为 null;台架通过后由 `bench_cert_id` 指向舰队级台架证书,`sub-ms` 才可出现——SLA 由 schema 强制,不靠文档自觉。

### 7.3 Ingest 流水线(坞站→云,六段)+ 每 1,000 h 算力标定

| 段 | 做什么 | 每 1k h(W 系)算力/成本 |
|---|---|---|
| 1 上传 | 坞站幂等分块上传(S3 兼容,内容寻址),raw 落 append-only 桶 + 对象锁 | 归档 ~14 TB,低频访问层(S3-IA 类 $0.0125/GB·月)~$175/月 → 90 天转冷($0.004/GB·月)~$56/月 |
| 2 验证 | GPMF 解析、哈希、DRDY 缺口率、啁啾丢失计数、单调性检查;此处判 sensor_reject(15–20% 预算) | CPU 忽略不计(<0.05× 实时) |
| 3 SLAM/精化 | ORB-SLAM3 单目-惯性重放 + AprilTag 锚板位姿图 + 固定滞后平滑;输出 60 Hz 位姿 + 逐段协方差 | ~1× 实时 @8 vCPU → 8,000 vCPU·h,spot ≈ **$120–200** |
| 4 证书计算 | ATE 上界(平滑器协方差 × 锚板残差校准系数,审计回合月度回归)、同步残差、频谱插值检查、隐私复检抽样 | +0.1× 实时 CPU;训练价值化验按 100 h 批:微调 spine-bench 小策略 ~15 GPU·h/批 → 150 GPU·h ≈ **$300**(L40S $2/h) |
| 5 去重/多样性 | DINOv2 ViT-B 每秒 1 帧嵌入(3.6 M 帧)→ FAISS;near_dup>0.92 降权不删 | ~4 GPU·h ≈ $8 |
| 6 编目+标注 | VLM hindsight(Qwen2.5-VL-7B 类,30 s 一段,120k 段)、语言一致性抽检 3%、目录索引 | ~60 GPU·h ≈ **$120** |

**计算类增量云成本合计 ≈ $550–650 / 1k h(段 3–6:$548–628,<$0.7/h);存储另计 ~$175/月/1k h(90 天后 ~$56/月),兼容 v1.1 全摊 $/h 表。** 队列深度、每段时延入遥测;段 3–6 全部以 raw 哈希为输入,可无限重放(P3 不变量)。

### 7.4 认证服务(独立主体,[复审 #17](data-scaling-strategy.md))

- **算什么/签什么:** 段 4 四元组(ATE 上界、同步残差+方法、力标定日期链、训练价值化验分)+ taxonomy + embodiment 元数据。Ed25519 签名,私钥在独立辖区 HSM(KMS 托管);每张证书入 RFC 6962 式 Merkle 透明日志——**证书不可静默重发,召回必须留痕**(对应"证书通胀"遏制)。
- **买家验证 API:** `GET /v1/cert/{episode_id}` → 签名 JSON;`GET /v1/log/proof/{leaf}` → 包含证明;公钥+审计报告公开页。买家离线验签,不依赖我方在线服务——"ARM 式生态税"的技术形态。
- 抽检不符 → 按 batch_id 整批 `revoked`,透明日志追加撤销叶,下游 dataloader 默认拒读。

### 7.5 多样性赏金调度器

输入:场景嵌入聚类占有数 `n_c`、清华幂律边际值、买家订单缺口向量(含失败 SKU 与世界模型长片段配额)、操作员质量分、化验增量反馈。赏金:`B(c) = B0 · (n_c+1)^(−γ) · max(1, demand_c) · assay_gain_ema_c`,γ 初值 0.6,每 5k h 用固定基准 co-training 增量回归重估;10% 预算 ε-greedy 探索未见聚类;饱和聚类(增量 <阈)赏金指数衰减至地板价。失败-恢复片段单独配额行,**不与成功片抢同一预算池**。

### 7.6 操作员 App + 舰队遥测

- **App(Android,BLE 连 MCU + GoPro Wi-Fi 状态):** 任务页=赏金列表按预期 ¥/h 排序;实况 QC 镜像端上三件套(漂移振动告警、啁啾丢失计数、锚板可见率),红黄绿三灯;开工 8 字仪式引导;**支付事件:接单托管 → 坞站证书通过即结算(sensor_reject 不付、task_failure 全额付——激励与三分类对齐,操作员无动机隐瞒失败)**;周结走支付宝/微信企业付款,质量分决定 L2 高价任务解锁。
- **遥测看板(TimescaleDB + Grafana):** 每设备时序:入坞晶振偏移(老化 >±5 ppm/月告警召回)、双 IMU 残差直方图、ATE 自测趋势、力标定漂移(空载零点+砝码抽检)、啁啾方差滚动 P95(>0.2 ms 触发整型号降级 LED 的自动工单)、坞站队列深度/转码时延。机队精度分布对买家只读开放——**证书的可信度本身是产品**。

### 7.7 训练对接(buyer-side)

**Dataloader 契约(伪代码):**

```python
ds = load_dataset("spine/w1-2026Q3")                 # 标准 LeRobot v2,零改造可用
certs = CertIndex(ds, pubkey=SPINE_PUBKEY)           # 验签 + 透明日志包含证明
ok = certs.filter(ate_upper_mm<=6, sync_residual_class=="sub-ms",
                  force_calib_valid=True, taxonomy in {"success","task_failure"},
                  revoked=False)
s2_view = ok.view(rate_hz=2, keys=["video","audio","lang"], dedup_max=0.92)   # 小时×多样性轴
s1_view = ok.filter(no_interp_spectrum_pass=True, taxonomy=="success") \
            .view(rate_hz=60, keys=["state","action","force_n","video"],
                  join_hf="data_hf")                  # 高频表按 t_gpmf_ns 对齐拼接
wm_view = ok.filter(worldmodel.uncut==True).view(segment_min_s=60,
                  keys=["video","ego_pose","depth?","outcome_branches"])
```

降级语义写死:`sync_method=="led"` 的 episode 在 s1_view 自动剔除、s2_view 保留——帧级同步只支撑 ≤10 Hz 用途,**契约由 dataloader 强制而非文档约定**(⚖ R6 的消费端)。

**大脑消费契约(四买家,全部是既有平面字段的消费视图):**

| 买家 | 读取字段 | 消费速率 | 证书必须保证 | 验收测试(脊柱 CI 预跑) |
|---|---|---|---|---|
| **S2(VLM,7–10 Hz)** | RGB 降采样 2–10 Hz、音频旁白、VLM hindsight 语言标注、多样性元数据、操作员 ID | ≤10 Hz;小时×多样性是主轴 | 同步 10 ms 级即可;隐私模糊完成;语言标注一致性抽检;近重复去重 | 固定基准 co-training 增益曲线(EgoMimic 型);语言标注盲评一致率 ≥ 阈值 |
| **S1(视觉运动,50–200 Hz)** | EEF 位姿流(Gen-1 ≥60 Hz recovered / L1 100 Hz measured)、开度、力 1 kSPS、RGB 全帧率、ATE 上界与同步残差 | 60 Hz(Gen-1)→200 Hz(Gen-2,50 vs 200 Hz 消融裁决,[复审 #12](data-scaling-strategy.md)) | per-episode ATE 上界(Gen-1 ≤6 mm)**实测非宣称**;跨模态 <0.5 ms(啁啾)或显式帧级降标;无插值伪影(频谱检查);标签率出处 | 微调 π0/GR00T 级策略测成功率增量;配对检验 N≥50、盲评(2602.09722 协议) |
| **S0(反射,0.5–1 kHz)+ RL 修正** | R1 总线镜像 1 kHz(measured 金标签)、干预 flag、结果标签、力/振动瞬态(Gen-2 接触麦 8–20 kHz) | 1 kHz 流;干预事件异步 | 总线时戳硬件来源(<100 µs 域);干预 flag 对齐 <1 帧;结果标签完备率 100%;力标定在有效期 | RECAP 式优势估计跑通(修正段可分离);sim 接触模型系统辨识残差下降 |
| **世界模型买家(AMI/Cosmos/1X 类)** | **不剪切长片段**、度量深度、帧级 ego-pose + 内参、同场景多结局分支(接 R 系结果标签)、物理密集事件段 | ≥分钟级整段消费 | **ego-pose ATE 证书 = 动作条件化保真度证书**([rethink §4.3](lecun-worldmodels-rethink.md));深度度量尺度标定;时间轴无剪切声明 | V-JEPA-2-AC 型动作条件化探针,held-out rollout 一致性;ATE 证书对锚板审计抽检复核 |

**契约闭环处:** S0 行的干预/结果标签正是流入 P3 的修正流;世界模型行的失败分支正是 P4 三分类留下的"任务失败片"——四个买家契约没有一条要求脊柱之外的新机制。这是"一台机器"的最终检验:任何新买家出现时,先问其验收测试能否由现有证书字段预跑;能,则是新 SKU;不能,则是对某平面不变量的修订提案,走门禁流程,不走补丁。

**验收测试 harness(CI 作业,买家看到的数字与 CI 产出同一行):** 夜间 job,8× L40S:(1) pin 基线策略(π0-small / GR00T-N1-2B 类)+ 固定基准 spine-bench-v1(仿真 + 3 台自营真机回归位);(2) 对照=基线配比,处理=+候选批,各微调 3 seed;(3) N≥50 paired rollout,盲评走 Grouped Blind Ensemble 协议(arXiv 2602.09722),报告 co_train_delta_pp ± CI;(4) delta 写回该批全部证书 `assay` 字段;负增量 → 批次挂 `negative_transfer_risk` 并触发混合配比建议再计算。

**RLDS 导出映射(一键导出器):** `videos/*.mp4`→`steps/observation/image`;`observation.state`→`steps/observation/state`;`action`→`steps/action`;`data_hf.force_n/taxel`(帧窗聚合)→`steps/observation/force`(原生率存 `hf/` 附表);`tasks.jsonl`+hindsight→`steps/language_instruction`;`intervention_flag/outcome`→`steps/is_intervention`+`episode_metadata/outcome`;`qc/*.cert.json` 全文→`episode_metadata/spine_cert`(签名原样携带,RLDS 侧仍可验签)。

## 8. Gen-2 传感头模组板级方案 (设计目标)

### 8.1 板卡架构(采集变体 = 机器人头/腕变体,同一 PCB)

- **相机:** 2× onsemi AR0234CSSM(2.3 MP 全局快门,~$40/颗 @1k (unverified)),各走 2-lane MIPI CSI-2 FPC;M12 镜座刚性铝梁,**基线 100 mm**,155° 鱼眼(Evetar 级 M12,~$25/只 (unverified));梁与 SoM 热隔离,标定后内外参哈希入证书。
- **硬件触发树(时间戳岛的物理形态):** STM32H743(~$8)TIM 输出 60 Hz FSIN 同打两颗 AR0234 帧同步脚;**同一 FSIN 脉冲接 ICM-42688-P 的 FSYNC 引脚**——快门事件以带内标记写进 IMU 数据流,对齐由构造保证;ICM-42688-P 走 **CLKIN 外部时钟**(32.768 kHz,STM32 晶振分频),整板单晶振域,2 kHz ODR,INT1 硬中断打戳。STM32 输入捕获 @240 MHz(4.2 ns tick)记录 FSIN 沿,快门中点 = FSIN + 曝光/2(寄存器回读)→ 时序预算 <10 µs 各分项落位。
- **计算双源(⚖ 整合裁决 R5):** 原架构"pin 兼容载板温备"落地为 **mezzanine + 双适配板**——单载板直落两颗异构 SoC 封装不现实。载板定义自有 mezzanine 标准:2× Hirose DF40 100-pin,承载 4-lane×2 MIPI CSI-2、PCIe Gen3 ×2、USB 3.0、SGMII、SPI/I²C/UART、12 GPIO(含触发域专线)、5 V 主轨。主选 D-Robotics RDK S100(¥2,799 (unverified),80 TOPS BPU + 4× Cortex-R52+ MCU 核)与温备 Quectel SP895BD-AP(Dragonwing Q-8750,80 TOPS)各配一块薄适配板(<$40),SoC 专属 pinmux/DDR/PMIC 全部圈禁在适配板内,载板零改;季度冒烟 = 换适配板跑月 11 门禁全集,切换承诺 180 天([复审 #15](data-scaling-strategy.md),90 天神话已否)——适配板方案反而使 180 天承诺更可信。锁步 R52 只做时间戳岛与触发树监督;Quectel 侧无锁步核时由 STM32H7 全权承担时间戳岛(架构上 STM32 本就是权威源,SoM 降级不破公理)。
- **力/触觉/声学:** 六轴 F/T(Landot 量产件,¥2–4k (unverified))走 CAN-FD 1 kHz(STM32 FDCAN 帧到达硬时戳);触觉垫专用 SPI @10 MHz,每垫独立 CS,100+ taxel×12-bit×500 Hz ≈ 0.6 Mbps/垫,扫描帧同步挂触发树;接触麦:压电换能器 → 电荷放大(OPA1652)→ TLV320ADC3140(~$6)48 kHz I²S,**主时钟由 STM32 域分频**——8–20 kHz 接触瞬态与力流同域同戳。
- **功耗/热:** SoM 8–12 W(BPU 占空比控制:VIO 仅在线 QC)+ 传感头 ~2 W + 杂项 2 W = **10–14 W**;镁铝中框传导,采集变体皮温 ≤43 ℃ 被动、>45 ℃ 微型风扇;99 Wh → 7.4 h ✓。
- **变体 BOM 差异(<5%):** 采集变体加 USB-PD 诱骗(CH224K,$0.3)、电池仓/绑带座、状态 LED;机器人变体删电池件、加 48 V→12 V 隔离砖(¥60 级)+ M12 连接器 + 三防漆。其余 100% 共板共产线——"卖进机器人的每颗头都是采集器"由 BOM 表兑现。

### 8.2 Bring-up 计划(月 6–11;相机板 4–6 个月 bring-up 在关键路径上)

| 月 | 里程碑 |
|---|---|
| M6 | 原理图冻结 + mezzanine 规格 v1.0;**并行启动最长项:AR0234 驱动/ISP tuning 直接在 RDK S100 EVK 上做,不等载板**;长交期器件下单 |
| M7 | 载板 Rev A 投板;STM32 固件(触发树+时戳岛)在 Nucleo 台架先行验证 |
| M8 | Rev A 回板:电源树、STM32、IMU CLKIN/FSYNC 链路点亮;单相机出图 |
| M9 | 双目 + VIO 移植(在线 QC 档);触发树全链路示波器验证;F/T、触觉、接触麦 AFE 联调 |
| M10 | Rev B(勘误)投板+回板;**Quectel 适配板冒烟**;热/振动预测试;ISP tuning 收敛判据:低照 SNR 与 AE 收敛达标 |
| M11 | 台架门禁(下),n=5 台整机 |

风险缓冲:ISP tuning 若 M10 未收敛,门禁只考时序与 ATE(tuning 参数可 OTA),但**任何一项时序失败即 Rev C,整代顺延 6 周并上报门禁委员会**——不许口头豁免。

### 8.3 月 11 台架门禁测试程序

1. **时序(公理项):** LED 闪光板 + 10 kHz 光电二极管基准,双相机快门中点/IMU/力/接触麦五路对齐,10–40 ℃ 温循 1 h,**全程 <10 µs 判过**;触发线拔除 → 设备必须自报下线(无戳即无数据)。
2. **精度:** 传感头装机械臂法兰(TCP 重复精度 ±0.05 mm 作真值),标准轨迹集(5 min×10 条,含 1–2 m/s 快动段),离线平滑输出 **台架 ATE ≤2 mm 且快动段 ≤3 mm** 判过;同步录 GELLO 审计臂交叉验证。
3. **啁啾对拍(承接月 1 遗留):** n=100 会话啁啾 vs 硬触发真值,给出该型号管线方差终值,决定 Gen-2 是否保留声学通道(预期废止——硬触发在手)。
4. **功耗/热浸:** 30 ℃ 环境 6 h 连录,皮温、掉帧率、时戳漂移三项达标;Quectel 适配板重复第 1 项(缩编 30 min)。

未过 → 按路线图预案:L 系扩产替位,W 系退守 6 mm 预训练定价,Rev C 不追加承诺日期。

## 9. 失效遏制与合规

### 9.1 失效遏制(按平面)

| 平面 | 断点 | 爆炸半径 | 检测 | 降级模式 + 第二源 |
|---|---|---|---|---|
| P1 | GoPro Hero9 停产(现状,走翻新);Hero13+Max Lens Mod 2.0 兼容**未验证** | W1/W1e 整线供应 | 供应链月检;翻新渠道 ≥150 台/月为 PVT 门禁项 | Hero13 验证挂日期门;Gen-2 自研传感头本身是 GoPro 退出计划 |
| P1 | DYNAMIXEL XL330 断供 | L1 | 同上 | 国产总线舵机(Feetech STS3215 类,~$16 (unverified))月 6 过台架 |
| P1 | RDK S100 断供 | Gen-2 全线 | 同上 | Quectel SP895BD-AP 温备:mezzanine 适配板(⚖ R5)+ 季度冒烟,切换承诺 180 天 |
| P1 | D405 断供 / Prophesee 单源 | L1/R1;Gen-3 事件相机 | 同上 | Orbbec Gemini 335 类替代 (unverified);无事件相机架构必须仍达 2.5mm |
| P2 | 啁啾方差超限 | 单型号 SLA 主张 | 月 1 台架 + 在线啁啾丢失计数 + 遥测 P95 自动工单 | LED 转正为主通道,啁啾降为漂移监测;时钟公理不降级 |
| P2 | 单设备晶振异常/双 IMU 残差 >2 cm/30 s | 单 episode | 端上漂移告警(振动提醒)+ 坞站权威复算 | 自动重采;ATE 自测 >8 mm 判下线 |
| P3 | 坞站积压(SLAM 吞吐)/ 转码节点宕机 | 单站点 24–72 h | 队列深度遥测 | 1:3 配比 + 72 h 缓存 + 磁盘摆渡;RK3588 HEVC 硬编降级(⚖ R1);raw 不可变可无限重放 |
| P4 | 证书通胀(标定漂移未被抓) | 商誉级(买家跑 500 h 化验砍价) | 每 operator 每周锚板密集审计回合;R1 同场对拍基准 | 年度高校第三方审计;训练价值化验层入证书([复审 #13](data-scaling-strategy.md));Merkle 透明日志防静默重发 |
| P4 | QC 误杀下个范式要买的数据 | 产品线级 | KPI = 不可用传感率,非废片率 | 三分类:传感废真删 / 任务失败留标 / 成功;失败-恢复 shard 单列 SKU |
| P5 | 负迁移(2mm 钢印盖在次优轨迹上) | 买家训练结果 | per-shard 固定基准 co-training 增量(CI harness) | 本体对齐元数据 + 混合配比建议随证书交付 |
| P5 | 客户拒供修正数据(逆向选择) | Gen-3 混合体 45% | 月 9 GTM 里程碑 | R 系白标既定:数据归客户,我方收时钟/QC/证书 SaaS + 传感 BOM 位;R 归零 B 计划配比预置 |

### 9.2 隐私、主权、同意

- **模糊管线落位:** Gen-1 在**坞站**——RK3588 NPU(3 核 6 TOPS)跑 YOLOv8-face 级检测 + 屏幕/文档检测,转码前烧入;模糊前 raw 以 per-episode 密钥加密落盘,密钥中国主体托管,30 天留存(仅复检)后销毁,`privacy.blur_stage="dock"` 入证书。Gen-2 **上模组**——BPU 跑蒸馏分割,人脸/屏幕在编码前抹除,未模糊像素不出模组(对应 [端侧大脑](on-device-brain.md) C1 远期"密钥+人脸模糊固化"块),`blur_stage="module"`。
- **数据主权分区([复审 #17](data-scaling-strategy.md)):** 双脊柱同格式——中国采集 → 境内云(证书云同区),买家为国内训练场/政府侧;美国买家从**独立辖区认证主体**购买 (a) 美国辖区操作员采集的数据、(b) 证书/化验/格式授权、(c) 采集器械 SKU——**中国 raw 不出境,PIPL/数据出境评估不触发**;证书格式与公钥全球同一,这正是"卖尺子不卖数据"的合规形态。R 系白标天然合规:数据本就归客户、留在客户辖区。
- **同意与支付:** App 内逐任务电子同意书(采集范围、模糊保证、撤回权:凭 episode_id 可要求删除且透明日志留撤销痕);入户任务附第三人告知卡;支付=证书通过事件驱动;中国走支付宝/微信企业付款周结,美国操作员走 Stripe Connect + 1099。操作员 ID 全链路只以加盐哈希出现。

## 10. 总排期(整合 EVT/DVT/PVT,门禁映射)

| 月 | W 系 | L1 | R1 | 坞站/脊柱 | Gen-2 (设计目标) | 路线图门禁 |
|---|---|---|---|---|---|---|
| **1** | EVT:W1 ×5、W1e ×3;**啁啾台架 100 会话对拍**;打戳纪律逻辑分析仪验证;力链 0.5 N;W1e 35 ℃ 6 h 热测;端到端 1 条合法 shard | 单臂 7 关节 100 Hz;触点辨识 <1.5 mm | tap 板 A 样:CAN listen-only 真实总线 48 h 零 ACK/零错误帧(示波器取证);EtherCAT 只收 tap 不破 DC 测距 | 单坞 SLAM 队列跑通;啁啾互相关代码即台架测量仪 | — | **月 1 门禁:啁啾方差 ≤200 µs → 进 SLA;否则 LED 转正、SLA 改帧级,判决冻结不再争论(全案最便宜实验,P2 第一门禁)** |
| **2–3** | DVT:W1 ×25、W1e ×10;试点站点 ≥2 周,**有效吞吐 ≥60–70 demos/h(v1.1 口径)**;传感废 ≤20% 逐周降;漂移告警误报 <1 次/h;OTA 全链;跌落 1 m ×6 面;BOM 冻结 | (EVT 续)FK 重复性 <1 mm | 客户总线零扰动书面报告 | **月 2 门禁:转码节点 8.6 h/天实测(⚖ R1 的验证项)**;shard/证书 schema 冻结 | — | 月 2 坞站吞吐实测 |
| **3–5** | (DVT 完成→PVT 准备) | DVT:双臂 + D405 对;归位梳/锚板套件定型;35 demos/h 疲劳实测;审计会话首份 per-session ATE 报告 | DVT:密码学边界端到端(客户 KMS 假想敌演练:我方全权限下无法读原始盘);干预事件↔总线帧 <1 ms 实测;热测壳温 | 1:3 满载 72 h 浸泡;单坞 3 台 ×7 天零积压;15–20% 传感废剔除流水打通;ingest 六段全通 | — | — |
| **4** | PVT:W1 ×100、W1e ×40;EOL 节拍 ≤12 min 实测;直通率 ≥90%;啁啾方差批间 σ 稳定;**翻新 Hero9 ≥150 台/月渠道确认,否则触发 Hero13 验证日期门** | — | — | — | — | — |
| **5–6** | Ramp 300 台/月,累计 ~600 台,支撑 Gen-1 舰队 1,600 台爬坡;首个完整 90 天力标定周期;首批带证书 shard 过买家 `load_dataset` 即训 | **交叉验证环(DVT 联合出口):** L1 遥操跟随臂,R1 侦听总线(1 kHz 黄金真值),W1 末端同录;**L1 FK vs R1 FK <2 mm** 认证 L1 为便携审计仪;随后 L1 野外审计 W1 → recovered ATE 实测。溯源链 R1→L1→W1 闭合,证书"实测非宣称"才有根 | 同左 | 同左 | M6:原理图冻结;**AR0234 驱动/ISP tuning 在 EVK 上并行启动(最长项)** | 月 6:Feetech 替代舵机过台架 |
| **6–9** | (量产运行) | PVT:3 套量产,EOL 三项全过 | PVT:5 盒装机 2 家客户;PTP offset 遥测入库 | 首站点 10 台满配 | M7–M9:载板 Rev A 投板/回板/点亮;VIO 移植;触发树示波器验证 | **月 9 门禁:ATE ≤2 mm 台架 / ≤4 mm 野外中位(测量基础设施=交叉验证环);未过 → L1 扩产替位自动生效**;月 9 GTM:R 系修正数据意向 |
| **10–11** | — | — | — | — | M10:Rev B + Quectel 适配板冒烟;M11:**台架门禁四项**(时序 <10 µs 公理项 / ATE ≤2 mm / 啁啾终验 / 热浸) | **月 11 门禁:任何时序项失败即 Rev C,整代顺延 6 周上报门禁委员会** |

**关键路径:** (1) 90 天内——**月 1 啁啾台架**是一切 sub-ms SLA 主张的闸门(判决冻结机制防止反复争论);(2) 全程——**Gen-2 相机板 bring-up(AR0234 驱动/ISP tuning,4–6 个月)**,故 M6 起在 RDK S100 EVK 上与载板并行,这是唯一无既定退路只能靠时间的项(时序失败=Rev C 顺延 6 周)。Gen-3 舰队 gPTP 与 C1 时间戳岛全部标 (设计目标) 且挂"≥50 万片跨 ≥2 家 top-10 本体厂意向"硬门禁——**本页架构在纯 COTS 路径下完整成立**。

---
**整合裁决索引(子系统对总架构的全部修正,均为工程落地而非立场变更):** R1 转码职责移至站点 NVENC 节点(RK3588 无 AV1 硬编,HEVC 硬编为命名退路,证书 codec 字段记实);R2 入坞时间按 30 MB/s 持续吞吐改口径 ~1.6 h(1:3 配比算术不变);R3 端上双 IMU 告警用两颗 MCU 侧异厂家 IMU,GoPro↔MCU 权威残差坞站离线复算(判据不变);R4 R1 相机 USB-only(D405 无 GMSL 变体);R5 Gen-2 双源落地为 mezzanine+双适配板(单载板直落双 SoC 不现实,180 天切换承诺反而更可信);R6 啁啾 SLA 由证书 schema 与 dataloader 双端强制(`bench_cert_id` 为 null 时 `residual_class` 只能填 frame)。

## Sources
- [data-engine-roadmap](data-engine-roadmap.md) — 三代路线、门禁体系、BOM 基线(本页的上游定案)
- [data-scaling-strategy](data-scaling-strategy.md) — 复审 #5/#11/#12/#13/#15/#17/#18:分层上行、三分类、消融裁决、化验层、180 天切换、主权分区、1 带 3
- [lecun-worldmodels-rethink](lecun-worldmodels-rethink.md) — §4.3 ego-pose ATE 证书 = 动作条件化保真度证书;世界模型买家契约依据
- [on-device-brain](on-device-brain.md) — S2/S1/S0 分层消费速率;C1 时间戳岛与模糊固化远期块
- [data-collection-devices](data-collection-devices.md) — UMI/GELLO/DROID 器件谱系与三家族对比矩阵(W1/L1 选型出处)
- https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/ — XL330 规格/价格、Fast Sync Read、Return Delay
- https://wuphilipp.github.io/gello_site — GELLO $363/臂、运动学孪生与重力补偿惯例
- https://www.intelrealsense.com/depth-camera-d405/ — D405 $272、无 inter-cam sync 引脚、USB-only
- https://developer.nvidia.com/embedded/jetson-orin-nano-super-developer-kit — Orin Nano Super 定价、无 NVENC
- https://www.ti.com/product/ISO1042 — 隔离 CAN-FD 收发器;Listen-Only 不可扰论证
- http://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html — RK3588 VPU:AV1 仅解码(⚖ R1 的依据)
- https://umi-gripper.github.io — 锚板/CharUco 审计仪式与 ATE 方法学、隐式立体反射镜构型
