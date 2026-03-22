---
name: kids-math-interactive
description: “为 5-10 岁儿童创建互动数学学习网站。当用户想要构建教育类数学 Web 应用、互动学习页面、数学测验游戏或任何适合儿童的基于 HTML 的数学教学工具时，请使用此技能。触发展现包括：请求”数学学习网站”、”儿童互动数学”、”数学测验游戏”、”儿童教育 Web 应用”、”数学练习网站”，或任何提到为儿童构建 Web 端数学学习体验的场景。当用户提供数学知识点、练习题或课程内容并希望将其转化为互动 Web 体验时，也会触发。此技能处理全流程：深色极光主题、语音合成集成、引导式示例讲解、互动测验以及循序渐进的揭示动画。即使由于数学内容较多，用户只说”把这个做成有趣的教学页面”，也要使用此技能。”
---

# 少儿数学互动 (Kids Math Interactive) — 儿童友好型学习网站生成器

## 概述 (Overview)

为儿童（5-10 岁）构建生产级的互动数学学习网站，具备以下特性：
- **深色极光主题**（深蓝黑背景 + 模块专属主题色 + Aurora 动效 + 点阵背景）
- 中文 Web Speech API 语音播报（支持播放/停止切换）
- 互动方法卡片，带有循序渐进的揭示动画
- 引导式题解流程（答案 → 引导提问 → 费曼讲解）
- 带有鼓励性反馈和重试机制的练习系统
- 移动端优先的响应式设计（针对 iPad 优化）

## 设计系统 (Design System)

### 深色极光调色板 (必须使用)

```css
:root {
  --bg: #030712;               /* 深蓝黑背景 */
  --bg2: #0a0f1e;
  --card: rgba(255,255,255,0.03);
  --card-border: rgba(255,255,255,0.08);
  --text: #f8fafc;             /* 主文字 */
  --muted: #94a3b8;            /* 次要文字 */
  --muted2: #64748b;           /* 更淡的次要文字 */
  /* 模块主题色（每个模块选一个，用于 tab active、hero badge、hover 等） */
  --amber: #f59e0b; --amber-light: #fcd34d;   /* 模块1 几何 */
  --orange: #f97316; --orange-light: #fdba74; /* 模块2 数与运算 */
  --emerald: #10b981;                          /* 成功/正确 */
  --cyan: #06b6d4;                             /* 引导/概念 */
  --purple: #8b5cf6; --purple-light: #a78bfa; /* 模块7 策略 */
}
```

**模块主题色对照（各模块使用对应主题色）：**

| 模块 | 主题色 | 主题色值 |
|-----|-------|---------|
| 模块一 几何与图形 | amber | `#f59e0b` / `#fcd34d` |
| 模块二 数与运算 | orange | `#f97316` / `#fdba74` |
| 模块三 逻辑推理 | cyan | `#06b6d4` / `#67e8f9` |
| 模块四 空间立体 | blue | `#3b82f6` / `#93c5fd` |
| 模块五 数据统计 | rose | `#f43f5e` / `#fda4af` |
| 模块六 测量单位 | amber | `#f59e0b` / `#fcd34d` |
| 模块七 组合策略 | purple | `#8b5cf6` / `#a78bfa` |

**通用语义色（不随模块变化）：**
- 正确/成功：`#10b981` (emerald) / `#6ee7b7`
- 错误/警告：`#ef4444` (red) / `#fca5a5`
- 引导提示：`#06b6d4` (cyan) / `#67e8f9`

### 字体 (Typography)

- 主字体：`'Inter'` — 现代清晰
- 中文字体：`'Noto Sans SC', sans-serif` — 清爽的中文支持
- 基础字号：`16px`
- 行高：`1.7`

### 字体引入 (必须包含)
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
```

### Aurora 背景动效 (必须包含)

```html
<!-- 放在 <body> 开始，.page 之前 -->
<div class="aurora">
  <div class="aurora-blob ab1"></div>
  <div class="aurora-blob ab2"></div>
  <div class="aurora-blob ab3"></div>
</div>
<div class="dot-grid"></div>
<div class="page">
  <!-- 所有页面内容 -->
