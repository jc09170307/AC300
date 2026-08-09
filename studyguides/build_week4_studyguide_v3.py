#!/usr/bin/env python3
"""AC300 Week 4 Study Guide - HT & SI. Week-3-style design: colored channel
cards with pill badges, two-column meta/external pages with MOA+CAM figures,
combined crossing-points/syndromes/five-shu pages. Builds Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

from week4_sg_content import (HT_POINTS, SI_POINTS, HT_COURSE, SI_COURSE, HT_META, SI_META,
                               HT_FUNCTIONS, SI_FUNCTIONS, SYNDROMES_HT, SYNDROMES_SI,
                               HT_HIGHEST_YIELD, SI_HIGHEST_YIELD, HT_FIVE_SHU, SI_FIVE_SHU,
                               CLINICAL_PEARLS_WK4, QUIZ4_FUNDAMENTALS, COMPARISON_HT_SI)

FIGS_DIR = "/home/claude/figs_final"

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.976, 0.965, 0.929)

HT_COLOR = (0.627, 0.220, 0.180)          # deep red (Fire)
HT_TINT = (0.976, 0.928, 0.919)
SI_COLOR = (0.784, 0.353, 0.294)          # coral-red (Fire, lighter)
SI_TINT = (0.983, 0.948, 0.938)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    OUT = "/mnt/user-data/outputs/AC300_Week4_StudyGuide_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week4_StudyGuide_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def blend(rgb, target=(1, 1, 1), amt=0.90):
    return tuple(rgb[i] + (target[i] - rgb[i]) * amt for i in range(3))


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]

F_BODY = 10.0
F_BODY_LH = 13.0
F_TABLE = 9.0
F_TABLE_LH = 11.8
F_SMALL = 8.4
F_SMALL_LH = 10.8

WEEK_LABEL = "AC300/AC375 | Week 4 | HT & SI Channels | VUIM Summer 2026"


def simple_header():
    setfill(DARK); c.setFont("Lora", 9)
    c.drawString(ML, H - 30, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 9)
    c.drawRightString(W - MR, H - 30, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6)
    c.line(ML, H - 38, W - MR, H - 38)


def simple_footer():
    setfill(NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora", 8)
    c.drawString(ML, 10, WEEK_LABEL)
    c.drawRightString(W - MR, 10, f"p.{page_num[0]}")


def new_page():
    page_bg()
    simple_header()


def end_page():
    simple_footer()
    c.showPage()
    page_num[0] += 1


_img_size_cache = {}


def get_img_size(fig_key):
    if fig_key not in _img_size_cache:
        with Image.open(f"{FIGS_DIR}/{fig_key}.jpeg") as im:
            _img_size_cache[fig_key] = im.size
    return _img_size_cache[fig_key]


IMG_FOOTER_CLEAR = 45  # keep this much clearance above the footer bar for images


def draw_image_contain(fig_key, x, y_top, box_w, box_h, border_color):
    """Draws image centered/contained within box, top-anchored. Height is capped
    to whatever vertical space remains above the footer, so it can never overflow
    onto the footer or next page. Returns bottom y."""
    iw, ih = get_img_size(fig_key)
    box_h = min(box_h, y_top - IMG_FOOTER_CLEAR)
    scale = min(box_w / iw, box_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (box_w - dw) / 2
    dy = y_top - dh
    setstroke(border_color); c.setLineWidth(0.8)
    c.rect(dx - 3, dy - 3, dw + 6, dh + 6, fill=0, stroke=1)
    c.drawImage(ImageReader(f"{FIGS_DIR}/{fig_key}.jpeg"), dx, dy, width=dw, height=dh)
    return dy


def channel_card(title, subtitle_right, color, pills, y_top=None):
    """Draws the colored title bar + pill row(s). Returns y just below the pill row(s)."""
    if y_top is None:
        y_top = H - 46
    bar_h = 30
    setfill(color); c.rect(ML - 4, y_top - bar_h, CW + 8, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1))
    title_size = 14
    sub_w = pdfmetrics.stringWidth(subtitle_right, "Lora-Italic", 9.5) + 14
    max_title_w = CW - sub_w
    while pdfmetrics.stringWidth(title, "Lora-Bold", title_size) > max_title_w and title_size > 9.5:
        title_size -= 0.5
    c.setFont("Lora-Bold", title_size)
    c.drawString(ML + 6, y_top - bar_h + 9, title)
    c.setFont("Lora-Italic", 9.5)
    c.drawRightString(W - MR - 2, y_top - bar_h + 10, subtitle_right)
    y = y_top - bar_h - 2

    # pill row(s) - wrap onto additional rows rather than truncating
    pill_h = 19
    darker = tuple(max(0, ch - 0.06) for ch in color)
    lighter = tuple(min(1, ch + 0.10) for ch in darker)
    c.setFont("Lora-Bold", 7.6)
    rows = [[]]
    px = ML + 4
    for label, val in pills:
        txt = f"{label} {val}"
        tw = pdfmetrics.stringWidth(txt, "Lora-Bold", 7.6) + 12
        if px + tw > W - MR - 4:
            rows.append([])
            px = ML + 4
        rows[-1].append((txt, tw))
        px += tw + 6
    for row in rows:
        setfill(darker); c.rect(ML - 4, y - pill_h, CW + 8, pill_h, fill=1, stroke=0)
        px = ML + 4
        for txt, tw in row:
            setfill(lighter)
            c.roundRect(px, y - pill_h + 3, tw, pill_h - 6, 5, fill=1, stroke=0)
            setfill((1, 1, 1))
            c.drawString(px + 6, y - pill_h + 6.5, txt)
            px += tw + 6
        y -= pill_h + 1
    return y - 15


def section_bar(y, title, color, size=13):
    """Full-width colored bar section title (used on crossing-points / combined pages)."""
    bar_h = 24
    setfill(color); c.rect(ML - 4, y - bar_h, CW + 8, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", size)
    c.drawString(ML + 6, y - bar_h + 7, title)
    return y - bar_h - 14


def quote_box(y, lines, color):
    box_h = len(lines) * 12.5 + 12
    setfill(CREAM); c.rect(ML - 4, y - box_h, CW + 8, box_h, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(2.2)
    c.line(ML - 4, y - box_h, ML - 4, y)
    setfill(DARK); c.setFont("Lora-Italic", 9)
    yy = y - 10
    for l in lines:
        c.drawString(ML + 8, yy, l)
        yy -= 12.5
    return y - box_h - 14


# ============================================================
# COVER
# ============================================================
page_bg()
simple_header()
y = H - 60
setfill(GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "WEEK 4")
c.setFont("Lora-Italic", 10)
c.drawRightString(W - MR, y, EDLABEL)
y -= 40
setfill(NAVY); c.setFont("Lora-Bold", 28)
c.drawString(ML, y, "Week 4 Study Guide")
y -= 28
setfill(HT_COLOR); c.setFont("Lora-Bold", 17)
c.drawString(ML, y, "Heart & Small Intestine Channels")
y -= 22
setfill(GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "HT (9 pts) + SI (19 pts) = 28 Points")
y -= 18
setstroke(GOLD); c.setLineWidth(1.2)
c.line(ML, y, W - MR, y)
y -= 28
setfill(HT_COLOR); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Document Covers:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.5)
bullets = [
    "Heart Meridian of Hand-Shaoyin (HT1-HT9) with MOA + CAM figures",
    "HT has ZERO crossing points - the only primary channel with none",
    "Small Intestine Meridian of Hand-Taiyang (SI1-SI19) with MOA + CAM figures",
    "SI's 2 Crossing Points - detailed (BL1, GB14)",
    "Syndromes, High-Yield Points, and Five-Shu tables for both channels",
    "Dr. Zhang's Clinical Pearls - direct from lecture",
    "Quiz 4 Fundamentals + HT vs SI Quick Reference comparison",
]
for b in bullets:
    setfill(GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(DARK)
    for i, l in enumerate(wrap_words(b, "Lora", 10.5, CW - 20)):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(wrap_words(b, "Lora", 10.5, CW - 20)))
    y -= 4

y -= 10
box_h = 62
setfill(CREAM); c.rect(ML - 4, y - box_h, CW + 8, box_h, fill=1, stroke=0)
setstroke(GOLD); c.setLineWidth(2.2)
c.line(ML - 4, y - box_h, ML - 4, y)
setfill(HT_COLOR); c.setFont("Lora-BoldItalic", 10)
c.drawString(ML + 8, y - 16, "QUIZ 4 (next class) covers: HT & SI channels.")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawString(ML + 8, y - 31, "MIDTERM (Week 5) covers Weeks 1-4 cumulative.")
c.drawString(ML + 8, y - 46, "MOA: HT pp.209-221 | SI pp.222-249   \u00b7   CAM (Deadman): HT/SI chapters")

y -= box_h + 100
setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawCentredString(W / 2, y, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")

end_page()


# ============================================================
# CHANNEL META PAGE (2-column: MOA image left, numbered course right)
# ============================================================
def channel_meta_page(name, subtitle_full, color, tint, meta_rows, subtitle_attrs,
                       course_beats, functions, moa_key, moa_caption):
    new_page()
    y = channel_card(f"{name} Meridian of {subtitle_full}", subtitle_attrs, color, meta_rows)

    col_gap = 20
    left_w = CW * 0.60
    right_w = CW - left_w - col_gap
    rx = ML + left_w + col_gap

    # Precompute Functions box height so we know how much space to reserve
    # below the image and course list before drawing either.
    lines_all = []
    for f in functions:
        lines_all.extend(wrap_words("\u2022 " + f, "Lora", F_BODY - 0.5, CW - 16))
    functions_box_h = len(lines_all) * (F_BODY_LH - 1) + 14

    setfill(color); c.setFont("Lora-Bold", 11.5)
    c.drawString(ML, y, "Channel Pathway (MOA)")
    y -= 4
    setstroke(color); c.setLineWidth(1.2)
    c.line(ML, y - 4, ML + left_w, y - 4)
    img_top = y - 14
    # Reserve exact space for: 30pt gap + 10pt gap + section_bar's own 38pt
    # (24 bar height + 14 internal gap) + the Functions box + safety margin above footer.
    img_max_h = img_top - functions_box_h - 125
    img_bottom = draw_image_contain(moa_key, ML, img_top, left_w, img_max_h, color)
    setfill(NAVY); c.setFont("Lora-BoldItalic", 8.8)
    c.drawCentredString(ML + left_w / 2, img_bottom - 14, moa_caption)

    setfill(color); c.setFont("Lora-Bold", 11.5)
    c.drawString(rx, y, "Internal Running Course")
    ry = y - 4
    setstroke(color); c.setLineWidth(1.2)
    c.line(rx, ry - 4, rx + right_w, ry - 4)
    ry -= 18
    for i, beat in enumerate(course_beats, 1):
        lines = wrap_words(beat, "Lora", F_BODY - 0.4, right_w - 22)
        setfill(color); c.circle(rx + 7, ry - 3, 7, fill=1, stroke=0)
        setfill((1, 1, 1)); c.setFont("Lora-Bold", 8)
        c.drawCentredString(rx + 7, ry - 6, str(i))
        setfill(DARK); c.setFont("Lora", F_BODY - 0.4)
        for j, l in enumerate(lines):
            c.drawString(rx + 20, ry - j * (F_BODY_LH - 1), l)
        ry -= len(lines) * (F_BODY_LH - 1) + 7

    y = min(img_bottom - 30, ry) - 10

    # Defensive backstop: if either column ran long and the Functions box
    # would still collide with the footer, push Functions onto a fresh page.
    if y - 38 - functions_box_h < 41:
        end_page()
        new_page()
        y = H - 46
        setfill(color); c.setFont("Lora-Bold", 12)
        c.drawString(ML, y, f"{name} \u2014 Functions (continued)")
        y -= 24

    # Functions bar (full width) - reuse the precomputed lines/height
    y = section_bar(y, f"Functions (MOA) \u2014 {name}", color, size=11.5)
    box_top = y
    setfill(tint); c.rect(ML - 4, box_top - functions_box_h, CW + 8, functions_box_h, fill=1, stroke=0)
    setfill(DARK); c.setFont("Lora", F_BODY - 0.5)
    yy = box_top - 12
    for l in lines_all:
        c.drawString(ML + 6, yy, l)
        yy -= (F_BODY_LH - 1)

    end_page()



# ============================================================
# EXTERNAL RUNNING COURSE & CAM FIGURE PAGE
# ============================================================
def external_cam_page(name, abbrev, color, tint, points, meta_rows, subtitle_attrs, cam_key, cam_caption, cam_source, table_frac=0.55):
    new_page()
    y = channel_card(f"{abbrev} \u2014 External Running Course & CAM Figure",
                      subtitle_attrs, color, meta_rows)
    img_top = y

    col_gap = 18
    table_w = CW * table_frac
    img_w = CW - table_w - col_gap
    ix = ML + table_w + col_gap

    setfill(color); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y, "Pt"); c.drawString(ML + 34, y, "Chinese"); c.drawString(ML + 112, y, "Location & Notes")
    y -= 13
    setstroke(color); c.setLineWidth(0.8)
    c.line(ML, y + 3, ML + table_w, y + 3)
    y -= 3

    img_bottom = draw_image_contain(cam_key, ix, img_top, img_w, img_top - IMG_FOOTER_CLEAR - 28, color)
    setfill(NAVY); c.setFont("Lora-BoldItalic", 8.6)
    c.drawCentredString(ix + img_w / 2, img_bottom - 14, cam_caption)
    setfill(GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawCentredString(ix + img_w / 2, img_bottom - 26, cam_source)

    row_i = 0
    loc_col_w = table_w - 112
    FOOTER_CLEAR = 40
    for pt, py, loc in points:
        lines = wrap_words(loc, "Lora", F_TABLE - 0.2, loc_col_w)
        row_h = len(lines) * (F_TABLE_LH - 0.6)
        if y - row_h < FOOTER_CLEAR:
            end_page()
            new_page()
            y = H - 46
            setfill(color); c.setFont("Lora-Bold", 12)
            c.drawString(ML, y, f"{abbrev} \u2014 Point Locations (continued)")
            y -= 18
            setfill(color); c.setFont("Lora-Bold", F_TABLE)
            c.drawString(ML, y, "Pt"); c.drawString(ML + 34, y, "Chinese"); c.drawString(ML + 112, y, "Location & Notes")
            y -= 13
            setstroke(color); c.setLineWidth(0.8)
            c.line(ML, y + 3, ML + table_w, y + 3)
            y -= 3
            row_i = 0
        if row_i % 2 == 0:
            setfill(tint); c.rect(ML - 4, y - row_h + 8, table_w + 4, row_h, fill=1, stroke=0)
        row_i += 1
        setfill(color); c.setFont("Lora-Bold", F_TABLE - 0.2); c.drawString(ML, y, pt)
        setfill(GRAY); c.setFont("Lora-Italic", F_TABLE - 0.2); c.drawString(ML + 34, y, py)
        setfill(DARK); c.setFont("Lora", F_TABLE - 0.2)
        for i, l in enumerate(lines):
            c.drawString(ML + 112, y - i * (F_TABLE_LH - 0.6), l)
        y -= row_h

    end_page()



# ============================================================
# CROSSING POINTS + SYNDROMES + HIGH-YIELD + FIVE-SHU (combined)
# ============================================================
def crossing_syndromes_page(name, abbrev, color, tint, crossing_title, crossing_quote,
                             crossing_detail, syn, high_yield, five_shu, forbidden_note=None):
    new_page()
    y = H - 46
    y = section_bar(y, crossing_title, color, size=13)
    y = quote_box(y, crossing_quote, color)

    for pt, loc_title, loc, clinical, src in crossing_detail:
        needed = 15 + 12 + len(wrap_words(loc, "Lora", F_BODY - 1, CW - 70)) * 11.5 + \
                 len(wrap_words(clinical, "Lora", F_BODY - 1, CW - 70)) * 11.5 + 16
        if y - needed < 60:
            end_page()
            new_page()
            y = H - 46
        setstroke(color); c.setLineWidth(2.2)
        c.line(ML - 4, y - needed + 14, ML - 4, y + 2)
        setfill(color); c.setFont("Lora-Bold", 10.5)
        c.drawString(ML + 4, y, f"{pt} \u2014 {loc_title}")
        setfill(GRAY); c.setFont("Lora-Italic", 8.4)
        c.drawRightString(W - MR, y, src)
        y -= 13.5
        setfill(DARK); c.setFont("Lora", F_BODY - 1)
        for l in wrap_words(f"Location: {loc}", "Lora", F_BODY - 1, CW - 12):
            c.drawString(ML + 4, y, l); y -= 11.5
        for l in wrap_words(f"Clinical: {clinical}", "Lora", F_BODY - 1, CW - 12):
            c.drawString(ML + 4, y, l); y -= 11.5
        y -= 10

    y -= 4
    col_w = (CW - 24) / 2
    top_y = y
    setfill(color); c.rect(ML - 4, y - 16, col_w + 4, 16, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 2, y - 12, "A. External Course Symptoms")
    y -= 24
    setfill(DARK); c.setFont("Lora", F_TABLE)
    for s in syn['external']:
        setfill(color); c.circle(ML + 2, y + 3, 1.6, fill=1, stroke=0)
        setfill(DARK)
        for l in wrap_words(s, "Lora", F_TABLE, col_w - 14):
            c.drawString(ML + 10, y, l); y -= F_TABLE_LH
        y -= 2
    left_bottom = y

    x2 = ML + col_w + 24
    y2 = top_y
    setfill(color); c.rect(x2 - 4, y2 - 16, col_w + 4, 16, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawString(x2 + 2, y2 - 12, f"B. Internal Organ ({name})")
    y2 -= 24
    setfill(DARK); c.setFont("Lora", F_TABLE)
    for s in syn['internal']:
        setfill(color); c.circle(x2 + 2, y2 + 3, 1.6, fill=1, stroke=0)
        setfill(DARK)
        for l in wrap_words(s, "Lora", F_TABLE, col_w - 14):
            c.drawString(x2 + 10, y2, l); y2 -= F_TABLE_LH
        y2 -= 2
    right_bottom = y2
    y = min(left_bottom, right_bottom) - 8

    y = section_bar(y, f"High-Yield {abbrev} Points", color, size=11)
    setfill(color); c.rect(ML - 4, y - 15, CW + 8, 15, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y - 11, "Pt"); c.drawString(ML + 38, y - 11, "Category"); c.drawString(ML + 175, y - 11, "Key Indications")
    y -= 15 + F_TABLE_LH
    row_i = 0
    for pt, cat, use in high_yield:
        lines = wrap_words(use, "Lora", F_TABLE, CW - 175)
        row_h = len(lines) * (F_TABLE_LH - 0.8)
        if row_i % 2 == 0:
            setfill(tint); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
        row_i += 1
        setfill(color); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, pt)
        setfill(NAVY); c.setFont("Lora-Italic", F_TABLE - 0.3); c.drawString(ML + 38, y, cat)
        setfill(DARK); c.setFont("Lora", F_TABLE)
        for i, l in enumerate(lines):
            c.drawString(ML + 175, y - i * (F_TABLE_LH - 0.8), l)
        y -= row_h
    y -= 10

    y = section_bar(y, f"Five-Shu (Antique) Points \u2014 {abbrev}", color, size=11)
    setfill(color); c.rect(ML - 4, y - 15, CW + 8, 15, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y - 11, "Shu Point"); c.drawString(ML + 95, y - 11, "Element")
    c.drawString(ML + 160, y - 11, "Pt"); c.drawString(ML + 300, y - 11, "Clinical Use")
    y -= 15 + F_TABLE_LH
    row_i = 0
    for shu, elem, pt, use in five_shu:
        lines = wrap_words(use, "Lora", F_TABLE, CW - 300)
        row_h = len(lines) * (F_TABLE_LH - 0.8)
        if row_i % 2 == 0:
            setfill(tint); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
        row_i += 1
        setfill(DARK); c.setFont("Lora", F_TABLE)
        c.drawString(ML, y, shu); c.drawString(ML + 95, y, elem); c.drawString(ML + 160, y, pt)
        for i, l in enumerate(lines):
            c.drawString(ML + 300, y - i * (F_TABLE_LH - 0.8), l)
        y -= row_h

    if forbidden_note:
        y -= 10
        box_h = len(wrap_words(forbidden_note[1], "Lora", F_SMALL, CW - 16)) * F_SMALL_LH + \
            13.5 + 10
        setfill(CREAM); c.rect(ML - 4, y - box_h, CW + 8, box_h, fill=1, stroke=0)
        setstroke(GOLD); c.setLineWidth(2.2)
        c.line(ML - 4, y - box_h, ML - 4, y)
        setfill(color); c.setFont("Lora-BoldItalic", 9.5)
        c.drawString(ML + 6, y - 13, forbidden_note[0])
        setfill(DARK); c.setFont("Lora", F_SMALL)
        yy = y - 26
        for l in wrap_words(forbidden_note[1], "Lora", F_SMALL, CW - 16):
            c.drawString(ML + 6, yy, l); yy -= F_SMALL_LH

    end_page()


HT_CROSSING_DETAIL = [
    ("HT \u2014 Zero Crossing Points", "A Genuinely Unique Feature",
     "HT is the only one of the 12 primary channels with no crossing (jiaohui) points anywhere on its external pathway.",
     "Every HT symptom traces directly back to the Heart or its own pathway - there is no 'borrowed' symptom picture "
     "from another channel to confuse it with. Dr. Zhang flagged this as one of the highest-yield unique-feature facts "
     "in the Weeks 1-4 scope.",
     "\u2014 confirmed from lecture"),
]

SI_CROSSING_DETAIL = [
    ("BL1 Jingming", "Bridge of the Nose / Inner Canthus",
     "Inner canthus of the eye, ~0.1 cun above the medial canthus.",
     "SI's ascending facial branch crosses BL here en route toward the eye. Treats all eye disorders: redness, pain, "
     "myopia, night blindness. Same crossing point used by the ST and BL channels themselves.",
     "BL1 / BL channel"),
    ("GB14 Yangbai", "Forehead",
     "1 cun above the midpoint of the eyebrow, directly above the pupil.",
     "SI's branch also crosses GB14 as it continues toward the forehead. Used for frontal headache, eyebrow pain, "
     "eyelid twitching, and eye disorders.",
     "GB14 / GB channel"),
]

QUIZ4_PRACTICE = [
    # (question, [A,B,C,D], correct_letter, explanation, difficulty)
    ("How many points does the HT channel have?",
     ["9", "11", "19", "20"], "A",
     "HT has 9 points (HT1-HT9) - the fewest of any primary channel.", "easy"),
    ("How many points does the SI channel have?",
     ["9", "11", "19", "20"], "C",
     "SI has 19 points (SI1-SI19) - more than double HT's count.", "easy"),
    ("What element do HT and SI both belong to?",
     ["Earth", "Fire", "Water", "Wood"], "B",
     "HT and SI are the Primary Fire pair (not to be confused with PC/SJ, the Ministerial Fire pair).", "easy"),
    ("HT is classified as which Yin/Yang type?",
     ["Yin (Hand-Shaoyin)", "Yang (Hand-Taiyang)", "Yin (Foot-Shaoyin)", "Yang (Foot-Taiyang)"], "A",
     "HT = Heart Meridian of Hand-Shaoyin - a Yin, Zang (organ) channel.", "easy"),
    ("SI is classified as which Yin/Yang type?",
     ["Yin (Hand-Shaoyin)", "Yang (Hand-Taiyang)", "Yin (Foot-Taiyin)", "Yang (Foot-Yangming)"], "B",
     "SI = Small Intestine Meridian of Hand-Taiyang - a Yang, Fu (bowel) channel.", "easy"),
    ("Peak Qi activity of the Heart meridian is:",
     ["9-11 AM", "11 AM-1 PM", "1-3 PM", "3-5 PM"], "B",
     "HT peaks 11 AM-1 PM, immediately after SP (9-11 AM) and before SI (1-3 PM).", "easy"),
    ("Peak Qi activity of the Small Intestine meridian is:",
     ["11 AM-1 PM", "1-3 PM", "3-5 PM", "5-7 PM"], "B",
     "SI peaks 1-3 PM, immediately after HT.", "easy"),
    ("The CONNECTING organ of the Heart meridian is:",
     ["Lung", "Stomach", "Small Intestine", "Bladder"], "C",
     "Pertaining = Heart, Connecting = Small Intestine (interior-exterior pair).", "easy"),
    ("HT's Back-Shu point is:",
     ["BL14", "BL15", "BL20", "BL27"], "B",
     "BL15 Xinshu is HT's Back-Shu point. (SI's is BL27 Xiaochangshu.)", "easy"),
    ("SI's Front-Mu point is:",
     ["CV12", "CV14", "CV4", "CV3"], "C",
     "CV4 Guanyuan is SI's Front-Mu point. (HT's is CV14 Juque.)", "easy"),
    ("HT7 Shenmen holds which special point categories?",
     ["He-Sea + Luo-Connecting", "Shu-Stream + Yuan-Source", "Jing-Well + Xi-Cleft", "Front-Mu + Back-Shu"], "B",
     "HT7 is both the Shu-Stream and Yuan-Source point - the single most important point for calming Shen.", "medium"),
    ("Which HT point is the He-Sea?",
     ["HT3 Shaohai", "HT7 Shenmen", "HT9 Shaochong", "HT1 Jiquan"], "A",
     "HT3 Shaohai is the He-Sea point, at the elbow crease.", "medium"),
    ("SI3 Houxi holds which special categories?",
     ["Yuan-Source only", "He-Sea + Xi-Cleft", "Shu-Stream + Confluent (opens Du Mai)", "Jing-Well + Luo"], "C",
     "SI3 is Shu-Stream and also a Confluent point opening the Du Mai.", "medium"),
    ("SI3's Confluent action opens the Du Mai in combination with which point?",
     ["LU7", "BL62 Shenmai", "KI6", "SP4"], "B",
     "SI3 (Houxi) pairs with BL62 (Shenmai) to open the Du Mai - one of the 8 Confluent point pairs.", "medium"),
    ("HT9 Shaochong is which Five-Shu category?",
     ["Jing-Well", "Ying-Spring", "Shu-Stream", "He-Sea"], "A",
     "HT9 is the Jing-Well point - the last point of HT, on the radial side of the little finger.", "medium"),
    ("SI's Lower He-Sea point is located on which channel?",
     ["SI itself", "BL", "ST", "GB"], "C",
     "SI's Lower He-Sea is ST39 Xiajuxu - on the STOMACH channel, not SI. True for all six Fu organs.", "medium"),
    ("Which point is SI's Xi-Cleft?",
     ["SI4 Wangu", "SI6 Yanglao", "SI7 Zhizheng", "SI8 Xiaohai"], "B",
     "SI6 Yanglao is the Xi-Cleft point, dorsal to the head of the ulna.", "medium"),
    ("HT5 Tongli's special category is:",
     ["Luo-Connecting", "Xi-Cleft", "Yuan-Source", "He-Sea"], "A",
     "HT5 Tongli is the Luo-Connecting point, linking HT to SI.", "medium"),
    ("SI16 Tianchuang is classified as:",
     ["Window of Heaven", "Confluent", "Front-Mu", "Back-Shu"], "A",
     "SI16 is a Window of Heaven point, near the laryngeal prominence - needle with care (carotid region).", "medium"),
    ("Per Dr. Zhang's lecture, which point is specifically noted for breast milk / lactation problems?",
     ["HT8 Shaofu", "SI1 Shaoze", "SI19 Tinggong", "HT3 Shaohai"], "B",
     "Dr. Zhang highlighted SI1 (Shaoze) specifically for lactation problems.", "medium"),
    ("How many crossing points does the HT channel have?",
     ["0", "2", "4", "6"], "A",
     "HT is the only one of the 12 primary channels with ZERO crossing points anywhere on its pathway.", "hard"),
    ("How many crossing points does SI have, and with which channels?",
     ["0", "2 (BL1, GB14)", "6 (mostly abdomen/chest)", "11 (mostly face/head)"], "B",
     "SI crosses only twice: BL1 (Jingming) and GB14 (Yangbai), both on its facial branch.", "hard"),
    ("SI's facial branch crosses BL1 Jingming en route to:",
     ["The ear", "The inner canthus of the eye", "The nose", "The mouth"], "B",
     "BL1 sits at the inner canthus; SI's ascending branch crosses it heading toward the eye.", "hard"),
    ("Which statement about HT is exam-critical and TRUE?",
     ["HT has the most points of any channel", "HT is the only channel with zero crossing points",
      "HT connects internally to the Lung", "HT's Back-Shu is CV14"], "B",
     "HT's zero crossing points is one of the highest-yield unique-feature facts in the Weeks 1-4 scope.", "hard"),
    ("Per Dr. Zhang's circuit-continuity trap, SI connects internally to which organ NEXT?",
     ["Pericardium", "San Jiao", "Bladder", "Kidney"], "C",
     "SI connects to BLADDER next (not PC/SJ) via its facial branch to BL1 - a classic exam trap.", "hard"),
    ("HT and SI together open which circuit?",
     ["Anterior Circuit", "Posterior Circuit (also called Inner Circuit)",
      "Ministerial Fire Circuit", "Middle Circuit"], "B",
     "HT -> SI opens the Posterior Circuit (also called Inner Circuit on the revised Lecture 4 slide).", "hard"),
    ("The Primary Fire pair (HT/SI) should not be confused with which other Fire pair?",
     ["LU/LI", "ST/SP", "PC/SJ (Ministerial Fire)", "BL/KI"], "C",
     "PC and SJ are Ministerial Fire, a separate pair with their own circuit taught in Week 6.", "hard"),
    ("EXCEPT: all of the following are TRUE about SI EXCEPT:",
     ["SI has more than double HT's points", "SI3 opens the Du Mai",
      "SI's Lower He-Sea is on the SI channel itself", "SI crosses BL1 and GB14"], "C",
     "SI's Lower He-Sea is ST39, on the STOMACH channel - not on SI itself. The trap answer.", "hard"),
    ("Which HT point is the emergency point for severe heart pain and revives consciousness?",
     ["HT7 Shenmen", "HT9 Shaochong", "HT3 Shaohai", "HT5 Tongli"], "B",
     "HT9 (Jing-Well) is HT's emergency point - severe heart pain, palpitations, revives consciousness.", "hard"),
    ("HT6 Yinxi (Xi-Cleft) is clinically noted for:",
     ["Anxiety and insomnia only", "Night sweats and acute heart pain", "Voice disorders", "Arm pain only"], "B",
     "As HT's Xi-Cleft (acute) point, HT6 treats night sweats and acute heart pain.", "hard"),
]


# ============================================================
# ORCHESTRATION - each organ's full page set built consecutively
# (Zang before Fu: HT meta -> HT external -> HT crossing, THEN
#  SI meta -> SI external -> SI crossing - never interleaved)
# ============================================================
channel_meta_page("Heart", "Hand-Shaoyin (HT)", HT_COLOR, HT_TINT, HT_META,
                   "Yin  |  Fire  |  11 AM-1 PM  |  9 Points",
                   HT_COURSE, HT_FUNCTIONS, "MOA_HT", "MOA \u2014 Heart Channel (internal pathway)")
external_cam_page("Heart", "HT", HT_COLOR, HT_TINT, HT_POINTS, HT_META,
                   "Yin  |  Fire  |  11 AM-1 PM  |  9 Points",
                   "CAM_HT", "CAM \u2014 Heart Meridian of Hand-Shaoyin (color figure)",
                   "CAM (Deadman) \u00b7 Col. Fig. 6, p.209 \u00b7 Locations OCR-verified (HE1, HE2, HE9)",
                   table_frac=0.38)
crossing_syndromes_page("Heart", "HT", HT_COLOR, HT_TINT,
                         "HT \u2014 Crossing Points (Detailed)",
                         ["Dr. Zhang: \"HT has zero crossing points - the only primary channel of the 12 with none.\"",
                          "Because of this, every HT symptom traces directly back to the Heart itself or its own pathway."],
                         HT_CROSSING_DETAIL, SYNDROMES_HT, HT_HIGHEST_YIELD, HT_FIVE_SHU)

channel_meta_page("Small Intestine", "Hand-Taiyang (SI)", SI_COLOR, SI_TINT, SI_META,
                   "Yang  |  Fire  |  1-3 PM  |  19 Points",
                   SI_COURSE, SI_FUNCTIONS, "MOA_SI", "MOA \u2014 Small Intestine Channel (internal pathway)")
external_cam_page("Small Intestine", "SI", SI_COLOR, SI_TINT, SI_POINTS, SI_META,
                   "Yang  |  Fire  |  1-3 PM  |  19 Points",
                   "CAM_SI", "CAM \u2014 Small Intestine Meridian of Hand-Taiyang (color figure)",
                   "CAM (Deadman) \u00b7 Col. Fig. 7, p.227 \u00b7 Locations OCR-verified (SI1,4,8,15,16)",
                   table_frac=0.39)
crossing_syndromes_page("Small Intestine", "SI", SI_COLOR, SI_TINT,
                         "SI \u2014 The 2 Crossing Points (Detailed)",
                         ["Dr. Zhang: \"HT has zero crossing points. SI crosses only twice, both on its facial branch",
                          "near the eye and forehead - far fewer than ST (11) or SP (6), but still tested.\""],
                         SI_CROSSING_DETAIL, SYNDROMES_SI, SI_HIGHEST_YIELD, SI_FIVE_SHU,
                         forbidden_note=None)


# ============================================================
# CLINICAL PEARLS
# ============================================================
new_page()
y = H - 46
y = section_bar(y, "Dr. Zhang's Clinical Pearls \u2014 Direct from Lecture", NAVY, size=13)
setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
c.drawString(ML, y, "Highest exam probability")
y -= 16
for idx, (title, body) in enumerate(CLINICAL_PEARLS_WK4):
    accent = HT_COLOR if idx % 2 == 0 else SI_COLOR
    lines_t = wrap_words(title, "Lora-Bold", 10.5, CW - 14)
    lines_b = wrap_words(body, "Lora", F_BODY, CW - 14)
    needed = len(lines_t) * 13.5 + len(lines_b) * F_BODY_LH + 14
    if y - needed < 50:
        end_page()
        new_page()
        y = H - 46
        y = section_bar(y, "Dr. Zhang's Clinical Pearls (cont.)", NAVY, size=13)
    setstroke(accent); c.setLineWidth(2.2)
    c.line(ML - 4, y - needed + 12, ML - 4, y + 2)
    setfill(accent); c.setFont("Lora-Bold", 10.5)
    for l in lines_t:
        c.drawString(ML + 4, y, l); y -= 13.5
    setfill(DARK); c.setFont("Lora", F_BODY)
    for l in lines_b:
        c.drawString(ML + 4, y, l); y -= F_BODY_LH
    y -= 12
end_page()


# ============================================================
# QUIZ 4 FUNDAMENTALS
# ============================================================
new_page()
y = H - 46
y = section_bar(y, "Quiz 4 Fundamentals \u2014 Distribution, Circuits & Nomenclature", NAVY, size=13)
setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
c.drawString(ML, y, "From Dr. Zhang's review slides")
y -= 18

col_w = (CW - 24) / 2
top_y = y
setfill(HT_COLOR); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Distribution of the 12 Main Meridians")
y -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['distribution']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(ML, y, ll); y -= F_TABLE_LH
left_bottom = y

y2 = top_y
x2 = ML + col_w + 24
setfill(SI_COLOR); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "Circulation of the 12 Meridians")
y2 -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['circulation']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(x2, y2, ll); y2 -= F_TABLE_LH
right_bottom = y2
y = min(left_bottom, right_bottom) - 16

y = section_bar(y, "Circuit Connections \u2014 exactly what links to what (exam trap)", NAVY, size=11.5)
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['circuit_connections']:
    for ll in wrap_words(l, "Lora", F_TABLE, CW - 4):
        c.drawString(ML, y, ll); y -= F_TABLE_LH
y -= 14

top_y = y
setfill(HT_COLOR); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Nomenclature")
y -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['nomenclature']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(ML, y, ll); y -= F_TABLE_LH
left_bottom = y

y2 = top_y
setfill(SI_COLOR); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "Meridian Clock \u2014 HT & SI peak times")
y2 -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['clock']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(x2, y2, ll); y2 -= F_TABLE_LH
right_bottom = y2
y = min(left_bottom, right_bottom) - 16

setfill(HT_COLOR); c.setFont("Lora-BoldItalic", 10)
for l in wrap_words(QUIZ4_FUNDAMENTALS['homework_rule'], "Lora-BoldItalic", 10, CW - 4):
    c.drawString(ML, y, l); y -= 13

end_page()


# ============================================================
# HT vs SI COMPARISON
# ============================================================
new_page()
y = H - 46
y = section_bar(y, "HT vs SI \u2014 Quick Reference Comparison", NAVY, size=13)
setfill(NAVY); c.setFont("Lora-Bold", F_TABLE)
c.drawString(ML, y, "Attribute"); c.drawString(ML + 135, y, "HT  |  Heart (Hand Shaoyin)")
c.drawString(ML + 350, y, "SI  |  Small Intestine (Hand Taiyang)")
y -= 15
row_i = 0
col2_x = ML + 135
col3_x = ML + 350
NEUTRAL_TINT = (0.94, 0.94, 0.95)
for attr, ht_val, si_val in COMPARISON_HT_SI:
    if row_i % 2 == 0:
        setfill(NEUTRAL_TINT); c.rect(ML - 4, y - 8, col2_x - 4 - (ML - 4), 13.5, fill=1, stroke=0)
        setfill(HT_TINT); c.rect(col2_x - 4, y - 8, col3_x - col2_x, 13.5, fill=1, stroke=0)
        setfill(SI_TINT); c.rect(col3_x - 4, y - 8, (ML - 4 + CW + 8) - (col3_x - 4), 13.5, fill=1, stroke=0)
    row_i += 1
    setfill(NAVY); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, attr)
    setfill(DARK); c.setFont("Lora", F_TABLE)
    c.drawString(col2_x, y, ht_val)
    c.drawString(col3_x, y, si_val)
    y -= 13.5

end_page()

# ============================================================
# PRACTICE QUIZ - 30 questions, varying difficulty (easy/medium/hard)
# ============================================================
DIFF_COLOR = {"easy": (0.318, 0.573, 0.345), "medium": (0.729, 0.573, 0.184), "hard": HT_COLOR}

def quiz_question_pages():
    global page_num
    new_page()
    y = H - 46
    y = section_bar(y, "Week 4 Practice Quiz \u2014 30 Questions (Varying Difficulty)", NAVY, size=13)
    setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
    c.drawString(ML, y, "Covers HT & SI \u00b7 green = easier recall, gold = applied, red = trap/nuance")
    y -= 18

    for qi, (q, opts, correct, expl, diff) in enumerate(QUIZ4_PRACTICE, 1):
        q_lines = wrap_words(f"{qi}  {q}", "Lora-Bold", 10, CW - 10)
        opt_lines = []
        for j in range(0, 4, 2):
            left = f"{chr(65+j)}. {opts[j]}"
            right = f"{chr(65+j+1)}. {opts[j+1]}"
            opt_lines.append((left, right))
        needed = len(q_lines) * 12.5 + len(opt_lines) * 12 + 12
        if y - needed < 45:
            end_page()
            new_page()
            y = H - 46
            y = section_bar(y, "Week 4 Practice Quiz (continued)", NAVY, size=13)
            y -= 8
        setfill(DIFF_COLOR[diff]); c.circle(ML + 2, y - 2, 3, fill=1, stroke=0)
        setfill(DARK); c.setFont("Lora-Bold", 10)
        for i, l in enumerate(q_lines):
            c.drawString(ML + 10 if i == 0 else ML, y - i * 12.5, l)
        y -= len(q_lines) * 12.5 + 2
        setfill(DARK); c.setFont("Lora", 9.3)
        col2 = ML + CW / 2
        for left, right in opt_lines:
            c.drawString(ML + 10, y, left)
            c.drawString(col2, y, right)
            y -= 12
        y -= 8

    end_page()


def quiz_answer_key_pages():
    new_page()
    y = H - 46
    y = section_bar(y, "Week 4 Practice Quiz \u2014 Answer Key (All 30 Questions)", NAVY, size=13)
    y -= 4

    for qi, (q, opts, correct, expl, diff) in enumerate(QUIZ4_PRACTICE, 1):
        q_short = wrap_words(q, "Lora-Italic", 8.6, CW - 30)
        expl_lines = wrap_words(expl, "Lora", 9.3, CW - 30)
        needed = 13 + len(q_short) * 10.5 + len(expl_lines) * 11.5 + 8
        if y - needed < 45:
            end_page()
            new_page()
            y = H - 46
            y = section_bar(y, "Week 4 Practice Quiz \u2014 Answer Key (continued)", NAVY, size=13)
            y -= 4
        setfill(DIFF_COLOR[diff]); c.circle(ML + 2, y - 3, 3, fill=1, stroke=0)
        setfill(NAVY); c.setFont("Lora-Bold", 10)
        c.drawString(ML + 10, y, f"{qi}.  {correct}")
        setfill(GRAY); c.setFont("Lora-Italic", 8.6)
        for i, l in enumerate(q_short):
            c.drawString(ML + 40, y - i * 10.5, l)
        y -= len(q_short) * 10.5 + 2
        setfill(DARK); c.setFont("Lora", 9.3)
        for l in expl_lines:
            c.drawString(ML + 10, y, l)
            y -= 11.5
        y -= 8

    end_page()


c.save()
print("SAVED:", OUT)
