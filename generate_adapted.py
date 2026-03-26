#!/usr/bin/env python3
"""
Generate adapted math question images with extracted figures from exam images.
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import textwrap

BASE_DIR = "/Users/yuankun/KangrooMath"
OUTPUT_DIR = os.path.join(BASE_DIR, "src/assets/adapted-images")

# Color palette
ORANGE = (255, 140, 0)
LIGHT_ORANGE = (255, 248, 235)
WHITE = (255, 255, 255)
DARK_GRAY = (50, 50, 50)
MID_GRAY = (120, 120, 120)
LIGHT_GRAY = (220, 220, 220)
DIVIDER_COLOR = (230, 230, 230)
OPTION_COLORS = [
    (255, 100, 100),   # A - red
    (255, 160, 60),    # B - orange
    (80, 180, 80),     # C - green
    (60, 140, 220),    # D - blue
    (160, 100, 200),   # E - purple
]
STAR_FILLED = (255, 200, 0)
STAR_EMPTY = (200, 200, 200)

IMG_WIDTH = 1600
PAD = 60

def get_font(size, bold=False):
    """Try to load a CJK-capable font."""
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Supplemental/PingFang.ttc",
        "/Library/Fonts/Arial Unicode MS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    return ImageFont.load_default()

def draw_star(draw, cx, cy, r, filled):
    """Draw a 5-pointed star centered at (cx, cy) with outer radius r."""
    import math
    points = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        radius = r if i % 2 == 0 else r * 0.4
        points.append((cx + radius * math.cos(angle), cy - radius * math.sin(angle)))
    color = STAR_FILLED if filled else STAR_EMPTY
    draw.polygon(points, fill=color)

def draw_text_wrapped(draw, text, x, y, max_width, font, fill, line_spacing=10):
    """Draw wrapped text, return final y position."""
    # Estimate chars per line
    try:
        bbox = font.getbbox("测")
        char_w = bbox[2] - bbox[0]
    except:
        char_w = font.size

    chars_per_line = max(1, int(max_width / char_w))

    # Split by explicit newlines first, then wrap each segment
    segments = text.split('\n')
    lines = []
    for seg in segments:
        if len(seg) <= chars_per_line:
            lines.append(seg)
        else:
            # Simple char-based wrap
            while len(seg) > chars_per_line:
                lines.append(seg[:chars_per_line])
                seg = seg[chars_per_line:]
            if seg:
                lines.append(seg)

    current_y = y
    for line in lines:
        try:
            bbox = font.getbbox(line)
            line_h = bbox[3] - bbox[1]
        except:
            line_h = font.size + 4
        draw.text((x, current_y), line, font=font, fill=fill)
        current_y += line_h + line_spacing
    return current_y

def extract_figure(exam_path, crop_box=None):
    """
    Extract the figure/diagram from an exam image.
    crop_box: (left, top, right, bottom) as fractions of image size, or None for auto-detect.
    Returns a PIL Image of the figure.
    """
    img = Image.open(exam_path).convert("RGB")
    w, h = img.size

    if crop_box is not None:
        # Use manual crop coordinates (as pixel values or fractions)
        # If all values are <= 1.0, treat as fractions; otherwise treat as pixels
        if all(isinstance(v, float) and v <= 1.0 for v in crop_box):
            # Fractions
            left = int(crop_box[0] * w)
            top = int(crop_box[1] * h)
            right = int(crop_box[2] * w)
            bottom = int(crop_box[3] * h)
        else:
            left, top, right, bottom = int(crop_box[0]), int(crop_box[1]), int(crop_box[2]), int(crop_box[3])
        return img.crop((left, top, right, bottom))

    # Auto-detect: find non-white bounding box
    gray = np.array(img.convert("L"))
    mask = gray < 240
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)

    row_indices = np.where(rows)[0]
    col_indices = np.where(cols)[0]

    if len(row_indices) == 0 or len(col_indices) == 0:
        return img

    top_row = row_indices[0]
    bottom_row = row_indices[-1]
    left_col = col_indices[0]
    right_col = col_indices[-1]

    # Take bottom 55% of the non-white area (skip question text at top)
    content_h = bottom_row - top_row
    figure_top = top_row + int(content_h * 0.45)

    return img.crop((left_col, figure_top, right_col, bottom_row))

def scale_figure(fig_img, max_w=1400, max_h=500):
    """Scale figure to fit within max dimensions, upscale if too small."""
    w, h = fig_img.size

    # Upscale if too small
    if w < 400:
        scale = 400 / w
        w = int(w * scale)
        h = int(h * scale)
        fig_img = fig_img.resize((w, h), Image.LANCZOS)

    # Downscale if too large
    if w > max_w or h > max_h:
        ratio = min(max_w / w, max_h / h)
        w = int(w * ratio)
        h = int(h * ratio)
        fig_img = fig_img.resize((w, h), Image.LANCZOS)

    return fig_img

def generate_image(output_path, w_num, stars, category, question_text, options, figure_img):
    """Generate the adapted question image."""
    font_question = get_font(32)
    font_option = get_font(30)
    font_badge = get_font(28, bold=True)
    font_label = get_font(22)
    font_cat = get_font(22)

    # --- First pass: measure total height ---
    # We'll build the layout by computing heights

    header_h = 80       # orange bar + header row
    divider_h = 2
    question_area_h = 0

    # Measure question text height
    max_text_w = IMG_WIDTH - PAD * 2
    try:
        bbox = font_question.getbbox("测")
        char_w = bbox[2] - bbox[0]
        char_h = bbox[3] - bbox[1]
    except:
        char_w = 32
        char_h = 40

    chars_per_line = max(1, int(max_text_w / char_w))
    lines = []
    text = question_text
    segments = text.split('\n')
    for seg in segments:
        while len(seg) > chars_per_line:
            lines.append(seg[:chars_per_line])
            seg = seg[chars_per_line:]
        lines.append(seg)

    question_h = len(lines) * (char_h + 10)

    # Figure area
    fig_w, fig_h = figure_img.size
    label_h = 40
    fig_area_h = label_h + 20 + fig_h + 40  # label + padding + figure + padding

    # Options area
    try:
        opt_bbox = font_option.getbbox("测")
        opt_h = opt_bbox[3] - opt_bbox[1]
    except:
        opt_h = 36

    options_h = len(options) * (opt_h + 18) + 20

    total_h = (
        PAD // 2 +      # top
        8 +             # orange bar
        10 +
        60 +            # header row
        15 +
        divider_h +
        20 +
        question_h +
        20 +
        divider_h +
        fig_area_h +
        divider_h +
        options_h +
        PAD
    )

    # --- Create image ---
    img = Image.new("RGB", (IMG_WIDTH, total_h), WHITE)
    draw = ImageDraw.Draw(img)

    y = 0

    # Orange top bar
    draw.rectangle([0, y, IMG_WIDTH, y + 8], fill=ORANGE)
    y += 8 + 10

    # Header row: W-badge + stars + category
    badge_r = 28
    badge_cx = PAD + badge_r
    badge_cy = y + badge_r + 5
    draw.ellipse([badge_cx - badge_r, badge_cy - badge_r,
                  badge_cx + badge_r, badge_cy + badge_r], fill=ORANGE)

    w_text = f"W{w_num:02d}"
    try:
        tb = font_badge.getbbox(w_text)
        tw = tb[2] - tb[0]
        th = tb[3] - tb[1]
    except:
        tw, th = 50, 30
    draw.text((badge_cx - tw // 2, badge_cy - th // 2), w_text, font=font_badge, fill=WHITE)

    # Stars
    star_x = badge_cx + badge_r + 20
    star_y = badge_cy
    for i in range(5):
        filled = i < stars
        draw_star(draw, star_x + i * 30, star_y, 12, filled)

    # Category tag
    cat_x = star_x + 5 * 30 + 20
    try:
        cb = font_cat.getbbox(category)
        cw = cb[2] - cb[0]
        ch = cb[3] - cb[1]
    except:
        cw, ch = len(category) * 18, 28

    cat_pad = 10
    tag_rect = [cat_x, badge_cy - ch // 2 - cat_pad, cat_x + cw + cat_pad * 2, badge_cy + ch // 2 + cat_pad]
    draw.rounded_rectangle(tag_rect, radius=8, outline=ORANGE, width=2)
    draw.text((cat_x + cat_pad, badge_cy - ch // 2), category, font=font_cat, fill=ORANGE)

    y = badge_cy + badge_r + 15

    # Divider
    draw.rectangle([PAD, y, IMG_WIDTH - PAD, y + divider_h], fill=DIVIDER_COLOR)
    y += divider_h + 20

    # Question text
    y = draw_text_wrapped(draw, question_text, PAD, y, max_text_w, font_question, DARK_GRAY, line_spacing=10)
    y += 20

    # Divider
    draw.rectangle([PAD, y, IMG_WIDTH - PAD, y + divider_h], fill=DIVIDER_COLOR)
    y += divider_h

    # Figure label
    label = "图示"
    try:
        lb = font_label.getbbox(label)
        lw = lb[2] - lb[0]
    except:
        lw = 40
    draw.text(((IMG_WIDTH - lw) // 2, y + 8), label, font=font_label, fill=MID_GRAY)
    y += label_h

    # Figure image (centered, white background frame)
    fig_pad = 20
    fig_x = (IMG_WIDTH - fig_w) // 2

    # Paste figure
    if figure_img.mode == "RGBA":
        img.paste(figure_img, (fig_x, y + fig_pad), figure_img)
    else:
        img.paste(figure_img, (fig_x, y + fig_pad))
    y += fig_pad + fig_h + 20

    # Divider
    draw.rectangle([PAD, y, IMG_WIDTH - PAD, y + divider_h], fill=DIVIDER_COLOR)
    y += divider_h + 10

    # Options
    for i, (letter, opt_text) in enumerate(options):
        color = OPTION_COLORS[i]
        # Circle badge
        cr = 18
        cx = PAD + cr
        cy = y + cr + 5
        draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=color)

        try:
            lb = font_option.getbbox(letter)
            lw = lb[2] - lb[0]
            lh = lb[3] - lb[1]
        except:
            lw, lh = 18, 28
        draw.text((cx - lw // 2, cy - lh // 2), letter, font=font_option, fill=WHITE)

        draw.text((PAD + cr * 2 + 15, cy - lh // 2), opt_text, font=font_option, fill=DARK_GRAY)
        y += opt_h + 18

    y += PAD

    # Trim to actual content height
    img = img.crop((0, 0, IMG_WIDTH, y))
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

# ============================================================
# Question data
# ============================================================

questions = [
    {
        "id": "w01", "num": 1, "stars": 1, "category": "立体图形·格子计数",
        "text": "小明在方格纸上浇花，不小心把水浇到了旁边的格子上。如图所示，水从水桶溢出后，共沾湿了多少个完整的小方格？",
        "options": [("A","14"),("B","16"),("C","18"),("D","19"),("E","20")],
        "exam": "src/assets/exam-images/2022/q08.png",
        # Grid+blob figure in right portion, cols 1000-1295, rows 18-250
        "crop": (1000, 18, 1295, 250),
    },
    {
        "id": "w02", "num": 2, "stars": 1, "category": "平面图形·格子计数",
        "text": "邻居家正在用相同的小砖块砌一道圆弧形花坛挡墙，如图所示，墙还没砌完，有几个位置空着。请问还缺几块这样形状的砖才能砌完？",
        "options": [("A","6"),("B","7"),("C","8"),("D","9"),("E","10")],
        "exam": "src/assets/exam-images/2017/q06.png",
        # Igloo figure, skip top text (fraction-based)
        "crop": (0.05, 0.28, 0.95, 0.88),
    },
    {
        "id": "w05", "num": 5, "stars": 1, "category": "平面图形·数三角形",
        "text": "爸爸给小华做了一个由三角形拼成的风筝图案，如图所示。请问这个风筝图案里，一共有多少个三角形？（包括大的、小的、以及由小三角形拼成的大三角形，全部都要数进去）",
        "options": [("A","4"),("B","5"),("C","6"),("D","7"),("E","8")],
        "exam": "src/assets/exam-images/2015/q02.png",
        # Girl figure (triangles in dress/body), centered, rows 558-808, cols 1/3 to 2/3
        # Use pixel coords: x=408,y=558 to x=816,y=808
        "crop": (408, 558, 816, 808),
    },
    {
        "id": "w08", "num": 8, "stars": 1, "category": "平面图形·铺砖计数",
        "text": "园艺师傅用特殊的五瓣花形砖铺花坛，左图是一块花形砖的形状，右图是用这种砖铺成的一小块花坛图案。请问右图中一共用了多少块花形砖？",
        "options": [("A","5"),("B","6"),("C","7"),("D","8"),("E","9")],
        "exam": "src/assets/exam-images/2018/q03.png",
        # Both stars (single + multi-petal), rows 325-475
        "crop": (0, 325, 1489, 475),
    },
    {
        "id": "w09", "num": 9, "stars": 1, "category": "平面图形·格子计数",
        "text": "奶奶织了一块5×5方格的毛毯，但因为中间有几处断线，部分格子没有织出来（如图，空白格子表示没织出来）。请问这块毛毯里有多少个小方格【没有】织出来？",
        "options": [("A","6"),("B","7"),("C","8"),("D","9"),("E","10")],
        "exam": "src/assets/exam-images/2014/q07.png",
        # Staircase grid figure in lower-left area
        "crop": (0.0, 0.35, 0.5, 0.82),
    },
    {
        "id": "w10", "num": 10, "stars": 2, "category": "平面图形·旋转规律",
        "text": "小陀螺比赛中，裁判给一个风车形状的陀螺拍摄了旋转中的3张照片（每次旋转角度相同）。照片1、2、3如图所示。请问第6次旋转后，陀螺看起来是哪种样子？",
        "options": [("A","样子A"),("B","样子B"),("C","样子C"),("D","样子D"),("E","样子E")],
        "exam": "src/assets/exam-images/2017/q11.png",
        # Spinner shapes span middle to lower portion
        "crop": (0.0, 0.2, 1.0, 0.82),
    },
    {
        "id": "w11", "num": 11, "stars": 2, "category": "平面图形·拼图",
        "text": "妈妈把一块正方形饼干按如图所示切成了4块。下面哪种形状【不能】用这4块饼干拼成？（饼干块可以翻转和旋转，但不能重叠）",
        "options": [("A","长方形"),("B","平行四边形"),("C","三角形"),("D","T形"),("E","L形")],
        "exam": "src/assets/exam-images/2014/q11.png",
        # Cut square + 5 shape options
        "crop": (0.0, 0.2, 1.0, 0.85),
    },
    {
        "id": "w12", "num": 12, "stars": 2, "category": "立体图形·涂色面数",
        "text": "小朋友用5个完全相同的小木块粘在一起做礼物盒模型，要给模型外表面全部涂上颜色。下面哪种摆法需要涂色的面【最少】？（粘在一起的面不用涂）",
        "options": [("A","一排平放"),("B","正方体堆叠"),("C","L形摆放"),("D","十字形"),("E","塔形竖放")],
        "exam": "src/assets/exam-images/2019/q14.png",
        # 3D blocks figure, rows 220-550 (skip text header)
        "crop": (0, 220, 1488, 550),
    },
    {
        "id": "w13", "num": 13, "stars": 2, "category": "逻辑推理·叠放顺序",
        "text": "图书馆书架上有8本书叠放在一起，第2本在最下面，第7本在最上面。从叠放图可以看出各书的压盖关系。请问第4层（从下往上数第4本）是哪本书？",
        "options": [("A","1号"),("B","3号"),("C","4号"),("D","5号"),("E","6号")],
        "exam": "src/assets/exam-images/2014/q15.png",
        # Crossing sticks figure, rows 300-740, cols 0-900
        "crop": (0, 300, 900, 740),
    },
    {
        "id": "w14", "num": 14, "stars": 2, "category": "平面图形·折纸剪纸",
        "text": "小明把一张纸对折两次，然后剪了两刀，如图所示。把纸展开后，这张纸被分成了多少张？",
        "options": [("A","3"),("B","4"),("C","5"),("D","6"),("E","8")],
        "exam": "src/assets/exam-images/2019/q12.png",
        # Paper folding diagrams (fold → fold → cut), rows 920-1115
        "crop": (0, 920, 1190, 1115),
    },
    {
        "id": "w17", "num": 17, "stars": 2, "category": "数数策略·重叠计数",
        "text": "客厅方格地板（10×10格）上铺了5块不同颜色的长方形地毯，相互有重叠。请问有多少个方格同时被【至少3块】地毯压住？（地毯位置如图所示）",
        "options": [("A","2"),("B","3"),("C","4"),("D","5"),("E","6")],
        "exam": "src/assets/exam-images/2025/q10.png",
        # Overlapping colored rugs on grid, tight crop to content area
        "crop": (185, 270, 825, 820),
    },
    {
        "id": "w22", "num": 22, "stars": 2, "category": "空间想象·路径展开",
        "text": "邮递员要在一个长2米、宽1米、高1米的纸箱外面绑一条丝带。丝带从底部中心出发，绕箱子一圈后回到顶部中心（如图所示），打结处再额外用1米丝带。请问丝带总共需要多少米？",
        "options": [("A","7"),("B","8"),("C","9"),("D","10"),("E","11")],
        "exam": "src/assets/exam-images/2024/q13.png",
        # Gift box with ribbon, rows 405-785, trim sides and text
        "crop": (100, 405, 1686, 785),
    },
    {
        "id": "w26", "num": 26, "stars": 5, "category": "路径迷宫·计数",
        "text": "一只蚂蚁在六边形蜂巢格子网上行走，只能经过【白色格子】，从C格走到D格，每个格子只能经过一次。请问共有多少种不同的走法？（格子布局如图所示）",
        "options": [("A","4"),("B","5"),("C","6"),("D","7"),("E","8")],
        "exam": "src/assets/exam-images/2020/q19.png",
        # Honeycomb figure, center of image
        "crop": (0.1, 0.28, 0.9, 0.82),
    },
    {
        "id": "w27", "num": 27, "stars": 5, "category": "路径迷宫·方向判断",
        "text": "小机器人只能【前进或右转】，不能左转也不能后退。从黑点出发，下面5条路线中，哪条是小机器人【可以】走完的？（路线图如图所示）",
        "options": [("A","路线A"),("B","路线B"),("C","路线C"),("D","路线D"),("E","路线E")],
        "exam": "src/assets/exam-images/2022/q23.png",
        # Route diagrams in lower half
        "crop": (0.0, 0.5, 1.0, 1.0),
    },
    {
        "id": "w31", "num": 31, "stars": 5, "category": "平面图形·面积比较",
        "text": "城市规划图上有5块绿地（A~E），每块绿地的边界都由方格线组成（如图）。请问哪块绿地的面积【最大】？",
        "options": [("A","A绿地"),("B","B绿地"),("C","C绿地"),("D","D绿地"),("E","E绿地")],
        "exam": "src/assets/exam-images/2022/q18.png",
        # Green shapes
        "crop": (0.0, 0.25, 1.0, 0.95),
    },
    {
        "id": "w32", "num": 32, "stars": 5, "category": "平面图形·拼图判断",
        "text": "小明有8个完全相同的等腰直角三角形（如图左所示）。他用全部8个三角形拼出一个完整图案（不重叠、不留空、不剪切）。下面哪个图案是【不可能】拼出来的？",
        "options": [("A","大正方形"),("B","长方形"),("C","六边形"),("D","十字形"),("E","平行四边形")],
        "exam": "src/assets/exam-images/2023/q17.png",
        # Triangle shapes
        "crop": (0.0, 0.18, 1.0, 0.92),
    },
]

for q in questions:
    exam_path = os.path.join(BASE_DIR, q["exam"])
    output_path = os.path.join(OUTPUT_DIR, f"{q['id']}.png")

    print(f"\nProcessing {q['id'].upper()}...")

    # Extract figure
    fig = extract_figure(exam_path, crop_box=q.get("crop"))
    fig = scale_figure(fig, max_w=1460, max_h=480)

    # Generate image
    generate_image(
        output_path=output_path,
        w_num=q["num"],
        stars=q["stars"],
        category=q["category"],
        question_text=q["text"],
        options=q["options"],
        figure_img=fig,
    )

print("\nDone!")
