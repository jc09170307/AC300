#!/usr/bin/env python3
"""AC300 Week 8 Pre-Lecture Analysis Sheet -- 15 Collaterals, 12 Divergent
Channels, 12 Muscle Regions, 12 Cutaneous Regions. NOTE: this lecture has
already occurred (full transcript + slide deck available), so this sheet
is framed as a lecture-consolidation tool following the same Behavioral
Interteaching structure (Sections A-F + Inter-Quiz) Jon uses every week,
rather than a true pre-lecture draft. Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk8")
from common_wk8 import (DocBuilder, setfill, setstroke, box, hairline, draw_paragraph,
                         wrap_words, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED,
                         LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM,
                         EDLABEL)
from wk8_content import (VOCAB, LEARNING_TARGETS, ANTICIPATORY_QUESTIONS, IQ_CHECKPOINTS,
                          IQ_ANSWERS, CLINICAL_CASE, CLINICAL_CASE_PRE_Q, CLINICAL_CASE_POST_Q,
                          WEEK7_REVIEW_QA, HOMEWORK_QUIZ_NOTE, READING_NOTE, ACCENT_LUO,
                          ACCENT_DIVERGENT, ACCENT_SINEW)

OUT = f"/mnt/user-data/outputs/AC300_Week8_PrepGuide_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 8 Lecture Consolidation Sheet"
FOOTER = "AC300/AC375 | Week 8 | Collaterals, Divergent, Sinew & Cutaneous | VUIM Summer 2026"
MINT = (0.938, 0.960, 0.958)

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def page_title(title, accent=NAVY):
    y = H - 60
    setfill(c, accent); c.setFont("Lora-Bold", 15)
    c.drawString(ML, y, title)
    y -= 10
    hairline(c, ML, y, RX, rgb=GOLD, w=1)
    return y - 20


def section_header(letter, title, subtitle=None):
    y = H - 58
    setfill(c, GOLD); c.rect(ML, y - 24, 30, 24, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 12 if len(letter) < 3 else 9)
    c.drawCentredString(ML + 15, y - 16, letter)
    setfill(c, NAVY); c.setFont("Lora-Bold", 14.5)
    c.drawString(ML + 40, y - 16, title)
    if subtitle:
        setfill(c, GRAY); c.setFont("Lora-Italic", 9)
        c.drawString(ML + 40, y - 30, subtitle)
        y -= 10
    y -= 30
    hairline(c, ML, y, RX, rgb=GOLD, w=0.8)
    return y - 16


def purpose_box(y, lines):
    bh = 12 + len(lines) * 11.5
    box(c, ML, y, CW, bh, tint(GOLD, 0.9))
    setfill(c, GOLD_DARK); c.rect(ML, y - bh, 3, bh, fill=1, stroke=0)
    ty = y - 11
    setfill(c, DARK); c.setFont("Lora-Italic", 8.4)
    for ln in lines:
        wl = wrap_words(ln, "Lora-Italic", 8.4, CW - 20)
        for l2 in wl:
            c.drawString(ML + 10, ty, l2); ty -= 11
    return y - bh - 12


def confidence_row(y, text):
    lines = wrap_words(text, "Lora", 8.8, CW - 190)
    row_h = max(20, len(lines) * 11 + 6)
    box(c, ML, y, CW, row_h, CARD_BG)
    setfill(c, DARK); c.setFont("Lora", 8.8)
    ty = y - 12
    for ln in lines:
        c.drawString(ML + 8, ty, ln); ty -= 11
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
    c.drawString(RX - 175, y - row_h + 8, "Pre: 1 2 3 4 5   Post: 1 2 3 4 5")
    return y - row_h - 4


def checkpoint_header(y, idx, label):
    setfill(c, NAVY); c.rect(ML, y - 15, CW, 15, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + 8, y - 11, f"CHECKPOINT {idx}  --  {label}")
    return y - 19


def checkpoint_item(y, n, tag, text):
    tag_color = RED if tag == "ACQ" else GOLD_DARK
    lines = wrap_words(text, "Lora", 8.4, CW - 70)
    row_h = max(15, len(lines) * 10.6 + 4)
    setfill(c, DARK); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML + 4, y - 10, f"{n}.")
    setfill(c, tag_color); c.setFont("Lora-Bold", 6.8)
    c.drawString(ML + 16, y - 9, f"[{tag}]")
    setfill(c, DARK); c.setFont("Lora", 8.4)
    ty = y - 10
    for ln in lines:
        c.drawString(ML + 50, ty, ln); ty -= 10.6
    return y - row_h


def selfcheck_line(y, n):
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawString(ML, y, f"Self-check score this block: ___/{n}")
    return y - 16


def write_box(y, h, n_lines=2):
    box(c, ML, y, CW, h, CARD_BG)
    setstroke(c, GOLD); c.setLineWidth(0.6)
    step = h / (n_lines + 1)
    for i in range(1, n_lines + 1):
        c.line(ML + 8, y - step * i, RX - 8, y - step * i)
    return y - h


# ============================================================= COVER
db.new_page(bare=True)
setfill(c, GOLD); c.rect(0, H - 5, W, 5, fill=1, stroke=0)
y = H - 80
setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 12)
c.drawCentredString(W / 2, y, "WEEK 8  \u00b7  LECTURE CONSOLIDATION SHEET")
y -= 46
setfill(c, NAVY); c.setFont("Lora", 24)
c.drawCentredString(W / 2, y, "LECTURE CONSOLIDATION SHEET")
y -= 32
setfill(c, NAVY); c.setFont("Lora-Italic", 14.5)
c.drawCentredString(W / 2, y, "15 Collaterals \u00b7 12 Divergent Channels \u00b7 12 Muscle Regions \u00b7 12 Cutaneous Regions")
y -= 26
setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 10.5)
c.drawCentredString(W / 2, y, "Built from the completed Lecture 8 transcript + slide deck (not a pre-lecture draft)")
y -= 22
setfill(c, DARK); c.setFont("Lora", 9.5)
c.drawCentredString(W / 2, y, "Prof. (Dr.) Vivian Zhang, Ph.D.")
y -= 30

body_lines = wrap_words("This week's content is structural/conceptual (no new organ acupoints) -- "
                          "sections below follow the usual Interteaching format but are filled in from "
                          "the completed lecture rather than pre-lecture predictions.",
                          "Lora", 8.4, CW - 24)
reading_lines = wrap_words(f"{READING_NOTE}", "Lora", 7.6, CW - 24)
banner_h = 22 + len(body_lines) * 11 + len(reading_lines) * 10.5 + 8
box(c, ML, y, CW, banner_h, tint(GOLD, 0.92))
setstroke(c, GOLD_DARK); c.setLineWidth(1.4)
c.rect(ML, y - banner_h, CW, banner_h, stroke=1, fill=0)
ty = y - 14
setfill(c, (0.55, 0.28, 0.08)); c.setFont("Lora-Bold", 9)
c.drawString(ML + 12, ty, "SCOPE FOR THIS WEEK")
ty -= 13
setfill(c, DARK); c.setFont("Lora", 8.4)
for l in body_lines:
    c.drawString(ML + 12, ty, l); ty -= 11
setfill(c, (0.35, 0.35, 0.35)); c.setFont("Lora", 7.6)
for l in reading_lines:
    c.drawString(ML + 12, ty, l); ty -= 10.5
y -= banner_h + 14

cards = [
    ("A", "Learning Targets", "8 targets, pre/post confidence 1-5"),
    ("B", "Activate -- Week 7 Bridge", "Confluent-points Q&A recap"),
    ("C", "Vocabulary Pre-Load", "10 key terms"),
    ("D", "Anticipatory Questions", "10 questions, 3 groups, starred = high-yield"),
    ("IQ", "Inter-Quiz", "12 items, 3 checkpoints"),
    ("E", "Clinical Case", "Reasoning + protocol"),
    ("F", "After-Lecture Synthesis", "3-column synthesis"),
]
col_w = (CW - 14) / 2
row_h = 38
gap = 8
n_rows = (len(cards) + 1) // 2
for i, (letter, title, desc) in enumerate(cards):
    col, row = i % 2, i // 2
    x = ML + col * (col_w + 14)
    ty = y - row * (row_h + gap)
    setfill(c, GOLD); c.rect(x, ty - row_h, 26, row_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 10 if len(letter) < 3 else 8)
    c.drawCentredString(x + 13, ty - row_h / 2 - 3, letter)
    box(c, x + 26, ty, col_w - 26, row_h, CARD_BG)
    setfill(c, NAVY); c.setFont("Lora", 10)
    c.drawString(x + 36, ty - 15, title)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    c.drawString(x + 36, ty - 28, desc)
y -= n_rows * (row_h + gap) + 10

hairline(c, ML, y, RX, rgb=GOLD, w=1.2)
y -= 18
setfill(c, GRAY); c.setFont("Lora", 9)
c.drawCentredString(W / 2, y, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
db.end_page()

# ============================================================= SECTION A
y = section_header("A", "Learning Targets")
y = purpose_box(y, [
    "Purpose: these define what you should be able to DO after review, not just recognize.",
    "Since the lecture already happened, rate your Pre score honestly based on where you were BEFORE building these materials.",
])
for t in LEARNING_TARGETS:
    y = confidence_row(y, t)
db.end_page()

# ============================================================= SECTION B
y = section_header("B", "Activate -- Connect to Week 7")
y = purpose_box(y, [
    "Purpose: Dr. Zhang opened Lecture 8 with a live Q&A review of the 8 Extraordinary Vessels' "
    "confluent points before introducing new content. Test yourself on the same Q&A she used.",
])
for q, a in WEEK7_REVIEW_QA:
    q_lines = wrap_words("Q: " + q, "Lora-Bold", 9, CW - 8)
    for ln in q_lines:
        setfill(c, DARK); c.setFont("Lora-Bold", 9)
        c.drawString(ML + 4, y, ln); y -= 12
    y -= 2
    y = write_box(y, 16, n_lines=1)
    y -= 6
db.end_page()

# ============================================================= SECTION C
y = section_header("C", "Vocabulary Pre-Load")
y = purpose_box(y, [
    "Purpose: load the Chinese/English terms this week's four systems are named with, before drilling content.",
])
hdr_h = 16
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 8)
c.drawString(ML + 6, y - hdr_h + 5, "PINYIN")
c.drawString(ML + 130, y - hdr_h + 5, "ENGLISH")
c.drawString(ML + 300, y - hdr_h + 5, "NOTE")
y -= hdr_h
row_h = 20
for i, (pin, eng, note) in enumerate(VOCAB):
    bg = CARD_BG if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, NAVY); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + 6, y - row_h + 6, pin)
    setfill(c, DARK); c.setFont("Lora", 8.4)
    c.drawString(ML + 130, y - row_h + 6, eng)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawString(ML + 300, y - row_h + 6, note)
    y -= row_h
db.end_page()

# ============================================================= SECTION D
y = section_header("D", "Anticipatory Questions", subtitle="* = starred, high-yield")
y = purpose_box(y, [
    "Purpose: these probe the reasoning behind this week's structure, not just recall.",
])
group_order = ["Structural", "Clinical", "Comparison"]
for group in group_order:
    items = [q for q in ANTICIPATORY_QUESTIONS if q[0] == group]
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y, group.upper())
    y -= 14
    for _, starred, text in items:
        star = "* " if starred else ""
        lines = wrap_words(star + text, "Lora", 8.8, CW - 8)
        for ln in lines:
            setfill(c, RED if starred else DARK); c.setFont("Lora", 8.8)
            c.drawString(ML + 4, y, ln); y -= 11
        y -= 5
    y -= 6
db.end_page()

# ============================================================= IQ
y = section_header("IQ", "Inter-Quiz -- Mid-Study Probe", subtitle="checkpoint format")
y = purpose_box(y, [
    "Purpose: spaced retrieval, checked every 4 items instead of at the end.",
    "Mastery: >= 10/12 across 3 separate sessions on different days.",
])
setfill(c, GRAY); c.setFont("Lora", 8.5)
c.drawString(ML, y, "Date: ______________   Start: ______   End: ______   Session score: ___/12")
y -= 20
for idx, (item_range, qs) in enumerate(IQ_CHECKPOINTS, 1):
    y = checkpoint_header(y, idx, item_range)
    for n, tag, t in qs:
        y = checkpoint_item(y, n, tag, t)
    y -= 4
    y = selfcheck_line(y, 4)
db.end_page()

# ============================================================= IQ Answer Key
y = section_header("IQ", "Inter-Quiz Answer Key", subtitle="check right after attempting each block")
setfill(c, DARK); c.setFont("Lora", 9.3)
for i, a in enumerate(IQ_ANSWERS, 1):
    setfill(c, DARK); c.setFont("Lora-Bold", 9.3)
    c.drawString(ML, y, f"{i}.")
    c.setFont("Lora", 9.1)
    y = draw_paragraph(c, a, ML + 20, y, CW - 20, size=9.1, leading=12.2)
    y -= 3
y -= 8
setfill(c, GRAY); c.setFont("Lora-Italic", 8.5)
c.drawString(ML, y, "Session 1: ___/12   Session 2: ___/12   Session 3: ___/12   Criterion met (>=10/12 x3): [ ]")
db.end_page()

# ============================================================= SECTION E + F
y = section_header("E", "Clinical Case -- Apply It")
y = purpose_box(y, ["Purpose: bridges structural theory to clinical reasoning."])
setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Case Vignette: Ms. Alvarez, 38 years old")
y -= 16
y = draw_paragraph(c, CLINICAL_CASE, ML, y, CW, size=9.1, leading=12.3)
y -= 8
setfill(c, GRAY); c.setFont("Lora-Italic", 8.4)
y = draw_paragraph(c, CLINICAL_CASE_PRE_Q, ML, y, CW, font="Lora-Italic", size=8.4, leading=11)
y -= 8
y = write_box(y, 55, n_lines=2)
y -= 16
setfill(c, GRAY); c.setFont("Lora-Italic", 8.4)
y = draw_paragraph(c, CLINICAL_CASE_POST_Q, ML, y, CW, font="Lora-Italic", size=8.4, leading=11)
y -= 8
y = write_box(y, 55, n_lines=2)
y -= 24

hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 16
setfill(c, NAVY); c.setFont("Lora-Bold", 11.5)
c.drawString(ML, y, "F.  After-Lecture Synthesis")
y -= 20
col_w3 = CW / 3 - 8
headers3 = ["Before I thought...", "Now I know...", "Still confused about..."]
hdr_h = 16
for i, h in enumerate(headers3):
    x = ML + i * (col_w3 + 12)
    setfill(c, NAVY); c.rect(x, y - hdr_h, col_w3, hdr_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 8.4)
    c.drawCentredString(x + col_w3 / 2, y - hdr_h + 4.5, h)
box_h3 = 110
for i in range(3):
    x = ML + i * (col_w3 + 12)
    box(c, x, y - hdr_h, col_w3, box_h3, CARD_BG)
y -= hdr_h + box_h3 + 14
setfill(c, GRAY); c.setFont("Lora-Italic", 8.2)
c.drawString(ML, y, "Update Section A confidence scores now, then file this sheet with your Week 8 Study Guide.")
db.end_page()

db.save()
