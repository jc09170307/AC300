#!/usr/bin/env python3
import sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
TEAL = (0.106, 0.369, 0.353)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
LINE_GRAY = (0.82, 0.82, 0.82)
HEADER_H = 44

OUT = "/mnt/user-data/outputs/AC300_Confusion_Log.pdf"
c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


ML, MR = 32, 32
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill((1, 1, 1)); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle=""):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    c.drawString(ML, H - HEADER_H + 15, "AC300 CONFUSION LOG")
    if subtitle:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle[:70])


def footer():
    setstroke(GOLD); c.setLineWidth(0.5)
    c.line(ML, 30, W - ML, 30)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 19, f"AC300/AC375 Confusion Log  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}")


def new_page(subtitle=""):
    page_bg(); header(subtitle)


def end_page():
    footer(); c.showPage(); page_num[0] += 1


y = [H - HEADER_H - 20]


def section_bar(text, accent=NAVY, sub=""):
    lines = wrap_words(text, "Lora-Bold", 12.5, CW - (pdfmetrics.stringWidth(sub, "Lora-Italic", 8.5) + 20 if sub else 0))
    line_h = 14
    est_h = len(lines) * line_h + 10
    setfill(accent); c.rect(ML, y[0] - est_h + 5, 3, est_h - 5, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", 12.5)
    for ln in lines:
        c.drawString(ML + 9, yy - 10, ln); yy -= line_h
    if sub:
        setfill(GRAY); c.setFont("Lora-Italic", 8.5)
        c.drawRightString(ML + CW, y[0] - 10, sub)
    y[0] -= est_h
    setstroke(accent); c.setLineWidth(1.1)
    c.line(ML, y[0] + 2, ML + CW, y[0] + 2)
    y[0] -= 9


# =====================================================================
# PAGE 1 -- INTRO + INSTRUCTIONS
# =====================================================================
new_page("How to use this")
y[0] = H - HEADER_H - 20
section_bar("CONFUSION LOG", accent=RED, sub="Fill this in yourself, week by week -- this is YOUR gaps, not mine")
setfill(DARK); c.setFont("Lora", 9.3)
for ln in wrap_words(
    "Every time you get something wrong on a Quiz Bank question, a Practice Final item, or a prep-cold "
    "attempt before reading -- log it here in one line. Don't log everything you find hard; log what you "
    "actually got wrong or guessed on. By Week 9 this page (not the 55-page Study Guide) is your fastest, "
    "most personalized review document, because every line on it is something that's already proven it can "
    "trip you up.", "Lora", 9.3, CW):
    c.drawString(ML, y[0], ln); y[0] -= 13
y[0] -= 10

section_bar("HOW TO FILL IN EACH COLUMN", accent=GOLD)
col_help = [
    ("Week / Source", "Which week's material, and where you hit it (Quiz Bank Q#, Practice Final, prep-cold attempt)."),
    ("What I missed", "The specific fact, not the whole topic. Not \u201cLuo points\u201d -- \u201cforgot SP21 is the Great Luo, "
     "not a 13th regular Luo point.\u201d"),
    ("Why I missed it", "Your own diagnosis. Confused with something similar? Never actually reviewed it? Right "
     "idea, wrong point? This column is where the real learning happens -- be honest, not just accurate."),
    ("Status", "Still shaky / Improving / Resolved. Update this as you re-test the same item -- watching this "
     "column fill up with \u201cResolved\u201d is the expectancy-building part."),
]
for label, text in col_help:
    needed = 30
    setfill(GOLD); c.rect(ML, y[0] - needed + 8, 2.5, needed - 8, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9)
    c.drawString(ML + 10, y[0] - 2, label)
    setfill(DARK); c.setFont("Lora", 8.6)
    yy = y[0] - 13
    for ln in wrap_words(text, "Lora", 8.6, CW - 14):
        c.drawString(ML + 10, yy, ln); yy -= 11
    y[0] = min(yy - 6, y[0] - needed)

end_page()


# =====================================================================
# TABLE PAGES
# =====================================================================
COLS = [("Week / Source", 0.15), ("What I Missed", 0.36), ("Why I Missed It", 0.34), ("Status", 0.15)]


def table_page(rows_per_page=16):
    new_page("Log")
    y[0] = H - HEADER_H - 20
    total_w = CW
    col_widths = [w * total_w for _, w in COLS]
    row_h = (y[0] - 50) / rows_per_page

    # header row
    setfill(NAVY); c.rect(ML, y[0] - 20, CW, 20, fill=1, stroke=0)
    xx = ML
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 8.6)
    for (label, _), w in zip(COLS, col_widths):
        c.drawString(xx + 5, y[0] - 14, label)
        xx += w
    y[0] -= 20

    for r in range(rows_per_page):
        top = y[0]
        if r % 2 == 0:
            setfill((0.976, 0.978, 0.982)); c.rect(ML, top - row_h, CW, row_h, fill=1, stroke=0)
        xx = ML
        setstroke(LINE_GRAY); c.setLineWidth(0.4)
        for w in col_widths:
            c.line(xx, top, xx, top - row_h)
            xx += w
        c.line(xx, top, xx, top - row_h)
        setstroke(LINE_GRAY); c.line(ML, top - row_h, ML + CW, top - row_h)
        y[0] -= row_h
    setstroke(NAVY); c.setLineWidth(1)
    c.line(ML, H - HEADER_H - 20, ML, y[0])
    c.line(ML + CW, H - HEADER_H - 20, ML + CW, y[0])
    end_page()


for _ in range(4):
    table_page(16)

c.save()
print("SAVED:", OUT)
