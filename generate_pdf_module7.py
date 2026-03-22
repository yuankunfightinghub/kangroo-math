#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

# Register Chinese CID font
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
FONT = "STSong-Light"

output_path = "/Users/yuankun/KangrooMath/src/assets/exam-images/模块七_组合与策略进阶练习题.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    leftMargin=2*cm,
    rightMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
)

W = A4[0] - 4*cm  # usable width

# Styles
title_style = ParagraphStyle(
    "title", fontName=FONT, fontSize=20, leading=28,
    alignment=TA_CENTER, textColor=colors.HexColor("#1a237e"), spaceAfter=6
)
subtitle_style = ParagraphStyle(
    "subtitle", fontName=FONT, fontSize=13, leading=18,
    alignment=TA_CENTER, textColor=colors.HexColor("#37474f"), spaceAfter=4
)
intro_style = ParagraphStyle(
    "intro", fontName=FONT, fontSize=11, leading=17,
    alignment=TA_CENTER, textColor=colors.HexColor("#546e7a"), spaceAfter=12
)
section_style = ParagraphStyle(
    "section", fontName=FONT, fontSize=14, leading=20,
    textColor=colors.HexColor("#0d47a1"), spaceBefore=14, spaceAfter=4,
    borderPad=4, backColor=colors.HexColor("#e3f2fd"), borderRadius=4,
    leftIndent=4, rightIndent=4,
)
desc_style = ParagraphStyle(
    "desc", fontName=FONT, fontSize=11, leading=17,
    textColor=colors.HexColor("#212121"), spaceAfter=6, leftIndent=4
)
point_style = ParagraphStyle(
    "point", fontName=FONT, fontSize=10, leading=15,
    textColor=colors.HexColor("#00695c"), spaceAfter=4, leftIndent=4,
    backColor=colors.HexColor("#e8f5e9"), borderPad=3,
)
table_header_style = ParagraphStyle(
    "table_header", fontName=FONT, fontSize=10, leading=14,
    textColor=colors.white, alignment=TA_CENTER
)
table_cell_style = ParagraphStyle(
    "table_cell", fontName=FONT, fontSize=10, leading=14,
    textColor=colors.HexColor("#212121"), alignment=TA_CENTER
)

questions = [
    {
        "header": "题目一｜2014年 第17题",
        "desc": "将 2、3、4、5 填入方框组成的乘法和加法算式中，求可能的最大值。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2014/q17.png",
        "point": "考察点：最优化枚举 — 穷举各种填入方式，比较结果大小找出最大值。",
    },
    {
        "header": "题目二｜2019年 第17题",
        "desc": "绵羊比奶牛多 8 只，奶牛是绵羊的一半，利用倍数关系和线段图求解农场动物总数。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2019/q17.png",
        "point": "考察点：倍数关系代换 — 建立「奶牛=绵羊÷2」的等量关系，联立求解。",
    },
    {
        "header": "题目三｜2019年 第19题",
        "desc": "10 只骆驼共有 14 个驼峰，利用假设法或等量代换求双峰驼的数量。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2019/q19.png",
        "point": "考察点：假设法/等量代换 — 假设全为单峰驼，通过差值推算双峰驼数量。",
    },
    {
        "header": "题目四｜2019年 第20题",
        "desc": "3 只松鼠共采 7 个坚果，条件是数量各不相同且至少有 1 个，求最多能采多少个坚果。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2019/q20.png",
        "point": "考察点：最优分配枚举 — 在约束条件下列出所有合法分配方案，找出最大值。",
    },
    {
        "header": "题目五｜2020年 第21题",
        "desc": "篮子里有苹果和梨，结合颜色特征与数量差的复杂条件进行分配推算。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2020/q21.png",
        "point": "考察点：多条件数量推理 — 综合颜色与数量差两类约束逐步缩小范围。",
    },
    {
        "header": "题目六｜2020年 第24题",
        "desc": "两人互相交换糖果，最后每人 4 颗，反推最初数量。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2020/q24.png",
        "point": "考察点：倒推策略 — 从结果逆向还原每一步交换前的状态。",
    },
    {
        "header": "题目七｜2021年 第18题",
        "desc": "女巫「3苹果=1香蕉，3香蕉=1苹果」的代换循环魔法，从4个苹果和5个香蕉开始最终剩什么？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2021/q18.png",
        "point": "考察点：等量代换循环 — 识别代换关系中的循环结构，判断最终等价数量。",
    },
    {
        "header": "题目八｜2021年 第19题",
        "desc": "将卡片放入两个盒子并要求总和相等，找出必须绑定在一起的数字组合。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2021/q19.png",
        "point": "考察点：分组等和约束 — 枚举卡片分组方式，找出使两组总和相等的必要绑定组合。",
    },
    {
        "header": "题目九｜2022年 第17题",
        "desc": "相连的每个房子里 5 个数字之和固定为 20，逆向反推被盖住的数字。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2022/q17.png",
        "point": "考察点：固定和逆推 — 利用「每5个连续数之和=20」的约束，推算被遮挡的数字。",
    },
    {
        "header": "题目十｜2022年 第21题",
        "desc": "利用不同形状代表不同数字的已知算式，解开最后的未知图形算式。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2022/q21.png",
        "point": "考察点：图形代数代换 — 从已知算式建立方程组，逐步代换求解未知图形的值。",
    },
    {
        "header": "题目十一｜2022年 第24题",
        "desc": "将桌上 5 张乱序卡片排成递增顺序，求需要交换的最少步数。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2022/q24.png",
        "point": "考察点：最少步数优化 — 分析当前排列与目标排列的差异，找出最优交换序列。",
    },
    {
        "header": "题目十二｜2023年 第22题",
        "desc": "选出形状合适的拼图块放在网格上，以覆盖并求出最大的数字之和。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2023/q22.png",
        "point": "考察点：覆盖最优化 — 在约束形状下枚举放置位置，最大化覆盖数字之和。",
    },
    {
        "header": "题目十三｜2024年 第18题",
        "desc": "从黑板上选两数相加，探究能够产生多少个不同的结果。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2024/q18.png",
        "point": "考察点：组合计数 — 枚举所有两数之和，去重后统计不同结果数量。",
    },
    {
        "header": "题目十四｜2024年 第21题",
        "desc": "通过观察三种不同积木搭成的三座塔的高度，代换推算第四座塔的高度。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2024/q21.png",
        "point": "考察点：方程组代换 — 建立三个高度方程，逐步消元求解各积木高度后推算第四座。",
    },
    {
        "header": "题目十五｜2024年 第23题",
        "desc": "「每天做2题周日完工，每天做3题周三完工」，通过工作天数推算总题量。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2024/q23.png",
        "point": "考察点：工作量方程 — 建立「天数×每日量=总量」的等式，利用两个条件联立求解。",
    },
    {
        "header": "题目十六｜2024年 第24题",
        "desc": "掷飞镖「初始10支，中靶奖2支，共掷20支」，利用动态平衡推算中靶次数。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2024/q24.png",
        "point": "考察点：动态平衡方程 — 建立「初始+奖励-消耗=0」的守恒方程推算中靶次数。",
    },
    {
        "header": "题目十七｜2025年 第18题",
        "desc": "一人买3条巧克力，另一人买5条且多付8欧，利用差价推算单价。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2025/q18.png",
        "point": "考察点：差价代换 — 建立两人花费的差值方程，直接求解单价。",
    },
    {
        "header": "题目十八｜2025年 第24题",
        "desc": "在方格里填色，要求相同颜色不相邻的最优分配策略。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2025/q24.png",
        "point": "考察点：约束着色最优化 — 在「相邻不同色」的约束下寻找使用颜色数最少或分配最优的方案。",
    },
]

