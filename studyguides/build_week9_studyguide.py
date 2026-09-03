#!/usr/bin/env python3
"""AC300 Week 9 Study Guide Classic -- Acupuncture Points: General Functions
& Categories (Five Shu Points, Eight Confluent Points, 15 Collaterals),
Middle-Circuit Collateral/Divergent/Sinew completion, 12 Cutaneous Regions,
and the Final Exam Master Review. Reference-only. Print + reMarkable."""
import sys
sys.path.insert(0, "/home/claude/ac300wk9")
from reportlab.pdfbase import pdfmetrics
from common_wk9 import (DocBuilder, studyguide_cover, setfill, setstroke, box, hairline,
                         draw_paragraph, wrap_words, section_label, draw_image_contain,
                         W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED, LBLUE, DARK,
                         GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM, EDLABEL)
from wk9_content import (
    CONFIRMATION_NOTE, READING_NOTE, HOMEWORK_QUIZ_NOTE, ACUPOINT_DEFINITION,
    ACUPOINT_NAME_CATEGORIES, ACUPOINT_PHYSIO_FUNCTION, ACUPOINT_PATHO_FUNCTION,
    ACUPOINT_APPLICATION_CATEGORIES, FIVE_SHU_DEFINITION, FIVE_SHU_ROWS, FIVE_SHU_CLASSIC,
    FIVE_SHU_MASTER, FIVE_SHU_YUAN_NOTE, CONFLUENT_DEFINITION, CONFLUENT_POINTS,
    CONFLUENT_PAIR_NOTE, LUO_DEFINITION, LUO_COURSE, LUO_MASTER, LUO_EXTRA,
    DIVERGENT_MIDDLE, SINEW_MIDDLE, SINEW_FUNCTIONS, SINEW_PATTERN_RULES,
    CUTANEOUS_DEFINITION, CUTANEOUS_SOURCE_QUOTE, CUTANEOUS_FUNCTIONS, CUTANEOUS_DIVISIONS,
    CUTANEOUS_EXCEPTION, CIRCULATION_RULES, QI_FLOW_DIRECTIONS, DISTRIBUTION_RULES,
    EXAM_MASTER_TABLE, EXAM_EXTRAORDINARY_NOTE, FINAL_EXAM_SUMMARY, EYE_RELATIONSHIP_TABLE,
    PCOS_INTRO, PCOS_PROTOCOL, PCOS_DISCLAIMER, INCONTINENCE_TYPES, INCONTINENCE_FIRSTLINE,
    INCONTINENCE_RED_FLAGS, INCONTINENCE_STUDY, EMMA_DATA,
    ACCENT_FIVESHU, ACCENT_CONFLUENT, ACCENT_LUO, ACCENT_EXAM, ACCENT_CLINICAL,
    ACCENT_MIDDLE, ACCENT_MIDDLE_WOOD,
)

OUT = f"/mnt/user-data/outputs/AC300_Week9_StudyGuide_Classic_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 9 Study Guide"
FOOTER = "AC300/AC375 | Week 9 Study Guide | Points, Final Review & Clinical Evidence | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def title_bar(title, accent, subtitle_right=None):
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, accent); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 13.2)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        title_w = pdfmetrics.stringWidth(title, "Lora-Bold", 13.2) + 14
        avail = CW - title_w - 20
        sub_size = 8.5
        while pdfmetrics.stringWidth(subtitle_right, "Lora-Italic", sub_size) > avail and sub_size > 6:
            sub_size -= 0.3
        c.setFont("Lora-Italic", sub_size)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot - 14


def _short(full):
    return full.split(" (")[0].strip()


def footnote(y, text):
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    for ln in wrap_words(text, "Lora-Italic", 7.2, CW):
        c.drawString(ML, y, ln); y -= 9
    return y


