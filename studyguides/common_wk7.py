"""Shared rendering framework for all Week 7 (Eight Extraordinary Vessels)
documents. Cover page geometry matches the locked Week 2 spec exactly.
Print + reMarkable editions controlled via sys.argv[1] in each build script."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

FONT_DIR = "/home/claude/ac300wk7/fonts"
FIGS_DIR = "/home/claude/ac300wk7/figs"
for _name, _fn in [("Lora", "Lora-Regular.ttf"), ("Lora-Bold", "Lora-Bold.ttf"),
                    ("Lora-Italic", "Lora-Italic.ttf"), ("Lora-BoldItalic", "Lora-BoldItalic.ttf")]:
    try:
        pdfmetrics.registerFont(TTFont(_name, f"{FONT_DIR}/{_fn}"))
    except Exception:
        pass

W, H = letter
ML, MR = 42, 42
RX = W - MR
CW = RX - ML

NAVY = (0x1d/255, 0x3a/255, 0x5e/255)
GOLD = (0xc8/255, 0x93/255, 0x3a/255)
GOLD_DARK = (0x9c/255, 0x7a/255, 0x37/255)
RED = (0xc0/255, 0x39/255, 0x2b/255)
LBLUE = (0.937, 0.949, 0.965)     # #edf2f6
GRAYBLUE = (0.933, 0.937, 0.949)  # ~#eeeff2, cram sheet cover boxes
DARK = (0.10, 0.10, 0.10)
GRAY = (0.40, 0.40, 0.40)
LGRAY = (0.55, 0.55, 0.55)
WHITE = (1, 1, 1)
CARD_BG = (0.937, 0.937, 0.898)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0
PAGE_BG = (0.98, 0.965, 0.93) if IS_RM else (1, 1, 1)
EDLABEL = "reMarkable Edition" if IS_RM else "Print Edition"
HEADER_SIZE = 51 if IS_RM else 44  # cover WEEK badge number size scales per reMarkable rule


def tint(rgb, amt=0.6):
    r, g, b = rgb
    return (r + (1 - r) * amt, g + (1 - g) * amt, b + (1 - b) * amt)


def new_canvas(path):
    return canvas.Canvas(path, pagesize=letter)


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


def draw_paragraph(c, text, x, y, max_width, font="Lora", size=9, leading=12,
                    color=DARK, align="left"):
    setfill(c, color)
    c.setFont(font, size)
    for ln in wrap_words(text, font, size, max_width):
        if align == "left":
            c.drawString(x, y, ln)
        elif align == "center":
            c.drawCentredString(x + max_width / 2, y, ln)
        y -= leading
    return y


def box(c, x, y, w, h, rgb):
    setfill(c, rgb)
    c.rect(x, y - h, w, h, stroke=0, fill=1)
    return y - h


def hairline(c, x1, y, x2, rgb=GOLD, w=0.75):
    setstroke(c, rgb)
    c.setLineWidth(w * LW_MULT)
    c.line(x1, y, x2, y)


def page_bg(c):
    setfill(c, PAGE_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def top_bar(c, doc_label):
    setfill(c, DARK); c.setFont("Lora", 8.5)
    c.drawString(ML, H - 30.3, f"AC300/AC375  |  {doc_label}  |  VUIM Summer 2026")
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(RX, H - 30.3, EDLABEL)
    hairline(c, ML, H - 38, RX, rgb=GOLD, w=0.6)


def bottom_bar(c, label, page_num):
    setfill(c, NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora", 8)
    c.drawString(ML, 10, label)
    c.drawRightString(RX, 10, f"p.{page_num}")


class DocBuilder:
    """Thin page-lifecycle wrapper shared by all four Week 7 build scripts."""
    def __init__(self, out_path, doc_label, footer_label):
        self.c = new_canvas(out_path)
        self.doc_label = doc_label
        self.footer_label = footer_label
        self.page_num = 1
        self.out_path = out_path

    def new_page(self, bare=False):
        page_bg(self.c)
        if not bare:
            top_bar(self.c, self.doc_label)

    def end_page(self):
        bottom_bar(self.c, self.footer_label, self.page_num)
        self.c.showPage()
        self.page_num += 1

    def save(self):
        self.c.save()
        print(f"Saved {self.out_path}  ({self.page_num - 1} pages)")


# ---------------------------------------------------------------------------
# COVER PAGES -- geometry locked to the Week 2 spec
# ---------------------------------------------------------------------------

def studyguide_cover(db, title, subtitle, points_line, covers_bullets, info_lines):
    c = db.c
    db.new_page(bare=True)
    # navy masthead bar, 80pt, centered white course title
    masthead_h = 80
    setfill(c, NAVY); c.rect(0, H - masthead_h, W, masthead_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 15)
    c.drawCentredString(W / 2, H - 34, "Acupuncture Channels & Points I")
    c.setFont("Lora-Italic", 10.5)
    c.drawCentredString(W / 2, H - 52, "AC300 / AC375  \u00b7  VUIM Summer 2026  \u00b7  Dr. Vivian Zhang, Ph.D.")
    setfill(c, GOLD); c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, H - 68, EDLABEL)

    y = H - masthead_h - 34
    # WEEK badge, centered, 68x68
    badge_w = 68
    bx = (W - badge_w) / 2
    setfill(c, LBLUE); c.rect(bx, y - badge_w, badge_w, badge_w, fill=1, stroke=0)
    setfill(c, GOLD); c.rect(bx, y - badge_w, 5, badge_w, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 7)
    c.drawCentredString(bx + badge_w / 2 + 2, y - 20, "WEEK")
    c.setFont("Lora-Bold", 22)
    c.drawCentredString(bx + badge_w / 2 + 2, y - 48, "7")
    y -= badge_w + 26

    setfill(c, NAVY); c.setFont("Lora-Bold", 32)
    c.drawCentredString(W / 2, y, title)
    y -= 30
    setfill(c, RED); c.setFont("Lora-BoldItalic", 18)
    c.drawCentredString(W / 2, y, subtitle)
    y -= 24
    setfill(c, GRAY); c.setFont("Lora-Italic", 11)
    c.drawCentredString(W / 2, y, points_line)
    y -= 16
    hairline(c, ML + 60, y, RX - 60, rgb=GOLD, w=1.2)
    y -= 26

    setfill(c, RED); c.setFont("Lora-Bold", 13)
    c.drawString(ML, y, "This Week Covers:")
    y -= 20
    box_top = y
    lbox_y = y
    box_lines_h = 0
    wrapped_bullets = []
    for b in covers_bullets:
        lines = wrap_words(b, "Lora", 8.5, CW - 44)
        wrapped_bullets.append(lines)
        box_lines_h += 12.5 * len(lines) + 3
    boxh = box_lines_h + 16
    box(c, ML, box_top, CW, boxh, LBLUE)
    ty = box_top - 13
    setfill(c, DARK); c.setFont("Lora", 8.5)
    for lines in wrapped_bullets:
        for i, ln in enumerate(lines):
            prefix = "\u2022  " if i == 0 else "   "
            c.drawString(ML + 14, ty, prefix + ln)
            ty -= 12.5
        ty -= 3
    y = box_top - boxh - 18

    infoh = 14 + 13 * len(info_lines)
    box(c, ML, y, CW, infoh, LBLUE)
    ty = y - 14
    setfill(c, DARK); c.setFont("Lora-Italic", 9)
    for ln in info_lines:
        c.drawString(ML + 14, ty, ln)
        ty -= 13
    y -= infoh + 30

    setfill(c, GRAY); c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
    db.end_page()


def cramsheet_cover(db, points_line, box_triplets, extras_line):
    """box_triplets: list of (heading, color, [2 italic lines])"""
    c = db.c
    db.new_page(bare=True)
    y = H - 70
    setfill(c, GOLD); c.setFont("Lora-Italic", 9.5)
    c.drawCentredString(W / 2, y, "WEEK 7  \u00b7  " + EDLABEL)
    y -= 34
    setfill(c, NAVY); c.setFont("Lora-Bold", 28)
    c.drawCentredString(W / 2, y, "CRAM SHEET")
    y -= 22
    setfill(c, RED); c.setFont("Lora-BoldItalic", 13)
    c.drawCentredString(W / 2, y, "The Eight Extraordinary Vessels \u2014 Qi Jing Ba Mai")
    y -= 20
    setfill(c, GRAY); c.setFont("Lora-Italic", 10.5)
    c.drawCentredString(W / 2, y, points_line)
    y -= 15
    setfill(c, GOLD_DARK); c.setFont("Lora-BoldItalic", 10.5)
    c.drawCentredString(W / 2, y, "Quiz Ready \u2014 Quiz 5")
    y -= 20
    rule_w = 240
    hairline(c, (W - rule_w) / 2, y, (W + rule_w) / 2, rgb=GOLD, w=1.2)
    y -= 30

    box_w, box_h, gap = 150, 54, 15
    total_w = 3 * box_w + 2 * gap
    x0 = (W - total_w) / 2
    for i, (heading, color, lines) in enumerate(box_triplets):
        bx = x0 + i * (box_w + gap)
        box(c, bx, y, box_w, box_h, GRAYBLUE)
        setfill(c, color); c.setFont("Lora-Bold", 9.5)
        c.drawCentredString(bx + box_w / 2, y - 16, heading)
        setfill(c, DARK); c.setFont("Lora-Italic", 7.6)
        ty = y - 30
        for ln in lines:
            c.drawCentredString(bx + box_w / 2, ty, ln)
            ty -= 10.5
    y -= box_h + 22

    setfill(c, GRAY); c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, y, extras_line)
    y -= 20
    hairline(c, ML, y, RX, rgb=GOLD, w=1)
    y -= 26

    setfill(c, GRAY); c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
    db.end_page()


# ---------------------------------------------------------------------------
# Vessel pathway "station strip" -- schematic substitute where no CAM/MOA
# photographic figure exists (all vessels except GV, which uses CAM_GV.jpeg).
# ---------------------------------------------------------------------------

def pathway_strip(c, course_steps, x, y_top, w, accent, size=8, node_r=6.5):
    """Vertical numbered-station diagram: circle-numbered nodes connected by
    a vertical accent line, one line of wrapped text per station."""
    line_x = x + node_r
    setstroke(c, accent); c.setLineWidth(1.6 * LW_MULT)
    y = y_top
    positions = []
    row_h_list = []
    leading = size * 1.4
    for i, step in enumerate(course_steps):
        lines = wrap_words(step, "Lora", size, w - 26)
        row_h = max(leading + 6, leading * len(lines) + 4)
        positions.append(y)
        row_h_list.append(row_h)
        y -= row_h
    # connecting line
    if len(positions) > 1:
        c.line(line_x, positions[0], line_x, positions[-1])
    for i, (step, ypos, row_h) in enumerate(zip(course_steps, positions, row_h_list)):
        setfill(c, accent); c.circle(line_x, ypos, node_r, fill=1, stroke=0)
        setfill(c, WHITE); c.setFont("Lora-Bold", size - 0.5)
        c.drawCentredString(line_x, ypos - 2.6, str(i + 1))
        setfill(c, DARK); c.setFont("Lora", size)
        lines = wrap_words(step, "Lora", size, w - 26)
        ty = ypos + 3
        for ln in lines:
            c.drawString(line_x + 16, ty, ln)
            ty -= leading
    return y - 6


def get_img_size(fig_key):
    with Image_open(f"{FIGS_DIR}/{fig_key}.jpeg") as im:
        return im.size


def Image_open(path):
    from PIL import Image
    return Image.open(path)


def draw_image_contain(c, fig_key, x, y_top, box_w, box_h, border_color):
    iw, ih = get_img_size(fig_key)
    scale = min(box_w / iw, box_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (box_w - dw) / 2
    dy = y_top - dh
    setstroke(c, border_color); c.setLineWidth(0.8 * LW_MULT)
    c.rect(dx - 2, dy - 2, dw + 4, dh + 4, fill=0, stroke=1)
    c.drawImage(ImageReader(f"{FIGS_DIR}/{fig_key}.jpeg"), dx, dy, width=dw, height=dh)
    return dy


def section_label(c, y, text, color, size=9.5, x=None):
    if x is None:
        x = ML
    setfill(c, color); c.setFont("Lora-Bold", size)
    c.drawString(x, y, text)
    return y - 14
