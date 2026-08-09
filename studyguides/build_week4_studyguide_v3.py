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


def draw_image_contain(fig_key, x, y_top, box_w, box_h, border_color):
    """Draws image centered/contained within box, top-anchored. Returns bottom y."""
    iw, ih = get_img_size(fig_key)
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
    left_w = CW * 0.42
    right_w = CW - left_w - col_gap
    rx = ML + left_w + col_gap

    setfill(color); c.setFont("Lora-Bold", 11.5)
    c.drawString(ML, y, "Channel Pathway (MOA)")
    y -= 4
    setstroke(color); c.setLineWidth(1.2)
    c.line(ML, y - 4, ML + left_w, y - 4)
    img_top = y - 14
    img_bottom = draw_image_contain(moa_key, ML, img_top, left_w, 430, color)
    setfill(NAVY); c.setFont("Lora-BoldItalic", 8.8)
    c.drawCentredString(ML + left_w / 2, img_bottom - 14, moa_caption)

    setfill(color); c.setFont("Lora-Bold", 11.5)
    c.drawString(rx, y, "Internal & External Running Course")
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

    # Functions bar (full width)
    y = section_bar(y, f"Functions (MOA) \u2014 {name}", color, size=11.5)
    box_top = y
    lines_all = []
    for f in functions:
        lines_all.extend(wrap_words("\u2022 " + f, "Lora", F_BODY - 0.5, CW - 16))
    box_h = len(lines_all) * (F_BODY_LH - 1) + 14
    setfill(tint); c.rect(ML - 4, box_top - box_h, CW + 8, box_h, fill=1, stroke=0)
    setfill(DARK); c.setFont("Lora", F_BODY - 0.5)
    yy = box_top - 12
    for l in lines_all:
        c.drawString(ML + 6, yy, l)
        yy -= (F_BODY_LH - 1)

    end_page()


channel_meta_page("Heart", "Hand-Shaoyin (HT)", HT_COLOR, HT_TINT, HT_META,
                   "Yin  |  Fire  |  11 AM-1 PM  |  9 Points",
                   HT_COURSE, HT_FUNCTIONS, "MOA_HT", "MOA \u2014 Heart Channel (internal pathway)")
channel_meta_page("Small Intestine", "Hand-Taiyang (SI)", SI_COLOR, SI_TINT, SI_META,
                   "Yang  |  Fire  |  1-3 PM  |  19 Points",
                   SI_COURSE, SI_FUNCTIONS, "MOA_SI", "MOA \u2014 Small Intestine Channel (internal pathway)")


# ============================================================
# EXTERNAL RUNNING COURSE & CAM FIGURE PAGE
# ============================================================
def external_cam_page(name, abbrev, color, tint, points, meta_rows, subtitle_attrs, cam_key, cam_caption, cam_source):
    new_page()
    y = channel_card(f"{abbrev} \u2014 External Running Course & CAM Figure",
                      subtitle_attrs, color, meta_rows)
    img_top = y

    col_gap = 18
    table_w = CW * 0.55
    img_w = CW - table_w - col_gap
    ix = ML + table_w + col_gap

    setfill(color); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y, "Pt"); c.drawString(ML + 34, y, "Chinese"); c.drawString(ML + 112, y, "Location & Notes")
    y -= 13
    setstroke(color); c.setLineWidth(0.8)
    c.line(ML, y + 3, ML + table_w, y + 3)
    y -= 3

    img_bottom = draw_image_contain(cam_key, ix, img_top, img_w, 520, color)
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


external_cam_page("Heart", "HT", HT_COLOR, HT_TINT, HT_POINTS, HT_META,
                   "Yin  |  Fire  |  11 AM-1 PM  |  9 Points",
                   "CAM_HT", "CAM \u2014 Heart Meridian of Hand-Shaoyin (color figure)",
                   "CAM (Deadman) \u00b7 Col. Fig. 6, p.209 \u00b7 Locations OCR-verified (HE1, HE2, HE9)")
external_cam_page("Small Intestine", "SI", SI_COLOR, SI_TINT, SI_POINTS, SI_META,
                   "Yang  |  Fire  |  1-3 PM  |  19 Points",
                   "CAM_SI", "CAM \u2014 Small Intestine Meridian of Hand-Taiyang (color figure)",
                   "CAM (Deadman) \u00b7 Col. Fig. 7, p.227 \u00b7 Locations OCR-verified (SI1,4,8,15,16)")


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
    setfill(tint); c.rect(ML - 4, y - 15, CW + 8, 15, fill=1, stroke=0)
    setfill(color); c.setFont("Lora-Bold", F_TABLE)
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
    setfill(tint); c.rect(ML - 4, y - 15, CW + 8, 15, fill=1, stroke=0)
    setfill(color); c.setFont("Lora-Bold", F_TABLE)
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
crossing_syndromes_page("Heart", "HT", HT_COLOR, HT_TINT,
                         "HT \u2014 Crossing Points (Detailed)",
                         ["Dr. Zhang: \"HT has zero crossing points - the only primary channel of the 12 with none.\"",
                          "Because of this, every HT symptom traces directly back to the Heart itself or its own pathway."],
                         HT_CROSSING_DETAIL, SYNDROMES_HT, HT_HIGHEST_YIELD, HT_FIVE_SHU)

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
for attr, ht_val, si_val in COMPARISON_HT_SI:
    if row_i % 2 == 0:
        setfill(HT_TINT); c.rect(ML - 4, y - 8, (CW + 8) / 2, 13.5, fill=1, stroke=0)
        setfill(SI_TINT); c.rect(ML - 4 + (CW + 8) / 2, y - 8, (CW + 8) / 2, 13.5, fill=1, stroke=0)
    row_i += 1
    setfill(NAVY); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, attr)
    setfill(DARK); c.setFont("Lora", F_TABLE)
    c.drawString(ML + 135, y, ht_val)
    c.drawString(ML + 350, y, si_val)
    y -= 13.5

end_page()

c.save()
print("SAVED:", OUT)
