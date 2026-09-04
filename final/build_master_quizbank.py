#!/usr/bin/env python3
"""AC300 Master Quiz Bank & Key -- Print + reMarkable.
Usage: python3 build_master_quizbank.py <print|remarkable>
"""
import sys
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, '.')
from quizbank_data import REAL_QUIZZES, BONUS_WEEKS

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
TEAL = (0.106, 0.369, 0.353)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

QUIZ_ACCENTS = {1: (0.365, 0.408, 0.451), 2: (0.663, 0.478, 0.169), 3: (0.690, 0.204, 0.169),
                4: (0.850, 0.420, 0.380), 5: (0.380, 0.180, 0.522), 6: (0.200, 0.480, 0.270)}
BONUS_ACCENT = GRAY

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_MasterQuizBank_Wk1-9_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_MasterQuizBank_Wk1-9_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


page_num = [1]
TOC_ENTRIES = []


def toc_mark(title, indent=0):
    TOC_ENTRIES.append((title, page_num[0], indent))


ML, MR = 36, 36
CW = W - ML - MR


def header(subtitle=""):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    c.drawString(ML, H - HEADER_H + 15, "AC300 MASTER QUIZ BANK")
    if subtitle:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle[:70])


def footer():
    setstroke(GOLD); c.setLineWidth(HAIRLINE)
    c.line(ML, 34, W - ML, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Master Quiz Bank (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}")


def new_page(subtitle=""):
    page_bg()
    header(subtitle)


def end_page():
    footer()
    c.showPage()
    page_num[0] += 1


y = [H - HEADER_H - 24]


def ensure_space(needed, subtitle):
    if y[0] - needed < 50:
        end_page()
        new_page(subtitle)
        y[0] = H - HEADER_H - 24


def section_bar(text, accent=NAVY, sub=""):
    lines = wrap_words(text, "Lora-Bold", 13, CW - (pdfmetrics.stringWidth(sub, "Lora-Italic", 9) + 20 if sub else 0))
    line_h = 15
    est_h = len(lines) * line_h + 12
    ensure_space(est_h + 10, "")
    setfill(accent); c.rect(ML, y[0] - est_h + 6, 3, est_h - 6, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", 13)
    for ln in lines:
        c.drawString(ML + 10, yy - 11, ln)
        yy -= line_h
    if sub:
        setfill(GRAY); c.setFont("Lora-Italic", 9)
        c.drawRightString(ML + CW, y[0] - 11, sub)
    y[0] -= est_h
    setstroke(accent); c.setLineWidth(1.2)
    c.line(ML, y[0] + 2, ML + CW, y[0] + 2)
    y[0] -= 10


def para(text, size=8.6, color=DARK, font="Lora", gap=6):
    lines = wrap_words(text, font, size, CW)
    needed = len(lines) * (size * 1.35) + gap
    ensure_space(needed, "")
    setfill(color); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML, y[0], ln)
        y[0] -= size * 1.35
    y[0] -= gap


# =====================================================================
# COVER
# =====================================================================
page_bg()
setfill(NAVY); c.rect(0, H - 90, W, 90, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 90, W, 4, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 24)
c.drawCentredString(W / 2, H - 55, "AC300 MASTER QUIZ BANK & KEY")
c.setFont("Lora-Italic", 12)
c.drawCentredString(W / 2, H - 78, EDLABEL)

yy = H - 150
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawCentredString(W / 2, yy, "The REAL Quiz 1-6, Confirmed From Live-Class Transcripts")
yy -= 24
setfill(DARK); c.setFont("Lora", 10)
for ln in wrap_words(
    "Dr. Zhang states the quiz number out loud in class every time -- this mapping is transcribed "
    "directly from her own words, not inferred: Week 3 \u2018begin our quiz two,\u2019 Week 4 \u2018start our quiz "
    "three,\u2019 Week 6 \u2018start the quiz four,\u2019 Week 7 \u2018take the quiz five,\u2019 Week 8 \u2018begin our q6\u2019 -- and "
    "Week 8 also directly confirms Week 9 has no quiz.", "Lora", 10, CW - 80):
    c.drawCentredString(W / 2, yy, ln)
    yy -= 15

yy -= 20
box_w = CW - 60
box_x = ML + 30
rows = [(f"Quiz {q['quiz_n']}", f"Week {q['week']} -- {q['topic']}", f"{len(q['questions'])} q") for q in REAL_QUIZZES]
setfill((0.965, 0.967, 0.972)); c.rect(box_x, yy - len(rows) * 20 - 10, box_w, len(rows) * 20 + 10, fill=1, stroke=0)
yy -= 14
for label, topic, count in rows:
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(box_x + 12, yy, label)
    setfill(DARK); c.setFont("Lora", 9.5)
    c.drawString(box_x + 65, yy, topic)
    setfill(GRAY); c.setFont("Lora", 9)
    c.drawRightString(box_x + box_w - 12, yy, count)
    yy -= 20

yy -= 30
setfill(TEAL); c.setFont("Lora-Bold", 12)
c.drawCentredString(W / 2, yy, "PLUS: Full Bonus Coverage -- Weeks 1, 5, 9")
yy -= 16
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, yy, "(no real quiz existed for these weeks -- included for complete review)")

