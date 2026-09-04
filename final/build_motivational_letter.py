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
c.drawString(ML, y, "Five Days Out")
y -= 26
setstroke(GOLD); c.setLineWidth(1.4)
c.line(ML, y, ML + CW, y)
y -= 28

setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawString(ML, y, "September 2026  \u00b7  To the AC300/AC375 Class")
y -= 24

setfill(DARK); c.setFont("Lora", 11)

paragraphs = [
    "To everyone finishing up AC300/AC375,",

    "Jon asked me to write this to the class instead of just to him, and I think that's the right call -- "
    "none of you are walking into Wednesday's final with less preparation behind you than the material in "
    "front of you suggests.",

    "Here's the actual argument, not just encouragement: confidence going into an exam should be calibrated "
    "from evidence, not talked into existence. And the evidence for this course is unusually good. Nine "
    "weeks of channel pathways, point categories, extraordinary vessels, and Five Shu points -- reviewed, "
    "quizzed, and reviewed again, culminating in a review week Dr. Zhang built specifically to consolidate "
    "all of it before Wednesday. That's not hope. That's a body of work you can point to.",

    "The material itself is not designed to trick you. Dr. Zhang has said directly that the final draws from "
    "the same quizzes you've already taken -- not new questions written to catch you off guard. That means "
    "the gap between now and Wednesday isn't about learning something new. It's about confirming what you "
    "already know and tightening the handful of things that still feel shaky. That's a much smaller, much "
    "more manageable task than it feels like five days out.",

    "So: sleep before the exam matters more than one more late read-through. Confirming what you know is "
    "worth more than re-learning what you already know. And whatever you use these last five days for, "
    "trust what you've already built more than the anxiety telling you it isn't enough. The anxiety is not "
    "evidence. The nine weeks are.",

    "Good luck Wednesday, all of you.",
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
c.drawString(ML, y, "Rooting for all of you,")
y -= 28
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Claude")

setstroke(GOLD); c.setLineWidth(1)
c.line(ML, 55, W - ML, 55)
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300/AC375 \u00b7 VUIM Summer 2026 \u00b7 Final Exam, Wednesday 9/9, 9:00 AM")

c.save()
print("SAVED:", OUT)
