#!/usr/bin/env python3
"""AC300 Week 6 Quiz Kit -- PC, SJ, GB, LR. 30-question standalone practice
exam. Rebuilt to match the ACTUAL Week 5 Quiz Kit PDF geometry exactly
(verified via PyMuPDF inspection, not guessed from an older script)."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, "/home/claude/work")
from wk6_quiz_questions import QUESTIONS

FONT_DIR = "/home/claude/work/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.176, 0.271, 0.412)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.12, 0.12, 0.12)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.945, 0.937, 0.906)
MINT = (0.938, 0.960, 0.958)
LGRAY = (0.950, 0.947, 0.963)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_Week6_QuizKit_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week6_QuizKit_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = wd
    if cur: lines.append(cur)
    return lines


ML, MR = 42, 42
RX = W - MR
CW = RX - ML
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def top_bar():
    setfill(DARK); c.setFont("Lora", 8.5)
    c.drawString(ML, H - 30.3, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(RX, H - 30.3, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6 * LW_MULT)
    c.line(ML, H - 38, RX, H - 38)


def bottom_bar(label):
    setfill(NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora", 8)
    c.drawString(ML, 10, label)
    c.drawRightString(RX, 10, f"p.{page_num[0]}")


def new_page():
    page_bg(); top_bar()


def end_page(label):
    bottom_bar(label); c.showPage(); page_num[0] += 1


WEEK_LABEL = "AC300/AC375 | Week 6 | PC, SJ, GB, LR Channels | VUIM Summer 2026"


def title_bar(title, subtitle_right):
    bar_top = H - 46
    bar_bot = H - 74
    setfill(NAVY); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 15)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot - 10


def question_card(y, num, question, options, tint):
    lines_q = wrap_words(question, "Lora-Bold", 9.6, CW - 40)
    col_w = CW / 2 - 40
    opt_lines = [wrap_words(opt, "Lora", 8.8, col_w) for opt in options]
    opt_pairs = [(opt_lines[0], opt_lines[1]), (opt_lines[2], opt_lines[3])]
    row_heights = [max(len(l), len(r)) * 11 for l, r in opt_pairs]
    card_h = 18 + len(lines_q) * 12.2 + sum(row_heights) + 8
    setfill(tint); c.rect(ML, y - card_h, CW, card_h, fill=1, stroke=0)
    setfill(NAVY); c.rect(ML + 4, y - 22, 18, 18, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawCentredString(ML + 13, y - 17.5, str(num))
    qy = y - 14
    tx = ML + 32
    setfill(DARK); c.setFont("Lora-Bold", 9.6)
    for l in lines_q:
        c.drawString(tx, qy, l); qy -= 12.2
    qy -= 3
    letters = ["A.", "B.", "C.", "D."]
    col2_x = ML + CW / 2 + 10
    for i, (left_lines, right_lines) in enumerate(opt_pairs):
        li = i * 2
        row_top = qy
        setfill(GOLD); c.setFont("Lora-Bold", 8.6)
        c.drawString(tx, row_top, letters[li])
        setfill(DARK); c.setFont("Lora", 8.8)
        for j, l in enumerate(left_lines):
            c.drawString(tx + 16, row_top - j * 11, l)
        setfill(GOLD); c.setFont("Lora-Bold", 8.6)
        c.drawString(col2_x, row_top, letters[li + 1])
        setfill(DARK); c.setFont("Lora", 8.8)
        for j, l in enumerate(right_lines):
            c.drawString(col2_x + 16, row_top - j * 11, l)
        qy -= row_heights[i]
    return y - card_h - 6


def measure_card_h(q, options=None):
    lines_q = wrap_words(q, "Lora-Bold", 9.6, CW - 40)
    if options is None:
        return 18 + len(lines_q) * 12.2 + 2 * 13.5 + 8
    col_w = CW / 2 - 40
    opt_lines = [wrap_words(opt, "Lora", 8.8, col_w) for opt in options]
    opt_pairs = [(opt_lines[0], opt_lines[1]), (opt_lines[2], opt_lines[3])]
    row_heights = [max(len(l), len(r)) * 11 for l, r in opt_pairs]
    return 18 + len(lines_q) * 12.2 + sum(row_heights) + 8


def paginate_questions(questions_all):
    """Pre-computes page groupings so titles can show accurate ranges."""
    groups = []
    idx = 0
    avail_start = (H - 74) - 10  # y right after title bar
    while idx < len(questions_all):
        y = avail_start
        start = idx
        while idx < len(questions_all):
            card_h = measure_card_h(questions_all[idx][0], questions_all[idx][1])
            if y - card_h < 55:
                break
            y -= card_h + 6
            idx += 1
        if idx == start:
            idx += 1  # safety: always advance
        groups.append((start, idx))
    return groups


def render_question_group(start, end, questions_all, subtitle_fn, tint_a, tint_b):
    new_page()
    y = title_bar(f"Week 6 Practice Quiz  -  Questions {start+1}-{end} (of 30)", subtitle_fn(start))
    for i in range(start, end):
        q, opts, ans, expl = questions_all[i]
        tint = tint_a if (i - start) % 2 == 0 else tint_b
        y = question_card(y, i + 1, q, opts, tint)
    end_page(WEEK_LABEL)


def answer_row(y, num, ans, question, expl):
    q_lines = wrap_words(question, "Lora-Bold", 9, CW - 60)
    lines_e = wrap_words(expl, "Lora-Italic", 8, CW - 60)
    row_h = 13 + (len(q_lines) - 1) * 11.5 + 12 + len(lines_e) * 10.4
    tint = MINT if num % 2 else (1, 1, 1)
    setfill(tint); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9)
    c.drawString(ML + 4, y - 12, str(num))
    setfill((0.62, 0.22, 0.18)); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 26, y - 12, ans)
    setfill(DARK); c.setFont("Lora-Bold", 9)
    qy = y - 12
    for l in q_lines:
        c.drawString(ML + 46, qy, l); qy -= 11.5
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    qy -= 1
    for l in lines_e:
        c.drawString(ML + 46, qy, l); qy -= 10.4
    return y - row_h - 2


def measure_answer_row_h(question, expl):
    q_lines = wrap_words(question, "Lora-Bold", 9, CW - 60)
    lines_e = wrap_words(expl, "Lora-Italic", 8, CW - 60)
    return 13 + (len(q_lines) - 1) * 11.5 + 12 + len(lines_e) * 10.4 + 2


def answer_key_page(title, qslice, start_num):
    new_page()
    y = title_bar(title, None)
    for i, (q, opts, ans, expl) in enumerate(qslice):
        num = start_num + i
        row_h_est = measure_answer_row_h(q, expl)
        if y - row_h_est < 55:
            end_page(WEEK_LABEL)
            new_page()
            y = title_bar(title + " (continued)", None)
        y = answer_row(y, num, ans, q, expl)
    end_page(WEEK_LABEL)


# ============================================================
# COVER (matches Week 5 spec exactly)
# ============================================================
new_page()
y = H - 60
setfill(GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "WEEK 6")
c.setFont("Lora-Italic", 10)
c.drawRightString(RX, y, EDLABEL)
y -= 40
setfill(NAVY); c.setFont("Lora-Bold", 28)
c.drawString(ML, y, "Week 6 Quiz Kit")
y -= 28
setfill((0.176, 0.412, 0.373)); c.setFont("Lora-Bold", 17)
c.drawString(ML, y, "Pericardium, San Jiao, Gallbladder & Liver Channels")
y -= 22
setfill(GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "Standalone practice quiz -- pairs with the Week 6 Study Guide")
y -= 18
setstroke(GOLD); c.setLineWidth(1.2)
c.line(ML, y, RX, y)
y -= 28
setfill((0.176, 0.412, 0.373)); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Kit Covers:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.5)
bullets = [
    "30-Question MCQ Quiz -- 7 PC, 8 SJ, 8 GB, 7 LR",
    "Covers pathway branches, crossing points, special points, and exam traps",
    "Includes the Middle Circuit milestone (PC+SJ+GB+LR complete all 3 circuits)",
    "Full Answer Key with explanations for every question",
]
for b in bullets:
    setfill(GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(DARK)
    for i, l in enumerate(wrap_words(b, "Lora", 10.5, CW - 20)):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(wrap_words(b, "Lora", 10.5, CW - 20)))
    y -= 4

y -= 10
box_h = 60
setfill(CREAM); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 16, y - 18, "QUIZ 5 (next class) covers: PC, SJ, GB & LR channels.")
c.drawString(ML + 16, y - 32, "Study first from the Week 6 Study Guide, then self-test here before class.")
c.drawString(ML + 16, y - 46, "Answer key begins after the final question block -- no peeking until you've answered!")
y -= box_h + 40

setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
end_page(WEEK_LABEL)

# ============================================================
# QUESTION PAGES -- dynamically paginated to prevent overflow
# ============================================================
def subtitle_for(idx):
    if idx < 7:
        return "Covers PC & SJ"
    elif idx < 15:
        return "Covers SJ & GB"
    elif idx < 23:
        return "Covers GB"
    else:
        return "Covers LR"

groups = paginate_questions(QUESTIONS)
for start, end in groups:
    render_question_group(start, end, QUESTIONS, subtitle_for, MINT, LGRAY)

# ============================================================
# ANSWER KEY -- dense list, matches Wk5 exactly
# ============================================================
answer_key_page("Week 6 Quiz - Answer Key (All 30 Questions)", QUESTIONS, 1)

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
