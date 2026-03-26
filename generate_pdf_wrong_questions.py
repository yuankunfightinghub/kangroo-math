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

output_path = "/Users/yuankun/KangrooMath/src/assets/错题汇总_待复习.pdf"

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
module_header_style = ParagraphStyle(
    "module_header", fontName=FONT, fontSize=15, leading=22,
    textColor=colors.HexColor("#b71c1c"), spaceBefore=18, spaceAfter=6,
    borderPad=5, backColor=colors.HexColor("#ffebee"), borderRadius=4,
    leftIndent=4, rightIndent=4,
)
wrong_info_style = ParagraphStyle(
    "wrong_info", fontName=FONT, fontSize=10, leading=15,
    textColor=colors.HexColor("#c62828"), spaceAfter=4, leftIndent=4,
    backColor=colors.HexColor("#fff3e0"), borderPad=3,
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

BASE = "/Users/yuankun/KangrooMath/src/assets/exam-images"

# Wrong questions grouped by module
modules = [
    {
        "name": "模块二 · 平面图形",
        "questions": [
            {
                "header": "题目一｜2017年 第11题",
                "wrong_info": "你的答案：C　　正确答案：E",
                "image": f"{BASE}/2017/q11.png",
                "point": "考察点：平面图形分析 — 仔细观察图形结构，注意形状特征与数量关系。",
            },
            {
                "header": "题目二｜2014年 第11题",
                "wrong_info": "你的答案：E　　正确答案：D",
                "image": f"{BASE}/2014/q11.png",
                "point": "考察点：平面图形分析 — 注意图形的对称性与变换规律。",
            },
        ],
        "summary": [
            ["年份", "题号", "你的答案", "正确答案", "分值"],
            ["2017", "Q11", "C", "E", "4分"],
            ["2014", "Q11", "E", "D", "4分"],
        ],
    },
    {
        "name": "模块四 · 立体图形",
        "questions": [
            {
                "header": "题目一｜2022年 第8题",
                "wrong_info": "你的答案：A　　正确答案：E",
                "image": f"{BASE}/2022/q08.png",
                "point": "考察点：立体图形空间想象 — 从不同角度观察三维形状，理解展开与折叠关系。",
            },
            {
                "header": "题目二｜2019年 第14题",
                "wrong_info": "你的答案：C　　正确答案：B",
                "image": f"{BASE}/2019/q14.png",
                "point": "考察点：立体图形计数与分析 — 准确数出隐藏部分，注意遮挡关系。",
            },
            {
                "header": "题目三｜2017年 第6题",
                "wrong_info": "你的答案：C　　正确答案：A",
                "image": f"{BASE}/2017/q06.png",
                "point": "考察点：立体图形识别 — 从平面图推断三维形体，注意各面的对应关系。",
            },
        ],
        "summary": [
            ["年份", "题号", "你的答案", "正确答案", "分值"],
            ["2022", "Q8", "A", "E", "3分"],
            ["2019", "Q14", "C", "B", "4分"],
            ["2017", "Q6", "C", "A", "3分"],
        ],
    },
    {
        "name": "模块三 · 逻辑推理",
        "questions": [
            {
                "header": "题目一｜2016年 第1题",
                "wrong_info": "你的答案：C　　正确答案：D",
                "image": f"{BASE}/2016/q01.png",
                "point": "考察点：逻辑推理 — 仔细分析条件，逐步排除不符合的选项。",
            },
            {
                "header": "题目二｜2015年 第1题",
                "wrong_info": "你的答案：A　　正确答案：D",
                "image": f"{BASE}/2015/q01.png",
                "point": "考察点：逻辑推理 — 理清多个条件之间的关系，找出唯一满足所有条件的答案。",
            },
            {
                "header": "题目三｜2014年 第15题",
                "wrong_info": "你的答案：D　　正确答案：B",
                "image": f"{BASE}/2014/q15.png",
                "point": "考察点：复杂逻辑推理 — 多步骤条件约束，注意每个条件的限制范围。",
            },
        ],
        "summary": [
            ["年份", "题号", "你的答案", "正确答案", "分值"],
            ["2016", "Q1", "C", "D", "3分"],
            ["2015", "Q1", "A", "D", "3分"],
            ["2014", "Q15", "D", "B", "4分"],
        ],
    },
    {
        "name": "模块五 · 路径与方向",
        "questions": [
            {
                "header": "题目一｜2025年 第5题",
                "wrong_info": "你的答案：D　　正确答案：A",
                "image": f"{BASE}/2025/q05.png",
                "point": "考察点：路径规划 — 分析可能的路径，注意方向限制与起终点。",
            },
            {
                "header": "题目二｜2023年 第8题",
                "wrong_info": "你的答案：B　　正确答案：D",
                "image": f"{BASE}/2023/q08.png",
                "point": "考察点：路径计数 — 系统枚举所有可能路径，避免重复或遗漏。",
            },
            {
                "header": "题目三｜2019年 第12题",
                "wrong_info": "你的答案：C　　正确答案：E",
                "image": f"{BASE}/2019/q12.png",
                "point": "考察点：路径与方向判断 — 追踪行走方向，注意转弯与朝向变化。",
            },
            {
                "header": "题目四｜2016年 第12题",
                "wrong_info": "你的答案：C　　正确答案：B",
                "image": f"{BASE}/2016/q12.png",
                "point": "考察点：迷宫路径分析 — 系统地尝试每条路径，找到满足条件的唯一路线。",
            },
            {
                "header": "题目五｜2015年 第18题",
                "wrong_info": "你的答案：B　　正确答案：D",
                "image": f"{BASE}/2015/q18.png",
                "point": "考察点：复杂路径推理（5分难题）— 结合方向与步数，精确追踪最终位置。",
            },
            {
                "header": "题目六｜2014年 第13题",
                "wrong_info": "你的答案：B　　正确答案：C",
                "image": f"{BASE}/2014/q13.png",
                "point": "考察点：路径方向综合 — 注意左右转与前进方向的组合，建立坐标系辅助分析。",
            },
        ],
        "summary": [
            ["年份", "题号", "你的答案", "正确答案", "分值"],
            ["2025", "Q5", "D", "A", "3分"],
            ["2023", "Q8", "B", "D", "3分"],
            ["2019", "Q12", "C", "E", "4分"],
            ["2016", "Q12", "C", "B", "4分"],
            ["2015", "Q18", "B", "D", "5分"],
            ["2014", "Q13", "B", "C", "4分"],
        ],
    },
]

story = []

# Title block
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("错题汇总 · 待复习练习册", title_style))
story.append(Paragraph("共 14 道错题，涵盖平面图形、立体图形、逻辑推理、路径与方向", subtitle_style))
story.append(Paragraph("针对每道错题，认真重做后对照正确答案，找出思路差距。", intro_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#ef9a9a"), spaceAfter=10))

q_num = 0
for module in modules:
    story.append(Paragraph(module["name"], module_header_style))

    for q in module["questions"]:
        q_num += 1
        story.append(Paragraph(f"第{q_num}题　{q['header']}", section_style))

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

    story.append(Spacer(1, 0.3*cm))

# Answer summary section at the end
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#ef9a9a"), spaceAfter=10))
story.append(Paragraph("答案汇总", title_style))
story.append(Paragraph("请完成所有题目后再翻阅答案", intro_style))
story.append(Spacer(1, 0.3*cm))

mod_summary_style = ParagraphStyle(
    "mod_summary", fontName=FONT, fontSize=12, leading=18,
    textColor=colors.HexColor("#0d47a1"), spaceBefore=8, spaceAfter=6,
    borderPad=4, backColor=colors.HexColor("#e3f2fd"),
    leftIndent=4, rightIndent=4,
)
col_widths = [W * 0.12, W * 0.12, W * 0.20, W * 0.20, W * 0.12]

for module in modules:
    story.append(Paragraph(f"{module['name']} — 答案", mod_summary_style))
    table_rows = []
    for i, row in enumerate(module["summary"]):
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
    story.append(Spacer(1, 0.4*cm))

doc.build(story)
print(f"PDF saved to: {output_path}")
