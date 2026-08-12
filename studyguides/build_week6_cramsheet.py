#!/usr/bin/env python3
"""AC300 Week 6 Cram Sheet -- PC, SJ, GB, LR. Dense night-before reference,
2-column layout. Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, "/home/claude/work")
from wk6_content import (PC_META, SJ_META, GB_META, LR_META, PC_POINTS, SJ_POINTS,
                          LR_POINTS, WEEK6_TALLY, CIRCUITS_NOTE)

FONT_DIR = "/home/claude/work/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
MINISTER = (0.80, 0.40, 0.36)
MIN_TINT = (0.976, 0.938, 0.930)
WOOD = (0.20, 0.48, 0.27)
WOOD_TINT = (0.925, 0.958, 0.928)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_Week6_CramSheet_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week6_CramSheet_Print.pdf"
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


ML, MR = 30, 30
CW = W - ML - MR
GUT = 16
COLW = (CW - GUT) / 2
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(title):
    page_bg()
    setfill(NAVY); c.rect(0, H - 44, W, 44, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 15)
    c.drawString(ML, H - 29, title)
    setfill(GOLD); c.setFont("Lora-Italic", 9)
    c.drawRightString(W - MR, H - 29, f"Week 6 Cram Sheet \u00b7 {EDLABEL}")


def footer():
    setstroke(GRAY); c.setLineWidth(0.4 * LW_MULT)
    c.line(ML, 24, W - MR, 24)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawString(ML, 12, "AC300/AC375 \u00b7 VUIM Summer 2026 \u00b7 Quiz 5 (Wk7): PC+SJ+GB+LR")
    c.drawRightString(W - MR, 12, f"p.{page_num[0]}")


def end_page():
    footer(); c.showPage(); page_num[0] += 1


def col_block_title(x, y, w, title, color):
    h = 16
    setfill(color); c.rect(x, y - h, w, h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9)
    c.drawString(x + 5, y - h + 4.5, title)
    return y - h - 3


def meta_lines(x, y, w, meta, color, tint, size=7.6):
    setfill(DARK); c.setFont("Lora", size)
    for k, v in meta:
        lines = wrap_words(f"{k}: {v}", "Lora", size, w - 6)
        row_h = 9.4 * len(lines) + 1.5
        setfill(tint); c.rect(x, y - row_h, w, row_h, fill=1, stroke=0)
        setfill(DARK)
        for i, l in enumerate(lines):
            c.setFont("Lora-Bold" if i == 0 else "Lora", size)
            c.drawString(x + 3, y - 8 - i * 9.4, l)
        y -= row_h + 0.8
    return y


def points_mini_table(x, y, w, points, color, tint, size=6.9):
    setfill(DARK); c.setFont("Lora-Bold", size + 0.3)
    c.drawString(x, y, "Pt"); c.drawString(x + 24, y, "Category / high-yield note")
    y -= 8.5
    row_i = 0
    for row in points:
        pt, pin, cat, loc = row[0], row[1], row[2], row[3]
        note = cat if cat != "--" else ""
        if "HIGH-YIELD" in loc:
            extra = loc.split("HIGH-YIELD:")[-1].strip()
            note = (note + " -- " if note else "") + "HY: " + extra
        lines = wrap_words(f"{pin}: {note}" if note else pin, "Lora", size, w - 28)
        row_h = 8.1 * len(lines) + 1.2
        bg = tint if row_i % 2 == 0 else (1, 1, 1)
        setfill(bg); c.rect(x, y - row_h, w, row_h, fill=1, stroke=0)
        setfill(color); c.setFont("Lora-Bold", size)
        c.drawString(x + 1, y - 6.5, pt)
        setfill(DARK); c.setFont("Lora", size)
        for i, l in enumerate(lines):
            c.drawString(x + 24, y - 6.5 - i * 8.1, l)
        y -= row_h + 0.6
        row_i += 1
    return y


# ============================================================
# PAGE 1 -- COVER-ISH DENSITY HEADER + PC/SJ META + GB/LR META
# ============================================================
header("Week 6 Cram Sheet -- PC \u00b7 SJ \u00b7 GB \u00b7 LR")
y = H - 56
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawString(ML, y, "PC(9) + SJ(23) + GB(44) + LR(14) = 90 points  \u00b7  Quiz 5 covers this week's material  \u00b7  Cross-check vs Study Guide for full detail")
y -= 16

y0 = y
xL, xR = ML, ML + COLW + GUT
yl = col_block_title(xL, y0, COLW, "PC \u00b7 Pericardium (Ministerial Fire)", MINISTER)
yl = meta_lines(xL, yl, COLW, PC_META, MINISTER, MIN_TINT)
yr = col_block_title(xR, y0, COLW, "SJ \u00b7 San Jiao (Ministerial Fire)", MINISTER)
yr = meta_lines(xR, yr, COLW, SJ_META, MINISTER, MIN_TINT)
y = min(yl, yr) - 6

y0 = y
yl = col_block_title(xL, y0, COLW, "PC Points (9)", MINISTER)
yl = points_mini_table(xL, yl - 10, COLW, PC_POINTS, MINISTER, MIN_TINT)
yr = col_block_title(xR, y0, COLW, "SJ Points (23) -- selected", MINISTER)
yr = points_mini_table(xR, yr - 10, COLW, SJ_POINTS, MINISTER, MIN_TINT)
y = min(yl, yr)
end_page()

# ============================================================
# PAGE 2 -- GB / LR META + POINTS
# ============================================================
header("Week 6 Cram Sheet -- GB \u00b7 LR")
y = H - 56
y0 = y
yl = col_block_title(xL, y0, COLW, "GB \u00b7 Gallbladder (Wood)", WOOD)
yl = meta_lines(xL, yl, COLW, GB_META, WOOD, WOOD_TINT)
yr = col_block_title(xR, y0, COLW, "LR \u00b7 Liver (Wood)", WOOD)
yr = meta_lines(xR, yr, COLW, LR_META, WOOD, WOOD_TINT)
y = min(yl, yr) - 6

y0 = y
setfill(DARK); c.setFont("Lora-Bold", 8.5)
c.drawString(xL, y0, "GB High-Yield Points")
gb_hy = [
    ("GB20", "--", "Wind Gate", "HIGH-YIELD: headache, dizziness, common cold, hypertension"),
    ("GB21", "--", "--", "HIGH-YIELD: FORBIDDEN in pregnancy -- strong descending action"),
    ("GB34", "--", "He-Sea+Hui(Sinews)", "HIGH-YIELD: master point for tendons/sinews"),
    ("GB40", "--", "Yuan-Source", ""),
    ("GB41", "--", "Confluent (Dai Mai)", "HIGH-YIELD: pairs with SJ5"),
    ("GB44", "--", "Jing-Well", "last point, links to LR"),
]
yl = points_mini_table(xL, y0 - 12, COLW, gb_hy, WOOD, WOOD_TINT)
yr = col_block_title(xR, y0 + 8, COLW, "LR Points (14)", WOOD)
yr = points_mini_table(xR, yr - 10, COLW, LR_POINTS, WOOD, WOOD_TINT)
y = min(yl, yr) - 8

y = col_block_title(ML, y, CW, "THREE CIRCUITS -- exam-safety naming", NAVY)
setfill(DARK); c.setFont("Lora", 8)
for l in wrap_words(CIRCUITS_NOTE, "Lora", 8, CW - 10):
    c.drawString(ML, y - 10, l); y -= 10.5
end_page()

# ============================================================
# PAGE 3 -- QUICK-HIT EXAM TRAPS
# ============================================================
header("Week 6 Cram Sheet -- Exam Traps & Fast Facts")
y = H - 56
traps = [
    ("PC and HT are the ONLY 2 primary channels with ZERO crossing points.", MINISTER),
    ("PC6 Neiguan opens Yin Wei Mai (pairs SP4); SJ5 Waiguan opens Yang Wei Mai (pairs GB41) -- do not swap these.", MINISTER),
    ("SJ5 (Yang Wei) and GB41 (Dai Mai) are BOTH confluent points introduced this week -- 4 of the 8 total confluent points are now covered (SP4/PC6, SI3/BL62 from earlier weeks + SJ5, GB41).", MINISTER),
    ("GB is the 3rd largest channel (44 pts) -- after BL (67) and ST (45). Don't confuse with SJ (23).", WOOD),
    ("GB21 is FORBIDDEN in pregnancy -- same trap category as LI4 and SP6.", WOOD),
    ("GB34 = He-Sea AND Hui-Meeting for Sinews/Tendons -- dual designation, easy to under-count on an exam.", WOOD),
    ("GB crossing point count is UNRESOLVED (12 vs 9 named) -- if tested, defer to what Dr. Zhang confirms in class.", WOOD),
    ("LR is the ONLY primary channel reaching the VERTEX (GV20) -- vertex headache = Liver channel.", WOOD),
    ("LR crosses IN FRONT of SP at 8 cun above the medial malleolus -- the one exception to the normal leg-Yin channel order.", WOOD),
    ("LR3 + LI4 = 'Four Gates' -- classic pairing to move Qi/Blood, taught this week.", WOOD),
    ("LR13 Zhangmen has a DOUBLE special-point status: Front-Mu of SPLEEN + Hui-Meeting of all 5 ZANG. Common exam mix-up.", WOOD),
    ("Active-hours clock this week: PC 7-9PM, SJ 9-11PM, GB 11PM-1AM, LR 1-3AM -- consecutive 2-hour blocks moving toward dawn.", NAVY),
    ("Quiz 4 (in-class this week) tested BL/KI (last week's material) -- Quiz 5 (next week) tests THIS week's PC/SJ/GB/LR.", NAVY),
]
setfill(DARK); c.setFont("Lora", 9.3)
for txt, color in traps:
    lines = wrap_words(txt, "Lora", 9.3, CW - 20)
    row_h = 12.5 * len(lines) + 6
    setfill(tuple(min(1, ch + 0.85) for ch in color)); c.rect(ML - 2, y - row_h, CW + 4, row_h, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(2.2 * LW_MULT)
    c.line(ML - 2, y - row_h, ML - 2, y)
    setfill(DARK); c.setFont("Lora", 9.3)
    for i, l in enumerate(lines):
        c.drawString(ML + 8, y - 12 - i * 12.5, l)
    y -= row_h + 4
end_page()

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
