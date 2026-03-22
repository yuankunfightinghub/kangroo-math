#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PIL import Image as PILImage
import os

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
FONT = "STSong-Light"

output_path = "/Users/yuankun/KangrooMath/src/assets/模块六_测量与单位_真题汇编.pdf"

doc = SimpleDocTemplate(
    output_path, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)
W = A4[0] - 4*cm

title_style = ParagraphStyle("title", fontName=FONT, fontSize=20, leading=28,
    alignment=TA_CENTER, textColor=colors.HexColor("#1a237e"), spaceAfter=6)
subtitle_style = ParagraphStyle("subtitle", fontName=FONT, fontSize=13, leading=18,
    alignment=TA_CENTER, textColor=colors.HexColor("#37474f"), spaceAfter=4)
intro_style = ParagraphStyle("intro", fontName=FONT, fontSize=11, leading=17,
    alignment=TA_CENTER, textColor=colors.HexColor("#546e7a"), spaceAfter=12)
section_style = ParagraphStyle("section", fontName=FONT, fontSize=14, leading=20,
    textColor=colors.HexColor("#0d47a1"), spaceBefore=14, spaceAfter=4,
    borderPad=4, backColor=colors.HexColor("#e3f2fd"), borderRadius=4,
    leftIndent=4, rightIndent=4)
desc_style = ParagraphStyle("desc", fontName=FONT, fontSize=11, leading=17,
    textColor=colors.HexColor("#212121"), spaceAfter=6, leftIndent=4)
point_style = ParagraphStyle("point", fontName=FONT, fontSize=10, leading=15,
    textColor=colors.HexColor("#00695c"), spaceAfter=4, leftIndent=4,
    backColor=colors.HexColor("#e8f5e9"), borderPad=3)
table_header_style = ParagraphStyle("table_header", fontName=FONT, fontSize=10, leading=14,
    textColor=colors.white, alignment=TA_CENTER)
table_cell_style = ParagraphStyle("table_cell", fontName=FONT, fontSize=10, leading=14,
    textColor=colors.HexColor("#212121"), alignment=TA_CENTER)

BASE = "/Users/yuankun/KangrooMath/src/assets/exam-images"

questions = [
    {
        "header": "题目一｜2025年 第12题",
        "desc": "狗和1只幼崽共14千克，狗和2只幼崽共18千克，这条狗多重？",
        "image": f"{BASE}/2025/q12.png",
        "point": "考察点：差值消元 — 两次称重相减，消去狗的重量得幼崽重量，再代入求狗重。解题思路：18-14=4（幼崽重量），狗=14-4=10千克。",
        "diff": "★★",
    },
    {
        "header": "题目二｜2024年 第7题",
        "desc": "每个数字用丝带做成，哪条丝带最长？",
        "image": f"{BASE}/2024/q07.png",
        "point": "考察点：长度比较 — 比较各数字形状所需丝带长度，判断最长的。解题思路：仔细比较每个数字图形的周长。",
        "diff": "★★",
    },
    {
        "header": "题目三｜2024年 第13题",
        "desc": "丝带绕1×1×2米的长方体盒子一圈，加上打结额外用的1米，计算总长度。",
        "image": f"{BASE}/2024/q13.png",
        "point": "考察点：三维立体的周长展开 — 正确识别绕行路径经过的面与边长组合，再加上1米结头。解题思路：计算绕行一圈的路径总长+1米。",
        "diff": "★★★",
    },
    {
        "header": "题目四｜2023年 第6题",
        "desc": "长蜡烛代表10岁，短蜡烛代表1岁，根据蛋糕上的蜡烛数判断爷爷多大？",
        "image": f"{BASE}/2023/q06.png",
        "point": "考察点：计数与单位换算 — 数出长短蜡烛各有几根，按10岁和1岁计算总年龄。解题思路：长蜡烛数×10 + 短蜡烛数×1。",
        "diff": "★",
    },
    {
        "header": "题目五｜2019年 第16题",
        "desc": "火车从Kang站早上6点出发，途经其他三个车站，不停车。哪条路线到达Aroo？",
        "image": f"{BASE}/2019/q16.png",
        "point": "考察点：时间推算与路程分配 — 根据出发时刻和各段用时累加，判断到达目的地的时刻与路线。",
        "diff": "★★★",
    },
    {
        "header": "题目六｜2019年 第15题",
        "desc": "地板铺满了相同形状的长方形瓷砖，每块瓷砖短边的长度是1米，带问号的边的长度是多少米？",
        "image": f"{BASE}/2019/q15.png",
        "point": "考察点：长度倍数推算 — 根据瓷砖铺设的行列规律，利用已知短边推算问号边的长度。解题思路：数出问号边方向上排了几块瓷砖，乘以长边长度。",
        "diff": "★★★",
    },
    {
        "header": "题目七｜2018年 第4题",
        "desc": "这张披萨被切成了大小相同的若干份，请问已经有几片被拿走了？",
        "image": f"{BASE}/2018/q04.png",
        "point": "考察点：分数直觉与缺失计数 — 通过等分切割判断总份数与缺失份数。解题思路：数出总切割数与剩余片数之差。",
        "diff": "★",
    },
    {
        "header": "题目八｜2017年 第14题",
        "desc": "现在是一点半，请问两个半小时之前是什么时间？",
        "image": f"{BASE}/2017/q14.png",
        "point": "考察点：时间倒推 — 在模拟时钟上减去2小时30分，找到正确时刻。解题思路：1:30 - 2:30 = 11:00（前一天）。",
        "diff": "★★",
    },
    {
        "header": "题目九｜2016年 第6题",
        "desc": "派传单到25号至57号的房子，共需要派多少间？",
        "image": f"{BASE}/2016/q06.png",
        "point": "考察点：区间计数 — 注意包含两端点，共有57-25+1=33间。解题思路：终点编号-起点编号+1（含首尾）。",
        "diff": "★★",
    },
    {
        "header": "题目十｜2016年 第10题",
        "desc": "Kanga现在1岁3个月，再过几个月就满2岁？",
        "image": f"{BASE}/2016/q10.png",
        "point": "考察点：时间间隔计算 — 1岁3个月=15个月，2岁=24个月，24-15=9个月。解题思路：先统一换算为月份，再相减。",
        "diff": "★★",
    },
    {
        "header": "题目十一｜2015年 第9题",
        "desc": "小J用半小时走了一半路，从学校到家全程需要多长时间？",
        "image": f"{BASE}/2015/q09.png",
        "point": "考察点：路程比例与时间推算 — 半程=半小时，全程=2×半小时=1小时。解题思路：等速行走，路程翻倍则时间翻倍。",
        "diff": "★★",
    },
    {
        "header": "题目十二｜2015年 第17题",
        "desc": "11个旗子等距排在直线跑道上，第一个在起点，最后一个在终点，每个间距8米，跑道多长？",
        "image": f"{BASE}/2015/q17.png",
        "point": "考察点：植树间隔原理 — n个旗子之间只有(n-1)个间距，总长=(n-1)×间距=(11-1)×8=80米。常见陷阱：误用11×8=88米。",
        "diff": "★★",
    },
    {
        "header": "题目十三｜2014年 第8题",
        "desc": "天平上需要多少只鸭子才能和鳄鱼平衡？",
        "image": f"{BASE}/2014/q08.png",
        "point": "考察点：天平等量关系 — 利用已知等量关系列式，代换求解。解题思路：根据天平图建立等式，逐步推算鸭子数量。",
        "diff": "★★",
    },
    {
        "header": "题目十四｜2013年 第9题",
        "desc": "George有2只体重相同的猫，George自己重30千克，根据天平图，一只猫多重？",
        "image": f"{BASE}/2013/q09.png",
        "point": "考察点：天平平衡推算 — 读懂天平图建立等式，用George的体重和猫的数量推算单只猫的重量。",
        "diff": "★★",
    },
]

