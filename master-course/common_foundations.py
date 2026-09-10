"""Shared rendering framework for the AC300 Master Course, Module 1: Foundations.
Adapted from the locked studyguides/common_wk9.py framework (cover geometry,
colors, fonts, QA constraints unchanged). Print + reMarkable editions via
sys.argv[1]."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/home/claude/foundations/fonts"
for _name, _fn in [("Lora", "Lora-Regular.ttf"), ("Lora-Bold", "Lora-Bold.ttf"),
                    ("Lora-Italic", "Lora-Italic.ttf"), ("Lora-BoldItalic", "Lora-BoldItalic.ttf")]:
    pdfmetrics.registerFont(TTFont(_name, f"{FONT_DIR}/{_fn}"))

W, H = letter
ML, MR = 42, 42
RX = W - MR
CW = RX - ML
BOTTOM_LIMIT = 46  # min y before forcing a page break

NAVY = (0x1d/255, 0x3a/255, 0x5e/255)
GOLD = (0xc8/255, 0x93/255, 0x3a/255)
GOLD_DARK = (0x9c/255, 0x7a/255, 0x37/255)
RED = (0xc0/255, 0x39/255, 0x2b/255)
LBLUE = (0.937, 0.949, 0.965)
GRAYBLUE = (0.933, 0.937, 0.949)
DARK = (0.10, 0.10, 0.10)
GRAY = (0.40, 0.40, 0.40)
LGRAY = (0.55, 0.55, 0.55)
WHITE = (1, 1, 1)
GREEN_DANCE = (0.13, 0.42, 0.29)  # dance-relevance sidebar accent (new, non-element color)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0
PAGE_BG = (0.98, 0.965, 0.93) if IS_RM else (1, 1, 1)
EDLABEL = "reMarkable Edition" if IS_RM else "Print Edition"


def setfill(c, rgb): c.setFillColorRGB(*rgb)
def setstroke(c, rgb): c.setStrokeColorRGB(*rgb)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def hairline(c, x1, y, x2, rgb=GOLD, w=0.75):
    setstroke(c, rgb)
    c.setLineWidth(w * LW_MULT)
    c.line(x1, y, x2, y)


def page_bg(c):
    setfill(c, PAGE_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def top_bar(c, doc_label):
    setfill(c, DARK); c.setFont("Lora", 8.5)
    c.drawString(ML, H - 30.3, f"AC300/AC375 Master Course  |  {doc_label}  |  VUIM")
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(RX, H - 30.3, EDLABEL)
    hairline(c, ML, H - 38, RX, rgb=GOLD, w=0.6)


def bottom_bar(c, label, page_num):
    setfill(c, NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora", 8)
    c.drawString(ML, 10, label)
    c.drawRightString(RX, 10, f"p.{page_num}")


class DocBuilder:
    def __init__(self, out_path, doc_label, footer_label):
        self.c = canvas.Canvas(out_path, pagesize=letter)
        self.doc_label = doc_label
        self.footer_label = footer_label
        self.page_num = 1
        self.out_path = out_path
        self.y = H

    def new_page(self, bare=False):
        page_bg(self.c)
        if not bare:
            top_bar(self.c, self.doc_label)
            self.y = H - 54
        else:
            self.y = H

    def end_page(self):
        bottom_bar(self.c, self.footer_label, self.page_num)
        self.c.showPage()
        self.page_num += 1

    def ensure(self, min_h):
        """Start a fresh content page if there isn't min_h of room left."""
        if self.y - min_h < BOTTOM_LIMIT:
            self.end_page()
            self.new_page()

    def save(self):
        self.c.save()
        print(f"Saved {self.out_path}  ({self.page_num - 1} pages)")


# ---------------------------------------------------------------------------
# Cover page -- Module variant of the locked Week-cover geometry
# ---------------------------------------------------------------------------

