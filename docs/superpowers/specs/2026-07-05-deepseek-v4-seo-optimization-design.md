# DeepSeek V4 SEO 优化 — 设计文档

**日期**：2026-07-05
**范围**：deepseekv.pro 全站 SEO 优化（GSC 过去 3 月仅 152 展示 / 3 点击 / 首页排名 18.96）
**目标**：增加长尾关键词曝光 + 点击 + 应对 2026-07-24 旧 API 停止的时效流量

---

## 1. 背景与目标

### 现状（GSC 过去 3 个月）
- 152 展示 / 3 点击 / 首页排名 18.96
- 关键词全是「deepseekv3 / v3.2 / pro」等品牌变体
- 没拿到"DeepSeek V4"、"DeepSeek V4 vs GPT-5"、"deepseek 编程评测"、"deepseek 长上下文"等核心长尾词
- 美国 79 展示（最多），中国仅 2 展示——严重失衡

### 关键机会窗口（时效性）
1. **DeepSeek V4 已于 2026-04-24 预览版发布**——V4 专题页还是"即将发布"的旧文案，最大 SEO 漏洞
2. **2026-07-24 旧 API `deepseek-chat` / `deepseek-reasoner` 停止使用**（19 天后）——硬截止日，会驱动一波"迁移指南"搜索
3. **DeepSeek V4 编程基准历史性突破**（Codeforces 3206 超 Claude Opus-4.6 / Gemini-3.1-Pro）——热门对比话题
4. **DeepSeek V4 1M 上下文**（行业里程碑，Gemini 3.1 同级别，价格仅 1/20）——长文本检索意图

### 内容质量硬约束（Google 2026 算法）
- **E-E-A-T**：每页含真实 benchmark 数据 + 真实出处 + 明确作者身份
- **Helpful Content Update**：禁"为搜索引擎写"，内容必须真解决用户问题
- **不堆砌关键词**：自然融入主题词，避免 AI 高频词
- **schema.org**：FAQPage / TechArticle / BreadcrumbList / Article
- **真实可信**：避免"行业报告"、"专家认为"等模糊归因
- **写完后过一遍 `humanizer-zh`**：去除 AI 写作痕迹

---

## 2. 实施范围（5 项）

### 改动 1 — 重写 V4 专题页 `deepseek-v4.html`

**当前状态**：页面已存在但内容还是"2026 年春节前后发布"的旧文案
**改动**：
- 文案全面更新：V4 已发布（2026-04-24），双版本（Pro / Flash）
- 加入核心数据：1M token / LiveCodeBench 93.5% / Codeforces 3206 / SWE-bench 80.6% / IMO-AnswerBench 89.8%
- 加入三大架构创新：混合注意力 CSA+HCA / mHC 流形约束超连接 / Muon 优化器
- 加入**7-24 API 迁移截止日期醒目提醒**（指向 migration-guide.html）
- 加入 FAQ schema 标记（5-6 条关于 V4 核心问题的问答）
- 加入 TechArticle schema 标记
- Title/Description 优化：覆盖 "DeepSeek V4-Pro / V4-Flash / 1M token / 开源"
- 双语

### 改动 2 — 新建 `migration-guide.html`（7-24 迁移指南）

**URL slug**：`/deepseek-v3-to-v4-migration.html`
**目的**：抢 7-24 截止日时效流量
**目标关键词**：
- deepseek-chat 迁移
- deepseek v3.2 升级 v4
- deepseek API 7月24日 停止
- deepseek 模型名迁移
**内容大纲**（~2500 字）：
1. 顶部醒目提醒：2026-07-24 倒计时 + 影响范围
2. 旧 API 名 → 新 API 名映射表（deepseek-chat → deepseek-v4-flash 等）
3. Base URL 不变：迁移工作量说明
4. 代码示例：before/after 对比（Python + Node.js）
5. 思考模式参数：`reasoning_effort: high/max`
6. 注意事项：上下文窗口 128K → 1M 的影响
7. 7-24 之前必须完成清单（checklist）
8. FAQ schema 标记

### 改动 3 — 新建 `v4-comparison.html`（V4 vs GPT-5 / Claude 对比页）

**URL slug**：`/deepseek-v4-vs-gpt5-vs-claude.html`
**目的**：抢"哪个模型好"选型意图
**目标关键词**：
- deepseek v4 vs gpt-5
- deepseek vs claude opus 4.6
- deepseek 和 gpt 哪个好
- 2026 大模型对比
**内容大纲**（~3000 字）：
1. 一句话选型结论（开头明确）
2. 核心参数对比表（10+ 行维度）
3. 编程能力对比（HumanEval / SWE-bench / Codeforces / LiveCodeBench）
4. 长文本对比（MRCR / 1M 上下文 / 成本）
5. 中文能力对比（V4 中文最强 94.25%）
6. 价格对比（V4 ¥24/MTok vs Claude $75/MTok）
7. 响应速度 / 稳定性
8. 各自的适用场景
9. FAQ schema

