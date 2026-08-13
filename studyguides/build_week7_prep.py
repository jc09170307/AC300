#!/usr/bin/env python3
"""AC300 Week 7 Pre-Lecture Analysis Sheet -- Divergent Channels, Sinew
Channels & Cutaneous Regions. Built BEFORE this lecture happens, per the PLA
document type's purpose. Two modes: zhang-only, and zhang+flinner (which adds
a clearly-flagged supplementary lens using only already-verified Flinner
facts -- no fabricated Week 7 Flinner content, since no such transcript
exists). Print + reMarkable per mode = 4 PDFs total.
"""
import sys
sys.path.insert(0, "/home/claude/build")
from pla_common import *
from week7_content import (ACCENT_DIVERGENT, ACCENT_SINEW, ACCENT_CUTANEOUS, GRAY,
                            READING_ASSIGNMENT, CONFLUENCES, VOCAB, LEARNING_TARGETS,
                            CONNECT_BLANKS, ANTICIPATORY_DIVERGENT, ANTICIPATORY_SINEW,
                            ANTICIPATORY_CUTANEOUS, ANTICIPATORY_COMPARE, IQ_CHECKPOINTS,
                            IQ_ANSWERS, FLINNER_NOTE, FLINNER_CROSSFIRE)

MODE = sys.argv[1] if len(sys.argv) > 1 else "zhang"      # "zhang" | "combined"
EDITION = sys.argv[2] if len(sys.argv) > 2 else "print"   # "print" | "remarkable"
IS_COMBINED = MODE == "combined"
IS_RM = EDITION == "remarkable"
set_edition(IS_RM)
# from pla_common import * bound these at import time, before set_edition()
# mutated them -- re-sync the local names now that the edition is set.
import pla_common as _plc
CARD_BG = _plc.CARD_BG
PAGE_BG = _plc.PAGE_BG
MINT = _plc.MINT

if IS_COMBINED:
    OUT = f"/mnt/user-data/outputs/AC300_Week7_PrepGuide_ZhangFlinner_{'reMarkable' if EDITION=='remarkable' else 'Print'}.pdf"
    DOC_TITLE = "PRE-LECTURE ANALYSIS SHEET (Zhang + Flinner)"
else:
    OUT = f"/mnt/user-data/outputs/AC300_Week7_PrepGuide_Zhang_{'reMarkable' if EDITION=='remarkable' else 'Print'}.pdf"
    DOC_TITLE = "PRE-LECTURE ANALYSIS SHEET"

TOTAL_PAGES = 10 if IS_COMBINED else 9
c = new_canvas(OUT)
paint_page_bg(c)
FOOTER_LABEL = "AC300/AC375 | Week 7 | Divergent/Sinew/Cutaneous | VUIM Summer 2026"

# ============================================================= COVER
set_fill(c, GOLD)
c.rect(0, PAGE_H - 5, PAGE_W, 5, stroke=0, fill=1)

y = PAGE_H - 80
set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 12)
c.drawCentredString(PAGE_W / 2, y, "WEEK 7  \u00b7  PRE-LECTURE DRAFT")
y -= 46
set_fill(c, NAVY); c.setFont("Lora", 24)
c.drawCentredString(PAGE_W / 2, y, DOC_TITLE)
y -= 32
set_fill(c, NAVY); c.setFont("Lora-Italic", 14.5)
c.drawCentredString(PAGE_W / 2, y, "Divergent Channels, Sinew Channels & Cutaneous Regions")
y -= 26
set_fill(c, GOLD_DARK); c.setFont("Lora-Italic", 10.5)
c.drawCentredString(PAGE_W / 2, y, "Jing Bie  /  Jing Jin  /  Pi Bu")
y -= 22
set_fill(c, BLACK); c.setFont("Lora", 9.5)
c.drawCentredString(PAGE_W / 2, y, "Prof. (Dr.) Vivian Zhang, Ph.D." + ("  +  Dr. Justin Flinner (parallel section)" if IS_COMBINED else ""))
y -= 30

# Correction / scope banner
body_lines = wrap_text("Per Dr. Zhang's own Week 1 syllabus reading: Week 7 = Divergent Channels, Sinew Channels & "
                        "Cutaneous Regions. The Eight Extraordinary Vessels are Week 8.", "Lora", 8.4, CONTENT_W - 24)
