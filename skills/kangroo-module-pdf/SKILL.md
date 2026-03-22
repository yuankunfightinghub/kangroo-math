---
name: kangroo-module-pdf
description: 为 KangrooMath 项目生成模块进阶练习题 PDF。用户提供模块名称、主题说明、题目列表（年份+题号+描述+考察点），自动检索真题图片并生成带真题原图的排版 PDF。
---

# KangrooMath 模块进阶 PDF 生成规范

适用项目：`/Users/yuankun/KangrooMath`

---

## 触发方式

用户提供以下信息时触发本 skill：
- 模块编号与名称（如"模块二 · 几何进阶"）
- 模块主题说明（一句话）
- 题目列表，每题包含：年份、题号、题目描述、考察点

---

## 执行流程

### Step 1：检索真题图片

图片路径规则：
```
/Users/yuankun/KangrooMath/src/assets/exam-images/{年份}/q{题号两位数}.png
```
例：2023年第18题 → `2023/q18.png`

**重要：先用 Read 工具读取每张图片，确认内容与题目描述一致。**

如果图片内容与题目描述不符（如多题共用同一页扫描），需从原始 PDF 重新截取：
- 原始 PDF 路径：`/Users/yuankun/KangrooMath/src/assets/{年份} 等级*.pdf`
- 用 PyMuPDF（`import fitz`）渲染对应页面（3x 分辨率），再用 Pillow 裁剪题目区域
- 覆盖保存到正确的 `exam-images/{年份}/q{N}.png`

### Step 2：生成 PDF

PDF 输出路径：
```
/Users/yuankun/KangrooMath/src/assets/exam-images/模块{N}_{名称}进阶练习题.pdf
```

脚本保存路径：
```
/Users/yuankun/KangrooMath/generate_pdf_module{N}.py
```

#### 样式规范（与现有模块保持一致）

使用 `reportlab` + `STSong-Light` CID 字体支持中文：

```python
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
FONT = "STSong-Light"
```

| 元素 | 样式 |
|------|------|
| 大标题 | fontSize=20，颜色 #1a237e，居中 |
| 副标题 | fontSize=13，颜色 #37474f，居中 |
| 简介 | fontSize=11，颜色 #546e7a，居中 |
| 题目标题 | fontSize=14，颜色 #0d47a1，背景 #e3f2fd |
| 题目描述 | fontSize=11，颜色 #212121 |
| 考察点框 | fontSize=10，颜色 #00695c，背景 #e8f5e9 |
| 分隔线 | 颜色 #b0bec5，thickness=0.5 |
| 汇总表头 | 背景 #0d47a1，白色文字 |
| 汇总表行 | 交替 #f5f5f5 / white |

#### 图片嵌入规则

```python
# 全宽嵌入，最大高度 10cm，保持宽高比
ratio = ih / iw
img_w = W  # 可用宽度 = A4宽 - 4cm
img_h = img_w * ratio
if img_h > 10 * cm:
    img_h = 10 * cm
    img_w = img_h / ratio
```

#### PDF 结构（每题）

1. 蓝色题目标题（`题目N｜{年份}年 第{题号}题`）
2. 题目描述文字
3. 真题原图（全宽嵌入）
4. 绿色考察点框
5. 分隔线

末尾附汇总表格（年份、题号、核心考点、难度/推理类型）。

### Step 3：验证

运行生成脚本，确认输出 PDF 路径正确，打印 `PDF saved to: ...`。

---

## 注意事项

- **不提交 exam/ PDF 原始试题文件到 git**（见项目记忆）
- 图片确认优先于生成，避免截图错误
- 若同一页扫描包含多题，必须精确裁剪目标题目区域
- 生成脚本复用现有风格，参考 `generate_pdf_module3.py`