# ============================================================
# COVER
# ============================================================
studyguide_cover(
    db,
    title="Points & Final Exam Review",
    subtitle="Five Shu Points \u00b7 Confluent Points \u00b7 15 Collaterals \u00b7 12 Cutaneous Regions",
    points_line="Comprehensive Final Exam Master Review \u00b7 Clinical Evidence Appendix",
    covers_bullets=[
        "Acupoint categories: Five Shu (Transport) Points -- full 60-point master table across all 12 meridians",
        "Eight Confluent Points -- detailed cards, master-couple pairing, location + function",
        "15 Collaterals master table + the 3 extra (non-organ) collaterals",
        "Middle Circuit completion: PC/SJ/GB/LR Divergent Channels + Muscle Regions (confirms Week 8 self-study flags)",
        "12 Cutaneous Regions -- definition, functions, all 6 groups with lecture figures",
        "Final Exam Master Review -- circulation rules, qi-flow directions, and the full 12-meridian summary table",
        "Clinical Evidence appendix: PCOS/PMOS protocol, urinary incontinence electroacupuncture (JAMA), EMMA robotic massage pilot data",
    ],
    info_lines=[
        "NEXT WEEK: Comprehensive Final Exam (material from Weeks 1-9). No new quiz/homework this week -- see flag inside.",
        READING_NOTE,
    ],
    week_num="9",
)

# ============================================================
# PAGE: Confirmation note + Acupoint categories overview
# ============================================================
db.new_page()
y = title_bar("This Week's Framework: Acupuncture Points", NAVY, "General Functions & Categories")
y -= 4
setfill(c, DARK)
y = draw_paragraph(c, ACUPOINT_DEFINITION, ML, y, CW, size=9.1, leading=12.2)
y -= 8

setfill(c, NAVY); c.setFont("Lora-Bold", 9.4)
c.drawString(ML, y, "Classified by name, location, and meridian:")
c.setFont("Lora", 8.6)
setfill(c, DARK)
c.drawString(ML + 250, y, "  \u00b7  ".join(ACUPOINT_NAME_CATEGORIES))
y -= 16
setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.6); c.drawString(ML, y, "Physiology: ")
setfill(c, DARK); c.setFont("Lora", 8.6)
c.drawString(ML + 58, y, ACUPOINT_PHYSIO_FUNCTION); y -= 12
setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.6); c.drawString(ML, y, "Pathology: ")
setfill(c, DARK); c.setFont("Lora", 8.6)
c.drawString(ML + 58, y, ACUPOINT_PATHO_FUNCTION); y -= 18

setfill(c, NAVY); c.setFont("Lora-Bold", 9.4)
c.drawString(ML, y, "This Week's 3 Special-Point Categories:")
y -= 15
for name, desc, accent in ACUPOINT_APPLICATION_CATEGORIES:
    box_h = 27
    box(c, ML, y, CW, box_h, tint(accent, 0.9))
    setfill(c, accent); c.rect(ML, y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 9.2)
    c.drawString(ML + 12, y - 12, name)
    setfill(c, DARK); c.setFont("Lora", 7.8)
    c.drawString(ML + 12, y - 22, desc)
    y -= box_h + 5
y -= 6

flag_lines = wrap_words(CONFIRMATION_NOTE, "Lora-Italic", 7.6, CW - 18)
flag_h = len(flag_lines) * 10.1 + 15
box(c, ML, y, CW, flag_h, tint((0.16, 0.44, 0.46), 0.87))
setfill(c, (0.16, 0.44, 0.46)); c.setFont("Lora-Bold", 8); c.drawString(ML + 8, y - 11, "CONFIRMED THIS WEEK (resolves a Week 8 flag):")
ty = y - 22
setfill(c, DARK); c.setFont("Lora-Italic", 7.6)
for ln in flag_lines:
    c.drawString(ML + 8, ty, ln); ty -= 10.1
y -= flag_h + 8

box_lines_hw = wrap_words(HOMEWORK_QUIZ_NOTE, "Lora-Italic", 7.6, CW - 18)
hw_h = len(box_lines_hw) * 10.1 + 15
box(c, ML, y, CW, hw_h, tint(RED, 0.87))
setfill(c, RED); c.setFont("Lora-Bold", 8); c.drawString(ML + 8, y - 11, "NEXT WEEK: FINAL EXAM")
ty = y - 22
setfill(c, DARK); c.setFont("Lora-Italic", 7.6)
for ln in box_lines_hw:
    c.drawString(ML + 8, ty, ln); ty -= 10.1
y -= hw_h + 10

setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
y = draw_paragraph(c, READING_NOTE, ML, y, CW, font="Lora-Italic", size=7.6, leading=10, color=GRAY)
db.end_page()

