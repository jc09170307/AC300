#!/usr/bin/env python3
"""AC300 Week 1 Cram Sheet - Channel Theory. Builds BOTH Print and reMarkable editions."""
import sys
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from week1_content import (TWELVE_MERIDIANS, ZANG_ORGANS, FU_ORGANS, CIRCUITS, DIRECTION_RULES,
                            MEETING_POINTS, MERIDIAN_CLOCK, CLOCK_ELEMENT, FUNCTIONS_OF_MERIDIANS, NOMENCLATURE,
                            CHANNELS_VS_MERIDIANS, QUIZ1_FUNDAMENTALS, HISTORY_KEY_QUESTION, HISTORY_TIMELINE,
                            MERIDIAN_VS_COLLATERAL_TABLE)

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
METAL = (0.365, 0.408, 0.451); EARTH = (0.663, 0.478, 0.169); FIRE = (0.690, 0.204, 0.169)
WATER = (0.180, 0.396, 0.612); WOOD = (0.239, 0.518, 0.278); MIN_FIRE = (0.831, 0.514, 0.478)
ELEMENT_COLORS = {"Metal": METAL, "Earth": EARTH, "Fire": FIRE, "Water": WATER, "Wood": WOOD, "Ministerial Fire": MIN_FIRE}
CIRCUIT_COLORS = {"Outer Circuit": METAL, "Inner Circuit": FIRE, "Middle Circuit": (0.380, 0.180, 0.522)}

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902); ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51; HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Week1_CramSheet_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1); ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44; HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Week1_CramSheet_Print.pdf"
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
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]
row_num = [0]


def header(subtitle):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 10)
    c.drawString(36, H - HEADER_H + 15, "AC300/AC375  |  Week 1 Cram Sheet  |  VUIM Summer 2026")
    c.setFont("Lora-Italic", 8.6)
    c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer():
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, 34, W - MR, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Week 1 Cram Sheet  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}  \u00b7  {EDLABEL}")


def new_page(subtitle):
    page_bg(); header(subtitle)


def end_page():
    footer(); c.showPage(); page_num[0] += 1


def section_rule(y, title, width=240, size=12):
    setfill(NAVY); c.setFont("Lora-Bold", size)
    c.drawString(ML, y, title)
    y -= 5
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, y, ML + width, y)
    return y - 14


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
c.drawCentredString(W / 2, H - 174, "Channel Theory \u2014 Concept, Nomenclature, Flow of Qi")
c.setFont("Lora", 10.5); setfill(DARK)
c.drawCentredString(W / 2, H - 194, "12 Meridians  \u00b7  3 Circuits  \u00b7  Quiz 1 Ready")

setstroke(GOLD); c.setLineWidth(1)
c.line(W / 2 - 120, H - 210, W / 2 - 40, H - 210)
c.line(W / 2 + 40, H - 210, W / 2 + 120, H - 210)
setfill(GOLD); c.circle(W / 2, H - 210, 2.5, fill=1, stroke=0)

box_w, box_h, gap = 150, 54, 15
total = box_w * 3 + gap * 2
bx0 = (W - total) / 2
by0 = H - 296
labels = [
    ("12 MERIDIANS", "6 Yin + 6 Yang", "3 Hand + 3 Foot each", (0.157, 0.302, 0.541)),
    ("3 CIRCUITS", "Outer / Inner / Middle", "4 meridians each", (0.380, 0.180, 0.522)),
    ("15 COLLATERALS", "12 primary + Du + Ren", "+ Spleen's Great Luo", (0.106, 0.369, 0.353)),
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
    "This is the foundation everything else builds on - know it cold before Week 2.",
    "The circulation rule (chest-hand-head-foot-chest) is the single most tested fact in the course.",
    "Draw each circuit by hand, more than once - Dr. Zhang's own studying advice.",
]:
    c.drawCentredString(W / 2, y, line)
    y -= 13

y -= 20
setstroke(GOLD); c.setLineWidth(1)
c.line(50, y, W - 50, y)
y -= 20
c.setFont("Lora-Italic", 8.5); setfill(GRAY)
c.drawCentredString(W / 2, y, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's Week 1 lecture, VUIM Summer 2026")

end_page()

# ============= PAGE 2: CORE DEFINITIONS =============
new_page(f"Core Definitions")
y = H - HEADER_H - 24
y = section_rule(y, "What Is a Channel?", width=200)
setfill(DARK); c.setFont("Lora", 9)
for l in wrap_words(CHANNELS_VS_MERIDIANS['definition'], "Lora", 9, CW - 4):
    c.drawString(ML, y, l); y -= 12
y -= 10
setfill(NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "The full system:")
y -= 13
setfill(DARK); c.setFont("Lora", 8.6)
for item in CHANNELS_VS_MERIDIANS['counts']:
    lines = wrap_words("\u2022 " + item, "Lora", 8.6, CW - 6)
    for l in lines:
        c.drawString(ML, y, l); y -= 11
    y -= 2
y -= 10

y = section_rule(y, "Zang-Fu Organs", width=180)
col_w = (CW - 20) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "Zang (Yin) - 6 organs")
y -= 13
setfill(DARK); c.setFont("Lora", 8.6)
for o in ZANG_ORGANS:
    c.drawString(ML, y, "\u2022 " + o); y -= 11.5
