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
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Exam_Day_Card_reMarkable.pdf"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HAIRLINE = 0.6
    OUT = "/mnt/user-data/outputs/AC300_Exam_Day_Card_Print.pdf"

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


ML, MR = 40, 40
CW = W - ML - MR

setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)
setfill(NAVY); c.rect(0, H - 64, W, 64, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 64, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 18)
c.drawCentredString(W / 2, H - 40, "EXAM DAY")
c.setFont("Lora-Italic", 10.5)
c.drawCentredString(W / 2, H - 56, "AC300/AC375 Final  \u00b7  Wednesday, September 9  \u00b7  9:00 AM")

y = H - 100

# ---- logistics box ----
box_h = 46
setfill(ROW_TINT); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(GOLD); c.rect(ML, y - box_h, 3, box_h, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML + 14, y - 18, "Before you leave the house:")
setfill(DARK); c.setFont("Lora", 9.3)
for i, ln in enumerate([
    "Confirm room/location and arrival time from the syllabus or Dr. Zhang's email -- don't guess.",
    "ID, pencil/pen, water. Nothing else needed -- you already did the studying part.",
]):
    c.drawString(ML + 14, y - 32 - i * 12, ln)
y -= box_h + 22

# ---- if you blank ----
setfill(RED); c.rect(ML, y - 2, CW, 2.5, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 12.5)
c.drawString(ML, y - 16, "IF YOU BLANK, REMEMBER THESE")
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawRightString(ML + CW, y - 16, "the most commonly mixed-up facts in the course")
y -= 30

traps = [
    ("ST truly begins at LI20, not ST1", "ST1 Chengqi is just the first NUMBERED point -- the pathway "
     "origin is LI20 Yingxiang on the face, a crossing point of the LI channel."),
    ("Heel pain -> think Kidney first", "KI's pathway curves directly behind the medial malleolus and "
     "through the heel -- Dr. Zhang's own explicit clinical teaching point."),
    ("BL's two back lines run SIMULTANEOUSLY", "Not a sequential up-down loop. Both the 1.5-cun and "
     "3-cun parallel lines run at the same time -- confirmed directly in Q&A."),
    ("HT and PC are the ONLY 2 channels with zero crossing points", "A classic easy paired exam trap."),
    ("Yuan-Source rule flips by polarity", "YIN channels: Yuan-Source = the Shu-Stream point (dual role, "
     "same point). YANG channels: Yuan-Source is a separate 6th point beyond the 5 Shu points."),
    ("Forbidden-in-pregnancy points", "LI4 Hegu, SP6 Sanyinjiao, BL60 Kunlun (promotes labor), BL67 "
     "Zhiyin (malposition correction via MOXA only -- needle contraindicated)."),
]

for label, text in traps:
    llines = wrap_words(label, "Lora-Bold", 9.6, CW - 14)
    tlines = wrap_words(text, "Lora", 8.7, CW - 14)
    needed = len(llines) * 12 + len(tlines) * 10.8 + 8
    setfill(RED); c.rect(ML, y - needed + 6, 2.5, needed - 6, fill=1, stroke=0)
    yy = y
    setfill(NAVY); c.setFont("Lora-Bold", 9.6)
    for ln in llines:
        c.drawString(ML + 12, yy, ln); yy -= 12
    setfill(DARK); c.setFont("Lora", 8.7)
    for ln in tlines:
        c.drawString(ML + 12, yy, ln); yy -= 10.8
    y -= needed + 8

y -= 6
setstroke((0.85, 0.85, 0.85)); c.setLineWidth(HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 26

setfill(TEAL); c.setFont("Lora-Bold", 11)
c.drawCentredString(W / 2, y, "You've done the work. This is just the day you show it.")
y -= 16
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, y, "Breathe. Read each question once before answering. Trust your first read.")

setstroke(GOLD); c.setLineWidth(HAIRLINE)
c.line(ML, 40, W - ML, 40)
setfill(GRAY); c.setFont("Lora-Italic", 7.5)
c.drawCentredString(W / 2, 26, "AC300/AC375 Exam Day Card  \u00b7  VUIM Summer 2026")

c.save()
print("SAVED:", OUT)
