#!/usr/bin/env python3
"""AC300 Master Map -- the 1-page channel skeleton (+ blank retrieval page).
Standalone doc: 12-channel sequence, 3 circuits, Yin/Yang direction rules,
channel positioning. Built per Jon's request after the ChatGPT study-system
conversation (Phase 1: 'build the skeleton before memorizing points').
Print + reMarkable editions."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from shared_data import CHANNELS, COLORS, ATTR, CIRCUITS, DIRECTION

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
    OUT = "/mnt/user-data/outputs/AC300_MasterMap_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    CARD_BG = (0.960, 0.962, 0.968)
    OUT = "/mnt/user-data/outputs/AC300_MasterMap_Print.pdf"
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


ML, MR = 40, 40
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(title, subtitle):
    page_bg()
    setfill(NAVY); c.rect(0, H - 62, W, 62, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - 62, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 16)
    c.drawString(ML, H - 32, title)
    setfill(GOLD); c.setFont("Lora-Italic", 9)
    c.drawRightString(W - MR, H - 20, EDLABEL)
    setfill((0.85, 0.88, 0.93)); c.setFont("Lora-Italic", 9.5)
    c.drawString(ML, H - 50, subtitle)
    return H - 84


def footer(label):
    setstroke(GOLD); c.setLineWidth(0.7 * LW_MULT)
    c.line(ML, 30, W - MR, 30)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 18, f"AC300/AC375 \u00b7 Master Map \u00b7 VUIM Summer 2026 \u00b7 {label} \u00b7 p.{page_num[0]}")


def end_page(label):
    footer(label); c.showPage(); page_num[0] += 1


def section_tag(y, title, color=NAVY):
    setfill(color); c.rect(ML, y - 18, 4, 18, fill=1, stroke=0)
    setfill(color); c.setFont("Lora-Bold", 11.5)
    c.drawString(ML + 12, y - 13, title)
    return y - 26


# ======================================================================
# PAGE 1 -- REFERENCE (filled)
# ======================================================================
y = header("AC300 Master Map", "The 12-channel skeleton \u2014 memorize this before memorizing points")

setfill((0.30, 0.30, 0.30)); c.setFont("Lora-Italic", 8.4)
for l in wrap_words("Per the ChatGPT study-system conversation: 'For every channel you should eventually answer six things without looking.' This page is the skeleton that makes those six things deducible instead of memorized one at a time.", "Lora-Italic", 8.4, CW):
    c.drawString(ML, y, l); y -= 10.8
y -= 10

# --- The Sequence ---
y = section_tag(y, "1.  THE SEQUENCE  (write this from memory every session)")
seq_h = 46
setfill(CARD_BG); c.rect(ML, y - seq_h, CW, seq_h, fill=1, stroke=0)
n = len(CHANNELS)
cell_w = (CW - 20) / n
cx = ML + 10
cy = y - 20
for i, ch in enumerate(CHANNELS):
    setfill(COLORS[ch]); c.circle(cx + cell_w * i + cell_w / 2 - 8, cy, 13, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 8.6)
    c.drawCentredString(cx + cell_w * i + cell_w / 2 - 8, cy - 3, ch)
    if i < n - 1:
        setfill(DARK); c.setFont("Lora-Bold", 9)
        c.drawCentredString(cx + cell_w * i + cell_w - 2, cy - 3, "->")
setfill(GRAY); c.setFont("Lora-Italic", 7.6)
c.drawCentredString(W / 2, y - seq_h + 10, "LR -> (loops back to) LU  \u2014  the Qi cycle is closed, 24-hour clock")
y -= seq_h + 16

# --- The Cycle ---
y = section_tag(y, "2.  THE CYCLE  (every channel is part of this loop)")
cyc_h = 34
setfill(CARD_BG); c.rect(ML, y - cyc_h, CW, cyc_h, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawCentredString(W / 2, y - 22, "Chest  ->  Hand  ->  Head  ->  Foot  ->  Chest")
y -= cyc_h + 16

# --- Direction Rules ---
y = section_tag(y, "3.  YIN/YANG DIRECTION RULES  (deduce direction from category)")
rows = [
    ("Hand-Yin", DIRECTION["Hand-Yin"], "LU, HT, PC"),
    ("Hand-Yang", DIRECTION["Hand-Yang"], "LI, SI, SJ"),
    ("Foot-Yang", DIRECTION["Foot-Yang"], "ST, BL, GB"),
    ("Foot-Yin", DIRECTION["Foot-Yin"], "SP, KI, LR"),
]
row_h = 22
hdr_h = 16
setfill(NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 8.5)
c.drawString(ML + 10, y - hdr_h + 5, "CATEGORY")
c.drawString(ML + 160, y - hdr_h + 5, "DIRECTION")
c.drawString(ML + 340, y - hdr_h + 5, "CHANNELS")
y -= hdr_h
for i, (cat, direc, chs) in enumerate(rows):
    bg = CARD_BG if i % 2 == 0 else (1, 1, 1) if not IS_RM else PAGE_BG
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 10, y - row_h + 7, cat)
    setfill(RED); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 160, y - row_h + 7, direc)
    setfill(DARK); c.setFont("Lora", 9.5)
    c.drawString(ML + 340, y - row_h + 7, chs)
    y -= row_h
setstroke(GRAY); c.setLineWidth(0.5)
c.rect(ML, y, CW, hdr_h + row_h * len(rows), fill=0, stroke=1)
y -= 18

# --- The 3 Circuits ---
y = section_tag(y, "4.  THE 3 CIRCUITS")
circ_h = 30
for name, chs, tint in CIRCUITS:
    setfill(tuple(min(1, ch + 0.75) for ch in tint)); c.rect(ML, y - circ_h, CW, circ_h, fill=1, stroke=0)
    setfill(tuple(max(0, ch - 0.05) for ch in tint)); c.rect(ML, y - circ_h, 4, circ_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 12, y - 13, name)
    setfill(DARK); c.setFont("Lora", 9.5)
    c.drawString(ML + 190, y - 13, " -> ".join(chs) + "  (chest -> hand -> head -> foot -> chest)")
    y -= circ_h + 6
y -= 6

setfill(RED); c.setFont("Lora-BoldItalic", 8.6)
for l in wrap_words("How to use: fill this whole page from a blank sheet before every study session. Once it's automatic, questions like \"SJ: hand or foot? Yin or Yang? Direction? Pair?\" become deductive instead of brute-force recall.", "Lora-BoldItalic", 8.6, CW):
    c.drawString(ML, y, l); y -= 10.6

end_page("Reference Page")

# ======================================================================
# PAGE 2 -- BLANK RETRIEVAL PRACTICE
# ======================================================================
y = header("Master Map \u2014 Blank Retrieval", "Close page 1. Fill this from memory. Check after, don't peek during.")

y = section_tag(y, "1.  THE SEQUENCE  (fill in all 12, in order)")
seq_h = 46
setfill(CARD_BG); c.rect(ML, y - seq_h, CW, seq_h, fill=1, stroke=0)
cell_w = (CW - 20) / 12
cx = ML + 10
cy = y - 20
for i in range(12):
    setstroke(GRAY); c.setLineWidth(0.8)
    c.circle(cx + cell_w * i + cell_w / 2 - 8, cy, 13, fill=0, stroke=1)
    if i < 11:
        setfill(DARK); c.setFont("Lora-Bold", 9)
        c.drawCentredString(cx + cell_w * i + cell_w - 2, cy - 3, "->")
setfill(GRAY); c.setFont("Lora-Italic", 7.6)
c.drawCentredString(W / 2, y - seq_h + 10, "hint: starts with LU, loops back to LU")
y -= seq_h + 16

y = section_tag(y, "2.  THE CYCLE  (fill in the 4 body regions)")
cyc_h = 34
setfill(CARD_BG); c.rect(ML, y - cyc_h, CW, cyc_h, fill=1, stroke=0)
setfill(GRAY); c.setFont("Lora", 12)
labels = ["_______", "->", "_______", "->", "_______", "->", "_______", "->", "_______"]
tx = ML + 30
for lab in labels:
    c.drawString(tx, y - 22, lab)
    tx += pdfmetrics.stringWidth(lab + "  ", "Lora", 12) + 6
y -= cyc_h + 16

y = section_tag(y, "3.  YIN/YANG DIRECTION RULES  (fill in direction + 3 channels each)")
row_h = 26
hdr_h = 16
setfill(NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 8.5)
c.drawString(ML + 10, y - hdr_h + 5, "CATEGORY")
c.drawString(ML + 160, y - hdr_h + 5, "DIRECTION")
c.drawString(ML + 340, y - hdr_h + 5, "CHANNELS")
y -= hdr_h
for i, cat in enumerate(["Hand-Yin", "Hand-Yang", "Foot-Yang", "Foot-Yin"]):
    bg = CARD_BG if i % 2 == 0 else (1, 1, 1) if not IS_RM else PAGE_BG
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 10, y - row_h + 10, cat)
    setstroke(GRAY); c.setLineWidth(0.6)
    c.line(ML + 160, y - row_h + 8, ML + 320, y - row_h + 8)
    c.line(ML + 340, y - row_h + 8, RX if False else (W - MR - 10), y - row_h + 8)
    y -= row_h
setstroke(GRAY); c.setLineWidth(0.5)
c.rect(ML, y, CW, hdr_h + row_h * 4, fill=0, stroke=1)
y -= 18

y = section_tag(y, "4.  THE 3 CIRCUITS  (fill in the 4 channels for each)")
circ_h = 32
for name, _, tint in CIRCUITS:
    setfill(tuple(min(1, ch + 0.75) for ch in tint)); c.rect(ML, y - circ_h, CW, circ_h, fill=1, stroke=0)
    setfill(tuple(max(0, ch - 0.05) for ch in tint)); c.rect(ML, y - circ_h, 4, circ_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 12, y - 14, name)
    setstroke(GRAY); c.setLineWidth(0.6)
    c.line(ML + 190, y - 14, W - MR - 20, y - 14)
    y -= circ_h + 6
y -= 10

setfill(GRAY); c.setFont("Lora-Italic", 8.4)
for l in wrap_words("Self-check: flip back to page 1 and grade yourself. Anything you hesitated on is Level A material -- redo this page tomorrow before touching a study guide.", "Lora-Italic", 8.4, CW):
    c.drawString(ML, y, l); y -= 10.6

end_page("Blank Retrieval Page")

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