left_bottom = y
y2 = top_y; x2 = ML + col_w + 20
setfill(NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(x2, y2, "Fu (Yang) - 6 organs")
y2 -= 13
setfill(DARK); c.setFont("Lora", 8.6)
for o in FU_ORGANS:
    c.drawString(x2, y2, "\u2022 " + o); y2 -= 11.5
right_bottom = y2
y = min(left_bottom, right_bottom) - 10

y = section_rule(y, "3-Part Nomenclature", width=200)
setfill(DARK); c.setFont("Lora", 8.6)
for i, part in enumerate(NOMENCLATURE['parts'], 1):
    lines = wrap_words(f"{i}. {part}", "Lora", 8.6, CW - 4)
    for l in lines:
        c.drawString(ML, y, l); y -= 11.5
y -= 2
setfill(GRAY); c.setFont("Lora-Italic", 8.2)
for l in wrap_words(NOMENCLATURE['example'], "Lora-Italic", 8.2, CW - 4):
    c.drawString(ML, y, l); y -= 10.5
y -= 12

y = section_rule(y, "History \u2014 Which Came First: Channels or Points?", width=380)
setfill(RED); c.setFont("Lora-BoldItalic", 8.8)
c.drawString(ML, y, "Answer: CHANNELS (Mawangdui Silk Manuscripts predate point-specific texts).")
y -= 13
setfill(DARK); c.setFont("Lora", 8.4)
for era, date, desc in HISTORY_TIMELINE:
    line = f"{era} ({date}): {desc.split('.')[0]}."
    for l in wrap_words(line, "Lora", 8.4, CW - 4):
        c.drawString(ML, y, l); y -= 10.8
    y -= 1
y -= 10

y = section_rule(y, "Meridians vs. Collaterals", width=220)
row_h = 11.5
col_w = [86, (CW - 86) / 2, (CW - 86) / 2]
setfill(NAVY); c.setFont("Lora-Bold", 7.6)
c.drawString(ML, y, "Aspect"); c.drawString(ML + col_w[0], y, "Meridians (Jingmai)")
c.drawString(ML + col_w[0] + col_w[1], y, "Collaterals (Luomai)")
y -= 12
setfill(DARK); c.setFont("Lora", 7.8)
for aspect, mer, col in MERIDIAN_VS_COLLATERAL_TABLE:
    short_mer = mer.split(" - ")[0].split(",")[0]
    short_col = col.split(" - ")[0].split(",")[0]
    c.drawString(ML, y, aspect)
    c.drawString(ML + col_w[0], y, short_mer[:34])
    c.drawString(ML + col_w[0] + col_w[1], y, short_col[:34])
    y -= 10.5

end_page()

# ============= PAGE 3: 12 MERIDIANS TABLE + CIRCUITS =============
new_page(f"12 Meridians & 3 Circuits")
y = H - HEADER_H - 24
y = section_rule(y, "The 12 Primary Meridians", width=220)
setfill(NAVY); c.setFont("Lora-Bold", 8)
c.drawString(ML, y, "Ab"); c.drawString(ML + 30, y, "Name"); c.drawString(ML + 150, y, "Classification")
c.drawString(ML + 280, y, "Direction"); c.drawString(ML + 400, y, "Circuit")
y -= 12
for ab, name, cls, pol, direction, circuit in TWELVE_MERIDIANS:
    if row_num[0] % 2 == 0:
        setfill(ROW_TINT); c.rect(ML - 4, y - 3, CW + 8, 12, fill=1, stroke=0)
    row_num[0] += 1
    setfill(RED); c.setFont("Lora-Bold", 8); c.drawString(ML, y, ab)
    setfill(DARK); c.setFont("Lora", 8)
    c.drawString(ML + 30, y, name)
    c.drawString(ML + 150, y, cls)
    c.drawString(ML + 280, y, direction)
    c.drawString(ML + 400, y, circuit)
    y -= 12.5
y -= 14

y = section_rule(y, "The 3 Circuits", width=140)
for circuit_name, position, members, elements in CIRCUITS:
    accent = CIRCUIT_COLORS[circuit_name]
    setfill(accent); c.rect(ML, y - 2, CW, 2.5, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML, y - 14, f"{circuit_name} ({position})")
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    c.drawRightString(ML + CW, y - 14, elements)
    y -= 26
    setfill(DARK); c.setFont("Lora", 8.6)
    seq = "  ->  ".join(members)
    lines = wrap_words(seq, "Lora", 8.6, CW - 4)
    for l in lines:
        c.drawString(ML, y, l); y -= 11.5
    y -= 8

end_page()

# ============= PAGE 4: DIRECTION, MEETING POINTS, CLOCK, FUNCTIONS =============
new_page(f"Circulation, Clock & Functions")
y = H - HEADER_H - 24
y = section_rule(y, "Direction of Qi Flow", width=200)
setfill(DARK); c.setFont("Lora", 8.8)
for rule, direction in DIRECTION_RULES:
    setfill(NAVY); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML, y, rule)
    setfill(RED); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML + 230, y, direction)
    y -= 13
