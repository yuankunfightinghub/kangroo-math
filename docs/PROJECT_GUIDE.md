# 🦘 袋鼠数学乐园 — 项目开发指南

## 用 Claude Code 进行编码开发 + Git 管理

---

## 一、项目初始化

### 1. 创建 GitHub 仓库

在 GitHub 上创建一个新仓库：
- 仓库名：`math-kangaroo`
- 可见性：Public（方便用 GitHub Pages 部署）
- 勾选 "Add a README file"

### 2. 在本地用 Claude Code 初始化

打开终端，运行以下命令：

```bash
# 克隆仓库
git clone https://github.com/你的用户名/math-kangaroo.git
cd math-kangaroo

# 创建项目结构
mkdir -p src/modules
mkdir -p src/assets
mkdir -p skills/kids-math-interactive
mkdir -p docs
```

### 3. 项目目录结构

```
math-kangaroo/
├── README.md                          # 项目说明
├── index.html                         # 主页（模块导航）
├── src/
│   ├── modules/
│   │   ├── module1-counting.html      # 模块一：计数与数感
│   │   ├── module2-geometry.html      # 模块二：几何与图形
│   │   ├── module3-logic.html         # 模块三：逻辑推理
│   │   ├── module4-spatial.html       # 模块四：空间想象
│   │   ├── module5-paths.html         # 模块五：路径迷宫
│   │   ├── module6-measurement.html   # 模块六：测量单位
│   │   └── module7-strategy.html      # 模块七：组合策略
│   └── assets/
│       └── (图片等静态资源)
├── skills/
│   └── kids-math-interactive/         # Claude Skill
│       ├── SKILL.md
│       └── references/
│           ├── components.md
│           └── interactions.md
├── docs/
│   ├── 袋鼠数学_七大模块完整学习手册.docx
│   └── (其他参考文档)
└── .gitignore
```

---

## 二、Claude Code 开发工作流

### 1. 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 在项目目录下启动 Claude Code

```bash
cd math-kangaroo
claude
```

### 3. 用 Claude Code 开发新模块

在 Claude Code 的命令行中，你可以直接说：

```
请基于 skills/kids-math-interactive/SKILL.md 这个 Skill，
为模块二（几何与图形认知）创建一个交互学习页面。

以下是模块二的内容：
- 核心概念：旋转识别、镜像翻转、拼图补全、多角度观察、图形叠加
- 学习方法：标记追踪法、镜子口诀、动手操作法、排除法、叠加法
- 例题1：2024年Q4 旋转识别题（附引导提问和费曼讲解）
- 例题2：2021年Q5 镜像翻转题（附引导提问和费曼讲解）
- 闯关题目：22道几何真题

请输出到 src/modules/module2-geometry.html
```

Claude Code 会读取 Skill 文件，按照里面的设计规范自动生成完整的 HTML 页面。

### 4. 常用 Claude Code 指令示例

```
# 创建新模块
请按照 Skill 规范创建模块三的交互学习页面

# 修改已有模块
在 module1-counting.html 的闯关挑战中增加5道新题目

# 创建主页导航
创建一个 index.html 主页，用马卡龙配色，展示7个模块的卡片导航

# 调试问题
module2 的语音按钮在 iPad 上不工作，请帮我检查并修复

# 批量操作
把所有模块的闯关挑战部分的字体从 17px 改成 18px
```

---

## 三、Git 版本管理

### 1. 基本工作流

```bash
# 查看修改了什么
git status
git diff

# 提交修改
git add .
git commit -m "feat: 完成模块一交互学习页面"

# 推送到 GitHub
git push origin main
```

### 2. 推荐的 Commit 规范

```
feat: 新增模块一交互学习页面
feat: 添加模块二几何类真题22道
fix: 修复 iPad Safari 语音播放问题
style: 更新马卡龙配色方案
docs: 添加项目开发文档
refactor: 重构语音播放组件为独立函数
```

### 3. 分支管理（可选）

```bash
# 开发新模块时创建分支
git checkout -b feature/module2-geometry

# 开发完成后合并回主分支
git checkout main
git merge feature/module2-geometry
git push origin main
```

### 4. .gitignore 文件

```
.DS_Store
node_modules/
*.log
.env
```

---

## 四、GitHub Pages 部署

### 1. 开启 GitHub Pages

1. 进入仓库 Settings → Pages
2. Source 选 `Deploy from a branch`
3. Branch 选 `main`，文件夹选 `/ (root)`
4. 点 Save

### 2. 等待部署

1-2分钟后，你的网站会在以下地址上线：

```
https://你的用户名.github.io/math-kangaroo/
```

### 3. iPad 访问

在 iPad 的 Safari 中打开上面的网址就能直接使用！

**添加到主屏幕：**
Safari → 点底部分享按钮 → "添加到主屏幕" → 改名为"袋鼠数学" → 添加

这样 iPad 桌面就会出现一个专属图标，点一下就能进入学习。

---

## 五、开发计划

### Phase 1：基础框架 ✅
- [x] 创建 Skill 规范文档
- [x] 完成模块一：计数与数感
- [ ] 创建主页导航 index.html

### Phase 2：7个模块
- [ ] 模块二：几何与图形认知
- [ ] 模块三：逻辑推理与规律发现
- [ ] 模块四：空间想象与立体几何
- [ ] 模块五：路径、迷宫与方向
- [ ] 模块六：测量与单位
- [ ] 模块七：组合与策略

### Phase 3：增强功能
- [ ] 学习进度存储（localStorage）
- [ ] 错题本功能
- [ ] 每日挑战模式
- [ ] 成就系统（徽章收集）
- [ ] 家长报告页面

---

## 六、技术栈

| 技术 | 用途 |
|------|------|
| HTML/CSS/JS | 前端（纯静态，无框架） |
| Web Speech API | 中文语音播放 |
| Google Fonts | ZCOOL KuaiLe + Noto Sans SC |
| GitHub Pages | 免费托管部署 |
| Claude Code | AI 辅助编码 |
| Claude Skill | 规范化开发模板 |
