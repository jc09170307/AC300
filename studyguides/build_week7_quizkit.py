#!/usr/bin/env python3
"""AC300 Week 7 Quiz Kit -- standalone practice exam for the Eight
Extraordinary Vessels. MC + confluent-point matching + fill-in-blank +
short answer + MAINT review, with full answer key. Print + reMarkable."""
import sys
sys.path.insert(0, "/home/claude/ac300wk7")
from common_wk7 import (DocBuilder, setfill, setstroke, box, hairline, draw_paragraph,
                         wrap_words, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED,
                         LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM,
                         EDLABEL)
from wk7_quiz_questions import (MC_QUESTIONS, CONFLUENT_MATCH_LEFT, CONFLUENT_MATCH_RIGHT,
                                 CONFLUENT_MATCH_ANSWER, FILL_BLANK, SHORT_ANSWER, MAINT_QUESTIONS,
                                 CROSSING_POINT_QUESTIONS)

OUT = f"/mnt/user-data/outputs/AC300_Week7_QuizKit_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 7 Quiz Kit"
FOOTER = "AC300/AC375 | Week 7 Quiz Kit | Eight Extraordinary Vessels | VUIM Summer 2026"
MINT = (0.938, 0.960, 0.958)
LGRAY2 = (0.950, 0.947, 0.963)

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def title_bar(title, subtitle_right=None):
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, NAVY); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 14.5)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        c.setFont("Lora-Italic", 9)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot - 10


# --------------------------- MC question cards ---------------------------

def mc_card_h(q, choices):
    lines_q = wrap_words(q, "Lora-Bold", 9.4, CW - 40)
    col_w = CW / 2 - 40
    opt_lines = [wrap_words(o, "Lora", 8.6, col_w) for o in choices]
    pairs = [(opt_lines[0], opt_lines[1]), (opt_lines[2], opt_lines[3])]
    row_h = [max(len(l), len(r)) * 10.8 for l, r in pairs]
    return 16 + len(lines_q) * 12 + sum(row_h) + 8


def mc_card(y, num, q, choices, tint_c):
    lines_q = wrap_words(q, "Lora-Bold", 9.4, CW - 40)
    col_w = CW / 2 - 40
    opt_lines = [wrap_words(o, "Lora", 8.6, col_w) for o in choices]
    pairs = [(opt_lines[0], opt_lines[1]), (opt_lines[2], opt_lines[3])]
    row_hs = [max(len(l), len(r)) * 10.8 for l, r in pairs]
    card_h = 16 + len(lines_q) * 12 + sum(row_hs) + 8
    setfill(c, tint_c); c.rect(ML, y - card_h, CW, card_h, fill=1, stroke=0)
    setfill(c, NAVY); c.rect(ML + 4, y - 21, 17, 17, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 9)
    c.drawCentredString(ML + 12.5, y - 16.5, str(num))
    qy = y - 13
    tx = ML + 30
    setfill(c, DARK); c.setFont("Lora-Bold", 9.4)
    for l in lines_q:
        c.drawString(tx, qy, l); qy -= 12
    qy -= 3
    letters = ["A.", "B.", "C.", "D."]
    col2_x = ML + CW / 2 + 8
    for i, (left_lines, right_lines) in enumerate(pairs):
        li = i * 2
        row_top = qy
        setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.4)
        c.drawString(tx, row_top, letters[li])
        setfill(c, DARK); c.setFont("Lora", 8.6)
        for j, l in enumerate(left_lines):
            c.drawString(tx + 15, row_top - j * 10.8, l)
        setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8.4)
        c.drawString(col2_x, row_top, letters[li + 1])
        setfill(c, DARK); c.setFont("Lora", 8.6)
        for j, l in enumerate(right_lines):
            c.drawString(col2_x + 15, row_top - j * 10.8, l)
        qy -= row_hs[i]
    return y - card_h - 6


