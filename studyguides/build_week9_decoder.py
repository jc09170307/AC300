#!/usr/bin/env python3
"""AC300 Week 9 Special Points Decoder -- standalone. This week's star
categories are the Five Shu Points (full 60-point treatment) and the Eight
Confluent Points (detailed cards), plus the Meeting/Crossing Points
appendix table and a cumulative A/B/C tiered recap of every other special-
point category, per the Week 6 pilot rolled forward through Weeks 7-9.
Print + reMarkable."""
import sys
sys.path.insert(0, "/home/claude/ac300wk9")
from reportlab.pdfbase import pdfmetrics
from common_wk9 import (DocBuilder, setfill, setstroke, box, hairline, draw_paragraph,
                         wrap_words, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED,
                         LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM,
                         EDLABEL, draw_image_contain)
from wk9_content import (FIVE_SHU_DEFINITION, FIVE_SHU_ROWS, FIVE_SHU_CLASSIC, FIVE_SHU_MASTER,
                          FIVE_SHU_YUAN_NOTE, CONFLUENT_DEFINITION, CONFLUENT_POINTS,
                          CONFLUENT_PAIR_NOTE, LUO_MASTER, LUO_EXTRA, MEETING_POINTS_NOTE,
                          MEETING_POINTS_HIGHLIGHTS, ACCENT_FIVESHU, ACCENT_CONFLUENT,
                          ACCENT_LUO, ACCENT_MEETING)

OUT = f"/mnt/user-data/outputs/AC300_Week9_SpecialPointsDecoder_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 9 Special Points Decoder"
FOOTER = "AC300/AC375 | Week 9 Special Points Decoder | Five Shu, Confluent & Meeting Points | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def title_bar(title, accent, subtitle_right=None):
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, accent); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 14)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        title_w = pdfmetrics.stringWidth(title, "Lora-Bold", 14) + 14
        avail = CW - title_w - 20
        sub_size = 8.5
        while pdfmetrics.stringWidth(subtitle_right, "Lora-Italic", sub_size) > avail and sub_size > 6:
            sub_size -= 0.3
        if avail >= 40:
            c.setFont("Lora-Italic", sub_size)
            c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot - 12


def _short(full):
    return full.split(" (")[0].strip()


# ============================================================
# COVER
# ============================================================
db.new_page(bare=True)
y = H - 60
setfill(c, GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "WEEK 9")
c.setFont("Lora-Italic", 10)
c.drawRightString(RX, y, EDLABEL)
y -= 40
setfill(c, NAVY); c.setFont("Lora-Bold", 28)
c.drawString(ML, y, "Special Points Decoder")
y -= 28
setfill(c, ACCENT_FIVESHU); c.setFont("Lora-Bold", 16)
c.drawString(ML, y, "Five Shu Points \u2014 in Full \u2014 + Confluent & Meeting Points")
y -= 22
setfill(c, GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "Standalone reference \u2014 pairs with the Week 9 Study Guide")
y -= 18
hairline(c, ML, y, RX, rgb=GOLD, w=1.2)
y -= 28
setfill(c, ACCENT_FIVESHU); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Decoder Covers:")
y -= 20
setfill(c, DARK); c.setFont("Lora", 10.5)
bullets = [
    "All 60 Five Shu Points, in full \u2014 the star special-point category this week",
    "Eight Confluent Points \u2014 detailed cards, with master-couple pairing",
    "15 Collaterals master table \u2014 cumulative recap (full detail: Week 8 Decoder)",
    "Meeting (Crossing) Points \u2014 full appendix table (source images) + high-yield highlights",
    "A/B/C tiered cumulative recap of every other special-point category, rolled forward from Week 6",
]
for b in bullets:
    setfill(c, GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(c, DARK)
    lines = wrap_words(b, "Lora", 10.5, CW - 20)
    for i, l in enumerate(lines):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(lines)) + 4

y -= 8
box_h = 54
box(c, ML, y, CW, box_h, tint(ACCENT_FIVESHU, 0.88))
setfill(c, DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 16, y - 18, "Five Shu Points + Confluent Points ARE the special-point content for this week --")
c.drawString(ML + 16, y - 32, "the final consolidation before comprehensive review of all categories together.")
c.drawString(ML + 16, y - 46, "Next week: comprehensive Final Exam (material from Weeks 1-9).")
y -= box_h + 40
setfill(c, GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
db.end_page()

# ============================================================
# PAGE: Five Shu Points -- full drillable content, definition + table
# ============================================================
db.new_page()
y = title_bar("The Five Shu (Transport) Points", ACCENT_FIVESHU, "This week's star category")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c, FIVE_SHU_DEFINITION, ML, y, CW, size=9.1, leading=12.3)
y -= 8