# ============================================================
# PAGE: Five Shu Points -- definition, category table, classic quote,
# full master table (all 3 cycles), Yuan note. Consolidated to one page.
# ============================================================
db.new_page()
y = title_bar("The Five Shu (Transport) Points", ACCENT_FIVESHU, "60 points -- 5 per meridian x 12 meridians")
y -= 4
setfill(c, DARK)
y = draw_paragraph(c, FIVE_SHU_DEFINITION, ML, y, CW, size=8.4, leading=11.2)
y -= 6

hdr_h = 12
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.6)
c.drawString(ML + 5, y - hdr_h + 3.4, "CATEGORY")
c.drawString(ML + 82, y - hdr_h + 3.4, "MEANING")
c.drawString(ML + 225, y - hdr_h + 3.4, "LOCATION")
c.drawString(ML + 350, y - hdr_h + 3.4, "CLINICAL APPLICATION")
y -= hdr_h
for i, (name, meaning, loc, app) in enumerate(FIVE_SHU_ROWS):
    row_h = 15.5
    bg = tint(ACCENT_FIVESHU, 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, ACCENT_FIVESHU); c.setFont("Lora-Bold", 6.9)
    c.drawString(ML + 5, y - 10.5, name)
    setfill(c, DARK); c.setFont("Lora-Italic", 6.2)
    c.drawString(ML + 82, y - 10.5, meaning)
    c.setFont("Lora", 6.3)
    c.drawString(ML + 225, y - 10.5, loc)
    c.drawString(ML + 350, y - 10.5, app[:64] + ("..." if len(app) > 64 else ""))
    y -= row_h
y -= 4
y = draw_paragraph(c, FIVE_SHU_CLASSIC, ML, y, CW, font="Lora-Italic", size=7, leading=9.4, color=GRAY)
y -= 10

setfill(c, NAVY); c.setFont("Lora-Bold", 9.6)
c.drawString(ML, y, "Five Shu Master Table \u2014 All 12 Meridians")
y -= 14
mhdr_h = 12
setfill(c, NAVY); c.rect(ML, y - mhdr_h, CW, mhdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.6)
col_w = (CW - 128) / 5
c.drawString(ML + 4, y - mhdr_h + 3.4, "MERIDIAN")
labels = ["JING-WELL", "YING-SPRING", "SHU-STREAM", "JING-RIVER", "HE-SEA"]
for i, lab in enumerate(labels):
    c.drawString(ML + 128 + i * col_w, y - mhdr_h + 3.4, lab)