def paginate(items, measure_fn):
    groups, idx = [], 0
    while idx < len(items):
        y = (H - 74) - 10
        start = idx
        while idx < len(items):
            h = measure_fn(items[idx])
            if y - h < 55:
                break
            y -= h + 6
            idx += 1
        if idx == start:
            idx += 1
        groups.append((start, idx))
    return groups


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
c.drawString(ML, y, "Week 7 Quiz Kit")
y -= 28
setfill(c, RED); c.setFont("Lora-Bold", 17)
c.drawString(ML, y, "The Eight Extraordinary Vessels")
y -= 22
setfill(c, GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "Standalone practice quiz -- pairs with the Week 7 Study Guide")
y -= 18
hairline(c, ML, y, RX, rgb=GOLD, w=1.2)
y -= 28
setfill(c, RED); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Kit Covers:")
y -= 20
setfill(c, DARK); c.setFont("Lora", 10.5)
bullets = [
    f"{len(MC_QUESTIONS)}-Question MCQ Section \u2014 vessel identity, sea titles, point counts, structural traits",
    "Confluent Point Matching \u2014 all 4 master-couple pairs (8 points)",
    "Fill-in-the-Blank \u2014 coalescent points, Luo-Connecting overlaps, first/last points",
    "Short Answer \u2014 pathology recognition tied to specific vessels",
    "MAINT Review \u2014 pulled directly from Dr. Zhang's live Quiz 5 review (PC/SJ/GB/LR)",
    "Crossing-Point Review \u2014 Dr. Zhang's own Q1/Q2/Q3 (GV14 intersections, supraclavicular fossa, periocular meridians)",
    "Full Answer Key with explanations for every question",
]
for b in bullets:
    setfill(c, GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(c, DARK)
    lines = wrap_words(b, "Lora", 10.5, CW - 20)
    for i, l in enumerate(lines):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(lines)) + 4

