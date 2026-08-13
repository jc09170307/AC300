#!/usr/bin/env python3
"""AC300 Study System Guide -- how to use the document set, weekly study
rhythm, what-to-study roadmap tied to the course calendar, and a motivation
page. Built after Jon's ChatGPT conversation about surface-learning vs
retrieval practice. Single reference doc, Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/home/claude/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.945, 0.937, 0.906)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    CARD_BG = (0.925, 0.902, 0.855)
    OUT = "/mnt/user-data/outputs/AC300_StudySystemGuide_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    CARD_BG = (0.960, 0.962, 0.968)
    OUT = "/mnt/user-data/outputs/AC300_StudySystemGuide_Print.pdf"
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


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle):
    page_bg()
    setfill(NAVY); c.rect(0, H - 46, W, 46, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - 46, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 14)
    c.drawString(ML, H - 30, "AC300 Study System Guide")
    setfill(GOLD); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(W - MR, H - 30, EDLABEL)
    setfill(GRAY); c.setFont("Lora-Italic", 8.3)
    c.drawString(ML, H - 60 + 20, subtitle) if False else None
    return H - 64


def footer():
    setstroke(GOLD); c.setLineWidth(0.7 * LW_MULT)
    c.line(ML, 28, W - MR, 28)
    setfill(GRAY); c.setFont("Lora-Italic", 7.3)
    c.drawCentredString(W / 2, 17, f"AC300/AC375 \u00b7 Study System Guide \u00b7 VUIM Summer 2026 \u00b7 {EDLABEL} \u00b7 p.{page_num[0]}")


def end_page():
    footer(); c.showPage(); page_num[0] += 1


def section_bar(y, title, color=NAVY, size=12.5):
    bar_h = 22
    setfill(color); c.rect(ML, y - bar_h, CW, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", size)
    c.drawString(ML + 8, y - bar_h + 6, title)
    return y - bar_h - 10


# ======================================================================
# COVER
# ======================================================================
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 80, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - 45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 62, EDLABEL)

y = H - 130
setfill(NAVY); c.setFont("Lora-Bold", 27)
c.drawCentredString(W / 2, y, "Study System Guide")
y -= 24
setfill(RED); c.setFont("Lora-BoldItalic", 13.5)
c.drawCentredString(W / 2, y, "How to use every document \u00b7 your weekly rhythm \u00b7 what to study when")
y -= 30

setfill(DARK); c.setFont("Lora", 10)
for l in wrap_words("You already have a full toolkit -- Study Guides, Cram Sheets, the Master Map, Comparison "
                     "Matrix, Special Points Decoder, Retrieval Packets, PLAs. The tools were never the problem. "
                     "This guide is the missing piece: which tool to open, in what order, on which day.", "Lora", 10, CW - 70):
    c.drawCentredString(W / 2, y, l); y -= 13
y -= 16

setfill(NAVY); c.setFont("Lora-Bold", 11.5)
c.drawCentredString(W / 2, y, "This Guide Contains:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.2)
for b in [
    "What each document type is for, and when to open it",
    "A 60-minute weekly study session template",
    "A course-calendar roadmap: what to study, and which docs to pull, every week",
    "A short page on mindset -- grounded, not hype",
]:
    c.drawCentredString(W / 2, y, b)
    y -= 15
y -= 14

box_w = 480
box_h = 40
setfill(CARD_BG); c.rect(W / 2 - box_w / 2, y - box_h, box_w, box_h, fill=1, stroke=0)
setfill(RED); c.setFont("Lora-Bold", 9.5)
c.drawCentredString(W / 2, y - 17, "This is a reference, not new content to memorize.")
setfill(DARK); c.setFont("Lora", 8.8)
c.drawCentredString(W / 2, y - 31, "Read it once now, then flip back to the roadmap page each week.")
y -= box_h + 24

setstroke(GOLD); c.setLineWidth(1)
c.line(50, y, W - 50, y)
y -= 22
c.setFont("Lora-Italic", 9); setfill(GRAY)
c.drawCentredString(W / 2, y, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM Summer 2026")

end_page()

# ======================================================================
# PAGE 2 -- DOCUMENT ROLES
# ======================================================================
y = header("What Each Document Is For")
y -= 4

DOCS = [
    ("Master Map", "1x, whole course", "The 12-channel skeleton -- sequence, circuits, direction rules. Fill it from memory every session, before anything else."),
    ("Comparison Matrix", "1x, cumulative", "Side-by-side triads + paired-channel table. Use for pattern recognition once 2+ weeks are in the same category (e.g. once you've learned a 2nd Hand-Yin channel)."),
    ("Study Guide", "per week", "Reference only -- facts, tables, pathways. Read AFTER you've already tried to recall, to check yourself, not as your first exposure."),
    ("Cram Sheet", "per week", "Night-before density sheet. This is your ANSWER KEY, not your study method -- open it last, not first."),
    ("Special Points Decoder (Tiered)", "per week", "All special-point categories with A/B/C priority tags. Drill Level A until automatic, then B, then C."),
    ("PLA / Prep Guide", "per wk, pre-lecture", "Pre-lecture priming -- confidence ratings, vocab, anticipatory questions, Inter-Quiz. Do Sections A-D before class, Section F after."),
    ("Active Retrieval Packet", "per week", "Closed-book blank-page reconstruction. The actual studying happens here, not in the guides."),
    ("Retrieval Answer Key", "per week", "Checked ONLY after a genuine closed-book attempt at the Retrieval Packet -- never read first."),
    ("Practice Draw", "per week", "Blank pathway silhouettes. Draw from memory, close the slides, draw again, correct in a second color."),
    ("Quiz Kit", "per week", "Standalone practice quiz mimicking the real quiz format."),
]
row_h = 40
hdr_h = 16
setfill(NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 7.8)
c.drawString(ML + 6, y - hdr_h + 5, "DOCUMENT")
c.drawString(ML + 140, y - hdr_h + 5, "CADENCE")
c.drawString(ML + 220, y - hdr_h + 5, "WHEN / HOW TO USE IT")
y -= hdr_h
for i, (name, cadence, desc) in enumerate(DOCS):
    bg = CARD_BG if i % 2 == 0 else ((1, 1, 1) if not IS_RM else PAGE_BG)
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 8.6)
    for li, l in enumerate(wrap_words(name, "Lora-Bold", 8.6, 128)):
        c.drawString(ML + 6, y - 13 - li * 10, l)
    setfill(GRAY); c.setFont("Lora-Italic", 7.6)
    for li, l in enumerate(wrap_words(cadence, "Lora-Italic", 7.6, 74)):
        c.drawString(ML + 140, y - 13 - li * 9.5, l)
    setfill(DARK); c.setFont("Lora", 7.9)
    for li, l in enumerate(wrap_words(desc, "Lora", 7.9, CW - 226)):
        c.drawString(ML + 220, y - 13 - li * 10, l)
    y -= row_h
setstroke(GRAY); c.setLineWidth(0.5)
c.rect(ML, y, CW, hdr_h + row_h * len(DOCS), fill=0, stroke=1)

end_page()

# ======================================================================
# PAGE 3 -- WEEKLY STUDY RHYTHM
# ======================================================================
y = header("Your 60-Minute Study Session Template")
y -= 4
setfill(DARK); c.setFont("Lora-Italic", 9)
for l in wrap_words("This is the session structure from the retrieval-practice conversation -- the sequence matters "
                     "as much as the content. Reference material comes LAST, not first.", "Lora-Italic", 9, CW):
    c.drawString(ML, y, l); y -= 11.5
y -= 10

BLOCKS = [
    ("0-5 min", "Blank-page Master Map", "Full 12-channel sequence + circuits + direction rules, from memory."),
    ("5-15 min", "Draw 1-2 channels", "Practice Draw, closed slides, correct in a 2nd color after."),
    ("15-30 min", "Closed-note recall", "Identity, pathway, pair, special points -- say it or write it before checking anything."),
    ("30-40 min", "Comparison drill", "Comparison Matrix -- against this week's triad or paired neighbor."),
    ("40-50 min", "Active Retrieval Packet", "Closed-book. This is the actual studying."),
    ("50-60 min", "Check + Cram Sheet", "Open the Answer Key and Cram Sheet LAST. Mark what you missed -- that's tomorrow's priority."),
]
row_h = 46
for i, (t, title, desc) in enumerate(BLOCKS):
    bg = CARD_BG if i % 2 == 0 else ((1, 1, 1) if not IS_RM else PAGE_BG)
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(GOLD); c.rect(ML, y - row_h, 4, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 14, y - 16, t)
    setfill(RED); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 90, y - 16, title)
    setfill(DARK); c.setFont("Lora", 8.6)
    for li, l in enumerate(wrap_words(desc, "Lora", 8.6, CW - 104)):
        c.drawString(ML + 90, y - 30 - li * 10.5, l)
    y -= row_h + 4

y -= 10
setfill(GRAY); c.setFont("Lora-Italic", 8.3)
for l in wrap_words("Weekly cadence: run this session 3-4x per week per active channel-week. The 3 Inter-Quiz/Retrieval "
                     "sessions for mastery criterion should land on different days, not the same day repeated.", "Lora-Italic", 8.3, CW):
    c.drawString(ML, y, l); y -= 10.6

end_page()

# ======================================================================
# PAGE 4 -- COURSE ROADMAP
# ======================================================================
y = header("What To Study, Week by Week")
y -= 4

ROADMAP = [
    ("1", "Channel theory, nomenclature, flow of Qi", "", "Week 1 materials"),
    ("2", "LU + LI", "Quiz 2", "Week 2 Study Guide, Cram, PLA"),
    ("3", "ST + SP", "Quiz 3", "Week 3 Study Guide, Cram, PLA, Special Points Decoder"),
    ("4", "HT + SI", "Quiz 4", "Week 4 Study Guide, Cram, Quiz Kit"),
    ("5", "BL + KI", "MIDTERM (wks 1-4)", "Midterm Kit + Week 5 materials"),
    ("6", "PC + SJ + GB + LR", "Quiz 6", "Week 6 full set + Tiered Decoder"),
    ("7", "Divergent / Sinew / Cutaneous systems", "Quiz 7", "Week 7 PLA (build Study Guide after lecture)"),
    ("8", "Eight Extraordinary Vessels", "Quiz 8", "Build EV package before this week"),
    ("9", "Acupuncture points overview", "", "TBD once syllabus confirms"),
    ("10", "Comprehensive review", "FINAL", "Master Comparison + Comparison Matrix + all Cram Sheets"),
]
row_h = 30
hdr_h = 16
setfill(NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 7.8)
c.drawString(ML + 6, y - hdr_h + 5, "WK")
c.drawString(ML + 40, y - hdr_h + 5, "TOPIC")
c.drawString(ML + 260, y - hdr_h + 5, "ASSESSMENT")
c.drawString(ML + 370, y - hdr_h + 5, "PULL THESE DOCS")
y -= hdr_h
for i, (wk, topic, assess, docs) in enumerate(ROADMAP):
    bg = CARD_BG if i % 2 == 0 else ((1, 1, 1) if not IS_RM else PAGE_BG)
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 6, y - 18, wk)
    setfill(DARK); c.setFont("Lora", 8.4)
    for li, l in enumerate(wrap_words(topic, "Lora", 8.4, 210)[:2]):
        c.drawString(ML + 40, y - 13 - li * 10, l)
    setfill(RED if assess else GRAY); c.setFont("Lora-Bold" if assess else "Lora-Italic", 8.2)
    c.drawString(ML + 260, y - 13, assess if assess else "--")
    setfill(GRAY); c.setFont("Lora-Italic", 7.6)
    for li, l in enumerate(wrap_words(docs, "Lora-Italic", 7.6, CW - 376)[:2]):
        c.drawString(ML + 370, y - 13 - li * 9.5, l)
    y -= row_h
setstroke(GRAY); c.setLineWidth(0.5)
c.rect(ML, y, CW, hdr_h + row_h * len(ROADMAP), fill=0, stroke=1)
y -= 16

setfill(GRAY); c.setFont("Lora-Italic", 8)
for l in wrap_words("Weeks 9 topic is provisional pending syllabus confirmation -- Dr. Zhang's Week 1 reading listed "
                     "week 9 as 'acupuncture points' but this hasn't been confirmed against a Week 8/9 transcript yet.",
                     "Lora-Italic", 8, CW):
    c.drawString(ML, y, l); y -= 10.4

end_page()

# ======================================================================
# PAGE 5 -- MINDSET
# ======================================================================
y = header("A Short Page on Mindset")
y -= 6

setfill(DARK); c.setFont("Lora", 9.6)
paras = [
    "Low confidence-rating scores at the start of a PLA aren't a bad sign. They're the actual starting measurement. "
    "The whole point of a Pre/Post rating is to have something honest to compare against -- a 2 that becomes a 4 by "
    "Friday is real progress; a 5 you never earned isn't useful data at all.",
    "The retrieval sessions will feel harder than rereading a Cram Sheet. That's expected, not a signal something's "
    "wrong. Recognition (rereading) and recall (blank-page reconstruction) use different memory systems, and only "
    "the second one is what a quiz or a real patient actually asks of you.",
    "This system is built around effort you're already putting in -- it's not asking for more hours, it's asking "
    "you to spend the hours you already have in a different order. Reference material at the end of a session "
    "instead of the start is a small change with a large effect.",
    "Three years from now, a patient is going to describe a pattern of symptoms and you're going to reconstruct "
    "the channel pathway in your head before you reach for a book. That's what today's blank-page drawing is "
    "actually training -- not this week's quiz, that instinct.",
]
for p in paras:
    for l in wrap_words(p, "Lora", 9.6, CW):
        c.drawString(ML, y, l); y -= 12.6
    y -= 8

y -= 8
setstroke(GOLD); c.setLineWidth(1)
c.line(ML, y, W - MR, y)
y -= 20
setfill(NAVY); c.setFont("Lora-BoldItalic", 10.5)
c.drawCentredString(W / 2, y, "Open the Master Map. Start there. Every session.")

end_page()

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