y -= 10

y = section_rule(y, "Where Meridians Meet", width=200)
for pair, location, note in MEETING_POINTS:
    setfill(NAVY); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML, y, f"{pair} {location}")
    y -= 11
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    for l in wrap_words(note, "Lora-Italic", 8, CW - 10):
        c.drawString(ML + 10, y, l); y -= 10.5
    y -= 3
y -= 8

col_w = (CW - 20) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "Meridian Clock (24 hr)")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 150, y)
y -= 13
c.setFont("Lora-Bold", 8.3)
for ab, tm in MERIDIAN_CLOCK:
    elem = CLOCK_ELEMENT[ab]
    setfill(ELEMENT_COLORS[elem])
    c.rect(ML, y - 1, 7, 7, fill=1, stroke=0)
    setfill(ELEMENT_COLORS[elem]); c.setFont("Lora-Bold", 8.3)
    c.drawString(ML + 11, y, ab)
    setfill(DARK); c.setFont("Lora", 8.3)
    c.drawString(ML + 32, y, f": {tm}")
    y -= 11.5
setfill(GRAY); c.setFont("Lora-Italic", 6.8)
c.drawString(ML, y - 2, "Metal / Earth / Fire / Water / Wood + Ministerial Fire (PC/SJ)")
left_bottom = y - 12

y2 = top_y; x2 = ML + col_w + 20
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(x2, y2, "3 Functions of Meridians")
y2 -= 4
setstroke(GOLD); c.line(x2, y2, x2 + 150, y2)
y2 -= 13
setfill(DARK); c.setFont("Lora", 8.3)
for name, desc in FUNCTIONS_OF_MERIDIANS:
    setfill(RED); c.setFont("Lora-Bold", 8.3); c.drawString(x2, y2, name); y2 -= 10.5
    setfill(DARK); c.setFont("Lora", 8)
    for l in wrap_words(desc, "Lora", 8, col_w - 4):
        c.drawString(x2, y2, l); y2 -= 10
    y2 -= 4
right_bottom = y2
y = min(left_bottom, right_bottom)

y -= 10
setstroke(GOLD); c.setLineWidth(HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 16

# ============= RAPID RECALL (continues on same page if room, else new page) =============
if y < 260:
    end_page()
    row_num[0] = 0
    new_page(f"Rapid Recall")
    y = H - HEADER_H - 24

setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, "Rapid Recall \u2014 Channel Theory")
y -= 14
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawString(ML, y, "Read this one last, on the way in")
y -= 20

y = section_rule(y, "The \u201cONLY\u201d List", width=180)
only_list = [
    ("Term for the whole system (meridians + collaterals)", "Channels"),
    ("Number of Zang (Yin) organs", "6"),
    ("Number of Fu (Yang) organs", "6"),
    ("Total collaterals (12 primary + Du + Ren + Spleen's Great Luo)", "15"),
    ("Circuit containing HT, SI, BL, KI", "Inner (Posterior)"),
    ("Circuit containing PC, SJ, GB, LR", "Middle"),
]
for fact, ans in only_list:
    lines = wrap_words(fact, "Lora", 8.6, CW - 150)
    setfill(DARK); c.setFont("Lora", 8.6)
    for i, l in enumerate(lines):
        c.drawString(ML, y - i * 10.8, l)
    setfill(RED); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + CW - 140, y, ans)
    y -= len(lines) * 10.8 + 4
y -= 12

y = section_rule(y, "Exam Traps", width=140)
setfill(DARK); c.setFont("Lora", 8.5)
traps = [
    "'Meridians' means the 12 Primary Meridians specifically. 'Channels' is the whole system - meridians AND collaterals.",
    "The location-based names (Taiyin/Yangming = anterior, etc.) describe medial/lateral POSITION on the limb, not organ function - don't conflate the two.",
    "Direction of flow depends on BOTH hand/foot AND yin/yang together - all four combinations are different (chest->hand, hand->head, head->foot, foot->chest).",
    "The Middle Circuit's Yang channel is San Jiao (Triple Burner/Trample Burner), not to be confused with Small Intestine.",
]
for t in traps:
    lines = wrap_words("\u2022 " + t, "Lora", 8.5, CW - 4)
    for l in lines:
        c.drawString(ML, y, l); y -= 11
    y -= 3

end_page()

c.save()
print("SAVED:", OUT)