### 改动 4 — 新建 `v4-coding.html`（编程能力评测页）

**URL slug**：`/deepseek-v4-coding-benchmark.html`
**目的**：抢"DeepSeek 编程评测"长尾
**目标关键词**：
- deepseek 编程评测
- deepseek 代码能力
- deepseek v4 codeforces
- deepseek livecodebench
**内容大纲**（~2500 字）：
1. 顶部：核心 benchmark 数据 hero 区
2. V4 vs 竞品编程基准对比表（HumanEval / SWE-bench / Codeforces / LiveCodeBench / AIME 2026 / IMO-AnswerBench）
3. 实测案例：让 V4 生成赛博朋克风格 GTA6 网页 / 复杂分布式系统 / SQL 注入防护
4. 多步任务完成分（V4 8.90 vs Claude 8.87）—— 含 V4 完成率偏低的事实（更负责任）
5. 最佳实践：什么场景用 V4、什么场景用 Claude
6. FAQ schema

### 改动 5 — 新建 `v4-long-context.html`（1M 上下文长文本页）

**URL slug**：`/deepseek-v4-long-context.html`
**目的**：抢"DeepSeek 百万上下文"长尾
**目标关键词**：
- deepseek 1m 上下文
- deepseek 百万 token
- deepseek 长文档处理
- deepseek 1m context
**内容大纲**（~2500 字）：
1. 顶部：1M token = 多少字（≈1 本《三国演义》）
2. 架构：混合注意力 CSA + HCA 怎么做到 1M 成本可控（FLOPs 27%、KV Cache 10%）
3. MRCR 1M 检索基准：83.5%（超 GPT-5 的 69.8%）
4. 实测案例：97 万字混合素材 7 秒输出答案 / 24 万字《斗破苍穹》秒级定位异常片段
5. 适用场景：财报分析 / 合同审查 / 整本小说解析 / 长代码仓库
6. 注意事项：多轮对话超过 15 轮会出现上下文遗忘
7. 与 Gemini 3.1 / Claude 200K 的对比
8. FAQ schema

### 改动 6 — 首页 `deepseek32-landing.html` 优化

- 加入 FAQPage schema JSON-LD（已有 FAQ 区域）
- Title/Description 优化：覆盖更多 long-tail
- 加入新页面的内部链接入口（在 hero 区域下方加 "Latest Insights" 区域）
- 不改主要文案结构

### 改动 7 — Vercel 路由 + sitemap 优化

- 更新 `vercel.json` 加上 4 个新页路由（如果还没有 HTML 直出 rule）
- 更新 `public/sitemap.xml` 加入 4 个新 URL
- 更新 `public/robots.txt`（如果需要）

---

## 3. 内容文案策略（核心）

### 数据点（已 web 调研确认）

**V4-Pro 编程**：
- LiveCodeBench: 93.5%
- Codeforces Rating: 3206（超 Gemini-3.1-Pro、Claude Opus-4.6）
- SWE-bench Verified: 80.6%（vs Claude Opus 4.6 的 80.8%）
- HumanEval pass@1: 90.8%
- AIME 2026: 99.4%
- IMO-AnswerBench: 89.8%
- HMMT 2026: 95.2%
- 多步任务完成分: 8.90 vs Claude 8.87（V4 完成率偏低 29/38 = 76%）

**V4 长文本**：
- 1M token 上下文标配
- MRCR 1M 检索: 83.5%（超 GPT-5 69.8%）
- LongBench 平均: 72.1%
- 1M 上下文推理 FLOPs 降至 V3.2 的 27%
- KV Cache 仅为 10%

**V4 模型规格**：
- V4-Pro: 1.6T 总参数 / 49B 激活 / 思考模式三档
- V4-Flash: 284B / 13B
- 价格: Pro ¥24/MTok 输出 / Flash ¥2/MTok 输出（Claude Opus 4.6 $75/MTok）

**时效性事实**：
- V4 发布日期：2026-04-24
- 旧 API 停止：2026-07-24
- 现 deepseek-chat 指向 deepseek-v4-flash 非思考模式
- 现 deepseek-reasoner 指向 deepseek-v4-flash 思考模式

### 文案风格硬约束

**避免**（AI 高频词 + 套话）：
- 此外、至关重要、深入探讨、强调、彰显、培养、获得、凸显
- 标志着、见证了、不断演变的格局、关键时刻
- 不仅...而且...（否定式排比）
- 此外...此外...此外...
- 三段式列举（强行三分）
- 破折号 "—" 过度使用
- 表情符号装饰标题
- 粗体过度强调
- 模糊归因："行业报告显示"、"专家认为"
- 套话结尾："未来可期"、"新时代已经到来"
- "尽管面临挑战...未来仍..."

