---
name: kids-math-interactive
description: "为 5-10 岁儿童创建互动数学学习网站。当用户想要构建教育类数学 Web 应用、互动学习页面、数学测验游戏或任何适合儿童的基于 HTML 的数学教学工具时，请使用此技能。触发展现包括：请求“数学学习网站”、“儿童互动数学”、“数学测验游戏”、“儿童教育 Web 应用”、“数学练习网站”，或任何提到为儿童构建 Web 端数学学习体验的场景。当用户提供数学知识点、练习题或课程内容并希望将其转化为互动 Web 体验时，也会触发。此技能处理全流程：马卡龙色系主题、语音合成集成、引导式示例讲解、互动测验以及循序渐进的揭示动画。即使由于数学内容较多，用户只说“把这个做成有趣的教学页面”，也要使用此技能。"
---

# 少儿数学互动 (Kids Math Interactive) — 儿童友好型学习网站生成器

## 概述 (Overview)

为儿童（5-10 岁）构建生产级的互动数学学习网站，具备以下特性：
- 马卡龙奶油色系（柔和、护眼）
- 中文 Web Speech API 语音播报（支持播放/停止切换）
- 互动方法卡片，带有循序渐进的揭示动画
- 引导式题解流程（答案 → 引导提问 → 费曼讲解）
- 带有鼓励性反馈和重试机制的练习系统
- 移动端优先的响应式设计（针对 iPad 优化）

## 设计系统 (Design System)

### 马卡龙调色板 (必须使用)

```css
:root {
  --bg: #FDF6F0;        /* 奶油淡暖白背景 */
  --card: #FFFFFF;
  --rose: #F4A7BB;       /* 玫瑰粉 — 主色调 */
  --rose-deep: #E8839E;
1:   --mint: #A8D8CB;        /* 薄荷绿 — 成功态、费曼讲解 */
29:   --mint-deep: #7CC4B2;
30:   --lemon: #F9E4A7;       /* 柠檬黄 — 高亮 */
31:   --lemon-deep: #F0D078;
32:   --lilac: #C5B3D9;       /* 丁香紫 — 练习、挑战 */
33:   --lilac-deep: #A68EC1;
34:   --sky: #A7CBE8;          /* 天空蓝 — 引导、概念 */
35:   --sky-deep: #7DB4D9;
36:   --peach: #F5C5A3;        /* 蜜桃橙 — 警告、逆向思维 */
37:   --peach-deep: #E8A87C;
38:   --dark: #4A3728;         /* 暖深棕 — 正文文字 */
39:   --muted: #8B7D75;        /* 柔和棕 — 次要文字 */
}
```

### 字体 (Typography)

- 标题字体：`'ZCOOL KuaiLe', cursive` (来自 Google Fonts) — 活泼、儿童友好
- 正文字体：`'Noto Sans SC', sans-serif` (来自 Google Fonts) — 清爽的中文支持
- 基础字号：`17px` (比普通字号大，适合平板电脑上的儿童)
- 行高：`1.7`

### 字体引入 (必须包含)
```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700;900&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
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
- 可展开的 `.mcard` 卡片 — 点击切换打开/关闭
- 每张卡片包含：
  1. 一个 **挑战问题** (例如：“数数这些水果！”)
  2. 一个 **揭示按钮** ("👆 点我看解法！")
  3. 隐藏的 `.mstep` 步骤，逐一动画显示（每个延迟 400ms）
  4. 底部的语音按钮
- 步骤使用带编号的圆圈 (`.snum`)，颜色与方法主题色一致

### 板块 3: 📖 例题精讲 (Example Problem Walkthrough)
这是最复杂的板块。流程如下：

```
显示题目 → 儿童选择答案
  ├─ 正确 → 显示 "🎉 答对了" → 开启引导链
  └─ 错误 → 显示两个按钮：
       ├─ "🔄 再试试哦" → 重置，让儿童重试
       └─ "📖 有点难哦，学学解法" → 标记正确答案，然后开启引导链

引导链 (顺序解锁):
  问题 1 (已解锁) → 点击 → 显示答案 + 🔊 → 解锁问题 2
  问题 2 → 点击 → 显示答案 + 🔊 → 解锁问题 3
  ...
  最后一个问题 → 点击 → 显示答案 → 自动显示费曼讲解框

费曼讲解框:
  绿边卡片，包含 3 步简单的解释 + 语音按钮
```

**关键规则：**
- 儿童必须先回答（或点击“学学解法”）才能看到任何解释
- 引导提问逐一解锁 — 必须查看当前项才能解锁下一项
- 费曼讲解框仅在所有引导问题查看后才会出现
- 错误答案显示两个按钮（重试 + 学习），不自动消失

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

阅读 `references/components.md` 以获取完整的 CSS 类参考，包括：
- `.vbtn` 变体 (`.vbtn-rose`, `.vbtn-mint`, `.vbtn-lilac`, `.vbtn-sky`, `.vbtn-peach`)
- `.cbox` 概念框
- `.mcard` 技巧卡片（含 `.mdetail` 和 `.mstep`）
- `.excard` 示例卡片（含 `.guide-chain` 和 `.feynman-box`）
- `.quiz-sec` 测验板块组件
- 动画关键帧

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