def module_cover(db, title, subtitle, points_line, covers_bullets, info_lines, module_num="1"):
    c = db.c
    db.new_page(bare=True)
    masthead_h = 80
    setfill(c, NAVY); c.rect(0, H - masthead_h, W, masthead_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 15)
    c.drawCentredString(W / 2, H - 34, "AC300 Master Course")
    c.setFont("Lora-Italic", 10.5)
    c.drawCentredString(W / 2, H - 52, "Acupuncture Channels & Points I  \u00b7  VUIM  \u00b7  Dr. Vivian Zhang, Ph.D.")
    setfill(c, GOLD); c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, H - 68, EDLABEL)

    y = H - masthead_h - 34
    badge_w = 68
    bx = (W - badge_w) / 2
    setfill(c, LBLUE); c.rect(bx, y - badge_w, badge_w, badge_w, fill=1, stroke=0)
    setfill(c, GOLD); c.rect(bx, y - badge_w, 5, badge_w, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 7)
    c.drawCentredString(bx + badge_w / 2 + 2, y - 20, "MODULE")
    c.setFont("Lora-Bold", 22)
    c.drawCentredString(bx + badge_w / 2 + 2, y - 48, module_num)
    y -= badge_w + 26

    setfill(c, NAVY); c.setFont("Lora-Bold", 30)
    for ln in wrap_words(title, "Lora-Bold", 30, CW - 20):
        c.drawCentredString(W / 2, y, ln)
        y -= 32
    y -= 2
    setfill(c, RED)
    sub_size = 16
    while pdfmetrics.stringWidth(subtitle, "Lora-BoldItalic", sub_size) > CW - 20 and sub_size > 11:
        sub_size -= 0.5
    c.setFont("Lora-BoldItalic", sub_size)
    for ln in wrap_words(subtitle, "Lora-BoldItalic", sub_size, CW - 20):
        c.drawCentredString(W / 2, y, ln)
        y -= sub_size + 4
    y -= 6
    setfill(c, GRAY); c.setFont("Lora-Italic", 11)
    for ln in wrap_words(points_line, "Lora-Italic", 11, CW - 20):
        c.drawCentredString(W / 2, y, ln)
        y -= 14
    y -= 2
    hairline(c, ML + 60, y, RX - 60, rgb=GOLD, w=1.2)
    y -= 26

    setfill(c, RED); c.setFont("Lora-Bold", 13)
    c.drawString(ML, y, "This Module Covers:")
    y -= 20
    box_top = y
    wrapped_bullets = []
    box_lines_h = 0
    for b in covers_bullets:
        lines = wrap_words(b, "Lora", 8.5, CW - 44)
        wrapped_bullets.append(lines)
        box_lines_h += 12.5 * len(lines) + 3
    boxh = box_lines_h + 16
    setfill(c, LBLUE); c.rect(ML, box_top - boxh, CW, boxh, fill=1, stroke=0)
    ty = box_top - 13
    setfill(c, DARK); c.setFont("Lora", 8.5)
    for lines in wrapped_bullets:
        for i, ln in enumerate(lines):
            prefix = "\u2022  " if i == 0 else "   "
            c.drawString(ML + 14, ty, prefix + ln)
            ty -= 12.5
        ty -= 3
    y = box_top - boxh - 18

    wrapped_info = [wrap_words(ln, "Lora-Italic", 8.3, CW - 28) for ln in info_lines]
    info_lines_h = sum(11.6 * len(wl) + 3 for wl in wrapped_info)
    infoh = info_lines_h + 14
    setfill(c, LBLUE); c.rect(ML, y - infoh, CW, infoh, fill=1, stroke=0)
    ty = y - 14
    setfill(c, DARK); c.setFont("Lora-Italic", 8.3)
    for wl in wrapped_info:
        for l2 in wl:
            c.drawString(ML + 14, ty, l2)
            ty -= 11.6
        ty -= 3
    y -= infoh + 30

    setfill(c, GRAY); c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
    db.end_page()


# ---------------------------------------------------------------------------
# Content-flow helpers
# ---------------------------------------------------------------------------

def section_header(db, text, size=15):
    db.ensure(34)
    c = db.c
    setfill(c, NAVY); c.setFont("Lora-Bold", size)
    c.drawString(ML, db.y, text)
    db.y -= 8
    hairline(c, ML, db.y, RX, rgb=GOLD, w=1.0)
    db.y -= 18


def sub_header(db, text, color=RED, size=11.5):
    db.ensure(22)
    c = db.c
    setfill(c, color); c.setFont("Lora-Bold", size)
    c.drawString(ML, db.y, text)
    db.y -= 16


def paragraph(db, text, font="Lora", size=9.3, leading=13, color=DARK, indent=0):
    lines = wrap_words(text, font, size, CW - indent)
    for ln in lines:
        db.ensure(leading)
        setfill(db.c, color); db.c.setFont(font, size)
        db.c.drawString(ML + indent, db.y, ln)
        db.y -= leading
    db.y -= 4


