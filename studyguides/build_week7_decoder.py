#!/usr/bin/env python3
"""AC300 Week 7 Special Points Decoder -- standalone. Week 7 (Extraordinary
Vessels) introduces TWO special point categories not seen on the primary
meridians: Confluent (Opening) Points and Coalescent Points. This decoder
leads with those two, drillable in full, then gives a brief cumulative
recap of the organ-based categories from Weeks 1-6 (not new this week,
included for continuity). Print + reMarkable."""
import sys
sys.path.insert(0, "/home/claude/ac300wk7")
from common_wk7 import (DocBuilder, setfill, setstroke, box, hairline, draw_paragraph,
                         wrap_words, draw_image_contain, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED,
                         LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM,
                         EDLABEL)
from wk7_content import ALL_VESSELS, CONFLUENT_PAIRS, NO_ORGAN_NOTE

OUT = f"/mnt/user-data/outputs/AC300_Week7_SpecialPointsDecoder_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 7 Special Points Decoder"
FOOTER = "AC300/AC375 | Week 7 Special Points Decoder | Eight Extraordinary Vessels | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def title_bar(title, subtitle_right=None):
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, NAVY); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 14)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        c.setFont("Lora-Italic", 8.5)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot - 12


# ============================================================
# COVER
# ============================================================
db.new_page(bare=True)
y = H - 60
setfill(c, GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "WEEK 7")
c.setFont("Lora-Italic", 10)
c.drawRightString(RX, y, EDLABEL)
y -= 40
setfill(c, NAVY); c.setFont("Lora-Bold", 28)
c.drawString(ML, y, "Special Points Decoder")
y -= 28
setfill(c, RED); c.setFont("Lora-Bold", 17)
c.drawString(ML, y, "Confluent & Coalescent Points \u2014 the Extraordinary Vessels")
y -= 22
setfill(c, GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "Standalone reference \u2014 pairs with the Week 7 Study Guide")
y -= 18
hairline(c, ML, y, RX, rgb=GOLD, w=1.2)
y -= 28
setfill(c, RED); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Decoder Covers:")
y -= 20
setfill(c, DARK); c.setFont("Lora", 10.5)
bullets = [
    "Confluent (Opening) Points \u2014 the special-point category unique to the 8 vessels; all 4 master-couple pairs drilled in full",
    "Coalescent Points (Jiao Hui Xue) \u2014 how 6 of the 8 vessels borrow points from primary meridians",
    "Why organ-based special-point categories (Yuan-Source, Luo-Connecting, etc.) do NOT apply this week",
    "Cumulative one-page recap of every special-point category from Weeks 1-6, for continuity",
]
for b in bullets:
    setfill(c, GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(c, DARK)
    lines = wrap_words(b, "Lora", 10.5, CW - 20)
    for i, l in enumerate(lines):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(lines)) + 4

y -= 8
box_h = 50
box(c, ML, y, CW, box_h, tint(GOLD, 0.88))
setfill(c, DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 16, y - 18, "No new organ-based special points this week -- GV/CV/Chong/Dai/Qiao/Wei pertain to no zang-fu organ.")
c.drawString(ML + 16, y - 32, "Confluent Points ARE the special-point content for Quiz 6.")
y -= box_h + 40
setfill(c, GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
db.end_page()

# ============================================================
# PAGE: Confluent Points -- full drillable content
# ============================================================
db.new_page()
y = title_bar("Confluent Points (Ba Mai Jiao Hui Xue)", "The star category this week")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c,
    "DEFINITION: Confluent points are special acupuncture points -- always located on a primary "
    "meridian, one per vessel -- that connect each Extraordinary Vessel to the 12 regular meridians. "
    "They are the clinical \u201copening\u201d points used to access that vessel's function, and they pair up "
    "into 4 \u201cmaster-couple\u201d combinations used together in treatment.",
    ML, y, CW, size=9.3, leading=12.5)
y -= 8
setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 7.8)
from wk7_content import CONFLUENT_POINTS_MOA_NOTE
y = draw_paragraph(c, CONFLUENT_POINTS_MOA_NOTE, ML, y, CW, font="Lora-Italic", size=7.8, leading=10)
y -= 6

