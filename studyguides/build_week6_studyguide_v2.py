#!/usr/bin/env python3
"""AC300 Week 6 Study Guide -- PC, SJ, GB, LR. REBUILT to match the Week 5
established page layout exactly (extracted via PyMuPDF geometry inspection):
title bar + solid pill row -> Internal Running Course page (MOA image left,
numbered pathway + Functions right) -> External/CAM page (dense point table
left, CAM image right). 2 pages per channel. Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

sys.path.insert(0, "/home/claude/work")
from wk6_content import (PC_META, SJ_META, GB_META, LR_META, PC_COURSE, SJ_COURSE,
                          GB_COURSE, LR_COURSE, PC_POINTS, SJ_POINTS, GB_POINTS_GROUPED,
                          LR_POINTS, PC_FUNCTIONS, SJ_FUNCTIONS, GB_FUNCTIONS, LR_FUNCTIONS)

FIGS_DIR = "/home/claude/work/figs"
FONT_DIR = "/home/claude/work/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter  # 612 x 792
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.10, 0.10, 0.10)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0x9c/255*0+0.945, 0.937, 0.906)   # tan info box (matches Wk2/5 cover box)

MINISTER = (0.80, 0.40, 0.36)
MIN_TINT = (0.976, 0.938, 0.930)
WOOD = (0.20, 0.48, 0.27)
WOOD_TINT = (0.925, 0.958, 0.928)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_Week6_StudyGuide_Classic_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week6_StudyGuide_Classic_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = wd
    if cur: lines.append(cur)
    return lines


ML, MR = 42, 42
RX = W - MR  # 570
CW = RX - ML
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def top_bar():
    setfill(DARK); c.setFont("Lora", 8.5)
    c.drawString(ML, H - 30.3, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(RX, H - 30.3, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6 * LW_MULT)
    c.line(ML, H - 38, RX, H - 38)


def bottom_bar(label):
    setfill(NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora", 8)
    c.drawString(ML, 10, label)
    c.drawRightString(RX, 10, f"p.{page_num[0]}")


def new_page():
    page_bg(); top_bar()


def end_page(label):
    bottom_bar(label); c.showPage(); page_num[0] += 1


def title_pills(title, subtitle_right, color, pills, y_top=None):
    """Exact Week 5 geometry: 28pt title bar @ y(H-92..H-64 relative), then a
    16pt pill row of solid same-color blocks with 4pt white gaps, 10pt gap
    between bar and pill row. Returns y just below pill row."""
    if y_top is None:
        y_top = H - 64  # bottom of title bar, matches wk5's y=74 from top(792-74=718->titletop46->bottom74, i.e. bar spans 792-74=718 to 792-46=746) -- reproduce with H-46 top edge
    bar_top = H - 46
    bar_bot = H - 74
    setfill(color); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill((1, 1, 1))
    title_size = 13
    sub_w = pdfmetrics.stringWidth(subtitle_right, "Lora-Italic", 9.5) + 20 if subtitle_right else 0
    max_title_w = CW - 14 - sub_w
    while pdfmetrics.stringWidth(title, "Lora-Bold", title_size) > max_title_w and title_size > 8.5:
        title_size -= 0.3
    c.setFont("Lora-Bold", title_size)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    # pill row
    pill_top = bar_bot - 10
    pill_h = 16
    pill_bot = pill_top - pill_h
    setfill((1, 1, 1)); c.rect(ML, pill_bot, CW, pill_h, fill=1, stroke=0)
    x = ML
    gap = 3
    n = len(pills)
    if n:
        avail = CW - gap * (n - 1)
        fsize = 6.8
        def widths_at(fsize):
            return [pdfmetrics.stringWidth(label + " ", "Lora", fsize) + pdfmetrics.stringWidth(val, "Lora-Bold", fsize) + 10 for label, val in pills]
        widths = widths_at(fsize)
        total = sum(widths)
        while total > avail and fsize > 5.2:
            fsize -= 0.2
            widths = widths_at(fsize)
            total = sum(widths)
        if total > avail:
            scale = avail / total
            widths = [w * scale for w in widths]
        xx = ML
        for (label, val), w in zip(pills, widths):
            setfill(color); c.rect(xx, pill_bot, w, pill_h, fill=1, stroke=0)
            setfill((1, 1, 1)); c.setFont("Lora", fsize)
            c.drawString(xx + 4, pill_bot + 4.7, label)
            lw = pdfmetrics.stringWidth(label + " ", "Lora", fsize)
            c.setFont("Lora-Bold", fsize)
            c.drawString(xx + 4 + lw, pill_bot + 4.7, val)
            xx += w + gap
    return pill_bot


_img_size_cache = {}


def get_img_size(fig_key):
    if fig_key not in _img_size_cache:
        with Image.open(f"{FIGS_DIR}/{fig_key}.jpeg") as im:
            _img_size_cache[fig_key] = im.size
    return _img_size_cache[fig_key]


def draw_image_contain(fig_key, x, y_top, box_w, box_h, border_color):
    iw, ih = get_img_size(fig_key)
    scale = min(box_w / iw, box_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (box_w - dw) / 2
    dy = y_top - dh
    setstroke(border_color); c.setLineWidth(0.8 * LW_MULT)
    c.rect(dx - 2, dy - 2, dw + 4, dh + 4, fill=0, stroke=1)
    c.drawImage(ImageReader(f"{FIGS_DIR}/{fig_key}.jpeg"), dx, dy, width=dw, height=dh)
    return dy


def section_label(y, text, color):
    setfill(color); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML, y, text)
    return y - 14


def key_pills(meta):
    """Select the 7 pills matching the established Wk5 pattern:
    Pertaining, Connecting, Back-Shu, Front-Mu, Yuan-Source, Luo, He-Sea."""
    d = dict(meta)
    order = [("Pertaining", "Pertaining"), ("Connecting", "Connecting"),
             ("Back-Shu", "Back-Shu"), ("Front-Mu", "Front-Mu"),
             ("Yuan-Source", "Yuan-Source"), ("Luo-Connecting", "Luo"),
             ("He-Sea", "He-Sea")]
    out = []
    for key, label in order:
        if key in d:
            out.append((label, d[key]))
    return out


# ============================================================
# PAGE A: Internal Running Course -- MOA image (left) + numbered pathway
# and Functions (right)
# ============================================================
def internal_page(name, subtitle, color, tint, meta, course, functions, fig_moa, chan_label):
    new_page()
    y = title_pills(name, subtitle, color, key_pills(meta))
    y -= 16
    y = section_label(y, "Internal Running Course", color)

    left_x, left_w = ML, 320
    right_x = ML + left_w + 16
    right_w = RX - right_x

    img_top = y
    draw_image_contain(fig_moa, left_x, img_top, left_w, img_top - 60, color)

    ry = y
    circ_r = 8
    for i, step in enumerate(course, 1):
        setfill(color); c.circle(right_x + circ_r, ry - circ_r, circ_r, fill=1, stroke=0)
        setfill((1, 1, 1)); c.setFont("Lora-Bold", 8.5)
        c.drawCentredString(right_x + circ_r, ry - circ_r - 3, str(i))
        setfill(DARK); c.setFont("Lora", 8.1)
        tx = right_x + circ_r * 2 + 8
        lines = wrap_words(step, "Lora", 8.1, right_w - circ_r * 2 - 8)
        for j, l in enumerate(lines):
            c.drawString(tx, ry - 8 - j * 9.6, l)
        ry -= max(2, len(lines)) * 9.6 + 8

    ry -= 8
    setfill(color); c.setFont("Lora-Bold", 9)
    c.drawString(right_x, ry, "Functions")
    ry -= 12
    setfill(DARK); c.setFont("Lora", 8)
    for f in functions:
        setfill(color); c.circle(right_x + 2, ry + 2.5, 1.4, fill=1, stroke=0)
        setfill(DARK)
        lines = wrap_words(f, "Lora", 8, right_w - 14)
        for j, l in enumerate(lines):
            c.drawString(right_x + 10, ry - j * 9.6, l)
        ry -= max(1, len(lines)) * 9.6 + 3
        if ry < 45:
            break
    end_page(f"AC300/AC375 | Week 6 | {chan_label} Channel | VUIM Summer 2026")


# ============================================================
# PAGE B: External Running Course & CAM Figures -- point table (left) +
# CAM image (right)
# ============================================================
def external_page(name, abbr, subtitle, color, tint, meta, points_rows, fig_cam, chan_label,
                   grouped=None):
    new_page()
    title = f"The {name} ({abbr})  -  External Running Course & CAM Figures"
    y = title_pills(title, subtitle, color, key_pills(meta))
    y -= 12

    table_x, table_w = ML, 210
    img_x = table_x + table_w + 14
    img_w = RX - img_x

    hdr_h = 12
    setfill(color); c.rect(table_x, y - hdr_h, table_w, hdr_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 6.8)
    c.drawString(table_x + 3, y - hdr_h + 3.4, "Pt")
    c.drawString(table_x + 32, y - hdr_h + 3.4, "Pinyin")
    c.drawString(table_x + 88, y - hdr_h + 3.4, "Location & Category")
    ty = y - hdr_h

    def draw_row(pt, pin, loc, special):
        nonlocal ty
        lines = wrap_words(loc, "Lora", 5.6, table_w - 88 - 3)
        row_h = max(6.8, 5.9 * len(lines) + 1.2)
        bg = tint if special else (0.972, 0.972, 0.972) if (draw_row.i % 2) else (1, 1, 1)
        setfill(bg); c.rect(table_x, ty - row_h, table_w, row_h, fill=1, stroke=0)
        setfill(DARK)
        c.setFont("Lora-BoldItalic" if special else "Lora", 5.9)
        c.drawString(table_x + 3, ty - 5.4, pt)
        c.setFont("Lora-Italic" if special else "Lora", 5.9)
        c.drawString(table_x + 32, ty - 5.4, pin)
        c.setFont("Lora", 5.6)
        for i, l in enumerate(lines):
            c.drawString(table_x + 88, ty - 5.4 - i * 5.9, l)
        ty -= row_h
        draw_row.i += 1
    draw_row.i = 0

    if grouped:
        for zone, pts in grouped:
            zh = 9
            setfill(GOLD); c.rect(table_x, ty - zh, table_w, zh, fill=1, stroke=0)
            setfill((1, 1, 1)); c.setFont("Lora-Bold", 6.2)
            c.drawString(table_x + 3, ty - zh + 2.2, zone)
            ty -= zh
            for pt, pin, cat, loc in pts:
                special = cat not in ("--",)
                draw_row(pt, pin, f"{cat}. {loc}" if cat != "--" else loc, special)
    else:
        for pt, pin, cat, loc in points_rows:
            special = cat not in ("--",)
            draw_row(pt, pin, f"{cat}. {loc}" if cat != "--" else loc, special)

    dy = draw_image_contain(fig_cam, img_x, y, img_w, y - 55, color)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(img_x + img_w / 2, dy - 12, f"CAM Col. Fig. \u2014 {name}")
    end_page(f"AC300/AC375 | Week 6 | {chan_label} Channel | VUIM Summer 2026")


# ============================================================
# COVER (matches Week 2/5 spec exactly: left-aligned, plain WEEK label,
# tan info box, credit line)
# ============================================================
new_page()
y = H - 60
setfill(GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "WEEK 6")
c.setFont("Lora-Italic", 10)
c.drawRightString(RX, y, EDLABEL)
y -= 40
setfill(NAVY); c.setFont("Lora-Bold", 28)
c.drawString(ML, y, "Week 6 Study Guide")
y -= 28
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-Bold", 17)
c.drawString(ML, y, "Pericardium, San Jiao, Gallbladder & Liver Channels")
y -= 22
setfill(GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "PC (9 pts) + SJ (23 pts) + GB (44 pts) + LR (14 pts) = 90 Points")
y -= 18
setstroke(GOLD); c.setLineWidth(1.2)
c.line(ML, y, RX, y)
y -= 28
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Document Covers:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.5)
bullets = [
    "Pericardium Meridian of Hand-Jueyin (PC1-PC9) with MOA + CAM figures",
    "PC has ZERO crossing points -- shares this trait with only Heart (Wk4)",
    "San Jiao Meridian of Hand-Shaoyang (SJ1-SJ23) with MOA + CAM figures",
    "SJ5 opens the Yang Wei Mai (confluent, pairs with GB41)",
    "Gallbladder Meridian of Foot-Shaoyang (GB1-GB44) with MOA + CAM figures",
    "GB crossing-point count flagged (12 on slide / 9 named) -- pending Dr. Zhang",
    "Liver Meridian of Foot-Jueyin (LR1-LR14) with MOA + CAM figures",
    "LR is the only channel reaching the vertex; LR3+LI4 'Four Gates' combination",
]
for b in bullets:
    setfill(GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(DARK)
    for i, l in enumerate(wrap_words(b, "Lora", 10.5, CW - 20)):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(wrap_words(b, "Lora", 10.5, CW - 20)))
    y -= 4

y -= 10
box_h = 60
setfill(CREAM); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 16, y - 18, "QUIZ 5 (Week 7) covers: PC, SJ, GB & LR material.")
c.drawString(ML + 16, y - 32, "PC/SJ/GB/LR are taught this week.")
c.drawString(ML + 16, y - 46, "MOA pp.367-472  |  CAM pp.77-82  |  Slides: Dr. Vivian Zhang, Week 6")
y -= box_h + 40

setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
end_page("AC300/AC375 | Week 6 | PC, SJ, GB, LR Channels | VUIM Summer 2026")

# ============================================================
# CHANNEL PAGES
# ============================================================
internal_page("The Pericardium Meridian of Hand-Jueyin", "Ministerial Fire  |  7-9 PM  |  9 Points",
              MINISTER, MIN_TINT, PC_META, PC_COURSE, PC_FUNCTIONS, "MOA_PC", "PC")
external_page("Pericardium Meridian", "PC", "Ministerial Fire  |  9 Points", MINISTER, MIN_TINT,
              PC_META, PC_POINTS, "CAM_PC", "PC")

internal_page("The San Jiao Meridian of Hand-Shaoyang", "Ministerial Fire  |  9-11 PM  |  23 Points",
              MINISTER, MIN_TINT, SJ_META, SJ_COURSE, SJ_FUNCTIONS, "MOA_SJ", "SJ")
external_page("San Jiao Meridian", "SJ", "Ministerial Fire  |  23 Points", MINISTER, MIN_TINT,
              SJ_META, SJ_POINTS, "CAM_SJ", "SJ")

internal_page("The Gallbladder Meridian of Foot-Shaoyang", "Wood  |  11 PM-1 AM  |  44 Points",
              WOOD, WOOD_TINT, GB_META, GB_COURSE, GB_FUNCTIONS, "MOA_GB", "GB")
external_page("Gallbladder Meridian", "GB", "Wood  |  44 Points", WOOD, WOOD_TINT,
              GB_META, None, "CAM_GB", "GB", grouped=GB_POINTS_GROUPED)

internal_page("The Liver Meridian of Foot-Jueyin", "Wood  |  1-3 AM  |  14 Points",
              WOOD, WOOD_TINT, LR_META, LR_COURSE, LR_FUNCTIONS, "MOA_LR", "LR")
external_page("Liver Meridian", "LR", "Wood  |  14 Points", WOOD, WOOD_TINT,
              LR_META, LR_POINTS, "CAM_LR", "LR")

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
