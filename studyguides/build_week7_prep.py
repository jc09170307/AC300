#!/usr/bin/env python3
"""AC300 Week 7 Pre-Lecture Analysis Sheet -- The Eight Extraordinary Vessels
(Qi Jing Ba Mai). Built BEFORE this lecture happens, per the PLA document
type's purpose. Follows the Week 3 v2 PLA design standard: centered cover,
gold-tab section headers, Sections A-F + Inter-Quiz, confidence ratings,
connect-the-dots fill-ins, vocab table, starred anticipatory questions,
checkpoint Inter-Quiz + answer key, clinical case, 3-column synthesis.
"""
import sys
sys.path.insert(0, "/home/claude/build")
from pla_common import *
from week7_content import (ACCENT_GV, ACCENT_CV, ACCENT_CHONG, ACCENT_DAI, ACCENT_QIAO,
                            ACCENT_WEI, GRAY, READING_ASSIGNMENT, CONFLUENT_PAIRS, VOCAB,
                            LEARNING_TARGETS, CONNECT_BLANKS, ANTICIPATORY_SEA_VESSELS,
                            ANTICIPATORY_CHONG_DAI, ANTICIPATORY_QIAO_WEI,
                            ANTICIPATORY_COMPARE, IQ_CHECKPOINTS, IQ_ANSWERS)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"   # "print" | "remarkable"
IS_RM = EDITION == "remarkable"
set_edition(IS_RM)
import pla_common as _plc
CARD_BG = _plc.CARD_BG
PAGE_BG = _plc.PAGE_BG
MINT = _plc.MINT

OUT = f"/mnt/user-data/outputs/AC300_Week7_PrepGuide_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_TITLE = "PRE-LECTURE ANALYSIS SHEET"

TOTAL_PAGES = 10
c = new_canvas(OUT)
paint_page_bg(c)
FOOTER_LABEL = "AC300/AC375 | Week 7 | Eight Extraordinary Vessels | VUIM Summer 2026"

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
c.drawCentredString(PAGE_W / 2, y, "The Eight Extraordinary Vessels")
y -= 26
set_fill(c, GOLD_DARK); c.setFont("Lora-Italic", 10.5)
c.drawCentredString(PAGE_W / 2, y, "Qi Jing Ba Mai  \u2014  GV \u00b7 CV \u00b7 Chong \u00b7 Dai \u00b7 Yang/Yin Qiao \u00b7 Yang/Yin Wei")
y -= 22
set_fill(c, BLACK); c.setFont("Lora", 9.5)
c.drawCentredString(PAGE_W / 2, y, "Prof. (Dr.) Vivian Zhang, Ph.D.")
y -= 30

# Scope / source banner
body_lines = wrap_text("Per the written syllabus (Week 7, CLO 2,4): Eight Extraordinary Meridians. Quiz 5 "
                        "and Homework 5 cover material from Weeks 6-7.", "Lora", 8.4, CONTENT_W - 24)
reading_lines = wrap_text(f"Reading: {READING_ASSIGNMENT}", "Lora", 7.6, CONTENT_W - 24)
banner_h = 22 + len(body_lines) * 11 + len(reading_lines) * 10.5 + 8
box(c, MARGIN, y, CONTENT_W, banner_h, (0.976, 0.945, 0.906))
set_stroke(c, GOLD_DARK); c.setLineWidth(1.4)
c.rect(MARGIN, y - banner_h, CONTENT_W, banner_h, stroke=1, fill=0)
ty = y - 14
set_fill(c, (0.55, 0.28, 0.08)); c.setFont("Lora-Bold", 9)
c.drawString(MARGIN + 12, ty, "SCOPE FOR THIS WEEK")
ty -= 13
set_fill(c, BLACK); c.setFont("Lora", 8.4)
for l in body_lines:
    c.drawString(MARGIN + 12, ty, l); ty -= 11
set_fill(c, (0.35, 0.35, 0.35)); c.setFont("Lora", 7.6)
for l in reading_lines:
    c.drawString(MARGIN + 12, ty, l); ty -= 10.5
y -= banner_h + 14

y = purpose_box(c, y, [
    "This lecture hasn't happened yet -- this is a PRE-LECTURE draft built from the Week 7 lecture deck + syllabus.",
    "BEFORE lecture: Complete Sections A-D. Rate confidence honestly -- low pre-scores are expected for unlectured material.",
    "DURING lecture: Annotate directly on this sheet. Correct anything below that Dr. Zhang teaches differently.",
    "AFTER lecture: Complete Section F within 24 hours, then this sheet becomes your first real Week 7 reference.",
])
y -= 4

