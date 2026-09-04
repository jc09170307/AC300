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
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

OUT = "/mnt/user-data/outputs/AC300_Motivational_Letter.pdf"
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

setfill((1, 1, 1)); c.rect(0, 0, W, H, fill=1, stroke=0)
setfill(NAVY); c.rect(0, H - 6, W, 6, fill=1, stroke=0)

y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 19)
c.drawString(ML, y, "On Your Way Into This Final")
y -= 26
setstroke(GOLD); c.setLineWidth(1.4)
c.line(ML, y, ML + CW, y)
y -= 28

setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawString(ML, y, "September 2026")
y -= 24

setfill(DARK); c.setFont("Lora", 11)

paragraphs = [
    "Jon,",

    "You know Expectancy-Value Theory better than I ever will, so I won't explain it to you -- I'll just point "
    "at what you've actually built and let you apply your own framework to it, because the evidence is "
    "unusually good.",

    "Expectancy is not a feeling you talk yourself into. It's calibrated from evidence of your own competence, "
    "and you've spent nine weeks generating that evidence directly: a 55-page Study Guide you pushed back on "
    "until it was actually right, a Decoder organized by point category instead of by channel because you "
    "knew that's a different kind of retrieval you'd need, two Practice Finals and a Master Quiz Bank you had "
    "checked and rechecked -- not because you doubted the content, but because you know that verified material "
    "is what makes confidence load-bearing instead of decorative. That's not busywork. That's exactly the kind "
    "of mastery experience your own field identifies as the strongest source of self-efficacy there is. You "
    "didn't hope you'd be ready. You built readiness, piece by piece, and checked each piece.",

    "Value doesn't need manufacturing here either. You're not cramming acupuncture trivia -- you're building "
    "the working knowledge you'll use on actual patients with actual heel pain and actual low back pain, for "
    "the rest of a career you chose on purpose. The utility value is not hypothetical. It's the whole reason "
    "the accuracy mattered enough to you to keep pushing until it was right.",

    "And cost -- the variable everyone underrates -- is lower now than it was in July. Not because the material "
    "got smaller, but because it's organized: you know what's real Quiz 1-6 content and what's supplementary, "
    "you know the six-division logic underneath the twelve channels instead of twelve isolated facts, you have "
    "a Table of Contents so you're never flipping blind at 11pm. Organized effort costs less than the same "
    "effort scattered.",

    "So here's the only prediction worth making: you are exactly as ready as the evidence says you are, and "
    "the evidence is thorough. Walk into Week 10 the same way you built these materials -- checking your work, "
    "trusting what checks out, and not needing anyone's reassurance to know the difference.",

    "You've got this, and you already know why.",
]

for i, para in enumerate(paragraphs):
    font = "Lora-Bold" if i == 0 else "Lora"
    size = 11.5 if i == 0 else 10.6
    lines = wrap_words(para, font, size, CW)
    setfill(DARK); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML, y, ln)
        y -= size * 1.48
    y -= 7

y -= 6
setfill(DARK); c.setFont("Lora", 10.6)
c.drawString(ML, y, "Rooting for you,")
y -= 28
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Claude")

setstroke(GOLD); c.setLineWidth(1)
c.line(ML, 55, W - ML, 55)
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300/AC375 \u00b7 VUIM Summer 2026 \u00b7 Final Exam, Week 10")

c.save()
print("SAVED:", OUT)
