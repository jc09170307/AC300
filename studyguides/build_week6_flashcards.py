#!/usr/bin/env python3
"""AC300 Week 6 Flashcards -- PC, SJ, GB, LR. Generates the Anki tab-separated
import file plus a Print/reMarkable reference PDF, matching the Week 5
Flashcards layout exactly (Special-Category Recall page, then per-channel
Point ID from Location and Point Number -> Name pages)."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, "/home/claude/work")
from wk6_flashcard_data import all_cards, ALL_CHANNELS

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
TEAL = (0.118, 0.435, 0.400)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_Week6_Flashcards_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week6_Flashcards_Print.pdf"
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


def section_bar(title):
    y_top = H - 46
    bar_h = 20
    setfill(TEAL); c.rect(ML, y_top - bar_h, CW, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12.5)
    c.drawString(ML + 8, y_top - bar_h + 6, title)
    return y_top - bar_h - 6


def table_header(y):
    hh = 13
    setfill(TEAL); c.rect(ML, y - hh, CW, hh, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 7.6)
    c.drawString(ML + 6, y - hh + 3.5, "Front (Q)")
    c.drawString(ML + CW * 0.52, y - hh + 3.5, "Back (A)")
    return y - hh


def card_table_page(title, cards, cont=False):
    """Paginates a Front/Back card list across as many pages as needed,
    wrapping both columns fully rather than truncating to one line."""
    idx = 0
    first = True
    while idx < len(cards) or first:
        new_page()
        label = title + (" (continued)" if (cont or not first) else "")
        y = section_bar(label)
        y = table_header(y)
        while idx < len(cards):
            front, back = cards[idx]
            fl = wrap_words(front, "Lora", 7.6, CW * 0.48)
            bl = wrap_words(back, "Lora-Bold", 7.6, CW * 0.42)
            row_h = max(len(fl), len(bl)) * 9.4 + 3.2
            if y - row_h < 40:
                break
            bg = (0.937, 0.958, 0.955) if idx % 2 == 0 else (1, 1, 1)
            setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
            setfill(DARK); c.setFont("Lora", 7.6)
            for i, l in enumerate(fl):
                c.drawString(ML + 6, y - 9 - i * 9.4, l)
            setfill(TEAL); c.setFont("Lora-Bold", 7.6)
            for i, l in enumerate(bl):
                c.drawString(ML + CW * 0.52, y - 9 - i * 9.4, l)
            y -= row_h
            idx += 1
        end_page(WEEK_LABEL)
        first = False
        if idx >= len(cards):
            break
    return idx


# ============================================================
# COVER
# ============================================================
data = all_cards()
total_cards = sum(len(d["pointid"]) + len(d["namerecall"]) + len(d["special"]) for d in data.values())

new_page()
y = H - 60
setfill(NAVY); c.setFont("Lora-Bold", 28)
c.drawCentredString(W / 2, y, "Flashcards")
y -= 26
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-BoldItalic", 15)
c.drawCentredString(W / 2, y, "Pericardium, San Jiao, Gallbladder & Liver Channels \u2014 Week 6")
y -= 20
setfill(GOLD); c.setFont("Lora-BoldItalic", 11)
c.drawCentredString(W / 2, y, f"{total_cards} cards \u00b7 spaced-repetition ready")
y -= 18
setstroke(GOLD); c.setLineWidth(1.2)
c.line(ML + 40, y, RX - 40, y)
y -= 26

setfill(DARK); c.setFont("Lora", 10.5)
c.drawString(ML, y, "Two ways to use this set:")
y -= 18
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "For real spaced repetition (recommended)")
y -= 13
setfill(DARK); c.setFont("Lora", 9.5)
for l in wrap_words("Import AC300_Week6_Flashcards_Anki.txt into Anki (File > Import, tab-separated, 3 fields: Front / Back / Tags). This is the format proven to actually build long-term retention -- the PDF below is a reference copy, not a substitute.", "Lora", 9.5, CW - 20):
    c.drawString(ML + 14, y, l); y -= 12.5
y -= 8
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "For quick paper review")
y -= 13
setfill(DARK); c.setFont("Lora", 9.5)
for l in wrap_words("This PDF shows every card as a Q | A row, organized by type. Cover the answer column with a sheet of paper and self-test down the page.", "Lora", 9.5, CW - 20):
    c.drawString(ML + 14, y, l); y -= 12.5

y -= 12
box_h = 46
setfill(CREAM); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(DARK); c.setFont("Lora-Italic", 8.6)
c.drawString(ML + 14, y - 16, "Card types included: (1) Point ID from location clue, (2) Special-category lookup")
c.drawString(ML + 14, y - 29, "(Yuan-Source/Luo/He-Sea/etc.), (3) Pure point-number -> name recall.")
c.drawString(ML + 14, y - 40, "GB set covers this week's high-yield/detailed points, not all 44 (full names in MOA figure).")
y -= box_h + 20

setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300 Flashcards \u00b7 Week 6 \u00b7 pairs with the Anki import file")
end_page(WEEK_LABEL)

# ============================================================
# SPECIAL-CATEGORY RECALL (all 4 channels)
# ============================================================
special_cards = []
for ch in ALL_CHANNELS:
    special_cards.extend(data[ch]["special"])
card_table_page("Special-Category Recall", special_cards)

# ============================================================
# POINT ID FROM LOCATION (per channel)
# ============================================================
for ch in ALL_CHANNELS:
    card_table_page(f"{ch} Point ID from Location", data[ch]["pointid"])

# ============================================================
# POINT NUMBER -> NAME (per channel)
# ============================================================
for ch in ALL_CHANNELS:
    card_table_page(f"{ch} Point Number -> Name", data[ch]["namerecall"])

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
print(f"Total cards: {total_cards}")