reading_lines = wrap_text(f"Reading: {READING_ASSIGNMENT}", "Lora", 7.6, CONTENT_W - 24)
banner_h = 22 + len(body_lines) * 11 + len(reading_lines) * 10.5 + 8
box(c, MARGIN, y, CONTENT_W, banner_h, (0.976, 0.945, 0.906))
set_stroke(c, GOLD_DARK); c.setLineWidth(1.4)
c.rect(MARGIN, y - banner_h, CONTENT_W, banner_h, stroke=1, fill=0)
ty = y - 14
set_fill(c, (0.55, 0.28, 0.08)); c.setFont("Lora-Bold", 9)
c.drawString(MARGIN + 12, ty, "THIS WEEK IS NOT THE EXTRAORDINARY VESSELS.")
ty -= 13
set_fill(c, BLACK); c.setFont("Lora", 8.4)
for l in body_lines:
    c.drawString(MARGIN + 12, ty, l); ty -= 11
set_fill(c, (0.35, 0.35, 0.35)); c.setFont("Lora", 7.6)
for l in reading_lines:
    c.drawString(MARGIN + 12, ty, l); ty -= 10.5
y -= banner_h + 14

y = purpose_box(c, y, [
    "This lecture hasn't happened yet -- this is a PRE-LECTURE draft built from the syllabus + Week 1 preview material only.",
    "BEFORE lecture: Complete Sections A-D. Rate confidence honestly -- low pre-scores are expected for unlectured material.",
    "DURING lecture: Annotate directly on this sheet. Correct anything below that Dr. Zhang teaches differently.",
    "AFTER lecture: Complete Section F within 24 hours, then this sheet becomes your first real Week 7 reference.",
])
y -= 4

cards = [
    ("A", "Learning Targets \u2014 I Can Statements", "Pre/post confidence ratings 1-5 for 8 learning outcomes"),
    ("B", "Activate \u2014 Connect to What You Know", "Bridge from Week 1 preview + fill-in prompts"),
    ("C", "Vocabulary Pre-Load", "10 key terms: Pinyin, English, space for your definition"),
    ("D", "Anticipatory Questions", "11 questions across 4 groups; starred = high-challenge/high-yield"),
    ("IQ", "Inter-Quiz: Mid-Study Probe", "12 items, 3 checkpoints; mastery \u2265 10/12 x3"),
    ("E", "Clinical Case", "Pre-lecture reasoning + post-lecture protocol"),
    ("F", "After-Lecture Synthesis", "3-column synthesis + review notes"),
]
if IS_COMBINED:
    cards.insert(4, ("FL", "Flinner Lens (supplementary)", "Cross-references already-verified Flinner facts -- flagged, not new claims"))
