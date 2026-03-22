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

output_path = "/Users/yuankun/KangrooMath/src/assets/exam-images/模块三_逻辑推理进阶练习题.pdf"

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
        "header": "题目一｜2015年 第20题",
        "desc": "Joy 连续 3 天抓老鼠，每天比前一天多抓 2 只，第三天抓的数量是第一天的两倍，问 3 天共抓了几只？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2015/q20.png",
        "point": "考察点：等差数列规律推算 — 建立方程，利用\u201c每天多 2 只\u201d与\u201c第三天是第一天两倍\u201d两个条件联立求解。",
    },
    {
        "header": "题目二｜2020年 第18题",
        "desc": "两列各有 31 节车厢、方向相反的火车，其中一列的第 19 节车厢与另一列的第 19 节车厢相对，问第 12 节车厢会与对面哪节车厢相对？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2020/q18.png",
        "point": "考察点：相向运动中的车厢对应关系 — 分析对称结构，推导任意编号车厢的配对规律。",
    },
    {
        "header": "题目三｜2020年 第20题",
        "desc": "图中箭头从 A 指向 B 表示 A 比 B 高。根据图中所有箭头指向关系，请问谁最矮？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2020/q20.png",
        "point": "考察点：有向图传递推理 — 梳理多条高矮关系链，找出唯一无法成为\u201c更高者\u201d的人。",
    },
    {
        "header": "题目四｜2022年 第22题",
        "desc": "三匹斑马参加比赛，Runa 有 15 条纹，Zara 比 Runa 少 3 条，小 R 比小 B 少 5 条，比小 Z 多 3 条，问获胜者（条纹最多）有多少条纹？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2022/q22.png",
        "point": "考察点：多条件数量推理 — 利用各个大小关系逐步推算每匹斑马的条纹数，排序找最大值。",
    },
    {
        "header": "题目五｜2023年 第18题",
        "desc": "五个孩子共同过生日，每人有自己的蛋糕。Leo 比 Jose 大两岁，Ali 比 Vittorio 小一岁，Vittorio 是最小的，请问 Sarah 的蛋糕是哪个？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2023/q18.png",
        "point": "考察点：多约束排序推理 — 综合年龄大小、相对关系等多个条件，确定每个孩子的年龄排名并对应蛋糕。",
    },
    {
        "header": "题目六｜2023年 第21题",
        "desc": "Emma 在独舞比赛中获得第三名，她前后各有三名选手，问比赛共有多少人参加？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2023/q21.png",
        "point": "考察点：间隔计数推理 — 根据'前三后三'的间隔人数结合名次推算总参赛人数，注意计数边界。",
    },
    {
        "header": "题目七｜2024年 第20题",
        "desc": "Ali、Bella、Che 和 Dimitry 各有 3 个图形，每位小朋友恰好有一个图形与其他每位小朋友相同，请问 Dimitry 有哪些图形？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2024/q20.png",
        "point": "考察点：多条件集合匹配 — 逐一比对已知三人的图形，利用'恰好各有一个相同'的约束逐步排除，确定第四人的组合。",
    },
    {
        "header": "题目八｜2025年 第17题",
        "desc": "Mary 书架上有几本书，先将灰色书与绿色书互换，再将灰色书与黑色书互换，问最终书架上的书是如何排列的？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2025/q17.png",
        "point": "考察点：多步操作顺序追踪 — 依次执行两次换位操作，追踪每本书的位置变化，避免混淆操作顺序。",
    },
    {
        "header": "题目九｜2025年 第21题",
        "desc": "每张瓢虫贴纸有 1、2、3 或 4 个点。将贴纸填入网格，使每行每列中的瓢虫点数各不相同，问填满后顶行是什么样子？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2025/q21.png",
        "point": "考察点：数独启蒙 — 在 4×4 网格中，依据已有约束逐步推断空格的唯一合法填法。",
    },
]

summary_data = [
    ["年份", "题号", "核心考点", "推理类型"],
    ["2015", "Q20", "等差规律 + 方程建立", "数量规律"],
    ["2020", "Q18", "车厢对称对应关系", "结构规律"],
    ["2020", "Q20", "有向图高矮传递推理", "关系推导"],
    ["2022", "Q22", "多条件数量大小排序", "条件约束"],
    ["2023", "Q18", "多约束年龄排序匹配", "条件约束"],
    ["2023", "Q21", "间隔计数推总人数", "数量规律"],
    ["2024", "Q20", "集合元素多对多匹配", "条件约束"],
    ["2025", "Q17", "多步换位操作追踪", "操作规律"],
    ["2025", "Q21", "数独填格唯一性推断", "条件约束"],
]

story = []

# Title block
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("模块三 · 逻辑推理进阶练习题汇总", title_style))
story.append(Paragraph("专项主题：多条件约束推理与规律推导", subtitle_style))
story.append(Paragraph("这是 5 分题中占比极高的部分，多为多条件约束（类似数独）或长周期的规律推导。", intro_style))
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
story.append(Paragraph("汇总表｜九题核心考点一览", summary_section_style))

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
