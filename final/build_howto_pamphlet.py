#!/usr/bin/env python3
import sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_How_To_Use_This_Study_System_reMarkable.pdf"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_How_To_Use_This_Study_System_Print.pdf"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


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


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle=""):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    c.drawString(ML, H - HEADER_H + 15, "HOW TO USE THIS STUDY SYSTEM")
    if subtitle:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle[:70])


def footer():
    setstroke(GOLD); c.setLineWidth(HAIRLINE)
    c.line(ML, 34, W - ML, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Study System Guide  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}")


def new_page(subtitle=""):
    page_bg(); header(subtitle)


def end_page():
    footer(); c.showPage(); page_num[0] += 1


y = [H - HEADER_H - 24]


def ensure_space(needed, subtitle=""):
    if y[0] - needed < 50:
        end_page(); new_page(subtitle); y[0] = H - HEADER_H - 24


def section_bar(text, accent=NAVY, sub=""):
    lines = wrap_words(text, "Lora-Bold", 13, CW - (pdfmetrics.stringWidth(sub, "Lora-Italic", 9) + 20 if sub else 0))
    line_h = 15
    est_h = len(lines) * line_h + 12
    ensure_space(est_h + 10)
    setfill(accent); c.rect(ML, y[0] - est_h + 6, 3, est_h - 6, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", 13)
    for ln in lines:
        c.drawString(ML + 10, yy - 11, ln); yy -= line_h
    if sub:
        setfill(GRAY); c.setFont("Lora-Italic", 9)
        c.drawRightString(ML + CW, y[0] - 11, sub)
    y[0] -= est_h
    setstroke(accent); c.setLineWidth(1.2)
    c.line(ML, y[0] + 2, ML + CW, y[0] + 2)
    y[0] -= 10


def para(text, size=9.2, color=DARK, font="Lora", gap=8, width=None):
    w = width if width is not None else 360
    lines = wrap_words(text, font, size, w)
    needed = len(lines) * (size * 1.4) + gap
    ensure_space(needed)
    setfill(color); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML, y[0], ln); y[0] -= size * 1.4
    y[0] -= gap