col_w = (CONTENT_W - 14) / 2
row_h = 40
gap = 8
n_rows = (len(cards) + 1) // 2
positions = [(i % 2, i // 2) for i in range(len(cards))]
for (col, row), (letter, title, desc) in zip(positions, cards):
    x = MARGIN + col * (col_w + 14)
    ty = y - row * (row_h + gap)
    set_fill(c, GOLD)
    c.rect(x, ty - row_h, 26, row_h, stroke=0, fill=1)
    set_fill(c, WHITE); c.setFont("Lora-Bold", 10 if len(letter) < 3 else 8)
    c.drawCentredString(x + 13, ty - row_h / 2 - 3, letter)
    box(c, x + 26, ty, col_w - 26, row_h, CARD_BG)
    set_fill(c, NAVY); c.setFont("Lora", 10.5)
    c.drawString(x + 36, ty - 16, title)
    set_fill(c, GRAY); c.setFont("Lora-Italic", 7.4)
    c.drawString(x + 36, ty - 29, desc)
y -= n_rows * (row_h + gap) + 10

hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=GOLD, w=1.2)
y -= 18
set_fill(c, GRAY); c.setFont("Lora", 9)
c.drawCentredString(PAGE_W / 2, y, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")

footer(c, FOOTER_LABEL, 1, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION A
y = section_header(c, "A", "Learning Targets -- I Can Statements")
y = purpose_box(c, y, [
    "Purpose: These define what you should be able to DO after lecture, not just recognize.",
    "Pre-lecture note: it's normal for every Pre score to be low/1 here -- this material hasn't been taught yet.",
])
for t in LEARNING_TARGETS:
    y = confidence_row(c, y, t)

footer(c, FOOTER_LABEL, 2, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION B
y = section_header(c, "B", "Activate -- Connect to What You Know")
y = purpose_box(c, y, [
    "Purpose: Activating prior knowledge before new input improves encoding.",
    "B1: Write whatever Dr. Zhang previewed in Week 1 about these 3 systems. B2: fill in before lecture.",
])

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B1 . What Dr. Zhang Already Told You (Week 1 preview)")
y -= 16
y = draw_paragraph(c,
    "In Week 1 Dr. Zhang previewed these 3 systems briefly: divergent channels 'govern the inside of the body... "
    "branched out from the primary meridians and mainly distributed on the chest, abdomen, and head... enhancing "
    "the relationship' between paired organs. Sinew channels are 'distribution of the primary meridians into "
    "muscles, reflecting the functional relationship between channels and body movement.' Cutaneous regions are "
    "'parts of the 12 meridians reflected on the body surface skin, where the Qi and meridians distribute.'",
    MARGIN, y, CONTENT_W, size=9, leading=12.2)
y -= 6
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(MARGIN, y, "Write it in your own words -- what do you think each system DOES that primary channels alone don't?")
y -= 10
y = write_box(c, y, CONTENT_W, 70, gold_bar=True, fill=CARD_BG, n_lines=3)
y -= 18

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B2 . Connect the Dots -- complete before lecture")
y -= 20
for before, bw, after in CONNECT_BLANKS:
    y = fill_blank_line(c, before, bw, after, MARGIN, y, size=8.8)
    y -= 20

footer(c, FOOTER_LABEL, 3, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION C
y = section_header(c, "C", "Vocabulary Pre-Load -- Define Before Class")
y = purpose_box(c, y, [
    "Purpose: Pre-loading key terms primes semantic memory so lecture content attaches to existing scaffolding.",
])
y = vocab_table_header(c, y)
for py, en, accent in VOCAB:
    y = vocab_row(c, y, py, en, accent=accent)

y -= 8
set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "The 6 Confluences (Liu He) -- fill in as Dr. Zhang confirms in lecture")
y -= 16
row_h = 15.5
hdr_h = 14
set_fill(c, NAVY)
c.rect(MARGIN, y - hdr_h, CONTENT_W, hdr_h, stroke=0, fill=1)
set_fill(c, WHITE); c.setFont("Lora-Bold", 7.6)
c.drawString(MARGIN + 8, y - hdr_h + 4, "YIN/YANG STAGE PAIRING")
c.drawString(MARGIN + 280, y - hdr_h + 4, "YANG CH.")
c.drawString(MARGIN + 360, y - hdr_h + 4, "YIN CH.")
y -= hdr_h
for i, (stage, yang, yin) in enumerate(CONFLUENCES):
    bg = CARD_BG if i % 2 == 0 else PAGE_BG
    box(c, MARGIN, y, CONTENT_W, row_h, bg)
    set_fill(c, BLACK); c.setFont("Lora", 8.4)
    c.drawString(MARGIN + 8, y - row_h + 5, stage)
    c.drawString(MARGIN + 280, y - row_h + 5, yang)
    c.drawString(MARGIN + 360, y - row_h + 5, yin)
    y -= row_h

footer(c, FOOTER_LABEL, 4, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION D
y = section_header(c, "D", "Anticipatory Questions", subtitle="* = high-challenge / high-yield")
y = purpose_box(c, y, [
    "Purpose: Generating answers before instruction improves retention, even (especially) when you get it wrong.",
])

def draw_group(y, title, items, accent):
    set_fill(c, accent); c.setFont("Lora-Bold", 10.5)
    c.drawString(MARGIN, y, title)
    y -= 18
    for n, star, topic, q in items:
        y = anticipatory_q(c, y, n, star, topic, q, accent=accent)
    return y

y = draw_group(y, "Divergent Channels (Jing Bie)", ANTICIPATORY_DIVERGENT, ACCENT_DIVERGENT)
footer(c, FOOTER_LABEL, 5, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

y = section_header(c, "D", "Anticipatory Questions (continued)")
y = draw_group(y, "Sinew Channels (Jing Jin)", ANTICIPATORY_SINEW, ACCENT_SINEW)
y = draw_group(y, "Cutaneous Regions (Pi Bu)", ANTICIPATORY_CUTANEOUS, ACCENT_CUTANEOUS)
y = draw_group(y, "Systems Comparison", ANTICIPATORY_COMPARE, GOLD_DARK)

footer(c, FOOTER_LABEL, 6, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= FLINNER LENS (combined mode only)
if IS_COMBINED:
    y = section_header(c, "FL", "Flinner Lens -- Supplementary Cross-Reference")
    y = purpose_box(c, y, [FLINNER_NOTE])
    set_fill(c, NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(MARGIN, y, "Relevant already-verified Flinner corrections, applied to this week's material:")
    y -= 20
    for note in FLINNER_CROSSFIRE:
        box_h = 14 + len(wrap_text(note, "Lora", 8.6, CONTENT_W - 24)) * 11.5
        set_fill(c, (0.965, 0.955, 0.93))
        c.rect(MARGIN, y - box_h, CONTENT_W, box_h, stroke=0, fill=1)
        set_stroke(c, GOLD_DARK); c.setLineWidth(2)
        c.line(MARGIN, y - box_h, MARGIN, y)
        ty = y - 14
        set_fill(c, BLACK); c.setFont("Lora", 8.6)
        for l in wrap_text(note, "Lora", 8.6, CONTENT_W - 24):
            c.drawString(MARGIN + 12, ty, l); ty -= 11.5
        y -= box_h + 12
    footer(c, FOOTER_LABEL, 7, TOTAL_PAGES)
    c.showPage()
    paint_page_bg(c)

# ============================================================= IQ (Inter-Quiz)
page_offset = 1 if IS_COMBINED else 0
y = section_header(c, "IQ", "Inter-Quiz -- Mid-Study Probe", subtitle="(checkpoint format)")
y = purpose_box(c, y, [
    "Purpose: Spaced retrieval, checked every 4 items instead of at the end.",
    "Mastery: \u2265 10/12 across 3 separate sessions on different days.",
])
set_fill(c, GRAY); c.setFont("Lora", 8.5)
c.drawString(MARGIN, y, "Date: ______________   Start: ______   End: ______   Session score: ___/12")
y -= 20

for idx, (item_range, qs) in enumerate(IQ_CHECKPOINTS, 1):
    y = checkpoint_header(c, y, idx, item_range)
    for n, tag, t in qs:
        y = checkpoint_item(c, y, n, tag, t)
    y = selfcheck_line(c, y, 4)

footer(c, FOOTER_LABEL, 7 + page_offset, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= IQ Answer Key
y = section_header(c, "IQ", "Inter-Quiz Answer Key", subtitle="check each block right after attempting it")
set_fill(c, BLACK); c.setFont("Lora", 9.5)
for i, a in enumerate(IQ_ANSWERS, 1):
    set_fill(c, BLACK); c.setFont("Lora-Bold", 9.5)
    c.drawString(MARGIN, y, f"{i}.")
    c.setFont("Lora", 9.3)
    y = draw_paragraph(c, a, MARGIN + 22, y, CONTENT_W - 22, size=9.3, leading=12.6)
    y -= 4

y -= 8
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.5)
c.drawString(MARGIN, y, "Session 1: ___/12   Session 2: ___/12   Session 3: ___/12   Criterion met (\u226510/12 x3): [ ]")

footer(c, FOOTER_LABEL, 8 + page_offset, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION E + F
y = section_header(c, "E", "Clinical Case -- Apply It Before & After")
y = purpose_box(c, y, [
    "Purpose: Case reasoning bridges textbook concepts to clinical logic. Struggling before lecture is expected.",
])
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Case Vignette: Ms. Torres, 38 years old")
y -= 16
y = draw_paragraph(c,
    "Ms. Torres has chronic lateral hip and outer-thigh pain along the Gallbladder channel distribution that "
    "hasn't fully resolved with GB34 and local primary-channel points alone. There's a tight, ropy band palpable "
    "along the lateral thigh, worse with prolonged sitting, no clear organ-level GB symptoms (no bitter taste, "
    "no hypochondriac distention). Tongue and pulse unremarkable.",
    MARGIN, y, CONTENT_W, size=9.2, leading=12.4)
y -= 8
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.4)
c.drawString(MARGIN, y, "Pre-lecture: which supplementary system (not primary-channel points) might explain why local points alone aren't enough?")
y -= 10
y = write_box(c, y, CONTENT_W, 55, gold_bar=True, fill=CARD_BG, n_lines=2)
y -= 16
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.4)
c.drawString(MARGIN, y, "Post-lecture: revise your answer with what Dr. Zhang actually teaches about treating along a Sinew Channel.")
y -= 10
y = write_box(c, y, CONTENT_W, 55, gold_bar=True, fill=CARD_BG, n_lines=2)
y -= 24

hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=GOLD, w=1)
y -= 16
set_fill(c, NAVY); c.setFont("Lora-Bold", 11.5)
c.drawString(MARGIN, y, "F.  After-Lecture Synthesis")
y -= 20

col_w3 = CONTENT_W / 3 - 8
headers3 = ["Before I thought...", "Now I know...", "Still confused about..."]
hdr_h = 16
for i, h in enumerate(headers3):
    x = MARGIN + i * (col_w3 + 12)
    set_fill(c, NAVY); c.rect(x, y - hdr_h, col_w3, hdr_h, stroke=0, fill=1)
    set_fill(c, WHITE); c.setFont("Lora-Bold", 8.4)
    c.drawCentredString(x + col_w3 / 2, y - hdr_h + 4.5, h)
box_h = 130
for i in range(3):
    x = MARGIN + i * (col_w3 + 12)
    box(c, x, y - hdr_h, col_w3, box_h, CARD_BG)
y -= hdr_h + box_h + 14

set_fill(c, GRAY); c.setFont("Lora-Italic", 8.2)
c.drawString(MARGIN, y, "Update Section A confidence scores now, then file this sheet with your Week 7 Study Guide once built.")

footer(c, FOOTER_LABEL, TOTAL_PAGES, TOTAL_PAGES)
c.showPage()

c.save()
print(f"Saved {OUT}")