y -= mhdr_h
row_h = 15.6
cycle_labels = {"Anterior": "ANTERIOR (OUTER) CYCLE", "Posterior": "POSTERIOR (INNER) CYCLE", "Middle": "MIDDLE (LATERAL) CYCLE"}
last_cycle = None
for i, row in enumerate(FIVE_SHU_MASTER):
    if row["cycle"] != last_cycle:
        setfill(c, GRAY); c.setFont("Lora-Bold", 6.2)
        c.drawString(ML + 2, y - 8.5, cycle_labels[row["cycle"]])
        y -= 10.5
        last_cycle = row["cycle"]
    bg = tint(row["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, row["accent"]); c.setFont("Lora-Bold", 7)
    c.drawString(ML + 4, y - row_h + 5, row["meridian"])
    setfill(c, DARK); c.setFont("Lora", 6.3)
    for j, pt in enumerate(row["pts"]):
        c.drawString(ML + 128 + j * col_w, y - row_h + 5, pt)
    y -= row_h
y -= 6
y = draw_paragraph(c, FIVE_SHU_YUAN_NOTE, ML, y, CW, font="Lora-Italic", size=7.4, leading=9.8)
db.end_page()

# ============================================================
# PAGE: Eight Confluent Points
# ============================================================
db.new_page()
y = title_bar("The Eight Confluent Points", ACCENT_CONFLUENT, "Connect the 8 Extraordinary Vessels to the 12 Regular Meridians")
y -= 4
setfill(c, DARK)
y = draw_paragraph(c, CONFLUENT_DEFINITION, ML, y, CW, size=9, leading=12.2)
y -= 10
col_w = (CW - 14) / 2

card_hs = []
for cp in CONFLUENT_POINTS:
    loc_lines = wrap_words(cp["location"], "Lora", 7.2, col_w - 16)
    func_lines = wrap_words(cp["function"], "Lora-Italic", 7.2, col_w - 16)
    card_hs.append(44 + len(loc_lines) * 9.2 + len(func_lines) * 9.2)
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
    setfill(c, NAVY); c.setFont("Lora-Bold", 9.6)
    c.drawString(x0 + 12, y_top - 14, cp["point"])
    setfill(c, RED); c.setFont("Lora-Bold", 7.8)
    c.drawString(x0 + 12, y_top - 26, cp["vessel"] + "  \u00b7  pairs w/ " + cp["partner"])
    ty = y_top - 40
    setfill(c, DARK); c.setFont("Lora", 7.2)
    for ln in wrap_words(cp["location"], "Lora", 7.2, col_w - 16):
        c.drawString(x0 + 12, ty, ln); ty -= 9.2
    ty -= 3
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 7.2)
    for ln in wrap_words(cp["function"], "Lora-Italic", 7.2, col_w - 16):
        c.drawString(x0 + 12, ty, ln); ty -= 9.2
    if col == 1:
        yy = y_top - ch - 8
y = yy
y -= 4
y = draw_paragraph(c, CONFLUENT_PAIR_NOTE, ML, y, CW, font="Lora-Italic", size=7.8, leading=10.4)
db.end_page()

# ============================================================
# PAGE: 15 Collaterals master table
# ============================================================
db.new_page()
y = title_bar("The 15 Collaterals \u2014 Master Table", ACCENT_LUO, "Full detail + clinical indications: Week 8 Decoder")
y -= 4
setfill(c, DARK)
y = draw_paragraph(c, LUO_DEFINITION, ML, y, CW, size=8.6, leading=11.6)
y -= 4
y = draw_paragraph(c, LUO_COURSE, ML, y, CW, size=8.6, leading=11.6)
y -= 10

hdr_h = 14
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(ML + 6, y - hdr_h + 4, "MERIDIAN")
c.drawString(ML + 150, y - hdr_h + 4, "LUO POINT")
c.drawString(ML + 270, y - hdr_h + 4, "CONNECTS TO")
y -= hdr_h
row_h = 16.5
for i, luo in enumerate(LUO_MASTER):
    bg = tint(luo["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, DARK); c.setFont("Lora", 8)
    c.drawString(ML + 6, y - row_h + 5.5, f"{luo['meridian']} ({luo['abbr']})")
    setfill(c, luo["accent"]); c.setFont("Lora-Bold", 8.2)
    c.drawString(ML + 150, y - row_h + 5.5, luo["point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
    c.drawString(ML + 270, y - row_h + 5.5, luo["partner"])
    y -= row_h
y -= 4
for extra in LUO_EXTRA:
    row_h2 = 16.5
    box(c, ML, y, CW, row_h2, tint(GOLD, 0.88))
    setfill(c, DARK); c.setFont("Lora", 8)
    c.drawString(ML + 6, y - row_h2 + 5.5, extra["name"])
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.2)
    c.drawString(ML + 270, y - row_h2 + 5.5, extra["point"])
    y -= row_h2
y -= 10
setfill(c, DARK); c.setFont("Lora-Bold", 8.8)
c.drawString(ML, y, "The 3 Extra Collaterals \u2014 running course:")
y -= 14
for extra in LUO_EXTRA:
    lines = wrap_words(f"{extra['name']} ({extra['point']}): {extra['course']}", "Lora", 8, CW - 8)
    for ln in lines:
        c.setFont("Lora", 8); setfill(c, DARK)
        c.drawString(ML + 4, y, ln); y -= 10.6
    y -= 5
y -= 6
setfill(c, DARK); c.setFont("Lora-Bold", 8.8)
c.drawString(ML, y, "Middle Circuit Divergent Channels (PC \u00b7 SJ \u00b7 GB \u00b7 LR):")
y -= 13
setfill(c, DARK); c.setFont("Lora-Italic", 7.6)
y = draw_paragraph(c, "Each is described by Li (beginning) / He (organs involved) / Chu (exiting) / Ru "
                       "(merging to). Divergent Channels have NO acupoints of their own.",
                    ML, y, CW, font="Lora-Italic", size=7.6, leading=10.2)
y -= 8
hdr_h3 = 13
setfill(c, NAVY); c.rect(ML, y - hdr_h3, CW, hdr_h3, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.6)
c.drawString(ML + 5, y - hdr_h3 + 3.4, "MERIDIAN")
c.drawString(ML + 95, y - hdr_h3 + 3.4, "BEGINNING (LI)")
c.drawString(ML + 225, y - hdr_h3 + 3.4, "ORGANS/SYSTEMS (HE)")
c.drawString(ML + 350, y - hdr_h3 + 3.4, "EXITING (CHU) / MERGING (RU)")
y -= hdr_h3
for i, d in enumerate(DIVERGENT_MIDDLE):
    exit_merge = f"{d['exiting']}  ->  {d['merging']}"
    lines_organs = wrap_words(d["organs"], "Lora", 6.6, 118)
    lines_em = wrap_words(exit_merge, "Lora", 6.4, RX - ML - 350 - 4)
    row_h3 = max(18, 8.8 * max(len(lines_organs), len(lines_em)) + 7)
    bg = tint(d["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h3, bg)
    setfill(c, d["accent"]); c.setFont("Lora-Bold", 7.2)
    c.drawString(ML + 5, y - 10.5, d["meridian"])
    setfill(c, DARK); c.setFont("Lora", 6.6)
    for j, ln in enumerate(wrap_words(d["beginning"], "Lora", 6.6, 122)):
        c.drawString(ML + 95, y - 10.5 - j * 8.8, ln)
    for j, ln in enumerate(lines_organs):
        c.drawString(ML + 225, y - 10.5 - j * 8.8, ln)
    for j, ln in enumerate(lines_em):
        c.drawString(ML + 350, y - 10.5 - j * 8.8, ln)
    y -= row_h3
y -= 8
setfill(c, DARK); c.setFont("Lora-Italic", 7.6)
y = draw_paragraph(c, "PC + SJ divergent channels converge with each other; GB + LR divergent channels "
                       "converge with each other -- Divergent Channels always travel in Yin/Yang "
                       "paired-meridian sets before merging into the Yang meridian.",
                    ML, y, CW, font="Lora-Italic", size=7.6, leading=10)
db.end_page()

# ============================================================
# PAGE: Middle Circuit Muscle Region pathway text + structural rules
# ============================================================
db.new_page()
y = title_bar("Middle Circuit \u2014 Muscle (Sinew) Region Pathways", ACCENT_MIDDLE, "PC \u00b7 SJ \u00b7 GB \u00b7 LR")
y -= 6
setfill(c, NAVY); c.setFont("Lora-Bold", 9.2)
c.drawString(ML, y, "General Functions of the 12 Muscle Regions:")
y -= 13
for f in SINEW_FUNCTIONS:
    lines = wrap_words("\u2022 " + f, "Lora", 8, CW - 8)
    for ln in lines:
        c.setFont("Lora", 8); setfill(c, DARK)
        c.drawString(ML + 4, y, ln); y -= 10.4
    y -= 2
y -= 10

col_w3 = (CW - 14) / 2
card_hs3 = []
for s in SINEW_MIDDLE:
    path_lines = wrap_words(s["path"], "Lora", 7.4, col_w3 - 8)
    card_hs3.append(30 + len(path_lines) * 9.6)
row_max3 = [max(card_hs3[0], card_hs3[1]), max(card_hs3[2], card_hs3[3])]
yy = y
y_top3 = y
for i, s in enumerate(SINEW_MIDDLE):
    col, row = i % 2, i // 2
    x0 = ML + col * (col_w3 + 14)
    if col == 0:
        y_top3 = yy
    ch = row_max3[row]
    box(c, x0, y_top3, col_w3, ch, tint(s["accent"], 0.92))
    setfill(c, s["accent"]); c.rect(x0, y_top3 - ch, 3, ch, fill=1, stroke=0)
    setfill(c, s["accent"]); c.setFont("Lora-Bold", 8.6)
    c.drawString(x0 + 10, y_top3 - 12, s["meridian"])
    ty = y_top3 - 24
    setfill(c, DARK); c.setFont("Lora", 7.4)
    for ln in wrap_words(s["path"], "Lora", 7.4, col_w3 - 18):
        c.drawString(x0 + 10, ty, ln); ty -= 9.6
    if col == 1:
        yy = y_top3 - ch - 8
y = yy
y -= 4
# Binds line strip beneath the cards, compact
setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 7.4)
binds_line = "   |   ".join(f"{s['meridian'].split(' (')[0]}: {s['binds']}" for s in SINEW_MIDDLE)
for ln in wrap_words(binds_line, "Lora-Italic", 7.4, CW):
    c.drawString(ML, y, ln); y -= 9.8
y -= 12

setfill(c, DARK); c.setFont("Lora-Bold", 8.8)
c.drawString(ML, y, "The 4 Structural Pattern Rules (all 12 Muscle Regions):")
y -= 13
for r in SINEW_PATTERN_RULES:
    lines = wrap_words("\u2022 " + r, "Lora", 7.6, CW - 8)
    for ln in lines:
        c.setFont("Lora", 7.6); setfill(c, DARK)
        c.drawString(ML + 4, y, ln); y -= 9.8
db.end_page()

# ============================================================
# PAGE: Middle Circuit Muscle Regions -- lecture figures (2x2 grid)
# ============================================================
db.new_page()
y = title_bar("Middle Circuit \u2014 Muscle Regions, Lecture Figures", ACCENT_MIDDLE, "PC \u00b7 SJ \u00b7 GB \u00b7 LR")
y -= 6
col_w = (CW - 16) / 2
img_h = 210
for i, s in enumerate(SINEW_MIDDLE):
    col, row = i % 2, i // 2
    x0 = ML + col * (col_w + 16)
    y0 = y - row * (img_h + 34)
    setfill(c, s["accent"]); c.setFont("Lora-Bold", 9.6)
    c.drawString(x0, y0, s["meridian"])
    y0 -= 14
    dy = draw_image_contain(c, s["fig"], x0, y0, col_w, img_h, s["accent"])
    y0 = dy - 6
    setfill(c, DARK); c.setFont("Lora-Italic", 6.8)
    for ln in wrap_words("Binds: " + s["binds"], "Lora-Italic", 6.8, col_w)[:2]:
        c.drawString(x0, y0, ln); y0 -= 8.6
bottom_y = y - 2 * (img_h + 34) - 12
footnote(bottom_y, "Lecture Fig. \u2014 2026AC300Lecture_9Vivian.pdf, slides 20/21/28/29 (Dr. Zhang).")
db.end_page()

# ============================================================
# PAGE: 12 Cutaneous Regions -- definition, functions, exception
# ============================================================
db.new_page()
y = title_bar("The 12 Cutaneous Regions (Pi Bu)", (0.35, 0.35, 0.35), "Fully new content this week")
y -= 4
setfill(c, DARK)
y = draw_paragraph(c, CUTANEOUS_DEFINITION, ML, y, CW, size=9, leading=12.2)
y -= 8
y = draw_paragraph(c, CUTANEOUS_SOURCE_QUOTE, ML, y, CW, font="Lora-Italic", size=7.8, leading=10.6, color=GRAY)
y -= 10
setfill(c, NAVY); c.setFont("Lora-Bold", 9.2)
c.drawString(ML, y, "Functions:")
y -= 13
for f in CUTANEOUS_FUNCTIONS:
    lines = wrap_words("\u2022 " + f, "Lora", 8, CW - 8)
    for ln in lines:
        c.setFont("Lora", 8); setfill(c, DARK)
        c.drawString(ML + 4, y, ln); y -= 10.6
    y -= 2
y -= 6
y = draw_paragraph(c, CUTANEOUS_EXCEPTION, ML, y, CW, font="Lora-Italic", size=8, leading=10.8)
y -= 12
setfill(c, NAVY); c.setFont("Lora-Bold", 9.2)
c.drawString(ML, y, "The 6 Cutaneous Groups:")
y -= 14
for div in CUTANEOUS_DIVISIONS:
    box(c, ML, y, CW, 16, tint(div["accent"], 0.9))
    setfill(c, div["accent"]); c.setFont("Lora-Bold", 8)
    c.drawString(ML + 6, y - 11.5, div["group"])
    setfill(c, DARK); c.setFont("Lora", 7.8)
    c.drawString(ML + 130, y - 11.5, "  \u00b7  ".join(div["members"]))
    y -= 18
db.end_page()

# ============================================================
# PAGE: Cutaneous Region lecture figures -- Yang + Yin combined
# ============================================================
db.new_page()
y = title_bar("12 Cutaneous Regions \u2014 Lecture Figures", (0.35, 0.35, 0.35), "Yang groups (top) \u00b7 Yin groups (bottom)")
y -= 6
setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.6)
c.drawString(ML, y, "Yang Groups: Taiyang \u00b7 Shaoyang \u00b7 Yangming")
y -= 12
draw_image_contain(c, "CUTANEOUS_YANG", ML, y, CW, 300, (0.35, 0.35, 0.35))
y -= 314
setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.6)
c.drawString(ML, y, "Yin Groups: Taiyin \u00b7 Shaoyin \u00b7 Jueyin")
y -= 12
draw_image_contain(c, "CUTANEOUS_YIN", ML, y, CW, 300, (0.35, 0.35, 0.35))
y -= 314
footnote(y, "Lecture Fig. \u2014 2026AC300Lecture_9Vivian.pdf, slides 41-42 (Dr. Zhang).")
db.end_page()

# ============================================================
# PAGE: Final Exam Master Review -- circulation, qi flow, distribution,
# eye landmarks, extraordinary vessels -- consolidated
# ============================================================
db.new_page()
y = title_bar("Final Exam Master Review \u2014 Circulation & Structure", ACCENT_EXAM, "The single highest-yield page in this packet")
y -= 4
setfill(c, DARK)
y = draw_paragraph(c, FINAL_EXAM_SUMMARY, ML, y, CW, size=8, leading=10.8)
y -= 8
setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(ML, y, "The 12 Meridians Circulate in a Fixed Sequence:")
y -= 12
for i, rule in enumerate(CIRCULATION_RULES):
    lines = wrap_words(f"{i+1}. {rule}", "Lora", 7.6, CW - 8)
    for ln in lines:
        c.setFont("Lora", 7.6); setfill(c, DARK)
        c.drawString(ML + 4, y, ln); y -= 9.8
    y -= 2
y -= 6

col_w2 = (CW - 16) / 2
left_x, right_x = ML, ML + col_w2 + 16
setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(left_x, y, "Direction of Qi Flow:")
yl = y - 13
for label, dirn in QI_FLOW_DIRECTIONS:
    box(c, left_x, yl, col_w2, 14, tint(ACCENT_EXAM, 0.9))
    setfill(c, DARK); c.setFont("Lora", 6.9)
    c.drawString(left_x + 5, yl - 10, label)
    setfill(c, ACCENT_EXAM); c.setFont("Lora-Bold", 6.9)
    c.drawRightString(left_x + col_w2 - 5, yl - 10, dirn)
    yl -= 16

setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(right_x, y, "Distribution Rules:")
yr = y - 13
for area, rule in DISTRIBUTION_RULES:
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 6.9); c.drawString(right_x, yr, area + ":")
    yr -= 9.5
    setfill(c, DARK); c.setFont("Lora", 6.7)
    for ln in wrap_words(rule, "Lora", 6.7, col_w2 - 4):
        c.drawString(right_x + 4, yr, ln); yr -= 8.8
    yr -= 3
y = min(yl, yr) - 8

setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(ML, y, "Which Meridians Pass the Eye, and Where:")
y -= 12
for m, note in EYE_RELATIONSHIP_TABLE:
    lines = wrap_words(note, "Lora", 6.9, CW - 130)
    row_h = max(11, 8.6 * len(lines) + 2)
    box(c, ML, y, CW, row_h, tint(ACCENT_EXAM, 0.93))
    setfill(c, ACCENT_EXAM); c.setFont("Lora-Bold", 6.9)
    c.drawString(ML + 5, y - row_h + (row_h - 7) / 2 + 4, m)
    setfill(c, DARK); c.setFont("Lora", 6.7)
    ty = y - 8.5
    for ln in lines:
        c.drawString(ML + 130, ty, ln); ty -= 8.6
    y -= row_h + 2
y -= 8
setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(ML, y, "The 8 Extraordinary Vessels \u2014 Key Structural Differences:")
y -= 12
y = draw_paragraph(c, EXAM_EXTRAORDINARY_NOTE, ML, y, CW, size=7.6, leading=10.2)
db.end_page()

# ============================================================
# PAGE: Final Exam Master Table -- all 12 meridians
# ============================================================
db.new_page()
y = title_bar("Final Exam Master Table \u2014 All 12 Primary Meridians", ACCENT_EXAM, None)
y -= 4
for row in EXAM_MASTER_TABLE:
    special_lines = wrap_words(row["special"], "Lora-Italic", 7, CW - 16)
    card_h = 40 + len(special_lines) * 9
    box(c, ML, y, CW, card_h, CARD_BG)
    setfill(c, NAVY); c.rect(ML, y - card_h, 4, card_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 9.2)
    c.drawString(ML + 12, y - 12, row["m"])
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 7.4)
    c.drawRightString(RX - 8, y - 12, f"Total pts: {row['total']}  \u00b7  {row['dirn']}")
    setfill(c, DARK); c.setFont("Lora", 7.4)
    c.drawString(ML + 12, y - 23, f"Pertains: {row['pert']}   |   Connects: {row['conn']}")
    c.drawString(ML + 12, y - 33.5, f"First: {row['first']}   |   Last: {row['last']}")
    ty = y - 33.5 - 11
    setfill(c, GRAY); c.setFont("Lora-Italic", 7)
    for ln in special_lines:
        c.drawString(ML + 12, ty, ln); ty -= 9
    y -= card_h + 5
db.end_page()

# ============================================================
# PAGE: Clinical Evidence -- PCOS/PMOS + Urinary Incontinence + EMMA,
# two-column layout to fit on one page
# ============================================================
db.new_page()
y = title_bar("Clinical Evidence \u2014 PCOS/PMOS, Incontinence & EMMA", ACCENT_CLINICAL, "Appendix -- not exam material")
y -= 4
col_w4 = (CW - 18) / 2
left_x4, right_x4 = ML, ML + col_w4 + 18
y_top4 = y

# --- LEFT COLUMN: PCOS/PMOS ---
setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(left_x4, y, "PCOS/PMOS Acupuncture Protocol")
yl = y - 13
setfill(c, DARK)
yl = draw_paragraph(c, PCOS_INTRO, left_x4, yl, col_w4, size=7.3, leading=9.8)
yl -= 6
for label, key in [("Study Design", "design"), ("Dosing", "dosing"), ("Protocol 1", "points_1"),
                    ("Protocol 2 (alternated)", "points_2"), ("Outcomes", "outcomes"), ("Basic Reference Set", "basic_set")]:
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 7.6)
    c.drawString(left_x4, yl, label + ":")
    yl -= 9.6
    yl = draw_paragraph(c, PCOS_PROTOCOL[key], left_x4 + 4, yl, col_w4 - 4, size=6.9, leading=9.1)
    yl -= 4
