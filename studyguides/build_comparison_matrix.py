#!/usr/bin/env python3
"""AC300 Comparison Matrix -- side-by-side quick-drill artifact. Covers the 4
same-category triads (Hand-Yin, Hand-Yang, Foot-Yang, Foot-Yin -- one channel
from each circuit) plus a compact paired-channel table. Cumulative: all 12
primary channels (through Week 6). Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from shared_data import CHANNELS, COLORS, ATTR, TRIADS, LIMB_POSITION, DIRECTION, direction_key

FONT_DIR = "/home/claude/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    CARD_BG = (0.925, 0.902, 0.855)
    OUT = "/mnt/user-data/outputs/AC300_ComparisonMatrix_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    CARD_BG = (0.960, 0.962, 0.968)
    OUT = "/mnt/user-data/outputs/AC300_ComparisonMatrix_Print.pdf"
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


ML, MR = 34, 34
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle):
    page_bg()
    setfill(NAVY); c.rect(0, H - 50, W, 50, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - 50, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 13.5)
    c.drawString(ML, H - 27, "AC300 Comparison Matrix")
    setfill(GOLD); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(W - MR, H - 27, EDLABEL)
    setfill((0.85, 0.88, 0.93)); c.setFont("Lora-Italic", 8.5)
    c.drawString(ML, H - 40, subtitle)
    return H - 64


def footer():
    setstroke(GOLD); c.setLineWidth(0.7 * LW_MULT)
    c.line(ML, 28, W - MR, 28)
    setfill(GRAY); c.setFont("Lora-Italic", 7.3)
    c.drawCentredString(W / 2, 17, f"AC300/AC375 \u00b7 Comparison Matrix \u00b7 VUIM Summer 2026 \u00b7 {EDLABEL} \u00b7 p.{page_num[0]}")


def end_page():
    footer(); c.showPage(); page_num[0] += 1


# ======================================================================
# COVER
# ======================================================================
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 80, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - 45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 62, EDLABEL)

y = H - 130
setfill(NAVY); c.setFont("Lora-Bold", 28)
c.drawCentredString(W / 2, y, "Comparison Matrix")
y -= 26
setfill(RED); c.setFont("Lora-BoldItalic", 14)
c.drawCentredString(W / 2, y, "Side-by-Side Quick-Drill \u2014 All 12 Channels, Cumulative")
y -= 34

setfill(DARK); c.setFont("Lora", 10)
for l in wrap_words("Isolated facts about one channel are 30 disconnected trivia items. Facts placed next to a channel's neighbors become pattern recognition. This document groups the 12 primary channels into the 4 sets that share hand/foot + Yin/Yang category -- one channel from each of the 3 circuits -- plus a compact paired-channel table.", "Lora", 10, CW - 80):
    c.drawCentredString(W / 2, y, l); y -= 13
y -= 14

setfill(NAVY); c.setFont("Lora-Bold", 11.5)
c.drawCentredString(W / 2, y, "This Document Contains:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.2)
for b in [
    "Hand-Yin Triad: LU vs PC vs HT",
    "Hand-Yang Triad: LI vs SJ vs SI",
    "Foot-Yang Triad: ST vs GB vs BL",
    "Foot-Yin Triad: SP vs LR vs KI (incl. the SP/LR crossing-point trap)",
    "Compact paired-channel table -- all 6 pairs, one page",
]:
    c.drawCentredString(W / 2, y, b)
    y -= 15
y -= 10

box_w = 480
box_h = 50
setfill(CARD_BG); c.rect(W / 2 - box_w / 2, y - box_h, box_w, box_h, fill=1, stroke=0)
setfill(RED); c.setFont("Lora-Bold", 9.5)
c.drawCentredString(W / 2, y - 17, "Core attributes verified via existing Master Comparison (Wk1-6)")
setfill(DARK); c.setFont("Lora", 8.8)
c.drawCentredString(W / 2, y - 32, "Limb-position + direction rows are standard CAM/Deadman topography,")
c.drawCentredString(W / 2, y - 44, "labeled as general reference rather than lecture-specific claims.")
y -= box_h + 22

setstroke(GOLD); c.setLineWidth(1)
c.line(50, y, W - 50, y)
y -= 22
c.setFont("Lora-Italic", 9); setfill(GRAY)
c.drawCentredString(W / 2, y, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM Summer 2026")

end_page()


# ======================================================================
# TRIAD PAGES
# ======================================================================
FIELDS = [
    ("Yin/Yang", "yinyang"), ("Hand/Foot", "hf"), ("Element", "elem"),
    ("Direction", None), ("Limb position", None), ("Pair", "pair"),
    ("# Points", "points"), ("Pertains", "pertains"), ("Connects", "connects"),
    ("Yuan-Source", "yuan"), ("Luo-Connecting", "luo"), ("Xi-Cleft", "xi"),
    ("He-Sea", "hesea"), ("Front-Mu", "frontmu"), ("Back-Shu", "backshu"),
    ("Confluent (8EV)", "confluent"),
]

DISTINGUISH = {
    "LU": "1st to receive Qi from food/air (Tai Yin opens); only channel with no crossing points listed",
    "PC": "Zero crossing points (same trap pattern as HT); pathway is the shortest of the 3",
    "HT": "Zero crossing points (same trap pattern as PC); the only Fire (proper) Yin channel",
    "LI": "Zero incoming meeting points; ends beside the nose, handing off to ST -- classic trap",
    "SJ": "Extensive GB overlap (both Shaoyang) -- crosses GB twice at the shoulder",
    "SI": "Longest hand-Yang pathway; scapula zigzag before reaching the face",
    "ST": "Only channel through the nipple; longest primary channel by point count (45)",
    "GB": "Most zigzagging head pathway of any channel; GB34 = He-Sea + Hui-Meeting of Sinews",
    "BL": "Most points of any channel (67); carries all 12 Back-Shu points",
    "SP": "Only channel with a distribution exception -- crosses in front of LR above 8 cun from medial malleolus",
    "LR": "Reaches the vertex (GV20) via its final branch; LR13 = Front-Mu of SP + Hui-Meeting of Zang (2 categories)",
    "KI": "Only medial-leg channel with NO crossing exception -- posterior line throughout",
}

for title, chs, note in TRIADS:
    y = header(f"{title}  \u00b7  " + " vs ".join(chs))
    setfill(GRAY); c.setFont("Lora-Italic", 8.6)
    c.drawString(ML, y, note)
    y -= 20

    n = len(chs)
    label_w = 108
    col_w = (CW - label_w) / n
    hdr_h = 22
    setfill(NAVY); c.rect(ML, y - hdr_h, label_w, hdr_h, fill=1, stroke=0)
    for i, ch in enumerate(chs):
        setfill(COLORS[ch]); c.rect(ML + label_w + i * col_w, y - hdr_h, col_w, hdr_h, fill=1, stroke=0)
        setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
        c.drawCentredString(ML + label_w + i * col_w + col_w / 2, y - hdr_h + 7, ch)
    y -= hdr_h

    row_h = 20
    for ridx, (label, key) in enumerate(FIELDS):
        bg = CARD_BG if ridx % 2 == 0 else ((1, 1, 1) if not IS_RM else PAGE_BG)
        setfill(NAVY); c.rect(ML, y - row_h, label_w, row_h, fill=1, stroke=0)
        setfill((1, 1, 1)); c.setFont("Lora-Bold", 7.6)
        for li, l in enumerate(wrap_words(label, "Lora-Bold", 7.6, label_w - 10)):
            c.drawString(ML + 6, y - row_h + 12 - li * 8.5, l)
        for i, ch in enumerate(chs):
            setfill(bg); c.rect(ML + label_w + i * col_w, y - row_h, col_w, row_h, fill=1, stroke=0)
            if key is not None:
                val = ATTR[ch][key]
            elif label == "Direction":
                val = DIRECTION[direction_key(ch)]
            else:
                val = LIMB_POSITION[ch].split(" -- ")[0]
            setfill(DARK); c.setFont("Lora", 8.4)
            lines = wrap_words(val, "Lora", 8.4, col_w - 8)
            for li, l in enumerate(lines[:2]):
                c.drawCentredString(ML + label_w + i * col_w + col_w / 2, y - row_h + 12 - li * 9, l)
        y -= row_h
    setstroke(GRAY); c.setLineWidth(0.5)
    c.rect(ML, y, CW, hdr_h + row_h * len(FIELDS), fill=0, stroke=1)
    y -= 20

    setfill(RED); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML, y, "Distinguishing features:")
    y -= 14
    for ch in chs:
        setfill(COLORS[ch]); c.circle(ML + 5, y + 3, 4, fill=1, stroke=0)
        setfill(NAVY); c.setFont("Lora-Bold", 8.6)
        c.drawString(ML + 14, y, f"{ch}:")
        setfill(DARK); c.setFont("Lora", 8.6)
        lines = wrap_words(DISTINGUISH[ch], "Lora", 8.6, CW - 50)
        for li, l in enumerate(lines):
            c.drawString(ML + 44, y - li * 10.8, l)
        y -= 10.8 * len(lines) + 6

    end_page()


# ======================================================================
# PAIRED-CHANNEL COMPACT TABLE
# ======================================================================
y = header("Paired-Channel Quick Comparison \u2014 all 6 pairs, one page")
PAIRS = [("LU", "LI"), ("ST", "SP"), ("HT", "SI"), ("BL", "KI"), ("PC", "SJ"), ("GB", "LR")]

col_headers = ["Pair", "Element", "Yin ch.", "Yang ch.", "Yin Yuan", "Yang Yuan", "Yin Luo", "Yang Luo", "Confluent link"]
col_w = [56, 66, 56, 56, 58, 58, 54, 54, 0]
col_w[-1] = CW - sum(col_w[:-1])
hdr_h = 20
x = ML
setfill(NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 7.6)
cx = ML
for w, lab in zip(col_w, col_headers):
    c.drawString(cx + 5, y - hdr_h + 7, lab)
    cx += w
y -= hdr_h

row_h = 44
for ridx, (a, b) in enumerate(PAIRS):
    bg = CARD_BG if ridx % 2 == 0 else ((1, 1, 1) if not IS_RM else PAGE_BG)
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(COLORS[a]); c.rect(ML, y - row_h, 4, row_h, fill=1, stroke=0)
    da, db = ATTR[a], ATTR[b]
    ca, cb = da["confluent"], db["confluent"]
    if ca != "--" and cb != "--":
        conf = f"{ca} / {cb}"
    elif ca != "--":
        conf = ca
    elif cb != "--":
        conf = cb
    else:
        conf = "--"
    vals = [f"{a}-{b}", da["elem"], a, b, da["yuan"], db["yuan"], da["luo"], db["luo"], conf]
    cx = ML
    for i, (w, v) in enumerate(zip(col_w, vals)):
        setfill(NAVY if i == 0 else DARK); c.setFont("Lora-Bold" if i == 0 else "Lora", 8.6 if i == 0 else 8.2)
        lines = wrap_words(str(v), "Lora", 8.2, w - 8)
        for li, l in enumerate(lines[:3]):
            c.drawString(cx + 5, y - 14 - li * 10, l)
        cx += w
    y -= row_h
setstroke(GRAY); c.setLineWidth(0.5)
c.rect(ML, y, CW, hdr_h + row_h * len(PAIRS), fill=0, stroke=1)
y -= 20

setfill(GRAY); c.setFont("Lora-Italic", 8.3)
for l in wrap_words("Note: 'Confluent link' lists every confluent point taught in the pair. PC-SJ and GB-LR each contribute two (different Extraordinary Vessels). LU-LI, ST-SP, HT-SI, BL-KI each contribute one, from only one member of the pair.", "Lora-Italic", 8.3, CW):
    c.drawString(ML, y, l); y -= 10.6

end_page()

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
