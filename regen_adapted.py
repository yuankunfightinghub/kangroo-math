#!/usr/bin/env python3
"""Regenerate adapted question images with embedded original exam figures."""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

FONT_PATH = "/System/Library/Fonts/PingFang.ttc"
OUTPUT_DIR = "/Users/yuankun/KangrooMath/src/assets/adapted-images"
EXAM_BASE = "/Users/yuankun/KangrooMath/src/assets/exam-images"

IMG_W = 1600
PADDING = 60
ORANGE = (255, 140, 0)
LIGHT_ORANGE = (255, 200, 100)
BG = (255, 255, 255)
GRAY = (130, 130, 130)
DARK = (40, 40, 40)
SEPARATOR_COLOR = (220, 220, 220)

OPTION_COLORS = [
    (66, 133, 244),   # A - blue
    (52, 168, 83),    # B - green
    (234, 67, 53),    # C - red
    (251, 188, 4),    # D - yellow
    (156, 39, 176),   # E - purple
]

def load_font(size, bold=False):
    idx = 1 if bold else 0
    return ImageFont.truetype(FONT_PATH, size, index=idx)

def draw_rounded_rect(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.ellipse([x0, y0, x0 + 2*radius, y0 + 2*radius], fill=fill)
    draw.ellipse([x1 - 2*radius, y0, x1, y0 + 2*radius], fill=fill)
    draw.ellipse([x0, y1 - 2*radius, x0 + 2*radius, y1], fill=fill)
    draw.ellipse([x1 - 2*radius, y1 - 2*radius, x1, y1], fill=fill)

def draw_circle_badge(draw, cx, cy, r, color, text, font):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw // 2, cy - th // 2 - bbox[1]), text, font=font, fill=(255, 255, 255))

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width."""
    words = text
    lines = []
    current = ""
    for char in words:
        test = current + char
        bbox = font.getbbox(test)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = char
        else:
            current = test
    if current:
        lines.append(current)
    return lines

def generate_image(qid, star, category, text, options, exam_img_path):
    font_num = load_font(36, bold=True)
    font_cat = load_font(28)
    font_star = load_font(30)
    font_text = load_font(32)
    font_opt = load_font(30)
    font_label = load_font(26)
    font_ref = load_font(24)

    # First pass: calculate height
    # We'll build on a tall canvas then crop
    canvas_h = 3000
    img = Image.new("RGB", (IMG_W, canvas_h), BG)
    draw = ImageDraw.Draw(img)

    y = 0

    # --- Top bar ---
    bar_h = 90
    draw.rectangle([0, 0, IMG_W, bar_h], fill=ORANGE)
    y = bar_h

    # --- Header row: badge + stars + category ---
    y += 24

    # Question number badge
    badge_text = qid.upper()
    bfont = load_font(34, bold=True)
    bbox = bfont.getbbox(badge_text)
    bw = bbox[2] - bbox[0] + 32
    bh = 54
    bx = PADDING
    draw_rounded_rect(draw, [bx, y, bx + bw, y + bh], 12, ORANGE)
    draw.text((bx + 16, y + 8), badge_text, font=bfont, fill=(255, 255, 255))

    # Stars
    star_x = bx + bw + 20
    star_y = y + 10
    stars_str = "★" * star + "☆" * (5 - star)
    draw.text((star_x, star_y), stars_str, font=font_star, fill=ORANGE)
    sbbox = font_star.getbbox(stars_str)
    star_end_x = star_x + sbbox[2] - sbbox[0] + 20

    # Category tag
    cat_bbox = font_cat.getbbox(category)
    cat_w = cat_bbox[2] - cat_bbox[0] + 24
    cat_h = 44
    cat_x = star_end_x
    cat_y = y + 5
    draw_rounded_rect(draw, [cat_x, cat_y, cat_x + cat_w, cat_y + cat_h], 10, (240, 240, 240))
    draw.text((cat_x + 12, cat_y + 6), category, font=font_cat, fill=(80, 80, 80))

    y += bh + 24

    # --- Separator ---
    draw.line([PADDING, y, IMG_W - PADDING, y], fill=SEPARATOR_COLOR, width=2)
    y += 20

    # --- Question text ---
    max_text_w = IMG_W - 2 * PADDING
    lines = wrap_text(text, font_text, max_text_w, draw)
    line_h = font_text.getbbox("A")[3] + 10
    for line in lines:
        draw.text((PADDING, y), line, font=font_text, fill=DARK)
        y += line_h + 4
    y += 16

    # --- Separator ---
    draw.line([PADDING, y, IMG_W - PADDING, y], fill=SEPARATOR_COLOR, width=2)
    y += 20

    # --- Reference label ---
    ref_text = "（参考原图）"
    ref_bbox = font_ref.getbbox(ref_text)
    ref_w = ref_bbox[2] - ref_bbox[0]
    draw.text(((IMG_W - ref_w) // 2, y), ref_text, font=font_ref, fill=GRAY)
    y += ref_bbox[3] - ref_bbox[1] + 12

    # --- Embed exam image ---
    exam_img = Image.open(exam_img_path).convert("RGBA")
    ew, eh = exam_img.size
    max_embed_w = IMG_W - 2 * PADDING
    max_embed_h = 500
    scale = min(max_embed_w / ew, max_embed_h / eh, 1.0)
    new_ew = int(ew * scale)
    new_eh = int(eh * scale)
    exam_img_resized = exam_img.resize((new_ew, new_eh), Image.LANCZOS)

    # Convert to RGB with white background
    exam_bg = Image.new("RGB", (new_ew, new_eh), (255, 255, 255))
    exam_bg.paste(exam_img_resized, mask=exam_img_resized.split()[3] if exam_img_resized.mode == 'RGBA' else None)

    ex = (IMG_W - new_ew) // 2
    img.paste(exam_bg, (ex, y))
    y += new_eh + 20

    # --- Separator ---
    draw.line([PADDING, y, IMG_W - PADDING, y], fill=SEPARATOR_COLOR, width=2)
    y += 20

    # --- Options ---
    opt_r = 22
    opt_line_h = opt_r * 2 + 14
    for i, opt_text in enumerate(options):
        letter = chr(ord('A') + i)
        color = OPTION_COLORS[i]
        cx = PADDING + opt_r
        cy = y + opt_r
        draw_circle_badge(draw, cx, cy, opt_r, color, letter, font_opt)
        draw.text((PADDING + opt_r * 2 + 14, y + 6), opt_text, font=font_opt, fill=DARK)
        y += opt_line_h

    y += PADDING

    # Crop to actual height
    result = img.crop((0, 0, IMG_W, y))
    return result

questions = [
    {
        "qid": "w01", "star": 1, "category": "立体图形·格子计数",
        "text": "小明在方格纸上浇花，不小心把水浇到了旁边的格子上。如图所示，水从水桶溢出后，共沾湿了多少个完整的小方格？",
        "options": ["14", "16", "18", "19", "20"],
        "exam_img": f"{EXAM_BASE}/2022/q08.png"
    },
    {
        "qid": "w02", "star": 1, "category": "立体图形·缺失计数",
        "text": "邻居家正在用相同的小砖块砌一道圆弧形花坛挡墙，如图所示，墙还没砌完，有几个位置空着。请问还缺几块这样形状的砖才能砌完？",
        "options": ["6", "7", "8", "9", "10"],
        "exam_img": f"{EXAM_BASE}/2017/q06.png"
    },
    {
        "qid": "w05", "star": 1, "category": "图形计数·嵌套三角形",
        "text": "爸爸给小华做了一个由三角形拼成的风筝图案，如图所示。请问这个风筝图案里，一共有多少个三角形？（包括大的、小的、以及由小三角形拼成的大三角形，全部都要数进去）",
        "options": ["4", "5", "6", "7", "8"],
        "exam_img": f"{EXAM_BASE}/2015/q02.png"
    },
    {
        "qid": "w08", "star": 1, "category": "图形组合·计数",
        "text": "园艺师傅用特殊的五瓣花形砖铺花坛，左图是一块花形砖的形状，右图是用这种砖铺成的一小块花坛图案。请问右图中一共用了多少块花形砖？",
        "options": ["5", "6", "7", "8", "9"],
        "exam_img": f"{EXAM_BASE}/2018/q03.png"
    },
    {
        "qid": "w09", "star": 1, "category": "立体图形·格子缺失",
        "text": "奶奶织了一块5×5方格的毛毯，但因为中间有几处断线，部分格子没有织出来（如图，空白格子表示没织出来）。请问这块毛毯里有多少个小方格【没有】织出来？",
        "options": ["6", "7", "8", "9", "10"],
        "exam_img": f"{EXAM_BASE}/2014/q07.png"
    },
    {
        "qid": "w10", "star": 2, "category": "平面图形·旋转规律",
        "text": "小陀螺比赛中，裁判给一个风车形状的陀螺拍摄了旋转中的3张照片（每次旋转角度相同）。照片1、2、3如图所示。请问第6次旋转后，陀螺看起来是哪种样子？",
        "options": ["样子A", "样子B", "样子C", "样子D", "样子E"],
        "exam_img": f"{EXAM_BASE}/2017/q11.png"
    },
    {
        "qid": "w11", "star": 2, "category": "平面图形·剪拼",
        "text": "妈妈把一块正方形饼干按如图所示切成了4块。下面哪种形状【不能】用这4块饼干拼成？（饼干块可以翻转和旋转，但不能重叠）",
        "options": ["长方形", "平行四边形", "三角形", "T形", "L形"],
        "exam_img": f"{EXAM_BASE}/2014/q11.png"
    },
    {
        "qid": "w12", "star": 2, "category": "立体图形·表面积",
        "text": "小朋友用5个完全相同的小木块粘在一起做礼物盒模型，要给模型外表面全部涂上颜色。下面哪种摆法需要涂色的面【最少】？（粘在一起的面不用涂）",
        "options": ["一排平放", "正方体堆叠", "L形摆放", "十字形", "塔形竖放"],
        "exam_img": f"{EXAM_BASE}/2019/q14.png"
    },
    {
        "qid": "w13", "star": 2, "category": "逻辑推理·叠放顺序",
        "text": "图书馆书架上有8本书叠放在一起，第2本在最下面，第7本在最上面。从叠放图可以看出各书的压盖关系。请问第4层（从下往上数第4本）是哪本书？",
        "options": ["1号", "3号", "4号", "5号", "6号"],
        "exam_img": f"{EXAM_BASE}/2014/q15.png"
    },
    {
        "qid": "w14", "star": 2, "category": "路径方向·折纸剪切",
        "text": "小明把一张纸对折两次，然后剪了两刀，如图所示。把纸展开后，这张纸被分成了多少张？",
        "options": ["3", "4", "5", "6", "8"],
        "exam_img": f"{EXAM_BASE}/2019/q12.png"
    },
    {
        "qid": "w17", "star": 2, "category": "数数策略·重叠计数",
        "text": "客厅方格地板（10×10格）上铺了5块不同颜色的长方形地毯，相互有重叠。请问有多少个方格同时被【至少3块】地毯压住？（地毯位置如图所示）",
        "options": ["2", "3", "4", "5", "6"],
        "exam_img": f"{EXAM_BASE}/2025/q10.png"
    },
    {
        "qid": "w22", "star": 2, "category": "度量单位·空间路径长度",
        "text": "邮递员要在一个长2米、宽1米、高1米的纸箱外面绑一条丝带。丝带从底部中心出发，绕箱子一圈后回到顶部中心（如图所示），打结处再额外用1米丝带。请问丝带总共需要多少米？",
        "options": ["7", "8", "9", "10", "11"],
        "exam_img": f"{EXAM_BASE}/2024/q13.png"
    },
    {
        "qid": "w26", "star": 5, "category": "路径方向·约束路径计数",
        "text": "一只蚂蚁在六边形蜂巢格子网上行走，只能经过【白色格子】，从C格走到D格，每个格子只能经过一次。请问共有多少种不同的走法？（格子布局如图所示）",
        "options": ["4", "5", "6", "7", "8"],
        "exam_img": f"{EXAM_BASE}/2020/q19.png"
    },
    {
        "qid": "w27", "star": 5, "category": "路径方向·方向约束路线",
        "text": "小机器人只能【前进或右转】，不能左转也不能后退。从黑点出发，下面5条路线中，哪条是小机器人【可以】走完的？（路线图如图所示）",
        "options": ["路线A", "路线B", "路线C", "路线D", "路线E"],
        "exam_img": f"{EXAM_BASE}/2022/q23.png"
    },
    {
        "qid": "w31", "star": 5, "category": "平面图形·不规则面积",
        "text": "城市规划图上有5块绿地（A~E），每块绿地的边界都由方格线组成（如图）。请问哪块绿地的面积【最大】？",
        "options": ["A绿地", "B绿地", "C绿地", "D绿地", "E绿地"],
        "exam_img": f"{EXAM_BASE}/2022/q18.png"
    },
    {
        "qid": "w32", "star": 5, "category": "平面图形·图形拼接",
        "text": "小明有8个完全相同的等腰直角三角形（如图左所示）。他用全部8个三角形拼出一个完整图案（不重叠、不留空、不剪切）。下面哪个图案是【不可能】拼出来的？",
        "options": ["大正方形", "长方形", "六边形", "十字形", "平行四边形"],
        "exam_img": f"{EXAM_BASE}/2023/q17.png"
    },
]

for q in questions:
    qid = q["qid"]
    exam_path = q["exam_img"]
    if not os.path.exists(exam_path):
        print(f"WARNING: missing exam image for {qid}: {exam_path}")
        continue
    print(f"Generating {qid}...")
    img = generate_image(
        qid=qid,
        star=q["star"],
        category=q["category"],
        text=q["text"],
        options=q["options"],
        exam_img_path=exam_path
    )
    out_path = os.path.join(OUTPUT_DIR, f"{qid}.png")
    img.save(out_path)
    print(f"  Saved {out_path} ({img.size})")

print("Done!")
