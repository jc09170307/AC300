#!/usr/bin/env python3
"""AC300 Week 8 Cram Sheet -- dense, text/table-only night-before reference
for the 15 Collaterals, 12 Divergent Channels, 12 Muscle Regions, and 12
Cutaneous Regions. Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk8")
from reportlab.pdfbase import pdfmetrics
from common_wk8 import (DocBuilder, cramsheet_cover, setfill, setstroke, box, hairline,
                         draw_paragraph, wrap_words, section_label, W, H, ML, MR, RX, CW,
                         NAVY, GOLD, GOLD_DARK, RED, LBLUE, GRAYBLUE, DARK, GRAY, LGRAY,
                         WHITE, CARD_BG, tint, EDITION, IS_RM)
from wk8_content import (LUO_POINTS, LUO_EXTRA, DIVERGENT_CHANNELS, SINEW_REGIONS,
                          SINEW_PATTERN_RULES, CUTANEOUS_DIVISIONS, WEEK7_REVIEW_QA,
                          HOMEWORK_QUIZ_NOTE, ACCENT_LUO, ACCENT_DIVERGENT, ACCENT_SINEW)

OUT = f"/mnt/user-data/outputs/AC300_Week8_CramSheet_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 8 Cram Sheet"
FOOTER = "AC300/AC375 | Week 8 Cram Sheet | Collaterals, Divergent, Sinew & Cutaneous | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def block_header(y, title, color):
    setfill(c, color); c.rect(ML, y - 13, CW, 13, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML + 6, y - 10.3, title)
    return y - 17


def _short(full):
    return full.split(",")[0].replace(" Meridian", "").strip()


def _fit(text, font, size, maxw):
    if pdfmetrics.stringWidth(text, font, size) <= maxw:
        return text
    while text and pdfmetrics.stringWidth(text + "...", font, size) > maxw:
        text = text[:-1]
    return text + "..."


# ============================================================
# COVER
# ============================================================
cramsheet_cover(
    db,
    points_line="15 Luo pts  \u00b7  12 Divergent channels (no pts)  \u00b7  12 Muscle Regions  \u00b7  12 Cutaneous Regions",
    box_triplets=[
        ("15, Not 12", GOLD_DARK, ["12 paired + CV + GV", "+ SP Great Luo"]),
        ("No New Quiz", RED, ["per Dr. Zhang, verbally", "see flag on p.2"]),
        ("4 Layers", NAVY, ["Luo \u00b7 Divergent", "Sinew \u00b7 Cutaneous"]),
    ],
    extras_line="+ Master tables for all 4 systems \u00b7 Week 7 confluent-point Q&A \u00b7 flagged discrepancies",
)

# ============================================================
# PAGE 1: 15 Collaterals + Divergent Channels master tables
# ============================================================
db.new_page()
y = H - 58
setfill(c, ACCENT_LUO); c.setFont("Lora-Bold", 13.5)
c.drawString(ML, y, "The 15 Collaterals (Luo-Connecting Points)")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 14

hdr_h = 13
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7)
c.drawString(ML + 5, y - hdr_h + 3.5, "MERIDIAN")
c.drawString(ML + 125, y - hdr_h + 3.5, "LUO POINT")
c.drawString(ML + 230, y - hdr_h + 3.5, "CONNECTS TO")
y -= hdr_h
row_h = 13.4
for i, luo in enumerate(LUO_POINTS):
    bg = tint(luo["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, DARK); c.setFont("Lora", 7)
    c.drawString(ML + 5, y - row_h + 4, f"{_short(luo['meridian'])} ({luo['abbr']})")
    setfill(c, luo["accent"]); c.setFont("Lora-Bold", 7.2)
    c.drawString(ML + 125, y - row_h + 4, luo["point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 6.6)
    c.drawString(ML + 230, y - row_h + 4, _short(luo["partner"]) + (" *" if luo.get("self_study") else ""))
    y -= row_h
y -= 3
for extra in LUO_EXTRA:
    bg = tint(GOLD, 0.88)
    box(c, ML, y, CW, row_h, bg)
    setfill(c, DARK); c.setFont("Lora", 7)
    c.drawString(ML + 5, y - row_h + 4, extra["name"].replace("Collateral of the ", "").replace("Collateral of ", ""))
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 7.2)
    c.drawString(ML + 230, y - row_h + 4, extra["point"])
    y -= row_h
y -= 3
setfill(c, GRAY); c.setFont("Lora-Italic", 6.6)
c.drawString(ML, y - 8, "* GB/LR collaterals: self-study slide content, not reached live.")
y -= 20

y = block_header(y, "THE 12 DIVERGENT CHANNELS (Jing Bie) -- No Points, No Organ", ACCENT_DIVERGENT)
y -= 3
hdr_h2 = 13
setfill(c, NAVY); c.rect(ML, y - hdr_h2, CW, hdr_h2, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.8)
c.drawString(ML + 5, y - hdr_h2 + 3.5, "MERIDIAN")
c.drawString(ML + 100, y - hdr_h2 + 3.5, "BEGINNING")
c.drawString(ML + 230, y - hdr_h2 + 3.5, "EXITING")
c.drawString(ML + 330, y - hdr_h2 + 3.5, "MERGES INTO")
y -= hdr_h2
row_h2 = 13.2
for i, d in enumerate(DIVERGENT_CHANNELS):
    bg = tint(d["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h2, bg)
    setfill(c, d["accent"]); c.setFont("Lora-Bold", 6.6)
    c.drawString(ML + 5, y - row_h2 + 4, d["meridian"] + (" *" if d.get("self_study") else ""))
    setfill(c, DARK); c.setFont("Lora", 6.3)
    c.drawString(ML + 100, y - row_h2 + 4, _fit(d["beginning"].split(" (")[0], "Lora", 6.3, 125))
    c.drawString(ML + 230, y - row_h2 + 4, _fit(d["exiting"].split(" (")[0], "Lora", 6.3, 95))
    c.drawString(ML + 330, y - row_h2 + 4, _fit(d["merging"], "Lora", 6.3, RX - ML - 330 - 4))
    y -= row_h2
setfill(c, GRAY); c.setFont("Lora-Italic", 6.6)
c.drawString(ML, y - 8, "* GB/LR divergent channels: self-study slide content, not reached live.")

db.end_page()

# ============================================================
# PAGE 2: Muscle Regions compact + Cutaneous Regions + flags + Week 7 review
# ============================================================
db.new_page()
y = H - 58
setfill(c, ACCENT_SINEW); c.setFont("Lora-Bold", 13.5)
c.drawString(ML, y, "The 12 Muscle (Sinew) Regions -- Binding Points")
y -= 8
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 14

col_w = (CW - 12) / 2
for i, s in enumerate(SINEW_REGIONS):
    col = i % 2
    row = i // 2
    x0 = ML + col * (col_w + 12)
    yy = y - row * 42
    bh = 38
    box(c, x0, yy - bh, col_w, bh, tint(s["accent"], 0.9))
    setfill(c, s["accent"]); c.rect(x0, yy - bh, 3, bh, fill=1, stroke=0)
    setfill(c, DARK); c.setFont("Lora-Bold", 7.4)
    label = s["meridian"] + (" *" if s.get("self_study") else "")
    c.drawString(x0 + 8, yy - 11, label)
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 6.6)
    bl = wrap_words("Binds: " + s["binds"], "Lora-Italic", 6.6, col_w - 16)
    ty = yy - 21
    for ln in bl[:2]:
        c.drawString(x0 + 8, ty, ln); ty -= 8
y -= 6 * 42 + 8
setfill(c, GRAY); c.setFont("Lora-Italic", 6.8)
c.drawString(ML, y, "* GB/LR muscle regions: self-study slide content, not reached live.")
y -= 18

y = block_header(y, "THE 4 STRUCTURAL PATTERN RULES", ACCENT_SINEW)
y -= 3
setfill(c, DARK); c.setFont("Lora", 7.6)
for r in SINEW_PATTERN_RULES:
    lines = wrap_words("\u2022 " + r, "Lora", 7.6, CW - 8)
    for ln in lines:
        c.drawString(ML + 4, y, ln); y -= 10
y -= 6

y = block_header(y, "THE 12 CUTANEOUS REGIONS (Pi Bu) -- self-study, not reached live", (0.35, 0.35, 0.35))
y -= 3
setfill(c, DARK); c.setFont("Lora", 7.8)
for div in CUTANEOUS_DIVISIONS:
    c.setFont("Lora-Bold", 7.6)
    c.drawString(ML + 4, y, div["group"] + ":")
    c.setFont("Lora", 7.6)
    c.drawString(ML + 150, y, "  \u00b7  ".join(m.split(" (")[0] for m in div["members"]))
    y -= 10.5
y -= 8

box_lines_flag = [
    "HOMEWORK/QUIZ: " + HOMEWORK_QUIZ_NOTE,
]
total_lines = []
for ln in box_lines_flag:
    total_lines += wrap_words(ln, "Lora", 7.2, CW - 16)
bh2 = len(total_lines) * 9.4 + 12
box(c, ML, y, CW, bh2, tint(RED, 0.85))
setfill(c, RED); c.setFont("Lora-Bold", 7.6); c.drawString(ML + 8, y - 10, "FLAGGED (not silently resolved):")
ty = y - 20
setfill(c, DARK); c.setFont("Lora", 7.2)
for ln in total_lines:
    c.drawString(ML + 8, ty, ln)
    ty -= 9.4
y -= bh2 + 12

y = block_header(y, "WEEK 7 REVIEW -- LIVE Q&A DR. ZHANG RAN AT THE START OF LECTURE 8", GOLD_DARK)
y -= 3
setfill(c, DARK); c.setFont("Lora", 7.4)
for q, a in WEEK7_REVIEW_QA:
    q_lines = wrap_words("Q: " + q, "Lora-Bold", 7.4, CW - 8)
    for ln in q_lines:
        c.setFont("Lora-Bold", 7.4)
        c.drawString(ML + 4, y, ln); y -= 9.6
    a_lines = wrap_words("A: " + a, "Lora-Italic", 7.2, CW - 12)
    for ln in a_lines:
        c.setFont("Lora-Italic", 7.2)
        setfill(c, GOLD_DARK)
        c.drawString(ML + 10, y, ln); y -= 9.2
    setfill(c, DARK)
    y -= 2

db.end_page()
db.save()