summary_data = [
    ["年份", "题号", "题目要点", "解题方法", "难度"],
    ["2025", "Q12", "狗和幼崽称重求狗重", "差值消元", "★★"],
    ["2024", "Q7",  "数字丝带哪条最长", "长度比较", "★★"],
    ["2024", "Q13", "丝带绕盒子总长", "周长展开", "★★★"],
    ["2023", "Q6",  "蜡烛数判断爷爷年龄", "计数换算", "★"],
    ["2019", "Q16", "火车路线时间推算", "时间累加", "★★★"],
    ["2019", "Q15", "瓷砖问号边长度", "倍数推算", "★★★"],
    ["2018", "Q4",  "披萨缺失片数", "分数计数", "★"],
    ["2017", "Q14", "时钟倒推两个半小时", "时间倒推", "★★"],
    ["2016", "Q6",  "派传单区间计数", "含端点计数", "★★"],
    ["2016", "Q10", "Kanga距2岁月数", "月份换算", "★★"],
    ["2015", "Q9",  "半程半小时推全程", "比例推算", "★★"],
    ["2015", "Q17", "11旗子间距求总长", "植树间隔", "★★"],
    ["2014", "Q8",  "天平鸭子平衡鳄鱼", "等量关系", "★★"],
    ["2013", "Q9",  "天平推算猫的重量", "天平代换", "★★"],
]

story = []
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("模块六 · 测量与单位  真题汇编", title_style))
story.append(Paragraph("共 14 题 · 涵盖重量、时间、长度、植树间隔等核心考点", subtitle_style))
story.append(Paragraph(
    "每年约2-3题，与生活联系最紧密。重点考察天平推算、时间倒推、植树间隔等思维陷阱。",
    intro_style
))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#90caf9"), spaceAfter=10))

for q in questions:
    story.append(Paragraph(q["header"], section_style))
    story.append(Paragraph(q["desc"], desc_style))
    img_path = q["image"]
    if os.path.exists(img_path):
        with PILImage.open(img_path) as im:
            iw, ih = im.size
        ratio = ih / iw
        img_w = W
        img_h = img_w * ratio
        max_h = 10 * cm
        if img_h > max_h:
            img_h = max_h
            img_w = img_h / ratio
        story.append(Image(img_path, width=img_w, height=img_h))
    else:
        story.append(Paragraph(f"[图片未找到: {img_path}]", desc_style))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(q["point"], point_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#b0bec5"), spaceAfter=8, spaceBefore=8))

# Summary table
story.append(Spacer(1, 0.5*cm))
summary_section_style = ParagraphStyle("summary_section", fontName=FONT, fontSize=14, leading=20,
    textColor=colors.HexColor("#0d47a1"), spaceBefore=10, spaceAfter=8,
    borderPad=4, backColor=colors.HexColor("#e3f2fd"), borderRadius=4,
    leftIndent=4, rightIndent=4)
story.append(Paragraph("汇总表｜十四题核心考点一览", summary_section_style))

col_widths = [W*0.09, W*0.09, W*0.38, W*0.28, W*0.16]
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
