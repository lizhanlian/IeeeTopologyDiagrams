"""
生成 nuwa-skill 风格的绿色「微信搜一搜」公众号横幅
需要: pip install pillow
"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QR_PATH = os.path.join(BASE_DIR, "assets", "wechat-qrcode.png")
OUT_PATH = os.path.join(BASE_DIR, "assets", "wechat-banner.png")

# ---------- 参数 ----------
WIDTH = 1200
HEIGHT = 420
PADDING = 40
QR_SIZE = 340          # 二维码最终尺寸（正方形）
GREEN = (7, 193, 96)   # 微信绿 #07C160
WHITE = (255, 255, 255)
DARK = (30, 30, 30)
GRAY = (80, 80, 80)
SEARCH_W = 560
SEARCH_H = 120
SEARCH_RADIUS = 20

# ---------- 创建画布 ----------
img = Image.new("RGB", (WIDTH, HEIGHT), GREEN)
draw = ImageDraw.Draw(img)

# ---------- 贴二维码（左侧，圆角白底）----------
qr = Image.open(QR_PATH).convert("RGB")
qr = qr.resize((QR_SIZE, QR_SIZE), Image.LANCZOS)
# 白底圆角容器
pad = 16
box_size = QR_SIZE + pad * 2
box_img = Image.new("RGB", (box_size, box_size), WHITE)
# 圆角
mask = Image.new("L", (box_size, box_size), 0)
mdraw = ImageDraw.Draw(mask)
r = 16
mdraw.rounded_rectangle([(0, 0), (box_size - 1, box_size - 1)], radius=r, fill=255)
box_img.paste(qr, (pad, pad))
x_qr = PADDING
y_qr = (HEIGHT - box_size) // 2
img.paste(box_img, (x_qr, y_qr), mask)

# ---------- 加载字体（尝试系统中文字体）----------
font_candidates = [
    "C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/msyh.ttf",
    "C:/Windows/Fonts/simhei.ttf",
    "C:/Windows/Fonts/simsun.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
]
font_title = None
font_search = None
for f in font_candidates:
    if os.path.exists(f):
        try:
            font_title = ImageFont.truetype(f, 64)
            font_search = ImageFont.truetype(f, 48)
            break
        except Exception:
            continue
if font_title is None:
    font_title = ImageFont.load_default()
    font_search = ImageFont.load_default()

# ---------- 右侧文字 ----------
text_x = PADDING + QR_SIZE + pad * 2 + 60

# 标题 "微信搜一搜"（居中大字）
title_text = "微信搜一搜"
tw = draw.textlength(title_text, font=font_title)
# 标题放在搜索框正上方，两者相对右侧空间居中
right_area_w = WIDTH - text_x - PADDING
title_x = text_x + (right_area_w - tw) // 2
title_y = 60
draw.text((title_x, title_y), title_text, fill=WHITE, font=font_title)

# ---------- 搜索框 ----------
search_x = text_x + (right_area_w - SEARCH_W) // 2
search_y = title_y + 110
# 圆角白底搜索框
sr = SEARCH_RADIUS
draw.rounded_rectangle(
    [(search_x, search_y), (search_x + SEARCH_W, search_y + SEARCH_H)],
    radius=sr, fill=WHITE
)
# 放大镜图标（圆形 + 斜线柄）
mag_cx = search_x + 45
mag_cy = search_y + SEARCH_H // 2
mag_r = 18
draw.ellipse([(mag_cx - mag_r, mag_cy - mag_r), (mag_cx + mag_r, mag_cy + mag_r)], outline=GRAY, width=4)
# 镜柄（从圆的右下向外）
handle_len = 22
draw.line(
    [(mag_cx + mag_r - 6, mag_cy + mag_r - 6),
     (mag_cx + mag_r - 6 + handle_len, mag_cy + mag_r - 6 + handle_len)],
    fill=GRAY, width=5
)
# 搜索词 "湛联说"
search_text = "湛联说"
draw.text((search_x + 110, search_y + (SEARCH_H - 48) // 2 - 4), search_text, fill=DARK, font=font_search)

# ---------- 保存 ----------
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
img.save(OUT_PATH, "PNG", optimize=True)
print(f"✅ 已生成: {OUT_PATH}")
print(f"   尺寸: {WIDTH}x{HEIGHT}")