hdr_h = 14
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(ML + 6, y - hdr_h + 4, "CATEGORY")
c.drawString(ML + 100, y - hdr_h + 4, "MEANING")
c.drawString(ML + 265, y - hdr_h + 4, "LOCATION")
c.drawString(ML + 400, y - hdr_h + 4, "CLINICAL APPLICATION")
y -= hdr_h
for i, (name, meaning, loc, app) in enumerate(FIVE_SHU_ROWS):
    app_lines = wrap_words(app, "Lora", 7, RX - (ML + 400) - 4)
    row_h = max(22, 9.4 * len(app_lines) + 8)
    bg = tint(ACCENT_FIVESHU, 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, ACCENT_FIVESHU); c.setFont("Lora-Bold", 8)
    c.drawString(ML + 6, y - 12, name)
    setfill(c, DARK); c.setFont("Lora-Italic", 7.2)
    for j, ln in enumerate(wrap_words(meaning, "Lora-Italic", 7.2, 158)):
        c.drawString(ML + 100, y - 12 - j * 9.4, ln)
    c.setFont("Lora", 7.2)
    for j, ln in enumerate(wrap_words(loc, "Lora", 7.2, 128)):
        c.drawString(ML + 265, y - 12 - j * 9.4, ln)
    for j, ln in enumerate(app_lines):
        c.drawString(ML + 400, y - 12 - j * 9.4, ln)
    y -= row_h
y -= 8
y = draw_paragraph(c, FIVE_SHU_CLASSIC, ML, y, CW, font="Lora-Italic", size=7.8, leading=10.4, color=GRAY)
y -= 10
y = draw_paragraph(c, FIVE_SHU_YUAN_NOTE, ML, y, CW, size=8.4, leading=11.4)
db.end_page()

# ============================================================
# PAGE(s): Five Shu master table -- full drillable, all 12 meridians
# ============================================================
def fiveshu_table_page(rows, title, subtitle):
    db.new_page()
    y = title_bar(title, ACCENT_FIVESHU, subtitle)
    y -= 6
    hdr_h = 15
    setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 7.6)
    col_w = (CW - 140) / 5
    c.drawString(ML + 5, y - hdr_h + 4.5, "MERIDIAN")
    labels = ["JING-WELL", "YING-SPRING", "SHU-STREAM", "JING-RIVER", "HE-SEA"]
    for i, lab in enumerate(labels):
        c.drawString(ML + 140 + i * col_w, y - hdr_h + 4.5, lab)
    y -= hdr_h
    row_h = 22
    for i, row in enumerate(rows):
        bg = tint(row["accent"], 0.9) if i % 2 == 0 else WHITE
        box(c, ML, y, CW, row_h, bg)
        setfill(c, row["accent"]); c.setFont("Lora-Bold", 9)
        c.drawString(ML + 5, y - row_h + 7.5, row["meridian"])
        setfill(c, DARK); c.setFont("Lora", 7.8)
        for j, pt in enumerate(row["pts"]):
            c.drawString(ML + 140 + j * col_w, y - row_h + 7.5, pt)
        y -= row_h
    return y


y = fiveshu_table_page([r for r in FIVE_SHU_MASTER if r["cycle"] == "Anterior"], "Five Shu Points \u2014 Anterior Cycle", "Lung \u00b7 Large Intestine \u00b7 Stomach \u00b7 Spleen")
y -= 12
setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
c.drawString(ML, y, "The Anterior Cycle runs Chest -> Hand -> Head -> Foot -> Chest along the anterior aspect of the body.")
db.end_page()

y = fiveshu_table_page([r for r in FIVE_SHU_MASTER if r["cycle"] == "Posterior"], "Five Shu Points \u2014 Posterior Cycle", "Heart \u00b7 Small Intestine \u00b7 Bladder \u00b7 Kidney")
y -= 12
setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
c.drawString(ML, y, "The Posterior Cycle runs the same 4-station course along the posterior aspect of the body.")
db.end_page()

y = fiveshu_table_page([r for r in FIVE_SHU_MASTER if r["cycle"] == "Middle"], "Five Shu Points \u2014 Middle Cycle", "Pericardium \u00b7 Sanjiao \u00b7 Gallbladder \u00b7 Liver")
y -= 12
setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
c.drawString(ML, y, "The Middle Cycle runs the lateral aspect of the body -- Jueyin/Shaoyang pairing.")
db.end_page()

