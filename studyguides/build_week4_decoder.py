#!/usr/bin/env python3
"""AC300 Week 4 Special Points Decoder - HT & SI. Builds BOTH Print and reMarkable editions."""
import sys
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
FIRE = (0.690, 0.204, 0.169)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Week4_SpecialPointsDecoder_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Week4_SpecialPointsDecoder_Print.pdf"
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
    c.drawString(36, H - HEADER_H + 15, "AC300/AC375  |  Week 4  |  Special Points Decoder  |  VUIM Summer 2026")
    c.setFont("Lora-Italic", 9)
    c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer(label):
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(36, 34, W - 36, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Week 4 Special Points Decoder  \u00b7  VUIM Summer 2026  \u00b7  {label}")


ML, MR = 36, 36
CW = W - ML - MR

# ============= PAGE 1: COVER =============
page_bg()
header(EDLABEL)
y = H - HEADER_H - 40
setfill(GOLD); c.rect(ML, y - 4, 120, 22, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10)
c.drawCentredString(ML + 60, y + 3, "WEEK 4")
y -= 50
setfill(NAVY); c.setFont("Lora-Bold", 24)
c.drawString(ML, y, "Special Points Decoder")
y -= 26
setfill(RED); c.setFont("Lora-BoldItalic", 14)
c.drawString(ML, y, "Heart & Small Intestine Channels")
y -= 20
setfill(DARK); c.setFont("Lora", 11)
c.drawString(ML, y, "HT (9 pts) + SI (19 pts) = 28 Points")
y -= 34

setfill(NAVY); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "This Document Contains:")
y -= 18
bullets = [
    "Every special-point CATEGORY explained in plain terms",
    "Five-Shu (Jing-Well through He-Sea) with yin/yang elements",
    "Yuan-Source, Luo, Xi-Cleft, Confluent, Back-Shu, Front-Mu",
    "Lower He-Sea, Hui-Meeting, Crossing points",
    "Worked HT & SI examples for every category",
]
setfill(DARK); c.setFont("Lora", 9.5)
for b in bullets:
    c.drawString(ML + 10, y, "\u2022  " + b)
    y -= 15

y -= 14
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
c.rect(ML, y - 58, CW, 58, fill=1, stroke=0)
setfill(RED); c.setFont("Lora-Bold", 9.5)
c.drawString(ML + 12, y - 18, "QUIZ 4 (next class) covers: HT & SI channels")
setfill(DARK); c.setFont("Lora", 9)
c.drawString(ML + 12, y - 34, "MIDTERM (Week 5) covers Weeks 1-4 cumulative \u2014 many midterm questions reuse quiz material.")
c.drawString(ML + 12, y - 48, "MOA: HT pp.208-221  |  SI pp.222-249   \u00b7   CAM: HT/SI color figures")

y -= 80
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawString(ML, y, "Dr. Vivian Zhang, Ph.D.  \u00b7  Jon Centeno, D.AcHM Candidate  \u00b7  VUIM")

footer("Page 1")
c.showPage()

# ============= PAGE 2+: DECODER TABLE =============
page_bg()
header(f"Week 4  \u00b7  HT & SI Channels  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Special Points Decoder \u2014 What Each Category Actually Means")
y -= 15
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
for line in [
    "HT & SI examples",
    "Know the CATEGORY, not just the point. Every point below is defined by what its category does in the body.",
    "The Five-Shu elements differ on yin vs yang channels - both are noted where they apply.",
]:
    c.drawString(ML, y, line)
    y -= 11
y -= 6

