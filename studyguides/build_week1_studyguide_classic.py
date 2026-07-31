#!/usr/bin/env python3
"""AC300 Week 1 Study Guide - Channel Theory. Builds BOTH Print and reMarkable editions."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from week1_content import (TWELVE_MERIDIANS, ZANG_ORGANS, FU_ORGANS, CIRCUITS, DIRECTION_RULES,
                            MEETING_POINTS, MERIDIAN_CLOCK, FUNCTIONS_OF_MERIDIANS, NOMENCLATURE,
                            CHANNELS_VS_MERIDIANS, CLINICAL_PEARLS_WK1, QUIZ1_FUNDAMENTALS)

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

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902); ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51; HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Week1_StudyGuide_Classic_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1); ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44; HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Week1_StudyGuide_Classic_Print.pdf"
    EDLABEL = "Print Edition"

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
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]
row_num = [0]

F_BODY = 10.0; F_BODY_LH = 13.0
F_TABLE = 9.3; F_TABLE_LH = 12.0
F_SMALL = 8.6; F_SMALL_LH = 11.0


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 11)
    c.drawString(36, H - HEADER_H + 15, "AC300/AC375  |  Week 1  |  Channel Theory  |  VUIM Summer 2026")
    c.setFont("Lora-Italic", 9)
    c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer():
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, 34, W - MR, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Week 1 Study Guide  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}  \u00b7  {EDLABEL}")


def new_page(subtitle):
    page_bg(); header(subtitle)


def end_page():
    footer(); c.showPage(); page_num[0] += 1


def section_rule(y, title, width=240, size=12.5):
    setfill(NAVY); c.setFont("Lora-Bold", size)
    c.drawString(ML, y, title)
    y -= 5
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, y, ML + width, y)
    return y - 16


def para(y, text, font="Lora", size=F_BODY, lh=F_BODY_LH, color=DARK, width=None):
    setfill(color); c.setFont(font, size)
    for l in wrap_words(text, font, size, width or CW - 4):
        c.drawString(ML, y, l); y -= lh
    return y


# ============= PAGE 1: COVER =============
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 80, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - 45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 62, EDLABEL)

bx, by, bs = W / 2 - 34, H - 165, 68
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD); c.rect(bx, by + bs - 8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 8)
c.drawCentredString(W / 2, by + bs - 24, "WEEK")
c.setFont("Lora-Bold", 26)
c.drawCentredString(W / 2, by + 16, "1")

c.setFont("Lora-Bold", 26); setfill(NAVY)
c.drawCentredString(W / 2, H - 227, "Week 1 Study Guide")
c.setFont("Lora-BoldItalic", 14); setfill(RED)
c.drawCentredString(W / 2, H - 252, "Channel Theory: Concept, Nomenclature, Flow of Qi")
c.setFont("Lora", 11); setfill(DARK)
c.drawCentredString(W / 2, H - 270, "12 Meridians  \u00b7  3 Circuits  \u00b7  Foundational Theory")

y = H - 310
setfill(NAVY); c.setFont("Lora-Bold", 11.5)
c.drawCentredString(W / 2, y, "This Document Contains:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.5)
for b in [
    "What a channel is, and how it differs from a meridian and a collateral",
    "Zang-Fu organ theory and the 12 Primary Meridians' full nomenclature",
    "The Three Circuits (Outer/Anterior, Inner/Posterior, Middle) in full detail",
    "Direction of Qi flow and exactly where paired meridians meet",
    "The full 24-hour Meridian Clock and its clinical application",
    "Dr. Zhang's Clinical Pearls + Quiz 1 Fundamentals",
]:
    c.drawCentredString(W / 2, y, b)
    y -= 15

y -= 16
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
box_w = 480
c.rect(W / 2 - box_w / 2, y - 62, box_w, 62, fill=1, stroke=0)
setfill(RED); c.setFont("Lora-Bold", 10)
c.drawCentredString(W / 2, y - 19, "QUIZ 1 covers: Channel Theory (this week's material)")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawCentredString(W / 2, y - 35, "This is the foundation every later week builds on directly")
c.drawCentredString(W / 2, y - 50, "No channel-specific points yet - LU/LI begin next week")

y -= 92
setstroke(GOLD); c.setLineWidth(1)
c.line(50, y, W - 50, y)
y -= 22
c.setFont("Lora-Italic", 9); setfill(GRAY)
c.drawCentredString(W / 2, y, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's Week 1 lecture, VUIM Summer 2026")

end_page()

# ============= PAGE 2: WHAT IS A CHANNEL =============
new_page(f"What Is a Channel?  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Channels, Meridians, and Collaterals")
y = para(y, CHANNELS_VS_MERIDIANS['definition'])
y -= 10
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "The Full Channel System")
y -= 16
setfill(DARK); c.setFont("Lora", F_BODY)
for item in CHANNELS_VS_MERIDIANS['counts']:
    lines = wrap_words("\u2022 " + item, "Lora", F_BODY, CW - 6)
    for l in lines:
        c.drawString(ML, y, l); y -= F_BODY_LH
    y -= 3
y -= 8
y = para(y, "This course's ten weeks build through this system in order: channel theory (this week), the 12 "
             "Primary Meridians one by one (Weeks 2-6), additional channels and regions (Week 7), the 8 "
             "Extraordinary Vessels (Week 8), and acupuncture points (Week 9). Everything after this week "
             "assumes this vocabulary is second nature.", size=9.5, lh=12.5, color=GRAY)

y -= 14
setstroke(GOLD); c.setLineWidth(HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 20

# ============= ZANG-FU + NOMENCLATURE (same page) =============
y = section_rule(y, "Zang-Fu Organ Theory")
col_w = (CW - 24) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Zang (Yin) Organs - 6 total")
y -= 16
setfill(DARK); c.setFont("Lora", F_BODY)
for o in ZANG_ORGANS:
    c.drawString(ML, y, "\u2022 " + o); y -= F_BODY_LH
left_bottom = y
y2 = top_y; x2 = ML + col_w + 24
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "Fu (Yang) Organs - 6 total")
y2 -= 16
setfill(DARK); c.setFont("Lora", F_BODY)
for o in FU_ORGANS:
    c.drawString(x2, y2, "\u2022 " + o); y2 -= F_BODY_LH
right_bottom = y2
y = min(left_bottom, right_bottom) - 14

y = para(y, "Zang organs are solid/dense and considered Yin. Fu organs are hollow and considered Yang. "
             "Each of the 12 Primary Meridians pertains to exactly one of these 12 organs, and connects to "
             "its interior-exterior paired organ (its Zang-Fu partner).", size=9.5, lh=12.5, color=GRAY)
y -= 16

y = section_rule(y, "The 3-Part Nomenclature System")
setfill(DARK); c.setFont("Lora", F_BODY)
for i, part in enumerate(NOMENCLATURE['parts'], 1):
    lines = wrap_words(f"{i}. {part}", "Lora", F_BODY, CW - 4)
    for l in lines:
        c.drawString(ML, y, l); y -= F_BODY_LH
    y -= 3
y -= 4
setfill(GRAY); c.setFont("Lora-Italic", 9.3)
for l in wrap_words(NOMENCLATURE['example'], "Lora-Italic", 9.3, CW - 4):
    c.drawString(ML, y, l); y -= 12
y -= 10
y = para(y, NOMENCLATURE['location_note'], size=9.3, lh=12, color=GRAY)

end_page()

# ============= PAGE 4: 12 MERIDIANS TABLE =============
new_page(f"The 12 Primary Meridians  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Full Reference Table", width=200)
setfill(NAVY); c.setFont("Lora-Bold", F_TABLE)
c.drawString(ML, y, "Ab"); c.drawString(ML + 36, y, "Name"); c.drawString(ML + 175, y, "Classification")
c.drawString(ML + 320, y, "Direction"); c.drawString(ML + 440, y, "Circuit")
y -= 15
for ab, name, cls, pol, direction, circuit in TWELVE_MERIDIANS:
    if row_num[0] % 2 == 0:
        setfill(ROW_TINT); c.rect(ML - 4, y - 3, CW + 8, 14, fill=1, stroke=0)
    row_num[0] += 1
    setfill(RED); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, ab)
    setfill(DARK); c.setFont("Lora", F_TABLE)
    c.drawString(ML + 36, y, name)
    c.drawString(ML + 175, y, cls)
    c.drawString(ML + 320, y, direction)
    c.drawString(ML + 440, y, circuit)
    y -= 14.5
y -= 14

y = para(y, "This is the single most important table in this document. Every week from here forward builds "
             "on knowing a channel's abbreviation, full classification, direction of flow, and which circuit "
             "it belongs to, instantly and without hesitation.", size=9.5, lh=12.5, color=GRAY)
y -= 8
setstroke(GOLD); c.setLineWidth(HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 16

# ============= DISTRIBUTION DIAGRAM (from Dr. Zhang's slides, same page) =============
y = section_rule(y, "Distribution of the 12 Main Meridians", width=280, size=11.5)
y = para(y, "From Dr. Zhang's own lecture slides: on the limbs, Yin meridians run the medial aspect and Yang "
             "meridians run the lateral aspect. On the head and trunk, Anterior = Yangming, Posterior = "
             "Taiyang, Lateral = Shaoyang.", size=9, lh=11.5)
y -= 6
img_w = CW * 0.85
img_h = img_w * 0.577
c.drawImage("/home/claude/wk1slides/jpg_p27.jpg", ML, y - img_h, width=img_w, height=img_h)
y -= img_h + 8
setfill(GRAY); c.setFont("Lora-Italic", 7.5)
c.drawCentredString(W / 2, y, "Source: Dr. Zhang's Week 1 lecture slides")
end_page()

# ============= THE THREE CIRCUITS, WITH DIAGRAMS =============
circuit_images = {"Outer Circuit": "jpg_p31.jpg", "Inner Circuit": "jpg_p33.jpg", "Middle Circuit": "jpg_p35.jpg"}
circuit_titles = {"Outer Circuit": "The Anterior Circuit", "Inner Circuit": "The Posterior Circuit", "Middle Circuit": "The Middle Circuit"}

for circuit_name, position, members, elements in CIRCUITS:
    new_page(f"{circuit_titles[circuit_name]}  \u00b7  {EDLABEL}")
    y = H - HEADER_H - 26
    y = section_rule(y, f"{circuit_titles[circuit_name]} ({position})", width=280)
    setfill(GRAY); c.setFont("Lora-Italic", 9)
    c.drawString(ML, y, elements)
    y -= 16
    setfill(DARK); c.setFont("Lora", F_BODY)
    seq = "  ->  ".join(members)
    for l in wrap_words(seq, "Lora", F_BODY, CW - 4):
        c.drawString(ML, y, l); y -= F_BODY_LH
    y -= 12
    img_w = CW
    img_h = img_w * 0.577
    c.drawImage(f"/home/claude/wk1slides/{circuit_images[circuit_name]}", ML, y - img_h, width=img_w, height=img_h)
    y -= img_h + 10
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    c.drawCentredString(W / 2, y, "Source: Dr. Zhang's Week 1 lecture slides")
    end_page()

# ============= THREE CIRCUITS SUMMARY DIAGRAM =============
new_page(f"Three Circuits Summary  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Three Main Circuits in the Flow of Qi \u2014 Summary", width=340)
y = para(y, "A useful way to remember: the Outer Circuit's Yang partner is Yangming (LI, ST); the Inner "
             "Circuit's Yang partner is Taiyang (SI, BL); the Middle Circuit's Yang partner is Shaoyang "
             "(SJ, GB). Match the location name to the circuit and the rest follows.", size=9.5, lh=12.5)
y -= 10
img_w = CW
img_h = img_w * 0.577
c.drawImage("/home/claude/wk1slides/jpg_p36.jpg", ML, y - img_h, width=img_w, height=img_h)
y -= img_h + 10
setfill(GRAY); c.setFont("Lora-Italic", 8)
c.drawCentredString(W / 2, y, "Source: Dr. Zhang's Week 1 lecture slides")

end_page()

# ============= PAGE 6: DIRECTION + MEETING POINTS =============
new_page(f"Circulation & Meeting Points  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Direction of Qi Flow", width=200)
for rule, direction in DIRECTION_RULES:
    setfill(NAVY); c.setFont("Lora-Bold", F_BODY)
    c.drawString(ML, y, rule)
    setfill(RED); c.setFont("Lora-Bold", F_BODY)
    c.drawString(ML + 260, y, direction)
    y -= 15
y -= 4
y = para(y, "This four-part rule is the single most repeated fact across every lecture and quiz review in "
             "this course. Memorize it as one continuous loop: chest to hand, hand to head, head to foot, "
             "foot to chest - and back to chest again, completing the cycle.", size=9.5, lh=12.5, color=GRAY)
y -= 14

y = section_rule(y, "Where Paired Meridians Meet", width=240)
for pair, location, note in MEETING_POINTS:
    setfill(NAVY); c.setFont("Lora-Bold", F_BODY)
    c.drawString(ML, y, f"{pair}, {location}")
    y -= 13
    setfill(GRAY); c.setFont("Lora-Italic", 9)
    for l in wrap_words(note, "Lora-Italic", 9, CW - 14):
        c.drawString(ML + 14, y, l); y -= 12
    y -= 4

y -= 10
setstroke(GOLD); c.setLineWidth(HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 18

# ============= MERIDIAN CLOCK + FUNCTIONS (same page) =============
y = section_rule(y, "The Meridian Clock (24-Hour Cycle)", width=280)
y = para(y, "Each meridian has a two-hour period of peak activity, following the same order the meridians "
             "connect to each other. Dr. Zhang's own clinical example: to treat a Large Intestine dysfunction, "
             "consider its 5-7 AM active window; symptoms that flare at a specific time of day can point "
             "directly to which channel is involved.")
y -= 8
col_w = (CW - 24) / 2
top_y = y
setfill(DARK); c.setFont("Lora", F_TABLE)
half = len(MERIDIAN_CLOCK) // 2
for ab, tm in MERIDIAN_CLOCK[:half]:
    c.drawString(ML, y, f"{ab}: {tm}"); y -= 13.5
left_bottom = y
y2 = top_y; x2 = ML + col_w + 24
for ab, tm in MERIDIAN_CLOCK[half:]:
    c.drawString(x2, y2, f"{ab}: {tm}"); y2 -= 13.5
right_bottom = y2
y = min(left_bottom, right_bottom) - 16

y = section_rule(y, "The 3 Functions of Meridians", width=240)
for name, desc in FUNCTIONS_OF_MERIDIANS:
    setfill(RED); c.setFont("Lora-Bold", F_BODY)
    c.drawString(ML, y, name); y -= 13
    y = para(y, desc, size=9.3, lh=12)
    y -= 6

end_page()

# ============= PAGE 8: CLINICAL PEARLS + QUIZ 1 FUNDAMENTALS =============
new_page(f"Clinical Pearls & Quiz 1 Fundamentals  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Dr. Zhang's Clinical Pearls \u2014 Direct from Lecture", width=340)
for title, body in CLINICAL_PEARLS_WK1:
    setfill(RED); c.setFont("Lora-Bold", 10.3)
    for l in wrap_words(title, "Lora-Bold", 10.3, CW - 4):
        c.drawString(ML, y, l); y -= 13.5
    y = para(y, body, size=9.5, lh=12.5)
    y -= 9

y -= 8
y = section_rule(y, "Quiz 1 Fundamentals", width=200)
for label, items in [
    ("Key Terms", QUIZ1_FUNDAMENTALS['key_terms']),
    ("Nomenclature", QUIZ1_FUNDAMENTALS['nomenclature']),
    ("Circulation", QUIZ1_FUNDAMENTALS['circulation']),
    ("Circuits", QUIZ1_FUNDAMENTALS['circuits']),
    ("Functions", QUIZ1_FUNDAMENTALS['functions']),
]:
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y, label); y -= 14
    setfill(DARK); c.setFont("Lora", F_TABLE)
    for item in items:
        for l in wrap_words("\u2022 " + item, "Lora", F_TABLE, CW - 6):
            c.drawString(ML, y, l); y -= 12
    y -= 8

setfill(RED); c.setFont("Lora-BoldItalic", 9.5)
for l in wrap_words(QUIZ1_FUNDAMENTALS['homework_note'], "Lora-BoldItalic", 9.5, CW - 4):
    c.drawString(ML, y, l); y -= 12.5

end_page()

c.save()
print("SAVED:", OUT)