yl -= 3
yl = draw_paragraph(c, PCOS_DISCLAIMER, left_x4, yl, col_w4, font="Lora-Italic", size=6.6, leading=8.8, color=GRAY)

# --- RIGHT COLUMN: Incontinence + EMMA ---
setfill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(right_x4, y, "Urinary Incontinence & EMMA Pilot Data")
yr = y - 13
for name, desc in INCONTINENCE_TYPES:
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 7.2); c.drawString(right_x4, yr, name + ": ")
    setfill(c, DARK); c.setFont("Lora", 7.2)
    lines = wrap_words(desc, "Lora", 7.2, col_w4 - 100)
    c.drawString(right_x4 + 100, yr, lines[0]); yr -= 9
    for ln in lines[1:]:
        c.drawString(right_x4 + 100, yr, ln); yr -= 9
yr -= 4
setfill(c, NAVY); c.setFont("Lora-Bold", 7.8)
yr = draw_paragraph(c, "JAMA 2017 Electroacupuncture RCT (" + INCONTINENCE_STUDY["citation"] + "):",
                     right_x4, yr, col_w4, font="Lora-Bold", size=7.8, leading=10, color=NAVY)
for key in ["design", "points", "technique", "course", "outcome", "caution"]:
    yr = draw_paragraph(c, INCONTINENCE_STUDY[key], right_x4, yr, col_w4, size=6.8, leading=9.1)
    yr -= 3
yr -= 2
yr = draw_paragraph(c, INCONTINENCE_RED_FLAGS, right_x4, yr, col_w4, font="Lora-Italic", size=6.6, leading=8.8, color=RED)
yr -= 6

setfill(c, NAVY); c.setFont("Lora-Bold", 7.8)
c.drawString(right_x4, yr, "EMMA Robotic Massage \u2014 Pelvic Pain Pilot Data:")
yr -= 10
for key in ["intro", "cohort", "results", "takeaway"]:
    yr = draw_paragraph(c, EMMA_DATA[key], right_x4, yr, col_w4, size=6.7, leading=9.0)
    yr -= 4

db.end_page()
db.save()
