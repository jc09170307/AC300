#!/usr/bin/env python3
"""AC300 Weekly Cram Sheet builder - generic engine for any week's channel pair.
Usage: python3 build_week_cram.py <week_num> <edition: print|remarkable>
Content data lives in cram_content.py
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from cram_content import WEEKS

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
METAL = (0.365, 0.408, 0.451)
EARTH = (0.663, 0.478, 0.169)
FIRE = (0.690, 0.204, 0.169)
ELEMENT_COLORS = {"Metal": METAL, "Earth": EARTH, "Fire": FIRE}

WEEK_NUM = int(sys.argv[1])
EDITION = sys.argv[2] if len(sys.argv) > 2 else "print"
IS_RM = EDITION == "remarkable"
WK = WEEKS[WEEK_NUM]

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    HAIRLINE = 1.0
    OUT = f"/mnt/user-data/outputs/AC300_Week{WEEK_NUM}_CramSheet_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    HAIRLINE = 0.5
    OUT = f"/mnt/user-data/outputs/AC300_Week{WEEK_NUM}_CramSheet_Print.pdf"
    EDLABEL = "Print Edition"

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


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle):
    setfill(NAVY)
    c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD)
    c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 11)
    c.drawString(36, H - HEADER_H + 15, f"AC300/AC375  |  Week {WEEK_NUM} Cram Sheet  |  {WK['abbrev_pair']}  |  VUIM Summer 2026")
    c.setFont("Lora-Italic", 9)
    c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer(label):
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(36, 34, W - 36, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Week {WEEK_NUM} Cram Sheet  \u00b7  VUIM Summer 2026  \u00b7  {label}")


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]


def new_content_page(subtitle):
    page_bg()
    header(f"{subtitle}  \u00b7  {EDLABEL}")


def end_page():
    footer(f"Page {page_num[0]}")
    c.showPage()
    page_num[0] += 1


def two_col_table(y, rows, col1_w=150):
    """rows: list of (label, value) tuples, two-column definition list"""
    for label, val in rows:
        setfill(NAVY); c.setFont("Lora-Bold", 8.6)
        lbl_lines = wrap_words(label, "Lora-Bold", 8.6, col1_w - 6)
        setfill(DARK); c.setFont("Lora", 8.6)
        val_lines = wrap_words(val, "Lora", 8.6, CW - col1_w - 6)
        n = max(len(lbl_lines), len(val_lines))
        row_h = n * 11
        if row_num[0] % 2 == 0:
            setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
        row_num[0] += 1
        setfill(NAVY); c.setFont("Lora-Bold", 8.6)
        for i, l in enumerate(lbl_lines):
            c.drawString(ML, y - i * 11, l)
        setfill(DARK); c.setFont("Lora", 8.6)
        for i, l in enumerate(val_lines):
            c.drawString(ML + col1_w, y - i * 11, l)
        y -= row_h
    return y


row_num = [0]

# ============= PAGE 1: COVER =============
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 80, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - 45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 62, EDLABEL)

c.setFont("Lora-Bold", 28); setfill(NAVY)
c.drawCentredString(W / 2, H - 150, "CRAM SHEET")
c.setFont("Lora-Italic", 13); setfill(RED)
c.drawCentredString(W / 2, H - 174, WK['channel_names'])
c.setFont("Lora", 10.5); setfill(DARK)
c.drawCentredString(W / 2, H - 194, f"{WK['pts_line']}  \u00b7  Quiz {WEEK_NUM} Ready")

setstroke(GOLD); c.setLineWidth(1)
c.line(W / 2 - 120, H - 210, W / 2 - 40, H - 210)
c.line(W / 2 + 40, H - 210, W / 2 + 120, H - 210)
setfill(GOLD); c.circle(W / 2, H - 210, 2.5, fill=1, stroke=0)

box_w, box_h, gap = 150, 54, 15
total = box_w * 3 + gap * 2
bx0 = (W - total) / 2
by0 = H - 296
labels = [
    ("SPECIAL PTS", "\n".join(WK['cover_special']).split("\n")[0], WK['cover_special'][1] if len(WK['cover_special']) > 1 else "", (0.157, 0.302, 0.541)),
    ("FIVE-SHU", "Both channels", "Well to Sea sequences", (0.380, 0.180, 0.522)),
    ("CROSSING PTS", WK['crossing_summary'][0], WK['crossing_summary'][1] if len(WK['crossing_summary']) > 1 else "", (0.106, 0.369, 0.353)),
]
for i, (t, l1, l2, col) in enumerate(labels):
    x = bx0 + i * (box_w + gap)
    setfill((0.933, 0.937, 0.949) if not IS_RM else (0.902, 0.878, 0.816))
    c.rect(x, by0, box_w, box_h, fill=1, stroke=0)
    c.setFillColorRGB(*col); c.rect(x, by0 + box_h - 3, box_w, 3, fill=1, stroke=0)
    c.setFont("Lora-Bold", 10)
    c.drawCentredString(x + box_w / 2, by0 + box_h - 20, t)
    c.setFont("Lora-Italic", 8); c.setFillColorRGB(*DARK)
    c.drawCentredString(x + box_w / 2, by0 + box_h - 33, l1)
    c.drawCentredString(x + box_w / 2, by0 + box_h - 45, l2)

y = by0 - 40
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, y, "How to use this")
y -= 18
setfill(DARK); c.setFont("Lora", 9)
for line in [
    "Read once the night before. Skim once more the morning of the quiz.",
    "The Channel ID Cards (next pages) have everything the exam tests.",
    "\u2018Exam Traps\u2019 at the end of each channel section are Dr. Zhang's own warnings.",
]:
    c.drawCentredString(W / 2, y, line)
    y -= 13

y -= 20
setstroke(GOLD); c.setLineWidth(1)
c.line(50, y, W - 50, y)
y -= 20
c.setFont("Lora-Italic", 8.5); setfill(GRAY)
c.drawCentredString(W / 2, y, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")

end_page()

# ============= PAGES: PER-CHANNEL ID CARDS =============
for ch in WK['channels']:
    row_num[0] = 0
    new_content_page(f"{ch['name']} \u2014 {ch['classification']}")
    y = H - HEADER_H - 22
    setfill(ELEMENT_COLORS.get(ch['element'], NAVY)); c.rect(ML, y - 3, CW, 3, fill=1, stroke=0)
    y -= 16
    setfill(NAVY); c.setFont("Lora-Bold", 15)
    c.drawString(ML, y, f"{ch['name'].upper()}  \u2014  {ch['classification']}")
    y -= 14
    setfill(GRAY); c.setFont("Lora-Italic", 9)
    c.drawString(ML, y, f"{ch['npts']} points  \u00b7  {ch['polarity']}  \u00b7  {ch['element']}  \u00b7  {ch['peak']}  \u00b7  {ch['direction_short']}")
    y -= 20

    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML, y, "Channel ID Card")
    y -= 4
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2); c.line(ML, y, ML + 160, y)
    y -= 14
    y = two_col_table(y, ch['id_card'])
    y -= 10

    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML, y, "Pathway in 8 Beats")
    y -= 4
    setstroke(GOLD); c.line(ML, y, ML + 160, y)
    y -= 14
    setfill(DARK); c.setFont("Lora", 8.5)
    for i, beat in enumerate(ch['pathway_beats'], 1):
        lines = wrap_words(beat, "Lora", 8.5, CW - 24)
        setfill(RED); c.setFont("Lora-Bold", 8.5)
        c.drawString(ML, y, f"{i}.")
        setfill(DARK); c.setFont("Lora", 8.5)
        for j, l in enumerate(lines):
            c.drawString(ML + 16, y - j * 10.5, l)
        y -= len(lines) * 10.5 + 3
    y -= 8

    # two-column: five-shu + crossing points
    col_w = (CW - 20) / 2
    top_y = y
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y, "Five-Shu (Antique) Points")
    y -= 4
    setstroke(GOLD); c.line(ML, y, ML + 140, y)
    y -= 13
    setfill(DARK); c.setFont("Lora-Bold", 8); c.drawString(ML, y, "Shu Point")
    c.drawString(ML + 75, y, "Element"); c.drawString(ML + 125, y, "Pt")
    y -= 11
    c.setFont("Lora", 8)
    for shu, elem, pt in ch['five_shu']:
        c.drawString(ML, y, shu); c.drawString(ML + 75, y, elem); c.drawString(ML + 125, y, pt)
        y -= 10.5
    left_bottom = y

    y2 = top_y
    x2 = ML + col_w + 20
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(x2, y2, f"Crossing Points ({ch['n_crossing']})")
    y2 -= 4
    setstroke(GOLD); c.line(x2, y2, x2 + 140, y2)
    y2 -= 13
    setfill(DARK); c.setFont("Lora", 8)
    for pt, why in ch['crossing_points']:
        lines = wrap_words(f"{pt} \u2014 {why}", "Lora", 8, col_w - 4)
        for l in lines:
            c.drawString(x2, y2, l)
            y2 -= 10.5
    right_bottom = y2

    y = min(left_bottom, right_bottom) - 12

    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML, y, "Highest-Yield Points")
    y -= 4
    setstroke(GOLD); c.line(ML, y, ML + 160, y)
    y -= 13
    for pt, cat, use in ch['highest_yield']:
        setfill(RED); c.setFont("Lora-Bold", 8.3); c.drawString(ML, y, pt)
        setfill(NAVY); c.setFont("Lora-Italic", 8); c.drawString(ML + 45, y, cat)
        setfill(DARK); c.setFont("Lora", 8.3)
        lines = wrap_words(use, "Lora", 8.3, CW - 200)
        c.drawString(ML + 195, y, lines[0])
        y -= 10.5
        for extra in lines[1:]:
            c.drawString(ML + 195, y, extra)
            y -= 10.5

    y -= 8
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML, y, "Exam Traps \u2014 read these last")
    y -= 4
    setstroke(GOLD); c.line(ML, y, ML + 200, y)
    y -= 13
    setfill(DARK); c.setFont("Lora", 8.3)
    for trap in ch['exam_traps']:
        lines = wrap_words(trap, "Lora", 8.3, CW - 4)
        for l in lines:
            c.drawString(ML, y, l)
            y -= 10.8

    end_page()

# ============= FINAL PAGE: RAPID RECALL =============
row_num[0] = 0
new_content_page("Rapid Recall")
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, f"Rapid Recall  \u2014  {WK['abbrev_pair']}")
y -= 14
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawString(ML, y, "Read this one last, on the way in")
y -= 20

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "The \u201cONLY\u201d List \u2014 guaranteed points")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 220, y)
y -= 14
for fact, ans in WK['only_list']:
    lines = wrap_words(fact, "Lora", 8.6, CW - 130)
    setfill(DARK); c.setFont("Lora", 8.6)
    for i, l in enumerate(lines):
        c.drawString(ML, y - i * 10.8, l)
    setfill(RED); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + CW - 120, y, ans)
    y -= len(lines) * 10.8 + 3
y -= 12

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Forbidden in Pregnancy (cumulative)")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 220, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
for line in WK['forbidden_pregnancy']:
    lines = wrap_words(line, "Lora", 8.5, CW - 4)
    for l in lines:
        c.drawString(ML, y, l)
        y -= 10.8
y -= 8

col_w = (CW - 20) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "Limb Distribution Rule")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 140, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.3)
for pos, yin, yang in [("Anterior", "Taiyin (yin)", "Yangming (yang)"), ("Middle", "Jueyin (yin)", "Shaoyang (yang)"), ("Posterior", "Shaoyin (yin)", "Taiyang (yang)")]:
    c.drawString(ML, y, f"{pos}: {yin} / {yang}")
    y -= 11
left_bottom = y

y2 = top_y
x2 = ML + col_w + 20
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(x2, y2, "Meridian Clock \u2014 full 24 hours")
y2 -= 4
setstroke(GOLD); c.line(x2, y2, x2 + 140, y2)
y2 -= 13
setfill(DARK); c.setFont("Lora", 8)
clock = [("LU", "3-5 AM"), ("LI", "5-7 AM"), ("ST", "7-9 AM"), ("SP", "9-11 AM"),
         ("HT", "11-1 PM"), ("SI", "1-3 PM"), ("BL", "3-5 PM"), ("KI", "5-7 PM"),
         ("PC", "7-9 PM"), ("SJ", "9-11 PM"), ("GB", "11-1 AM"), ("LR", "1-3 AM")]
for ch2, tm in clock:
    bold = ch2 in WK['this_week_abbrevs']
    c.setFont("Lora-Bold" if bold else "Lora", 8)
    setfill(RED if bold else DARK)
    c.drawString(x2, y2, f"{ch2}: {tm}")
    y2 -= 10.5
right_bottom = y2
y = min(left_bottom, right_bottom) - 12

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Last 60 Seconds")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
for line in WK['last_60_seconds']:
    lines = wrap_words(line, "Lora", 8.5, CW - 4)
    for l in lines:
        c.drawString(ML, y, l)
        y -= 10.8
y -= 8

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Commonly Confused \u2014 know both sides")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 220, y)
y -= 13
for pair, dist in WK['commonly_confused']:
    setfill(NAVY); c.setFont("Lora-Bold", 8.3)
    c.drawString(ML, y, pair)
    lines = wrap_words(dist, "Lora", 8.3, CW - 130)
    setfill(DARK); c.setFont("Lora", 8.3)
    c.drawString(ML + 110, y, lines[0])
    y -= 10.8
    for extra in lines[1:]:
        c.drawString(ML + 110, y, extra)
        y -= 10.8

end_page()

c.save()
print("SAVED:", OUT)