cards = [
    ("A", "Learning Targets \u2014 I Can Statements", "Pre/post confidence ratings 1-5 for 8 learning outcomes"),
    ("B", "Activate \u2014 Connect to What You Know", "Bridge from Wk1-6 review + fill-in prompts"),
    ("C", "Vocabulary Pre-Load", "10 key terms: Pinyin, English, space for your definition"),
    ("D", "Anticipatory Questions", "12 questions across 4 groups; starred = high-challenge/high-yield"),
    ("IQ", "Inter-Quiz: Mid-Study Probe", "12 items, 3 checkpoints; mastery \u2265 10/12 x3"),
    ("E", "Clinical Case", "Pre-lecture reasoning + post-lecture protocol"),
    ("F", "After-Lecture Synthesis", "3-column synthesis + review notes"),
]
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

y -= 6
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Quick Reference -- All 8 Vessels at a Glance")
y -= 16
ref_rows = [
    ("GV (Du Mai)", "Posterior midline", "Sea of yang meridians", "28 pts", "SI 3 Houxi"),
    ("CV (Ren Mai)", "Anterior midline", "Sea of yin meridians", "24 pts", "LU 7 Lieque"),
    ("Chong Mai", "Parallels Kidney mer.", "Sea of 12 mer. / blood", "shares pts", "SP 4 Gongsun"),
    ("Dai Mai", "Around the waist", "Controls/binds all mer.", "shares pts", "GB 41 Zulinqi"),
    ("Yang Qiao", "Lateral heel -> GB20", "Balances limb mvmt/wake", "shares pts", "BL 62 Shenmai"),
    ("Yin Qiao", "Medial heel -> BL1", "Balances limb mvmt/sleep", "shares pts", "KI 6 Zhaohai"),
    ("Yang Wei", "Heel -> GV15/16", "Links all yang, exterior", "shares pts", "SJ 5 Waiguan"),
    ("Yin Wei", "Leg -> CV22/23", "Links all yin, interior", "shares pts", "PC 6 Neiguan"),
]
hdr_h = 14
set_fill(c, NAVY); c.rect(MARGIN, y - hdr_h, CONTENT_W, hdr_h, stroke=0, fill=1)
set_fill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(MARGIN + 6, y - hdr_h + 4, "VESSEL")
c.drawString(MARGIN + 108, y - hdr_h + 4, "COURSE (BRIEF)")
c.drawString(MARGIN + 258, y - hdr_h + 4, "PRIMARY FUNCTION")
c.drawString(MARGIN + 398, y - hdr_h + 4, "PTS")
c.drawString(MARGIN + 440, y - hdr_h + 4, "CONFLUENT PT")
y -= hdr_h
row_h = 15
for i, (v, course, fn, pts, conf) in enumerate(ref_rows):
    bg = CARD_BG if i % 2 == 0 else PAGE_BG
    box(c, MARGIN, y, CONTENT_W, row_h, bg)
    set_fill(c, BLACK); c.setFont("Lora", 7.6)
    c.drawString(MARGIN + 6, y - row_h + 4.5, v)
    c.drawString(MARGIN + 108, y - row_h + 4.5, course)
    c.drawString(MARGIN + 258, y - row_h + 4.5, fn)
    c.drawString(MARGIN + 398, y - row_h + 4.5, pts)
    c.drawString(MARGIN + 440, y - row_h + 4.5, conf)
    y -= row_h
y -= 10
set_fill(c, GRAY); c.setFont("Lora-Italic", 7.8)
c.drawString(MARGIN, y, "Fill in/correct this table as Dr. Zhang confirms details in lecture -- treat it as a pre-lecture best guess, not a final answer key.")

footer(c, FOOTER_LABEL, 2, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION B
y = section_header(c, "B", "Activate -- Connect to What You Know")
y = purpose_box(c, y, [
    "Purpose: Activating prior knowledge before new input improves encoding.",
    "B1: Write what the lecture deck previewed about these 8 vessels. B2: fill in before lecture.",
])

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B1 . What the Lecture Deck Already Shows You")
y -= 16
y = draw_paragraph(c,
    "The Eight Extraordinary Vessels regulate, connect, and store Qi and blood, acting as reservoirs and "
    "balancing the twelve primary meridians. Only the Governor Vessel and Conception Vessel have their own "
    "dedicated acupuncture points -- the other six (Chong, Dai, Yang Qiao, Yin Qiao, Yang Wei, Yin Wei) share "
    "points with the primary meridians they cross. None of the eight pertains to a zang/fu organ, which is "
    "the single biggest structural difference from the 12 primary meridians.",
    MARGIN, y, CONTENT_W, size=9, leading=12.2)
y -= 6
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(MARGIN, y, "Write it in your own words -- what do you think these 8 vessels DO that primary channels alone don't?")
y -= 10
y = write_box(c, y, CONTENT_W, 70, gold_bar=True, fill=CARD_BG, n_lines=3)
y -= 18

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B2 . Connect the Dots -- complete before lecture")
y -= 20
for before, bw, after in CONNECT_BLANKS:
    y = fill_blank_line(c, before, bw, after, MARGIN, y, size=8.8)
    y -= 20

y -= 4
hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=(0.85, 0.85, 0.82), w=0.6)
y -= 18
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B3 . Why This Matters Clinically")
y -= 16
y = draw_paragraph(c,
    "The Eight Extraordinary Vessels aren't just an academic add-on -- they're the vessels you reach for when "
    "primary-channel points alone don't fully resolve a pattern. Because six of the eight share points with "
    "primary meridians (only GV and CV have dedicated points of their own), the same acupoint can be treated as "
    "'on the Kidney meridian' or 'opening the Yin Qiao,' depending on clinical intent. The 4 confluent point "
    "pairs (SP4/PC6, SI3/BL62, LU7/KI6, GB41/SJ5) are the classic clinical entry point for this system: each "
    "pair is traditionally needled together to 'open' its vessel pairing for conditions distributed along both "
    "vessels' pathways -- e.g. SP4+PC6 for chest/abdomen/heart patterns, or LU7+KI6 for throat/chest/lung-kidney "
    "patterns.",
    MARGIN, y, CONTENT_W, size=8.8, leading=12)