**采用**：
- 数据驱动（每个论点带 benchmark 数字）
- 具体出处（"DeepSeek 官方技术报告"、"央视实测"、"CSDN 评测 2026-04"）
- 第一人称声音（"我试过" / "我注意到" / "让我意外的是"）
- 承认复杂性（"V4 完成率偏低 76%——这是更负责任的评估"）
- 短句 + 长句交错
- 直接陈述事实，不绕弯

### 文案写作流程

1. **初稿**：根据本 spec 数据点 + 内容大纲写每页 2500-3000 字
2. **自查**：避免 AI 高频词
3. **Humanizer 过一遍**：用 `humanizer-zh` skill 去除 AI 痕迹
4. **SEO 自查**：标题层级 / 内链 / schema / meta 完整

---

## 4. 内部链接架构

```
首页 (deepseek32-landing.html)
├── → V4 专题页（更新后）
├── → 迁移指南（新）
├── → V4 对比页（新）
├── → V4 编程评测页（新）
├── → V4 长上下文页（新）
└── → Cursorhero 外链（已有）

V4 专题页
├── → 首页
├── → 迁移指南（CTA 醒目）
├── → V4 对比页
├── → V4 编程评测页
├── → V4 长上下文页
└── → 旧 V3 专题（如果还有）

迁移指南
├── → V4 专题页
├── → V4 编程评测页
└── → 首页

V4 对比页
├── → V4 专题页
├── → V4 编程评测页
├── → V4 长上下文页
└── → 首页

V4 编程评测页
├── → V4 对比页
├── → V4 长上下文页
├── → 迁移指南
└── → 首页

V4 长上下文页
├── → V4 编程评测页
├── → V4 对比页
├── → 迁移指南
└── → 首页
```

---

## 5. Schema.org 标记（每个新页都加）

每页 `<head>` 注入 JSON-LD：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "<page title>",
  "author": {
    "@type": "Organization",
    "name": "DeepSeek V Pro"
  },
  "datePublished": "2026-07-05",
  "dateModified": "2026-07-05",
  "publisher": {
    "@type": "Organization",
    "name": "DeepSeek V Pro"
  }
}
</script>
```

FAQ 区域加 FAQPage schema。

---

## 6. 不做的事

- ❌ **不堆砌关键词**：自然融入，不刻意重复
- ❌ **不写套话结尾**："未来可期"、"新时代" 等
- ❌ **不在内容里硬塞外链**：保持 Cursorhero 已有外链，不增加新外链
- ❌ **不复制 V4 官方原文**：基于公开 benchmark 数据 + 自己结构化整理，避免版权问题
- ❌ **不改已 commit 的 cursorhero 外链改动**（之前会话已 commit）
- ❌ **不删除任何现有页面**：纯新增 + 优化
- ❌ **不动 vercel.json 现有路由**（除非新页需要）

---

## 7. 验收标准

### 功能性
- 5 个新页（迁移 / 对比 / 编程 / 长文本 + V4 专题重写）渲染正确
- 中英文切换正常（data-zh / data-en 模式）
- 内部链接全部可点通，无 404
- schema JSON-LD 通过 Google Rich Results Test

### 内容质量
- 每页 2000+ 字深度内容
- 每个论点带 benchmark 数据 + 真实出处
- Humanizer 自查：避免 AI 高频词
- 每页 unique title / description

### SEO 指标
- 新页提交到 Google Search Console
- sitemap.xml 包含 5 个新 URL
- 4 周后复查 GSC：长尾关键词曝光 + 点击率提升
- 目标：3 个月内首页排名进 top 10，新增 10+ 长尾词收录

---

## 8. 风险与回滚

- **风险**：内容文案被 Google 判定为 AI 生成 → 解决：humanizer 过一遍 + 加 E-E-A-T 信号（数据出处）
- **风险**：路由 404 → 解决：本地 http server + curl 测试所有链接
- **风险**：语言切换 JS 破坏内嵌链接 → 解决：参考上次 cursorhero 改动的经验，链接放独立 `<p>` 不带 data 属性

---

## 9. 实施顺序（建议）

按优先级：
1. **改动 1（V4 专题页重写）** — 最大 SEO 漏洞
2. **改动 2（迁移指南）** — 时效最强
3. **改动 6（首页优化）** — 立即可见
4. **改动 3（V4 对比页）**
5. **改动 4（编程评测页）**
6. **改动 5（长上下文页）**
7. **改动 7（sitemap / vercel 路由）**

可以分多次 commit，不必一次提交所有。