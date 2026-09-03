#!/usr/bin/env python3
"""AC300 Week 9 Cram Sheet -- dense, night-before reference for the Five Shu
Points, Eight Confluent Points, 15 Collaterals, and the Final Exam Master
Table. Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk9")
from reportlab.pdfbase import pdfmetrics
from common_wk9 import (DocBuilder, cramsheet_cover, setfill, setstroke, box, hairline,
                         draw_paragraph, wrap_words, section_label, W, H, ML, MR, RX, CW,
                         NAVY, GOLD, GOLD_DARK, RED, LBLUE, GRAYBLUE, DARK, GRAY, LGRAY,
                         WHITE, CARD_BG, tint, EDITION, IS_RM)
from wk9_content import (FIVE_SHU_MASTER, CONFLUENT_POINTS, LUO_MASTER, LUO_EXTRA,
                          EXAM_MASTER_TABLE, CIRCULATION_RULES, QI_FLOW_DIRECTIONS,
                          DISTRIBUTION_RULES, EYE_RELATIONSHIP_TABLE, HOMEWORK_QUIZ_NOTE,
                          CUTANEOUS_DIVISIONS, ACCENT_FIVESHU, ACCENT_CONFLUENT, ACCENT_LUO,
                          ACCENT_EXAM)

OUT = f"/mnt/user-data/outputs/AC300_Week9_CramSheet_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 9 Cram Sheet"
FOOTER = "AC300/AC375 | Week 9 Cram Sheet | Points, Final Exam Review | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def block_header(y, title, color):
    setfill(c, color); c.rect(ML, y - 13, CW, 13, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + 6, y - 10.3, title)
    return y - 17


def _short(full):
    return full.split(" (")[0].strip()


# ============================================================
# COVER
# ============================================================
cramsheet_cover(
    db,
    points_line="60 Five Shu pts \u00b7 8 Confluent pts \u00b7 15 Collaterals \u00b7 12-meridian Master Table",
    box_triplets=[
        ("Final Exam", RED, ["Next week -- Weeks", "1-9, 30 questions"]),
        ("3 Categories", ACCENT_FIVESHU, ["Five Shu \u00b7 Confluent", "\u00b7 Collaterals"]),
        ("12 Meridians", NAVY, ["Full master table", "on reverse"]),
    ],
    extras_line="+ Circulation & distribution rules \u00b7 eye landmarks \u00b7 cutaneous groups",
    subtitle="Points \u00b7 Final Exam Master Review",
    ready_line="Comprehensive Final Exam Next Week",
)

# ============================================================
# PAGE 1: Five Shu Master Table + Confluent Points quick table
# ============================================================
db.new_page()
y = H - 58
setfill(c, ACCENT_FIVESHU); c.setFont("Lora-Bold", 12.5)
c.drawString(ML, y, "Five Shu Points \u2014 All 12 Meridians (60 points)")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 12

hdr_h = 11
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.2)
col_w = (CW - 118) / 5
c.drawString(ML + 4, y - hdr_h + 3, "MERIDIAN")
for i, lab in enumerate(["JING-WELL", "YING-SPRING", "SHU-STREAM", "JING-RIVER", "HE-SEA"]):
    c.drawString(ML + 118 + i * col_w, y - hdr_h + 3, lab)
y -= hdr_h
row_h = 12.6
for i, row in enumerate(FIVE_SHU_MASTER):
    bg = tint(row["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, row["accent"]); c.setFont("Lora-Bold", 6.3)
    c.drawString(ML + 4, y - row_h + 3.6, row["abbr"])
    setfill(c, DARK); c.setFont("Lora", 5.9)
    for j, pt in enumerate(row["pts"]):
        c.drawString(ML + 118 + j * col_w, y - row_h + 3.6, pt)
    y -= row_h
y -= 12

y = block_header(y, "EIGHT CONFLUENT POINTS", ACCENT_CONFLUENT)
y -= 3
hdr_h2 = 11
setfill(c, NAVY); c.rect(ML, y - hdr_h2, CW, hdr_h2, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.4)
c.drawString(ML + 4, y - hdr_h2 + 3, "POINT")
c.drawString(ML + 120, y - hdr_h2 + 3, "VESSEL")
c.drawString(ML + 260, y - hdr_h2 + 3, "PAIRS WITH")
c.drawString(ML + 400, y - hdr_h2 + 3, "KEY FUNCTION")
y -= hdr_h2
row_h2 = 12.6
for i, cp in enumerate(CONFLUENT_POINTS):
    bg = tint(cp["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h2, bg)
    setfill(c, cp["accent"]); c.setFont("Lora-Bold", 6.4)
    c.drawString(ML + 4, y - row_h2 + 3.6, cp["point"])
    setfill(c, DARK); c.setFont("Lora", 6.1)
    c.drawString(ML + 120, y - row_h2 + 3.6, cp["vessel"])
    c.drawString(ML + 260, y - row_h2 + 3.6, cp["partner"])
    func_short = cp["function"].split(";")[0].split(".")[0].split(",")[0]
    avail_w = RX - (ML + 400) - 4
    if pdfmetrics.stringWidth(func_short, "Lora", 6.1) > avail_w:
        while pdfmetrics.stringWidth(func_short + "...", "Lora", 6.1) > avail_w and len(func_short) > 3:
            func_short = func_short[:-1]
        func_short += "..."
    c.drawString(ML + 400, y - row_h2 + 3.6, func_short)
    y -= row_h2
y -= 10

y = block_header(y, "THE 15 COLLATERALS", ACCENT_LUO)
y -= 3
col_wL = (CW - 12) / 2
row_hL = 12
for i, luo in enumerate(LUO_MASTER):
    col, row = i % 2, i // 2
    x0 = ML + col * (col_wL + 12)
    yy = y - row * row_hL
    box(c, x0, yy, col_wL, row_hL - 1.5, tint(luo["accent"], 0.9) if row % 2 == 0 else WHITE)
    setfill(c, DARK); c.setFont("Lora", 6.3)
    c.drawString(x0 + 3, yy - 8.5, f"{luo['abbr']}")
    setfill(c, luo["accent"]); c.setFont("Lora-Bold", 6.5)
    c.drawString(x0 + 30, yy - 8.5, luo["point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 5.8)
    c.drawString(x0 + 120, yy - 8.5, "-> " + _short(luo["partner"]))
y -= 6 * row_hL + 4
for extra in LUO_EXTRA:
    box(c, ML, y, CW, 12, tint(GOLD, 0.88))
    setfill(c, DARK); c.setFont("Lora", 6.3)
    c.drawString(ML + 3, y - 8.5, extra["name"])
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 6.5)
    c.drawString(ML + 260, y - 8.5, extra["point"])
    y -= 12
y -= 12

y = block_header(y, "THE 6 CUTANEOUS GROUPS", (0.35, 0.35, 0.35))
y -= 3
for div in CUTANEOUS_DIVISIONS:
    setfill(c, div["accent"]); c.setFont("Lora-Bold", 6.8)
    c.drawString(ML + 3, y, div["group"] + ":")
    setfill(c, DARK); c.setFont("Lora", 6.6)
    c.drawString(ML + 90, y, "  \u00b7  ".join(div["members"]))
    y -= 9.6
db.end_page()

# ============================================================
# PAGE 2: Final Exam Master Table + Circulation/Distribution/Eye rules
# ============================================================
db.new_page()
y = H - 58
setfill(c, ACCENT_EXAM); c.setFont("Lora-Bold", 12.5)
c.drawString(ML, y, "Final Exam Master Table \u2014 All 12 Meridians")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 12

hdr_h3 = 11
setfill(c, NAVY); c.rect(ML, y - hdr_h3, CW, hdr_h3, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.2)
c.drawString(ML + 4, y - hdr_h3 + 3, "MERIDIAN")
c.drawString(ML + 100, y - hdr_h3 + 3, "PERTAINS/CONNECTS")
c.drawString(ML + 260, y - hdr_h3 + 3, "FIRST -> LAST")
c.drawString(ML + 440, y - hdr_h3 + 3, "PTS")
c.drawString(ML + 470, y - hdr_h3 + 3, "DIRECTION")
y -= hdr_h3
row_h3 = 13.4
for i, row in enumerate(EXAM_MASTER_TABLE):
    bg = tint(ACCENT_EXAM, 0.92) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h3, bg)
    setfill(c, NAVY); c.setFont("Lora-Bold", 6.4)
    c.drawString(ML + 4, y - row_h3 + 4, row["m"])
    setfill(c, DARK); c.setFont("Lora", 5.9)
    c.drawString(ML + 100, y - row_h3 + 4, f"{row['pert']} / {row['conn']}"[:38])
    c.drawString(ML + 260, y - row_h3 + 4, f"{row['first'].split(' (')[0]} -> {row['last'].split(' (')[0]}"[:44])
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 6.1)
    c.drawString(ML + 440, y - row_h3 + 4, row["total"])
    c.drawString(ML + 470, y - row_h3 + 4, row["dirn"])
    y -= row_h3
y -= 12

col_w2 = (CW - 16) / 2
left_x, right_x = ML, ML + col_w2 + 16
y = block_header(y, "CIRCULATION & QI-FLOW RULES", ACCENT_EXAM)
y -= 3
for i, rule in enumerate(CIRCULATION_RULES):
    lines = wrap_words(f"{i+1}. {rule}", "Lora", 6.6, CW - 6)
    for ln in lines:
        c.setFont("Lora", 6.6); setfill(c, DARK)
        c.drawString(ML + 3, y, ln); y -= 8.4
y -= 4
for label, dirn in QI_FLOW_DIRECTIONS:
    box(c, ML, y, CW, 11.5, tint(ACCENT_EXAM, 0.9))
    setfill(c, DARK); c.setFont("Lora", 6.4)
    c.drawString(ML + 4, y - 8.3, label)
    setfill(c, ACCENT_EXAM); c.setFont("Lora-Bold", 6.4)
    c.drawRightString(RX - 4, y - 8.3, dirn)
    y -= 13
y -= 8

y_save = y
setfill(c, NAVY); c.setFont("Lora-Bold", 7.6)
c.drawString(left_x, y, "DISTRIBUTION RULES")
yl = y - 11
for area, rule in DISTRIBUTION_RULES:
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 6.2); c.drawString(left_x, yl, area + ":")
    yl -= 8.2
    setfill(c, DARK); c.setFont("Lora", 6.1)
    for ln in wrap_words(rule, "Lora", 6.1, col_w2 - 4):
        c.drawString(left_x + 4, yl, ln); yl -= 7.8
    yl -= 2

setfill(c, NAVY); c.setFont("Lora-Bold", 7.6)
c.drawString(right_x, y, "EYE LANDMARKS")
yr = y - 11
for m, note in EYE_RELATIONSHIP_TABLE:
    setfill(c, ACCENT_EXAM); c.setFont("Lora-Bold", 6.1); c.drawString(right_x, yr, m + ":")
    yr -= 7.8
    setfill(c, DARK); c.setFont("Lora", 5.9)
    for ln in wrap_words(note, "Lora", 5.9, col_w2 - 4):
        c.drawString(right_x + 4, yr, ln); yr -= 7.4
    yr -= 1.5
y = min(yl, yr) - 10

box_lines_flag = wrap_words(HOMEWORK_QUIZ_NOTE, "Lora", 6.6, CW - 16)
bh2 = len(box_lines_flag) * 8.6 + 12
box(c, ML, y, CW, bh2, tint(RED, 0.85))
setfill(c, RED); c.setFont("Lora-Bold", 7); c.drawString(ML + 8, y - 9, "NEXT WEEK: FINAL EXAM")
ty = y - 18
setfill(c, DARK); c.setFont("Lora", 6.6)
for ln in box_lines_flag:
    c.drawString(ML + 8, ty, ln)
    ty -= 8.6

db.end_page()
db.save()
