"""Shared design system for AC300 Week 6 (PC/SJ/GB/LR) documents."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/home/claude/ac300wk6/fonts"
pdfmetrics.registerFont(TTFont("Lora", f"{FONT_DIR}/Lora-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Lora-Bold", f"{FONT_DIR}/Lora-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Lora-Italic", f"{FONT_DIR}/Lora-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Lora-BoldItalic", f"{FONT_DIR}/Lora-BoldItalic.ttf"))

PAGE_W, PAGE_H = letter

# ---- Locked design tokens ----
NAVY = (0x1d/255, 0x3a/255, 0x5e/255)
GOLD = (0x9c/255, 0x7a/255, 0x37/255)
GOLD_TAB = (0xc8/255, 0x93/255, 0x3a/255)
RED = (0xa0/255, 0x38/255, 0x2e/255)
RED2 = (0xc0/255, 0x39/255, 0x2b/255)
LIGHTBLUE = (0xed/255, 0xf2/255, 0xf6/255)
GRAY = (0.35, 0.35, 0.35)
LGRAY = (0.55, 0.55, 0.55)
WHITE = (1, 1, 1)
BLACK = (0.08, 0.08, 0.08)

# Element color coding (locked, enforced every build)
MINISTER = (0.80, 0.40, 0.36)   # PC/SJ - Ministerial Fire - coral/lighter red, NEVER purple
WOOD = (0.20, 0.48, 0.27)       # GB/LR - Wood - green

def tint(rgb, amt=0.60):
    r, g, b = rgb
    return (r + (1 - r) * amt, g + (1 - g) * amt, b + (1 - b) * amt)

MARGIN = 42
CONTENT_W = PAGE_W - 2 * MARGIN
TOP_BAR_H = 46
FOOTER_Y = 30

def new_canvas(path):
    return canvas.Canvas(path, pagesize=letter)

def set_fill(c, rgb):
    c.setFillColorRGB(*rgb)

def set_stroke(c, rgb):
    c.setStrokeColorRGB(*rgb)

def hairline(c, x1, y, x2, rgb=GOLD, w=0.75):
    set_stroke(c, rgb)
    c.setLineWidth(w)
    c.line(x1, y, x2, y)

def wrap_text(text, font, size, max_width):
    words = text.split()
    lines = []
    cur = ""
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
                    color=BLACK, align="left"):
    set_fill(c, color)
    c.setFont(font, size)
    lines = wrap_text(text, font, size, max_width)
    for ln in lines:
        if align == "left":
            c.drawString(x, y, ln)
        elif align == "center":
            c.drawCentredString(x + max_width / 2, y, ln)
        y -= leading
    return y

def header_bar(c, section_letter, title, subtitle=None):
    label = f"Section {section_letter} \u2014 {title}" if section_letter else title
    # Shrink title font if needed so it always fits on one line within margins.
    size = 15
    while pdfmetrics.stringWidth(label, "Lora-Bold", size) > CONTENT_W and size > 9:
        size -= 0.5
    bar_h = TOP_BAR_H if not subtitle else TOP_BAR_H + 16
    set_fill(c, NAVY)
    c.rect(0, PAGE_H - bar_h, PAGE_W, bar_h, stroke=0, fill=1)
    set_fill(c, GOLD_TAB)
    c.rect(0, PAGE_H - bar_h - 3, PAGE_W, 3, stroke=0, fill=1)
    set_fill(c, WHITE)
    c.setFont("Lora-Bold", size)
    c.drawString(MARGIN, PAGE_H - 30, label)
    if subtitle:
        sub_size = 9.5
        while pdfmetrics.stringWidth(subtitle, "Lora-Italic", sub_size) > CONTENT_W and sub_size > 7:
            sub_size -= 0.5
        c.setFont("Lora-Italic", sub_size)
        set_fill(c, (0.78, 0.84, 0.91))
        c.drawString(MARGIN, PAGE_H - 48, subtitle)
    return PAGE_H - bar_h - 22

def footer(c, page_label, page_num):
    hairline(c, MARGIN, FOOTER_Y + 12, PAGE_W - MARGIN, rgb=LGRAY, w=0.5)
    set_fill(c, LGRAY)
    c.setFont("Lora-Italic", 7.5)
    c.drawString(MARGIN, FOOTER_Y, f"AC300/375 \u00b7 Week 6 \u00b7 PC/SJ/GB/LR \u00b7 {page_label}")
    c.drawRightString(PAGE_W - MARGIN, FOOTER_Y, f"p.{page_num}")

def write_lines(c, x, y, width, n=1, gap=26, rgb=GOLD, w=0.6):
    for i in range(n):
        hairline(c, x, y - i * gap, x + width, rgb=rgb, w=w)
    return y - (n - 1) * gap

def numbered_question(c, num, text, x, y, width, lines=1, size=9, leading=12.5,
                       gap=24, font="Lora", label_color=NAVY):
    set_fill(c, label_color)
    c.setFont("Lora-Bold", size)
    num_str = f"{num}."
    c.drawString(x, y, num_str)
    num_w = pdfmetrics.stringWidth(num_str + " ", "Lora-Bold", size)
    y2 = draw_paragraph(c, text, x + num_w, y, width - num_w, font=font,
                         size=size, leading=leading, color=BLACK)
    y2 -= 6
    y2 = write_lines(c, x + 10, y2, width - 10, n=lines, gap=gap)
    return y2 - gap + 4

def tag_badge(c, x, y, label, rgb):
    c.setFont("Lora-Bold", 7.5)
    w = pdfmetrics.stringWidth(label, "Lora-Bold", 7.5) + 10
    set_fill(c, rgb)
    c.roundRect(x, y - 2, w, 12, 2, stroke=0, fill=1)
    set_fill(c, WHITE)
    c.drawCentredString(x + w / 2, y + 1, label)
    return w

def callout_box(c, x, y, w, h, rgb_fill=LIGHTBLUE):
    set_fill(c, rgb_fill)
    c.rect(x, y - h, w, h, stroke=0, fill=1)
    return y - h
