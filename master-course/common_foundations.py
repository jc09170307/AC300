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


# ---------------------------------------------------------------------------
# Diagrams -- redrawn as vectors from Lecture 1 source slides (cited in caption)
# ---------------------------------------------------------------------------

def draw_arrow(c, x1, y1, x2, y2, color=NAVY, width=1.3, head_len=6.5, head_w=4):
    import math
    setstroke(c, color); setfill(c, color)
    c.setLineWidth(width * LW_MULT)
    c.line(x1, y1, x2, y2)
    ang = math.atan2(y2 - y1, x2 - x1)
    bx = x2 - head_len * math.cos(ang)
    by = y2 - head_len * math.sin(ang)
    lx = bx - head_w * math.sin(ang)
    ly = by + head_w * math.cos(ang)
    rx = bx + head_w * math.sin(ang)
    ry = by - head_w * math.cos(ang)
    p = c.beginPath()
    p.moveTo(x2, y2); p.lineTo(lx, ly); p.lineTo(rx, ry); p.close()
    c.drawPath(p, fill=1, stroke=0)


def figure_caption(db, text):
    c = db.c
    lines = wrap_words(text, "Lora-Italic", 7.8, CW - 10)
    for ln in lines:
        db.ensure(11)
        setfill(c, LGRAY); c.setFont("Lora-Italic", 7.8)
        c.drawCentredString(ML + CW / 2, db.y, ln)
        db.y -= 10.5
    db.y -= 6


def circulation_diagram(db):
    """Redrawn from Lecture 1, Slide 29 ('Circulation of the Twelve Main
    Meridians') -- the chest/hand/head/foot/abdomen directional loop."""
    box_h = 270
    db.ensure(box_h + 40)
    c = db.c
    top = db.y
    setstroke(c, GOLD); c.setLineWidth(0.8 * LW_MULT)
    c.rect(ML, top - box_h, CW, box_h, fill=0, stroke=1)

    cx = ML + CW * 0.46
    head = (cx, top - 38)
    foot = (cx, top - 178)
    chest = (cx - 148, top - 108)
    hand = (cx + 148, top - 108)
    abdomen = (cx - 112, top - 218)

    draw_arrow(c, chest[0] + 30, chest[1], hand[0] - 30, hand[1], NAVY)
    draw_arrow(c, hand[0] - 6, hand[1] + 9, head[0] + 8, head[1] - 9, NAVY)
    draw_arrow(c, head[0], head[1] - 13, foot[0], foot[1] + 13, NAVY)
    draw_arrow(c, foot[0] - 9, foot[1] + 6, abdomen[0] + 12, abdomen[1] - 6, NAVY)
    draw_arrow(c, abdomen[0] + 5, abdomen[1] + 9, chest[0] - 4, chest[1] - 13, NAVY)

    for (x, y, label) in [(head[0], head[1], "Head"), (foot[0], foot[1], "Foot"),
                           (chest[0], chest[1], "Chest"), (hand[0], hand[1], "Hand"),
                           (abdomen[0], abdomen[1], "Abdomen")]:
        setfill(c, WHITE); c.setLineWidth(0.6 * LW_MULT); setstroke(c, NAVY)
        c.circle(x, y, 3, fill=1, stroke=1)
        setfill(c, NAVY); c.setFont("Lora-Bold", 9.5)
        c.drawCentredString(x, y + 10, label)

    setfill(c, RED); c.setFont("Lora-Italic", 7.5)
    # chest -> hand: label sits just ABOVE the line, clear of the vertical head-foot line's own labels
    c.drawCentredString(cx, chest[1] + 9, "Three Yin Meridians of Hand")
    # hand -> head: upper-right, well clear of the Hand node label above and the diagonal itself
    c.drawCentredString(cx + 100, top - 58, "Three Yang Meridians")
    c.drawCentredString(cx + 100, top - 68, "of Hand")
    # head -> foot: right of the vertical line, lower-middle, clear of the two labels above
    c.drawCentredString(cx + 60, top - 148, "Three Yang")
    c.drawCentredString(cx + 60, top - 158, "Meridians of Foot")
    # foot -> abdomen: below-left of that diagonal, clear of the Abdomen node label
    c.drawCentredString(cx - 40, top - 205, "Three Yin")
    c.drawCentredString(cx - 40, top - 215, "Meridians of Foot")

    db.y = top - box_h - 10
    figure_caption(db, "Redrawn from Lecture 1, Slide 29 (\u201cCirculation of the Twelve Main "
                        "Meridians\u201d) \u2014 the closed chest-hand-head-foot-abdomen loop described in Section 5.")


ELEMENT_METAL = (0.42, 0.47, 0.53)
ELEMENT_EARTH = (0.72, 0.55, 0.20)
ELEMENT_FIRE = (0.65, 0.10, 0.10)
ELEMENT_WATER = (0.16, 0.35, 0.62)
ELEMENT_MIN_FIRE = (0.82, 0.42, 0.36)
ELEMENT_WOOD = (0.20, 0.50, 0.28)