y -= 8
box_h = 58
box(c, ML, y, CW, box_h, tint(GOLD, 0.88))
setfill(c, DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 16, y - 18, "QUIZ 6 (next week) covers: the Eight Extraordinary Vessels + cumulative Middle Circuit review.")
c.drawString(ML + 16, y - 32, "Study first from the Week 7 Study Guide, then self-test here before class.")
c.drawString(ML + 16, y - 46, "Answer key begins after the final question block \u2014 no peeking until you've answered!")
y -= box_h + 40
setfill(c, GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
db.end_page()

# ============================================================
# SECTION A -- MC questions, auto-paginated
# ============================================================
groups = paginate(MC_QUESTIONS, lambda item: mc_card_h(item["q"], item["choices"]))
for gi, (start, end) in enumerate(groups):
    db.new_page()
    y = title_bar(f"Section A: Multiple Choice  \u2014  Q{start+1}-{end} (of {len(MC_QUESTIONS)})",
                   "Vessel identity, sea titles, structure")
    for i in range(start, end):
        item = MC_QUESTIONS[i]
        tc = MINT if (i - start) % 2 == 0 else LGRAY2
        y = mc_card(y, i + 1, item["q"], item["choices"], tc)
    db.end_page()

# ============================================================
# SECTION B -- Confluent Point Matching
# ============================================================
db.new_page()
y = title_bar("Section B: Confluent Point Matching", "Match each vessel to its confluent point")
y -= 10
setfill(c, DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML, y, "Match each vessel (left) to its confluent/opening point (right). Each letter is used exactly once.")
y -= 22
col_w = CW / 2 - 10
for i, left in enumerate(CONFLUENT_MATCH_LEFT):
    ly = y - i * 24
    box(c, ML, ly, col_w, 20, MINT if i % 2 == 0 else (1, 1, 1))
    setfill(c, DARK); c.setFont("Lora", 9.5)
    c.drawString(ML + 8, ly - 14, left)
    setfill(c, GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawString(ML + col_w - 60, ly - 14, "Answer: ____")
right_x = ML + col_w + 20
for i, right in enumerate(CONFLUENT_MATCH_RIGHT):
    ly = y - i * 24
    box(c, right_x, ly, col_w, 20, LGRAY2 if i % 2 == 0 else (1, 1, 1))
    setfill(c, DARK); c.setFont("Lora", 9.5)
    c.drawString(right_x + 8, ly - 14, right)
y -= 8 * 24 + 30

setfill(c, NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "Bonus: name the shared clinical indication for each pair (from the Study Guide/Cram Sheet).")
db.end_page()

# ============================================================
# SECTION C -- Fill in the Blank
# ============================================================
db.new_page()
y = title_bar("Section C: Fill in the Blank", None)
y -= 14
for i, (prompt, ans) in enumerate(FILL_BLANK):
    lines = wrap_words(f"{i+1}. {prompt}", "Lora", 9.6, CW - 8)
    box_h = 12 * len(lines) + 22
    box(c, ML, y, CW, box_h, MINT if i % 2 == 0 else (1, 1, 1))
    setfill(c, DARK); c.setFont("Lora", 9.6)
    ty = y - 13
    for l in lines:
        c.drawString(ML + 8, ty, l); ty -= 12
    y -= box_h + 6
db.end_page()

# ============================================================
# SECTION D -- Short Answer
# ============================================================
db.new_page()
y = title_bar("Section D: Short Answer \u2014 Pathology Recognition", None)
y -= 14
for i, item in enumerate(SHORT_ANSWER):
    lines = wrap_words(f"{i+1}. {item['q']}", "Lora-Bold", 9.4, CW - 16)
    box_h = 12.2 * len(lines) + 46
    box(c, ML, y, CW, box_h, MINT if i % 2 == 0 else (1, 1, 1))
    setfill(c, DARK); c.setFont("Lora-Bold", 9.4)
    ty = y - 13
    for l in lines:
        c.drawString(ML + 8, ty, l); ty -= 12.2
    ty -= 4
    hairline(c, ML + 8, ty, RX - 8, rgb=(0.75, 0.75, 0.7), w=0.5); ty -= 16
    hairline(c, ML + 8, ty, RX - 8, rgb=(0.75, 0.75, 0.7), w=0.5)
    y -= box_h + 8
db.end_page()

# ============================================================
# SECTION E -- MAINT Review
# ============================================================
db.new_page()
y = title_bar("Section E: MAINT Review \u2014 PC/SJ/GB/LR", "From Dr. Zhang's live Quiz 5 review")
y -= 14
for i, item in enumerate(MAINT_QUESTIONS):
    lines = wrap_words(f"{i+1}. {item['q']}", "Lora-Bold", 9.4, CW - 16)
    box_h = 12.2 * len(lines) + 34
    box(c, ML, y, CW, box_h, LGRAY2 if i % 2 == 0 else (1, 1, 1))
    setfill(c, DARK); c.setFont("Lora-Bold", 9.4)
    ty = y - 13
    for l in lines:
        c.drawString(ML + 8, ty, l); ty -= 12.2
    ty -= 6
    hairline(c, ML + 8, ty, RX - 8, rgb=(0.75, 0.75, 0.7), w=0.5)
    y -= box_h + 8
db.end_page()

# ============================================================
# SECTION F -- Crossing-Point Review (new, Dr. Zhang's own Q1/Q2/Q3)
# ============================================================
db.new_page()
y = title_bar("Section F: Crossing-Point Review", "Dr. Zhang's own end-of-lecture questions (2026 deck)")
y -= 14
for i, item in enumerate(CROSSING_POINT_QUESTIONS):
    lines = wrap_words(f"Q{i+1}. {item['q']}", "Lora-Bold", 9.4, CW - 16)
    box_h = 12.2 * len(lines) + 34
    box(c, ML, y, CW, box_h, MINT if i % 2 == 0 else (1, 1, 1))
    setfill(c, DARK); c.setFont("Lora-Bold", 9.4)
    ty = y - 13
    for l in lines:
        c.drawString(ML + 8, ty, l); ty -= 12.2
    ty -= 6
    hairline(c, ML + 8, ty, RX - 8, rgb=(0.75, 0.75, 0.7), w=0.5)
    y -= box_h + 8
db.end_page()

# ============================================================
# ANSWER KEY
# ============================================================

def answer_row(y, label, ans_text, expl):
    lines = wrap_words(ans_text, "Lora-Bold", 9.3, CW - 60)
    lines_e = wrap_words(expl, "Lora-Italic", 8, CW - 60) if expl else []
    row_h = 13 + (len(lines) - 1) * 11.5 + (12 + len(lines_e) * 10.4 if lines_e else 4)
    box(c, ML, y, CW, row_h, MINT)
    setfill(c, RED); c.setFont("Lora-Bold", 9.3)
    c.drawString(ML + 6, y - 12, label)
    setfill(c, DARK); c.setFont("Lora-Bold", 9.3)
    ty = y - 12
    for l in lines:
        c.drawString(ML + 50, ty, l); ty -= 11.5
    if lines_e:
        setfill(c, GRAY); c.setFont("Lora-Italic", 8)
        ty -= 1
        for l in lines_e:
            c.drawString(ML + 50, ty, l); ty -= 10.4
    return y - row_h - 3


def measure_answer_row(ans_text, expl):
    lines = wrap_words(ans_text, "Lora-Bold", 9.3, CW - 60)
    lines_e = wrap_words(expl, "Lora-Italic", 8, CW - 60) if expl else []
    row_h = 13 + (len(lines) - 1) * 11.5 + (12 + len(lines_e) * 10.4 if lines_e else 4)
    return row_h + 3


db.new_page()
y = title_bar("Answer Key \u2014 Section A (Multiple Choice)", None)
y -= 8
for i, item in enumerate(MC_QUESTIONS):
    ans_letter = "ABCD"[item["answer"]]
    ans_text = f"Q{i+1}: {ans_letter}. {item['choices'][item['answer']]}"
    rh = measure_answer_row(ans_text, item["explain"])
    if y - rh < 55:
        db.end_page(); db.new_page(); y = title_bar("Answer Key \u2014 Section A (continued)", None); y -= 8
    y = answer_row(y, f"{i+1}.", ans_text, item["explain"])
db.end_page()

db.new_page()
y = title_bar("Answer Key \u2014 Sections B-E", None)
y -= 10
setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Section B: Confluent Point Matching")
y -= 16
setfill(c, DARK); c.setFont("Lora", 9)
match_line = "  ".join(f"{k}-{v}" for k, v in CONFLUENT_MATCH_ANSWER.items())
y = draw_paragraph(c, match_line, ML, y, CW, size=9, leading=12)
y -= 12

setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Section C: Fill in the Blank")
y -= 16
for i, (prompt, ans) in enumerate(FILL_BLANK):
    rh = measure_answer_row(f"{i+1}. {ans}", None)
    if y - rh < 55:
        db.end_page(); db.new_page(); y = title_bar("Answer Key \u2014 Sections B-E (continued)", None); y -= 10
    y = answer_row(y, "", f"{i+1}. {ans}", None)
y -= 6

setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Section D: Short Answer")
y -= 16
for i, item in enumerate(SHORT_ANSWER):
    rh = measure_answer_row(f"{i+1}.", item["answer"])
    if y - rh < 55:
        db.end_page(); db.new_page(); y = title_bar("Answer Key \u2014 Sections B-E (continued)", None); y -= 10
    y = answer_row(y, "", item["answer"], None)
y -= 6

setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Section E: MAINT Review")
y -= 16
for i, item in enumerate(MAINT_QUESTIONS):
    rh = measure_answer_row(f"{i+1}.", item["answer"])
    if y - rh < 55:
        db.end_page(); db.new_page(); y = title_bar("Answer Key \u2014 Sections B-E (continued)", None); y -= 10
    y = answer_row(y, "", item["answer"], None)
y -= 6

setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Section F: Crossing-Point Review")
y -= 16
for i, item in enumerate(CROSSING_POINT_QUESTIONS):
    rh = measure_answer_row(f"Q{i+1}.", item["answer"])
    if y - rh < 55:
        db.end_page(); db.new_page(); y = title_bar("Answer Key \u2014 Sections B-F (continued)", None); y -= 10
    y = answer_row(y, "", f"Q{i+1}: " + item["answer"], None)

db.end_page()
db.save()
