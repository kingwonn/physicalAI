# HANDOFF — 本地会话交接文档

写给在用户 Mac 上启动的 Claude Code 会话。云端会话（2026-07-12，做了 blog-zh/001 与方法论）
受网络白名单限制无法转录音频、无法读本地目录；你在本地没有这些限制。读完本页 +
[README.md](README.md) + [methodology.md](methodology.md) 即可接手。

## 你所在系统的全景

- 本仓库 = LLM-wiki（协议见根目录 CLAUDE.md；注意默认分支是 **main**，CLAUDE.md 写的
  master 是笔误）。wiki 正文有对抗核查纪律：**新事实先进 `wiki/_meta/queue.md`，
  不直接改 wiki 页**。
- `blog-zh/` = 中文博客层：一份播客源材料 → 一篇归档+分析（编号 S-00x 对齐）。
  已完成 001（晚点聊 166 许华哲，基于文字版重建，**非逐字稿**）。
- 配套可视化档案站（技术树/产业地图）：kingwonn/ycfs 仓库 `embodied-ai/` 目录，
  分支 `claude/embodied-ai-tech-history-hxx4ew`；artifact 903d6ad2-2090-4e2f-845a-68c982c0631a。

## 本地独有的资产：hermes 转录目录

`/Users/ayr/ai/physicalAI-hermes/`（另一个本地 agent 维护的转录厂）：
- `raw/transcripts/xiaoyuzhou/{filename}.md` — 原始转录
- `processed/transcripts/xiaoyuzhou-cleaned/{filename}-cleaned.md` — LLM 清洗版
- 已有 ~15 集（许华哲 ×5、王鹤 106 学术史、高继扬 ×2、谢晨 ×2、谭捷 DeepMind、
  何小鹏 Iron、谢赛宁世界模型、王乃岩等）

云端会话对该方案的评审结论（详见会话记录，要点）：转录厂方向正确、raw/cleaned 分离正确、
选集好；缺稳定 ID 与溯源 manifest、cleaned 是黑箱（LLM 清洗可能静默改写原话）、
ASR 专有名词错误待归一化、diarization/时间戳状态未知。

## 你的任务清单（按序）

1. **审计**：抽 2-3 集做 raw↔cleaned diff，判断清洗是否改写内容（去语气词=安全，
   改写句子=危险），给出清洗可信度结论。
2. **manifest**：建 `sources/manifest.json`——逐集补：稳定 ID（沿用 S-00x）、播客名、
   期号、标题、嘉宾、发布日期、小宇宙 URL（ObjectId 前 8 hex = unix 时间戳，可反查日期）、
   raw/cleaned 路径、转录与清洗的模型及日期。
3. **归一化**：用 `wiki/glossary.md` + 公司页做词典修 ASR 专名错误，留修改日志，不静默改。
4. **回补 001**：用 ep-166 逐字稿把 blog-zh/001 的 paraphrase 升级为原文引用，
   校正时间轴后半段两处存疑对齐，`confidence` 可视情况升级。
5. **批量归档 002-016**：建议顺序——王鹤 106（学术史）→ 高继扬两集 → 谢晨两集 →
   谢赛宁 → 何小鹏 → 其余。每篇照 methodology.md 流水线：归档 + 分析 + queue 线索 +
   更新 README 索引 + 同步 ycfs 档案站（每处修订标 〔S-NNN〕）。
6. **新节目的常态循环**：hermes 转录 → 你归档 → push。音频你也可以自己拉
   （RSS/媒体 CDN 本地无封锁）+ 本地 whisper，不必依赖 hermes。

## 纪律（不可妥协的三条）

- 观点归属讲者，不写成事实；单一来源标 (unverified)；不确定性外置到「核查状态」。
- wiki 正文只能经 queue → verify 进入，博客不越权直改。
- 提交风格：本目录用 `blog-zh: ...`，一次任务一个 commit，推 main。
