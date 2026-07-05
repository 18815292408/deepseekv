# Cursorhero 外链嵌入 deepseekv 站 — 设计文档

**日期**：2026-07-05
**范围**：在已上线的 deepseekv 站（deepseek32-landing.html + deepseek-v4.html）加入指向 https://cursorhero.com/ 的外链
**目标**：按"分层原则"（内容嵌入 > 横幅海报 > footer 兜底）获得高质量外链，同时不破坏站内调性

---

## 1. 背景与原则

deepseekv 站 = DeepSeek V3.2/V4 模型营销页（已上线 deepseekv.vercel.app / deepseekv.pro），受众是 AI 从业者和潜在开发者。
Cursorhero = AI 生成自定义鼠标光标的 SaaS（Next.js + React + TS），面向桌面美化用户 / 极客。

**两站相关性**：弱关联——同属 AI 圈但场景不重叠（模型层 vs 应用层）。

**deepseekv 流量判断**：中低（独立 AI 模型营销站，未做付费推广），未达到"挂横幅海报导流"的流量门槛。

**结论**：采用「内容里自然嵌入（主力）+ footer 全站兜底」两层结构，**不上横幅海报**。

---

## 2. 实施点（3 处）

### 改动 1 — 内容里自然嵌入（⭐ 主力层）

**文件**：`deepseek32-landing.html`
**位置**：FAQ 区域，"普通用户有哪些具体使用场景？"问答的答案段（约 1178–1181 行）
**形式**：在"生活与娱乐"场景列表后自然延伸出"桌面个性化"子场景，链接到 Cursorhero
**属性**：`data-zh` / `data-en` 双语字段同步；链接 `target="_blank"` `rel="nofollow noopener"`（外链标准姿势）；`nofollow` 是因为 deepseekv 是营销站、不是行业权威内容站，避免给新站传递不必要的 PageRank 信号（实际 SEO 价值靠 anchor 文本和上下文传递，nofollow 不影响爬取和权重流入的间接效果）

**原段落（zh）**：
> 学习与知识：解题辅导、文书写作润色、知识问答。工作与效率：编程辅助、文档分析总结、头脑风暴。生活与娱乐：旅行规划、创意写作、日常解惑。支持 128K 超长上下文，可处理整本书、长篇报告...

**新增段落（zh）**：
> 桌面个性化：AI 一句话生成专属鼠标光标，支持赛博朋克、水彩、像素风等风格，Windows 可直接安装试用——[Cursorhero](https://cursorhero.com)

**英文版本**：
> Desktop personalization: Generate custom mouse cursors with AI — cyberpunk, watercolor, pixel art styles — installable directly on Windows. Try [Cursorhero](https://cursorhero.com)

### 改动 2 — 首页友情链接 section 加卡片（兜底层）

**文件**：`deepseek32-landing.html`
**位置**：`#friendlinks` section，第 1419–1434 行 `.friendlinks-container`
**形式**：在现有 2 张卡片（V4 专题、订婚摄影）后面追加第 3 张卡片，复用现有样式
**属性**：双语；`target="_blank"` `rel="nofollow noopener"`；icon 用 `ri-cursor-line`（remixicon 已有此 icon）；文案"AI 鼠标光标" / "AI Cursor Generator"

### 改动 3 — V4 专题页 footer 加链接（全站兜底层）

**文件**：`deepseek-v4.html`
**位置**：footer `.links` 区域，约 863–868 行
**形式**：在现有 4 条链接（首页 / DeepSeek 3.2 / 官网 / GitHub）末尾追加 Cursorhero 链接
**属性**：双语 `data-zh` / `data-en`；`target="_blank"` `rel="nofollow noopener"`

---

## 3. 明确不做的事

- ❌ **不上首页横幅海报**：deepseekv 流量没起来，banner 会破坏页面调性、显得 hard-sell
- ❌ **不在 V4 页面正文里嵌入**：V4 内容全是技术参数（128K、DSA、Speciale），跟 cursor 主题没自然接点，硬塞伤 SEO 体验
- ❌ **不改友情链接现有 2 条**：V4 专题和 engagement-photos 保持原样
- ❌ **不在 V4 加 friendlinks section**：V4 主题性强（V4 技术参数），加友情链接 section 反而稀释主题
- ❌ **不用 `dofollow`**：deepseekv 是营销站不是权威内容站，`nofollow` 避免给新站带来 PageRank 信号过载；SEO 价值靠 anchor 文本和上下文传递足够

---

## 4. 验收标准

- 三处改动在 `deepseek32-landing.html` 和 `deepseek-v4.html` 落档
- 中英文切换脚本（localStorage 控制的 currentLanguage 切换）下三处文案都正确显示
- 三处链接均指向 https://cursorhero.com/，`target="_blank"` `rel="nofollow noopener"` 正确
- 本地浏览器或 curl 渲染检查通过
- 现有友情链接 2 条、FAQ 其他问答、其他 footer 链接、V4 内容不被破坏
- 不引入新依赖、不改 CSS、不动 JS

---

## 5. 风险与回滚

- 风险：嵌入文案破坏 FAQ 阅读体验 → 回滚单个 `<p>` 改动即可，影响面小
- 风险：friendlinks 卡片太多导致布局错位 → 现有样式已用 flex-wrap，移动端断点已设，回滚单卡即可
- 风险：V4 footer 链接过多影响美观 → 改动只在原 `<a>` 列表追加一条，无布局变更

如出现未预期问题，三处改动可独立 revert，互不影响。