CATS = [
    ("Jing-Well", "Wood",
     "Where channel Qi begins to bubble up; most distal point (fingertip/toe-tip). Used for acute conditions, mental restlessness, and reviving consciousness.",
     "HT9 Shaochong | SI1 Shaoze"),
    ("Ying-Spring", "Fire (yin) / Water (yang)",
     "Qi glides like a shallow spring; just distal to the MCP joint. Clears heat from the channel and its organ.",
     "HT8 Shaofu (clears heart fire) | SI2 Qiangu"),
    ("Shu-Stream", "Earth (yin) / Wood (yang)",
     "Qi pours down a stream; on yin channels this point doubles as the Yuan-Source. Treats heaviness, joint pain, and intermittent chronic disease.",
     "HT7 Shenmen (= Yuan-Source) | SI3 Houxi (also Confluent)"),
    ("Jing-River", "Metal (yin) / Fire (yang)",
     "Qi flows abundantly like a river, near the wrist. Treats cough, asthma, chills-and-fever, and disorders of voice.",
     "HT4 Lingdao | SI5 Yanggu"),
    ("He-Sea", "Water (yin) / Earth (yang)",
     "Qi collects and enters deep toward the organ, like a river reaching the sea; at the elbow. Best for the Fu organ itself and for rebellious Qi.",
     "HT3 Shaohai (clears heart fire, fear/arm pain) | SI8 Xiaohai"),
    ("Yuan-Source", None,
     "The point where the organ's primary (source) Qi surfaces. Tonifies and regulates the organ directly; pairs with the Luo of the coupled channel (Host-Guest technique).",
     "HT7 Shenmen | SI4 Wangu (wrist/finger pain, febrile disease)"),
    ("Luo-Connecting", None,
     "The junction that links a channel to its interior-exterior partner. Treats disorders of BOTH channels and its own symptom pair (excess/deficiency).",
     "HT5 Tongli | SI7 Zhizheng"),
    ("Xi-Cleft", None,
     "A deep cleft where Qi and Blood pool. THE point for acute, painful, and sudden flare-ups; yin-channel Xi-Cleft points also treat bleeding.",
     "HT6 Yinxi (night sweats, acute heart pain) | SI6 Yanglao"),
    ("Confluent", None,
     "Opens one of the Eight Extraordinary Vessels. Paired across two channels to command that vessel (the Host-Guest pairing of the extraordinary system).",
     "SI3 Houxi opens the DU MAI (pairs with BL62) \u2014 HT has no confluent point"),
    ("Command (Four/Six)", None,
     "A point that \u2018commands\u2019 a whole body region regardless of channel theory - memorize by region. Neither HT nor SI holds a Command point.",
     "LI4 = Command of Face/Mouth (Wk 2) | ST36 = Command of Abdomen (Wk 3)"),
    ("Lower He-Sea", None,
     "The true He-Sea for the six Fu organs, all found on the LEG yang channels. Where you treat the Fu organ even when its own channel is on the arm.",
     "SI's Lower He-Sea = ST39 Xiajuxu (on the ST channel, not SI itself)"),
    ("Back-Shu", None,
     "Points on the Bladder channel beside the spine that transport Qi to a specific organ. Diagnostic (tenderness) and tonifying for chronic organ patterns.",
     "BL15 Xinshu (Heart) | BL27 Xiaochangshu (Small Intestine)"),
    ("Front-Mu", None,
     "Points on the chest/abdomen where an organ's Qi gathers on the front of the body. Pairs with the Back-Shu (Shu-Mu technique); best for acute conditions.",
     "CV14 Juque (Heart) | CV4 Guanyuan (Small Intestine)"),
    ("Hui-Meeting", None,
     "Eight influential points, each governing one tissue or substance (Qi, Blood, sinew, vessel, bone, marrow, Zang, Fu). Not on the HT/SI channels but tested as a category.",
     "e.g. CV17 = Hui of Qi | LU9 = Hui of Vessels (Wk 2)"),
    ("Crossing (Meeting)", None,
     "Where two or more channels intersect; one needle treats every channel that crosses there.",
     "HT has ZERO crossing points \u2014 the only primary channel with none. SI crosses BL1 and GB14 near the face/eye."),
]

row_i = [0]


def ensure_space(needed):
    global y
    if y - needed < 40:
        footer(f"Page {page_num[0]}")
        c.showPage()
        page_num[0] += 1
        page_bg()
        header(f"Week 4  \u00b7  HT & SI Channels  \u00b7  {EDLABEL}")
        y = H - HEADER_H - 26


page_num = [2]

for cat, elem, desc, ex in CATS:
    head_lines = wrap_words(desc, "Lora", 8.5, CW - 190)
    ex_lines = wrap_words(ex, "Lora-Bold", 8.3, 175)
    n_lines = max(len(head_lines) + (1 if elem else 0), len(ex_lines))
    LH = 10.8
    needed = n_lines * LH + 6
    ensure_space(needed)

    band_h = needed - 1
    if row_i[0] % 2 == 0:
        setfill(ROW_TINT)
        c.rect(ML - 4, y - band_h + 6, CW + 8, band_h, fill=1, stroke=0)
    row_i[0] += 1

    top_y = y
    setfill(NAVY); c.setFont("Lora-Bold", 9.3)
    c.drawString(ML, top_y, cat)
    yy = top_y
    if elem:
        yy -= LH
        setfill(FIRE); c.setFont("Lora-Italic", 8)
        c.drawString(ML, yy, elem)
    yy -= LH
    setfill(DARK); c.setFont("Lora", 8.5)
    for hl in head_lines:
        c.drawString(ML, yy, hl)
        yy -= LH

    ex_y = top_y
    setfill(RED); c.setFont("Lora-Bold", 8.3)
    for el in ex_lines:
        c.drawRightString(ML + CW, ex_y, el)
        ex_y -= LH

    y = min(yy, ex_y) - 3

footer(f"Page {page_num[0]}")
c.showPage()
c.save()
print("SAVED:", OUT)
