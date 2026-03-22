#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

# Register Chinese CID font
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
FONT = "STSong-Light"

output_path = "/Users/yuankun/KangrooMath/模块二_几何进阶练习题.pdf"

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

questions = [
    {
        "header": "题目一｜2014年 第18题",
        "desc": "正方形中心的方格被移除后，将其切成相等的几块纸片。请问哪一种形状是不可能得到的？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2014/q18.png",
        "point": "考察点：切割还原 — 在特殊缺口条件下，判断等面积分割后各块的可能形状。",
    },
    {
        "header": "题目二｜2019年 第18题",
        "desc": "如图所示，一个图形被切成3块。问原本完整的图形可能是哪一个？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2019/q18.png",
        "point": "考察点：切割还原 — 从碎片反推原始完整图形的轮廓与形状。",
    },
    {
        "header": "题目三｜2021年 第17题",
        "desc": "Mara 用以下5个碎片中的4个拼成了一个正方形。请问哪个形状没有被用到？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2021/q17.png",
        "point": "考察点：图形拼接 — 从5个候选碎片中排除多余一块，判断能组成正方形的组合。",
    },
    {
        "header": "题目四｜2022年 第18题",
        "desc": "下图展示了几块不同形状的草坪（带有网格点）。请问哪一块草坪的面积最小？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2022/q18.png",
        "point": "考察点：不规则图形面积比较 — 利用格点法比较各块不规则多边形的面积。",
    },
    {
        "header": "题目五｜2023年 第17题",
        "desc": "Elvis 有6个完全相同的三角形（如图所示）。用这6个三角形能拼出以下哪个图案？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2023/q17.png",
        "point": "考察点：图形拼接 — 用固定数量的相同形状拼合，判断哪些复杂图案可以实现。",
    },
    {
        "header": "题目六｜2024年 第19题",
        "desc": "在不重叠的情况下，用两块图形将残缺的大方格补全。请问是哪两块？",
        "image": "/Users/yuankun/KangrooMath/src/assets/exam-images/2024/q19.png",
        "point": "考察点：不重叠覆盖 — 从候选形状中选出恰好能无缝填补缺口的两块，不得重叠或超出边界。",
    },
]

story = []

# Title block
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("模块二 · 几何进阶练习题汇总", title_style))
story.append(Paragraph("专项主题：图形拼接、切割还原与不重叠覆盖", subtitle_style))
story.append(Paragraph("此类压轴题突破了基础的形状认知，重点考察图形的复杂拼接、切割还原以及不重叠覆盖。", intro_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#90caf9"), spaceAfter=10))

for q in questions:
    story.append(Paragraph(q["header"], section_style))
    story.append(Paragraph(q["desc"], desc_style))

    img_path = q["image"]
    if os.path.exists(img_path):
        from PIL import Image as PILImage
        with PILImage.open(img_path) as im:
            iw, ih = im.size
        # Scale to full width, preserve aspect ratio, max height 10cm
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

doc.build(story)
print(f"PDF saved to: {output_path}")
