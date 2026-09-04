#!/usr/bin/env python3
import sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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
ROW_TINT = (0.965, 0.967, 0.972)
HEADER_H = 44

OUT = "/mnt/user-data/outputs/AC300_How_To_Use_This_Study_System.pdf"
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
    setfill((1, 1, 1)); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle=""):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    c.drawString(ML, H - HEADER_H + 15, "HOW TO USE THIS STUDY SYSTEM")
    if subtitle:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle[:70])


def footer():
    setstroke(GOLD); c.setLineWidth(0.5)
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


def para(text, size=9.2, color=DARK, font="Lora", gap=8):
    lines = wrap_words(text, font, size, CW)
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
    needed = 46
    ensure_space(needed)
    setfill(ROW_TINT); c.rect(ML, y[0] - needed + 8, CW, needed - 8, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 10, y[0] - 12, name)
    setfill(DARK); c.setFont("Lora", 8.6)
    for i, ln in enumerate(wrap_words(purpose, "Lora", 8.6, CW - 20)):
        c.drawString(ML + 10, y[0] - 25 - i * 10.5, ln)
    setfill(TEAL); c.setFont("Lora-Italic", 8.2)
    c.drawRightString(ML + CW - 10, y[0] - 12, when)
    y[0] -= needed + 4


# =====================================================================
# COVER / INTRO
# =====================================================================
new_page("Overview")
y[0] = H - HEADER_H - 24
section_bar("HOW TO USE THIS STUDY SYSTEM", accent=NAVY, sub="AC300/AC375 -- Final Exam, Week 10")
para("You have six documents now. This page is the seventh -- the one that tells you what order to use them "
     "in and why, so the system works as a system instead of six separate PDFs competing for your attention "
     "the week before the exam.", size=9.4, gap=14)

section_bar("THE LINEUP -- WHAT EACH DOCUMENT IS ACTUALLY FOR", accent=GOLD)
doc_row("Final Study Guide (55 pp)", "Your primary text. Full reference per channel: pathway, functions, "
        "indications, highest-yield points, clinical pearls. Read this to LEARN, not to test yourself.",
        "First pass, every week")
doc_row("Master Special Points Decoder", "Organized by POINT CATEGORY, not by channel -- \u201call 12 Yuan-Source "
        "points\u201d in one place instead of scattered across 12 channel pages. Use when the Study Guide's "
        "organization isn't the retrieval structure you need.", "Cross-reference, ongoing")
doc_row("Final Cram Sheet (5 pp)", "Everything compressed to its densest, fastest-scan form. This is not "
        "where you learn something for the first time -- it's where you confirm you still know it.",
        "Final 48 hours")
doc_row("Master Quiz Bank & Key", "Part 1 = the REAL Quiz 1-6 (36 questions, verified against transcripts). "
        "Part 2 = 264 additional practice questions I wrote, all 9 weeks. Part 1 tells you exactly what's "
        "been tested; Part 2 is volume for reinforcement.", "Retrieval practice, weekly")
doc_row("Practice Final, Set 1 & 2", "Two full closed-book simulations, no week labels, timed conditions. "
        "This is the dress rehearsal, not a study tool -- don't open the answer key until you've finished "
        "the whole thing.", "1-2 full run-throughs, final week")

# =====================================================================
# THE SEQUENCE -- flows continuously from the lineup above
# =====================================================================
ensure_space(160)
section_bar("THE WEEKLY CYCLE -- HOW THE PIECES FIT TOGETHER", accent=RED,
            sub="Adapted from interteaching: prep before exposure, not after")
para("The single highest-leverage change you can make to how you use these documents: answer questions on a "
     "topic BEFORE you read about it, not after. Struggling to retrieve something you haven't learned yet "
     "feels unproductive, but it's exactly what makes the reading that follows stick -- it tells your brain "
     "what to pay attention to.", size=9.2, gap=14)