for pair_name, master, couple, note in CONFLUENT_PAIRS:
    box_h = 56
    box(c, ML, y, CW, box_h, LBLUE)
    setfill(c, GOLD); c.rect(ML, y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 14, y - 15, pair_name)
    setfill(c, RED); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 14, y - 30, master + "   \u00d7   " + couple)
    setfill(c, GRAY); c.setFont("Lora-Italic", 8.2)
    draw_paragraph(c, note, ML + 14, y - 44, CW - 24, font="Lora-Italic", size=8.2, leading=10.6)
    y -= box_h + 8

y -= 6
setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "MEMORY AID")
y -= 13
setfill(c, DARK); c.setFont("Lora-Italic", 8.6)
y = draw_paragraph(c,
    "All 4 pairs put one point on the ARM and one on the LEG. The arm point is always the vessel's "
    "confluent point on a Yin (Lung/Pericardium) or Yang (Small Intestine/San Jiao) hand meridian; "
    "the leg point mirrors it on the corresponding foot meridian territory (Kidney/Spleen for the "
    "yin pairs, Bladder/Gallbladder for the yang pairs).",
    ML, y, CW, font="Lora-Italic", size=8.6, leading=11)

db.end_page()

# ============================================================
# PAGE: Confluent Points -- individual location cards (new, from
# 2026AC300Lecture_8Vivian.pdf slides 8-9, real point diagrams)
# ============================================================
db.new_page()
y = title_bar("Confluent Points \u2014 Location Cards", "New for this edition -- Dr. Zhang's own review slides")
y -= 6

from wk7_content import CONFLUENT_POINT_DETAIL
point_order = ["SI 3  Houxi", "LU 7  Lieque", "SP 4  Gongsun", "GB 41  Zulinqi",
               "KI 6  Zhaohai", "BL 62  Shenmai", "PC 6  Neiguan", "SJ 5  Waiguan"]

col_w = (CW - 14) / 2
card_h = 118
for i, pt in enumerate(point_order):
    d = CONFLUENT_POINT_DETAIL[pt]
    col = i % 2
    row = i // 2
    x0 = ML + col * (col_w + 14)
    yy = y - row * (card_h + 10)
    box(c, x0, yy, col_w, card_h, tint(GOLD, 0.93))
    img_w = 78
    draw_image_contain(c, d["figure"], x0 + 6, yy - 6, img_w, card_h - 12, GOLD_DARK)
    tx = x0 + img_w + 16
    setfill(c, RED); c.setFont("Lora-Bold", 10.5)
    c.drawString(tx, yy - 16, pt)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawString(tx, yy - 27, d["vessel"])
    setfill(c, DARK); c.setFont("Lora-Bold", 7.4)
    c.drawString(tx, yy - 41, "LOCATION")
    setfill(c, DARK); c.setFont("Lora", 7.4)
    ty = yy - 52
    for ln in wrap_words(d["location"], "Lora", 7.4, col_w - img_w - 22):
        c.drawString(tx, ty, ln); ty -= 9.6
    ty -= 4
    setfill(c, DARK); c.setFont("Lora-Bold", 7.4)
    c.drawString(tx, ty, "KEY FUNCTIONS"); ty -= 10.5
    setfill(c, DARK); c.setFont("Lora", 7.2)
    for ln in wrap_words(d["functions"], "Lora", 7.2, col_w - img_w - 22):
        c.drawString(tx, ty, ln); ty -= 9.4

y -= 4 * (card_h + 10) - 10
db.end_page()

# ============================================================
# PAGE: Coalescent Points -- full drillable content
# ============================================================
db.new_page()
y = title_bar("Coalescent Points (Jiao Hui Xue)", "How the vessels without their own points work")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c,
    "DEFINITION: Coalescent points are the meeting points between an Extraordinary Vessel and a "
    "primary meridian along the vessel's course. Only GV and CV have their own dedicated points -- "
    "the other 6 vessels are described ENTIRELY through the primary-meridian points they cross. "
    "Do not confuse a vessel's coalescent points (many, descriptive of its course) with its ONE "
    "confluent point (the clinical opening point).",
    ML, y, CW, size=9.3, leading=12.5)
y -= 16

setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Coalescent Points by Vessel")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=0.8)
y -= 14

for v in ALL_VESSELS:
    accent = v["accent"]
    label = f"{v['name']} ({v['pinyin']})"
    coal = "  \u00b7  ".join(v["coalescent_points"])
    lines = wrap_words(coal, "Lora", 8.2, CW - 16)
    row_h = 14 + len(lines) * 10.6 + (10 if v.get("coalescent_flag") else 2)
    box(c, ML, y, CW, row_h, tint(accent, 0.9))
    setfill(c, accent); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML + 8, y - 12, label + f"  ({len(v['coalescent_points'])} pts)"
                 if v["coalescent_points"] else label)
    setfill(c, DARK); c.setFont("Lora", 8.2)
    ty = y - 24
    for l in lines:
        c.drawString(ML + 8, ty, l); ty -= 10.6
    if v.get("coalescent_flag"):
        setfill(c, RED); c.setFont("Lora-Italic", 7.4)
        c.drawString(ML + 8, ty - 2, "\u2022 " + v["coalescent_flag"])
    y -= row_h + 6

db.end_page()

# ============================================================
# PAGE: Why organ-based categories don't apply + cumulative recap
# ============================================================
db.new_page()
y = title_bar("Cumulative Recap \u2014 Categories NOT New This Week", "For continuity only")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c, NO_ORGAN_NOTE, ML, y, CW, size=9.3, leading=12.5)
y -= 6
y = draw_paragraph(c,
    "Because none of the 8 vessels pertains to a zang/fu organ, the organ-based special-point "
    "categories drilled in earlier weeks' decoders (Yuan-Source, Luo-Connecting, Xi-Cleft, He-Sea, "
    "Lower He-Sea, Front-Mu, Back-Shu, Hui-Meeting, Jing-Well/Ying-Spring/Shu-Stream/Jing-River, "
    "Command Points) do not introduce new examples this week. They stay exactly as covered "
    "previously -- listed below strictly for cumulative review continuity.",
    ML, y, CW, size=9, leading=12)
y -= 16

RECAP = [
    ("YUAN-SOURCE", "Where the Source (Yuan) Qi is accessed.", "Last new examples: Week 6 (PC7, SJ4, GB40, LR3)"),
    ("LUO-CONNECTING", "Where a Luo-vessel branches to the paired channel.", "Last new examples: Week 6 (PC6, SJ5, GB37, LR5)"),
    ("HE-SEA", "At elbow/knee; treats counterflow Qi and organ-level disorders.", "Last new examples: Week 6 (PC3, SJ10, GB34, LR8)"),
    ("XI-CLEFT", "Cleft point for acute conditions/pain.", "Last new examples: Week 6 (PC4, SJ7, GB36, LR6)"),
    ("FRONT-MU", "Where a zang/fu organ's Qi gathers anteriorly.", "Last new examples: Week 6 (CV17, CV5, GB24, LR14)"),
    ("BACK-SHU", "Bladder-channel transport points for each organ.", "Last new examples: Week 6 (BL14, BL22, BL19, BL18)"),
    ("HUI-MEETING (INFLUENTIAL)", "8 points, meeting place for a tissue/substance category.", "Last new examples: Week 6 (GB34 = Sinews; LR13 = Zang)"),
    ("JING-WELL / YING-SPRING / SHU-STREAM / JING-RIVER", "The Five-Shu points along each channel.", "Last new examples: Week 6"),
    ("LOWER HE-SEA", "Special He-Sea points for the 6 Fu organs, on the leg.", "Last new examples: Week 6 (SJ's is BL39, off-channel)"),
    ("CROSSING POINTS", "A point crossed by more than one channel's pathway.", "GB count still flagged/unresolved (Week 6)"),
]
for cat, defn, last in RECAP:
    row_h = 15 + 10 + 10
    box(c, ML, y, CW, row_h, CARD_BG)
    setfill(c, NAVY); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML + 8, y - 12, cat)
    setfill(c, DARK); c.setFont("Lora", 7.8)
    c.drawString(ML + 8, y - 23, defn)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
    c.drawString(ML + 8, y - 33, last)
    y -= row_h + 4

db.end_page()
db.save()