</div>
```

```css
/* Aurora blobs — 颜色根据模块主题色调整 */
.aurora { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.aurora-blob { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.12; animation: auroraF linear infinite; }
/* 以模块七（紫色）为例 */
.ab1 { width: 600px; height: 600px; background: radial-gradient(circle,#8b5cf6,transparent 70%); top: -100px; left: -100px; animation-duration: 22s; }
.ab2 { width: 500px; height: 500px; background: radial-gradient(circle,#6d28d9,transparent 70%); top: 50%; right: -100px; animation-duration: 28s; animation-delay:-10s; }
.ab3 { width: 400px; height: 400px; background: radial-gradient(circle,#ec4899,transparent 70%); bottom: 10%; left: 20%; animation-duration: 20s; animation-delay:-5s; }
@keyframes auroraF { 0%{transform:translate(0,0)} 33%{transform:translate(30px,-25px)} 66%{transform:translate(-15px,35px)} 100%{transform:translate(0,0)} }

/* 点阵背景 */
.dot-grid { position: fixed; inset: 0; z-index: 0; pointer-events: none; background-image: radial-gradient(rgba(255,255,255,0.05) 1px,transparent 1px); background-size: 28px 28px; mask-image: radial-gradient(ellipse 70% 70% at 50% 50%,black 40%,transparent 100%); }
.page { position: relative; z-index: 1; }
```

### Topbar、Hero、Tab Nav 结构模板

```html
<!-- Sticky topbar -->
<div class="topbar">
  <div class="topbar-inner">
    <a href="../../index.html" class="back-link">← 返回主页</a>
    <span class="topbar-sep">/</span>
    <span class="topbar-title">模块X · 模块名称</span>
  </div>
</div>

<div class="container">
  <!-- Hero -->
  <div class="mod-hero">
    <div class="hero-badge">🔷 模块X</div>
    <h1 class="hero-title">关键词 · 关键词 · <span class="hero-grad">亮点词</span></h1>
    <p class="hero-sub">一句话描述模块内容</p>
    <div class="hero-stats">
      <div class="hstat"><span class="hstat-num">N</span><span class="hstat-label">核心概念</span></div>
      <div class="hstat"><span class="hstat-num">N</span><span class="hstat-label">学习技巧</span></div>
      <div class="hstat"><span class="hstat-num">N</span><span class="hstat-label">例题精讲</span></div>
      <div class="hstat"><span class="hstat-num">N</span><span class="hstat-label">闯关题目</span></div>
    </div>
    <nav class="tab-nav">
      <button class="tab-pill on" data-s="s1">💡 概念</button>
      <button class="tab-pill" data-s="s2">🛠 技巧</button>
      <button class="tab-pill" data-s="s3">📖 例题</button>
      <button class="tab-pill" data-s="s4">🎮 闯关</button>
    </nav>
  </div>

  <!-- Sections (tab panels) -->
  <div id="s1" class="sec on">…</div>
  <div id="s2" class="sec">…</div>
  <div id="s3" class="sec">…</div>
  <div id="s4" class="sec">…</div>
</div>
```

**Tab 切换 JS（必须使用）：**
```javascript
document.querySelectorAll('.tab-pill').forEach(btn => {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.tab-pill').forEach(b => b.classList.remove('on'));
    document.querySelectorAll('.sec').forEach(s => s.classList.remove('on'));
    this.classList.add('on');
    document.getElementById(this.dataset.s).classList.add('on');
    speechSynthesis.cancel();
    if (currentBtn) { currentBtn.classList.remove('playing'); currentBtn.innerHTML = currentBtn.dataset.orig || currentBtn.innerHTML; currentBtn = null; }
  });
});
```

### 核心 CSS（必须包含，主题色用模块对应颜色替换 `--theme-*`）

```css
/* Topbar */
.topbar { position: sticky; top: 0; z-index: 100; background: rgba(3,7,18,0.8); backdrop-filter: blur(20px); border-bottom: 1px solid var(--card-border); padding: 0 24px; }
.topbar-inner { max-width: 960px; margin: 0 auto; display: flex; align-items: center; gap: 16px; height: 60px; }
.back-link { display: inline-flex; align-items: center; gap: 6px; color: var(--muted); font-size: 13px; font-weight: 500; text-decoration: none; transition: color .2s; padding: 6px 12px; border-radius: 8px; }
.back-link:hover { color: var(--text); background: rgba(255,255,255,0.05); }
.topbar-sep { color: var(--muted2); font-size: 14px; }
.topbar-title { font-size: 14px; font-weight: 600; color: var(--muted); }

/* Tab Nav */
.tab-nav { display: inline-flex; gap: 6px; background: rgba(255,255,255,0.04); border: 1px solid var(--card-border); border-radius: 16px; padding: 6px; margin-top: 24px; }
.tab-pill { padding: 10px 22px; border-radius: 10px; font-size: 14px; font-weight: 600; border: none; background: transparent; color: var(--muted); cursor: pointer; transition: all .25s; white-space: nowrap; font-family: 'Noto Sans SC', sans-serif; display: flex; align-items: center; gap: 6px; }
.tab-pill:hover { background: rgba(255,255,255,0.06); color: var(--text); }
/* 模块主题色 — 以 amber 为例，替换为对应模块颜色 */
.tab-pill.on { background: rgba(245,158,11,0.18); color: #fcd34d; box-shadow: 0 0 0 1px rgba(245,158,11,0.35); }

/* Hero */
.mod-hero { padding: 40px 0 32px; animation: fadeUp .5s ease both; }
.hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; border-radius: 999px; background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.25); font-size: 12px; font-weight: 700; color: #fcd34d; margin-bottom: 16px; }
.hero-title { font-size: clamp(28px,5vw,48px); font-weight: 900; letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 12px; }
.hero-grad { background: linear-gradient(135deg,#fcd34d,#fdba74); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.hero-sub { font-size: 16px; color: var(--muted); max-width: 560px; line-height: 1.6; }
.hero-stats { display: flex; gap: 20px; margin-top: 20px; flex-wrap: wrap; }
.hstat { display: flex; flex-direction: column; }
.hstat-num { font-size: 22px; font-weight: 800; color: #fcd34d; }
.hstat-label { font-size: 11px; color: var(--muted2); font-weight: 500; }

/* Container & Sections */
.container { max-width: 960px; margin: 0 auto; padding: 0 24px 80px; }
.sec { display: none; animation: fadeUp .4s ease; }
.sec.on { display: block; }
.sec-heading { font-size: 22px; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--card-border); }

/* Glass Card */
.gcard { background: var(--card); border: 1px solid var(--card-border); border-radius: 20px; padding: 28px; margin-bottom: 20px; position: relative; transition: border-color .3s; }
.gcard:hover { border-color: rgba(245,158,11,0.25); }

/* Concept Box */
.cbox { border-radius: 16px; padding: 20px 20px 20px 24px; margin: 14px 0; position: relative; border-left: 3px solid var(--accent, #f59e0b); background: var(--accent-bg, rgba(245,158,11,0.05)); }
.cbox h4 { font-size: 17px; font-weight: 700; margin-bottom: 8px; color: var(--accent, #fcd34d); }
.cbox p, .cbox ul { font-size: 15px; color: var(--muted); line-height: 1.8; }

/* Voice Button */
.vbtn { position: absolute; top: 14px; right: 14px; display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 8px; border: none; font-size: 15px; font-weight: 600; cursor: pointer; transition: all .25s; font-family: 'Noto Sans SC', sans-serif; }
.vbtn-a { background: rgba(245,158,11,0.12); color: #fcd34d; border: 1px solid rgba(245,158,11,0.25); }
.vbtn-o { background: rgba(249,115,22,0.12); color: #fdba74; border: 1px solid rgba(249,115,22,0.25); }
.vbtn-e { background: rgba(16,185,129,0.12); color: #6ee7b7; border: 1px solid rgba(16,185,129,0.25); }
.vbtn-c { background: rgba(6,182,212,0.12); color: #67e8f9; border: 1px solid rgba(6,182,212,0.25); }
.vbtn-p { background: rgba(139,92,246,0.12); color: #a78bfa; border: 1px solid rgba(139,92,246,0.25); }

/* Inline voice button (non-absolute) */
.va-btn { display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 8px; border: none; font-size: 15px; font-weight: 600; cursor: pointer; transition: all .25s; background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.25); color: #fcd34d; font-family: 'Noto Sans SC', sans-serif; }

/* Method Card */
.mcard { background: var(--card); border: 1px solid var(--card-border); border-radius: 16px; margin-bottom: 12px; cursor: pointer; transition: all .3s; overflow: hidden; }
.mcard-head { padding: 20px 24px; display: flex; align-items: center; gap: 16px; }
.mcard-chevron { font-size: 18px; color: var(--muted); transition: transform .3s; margin-left: auto; }
.mcard.open .mcard-chevron { transform: rotate(180deg); color: #fcd34d; }
.mcard-body { max-height: 0; overflow: hidden; transition: max-height .5s cubic-bezier(0.23,1,0.32,1); }
.mcard-body.open { max-height: 1400px; }
.mcard-body-inner { padding: 0 24px 24px; border-top: 1px solid var(--card-border); }

/* Reveal button */
.reveal-btn { display: inline-flex; align-items: center; gap: 6px; padding: 8px 18px; border-radius: 10px; background: rgba(245,158,11,0.1); border: 1px dashed rgba(245,158,11,0.35); color: #fcd34d; font-size: 13px; font-weight: 600; cursor: pointer; transition: all .25s; margin-bottom: 12px; font-family: 'Noto Sans SC', sans-serif; }

/* Choice buttons (example & quiz) */
.choice-btn { padding: 10px 20px; border-radius: 12px; font-size: 15px; font-weight: 600; border: 1.5px solid var(--card-border); background: rgba(255,255,255,0.03); color: var(--text); cursor: pointer; transition: all .25s; font-family: 'Noto Sans SC', sans-serif; }
.choice-btn:hover:not(.dis) { border-color: rgba(245,158,11,0.4); background: rgba(245,158,11,0.08); }
.choice-btn.correct { background: rgba(16,185,129,0.15); border-color: #6ee7b7; color: #6ee7b7; }
.choice-btn.wrong { background: rgba(239,68,68,0.1); border-color: #fca5a5; color: #fca5a5; animation: shake .4s ease; }
@keyframes shake { 0%,100%{transform:translateX(0)} 25%{transform:translateX(-6px)} 75%{transform:translateX(6px)} }

/* Guide chain */
.guide-item { border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.07); background: rgba(255,255,255,0.02); margin-bottom: 8px; }
.guide-item.active { border-color: rgba(245,158,11,0.35); }
.guide-item.locked { opacity: .4; pointer-events: none; }
.guide-q { padding: 12px 16px; font-size: 14px; color: var(--muted); cursor: pointer; display: flex; align-items: center; gap: 10px; }
.guide-a { display: none; padding: 12px 16px; border-top: 1px solid rgba(255,255,255,0.06); background: rgba(245,158,11,0.05); font-size: 14px; color: var(--muted); line-height: 1.7; }
.guide-a strong { color: var(--text); }

/* Feynman box */
.feynman-box { background: rgba(16,185,129,0.07); border: 1.5px solid rgba(16,185,129,0.25); border-radius: 14px; padding: 18px; margin-top: 14px; display: none; }
.feynman-box.show { display: block; }
.feynman-box .fn-title { font-size: 15px; font-weight: 700; color: #6ee7b7; margin-bottom: 12px; }

/* Quiz */
.q-dot { width: 28px; height: 28px; border-radius: 50%; background: rgba(255,255,255,0.06); border: 1.5px solid var(--card-border); font-size: 11px; font-weight: 700; color: var(--muted2); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all .25s; }
.q-dot.on { background: rgba(245,158,11,0.2); border-color: #fcd34d; color: #fcd34d; }
.q-dot.ok { background: rgba(16,185,129,0.15); border-color: #6ee7b7; color: #6ee7b7; }
.q-dot.bad { background: rgba(239,68,68,0.1); border-color: #fca5a5; color: #fca5a5; }
.q-opt { padding: 12px 16px; border-radius: 12px; border: 1.5px solid var(--card-border); background: rgba(255,255,255,0.02); font-size: 14px; color: var(--text); cursor: pointer; transition: all .25s; text-align: left; font-family: 'Noto Sans SC', sans-serif; }
.q-opt:hover:not(.dis) { border-color: rgba(245,158,11,0.4); background: rgba(245,158,11,0.06); }
.q-opt.correct { background: rgba(16,185,129,0.12); border-color: #6ee7b7; color: #6ee7b7; }
.q-opt.wrong { background: rgba(239,68,68,0.08); border-color: #fca5a5; animation: shake .4s ease; }

/* ctrl-btn */
.ctrl-btn { padding: 7px 14px; border-radius: 9px; font-size: 13px; font-weight: 600; cursor: pointer; border: 1px solid rgba(245,158,11,0.3); background: rgba(245,158,11,0.07); color: #fcd34d; transition: all .2s; font-family: 'Noto Sans SC', sans-serif; }

@keyframes fadeUp { from { opacity:0; transform:translateY(16px); } to { opacity:1; transform:none; } }
```

## 架构 — 4 个板块 (Architecture)

每个学习页面固定包含 4 个标签页板块，通过药丸状按钮导航：

### 板块 1: 💡 概念详解 (Concept Details) — 交互可视化优先

**核心原则：每个概念必须用可交互的图形/动效来表达，禁止纯文字说明。**

每个概念对应一个独立的交互组件卡片（`.cbox`），卡片内包含：
1. **交互区域**（Canvas / SVG / CSS Grid）— 儿童能直接操作
2. **状态反馈**（实时显示操作结果）
3. **辅助文字标注**（简短说明，非主要内容）
4. 语音按钮 (🔊) 位于卡片 **右上角**

#### 交互组件类型选择指南

| 概念类型 | 推荐组件 | 示例 |
|---------|---------|------|
| 角度、方向、旋转 | `<canvas>` + 鼠标/触摸拖拽 | 拖动射线改变角度，实时显示度数和类型 |
| 对称、折叠、翻转 | SVG + 动画（CSS keyframes / JS） | 点击形状切换对称轴，演示折叠效果 |
| 面积、计数、分组 | CSS Grid + 点击切换 | 点击格子涂色，实时显示面积数量 |
| 数轴、比较大小 | SVG + 拖动滑块 | 拖动点在数轴上，显示大小关系 |
| 图形识别、分类 | SVG 形状 + 点击高亮 | 点击图形看属性标注弹出 |
| 分数、比例 | SVG 扇形/矩形分割 + 点击 | 点击区域改变着色，显示分数值 |
| 3D 展开图 | CSS 3D transform + 按钮 | 点击"展开"将立体图展平，点击"折叠"还原 |
| 时钟、时间 | Canvas 时钟盘 + 拖动指针 | 拖动分针/时针，读出对应时间 |

#### Canvas 拖拽组件模板（以角度为例）

```javascript
// 支持鼠标 + 触摸（iPad 兼容）
canvas.addEventListener('mousedown', startDrag);
canvas.addEventListener('touchstart', e => startDrag(e.touches[0]));
canvas.addEventListener('mousemove', onDrag);
canvas.addEventListener('touchmove', e => { e.preventDefault(); onDrag(e.touches[0]); }, { passive: false });
canvas.addEventListener('mouseup', endDrag);
canvas.addEventListener('touchend', endDrag);

function draw() {
  ctx.clearRect(0, 0, W, H);
  // 绘制固定臂 + 可拖动臂 + 弧形 + 标注
  // 根据角度值改变颜色（锐角/直角/钝角/平角）
  requestAnimationFrame(draw);  // 仅拖动时调用，非循环
}
```

#### SVG 动态组件模板（以对称为例）

```html
<svg id="sym-svg" viewBox="0 0 300 300" width="100%">
  <!-- 形状路径 -->
  <path id="shape" d="..." fill="#A7CBE8" stroke="#7DB4D9" stroke-width="2"/>
  <!-- 对称轴（虚线，动画显示） -->
  <line id="axis-h" x1="0" y1="150" x2="300" y2="150"
        stroke="#F4A7BB" stroke-width="2" stroke-dasharray="8 4"
        style="animation: dash-in 0.5s ease forwards"/>
</svg>
<!-- 切换形状按钮 + 折叠演示按钮 -->
```

#### CSS Grid 可点击面积组件模板

```html
<div class="area-grid" style="display:grid;grid-template-columns:repeat(5,44px);gap:3px">
  <!-- 每格: filled(实色)/filled-half(三角)/empty(灰色虚线) -->
  <div class="ag-cell filled" onclick="toggleCell(this)"></div>
  ...
</div>
<div class="area-count">已选：<strong id="cnt">9</strong> 格</div>
```

#### 预设按钮组（辅助交互）

每个交互组件底部提供 3-4 个**预设案例按钮**，一键切换到典型示例：
```html
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:12px">
  <button class="preset-btn" onclick="loadPreset('锐角')">📐 锐角</button>
  <button class="preset-btn" onclick="loadPreset('直角')">📐 直角</button>
  <button class="preset-btn" onclick="loadPreset('钝角')">📐 钝角</button>
</div>
```

#### 禁止的做法
- ❌ 纯文字定义（"锐角是小于90°的角"）
- ❌ 静态图片替代交互
- ❌ 只有文字列表，无可操作元素
- ✅ 必须让孩子能"动手"改变图形状态，通过自己操作理解规律

### 板块 2: 🛠 学习技巧 (Interactive Methods)

每个技巧方法用一个 `.mcard` 卡片展示，**必须包含挑战题图 + 步骤横向平铺**。

#### 技巧卡片结构

```html
<div class=”mcard”>
  <div class=”mcard-hd” onclick=”toggleCard(this)”>
    <span>🔷 技巧名称</span><span class=”arr”>▶</span>
  </div>
  <div class=”mcard-body”>

    <!-- 1. 挑战图形区：用 SVG 视觉化展示题目 -->
    <div class=”mcard-figure”>
      <div class=”fig-label”>挑战：题目文字描述</div>
      <svg viewBox=”0 0 200 120” width=”100%” style=”max-width:300px”>
        <!-- 题目图形 SVG，清晰展示题目中的几何形状 -->
      </svg>
    </div>

    <!-- 2. 揭示按钮 -->
    <button class=”reveal-btn vbtn vbtn-lilac” onclick=”revealSteps('ms1')”>
      👆 点我看解法！
    </button>

    <!-- 3. 步骤容器：横向平铺布局 -->
    <div id=”ms1” class=”steps-row”>
      <div class=”step”>
        <div class=”step-vis”>
          <svg viewBox=”0 0 160 100” width=”100%” height=”auto”>
            <!-- 步骤动画 SVG，使用 .sv / .sv-draw / .sv.pop 类 -->
          </svg>
        </div>
        <div class=”step-label”>① 第一步文字说明</div>
      </div>
      <div class=”step”><!-- 第二步 ... --></div>
      <div class=”step”><!-- 第三步 ... --></div>
    </div>

    <!-- 4. 语音按钮 -->
    <button class=”vbtn vbtn-sky” onclick=”toggleVoice(this, '语音文本')”>🔊 听讲解</button>
  </div>
</div>
```

#### 步骤横向平铺 CSS（必须使用）

```css
/* 步骤容器：横向 flex，每步一张卡片 */
[id^=”ms”] {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: stretch;
  margin-bottom: 4px;
}

/* 每个步骤卡片：竖向排列（图 + 文字） */
.step {
  flex: 1;
  min-width: 140px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 12px 10px;
  background: rgba(255,255,255,0.03);
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,0.07);
  opacity: 0;
  transform: translateY(14px);
  transition: all .45s cubic-bezier(.23,1,.32,1);
}
.step.show { opacity: 1; transform: translateY(0); }

/* 步骤图形区：充满卡片宽度 */
.step-vis { width: 100%; }
.step-vis svg { width: 100%; height: auto; display: block; border-radius: 8px; overflow: visible; }

/* 揭示按钮独占一行 */
[id^=”ms”] ~ .va-btn,
[id^=”ms”] .va-btn { flex-basis: 100%; }

/* 挑战图形区 */
.mcard-figure {
  text-align: center;
  margin-bottom: 12px;
  padding: 12px;
  background: rgba(255,255,255,0.04);
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.08);
}
.fig-label {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 8px;
}
```

#### SVG 动画系统（步骤图的动效）

每个步骤 SVG 内的元素通过 `.sv`、`.sv-draw`、`.sv.pop` 类实现动效，动效随 `.step.show` 类被添加时触发。

```css
/* 淡入 */
.sv { opacity: 0; }
.step.show .sv { animation: svFade .5s ease forwards; }

/* 描线（需要 SVG 元素设置 stroke-dasharray=”1” pathLength=”1”） */
.sv-draw { stroke-dashoffset: 1; stroke-dasharray: 1; }
.step.show .sv-draw { animation: svLine .6s ease forwards; }

/* 弹出缩放 */
.step.show .sv.pop { animation: svPop .4s cubic-bezier(.34,1.56,.64,1) forwards; }

@keyframes svFade  { to { opacity: 1; } }
@keyframes svLine  { to { stroke-dashoffset: 0; } }
@keyframes svPop   { from { opacity:0; transform:scale(.4); } to { opacity:1; transform:scale(1); } }
```

**动效用法示例：**
- 描线（画边/辅助线）：`<line class=”sv sv-draw” pathLength=”1” stroke-dasharray=”1” stroke-dashoffset=”1” .../>`
- 淡入文字/标注：`<text class=”sv” .../>`
- 弹出（公式框、结果）：`<rect class=”sv pop” .../>`、`<text class=”sv pop” .../>`
- 延迟：在元素上加 `style=”animation-delay:.2s”`

#### 步骤揭示 JS（必须使用重置动画版本）

```javascript
function revealSteps(id) {
  const c = document.getElementById(id);
  // 先重置（强制 reflow 让 CSS 动画重新触发）
  c.querySelectorAll('.step').forEach(s => {
    s.classList.remove('show');
    void s.offsetHeight;  // 强制重排，重启动画
  });
  // 逐步显示，每步延迟 520ms
  c.querySelectorAll('.step').forEach((s, i) =>
    setTimeout(() => s.classList.add('show'), i * 520)
  );
  // 隐藏揭示按钮
  const rb = c.previousElementSibling;
  if (rb && rb.classList.contains('reveal-btn')) rb.style.display = 'none';
}
```

#### 各技巧类型步骤图参考

| 技巧类型 | 步骤图建议 |
|---------|-----------|
| 数边认形（多边形） | ①描边动画（逐边 svLine）→ ②公式弹出（sv pop）→ ③角标注（svFade） |
| 方格计数（面积） | ①整格高亮（svFade 序列）→ ②半格标注（svFade）→ ③加法合并（sv pop） |
| 折叠对称验证 | ①对称轴描线（svLine）→ ②折叠色块叠合（svFade）→ ③✅/❌标记（sv pop） |
| 图形分割法 | ①切割线描出（svLine）→ ②各块面积标注（svFade）→ ③求和公式（sv pop） |
| 旋转/平移规律 | ①原图→②变换后位置（svFade）→ ③规律说明（sv pop） |

#### 挑战题 SVG 显示完整性校验（生成后必须逐一自查）

每个 `.mcard-figure` 内的挑战 SVG 生成后，**必须按以下清单逐项自查**，确保内容不被裁切：

**① viewBox 边界检查**
- 计算 SVG 内所有元素的实际占用范围（x + width、y + height 的最大值）
- 确认 viewBox 的宽高 ≥ 内容最大边界 + **至少 8px 内边距**
- 文字元素：`<text>` 的 y 坐标是基线，字体 `font-size` 的约 30% 会超出基线向下延伸，需额外预留
- 例：`font-size="14"` 的文字基线 y=90，实际底部约 y=94，viewBox 高度至少需 102

**② 每类元素的裁切风险点**

| 元素类型 | 裁切风险 | 修复方法 |
|---------|---------|---------|
| `<text>` 基线 | 文字底部（descender）超出 y 坐标约 20-30% | viewBox 高度多留 `font-size × 0.35` |
| `<text>` 行末 | 中文字符比估算宽，末字可能超出右边界 | 宽度多留 20-30px，或用 `text-anchor="middle"` 居中 |
| `<circle>` 边缘 | cx-r < 0 或 cx+r > width | 确认 cx ≥ r+2，cx+r ≤ viewBox宽-2 |
| `<rect>` 右/下边 | x+width 或 y+height 超出 | 与 viewBox 尺寸对比，确认不超出 |
| stroke 超边 | stroke-width 向外扩展 stroke-width/2 | 内边距 ≥ max(stroke-width)/2 |
| `animation:svPop` | scale弹出时元素原始尺寸 ×1，不超边即可 | 检查原始位置而非动画中间态 |

**③ 自查流程（生成每个挑战 SVG 后执行）**

```
1. 列出 SVG 内所有元素的坐标极值：
   - x_max = max(所有 x + width，所有 cx + r，所有 text_x + 估算宽度)
   - y_max = max(所有 y + height，所有 cy + r，所有 text_y + font-size×0.35)
2. 对比 viewBox：
   - 若 x_max > viewBox_width - 8  → 增大 viewBox 宽度 或 缩小/移动元素
   - 若 y_max > viewBox_height - 8 → 增大 viewBox 高度 或 缩小/移动元素
3. 文字多行时，每行额外占 line-height（通常 font-size × 1.4）
4. 对 max-width 样式：确认缩放后在移动端（最小约 280px 宽）不会有内容超出 SVG 比例
```

**④ 常见错误示例与修正**

```html
<!-- ❌ 错误：文字基线 y=88，font-size=13，底部约 y=93，viewBox高度90不够 -->
<svg viewBox="0 0 200 90">
  <text x="100" y="88" font-size="13">说明文字</text>
</svg>

<!-- ✅ 修正：viewBox高度改为 105，预留足够空间 -->
<svg viewBox="0 0 200 105">
  <text x="100" y="88" font-size="13">说明文字</text>
</svg>

<!-- ❌ 错误：圆半径28，圆心x=28，左边界 28-28=0，stroke会被裁切 -->
<svg viewBox="0 0 200 100">
  <circle cx="28" cy="50" r="28" stroke-width="2"/>
</svg>

<!-- ✅ 修正：圆心x至少=r+stroke/2+2=31 -->
<svg viewBox="0 0 200 100">
  <circle cx="31" cy="50" r="28" stroke-width="2"/>
</svg>
```

#### 禁止的做法
- ❌ 步骤纯文字列表（无 SVG 图形）
- ❌ 挑战题没有配图（`.mcard-figure` 不可省略）
- ❌ 步骤垂直堆叠（必须横向 flex 平铺）
- ❌ 步骤图太小（每张步骤卡 `flex:1; min-width:140px`，SVG 充满卡片宽度）
- ❌ SVG 内容超出 viewBox 边界（必须通过上方校验清单）
- ✅ 每步一张卡，图在上（SVG 动画），文字简短在下
- ✅ 生成后对每个挑战 SVG 执行坐标极值自查，确认内容完整可见

### 板块 3: 📖 例题精讲 (Example Problem Walkthrough)
这是最复杂的板块。流程如下：

```
显示题目 → 儿童选择答案
  ├─ 正确 → 显示 “🎉 答对了” + “📖 点击查看解题讲解 →” 按钮
  │           点击按钮 → showExplanation(id)
  └─ 错误 → 显示两个按钮：
       ├─ “🔄 再试试” → 重置，让儿童重试
       └─ “📖 查看解法” → 标记正确答案，直接调用 showExplanation(id)（无需再次点击）

showExplanation(id):
  1. 查找 #exN-visual（互动可视化区，可选）
  2. 若存在则 classList.add('show')，fadeUp 动画展开，滚动到该位置
  3. 500ms 后（无 visual 则立即）调用 buildGuide(id, data)

引导链 buildGuide (顺序解锁):
  问题 1 (已解锁) → 点击 → 显示答案 + 🔊 → 解锁问题 2
  ...
  最后一个问题 → 点击 → 显示答案 → 自动显示费曼讲解框

费曼讲解框:
  绿边卡片，包含 3 步简单的解释 + 语音按钮
```

**关键规则：**
- 儿童必须先回答才能看到任何解释（讲解入口在答题结果里）
- 答对显示按钮入口，点击后才展开讲解
- 答错点”查看解法”直接展开讲解（不需要再多点一次）
- 互动可视化（`.ex-visual`）放在 `.ex-result` **后面**，CSS 默认 `display:none`，通过 `showExplanation` 添加 `.show` 类展开
- 引导提问逐一解锁，费曼讲解框仅在所有引导问题查看后出现

#### HTML 结构顺序（必须严格遵守）

```html
<div class=”excard-body”>
  <!-- 1. 题目 -->
  <div class=”qbox”>…</div>
  <p style=”font-size:13px;color:var(--muted);margin-bottom:12px”>选择你的答案 ↓</p>

  <!-- 2. 选项（JS initEx 生成） -->
  <div class=”ex-opts” id=”exN-opts”></div>

  <!-- 3. 答题结果 + 讲解入口按钮（JS handleEx 填充） -->
  <div class=”ex-result” id=”exN-result”></div>

  <!-- 4. 互动可视化（可选，默认隐藏，showExplanation 时展开） -->
  <div class=”ex-visual” id=”exN-visual”>…</div>

  <!-- 5. 引导链（JS buildGuide 生成） -->
  <div class=”guide-chain” id=”exN-guide”></div>

  <!-- 6. 费曼讲解框（引导链末尾自动出现） -->
  <div class=”feynman-box” id=”exN-feynman”>…</div>
</div>
```

> ⚠️ `ex-visual` 必须放在 `ex-result` **后面**，**绝不放在题目上方**。

#### CSS（必须包含）

```css
.ex-visual { display: none; }
.ex-visual.show { display: block; animation: fadeUp .4s ease both; }
```

#### JS 核心函数

```javascript
function handleEx(id, idx) {
  const data = exData[id];
  const opts = document.querySelectorAll('#'+id+'-opts .ex-opt');
  const res = document.getElementById(id+'-result');
  if (data.opts[idx].v) {
    opts.forEach((o,i) => { o.classList.add('dim'); if(data.opts[i].v) o.classList.add('correct'); });
    res.style.cssText = 'display:block;padding:12px 16px;border-radius:12px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);color:#6ee7b7;margin-bottom:12px';
    res.innerHTML = `🎉 答对了！你真棒！<br><button onclick=”showExplanation('${id}')” style=”margin-top:10px;padding:8px 18px;border-radius:10px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.35);color:#6ee7b7;font-size:13px;font-weight:700;cursor:pointer;font-family:'Noto Sans SC',sans-serif”>📖 点击查看解题讲解 →</button>`;
  } else {
    opts[idx].classList.add('wrong');
    res.style.cssText = 'display:block;padding:12px 16px;border-radius:12px;background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.2);color:#fcd34d;margin-bottom:12px';
    res.innerHTML = `<div style=”margin-bottom:10px”>💡 这个答案不太对哦，没关系！</div>
      <div style=”display:flex;gap:8px;flex-wrap:wrap”>
        <button onclick=”retryEx('${id}',${idx})” style=”padding:8px 16px;border-radius:10px;background:rgba(6,182,212,0.12);border:1px solid rgba(6,182,212,0.3);color:#67e8f9;font-size:13px;font-weight:700;cursor:pointer;font-family:'Noto Sans SC',sans-serif”>🔄 再试试</button>
        <button onclick=”learnEx('${id}')” style=”padding:8px 16px;border-radius:10px;background:rgba(245,158,11,0.12);border:1px solid rgba(245,158,11,0.3);color:#fcd34d;font-size:13px;font-weight:700;cursor:pointer;font-family:'Noto Sans SC',sans-serif”>📖 查看解法</button>
      </div>`;
  }
}

function learnEx(id) {
  const data = exData[id];
  document.querySelectorAll('#'+id+'-opts .ex-opt').forEach((o,i) => {
    o.classList.add('dim'); if(data.opts[i].v) o.classList.add('correct');
  });
  const res = document.getElementById(id+'-result');
  res.style.cssText = 'display:block;padding:12px 16px;border-radius:12px;background:rgba(96,165,250,0.08);border:1px solid rgba(96,165,250,0.2);color:#93c5fd;margin-bottom:12px';
  res.innerHTML = '📖 没关系！正确答案已标出，我们一起来看——';
  setTimeout(() => showExplanation(id), 400);  // 直接展开，无需再点
}

function showExplanation(id) {
  const data = exData[id];
  const vis = document.getElementById(id+'-visual');
  if (vis) { vis.classList.add('show'); vis.scrollIntoView({behavior:'smooth', block:'center'}); }
  setTimeout(() => buildGuide(id, data), vis ? 500 : 0);
}
```

#### 袋鼠真题截图处理规则 (Real Exam Question Screenshots)

当例题来自袋鼠数学竞赛真题（kangaroo math competition）时，**优先使用 PDF 截图**展示题目，而不是把题目文字重新打出来。

**真题截图例题的 HTML 结构：**

```html
<div class=”excard”>
  <div class=”excard-hdr”>
    <span class=”ex-num”>例题X</span>
    <span class=”ex-tag”>20XX年 · 考点名称</span>
  </div>
  <div class=”excard-body”>
    <div class=”qbox”>
      🦘 <strong>袋鼠数学竞赛真题（20XX年 第N题）</strong><br><br>
      <img src=”../assets/exam-images/20XX/qNN.png”
           alt=”20XX年第N题”
           style=”width:100%;border-radius:10px;margin:8px 0 4px”>
      <small>提示：……（针对该题关键切入点的一句话提示）</small>
    </div>
    <p style=”font-size:13px;color:var(--muted);margin-bottom:12px”>选择你的答案 ↓</p>
    <div class=”ex-opts” id=”exN-opts”></div>
    <div class=”ex-result” id=”exN-result”></div>
    <!-- ex-visual 可选，放这里 -->
    <div class=”guide-chain” id=”exN-guide”></div>
    <div class=”feynman-box” id=”exN-feynman”>…</div>
  </div>
</div>
```

**选项展示决策规则：**

| 选项内容 | 处理方式 |
|---------|---------|
| 纯文字或纯数字（如 “34426”、”10千克”、”丙”） | `exData` 中用文字字符串，渲染为可点击文字按钮 |
| 包含图形、图案、图片的选项 | **在 `<img>` 下方额外放选项截图**，同时保留文字按钮用于交互（标注 A/B/C/D/E） |
| 混合型（文字 + 图案组合） | 以图形优先，截图展示，文字按钮标 (A)~(E) |

**图形选项的处理示例：**

```html
<div class=”qbox”>
  🦘 <strong>袋鼠数学竞赛真题（20XX年 第N题）</strong><br><br>
  <!-- 题目主图（含选项图形） -->
  <img src=”../assets/exam-images/20XX/qNN.png” …>
  <small>提示：选项图案在图中已标出(A)~(E)，选择你认为正确的字母。</small>
</div>
```

> 当 PDF 整页截图已包含 ABCDE 选项时，无需额外截图选项部分；直接展示整页图即可，文字按钮仅起”提交答案”作用。

**图片路径规则：**
- 本项目的真题截图统一存放于 `src/assets/exam-images/<年份>/qNN.png`
- 在 `src/modules/` 目录下的 HTML 中，相对路径为 `../assets/exam-images/<年份>/qNN.png`
- 年份目录：2013~2025；文件命名：`q01.png`~`q24.png`（按题号，两位数补零）

**`exData` 对应写法（真题，文字选项）：**

```javascript
exN: {
  opts: [
    {t:'(A) 选项文字', v:false},
    {t:'(B) 选项文字', v:true},   // v:true 为正确答案
    {t:'(C) 选项文字', v:false},
    {t:'(D) 选项文字', v:false},
    {t:'(E) 选项文字', v:false}
  ],
  guide: [
    {q:'引导问题1', a:'答案1', vc:'口语化讲解1', va:'音频id_g1'},
    {q:'引导问题2', a:'答案2', vc:'口语化讲解2', va:'音频id_g2'},
    {q:'引导问题3', a:'答案3', vc:'口语化讲解3', va:'音频id_g3'}
  ]
}
```

**答案索引对照（0-indexed）：**
- A=0, B=1, C=2, D=3, E=4
- 与 `exam-data.js` 中的 `ans` 字段一致，可直接复用

**提示语撰写要求：**
- 必须写，不可省略
- 一句话，直接说明解题切入点，如：
  - “提示：找出哪几个位置的形状相同。”
  - “提示：两张图的区别是什么？差了多少重量？”
  - “提示：每种图案代表不同数字，从最简单的行/列入手。”
- 语气引导而非直接给答案

### 板块 4: 🎮 闯关挑战 (Quiz Challenge)
- 星级进度条 (每个题目对应 ⭐/☆)
- 题目跳转导航点
- 每个题目显示：难度勋章 + 来源参考标签
- 错误答案：抖动动画 + 提示文字 + 2.2s 后自动清除
- 正确答案：标记为绿色 + 显示鼓励性反馈
- 前进/后退导航按钮

## 语音系统 (Web Speech API)

```javascript
// 切换模式：点击播放，再次点击停止
let currentBtn = null;
function toggleVoice(btn, text) {
  if (btn.classList.contains('playing')) {
    speechSynthesis.cancel();
    btn.classList.remove('playing');
    btn.innerHTML = btn.dataset.orig;
    currentBtn = null;
    return;
  }
  // 停止任何正在播放的声音
  if (currentBtn) {
    speechSynthesis.cancel();
    currentBtn.classList.remove('playing');
    currentBtn.innerHTML = currentBtn.dataset.orig;
  }
  btn.dataset.orig = btn.innerHTML;
  btn.innerHTML = '⏹';
  btn.classList.add('playing');
  currentBtn = btn;

  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'zh-CN';
  u.rate = 0.82;   // 语速较慢，适合儿童
  u.pitch = 1.15;  // 音调略高，更亲切
  // 优先选用高质量中文语音
  const voices = speechSynthesis.getVoices();
  const best = voices.find(v =>
    v.name.includes('Tingting') || v.name.includes('Xiaoxiao')
  ) || voices.find(v => v.lang.startsWith('zh'));
  if (best) u.voice = best;
  u.onend = () => {
    btn.classList.remove('playing');
    btn.innerHTML = btn.dataset.orig;
    currentBtn = null;
  };
  speechSynthesis.speak(u);
}
```

**语音按钮规则：**
- 所有语音按钮使用切换模式 (播放/停止)
- 一次只能播放一个语音
- 概念卡片中的语音按钮：位于卡片右上角
- 技巧/示例中的语音按钮：紧跟内容内联显示
- 播放时按钮变为 ⏹，并带有 `.playing` CSS 动画
- 切换标签页时取消所有正在播放的语音

## CSS 组件参考 (CSS Component Reference)

完整 CSS 在「核心 CSS」章节中列出，主要组件：
- `.vbtn-a/o/e/c/p` — 语音按钮（amber/orange/emerald/cyan/purple 五色变体）
- `.va-btn` — 内联语音按钮（非绝对定位）
- `.ctrl-btn` — 交互控制按钮
- `.cbox` — 概念框（`--accent` 和 `--accent-bg` 自定义颜色）
- `.mcard` + `.mcard-head` + `.mcard-body` — 可折叠技巧卡片
- `.gcard` — 玻璃感卡片容器
- `.reveal-btn` — 步骤揭示按钮
- `.choice-btn` / `.q-opt` — 选择题选项按钮
- `.guide-item` / `.guide-q` / `.guide-a` — 引导链
- `.feynman-box` — 费曼讲解框
- `.q-dot` — 题目导航点
- 动画关键帧：`fadeUp`、`shake`、`auroraF`

## 内容准则 (Content Guidelines)

### 语言与语气
- 全程使用中文 (zh-CN)
- 语气像一个有趣的大朋友，而不是老师
- 多用“我们一起”、“你觉得呢”、“你注意到了吗”
- 严禁说“这道题很简单”或“你应该知道”
- 针对错误答案：“这个想法很有创意！不过让我们再看看……”
- 内容中大量使用表情符号 (🎈🦘⭐🎉✅❌💡🔍)

### 语音文本规则
- 将语音文本写成自然的中文口语（不是朗读书面文字）
- 每个语音段控制在 30 秒以内（约 80-100 个汉字）
- 使用停顿：文本中的“……”会产生自然的语音停顿
- 语音内容应自包含（不看屏幕也能听懂）

## 输入要求 (Input Requirements)

当用户提供内容用于构建学习页面时，期望包含：
1. **模块名称** — 例如：”计数与数感”
2. **核心概念** — 3-5 个概念，**每个概念必须说明用什么交互形式展示**（如无说明，自行判断最适合的交互类型）
3. **学习技巧** — 3-5 个带名称和描述的方法
4. **例题讲解** — 1-3 个题目，包含：
   - 题目文本和选项
   - 引导提问链 (4-5 个循序渐进的问题及答案)
   - 费曼风格的 3 步讲解
5. **练习题** — 5-20 个题目，包含选项、正确答案和反馈

**生成顺序：先确定每个概念的交互方式（Canvas/SVG/Grid），再写代码。**

## 输出 (Output)

单个自包含的 `.html` 文件，包含：
- 所有的 CSS 内联在 `<style>` 标签中
- 所有的 JavaScript 内联在 `<script>` 标签中
- 通过 CDN 链接加载 Google Fonts
- 除了字体 CDN 外，无其他外部依赖
- 移动端响应式（可在 iPad 的 Safari 中正常运行）
- 文件保存至 `/mnt/user-data/outputs/`