summary_data = [
    ["年份", "题号", "核心考点", "考察类型"],
    ["2014", "Q17", "填数求最大值", "最优化枚举"],
    ["2019", "Q17", "倍数关系联立求解", "等量代换"],
    ["2019", "Q19", "假设法求双峰驼", "假设代换"],
    ["2019", "Q20", "约束条件最优分配", "最优化"],
    ["2020", "Q21", "多条件数量推理", "条件约束"],
    ["2020", "Q24", "交换糖果倒推", "倒推策略"],
    ["2021", "Q18", "代换循环魔法", "等量代换"],
    ["2021", "Q19", "分组等和约束", "组合约束"],
    ["2022", "Q17", "固定和逆推隐藏数", "逆推策略"],
    ["2022", "Q21", "图形代数代换", "等量代换"],
    ["2022", "Q24", "最少交换步数", "最优化"],
    ["2023", "Q22", "覆盖最大数字和", "最优化"],
    ["2024", "Q18", "两数和不同结果数", "组合计数"],
    ["2024", "Q21", "积木高度代换推算", "等量代换"],
    ["2024", "Q23", "工作量方程联立", "等量代换"],
    ["2024", "Q24", "动态平衡中靶次数", "动态分配"],
    ["2025", "Q18", "差价推算单价", "等量代换"],
    ["2025", "Q24", "约束着色最优分配", "最优化"],
]

story = []

# Title block
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("模块七 · 组合与策略进阶练习题汇总", title_style))
story.append(Paragraph("专项主题：代数等量代换、最优化寻找与动态分配", subtitle_style))
story.append(Paragraph(
    "这是历年压轴题中的「得分分水岭」，重点考察代数等量代换启蒙、最优化寻找（最少/最多）以及动态分配。",
    intro_style
))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#90caf9"), spaceAfter=10))

for q in questions:
    story.append(Paragraph(q["header"], section_style))
    story.append(Paragraph(q["desc"], desc_style))

    img_path = q["image"]
    if os.path.exists(img_path):
        from PIL import Image as PILImage
        with PILImage.open(img_path) as im:
            iw, ih = im.size
        ratio = ih / iw
        img_w = W
        img_h = img_w * ratio
        max_h = 10 * cm
        if img_h > max_h:
            img_h = max_h
            img_w = img_h / ratio
        img = Image(img_path, width=img_w, height=img_h)
        story.append(img)
    else:
        story.append(Paragraph(f"[图片未找到: {img_path}]", desc_style))

    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(q["point"], point_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#b0bec5"), spaceAfter=8, spaceBefore=8))

# Summary table
story.append(Spacer(1, 0.5*cm))
summary_section_style = ParagraphStyle(
    "summary_section", fontName=FONT, fontSize=14, leading=20,
    textColor=colors.HexColor("#0d47a1"), spaceBefore=10, spaceAfter=8,
    borderPad=4, backColor=colors.HexColor("#e3f2fd"), borderRadius=4,
    leftIndent=4, rightIndent=4,
)
story.append(Paragraph("汇总表｜十八题核心考点一览", summary_section_style))

col_widths = [W * 0.10, W * 0.10, W * 0.45, W * 0.35]
table_rows = []
for i, row in enumerate(summary_data):
    para_style = table_header_style if i == 0 else table_cell_style
    table_rows.append([Paragraph(cell, para_style) for cell in row])

t = Table(table_rows, colWidths=col_widths, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0d47a1")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#f5f5f5"), colors.white]),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#b0bec5")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))
story.append(t)

doc.build(story)
print(f"PDF saved to: {output_path}")