for step, label, text in [
    ("1", "Prep cold", "Before opening that week's Study Guide section, pull 5-6 questions on the topic from "
     "the Master Quiz Bank (Part 2) and attempt them with nothing open. You will get most of them wrong. "
     "That's the point -- it's not a test, it's priming."),
    ("2", "Read to fill the gaps", "Now read that week's Study Guide section, paying deliberate attention to "
     "whatever you got wrong or guessed on in Step 1. This is what interteaching calls the \u201cclarifying "
     "lecture\u201d -- focused on your actual gaps, not a generic re-read."),
    ("3", "Re-test the same items", "Go back to the exact questions from Step 1. If you're now getting them "
     "right, the material moved from short-term to working knowledge. If not, that's real signal -- log it "
     "(see the Confusion Log idea below) rather than re-reading and hoping."),
    ("4", "Cross-check in the Decoder", "For any special-point category that gave you trouble (Yuan-Source, "
     "Luo, Xi-Cleft, etc.), look it up in the Decoder's category view. Seeing all 12 channels' version of the "
     "same point-type side by side often resolves confusion that channel-by-channel reading doesn't."),
]:
    ensure_space(70)
    setfill(RED); c.circle(ML + 10, y[0] - 4, 9, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawCentredString(ML + 10, y[0] - 7.5, step)
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 26, y[0] - 4, label)
    y[0] -= 18
    for ln in wrap_words(text, "Lora", 8.9, CW - 26):
        setfill(DARK); c.setFont("Lora", 8.9)
        c.drawString(ML + 26, y[0], ln)
        y[0] -= 12.5
    y[0] -= 10

section_bar("BUILT-IN, NO NEW FILE NEEDED", accent=TEAL)
bullet("Confusion Log", "Keep a single running note (paper, notes app, whatever) of specific items you get "
       "wrong across Steps 1 and 3, week over week. By Week 9 this becomes your single most efficient "
       "review document -- shorter than any of the six PDFs, and it's entirely YOUR gaps, not a generic list.",
       accent=TEAL)
bullet("Utility-value check", "Once a week, in one sentence: why does this week's material actually matter "
       "for the practitioner you're becoming, beyond the exam? You know the research on this better than "
       "anyone -- the point is that YOU write the connection, not that I tell you one.", accent=TEAL)

# =====================================================================
# FINAL TWO WEEKS -- flows continuously from the cycle above
# =====================================================================
ensure_space(160)
section_bar("THE FINAL TWO WEEKS -- SHIFTING FROM LEARNING TO CONFIRMING", accent=GOLD,
            sub="Week 9 review -> Week 10 final")
para("By Week 9, the goal changes. You're not learning new material (Dr. Zhang confirmed Week 9 is 100% "
     "review) -- you're confirming what's solid and triaging what isn't. Don't keep reading the Study Guide "
     "cover to cover; that's Weeks 1-8 behavior applied to a week where it's the wrong tool.", size=9.2, gap=14)

for label, text in [
    ("Run Practice Final Set 1", "Full closed-book, timed, no peeking. Score it. Do NOT read explanations yet "
     "for anything you got right -- only for misses and guesses."),
    ("Work the Confusion Log", "Whatever's accumulated there all course is now your primary study document. "
     "It's already filtered to exactly what you don't know."),
    ("Run Practice Final Set 2", "48-72 hours later, same closed-book conditions. Compare to Set 1 -- new "
     "misses here are your highest-priority items for the final 48 hours."),
    ("Cram Sheet, cover to cover", "One full pass, out loud if that helps retrieval. This is confirmation, "
     "not first exposure -- if something here surprises you, that's a flag to go back to the Study Guide "
     "entry, not just re-read the Cram Sheet line."),
    ("Quiz Bank Part 1 only", "The 36 real questions, one last time. This is verbatim-sourced content -- if "
     "you get every one of these right, you've covered the highest-confidence-of-recurrence material there is."),
]:
    bullet(label, text, accent=GOLD, size=8.9)

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