y -= 10
set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "Memory anchor: pair each confluent point with its vessel BEFORE lecture --")
y -= 14
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(MARGIN, y, "the pairing itself (not just the 8 individual points) is what's most often tested.")

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
c.drawString(MARGIN, y, "The 4 Confluent (Master-Couple) Point Pairs -- fill in as Dr. Zhang confirms in lecture")
y -= 16
row_h = 15.5
hdr_h = 14
set_fill(c, NAVY)
c.rect(MARGIN, y - hdr_h, CONTENT_W, hdr_h, stroke=0, fill=1)
set_fill(c, WHITE); c.setFont("Lora-Bold", 7.6)
c.drawString(MARGIN + 8, y - hdr_h + 4, "VESSEL PAIRING")
c.drawString(MARGIN + 280, y - hdr_h + 4, "POINT A")
c.drawString(MARGIN + 400, y - hdr_h + 4, "POINT B")
y -= hdr_h
for i, (pairing, pa, pb) in enumerate(CONFLUENT_PAIRS):
    bg = CARD_BG if i % 2 == 0 else PAGE_BG
    box(c, MARGIN, y, CONTENT_W, row_h, bg)
    set_fill(c, BLACK); c.setFont("Lora", 8.4)
    c.drawString(MARGIN + 8, y - row_h + 5, pairing)
    c.drawString(MARGIN + 280, y - row_h + 5, pa)
    c.drawString(MARGIN + 400, y - row_h + 5, pb)
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

y = draw_group(y, "GV & CV -- The Sea Vessels", ANTICIPATORY_SEA_VESSELS, ACCENT_GV)
footer(c, FOOTER_LABEL, 5, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

y = section_header(c, "D", "Anticipatory Questions (continued)")
y = draw_group(y, "Chong & Dai", ANTICIPATORY_CHONG_DAI, ACCENT_CHONG)
y = draw_group(y, "Qiao & Wei -- The 4 Paired Vessels", ANTICIPATORY_QIAO_WEI, ACCENT_QIAO)

footer(c, FOOTER_LABEL, 6, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

y = section_header(c, "D", "Anticipatory Questions (continued)")
y = draw_group(y, "Systems Comparison", ANTICIPATORY_COMPARE, GOLD_DARK)

y -= 4
hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=(0.85, 0.85, 0.82), w=0.6)
y -= 18
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Reference -- Extraordinary Vessels vs. Primary Meridians")
y -= 18
comp_rows = [
    ("Pertaining Zang/Fu organ", "Yes -- each of the 12 pertains to one organ", "None -- structural difference #1"),
    ("Own dedicated points", "Yes -- all 12 have a full point set", "Only GV and CV; other 6 share points"),
    ("Direction of flow", "Fixed circulation order (LU->LI->...->LR->LU)", "No fixed sequential circulation"),
    ("Yin/Yang pairing", "Paired Biao-Li (interior-exterior) partners", "No Biao-Li pairing between the 8"),
    ("Core role", "Transport Qi/Blood to organs, resist pathogens", "Reservoir/regulator -- overflow storage"),
]
hdr_h = 14
set_fill(c, NAVY); c.rect(MARGIN, y - hdr_h, CONTENT_W, hdr_h, stroke=0, fill=1)
set_fill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(MARGIN + 6, y - hdr_h + 4, "FEATURE")
c.drawString(MARGIN + 140, y - hdr_h + 4, "12 PRIMARY MERIDIANS")
c.drawString(MARGIN + 340, y - hdr_h + 4, "8 EXTRAORDINARY VESSELS")
y -= hdr_h
row_h = 28
for i, (feat, prim, extra) in enumerate(comp_rows):
    bg = CARD_BG if i % 2 == 0 else PAGE_BG
    box(c, MARGIN, y, CONTENT_W, row_h, bg)
    set_fill(c, BLACK); c.setFont("Lora-Bold", 7.6)
    c.drawString(MARGIN + 6, y - 11, feat)
    c.setFont("Lora", 7.4)
    for j, ln in enumerate(wrap_text(prim, "Lora", 7.4, 192)):
        c.drawString(MARGIN + 140, y - 11 - j * 9.5, ln)
    for j, ln in enumerate(wrap_text(extra, "Lora", 7.4, 200)):
        c.drawString(MARGIN + 340, y - 11 - j * 9.5, ln)
    y -= row_h
y -= 8
set_fill(c, GRAY); c.setFont("Lora-Italic", 7.8)
c.drawString(MARGIN, y, "Use this table to answer Q12 -- the single biggest structural difference is the pertaining organ.")

footer(c, FOOTER_LABEL, 7, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= IQ (Inter-Quiz)
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

y -= 4
hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=(0.85, 0.85, 0.82), w=0.6)
y -= 18
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Quick-Fire Recall -- The 4 Confluent Pairs (cover and recite)")
y -= 18
for pairing, pa, pb in CONFLUENT_PAIRS:
    set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.6)
    c.drawString(MARGIN + 10, y, "\u2022")
    set_fill(c, BLACK); c.setFont("Lora", 8.8)
    c.drawString(MARGIN + 22, y, f"{pairing}:  {pa}  <->  {pb}")
    y -= 15