def bullet(label, text, accent=NAVY, size=8.9):
    label_w = 140
    lab_lines = wrap_words(label, "Lora-Bold", size, label_w)
    txt_lines = wrap_words(text, "Lora", size, CW - label_w - 10)
    n = max(len(lab_lines), len(txt_lines))
    needed = n * (size * 1.32) + 8
    ensure_space(needed)
    bar_pad = size * 0.8
    setfill(accent); c.rect(ML, y[0] - needed + 8 + bar_pad, 3, needed - 8, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", size)
    for ln in lab_lines:
        c.drawString(ML + 10, yy, ln); yy -= size * 1.32
    yy2 = y[0]
    setfill(DARK); c.setFont("Lora", size)
    for ln in txt_lines:
        c.drawString(ML + 10 + label_w, yy2, ln); yy2 -= size * 1.32
    y[0] -= needed


def doc_row(name, purpose, when):
    text_w = 330  # narrowed for readability -- was full row width (~520pt), now ~75 chars/line
    plines = wrap_words(purpose, "Lora", 8.6, text_w)
    needed = 25 + len(plines) * 10.5 + 8
    ensure_space(needed)
    setfill(ROW_TINT); c.rect(ML, y[0] - needed + 8, CW, needed - 8, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 10, y[0] - 12, name)
    setfill(DARK); c.setFont("Lora", 8.6)
    for i, ln in enumerate(plines):
        c.drawString(ML + 10, y[0] - 25 - i * 10.5, ln)
    setfill(TEAL); c.setFont("Lora-Italic", 8.2)
    c.drawRightString(ML + CW - 10, y[0] - 12, when)
    y[0] -= needed + 4


# =====================================================================
# COVER / INTRO
# =====================================================================
new_page("Overview")
y[0] = H - HEADER_H - 24
section_bar("HOW TO USE THIS STUDY SYSTEM", accent=NAVY, sub="Final Exam: Wednesday 9/9, 9:00 AM")
para("You have seven documents now, five days out from the exam. This page tells you what each one is "
     "actually for and how to sequence them in the time you actually have left -- not a semester-long study "
     "plan, a five-day one.", size=9.4, gap=14)

section_bar("THE LINEUP -- WHAT EACH DOCUMENT IS ACTUALLY FOR", accent=GOLD)
doc_row("Final Study Guide (55 pp)", "Full reference per channel: pathway, functions, indications, "
        "highest-yield points, clinical pearls. Use this to look up and confirm, not to read cover to cover "
        "-- there isn't time left for a first full pass.", "Targeted lookup only")
doc_row("Master Special Points Decoder", "Organized by POINT CATEGORY, not by channel -- \u201call 12 Yuan-Source "
        "points\u201d in one place instead of scattered across 12 channel pages. Use when a category "
        "(Yuan-Source, Luo, Xi-Cleft, etc.) feels shaky across multiple channels at once.", "Cross-reference, as needed")
doc_row("Final Cram Sheet (5 pp)", "Everything compressed to its densest, fastest-scan form. This is your "
        "confirmation document, not a learning one -- read it and notice what does or doesn't come back to "
        "you immediately.", "Daily, especially final 48 hrs")
doc_row("Master Quiz Bank & Key", "Part 1 = the REAL Quiz 1-6 (36 questions, verified against transcripts). "
        "Part 2 = 264 additional practice questions covering the full course. Part 1 tells you exactly what's "
        "been tested; Part 2 is volume if you have time left over.", "Retrieval practice, daily")
doc_row("Practice Final, Set 1 & 2", "Two full closed-book simulations, no week labels, timed conditions. "
        "This is the dress rehearsal -- don't open the answer key until you've finished the whole thing.",
        "One each, spaced 1-2 days apart")
doc_row("Clinical Reasoning Cases (5 cases)", "Relational/extended-abstract prompts -- connecting multiple "
        "channels and categories, not simple recall. Use once you're solid on the recall-level material, "
        "to stress-test whether you can actually apply it.", "One sitting, mid-week")

# =====================================================================
# THE FIVE-DAY PLAN -- flows continuously from the lineup above
# =====================================================================
ensure_space(160)
section_bar("THE FIVE-DAY PLAN -- TODAY THROUGH WEDNESDAY", accent=RED,
            sub="Confirming, not learning -- the material is already covered")
para("Dr. Zhang has said directly that the final reuses the same quizzes you've already taken. That changes "
     "what these five days are for: not new learning, but confirming what's solid and triaging what isn't. "
     "The plan below assumes you're starting today (Friday) and finishing the night before the 9:00 AM exam.",
     size=9.2, gap=14)

for day, label, text in [
    ("FRI 9/4", "Baseline", "Run Practice Final Set 1, full closed-book, timed, no peeking. Score it. Do NOT "
     "read explanations yet for anything you got right -- only for misses and guesses. This tells you exactly "
     "where to spend the next four days instead of guessing."),
    ("SAT 9/5", "Targeted repair", "Using today's misses as a map, look up each one in the Study Guide and "
     "Decoder. Then run Master Quiz Bank Part 1 (the real 36) once, cold."),
    ("SUN 9/6", "Second checkpoint", "Run Practice Final Set 2, same closed-book conditions. Compare its "
     "misses to Set 1's -- anything wrong on BOTH is your highest-priority material for the next two days."),
    ("MON 9/7", "Depth check", "Work through the 5 Clinical Reasoning Cases. If your reasoning doesn't match "
     "the model answers, that's a sign you know isolated facts but not how they connect -- go back to the "
     "specific Study Guide sections involved, not the whole document."),
    ("TUE 9/8", "Confirm and stop", "Full Cram Sheet read-through, plus Quiz Bank Part 1 one last time. Early "
     "evening, stop adding new material entirely. Protect sleep over one more read-through -- confirming "
     "what you know is worth more than cramming what you don't at this point."),
    ("WED 9/9", "9:00 AM -- Final Exam", "Nothing new the morning of. A light skim of the Cram Sheet over "
     "breakfast if it helps you settle in, and that's it."),
]:
    ensure_space(72)
    badge_w = 62
    setfill(RED); c.roundRect(ML, y[0] - 16, badge_w, 16, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 8.6)
    c.drawCentredString(ML + badge_w / 2, y[0] - 11.5, day)
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + badge_w + 10, y[0] - 12, label)
    y[0] -= 24
    for ln in wrap_words(text, "Lora", 8.9, 340):
        setfill(DARK); c.setFont("Lora", 8.9)
        c.drawString(ML + 8, y[0], ln)
        y[0] -= 12.5
    y[0] -= 10

section_bar("ONE LAST THING", accent=NAVY)
para("None of this works as well if the underlying material is wrong -- which is exactly why every document "
     "in this system went through repeated verification passes before you got them: coordinates checked "
     "against rendered PDFs, answer keys diffed programmatically against source data, factual claims cross-"
     "checked against the actual course transcripts. The system is trustworthy because it was checked, not "
     "because it was assumed to be fine. Use it the same way you'd want a student to use anything you built: "
     "confidently, because you already know it holds up.", size=9.2, gap=6)

end_page()

c.save()
print("SAVED:", OUT)