setstroke(GOLD); c.setLineWidth(1)
c.line(ML, 70, W - ML, 70)
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 50, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's live-class quizzes, Weeks 1-9")
c.showPage()
page_num[0] += 1

# =====================================================================
# PART 1: THE REAL QUIZ 1-6
# =====================================================================
new_page("The Real Quiz 1-6")
y[0] = H - HEADER_H - 24
section_bar("PART 1 -- THE REAL QUIZ 1-6", accent=RED,
            sub="Confirmed from live-class transcripts -- this is what the final reuses")
toc_mark("Part 1 -- The Real Quiz 1-6")
para("Per Dr. Zhang's own statement: \u201cthe final exam mentions all the questions, including in the final "
     "examination, concerns from each quiz, not new question.\u201d Every question below is from a real, "
     "administered quiz -- not a practice question written to match the style.", size=8.8, color=GRAY, gap=14)

for quiz in REAL_QUIZZES:
    qn, wk, topic, questions = quiz['quiz_n'], quiz['week'], quiz['topic'], quiz['questions']
    accent = QUIZ_ACCENTS.get(qn, NAVY)
    ensure_space(60, f"Quiz {qn} -- Week {wk}")
    section_bar(f"QUIZ {qn} -- WEEK {wk}: {topic.upper()}", accent=accent, sub=f"{len(questions)} questions")
    for qd in questions:
        qtext = f"Q{qd['n']}.  {qd['q']}"
        qlines = wrap_words(qtext, "Lora-Bold", 8.8, CW)
        n_opt = len(qd['opts'])
        opt_h = 12.5
        needed = len(qlines) * 11.5 + n_opt * opt_h + 10
        ensure_space(needed, f"Quiz {qn} -- Week {wk}")
        setfill(DARK); c.setFont("Lora-Bold", 8.8)
        for ql in qlines:
            c.drawString(ML, y[0], ql)
            y[0] -= 11.5
        y[0] -= 1
        letters = ["A", "B", "C", "D"]
        c.setFont("Lora", 8.3)
        for i, opt in enumerate(qd['opts']):
            olines = wrap_words(f"{letters[i]}.  {opt}", "Lora", 8.3, CW - 14)
            setfill(DARK)
            c.drawString(ML + 14, y[0], olines[0])
            y[0] -= opt_h
            for extra in olines[1:]:
                c.drawString(ML + 28, y[0], extra)
                y[0] -= opt_h
        y[0] -= 6

end_page()

# =====================================================================
# ANSWER KEY -- PART 1
# =====================================================================
new_page("Answer Key -- Quiz 1-6")
y[0] = H - HEADER_H - 24
section_bar("ANSWER KEY -- QUIZ 1-6", accent=RED, sub="Score yourself, then read explanations for missed items")
toc_mark("Answer Key -- Quiz 1-6")

row_toggle = [0]