# ============================================================
# PAGE: Eight Confluent Points -- full drillable content
# ============================================================
db.new_page()
y = title_bar("The Eight Confluent Points", ACCENT_CONFLUENT, "Full detail")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c, CONFLUENT_DEFINITION, ML, y, CW, size=9.1, leading=12.3)
y -= 10
col_w = (CW - 14) / 2
card_hs = []
for cp in CONFLUENT_POINTS:
    loc_lines = wrap_words(cp["location"], "Lora", 7.6, col_w - 16)
    func_lines = wrap_words(cp["function"], "Lora-Italic", 7.6, col_w - 16)
    card_hs.append(46 + len(loc_lines) * 9.8 + len(func_lines) * 9.8)
row_max = [max(card_hs[i], card_hs[i + 1]) for i in range(0, len(card_hs), 2)]
yy = y
y_top = y
for i, cp in enumerate(CONFLUENT_POINTS):
    col = i % 2
    row = i // 2
    x0 = ML + col * (col_w + 14)
    if col == 0:
        y_top = yy
    ch = row_max[row]
    box(c, x0, y_top, col_w, ch, tint(cp["accent"], 0.9))
    setfill(c, cp["accent"]); c.rect(x0, y_top - ch, 4, ch, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.2)
    c.drawString(x0 + 12, y_top - 15, cp["point"])
    setfill(c, RED); c.setFont("Lora-Bold", 8.2)
    c.drawString(x0 + 12, y_top - 28, cp["vessel"] + "  \u00b7  pairs w/ " + cp["partner"])
    ty = y_top - 43
    setfill(c, DARK); c.setFont("Lora", 7.6)
    for ln in wrap_words(cp["location"], "Lora", 7.6, col_w - 16):
        c.drawString(x0 + 12, ty, ln); ty -= 9.8
    ty -= 3
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 7.6)
    for ln in wrap_words(cp["function"], "Lora-Italic", 7.6, col_w - 16):
        c.drawString(x0 + 12, ty, ln); ty -= 9.8
    if col == 1:
        yy = y_top - ch - 8
y = yy
y -= 4
y = draw_paragraph(c, CONFLUENT_PAIR_NOTE, ML, y, CW, size=8.4, leading=11.4)
db.end_page()

# ============================================================
# PAGE: 15 Collaterals -- cumulative recap master table
# ============================================================
db.new_page()
y = title_bar("The 15 Collaterals \u2014 Cumulative Recap", ACCENT_LUO, "Full clinical detail: Week 8 Decoder")
y -= 6
hdr_h = 14
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(ML + 6, y - hdr_h + 4, "MERIDIAN")
c.drawString(ML + 150, y - hdr_h + 4, "LUO POINT")
c.drawString(ML + 270, y - hdr_h + 4, "CONNECTS TO")
y -= hdr_h
row_h = 17
for i, luo in enumerate(LUO_MASTER):
    bg = tint(luo["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, DARK); c.setFont("Lora", 8.2)
    c.drawString(ML + 6, y - row_h + 5.8, f"{luo['meridian']} ({luo['abbr']})")
    setfill(c, luo["accent"]); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML + 150, y - row_h + 5.8, luo["point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawString(ML + 270, y - row_h + 5.8, luo["partner"])
    y -= row_h
y -= 4
for extra in LUO_EXTRA:
    box(c, ML, y, CW, row_h, tint(GOLD, 0.88))
    setfill(c, DARK); c.setFont("Lora", 8.2)
    c.drawString(ML + 6, y - row_h + 5.8, extra["name"])
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML + 270, y - row_h + 5.8, extra["point"])
    y -= row_h
db.end_page()

# ============================================================
# PAGE: Meeting (Crossing) Points -- highlights + source table images
# ============================================================
db.new_page()
y = title_bar("Meeting (Crossing) Points", ACCENT_MEETING, "Where more than one channel's pathway crosses")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c, MEETING_POINTS_NOTE, ML, y, CW, size=8.6, leading=11.6)
y -= 10
setfill(c, NAVY); c.setFont("Lora-Bold", 9.4)
c.drawString(ML, y, "High-Yield Highlights:")
y -= 14
for pt, note in MEETING_POINTS_HIGHLIGHTS:
    lines = wrap_words(note, "Lora", 7.8, CW - 130)
    row_h = max(16, 10 * len(lines) + 6)
    box(c, ML, y, CW, row_h, tint(ACCENT_MEETING, 0.92))
    setfill(c, ACCENT_MEETING); c.setFont("Lora-Bold", 8)
    c.drawString(ML + 6, y - row_h + (row_h - 8) / 2 + 5, pt)
    setfill(c, DARK); c.setFont("Lora", 7.8)
    ty = y - 11
    for ln in lines:
        c.drawString(ML + 130, ty, ln); ty -= 10
    y -= row_h + 4
db.end_page()

for i in range(1, 5):
    db.new_page()
    y = title_bar(f"Meeting Points of the Channels \u2014 Source Table, p.{i} of 4", ACCENT_MEETING, None)
    y -= 8
    draw_image_contain(c, f"MEETING_PTS_{i}", ML, y, CW, 630, ACCENT_MEETING)
    y -= 644
    setfill(c, GRAY); c.setFont("Lora-Italic", 7)
    c.drawString(ML, y, "Source: Lecture_9Meeting_Points_List_.pdf, p." + str(51 + i) + " (MOA-style appendix table).")
    db.end_page()

# ============================================================
# PAGE: Cumulative recap of every other special-point category (A/B/C)
# ============================================================
db.new_page()
y = title_bar("Cumulative Recap \u2014 All Special-Point Categories", ACCENT_LUO, "Tiered A/B/C, per the Week 6 pilot")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c,
    "Five Shu Points and Confluent Points received full treatment above. The categories below stay "
    "exactly as covered previously -- listed here for final cumulative review, with the A/B/C "
    "exam-priority tiering piloted in the Week 6 Decoder and rolled forward every week since.",
    ML, y, CW, size=8.8, leading=12)
