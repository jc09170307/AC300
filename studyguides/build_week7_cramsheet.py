#!/usr/bin/env python3
"""AC300 Week 7 Cram Sheet -- dense, text/table-only night-before reference.
Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk7")
from common_wk7 import (DocBuilder, cramsheet_cover, setfill, setstroke, box, hairline,
                         draw_paragraph, wrap_words, section_label, W, H, ML, MR, RX, CW,
                         NAVY, GOLD, GOLD_DARK, RED, LBLUE, GRAYBLUE, DARK, GRAY, LGRAY,
                         WHITE, CARD_BG, tint, EDITION, IS_RM)
from wk7_content import (ALL_VESSELS, GV, CV, CHONG, DAI, YANG_QIAO, YIN_QIAO, YANG_WEI,
                          YIN_WEI, CONFLUENT_PAIRS, ONE_SOURCE_THREE_BRANCHES, NO_ORGAN_NOTE,
                          QUIZ5_REVIEW_TRANSCRIPT_ITEMS)

OUT = f"/mnt/user-data/outputs/AC300_Week7_CramSheet_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 7 Cram Sheet"
FOOTER = "AC300/AC375 | Week 7 Cram Sheet | Eight Extraordinary Vessels | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def block_header(y, title, color):
    setfill(c, color); c.rect(ML, y - 13, CW, 13, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML + 6, y - 10.3, title)
    return y - 17


def vessel_row(y, v):
    """One dense row per vessel: name, sea, points, first/last, coalescent
    count, confluent pair."""
    accent = v["accent"]
    row_h = 30
    setfill(c, tint(accent, 0.88)); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(c, accent); c.rect(ML, y - row_h, 3, row_h, fill=1, stroke=0)
    setfill(c, DARK); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + 10, y - 11, f"{v['name']}  ({v['pinyin']})")
    setfill(c, GRAY)
    sea_txt = v["sea"] or ""
    sea_size = 7.2
    while c.stringWidth(sea_txt, "Lora-Italic", sea_size) > 195 and sea_size > 5.6:
        sea_size -= 0.2
    c.setFont("Lora-Italic", sea_size)
    c.drawString(ML + 10, y - 21, sea_txt)

    col2_x = ML + 205
    setfill(c, DARK); c.setFont("Lora", 7.2)
    if v["own_points"]:
        pts_txt = f"{v['n_points']} pts (own)"
    else:
        pts_txt = "shares primary pts"
    c.drawString(col2_x, y - 11, pts_txt)
    c.drawString(col2_x, y - 21, f"Coalescent: {len(v['coalescent_points'])}")

    col3_x = ML + 340
    setfill(c, accent); c.setFont("Lora-Bold", 7.6)
    c.drawString(col3_x, y - 11, "Confluent: " + v["confluent_point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 6.8)
    pair_lines = wrap_words("pairs " + v["confluent_partner"], "Lora-Italic", 6.8, RX - col3_x - 4)
    ty = y - 20
    for ln in pair_lines[:2]:
        c.drawString(col3_x, ty, ln)
        ty -= 8
    return y - row_h - 3


# ============================================================
# COVER
# ============================================================
cramsheet_cover(
    db,
    points_line="GV 28 pts  \u00b7  CV 24 pts  \u00b7  Chong/Dai/Qiao\u00d72/Wei\u00d72 share primary points",
    box_triplets=[
        ("Only 2 Have Points", GOLD_DARK, ["GV (28) + CV (24)", "the other 6 share pts"]),
        ("4 Confluent Pairs", RED, ["8 points total", "master-couple system"]),
        ("Zero Organs", NAVY, ["no zang/fu pertaining", "no interior-exterior pair"]),
    ],
    extras_line="+ Confluent pairs table \u00b7 one-source-three-branches \u00b7 Quiz 5 MAINT review \u00b7 Homework 5 rubric",
)

# ============================================================
# PAGE 1: Confluent Points table (the highest-yield content) + One Source
# ============================================================
db.new_page()
y = H - 58
setfill(c, NAVY); c.setFont("Lora-Bold", 13.5)
c.drawString(ML, y, "The 4 Confluent (Master-Couple) Pairs")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 16

col_w = (CW - 12) / 2
positions = [(ML, y), (ML + col_w + 12, y)]
for i, (pair_name, master, couple, note) in enumerate(CONFLUENT_PAIRS):
    col = i % 2
    row = i // 2
    x0 = ML + col * (col_w + 12)
    yy = y - row * 100
    box_h = 92
    setfill(c, LBLUE); c.rect(x0, yy - box_h, col_w, box_h, fill=1, stroke=0)
    setfill(c, GOLD); c.rect(x0, yy - box_h, 3, box_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 9.3)
    c.drawString(x0 + 10, yy - 14, pair_name)
    setfill(c, RED); c.setFont("Lora-Bold", 9)
    c.drawString(x0 + 10, yy - 28, master)
    setfill(c, DARK); c.setFont("Lora-Bold", 9)
    c.drawString(x0 + 10, yy - 40, "\u00d7  " + couple)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    draw_paragraph(c, note, x0 + 10, yy - 54, col_w - 20, font="Lora-Italic", size=7.2, leading=9.4)
y -= 2 * 100 + 6

y = block_header(y, "\u201cONE SOURCE, THREE BRANCHES\u201d  (Yi Yuan San Qi)", NAVY)
y -= 3
setfill(c, DARK)
y = draw_paragraph(c, ONE_SOURCE_THREE_BRANCHES, ML + 4, y, CW - 8, size=8, leading=10.6)
y -= 8

y = block_header(y, "THE DEFINING TRAIT", NAVY)
y -= 3
y = draw_paragraph(c, NO_ORGAN_NOTE, ML + 4, y, CW - 8, size=8, leading=10.6)
y -= 10

y = block_header(y, "\u201cSEA\u201d TITLES", GOLD_DARK)
y -= 3
sea_rows = [("Du Mai (GV)", "sea of the YANG meridians"),
            ("Ren Mai (CV)", "sea of the YIN meridians"),
            ("Chong Mai", "sea of 12 meridians \u00b7 blood \u00b7 zang-fu organs")]
for name, txt in sea_rows:
    setfill(c, DARK); c.setFont("Lora-Bold", 8)
    c.drawString(ML + 4, y, name + ":")
    setfill(c, GRAY); c.setFont("Lora-Italic", 8)
    c.drawString(ML + 100, y, txt)
    y -= 11.5

db.end_page()

# ============================================================
# PAGE 2: Per-vessel dense rows + flagged discrepancies + Quiz 5 review
# ============================================================
db.new_page()
y = H - 58
setfill(c, NAVY); c.setFont("Lora-Bold", 13.5)
c.drawString(ML, y, "All 8 Vessels at a Glance")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 14

for v in ALL_VESSELS:
    y = vessel_row(y, v)

y -= 6
box_lines_flag = [
    "Yang Qiao Mai: slide header says \u201c(12)\u201d coalescent points, only 10 named. FLAGGED.",
    "Yang Wei Mai: slide header says \u201c(15)\u201d coalescent points, only 14 named. FLAGGED.",
]
bh = len(box_lines_flag) * 11 + 12
box(c, ML, y, CW, bh, tint(RED, 0.85))
setfill(c, RED); c.setFont("Lora-Bold", 8); c.drawString(ML + 8, y - 11, "UNRESOLVED DISCREPANCIES (do not silently resolve):")
ty = y - 22
setfill(c, DARK); c.setFont("Lora", 7.6)
for ln in box_lines_flag:
    c.drawString(ML + 8, ty, ln)
    ty -= 11
y -= bh + 12

y = block_header(y, "QUIZ 5 MAINT REVIEW  (from Dr. Zhang's live review, per transcript)", GOLD_DARK)
y -= 3
setfill(c, DARK); c.setFont("Lora", 7.8)
for item in QUIZ5_REVIEW_TRANSCRIPT_ITEMS:
    lines = wrap_words("\u2022 " + item, "Lora", 7.8, CW - 8)
    for ln in lines:
        c.drawString(ML + 4, y, ln)
        y -= 10.2
    y -= 1
y -= 10

from wk7_content import HOMEWORK5_NOTE
y = block_header(y, "HOMEWORK 5  (new for this edition -- 2026 deck)", GOLD_DARK)
y -= 3
setfill(c, DARK); c.setFont("Lora", 7.8)
for ln in wrap_words(HOMEWORK5_NOTE, "Lora", 7.8, CW - 8):
    c.drawString(ML + 4, y, ln)
    y -= 10.2

db.end_page()
db.save()