def answer_block(qd, tag=""):
    prefix_w = 42
    head_lines = wrap_words(qd['q'], "Lora-Bold", 8.2, CW - prefix_w)
    exp_lines = wrap_words(qd['exp'], "Lora", 7.8, CW - prefix_w)
    total_lines = len(head_lines) + len(exp_lines)
    needed = total_lines * 10.2 + 8
    ensure_space(needed, tag)

    band_h = needed - 3
    if row_toggle[0] % 2 == 0:
        setfill(ROW_TINT)
        c.rect(ML - 4, y[0] - band_h + 7, CW + 8, band_h, fill=1, stroke=0)
    row_toggle[0] += 1

    setfill(NAVY); c.setFont("Lora-Bold", 8.2)
    c.drawString(ML, y[0], f"Q{qd['n']}")
    setfill(RED)
    c.drawString(ML + 24, y[0], qd['ans'])
    setfill(NAVY)
    for hl in head_lines:
        c.drawString(ML + prefix_w, y[0], hl)
        y[0] -= 10.2
    setfill(DARK); c.setFont("Lora", 7.8)
    for el in exp_lines:
        c.drawString(ML + prefix_w, y[0], el)
        y[0] -= 10.2
    y[0] -= 5


for quiz in REAL_QUIZZES:
    qn, wk, topic, questions = quiz['quiz_n'], quiz['week'], quiz['topic'], quiz['questions']
    ensure_space(26, f"Answer Key -- Quiz {qn}")
    setfill(QUIZ_ACCENTS.get(qn, NAVY)); c.rect(ML, y[0] - 2, CW, 2.5, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y[0] - 14, f"QUIZ {qn} -- WEEK {wk}: {topic.upper()}")
    y[0] -= 24
    for qd in questions:
        answer_block(qd, f"Answer Key -- Quiz {qn}")

end_page()

# =====================================================================
# PART 2: BONUS -- FULL COVERAGE (Weeks 1, 5, 9)
# =====================================================================
new_page("Part 2 -- Bonus Weeks (No Real Quiz)")
y[0] = H - HEADER_H - 24
section_bar("PART 2 -- BONUS: WEEKS WITH NO REAL QUIZ", accent=TEAL,
            sub="Weeks 1, 5, 9 -- included for complete coverage")
toc_mark("Part 2 -- Bonus Weeks (No Real Quiz)")
para("These three weeks never had a real administered quiz (Week 1 = Day 1 foundations, Week 5 = Midterm "
     "week, Week 9 = pure review per Dr. Zhang). The questions below are extra practice for completeness, "
     "not verbatim final-exam source material like Part 1.", size=8.8, color=GRAY, gap=14)

for wkdata in BONUS_WEEKS:
    wk, topic, questions = wkdata['week'], wkdata['topic'], wkdata['questions']
    ensure_space(60, f"Week {wk} Bonus")
    section_bar(f"WEEK {wk} -- {topic.upper()}", accent=BONUS_ACCENT, sub=f"{len(questions)} questions")
    for qd in questions:
        qtext = f"Q{qd['n']}.  {qd['q']}"
        qlines = wrap_words(qtext, "Lora-Bold", 8.8, CW)
        n_opt = len(qd['opts'])
        opt_h = 12.5
        needed = len(qlines) * 11.5 + n_opt * opt_h + 10
        ensure_space(needed, f"Week {wk} Bonus")
        setfill(DARK); c.setFont("Lora-Bold", 8.8)
        for ql in qlines:
            c.drawString(ML, y[0], ql)
            y[0] -= 11.5
        y[0] -= 1
        letters = ["A", "B", "C", "D"]
        c.setFont("Lora", 8.3)
        for i, opt in enumerate(qd['opts']):
            olines = wrap_words(f"{letters[i]}.  {opt}", "Lora", 8.3, CW - 14)
            setfill(DARK)
            c.drawString(ML + 14, y[0], olines[0])
            y[0] -= opt_h
            for extra in olines[1:]:
                c.drawString(ML + 28, y[0], extra)
                y[0] -= opt_h
        y[0] -= 6

end_page()

# =====================================================================
# ANSWER KEY -- PART 2
# =====================================================================
new_page("Answer Key -- Bonus Weeks")
y[0] = H - HEADER_H - 24
section_bar("ANSWER KEY -- BONUS WEEKS", accent=TEAL, sub="Weeks 1, 5, 9")
toc_mark("Answer Key -- Bonus Weeks")

