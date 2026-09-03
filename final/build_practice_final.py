#!/usr/bin/env python3
"""AC300 Practice Final Exam (Weeks 1-9 cumulative) - builds Print + reMarkable, Set 1 or 2.
Usage: python3 build_practice_final.py <print|remarkable> <1|2>
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
SETNUM = sys.argv[2] if len(sys.argv) > 2 else "1"
IS_RM = EDITION == "remarkable"

if SETNUM == "1":
    from final_questions_set1 import SECTIONS, TOTAL_Q
else:
    from final_questions_set2 import SECTIONS, TOTAL_Q

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

METAL = (0.365, 0.408, 0.451)
EARTH = (0.663, 0.478, 0.169)
FIRE = (0.690, 0.204, 0.169)
WATER = (0.176, 0.310, 0.541)
FIREMIN = (0.850, 0.420, 0.380)
WOOD = (0.200, 0.480, 0.270)
EXTRA = (0.380, 0.180, 0.522)

SECTION_ACCENTS = {
    "Week 1": NAVY, "Week 2": METAL, "Week 3": EARTH, "Week 4": FIRE, "Week 5": WATER,
    "Week 6": FIREMIN, "Week 7": EXTRA, "Week 8-9": WOOD, "Week 9": WOOD, "Weeks 1-9": RED,
}

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    COVER_MASTHEAD_H = 86
    HAIRLINE = 1.0
    OUT = f"/mnt/user-data/outputs/AC300_PracticeFinal{SETNUM}_Wk1-9_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    COVER_MASTHEAD_H = 80
    HAIRLINE = 0.5
    OUT = f"/mnt/user-data/outputs/AC300_PracticeFinal{SETNUM}_Wk1-9_Print.pdf"
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


def header(subtitle):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    c.drawString(36, H - HEADER_H + 15, f"AC300 PRACTICE FINAL -- SET {SETNUM}")
    c.setFont("Lora-Italic", 9.5)
    # auto-shrink subtitle if it would collide with the title
    title_w = pdfmetrics.stringWidth(f"AC300 PRACTICE FINAL -- SET {SETNUM}", "Lora-Bold", 12)
    avail = (W - 36) - (36 + title_w) - 10
    sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", 9.5)
    fs = 9.5
    while sw > avail and fs > 6.5:
        fs -= 0.5
        sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    if avail > 40:
        c.setFont("Lora-Italic", fs)
        c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer(page_label):
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(36, 34, W - 36, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Practice Final Set {SETNUM} (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  {page_label}")


def new_page(subtitle):
    page_bg(); header(subtitle)


def end_page(label):
    footer(label); c.showPage(); page_num[0] += 1


# ============= COVER =============
page_bg()
setfill(NAVY); c.rect(0, H - COVER_MASTHEAD_H, W, COVER_MASTHEAD_H, fill=1, stroke=0)
setfill(GOLD)
if IS_RM:
    c.rect(0, H - COVER_MASTHEAD_H, W, 3, fill=1, stroke=0)
    c.rect(0, H - COVER_MASTHEAD_H - 5, W, 2, fill=1, stroke=0)
else:
    c.rect(0, H - COVER_MASTHEAD_H, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 35, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 18, EDLABEL)

bx, by, bs = W / 2 - 34, H - 165, 68
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD); c.rect(bx, by + bs - 8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 7)
c.drawCentredString(W / 2, by + bs - 22, "FINAL")
c.setFont("Lora-Bold", 20)
c.drawCentredString(W / 2, by + 18, "1-9")

c.setFont("Lora-Bold", 26); setfill(NAVY)
c.drawCentredString(W / 2, H - 227, f"PRACTICE FINAL EXAM -- SET {SETNUM}")
c.setFont("Lora-BoldItalic", 12.5); setfill(RED)
c.drawCentredString(W / 2, H - 250, "Channel Theory through Cutaneous Regions -- Cumulative")
c.setFont("Lora", 10.5); setfill(DARK)
c.drawCentredString(W / 2, H - 268, f"{TOTAL_Q} questions  \u00b7  MC / True-False / EXCEPT format  \u00b7  Weeks 1-9  \u00b7  Modeled on Dr. Zhang's Final")

setstroke(GOLD); c.setLineWidth(1)
c.line(W / 2 - 120, H - 282, W / 2 - 40, H - 282)
c.line(W / 2 + 40, H - 282, W / 2 + 120, H - 282)
setfill(GOLD); c.circle(W / 2, H - 282, 2.5, fill=1, stroke=0)

box_w, box_h, gap = 150, 58, 15
total = box_w * 3 + gap * 2
bx0 = (W - total) / 2
by0 = H - 370
labels = [
    ("FORMAT", "Multiple choice", "True/False + EXCEPT", (0.157, 0.302, 0.541)),
    ("COVERAGE", "All 9 weeks", "Cumulative, per Dr. Zhang", (0.380, 0.180, 0.522)),
    ("ANSWER KEY", "Full explanations", f"for all {TOTAL_Q} questions", (0.106, 0.369, 0.353)),
]
for i, (t, l1, l2, col) in enumerate(labels):
    x = bx0 + i * (box_w + gap)
    setfill((0.933, 0.937, 0.949) if not IS_RM else (0.902, 0.878, 0.816))
    c.rect(x, by0, box_w, box_h, fill=1, stroke=0)
    c.setFillColorRGB(*col); c.rect(x, by0 + box_h - 3, box_w, 3, fill=1, stroke=0)
    c.setFont("Lora-Bold", 10)
    c.drawCentredString(x + box_w / 2, by0 + box_h - 20, t)
    c.setFont("Lora-Italic", 8); c.setFillColorRGB(*DARK)
    c.drawCentredString(x + box_w / 2, by0 + box_h - 33, l1)
    c.drawCentredString(x + box_w / 2, by0 + box_h - 45, l2)

setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, by0 - 26, "How to use this")
c.setFont("Lora", 9); setfill(DARK)
howto = [
    "Close the book. No notes, no app - simulate real final-exam conditions.",
    f"Take all {TOTAL_Q} in one sitting. Dr. Zhang's real final is 30 questions, cumulative, closed book.",
    "Score yourself, then re-drill ONLY the categories you missed using the Final Study Guide + Cram Sheet.",
    "Dr. Zhang has confirmed the real final reuses questions from EVERY quiz you've taken (Quiz 1-6) --",
    "re-open each week's Quiz Kit as part of your review, not just this practice set.",
]
yy = by0 - 42
for line in howto:
    c.drawCentredString(W / 2, yy, line)
    yy -= 13

setstroke(GOLD); c.setLineWidth(1)
c.line(50, 70, W - 50, 70)
c.setFont("Lora-Italic", 8.5); setfill(GRAY)
c.drawCentredString(W / 2, 50, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")
c.showPage()
page_num[0] += 1

# ============= QUESTION PAGES =============
ML, MR = 36, 36
CW = W - ML - MR

new_page(f"Questions 1-{TOTAL_Q}  \u00b7  closed book")
y = H - HEADER_H - 22


def ensure_space(needed, subtitle_for_next):
    global y
    if y - needed < 50:
        end_page(f"Page {page_num[0]}")
        new_page(subtitle_for_next)
        y = H - HEADER_H - 22


for sec_title, sec_wk, questions in SECTIONS:
    accent = SECTION_ACCENTS.get(sec_wk, NAVY)
    ensure_space(40, f"{sec_title}  \u00b7  {sec_wk}")
    setfill(accent); c.rect(ML, y - 3, CW, 3, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 11.5)
    c.drawString(ML, y - 18, sec_title)
    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(ML + CW, y - 18, sec_wk)
    y -= 30

    for qd in questions:
        qtext = f"Q{qd['n']}.  " + (
            "[EXCEPT]  " if qd['type'] == 'EXCEPT' else
            "[T/F]  " if qd['type'] == 'TF' else ""
        ) + qd['q']
        qlines = wrap_words(qtext, "Lora-Bold", 9.3, CW)
        n_opt = len(qd['opts'])
        opt_h = 13
        needed = len(qlines) * 12 + n_opt * opt_h + 12
        ensure_space(needed, f"{sec_title}  \u00b7  {sec_wk}")

        setfill(DARK); c.setFont("Lora-Bold", 9.3)
        for ql in qlines:
            c.drawString(ML, y, ql)
            y -= 12
        y -= 2
        letters = ["A", "B", "C", "D"]
        c.setFont("Lora", 8.8)
        for i, opt in enumerate(qd['opts']):
            olines = wrap_words(f"{letters[i]}.  {opt}", "Lora", 8.8, CW - 14)
            setfill(DARK)
            c.drawString(ML + 14, y, olines[0])
            y -= opt_h
            for extra in olines[1:]:
                c.drawString(ML + 28, y, extra)
                y -= opt_h
        y -= 8

if y > 260:
    y -= 10
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, y, ML + CW, y)
    y -= 20
    setfill(NAVY); c.setFont("Lora-Bold", 11)
    c.drawString(ML, y, "SCORING GUIDE")
    y -= 18
    scoring = [
        (f"{round(TOTAL_Q*0.9)}-{TOTAL_Q} correct", "Exam ready. Do a final pass on the Five Shu master table and Exam Traps page."),
        (f"{round(TOTAL_Q*0.75)}-{round(TOTAL_Q*0.9)-1} correct", "Solid. Re-drill the specific weeks you missed (see section headers above)."),
        (f"{round(TOTAL_Q*0.55)}-{round(TOTAL_Q*0.75)-1} correct", "Re-read the Final Cram Sheet and Study Guide before the exam."),
        (f"Below {round(TOTAL_Q*0.55)}", "Full re-study needed - work back through each week's Study Guide in order."),
    ]
    c.setFont("Lora-Bold", 9)
    for label, txt in scoring:
        setfill(RED); c.drawString(ML, y, label)
        setfill(DARK); c.setFont("Lora", 9)
        for line in wrap_words(txt, "Lora", 9, CW - 130):
            c.drawString(ML + 122, y, line)
            y -= 13
        c.setFont("Lora-Bold", 9)
        y -= 3
    y -= 10
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    c.drawString(ML, y, "Note: Dr. Zhang confirmed the real final reuses quiz questions directly -- re-drill every")
    y -= 11
    c.drawString(ML, y, "weekly Quiz Kit (1-6) once more, not just this practice set.")

end_page(f"Page {page_num[0]}")

# ============= ANSWER KEY =============
new_page("Answer Key with Explanations")
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "ANSWER KEY \u2014 FULL EXPLANATIONS")
y -= 8
setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2); c.line(ML, y, ML + 220, y)
y -= 16
setfill(GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(ML, y, "Score yourself first, then read explanations only for questions you missed or guessed on.")
y -= 20

row_toggle = [0]


def answer_block(qd):
    global y
    ans_letter = qd['ans']
    prefix_w = 38
    head_lines = wrap_words(qd['q'], "Lora-Bold", 8.6, CW - prefix_w)
    exp_lines = wrap_words(qd['exp'], "Lora", 8.3, CW - prefix_w)
    total_lines = len(head_lines) + len(exp_lines)
    needed = total_lines * 10.8 + 10
    ensure_space(needed, "Answer Key with Explanations")

    band_h = needed - 4
    if row_toggle[0] % 2 == 0:
        setfill(ROW_TINT)
        c.rect(ML - 4, y - band_h + 8, CW + 8, band_h, fill=1, stroke=0)
    row_toggle[0] += 1

    setfill(NAVY); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML, y, f"Q{qd['n']}")
    setfill(RED)
    c.drawString(ML + 22, y, ans_letter)
    setfill(NAVY)
    for hl in head_lines:
        c.drawString(ML + prefix_w, y, hl)
        y -= 10.8
    setfill(DARK); c.setFont("Lora", 8.3)
    for el in exp_lines:
        c.drawString(ML + prefix_w, y, el)
        y -= 10.8
    y -= 6


for sec_title, sec_wk, questions in SECTIONS:
    ensure_space(24, "Answer Key with Explanations")
    setfill(SECTION_ACCENTS.get(sec_wk, NAVY)); c.rect(ML, y - 2, CW, 2.5, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y - 14, f"{sec_title}  ({sec_wk})")
    y -= 24
    for qd in questions:
        answer_block(qd)

end_page(f"Page {page_num[0]}")

c.save()
print("SAVED:", OUT)