def bullet_list(db, items, font="Lora", size=9.3, leading=12.5, color=DARK, marker="\u2022"):
    for item in items:
        lines = wrap_words(item, font, size, CW - 16)
        for i, ln in enumerate(lines):
            db.ensure(leading)
            setfill(db.c, color); db.c.setFont(font, size)
            prefix = f"{marker}  " if i == 0 else "   "
            db.c.drawString(ML, db.y, prefix + ln)
            db.y -= leading
        db.y -= 2
    db.y -= 4


def numbered_list(db, items, font="Lora", size=9.3, leading=12.5, color=DARK):
    for i, item in enumerate(items, start=1):
        lines = wrap_words(item, font, size, CW - 20)
        for j, ln in enumerate(lines):
            db.ensure(leading)
            setfill(db.c, color); db.c.setFont(font, size)
            prefix = f"{i}.  " if j == 0 else "    "
            db.c.drawString(ML, db.y, prefix + ln)
            db.y -= leading
        db.y -= 2
    db.y -= 4


def table(db, headers, rows, col_widths, header_color=NAVY, font_size=8.3, leading=11.5):
    """Simple flowing table. col_widths sum should equal CW."""
    c = db.c
    def row_height(cells):
        h = 0
        for w, cell in zip(col_widths, cells):
            n = max(1, len(wrap_words(cell, "Lora", font_size, w - 10)))
            h = max(h, n * leading)
        return h + 8

    # header row
    db.ensure(row_height(headers) + 4)
    x = ML
    setfill(c, header_color); c.rect(ML, db.y - row_height(headers), CW, row_height(headers), fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", font_size)
    ty = db.y - 12
    for w, h in zip(col_widths, headers):
        for k, ln in enumerate(wrap_words(h, "Lora-Bold", font_size, w - 10)):
            c.drawString(x + 5, ty - k * leading, ln)
        x += w
    db.y -= row_height(headers)

    shade = False
    for row in rows:
        rh = row_height(row)
        db.ensure(rh + 2)
        if shade:
            setfill(c, LBLUE); c.rect(ML, db.y - rh, CW, rh, fill=1, stroke=0)
        shade = not shade
        x = ML
        setfill(c, DARK); c.setFont("Lora", font_size)
        ty = db.y - 12
        for w, cell in zip(col_widths, row):
            for k, ln in enumerate(wrap_words(cell, "Lora", font_size, w - 10)):
                c.drawString(x + 5, ty - k * leading, ln)
            x += w
        setstroke(c, GOLD); c.setLineWidth(0.4 * LW_MULT)
        c.line(ML, db.y - rh, RX, db.y - rh)
        db.y -= rh
    db.y -= 10


def dance_sidebar(db, heading, text):
    """Green-accented sidebar box marking original (non-lecture) dance-relevance synthesis."""
    lines = wrap_words(text, "Lora", 8.6, CW - 32)
    box_h = 22 + len(lines) * 11.8
    db.ensure(box_h + 8)
    c = db.c
    setfill(c, (0.92, 0.96, 0.93)); c.rect(ML, db.y - box_h, CW, box_h, fill=1, stroke=0)
    setfill(c, GREEN_DANCE); c.rect(ML, db.y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, GREEN_DANCE); c.setFont("Lora-BoldItalic", 9.3)
    c.drawString(ML + 14, db.y - 15, f"Ballroom/Dance Relevance \u2014 {heading} (original synthesis, not lecture content)")
    setfill(c, DARK); c.setFont("Lora", 8.6)
    ty = db.y - 30
    for ln in lines:
        c.drawString(ML + 14, ty, ln)
        ty -= 11.8
    db.y -= box_h + 12


def flag_box(db, text):
    """Amber flag box for content gaps / open items."""
    lines = wrap_words(text, "Lora-Italic", 8.6, CW - 32)
    box_h = 10 + len(lines) * 11.8
    db.ensure(box_h + 8)
    c = db.c
    setfill(c, (0.98, 0.94, 0.88)); c.rect(ML, db.y - box_h, CW, box_h, fill=1, stroke=0)
    setfill(c, GOLD_DARK); c.rect(ML, db.y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, (0.15, 0.1, 0.02)); c.setFont("Lora-Italic", 8.6)
    ty = db.y - 13
    for ln in lines:
        c.drawString(ML + 14, ty, ln)
        ty -= 11.8
    db.y -= box_h + 12