for wkdata in BONUS_WEEKS:
    wk, topic, questions = wkdata['week'], wkdata['topic'], wkdata['questions']
    ensure_space(26, f"Answer Key -- Week {wk}")
    setfill(BONUS_ACCENT); c.rect(ML, y[0] - 2, CW, 2.5, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y[0] - 14, f"WEEK {wk} -- {topic.upper()}")
    y[0] -= 24
    for qd in questions:
        answer_block(qd, f"Answer Key -- Week {wk}")

end_page()

c.save()
print("SAVED (pre-TOC):", OUT)

# =====================================================================
# TABLE OF CONTENTS
# =====================================================================
import fitz as _fitz

toc_path = OUT.replace(".pdf", "_TOC_TEMP.pdf")
tc = canvas.Canvas(toc_path, pagesize=(W, H))


def _tc_setfill(rgb): tc.setFillColorRGB(*rgb)
def _tc_setstroke(rgb): tc.setStrokeColorRGB(*rgb)


_tc_setfill(PAGE_BG); tc.rect(0, 0, W, H, fill=1, stroke=0)
_tc_setfill(NAVY); tc.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
_tc_setfill(GOLD); tc.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
_tc_setfill((1, 1, 1)); tc.setFont("Lora-Bold", 12)
tc.drawString(ML, H - HEADER_H + 15, "AC300 MASTER QUIZ BANK")
tc.setFont("Lora-Italic", 9.5)
tc.drawRightString(W - ML, H - HEADER_H + 15, "Table of Contents")

ty = H - HEADER_H - 46
_tc_setfill(NAVY); tc.setFont("Lora-Bold", 20)
tc.drawString(ML, ty, "TABLE OF CONTENTS")
ty -= 12
_tc_setstroke(GOLD); tc.setLineWidth(1.6)
tc.line(ML, ty, ML + CW, ty)
ty -= 40

PAGE_OFFSET = 1
for title, pnum, indent in TOC_ENTRIES:
    shown_page = pnum + PAGE_OFFSET
    x = ML + (22 if indent else 0)
    fsize = 13
    _tc_setfill(NAVY); tc.setFont("Lora-Bold", fsize)
    tc.drawString(x, ty, title)
    tc.setFont("Lora", fsize)
    _tc_setfill(GRAY)
    num_str = str(shown_page)
    num_w = pdfmetrics.stringWidth(num_str, "Lora", fsize)
    dot_right = ML + CW - num_w - 4
    title_w = pdfmetrics.stringWidth(title, "Lora-Bold", fsize)
    dot_start = x + title_w + 8
    if dot_right > dot_start:
        tc.setDash(1, 3)
        tc.setLineWidth(0.7)
        _tc_setstroke((0.72, 0.72, 0.72))
        tc.line(dot_start, ty + 3, dot_right, ty + 3)
        tc.setDash()
    _tc_setfill(NAVY)
    tc.drawRightString(ML + CW, ty, num_str)
    ty -= 34

ty -= 16
_tc_setstroke((0.85, 0.85, 0.85)); tc.setLineWidth(0.7)
tc.line(ML, ty, ML + CW, ty)
ty -= 26
_tc_setfill(NAVY); tc.setFont("Lora-Bold", 12)
tc.drawString(ML, ty, "Quiz 1-6 Week Map (confirmed from transcripts)")
ty -= 20
_tc_setfill(DARK); tc.setFont("Lora", 9.5)
for q in REAL_QUIZZES:
    line = f"Quiz {q['quiz_n']}  =  Week {q['week']} ({q['topic']})"
    tc.drawString(ML, ty, line)
    ty -= 15

_tc_setstroke(GOLD); tc.setLineWidth(HAIRLINE * 1.2)
tc.line(ML, 34, W - ML, 34)
_tc_setfill(GRAY); tc.setFont("Lora-Italic", 7.5)
tc.drawCentredString(W / 2, 22, "AC300/AC375 Master Quiz Bank (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  Table of Contents")
tc.save()

main_doc = _fitz.open(OUT)
toc_doc = _fitz.open(toc_path)
main_doc.insert_pdf(toc_doc, start_at=1)
tmp_out = OUT.replace(".pdf", "_WITH_TOC_TEMP.pdf")
main_doc.save(tmp_out)
main_doc.close()
toc_doc.close()
os.remove(toc_path)
os.replace(tmp_out, OUT)
print("SAVED (with TOC):", OUT)