y -= 6
setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
y = draw_paragraph(c,
    "Tier key: A = high-yield, drill to automaticity. B = know the definition + 1 example cold. "
    "C = recognize the name and general function only.",
    ML, y, CW, font="Lora-Italic", size=7.6, leading=10)
y -= 12

RECAP = [
    ("A", "FIVE SHU POINTS", "Jing-Well/Ying-Spring/Shu-Stream/Jing-River/He-Sea; 60 points total.", "Full treatment: this week's Decoder"),
    ("A", "YUAN-SOURCE", "Where the Source (Yuan) Qi is accessed.", "Last new examples: Week 6 (PC7, SJ4, GB40, LR3)"),
    ("A", "LUO-CONNECTING", "Where a Luo-vessel branches to the paired channel.", "Full treatment: Week 8 Decoder"),
    ("A", "HE-SEA", "At elbow/knee; treats counterflow Qi and organ-level disorders.", "Last new examples: Week 6 (PC3, SJ10, GB34, LR8)"),
    ("A", "CONFLUENT (OPENING) POINTS", "Access point for each Extraordinary Vessel.", "Full treatment: this week's Decoder"),
    ("B", "XI-CLEFT", "Cleft point for acute conditions/pain.", "Last new examples: Week 6 (PC4, SJ7, GB36, LR6)"),
    ("B", "FRONT-MU", "Where a zang/fu organ's Qi gathers anteriorly.", "Last new examples: Week 6 (CV17, CV5, GB24, LR14)"),
    ("B", "BACK-SHU", "Bladder-channel transport points for each organ.", "Last new examples: Week 6 (BL14, BL22, BL19, BL18)"),
    ("B", "MEETING (CROSSING) POINTS", "A point crossed by more than one channel's pathway.", "Full table: this week's Decoder (resolves the GB20 discrepancy)"),
    ("C", "HUI-MEETING (INFLUENTIAL)", "8 points, meeting place for a tissue/substance category.", "Last new examples: Week 6 (GB34 = Sinews; LR13 = Zang)"),
    ("C", "LOWER HE-SEA", "Special He-Sea points for the 6 Fu organs, on the leg.", "Last new examples: Week 6 (SJ's is BL39, off-channel)"),
    ("C", "COALESCENT POINTS (JIAO HUI XUE)", "Meeting points between an Extraordinary Vessel and a primary meridian.", "Full treatment: Week 7 Decoder"),
]
tier_colors = {"A": RED, "B": GOLD_DARK, "C": GRAY}
for tier, cat, defn, last in RECAP:
    row_h = 15 + 10 + 10
    box(c, ML, y, CW, row_h, CARD_BG)
    setfill(c, tier_colors[tier]); c.rect(ML, y - row_h, 20, row_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 10)
    c.drawCentredString(ML + 10, y - row_h / 2 - 3.5, tier)
    setfill(c, NAVY); c.setFont("Lora-Bold", 8.2)
    c.drawString(ML + 28, y - 12, cat)
    setfill(c, DARK); c.setFont("Lora", 7.6)
    c.drawString(ML + 28, y - 23, defn)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    c.drawString(ML + 28, y - 33, last)
    y -= row_h + 4

db.end_page()
db.save()
