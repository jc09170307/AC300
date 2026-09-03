#!/usr/bin/env python3
"""AC300 Week 9 Pre-Lecture Analysis / Lecture Consolidation Sheet -- Five
Shu Points, Confluent Points, Collaterals, Cutaneous Regions, Final Exam
Review. Follows the Behavioral Interteaching structure (Sections A-F +
Inter-Quiz) Jon uses every week. This lecture has already occurred, so this
sheet is framed as a consolidation tool. Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk9")
from common_wk9 import (DocBuilder, setfill, setstroke, box, hairline, draw_paragraph,
                         wrap_words, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED,
                         LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM,
                         EDLABEL)
from wk9_content import (VOCAB, LEARNING_TARGETS, ANTICIPATORY_QUESTIONS, IQ_CHECKPOINTS,
                          IQ_ANSWERS, CLINICAL_CASE, CLINICAL_CASE_PRE_Q, CLINICAL_CASE_POST_Q,
                          HOMEWORK_QUIZ_NOTE, READING_NOTE, CONFIRMATION_NOTE, ACCENT_FIVESHU,
                          ACCENT_CONFLUENT, ACCENT_LUO)

OUT = f"/mnt/user-data/outputs/AC300_Week9_PrepGuide_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 9 Lecture Consolidation Sheet"
FOOTER = "AC300/AC375 | Week 9 | Points, Final Exam Review | VUIM Summer 2026"
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
            c.drawString(ML + 14, ty, l2); ty -= 11.5
    return y - bh - 12


def confidence_row(y, text):
    y = draw_paragraph(c, text, ML, y, CW, font="Lora", size=9.3, leading=12, color=DARK)
    y -= 2
    setfill(c, LGRAY); c.setFont("Lora", 8)
    c.drawString(ML, y, "Pre")
    xx = ML + 30
    c.setFont("Lora", 9); setfill(c, DARK)
    for n in range(1, 6):
        c.drawString(xx, y, str(n)); xx += 15
    setfill(c, LGRAY); c.setFont("Lora", 8)
    c.drawString(ML + 260, y, "Post")
    xx = ML + 290
    c.setFont("Lora", 9); setfill(c, DARK)
    for n in range(1, 6):
        c.drawString(xx, y, str(n)); xx += 15
    y -= 8
    hairline(c, ML, y, RX, rgb=(0.85, 0.85, 0.82), w=0.6)
    return y - 12


def write_lines(y, h, n=2):
    box(c, ML, y, CW, h, CARD_BG)
    setfill(c, GOLD); c.rect(ML, y - h, 3, h, fill=1, stroke=0)
    ly = y - 16
    for i in range(n):
        hairline(c, ML + 12, ly, RX - 10, rgb=(0.78, 0.72, 0.55), w=0.6)
        ly -= 16
    return y - h


# ============================================================
# COVER
# ============================================================
db.new_page(bare=True)
y = H - 70
setfill(c, GOLD); c.setFont("Lora-Bold", 11)
c.drawCentredString(W / 2, y, "WEEK 9  \u00b7  " + EDLABEL)
y -= 36
setfill(c, NAVY); c.setFont("Lora-Bold", 26)
c.drawCentredString(W / 2, y, "Lecture Consolidation Sheet")
y -= 24
setfill(c, RED); c.setFont("Lora-BoldItalic", 14)
c.drawCentredString(W / 2, y, "Acupuncture Points \u00b7 Final Exam Master Review")
y -= 20
setfill(c, GRAY); c.setFont("Lora-Italic", 10.5)
c.drawCentredString(W / 2, y, "Five Shu Points \u00b7 Confluent Points \u00b7 15 Collaterals \u00b7 Cutaneous Regions")
y -= 24
hairline(c, (W - 240) / 2, y, (W + 240) / 2, rgb=GOLD, w=1.2)
y -= 30

setfill(c, DARK); c.setFont("Lora-Italic", 9)
note = ("This lecture has already occurred (full transcript + slide deck available), so this sheet is "
        "framed as a consolidation tool following the same Behavioral Interteaching structure "
        "(Sections A-F + Inter-Quiz) used every week, rather than a true pre-lecture draft.")
y = draw_paragraph(c, note, ML + 30, y, CW - 60, font="Lora-Italic", size=9, leading=12.4, align="center")
y -= 20

box_h = 60
box(c, ML, y, CW, box_h, tint(RED, 0.88))
setfill(c, RED); c.setFont("Lora-Bold", 9.5)
c.drawCentredString(W / 2, y - 16, "NEXT WEEK: COMPREHENSIVE FINAL EXAM")
setfill(c, DARK); c.setFont("Lora-Italic", 8.4)
y2 = draw_paragraph(c, "Material from Weeks 1-9, 30 questions. No new quiz or homework this week -- "
                        "submit outstanding Homework 5 before the final.", ML + 20, y - 32, CW - 40,
                    font="Lora-Italic", size=8.4, leading=11, align="center")
y -= box_h + 30
setfill(c, GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
db.end_page()

# ============================================================
# SECTION A -- I Can Statements
# ============================================================
db.new_page()
y = section_header("A", "I Can Statements", "Rate your confidence before AND after lecture review")
y = purpose_box(y, ["Rate your confidence (1=not at all, 5=fully confident) on each statement before "
                     "and after reviewing this week's material."])
for target in LEARNING_TARGETS:
    y = confidence_row(y, "I can " + target[0].lower() + target[1:])
db.end_page()

# ============================================================
# SECTION B -- Activate/Connect
# ============================================================
db.new_page()
y = section_header("B", "Activate & Connect", "Bridging from Week 8")
y = purpose_box(y, ["Before diving into new content, reconnect with what Week 8 already established."])
setfill(c, DARK)
y = draw_paragraph(c, CONFIRMATION_NOTE, ML, y, CW, size=9, leading=12.4)
y -= 16
setfill(c, NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "Quick recall (no peeking):")
y -= 18
prompts = [
    "What are the 3 extra Collaterals (not tied to a paired-organ meridian)?",
    "Name any 2 of the 8 Confluent Points and their paired vessel.",
    "Why do Cutaneous Regions form only 6 groups instead of 12?",
]
for p in prompts:
    y = draw_paragraph(c, "\u2022 " + p, ML + 4, y, CW - 4, size=9.2, leading=12.4)
    y -= 4
    y = write_lines(y, 22, n=1)
    y -= 10
db.end_page()

# ============================================================
# SECTION C -- Vocabulary
# ============================================================
db.new_page()
y = section_header("C", "Vocabulary Pre-Load", "Pinyin -> English, no CJK")
setfill(c, GRAY); c.setFont("Lora-Bold", 8.5)
c.drawString(ML, y, "PINYIN")
c.drawString(ML + 170, y, "ENGLISH")
c.drawString(ML + 400, y, "MY NOTE")
y -= 6
hairline(c, ML, y, RX, rgb=NAVY, w=1)
y -= 14
for pinyin, english, accent in VOCAB:
    if accent:
        box(c, ML, y + 10, CW, 20, tint(accent, 0.85))
    setfill(c, DARK); c.setFont("Lora", 9)
    c.drawString(ML, y, pinyin)
    c.drawString(ML + 170, y, english)
    hairline(c, ML + 400, y - 3, RX, rgb=(0.8, 0.8, 0.76), w=0.5)
    y -= 20
db.end_page()

# ============================================================
# SECTION D -- Anticipatory Questions
# ============================================================
db.new_page()
y = section_header("D", "Anticipatory Questions", "* = high exam probability")
for qnum, star, topic, question in ANTICIPATORY_QUESTIONS:
    label = f"Q{qnum}{'*' if star else ''}"
    setfill(c, GOLD); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML, y, label)
    setfill(c, DARK); c.setFont("Lora-Bold", 9)
    c.drawString(ML + 34, y, topic.upper())
    y -= 14
    y = draw_paragraph(c, question, ML + 16, y, CW - 16, size=9, leading=12)
    y -= 4
    y = write_lines(y, 40, n=2)
    y -= 14
db.end_page()

# ============================================================
# SECTION E -- Inter-Quiz
# ============================================================
db.new_page()
y = section_header("E", "Inter-Quiz", "Checkpoint self-test -- ACQ (new) / MAINT (review)")
y = purpose_box(y, ["Answer from memory, then check the answer key at the end of this section. Score "
                     "yourself before moving on."])
for num, tag, text in IQ_CHECKPOINTS:
    setfill(c, NAVY); c.setFont("Lora-Bold", 9)
    c.drawString(ML, y, str(num))
    setfill(c, LGRAY); c.setFont("Lora-Italic", 7.3)
    c.drawString(ML + 16, y, tag)
    setfill(c, DARK); c.setFont("Lora", 9)
    y2 = draw_paragraph(c, text, ML + 58, y, CW - 58, size=9, leading=12)
    y = min(y2, y - 12) - 10
db.end_page()

db.new_page()
y = section_header("E", "Inter-Quiz \u2014 Answer Key", None)
for i, ans in enumerate(IQ_ANSWERS):
    setfill(c, RED); c.setFont("Lora-Bold", 9)
    c.drawString(ML, y, f"{i+1}.")
    setfill(c, DARK); c.setFont("Lora", 9)
    y2 = draw_paragraph(c, ans, ML + 20, y, CW - 20, size=9, leading=12.2)
    y = min(y2, y - 12) - 8
y -= 8
box_h = 20
box(c, ML, y, CW, box_h, CARD_BG)
setfill(c, GRAY); c.setFont("Lora-Italic", 8)
c.drawString(ML + 10, y - 13, "Self-check now -- score this block: ___ / " + str(len(IQ_CHECKPOINTS)) + " before moving on.")
db.end_page()

# ============================================================
# SECTION F -- Clinical Case + Synthesis
# ============================================================
db.new_page()
y = section_header("F", "Clinical Case \u2014 Before-Lecture", "PCOS/PMOS presentation")
setfill(c, DARK)
y = draw_paragraph(c, CLINICAL_CASE, ML, y, CW, size=9.4, leading=12.6)
y -= 16
setfill(c, NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "Pre-Lecture Question:")
y -= 16
y = draw_paragraph(c, CLINICAL_CASE_PRE_Q, ML, y, CW, size=9.2, leading=12.4)
y -= 8
y = write_lines(y, 70, n=4)
y -= 20

setfill(c, NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "After-Lecture Synthesis Question:")
y -= 16
y = draw_paragraph(c, CLINICAL_CASE_POST_Q, ML, y, CW, size=9.2, leading=12.4)
y -= 8
y = write_lines(y, 90, n=5)
y -= 16
box_lines_hw = wrap_words(HOMEWORK_QUIZ_NOTE, "Lora-Italic", 8, CW - 18)
hw_h = len(box_lines_hw) * 10.6 + 16
box(c, ML, y, CW, hw_h, tint(RED, 0.87))
setfill(c, RED); c.setFont("Lora-Bold", 8.4); c.drawString(ML + 8, y - 12, "NEXT WEEK: FINAL EXAM")
ty = y - 24
setfill(c, DARK); c.setFont("Lora-Italic", 8)
for ln in box_lines_hw:
    c.drawString(ML + 8, ty, ln); ty -= 10.6
db.end_page()

db.save()
