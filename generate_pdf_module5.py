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

output_path = "/Users/yuankun/KangrooMath/src/assets/exam-images/模块五_路径迷宫与方向进阶练习题.pdf"

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
        "header": "题目一｜2015年 第18题",
        "desc": "袋鼠从圆圈 S 沿连线跳到相邻圆圈，每个圆圈只能跳过一次，且只允许跳 4 次，请问共有几种不同的方式能跳到圆圈 F？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2015/q18.png",
        "point": "考察点：路径计数 \u2014 在图结构中，满足\u201c限定步数 + 不重复经过\u201d约束下枚举所有合法路径。",
    },
    {
        "header": "题目二｜2020年 第19题",
        "desc": "蜜蜂只能在灰色蜂房中行走。Mark 需要恰好涂色 2 个白色蜂房，使蜜蜂能从 A 走到 B，请问有几种涂法？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2020/q19.png",
        "point": "考察点：路径连通性 — 在六边形网格中，判断添加最少节点后能打通从 A 到 B 的路径，枚举合法方案数。",
    },
    {
        "header": "题目三｜2022年 第23题",
        "desc": "小凯的车只能左转，不能右转。以下五条路线中，小凯可以走哪条？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2022/q23.png",
        "point": "考察点：方向约束路径判断 — 逐一分析路线图中的每个转弯方向，排除含右转的路线，找出全程只左转的合法路线。",
    },
    {
        "header": "题目四｜2023年 第19题",
        "desc": "地图上标有 5 个村庄 A、B、C、D、E 及各村庄之间的公里数。无论选哪条路线，任意两村庄之间的距离都相等，请问是哪两个村庄？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2023/q19.png",
        "point": "考察点：地图距离分析 — 读取带权图中各路径的公里数，找出任意路线总距离相同的两点对。",
    },
    {
        "header": "题目五｜2023年 第20题",
        "desc": "同上页，地图村庄距离题延伸分析。注意：此图与Q19为同一页扫描图。",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2023/q20.png",
        "point": "考察点：路径等距判断 — 综合多条路线的公里数，找出无论经何路线距离恒等的两个村庄。",
    },
]

summary_data = [
    ["年份", "题号", "核心考点", "难度方向"],
    ["2015", "Q18", "限步数路径枚举", "图遍历 + 计数"],
    ["2020", "Q19", "六边形网格连通补色", "路径连通性"],
    ["2022", "Q23", "只左转路线判断", "方向约束"],
    ["2023", "Q19", "地图等距村庄对", "权图分析"],
    ["2023", "Q20", "地图村庄距离（同页）", "权图分析"],
]

story = []

# Title block
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("模块五 · 路径、迷宫与方向进阶练习题汇总", title_style))
story.append(Paragraph("专项主题：最优路径选择、方向约束与空间导航", subtitle_style))
story.append(Paragraph("结合了方向感与最优路径的选择，部分题目带有障碍物或特殊行进规则。", intro_style))
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
story.append(Paragraph("汇总表｜五题核心考点一览", summary_section_style))

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