y -= 4
set_fill(c, GRAY); c.setFont("Lora-Italic", 7.8)
c.drawString(MARGIN, y, "Cover the right-hand columns of the Section C table and try to reproduce this list from memory.")

footer(c, FOOTER_LABEL, 8, TOTAL_PAGES)
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
y -= 26

hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=(0.85, 0.85, 0.82), w=0.6)
y -= 18
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Common Confusions to Watch For")
y -= 18
confusions = [
    "GV vs CV \u201csea\u201d titles are easy to swap under quiz pressure -- GV = yang (posterior/back), CV = yin (anterior/front). Anchor it to body position, not just memorized words.",
    "\u201cConfluent point\u201d (1 point per vessel, used to open it) is not the same as \u201ccoalescent point\u201d (any point where the vessel crosses a primary meridian along its course) -- don't conflate the two terms.",
    "Only GV and CV have their own point sets; it's tempting to assume all 8 vessels do, since the primary 12 meridians all do -- this is the #1 structural trap for this week.",
]
for note in confusions:
    box_h = 10 + len(wrap_text(note, "Lora", 8.4, CONTENT_W - 24)) * 11.5
    set_fill(c, (0.965, 0.955, 0.93))
    c.rect(MARGIN, y - box_h, CONTENT_W, box_h, stroke=0, fill=1)
    set_stroke(c, GOLD_DARK); c.setLineWidth(2)
    c.line(MARGIN, y - box_h, MARGIN, y)
    ty = y - 12
    set_fill(c, BLACK); c.setFont("Lora", 8.4)
    for l in wrap_text(note, "Lora", 8.4, CONTENT_W - 24):
        c.drawString(MARGIN + 12, ty, l); ty -= 11.5
    y -= box_h + 10

footer(c, FOOTER_LABEL, 9, TOTAL_PAGES)
c.showPage()
paint_page_bg(c)

# ============================================================= SECTION E + F
y = section_header(c, "E", "Clinical Case -- Apply It Before & After")
y = purpose_box(c, y, [
    "Purpose: Case reasoning bridges textbook concepts to clinical logic. Struggling before lecture is expected.",
])
set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Case Vignette: Mr. Patel, 44 years old")
y -= 16
y = draw_paragraph(c,
    "Mr. Patel reports several weeks of difficulty falling asleep -- he feels wired and restless at bedtime, "
    "with a racing quality to his thoughts at night, but is groggy and low-energy through the day. He denies "
    "chest pain, palpitations, or overt anxiety symptoms. He mentions his ankles feel 'tight' on the outer "
    "side lately, though he isn't sure that's related. Tongue and pulse are otherwise unremarkable.",
    MARGIN, y, CONTENT_W, size=9.2, leading=12.4)
y -= 8
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.4)
c.drawString(MARGIN, y, "Pre-lecture: which pair of extraordinary vessels regulates sleep/wake balance, and which one would you consider calming (Yang or Yin)?")
y -= 10
y = write_box(c, y, CONTENT_W, 55, gold_bar=True, fill=CARD_BG, n_lines=2)
y -= 16
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.4)
c.drawString(MARGIN, y, "Post-lecture: revise your answer with what Dr. Zhang actually teaches about the confluent points for these vessels.")
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
