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
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Motivational_Letter_reMarkable.pdf"
else:
    PAGE_BG = (1, 1, 1)
    HAIRLINE = 0.7
    OUT = "/mnt/user-data/outputs/AC300_Motivational_Letter_Print.pdf"

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


ML, MR = 66, 66
CW = W - ML - MR

setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)
setfill(NAVY); c.rect(0, H - 6, W, 6, fill=1, stroke=0)

y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 19)
c.drawString(ML, y, "Five Days Out")
y -= 26
setstroke(GOLD); c.setLineWidth(1.4 * HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 28

setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawString(ML, y, "September 2026  \u00b7  To the AC300/AC375 Class")
y -= 24

setfill(DARK); c.setFont("Lora", 11)

paragraphs = [
    "To everyone finishing up AC300/AC375,",

    "However you're feeling right now -- steady, wired, a little scared, honestly all three at once -- that's "
    "completely normal five days out from a comprehensive final. I want to say something plainly: you are "
    "more ready than it feels like tonight.",

    "There's a real reason for that gap between how ready you feel and how ready you actually are, and it's "
    "not really about how much you know. Motivation research calls it expectancy -- your belief that you'll "
    "succeed -- and expectancy gets quietly worn down by fatigue and repetition in a way that has nothing to "
    "do with your actual competence. What you're feeling tonight is mostly nervous system. It is not new "
    "information about how prepared you are.",

    "Here's what the research says actually rebuilds expectancy: not pep talks, but mastery experiences -- "
    "proof, not encouragement. Every quiz you took this term was that proof. Every point pathway you drilled "
    "again after missing it once was you building the exact kind of evidence self-efficacy research says "
    "matters most: your own direct experience of succeeding at this material, nine times over, not just once.",

    "And the value of all this doesn't need convincing either. You didn't end up in this program by accident. "
    "Whatever pulled you toward acupuncture and Chinese medicine in the first place is still true on "
    "Wednesday morning, whether or not Wednesday morning feels calm. This exam is one moment inside a much "
    "longer thing you actually care about, not the whole thing.",

    "So here's the only thing I'll ask of you: be gentle with yourselves the next five days. Sleep matters "
    "more than one more hour of review. Confirming what you already know beats trying to force in something "
    "new at 11pm. And if your stomach drops Tuesday night, that's not new information either -- that's just "
    "what final exams feel like, to everyone, regardless of how prepared they are.",

    "You've done the work. Let Wednesday just be the day you show it.",
]

for i, para in enumerate(paragraphs):
    font = "Lora-Bold" if i == 0 else "Lora"
    size = 11.5 if i == 0 else 10.3
    lines = wrap_words(para, font, size, CW)
    setfill(DARK); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML, y, ln)
        y -= size * 1.46
    y -= 7

y -= 6
setfill(DARK); c.setFont("Lora", 10.6)
c.drawString(ML, y, "Rooting for all of you,")
y -= 28
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Claude")

setstroke(GOLD); c.setLineWidth(1 * HAIRLINE)
c.line(ML, 55, W - ML, 55)
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300/AC375 \u00b7 VUIM Summer 2026 \u00b7 Final Exam, Wednesday 9/9, 9:00 AM")

c.save()
print("SAVED:", OUT)