def circuits_diagram(db):
    """Redrawn from Lecture 1, Slide 37 ('Three Main Circuits in the Flow of
    Qi'). Element-arrow colors follow the locked element color coding."""
    panel_h = 66
    gap = 14
    banner_h = 26
    total_h = panel_h * 3 + gap * 2 + banner_h + 16
    db.ensure(total_h + 20)
    c = db.c
    top = db.y

    left_lab_w = 62
    right_lab_w = 78
    panel_x0 = ML + left_lab_w
    panel_w = CW - left_lab_w - right_lab_w

    panels = [
        ("Lung", "Large Intestine", "Metal", ELEMENT_METAL,
         "Spleen", "Stomach", "Earth", ELEMENT_EARTH, "Taiyin", "Yangming"),
        ("Heart", "Small Intestine", "Fire", ELEMENT_FIRE,
         "Kidney", "Bladder", "Water", ELEMENT_WATER, "Shaoyin", "Taiyang"),
        ("Pericardium", "San Jiao (SJ)", "Ministerial Fire", ELEMENT_MIN_FIRE,
         "Liver", "Gallbladder", "Wood", ELEMENT_WOOD, "Jueyin", "Shaoyang"),
    ]

    py_top = top
    prev_bl = None
    for (tl, tr, el_top, col_top, bl, br, el_bot, col_bot, yin_lab, yang_lab) in panels:
        panel_top = py_top
        panel_bottom = panel_top - panel_h
        setfill(c, (0.933, 0.925, 0.86)); c.rect(panel_x0, panel_bottom, panel_w, panel_h, fill=1, stroke=0)
        setstroke(c, (0.15, 0.15, 0.15)); c.setLineWidth(1.0 * LW_MULT)
        c.rect(panel_x0, panel_bottom, panel_w, panel_h, fill=0, stroke=1)

        row1_y = panel_top - 20
        row2_y = panel_bottom + 14

        setfill(c, DARK); c.setFont("Lora-Bold", 9.5)
        c.drawString(panel_x0 + 10, row1_y, tl)
        c.drawRightString(panel_x0 + panel_w - 10, row1_y, tr)
        tl_w = pdfmetrics.stringWidth(tl, "Lora-Bold", 9.5)
        tr_w = pdfmetrics.stringWidth(tr, "Lora-Bold", 9.5)
        ax1 = panel_x0 + 14 + tl_w
        ax2 = panel_x0 + panel_w - 14 - tr_w
        draw_arrow(c, ax1, row1_y + 3, ax2, row1_y + 3, col_top, width=1.4)
        setfill(c, col_top); c.setFont("Lora-BoldItalic", 6.6)
        c.drawCentredString((ax1 + ax2) / 2, row1_y + 8, el_top)

        # vertical connector top-right -> bottom-right ("hand to face")
        draw_arrow(c, panel_x0 + panel_w - 10, row1_y - 8, panel_x0 + panel_w - 10, row2_y + 8, NAVY, width=1.1, head_len=5, head_w=3)

        setfill(c, DARK); c.setFont("Lora-Bold", 9.5)
        c.drawString(panel_x0 + 10, row2_y, bl)
        c.drawRightString(panel_x0 + panel_w - 10, row2_y, br)
        bl_w = pdfmetrics.stringWidth(bl, "Lora-Bold", 9.5)
        br_w = pdfmetrics.stringWidth(br, "Lora-Bold", 9.5)
        bx1 = panel_x0 + panel_w - 14 - br_w
        bx2 = panel_x0 + 14 + bl_w
        draw_arrow(c, bx1, row2_y + 3, bx2, row2_y + 3, col_bot, width=1.4)
        setfill(c, col_bot); c.setFont("Lora-BoldItalic", 6.6)
        c.drawCentredString((bx1 + bx2) / 2, row2_y + 8, el_bot)

        setfill(c, NAVY); c.setFont("Lora-Bold", 9)
        c.drawCentredString(ML + left_lab_w / 2, (panel_top + panel_bottom) / 2 - 3, yin_lab)
        c.drawCentredString(RX - right_lab_w / 2 + 6, (panel_top + panel_bottom) / 2 - 3, yang_lab)

        if prev_bl is not None:
            draw_arrow(c, prev_bl[0], prev_bl[1], panel_x0 + 10, panel_top, NAVY, width=1.1, head_len=5, head_w=3)
        prev_bl = (panel_x0 + 10, panel_bottom)

        py_top = panel_bottom - gap

    banner_top = py_top + gap - 4
    banner_bottom = banner_top - banner_h
    setfill(c, LBLUE); c.rect(ML, banner_bottom, CW, banner_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawCentredString(ML + CW / 2, banner_bottom + 9,
                         "Chest   >   Hands/Fingers   >   Face/Head   >   Foot/Toes   >   Chest")

    db.y = banner_bottom - 8
    figure_caption(db, "Redrawn from Lecture 1, Slide 37 (\u201cThree Main Circuits in the Flow of "
                        "Qi\u201d). Arrow colors follow the locked element color coding (Metal, Earth, "
                        "Fire, Water, Ministerial Fire, Wood).")
