"""Week 6 Pre-Lecture Analysis Sheet v2 -- design system forked from Week 3 v2
(the established PLA reference standard, per Jon's feedback). Centered cover,
gold-tab section headers, confidence-rating rows, connect-the-dots fill-ins,
vocab table, starred anticipatory questions, checkpoint Inter-Quiz + answer key,
clinical case, 3-column after-lecture synthesis."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/home/claude/ac300wk6/fonts"
for name, fn in [("Lora", "Lora-Regular.ttf"), ("Lora-Bold", "Lora-Bold.ttf"),
                  ("Lora-Italic", "Lora-Italic.ttf"), ("Lora-BoldItalic", "Lora-BoldItalic.ttf")]:
    try:
        pdfmetrics.registerFont(TTFont(name, f"{FONT_DIR}/{fn}"))
    except Exception:
        pass

PAGE_W, PAGE_H = letter
MARGIN = 62
CONTENT_W = PAGE_W - 2 * MARGIN

NAVY = (0x1d/255, 0x3a/255, 0x5e/255)
GOLD = (0xc9/255, 0xa0/255, 0x2c/255)
GOLD_DARK = (0x9c/255, 0x7a/255, 0x37/255)
MINT = (0.933, 0.949, 0.918)
CARD_BG = (0.937, 0.937, 0.898)
GRAY = (0.40, 0.40, 0.40)
LGRAY = (0.55, 0.55, 0.55)
WHITE = (1, 1, 1)
BLACK = (0.08, 0.08, 0.08)
MINISTER = (0.80, 0.40, 0.36)   # PC/SJ - Ministerial Fire
WOOD = (0.20, 0.48, 0.27)       # GB/LR - Wood

def tint(rgb, amt=0.6):
    r, g, b = rgb
    return (r + (1 - r) * amt, g + (1 - g) * amt, b + (1 - b) * amt)

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
                    color=BLACK, align="left"):
    set_fill(c, color)
    c.setFont(font, size)
    for ln in wrap_text(text, font, size, max_width):
        if align == "left":
            c.drawString(x, y, ln)
        elif align == "center":
            c.drawCentredString(x + max_width / 2, y, ln)
        y -= leading
    return y

def box(c, x, y, w, h, rgb):
    set_fill(c, rgb)
    c.rect(x, y - h, w, h, stroke=0, fill=1)
    return y - h

def footer(c, meta, page_num, total):
    hairline(c, MARGIN, 34, PAGE_W - MARGIN, rgb=LGRAY, w=0.5)
    set_fill(c, LGRAY)
    c.setFont("Lora-Italic", 7.8)
    c.drawString(MARGIN, 22, meta)
    c.drawRightString(PAGE_W - MARGIN, 22, f"p.{page_num}/{total}")

TOP_OFFSET = 34  # distance from page top to the header bar (independent of side MARGIN)

def section_header(c, letter, title, subtitle=None):
    """Dark navy header bar with a gold left-edge tab, ALL CAPS title."""
    bar_h = 40
    bar_top = PAGE_H - TOP_OFFSET
    set_fill(c, GOLD)
    c.rect(0, bar_top - bar_h, 6, bar_h, stroke=0, fill=1)
    set_fill(c, NAVY)
    c.rect(6, bar_top - bar_h, PAGE_W - 6, bar_h, stroke=0, fill=1)
    set_fill(c, WHITE)
    c.setFont("Lora-Bold", 10.5)
    c.drawString(MARGIN, bar_top - 16, letter)
    c.setFont("Lora-Bold", 14.5)
    c.drawString(MARGIN + 26, bar_top - 27, title.upper())
    y = bar_top - bar_h - 20
    if subtitle:
        set_fill(c, GRAY)
        c.setFont("Lora-Italic", 8.5)
        y = draw_paragraph(c, subtitle, MARGIN, y, CONTENT_W, font="Lora-Italic",
                            size=8.5, leading=11.5, color=GRAY)
        y -= 4
    return y

def purpose_box(c, y, lines, fill=MINT):
    # Pre-wrap all lines first so we can size the box correctly, then draw.
    wrapped = []
    for ln in lines:
        wrapped.extend(wrap_text(ln, "Lora-Italic", 8.3, CONTENT_W - 24))
    h = 14 + len(wrapped) * 12.5
    box(c, MARGIN, y, CONTENT_W, h, fill)
    ty = y - 12
    set_fill(c, (0.30, 0.34, 0.30))
    c.setFont("Lora-Italic", 8.3)
    for ln in wrapped:
        c.drawString(MARGIN + 12, ty, ln)
        ty -= 12.5
    return y - h - 12

def confidence_row(c, y, text):
    """One 'I Can' statement with Pre/Post 1-5 confidence circles."""
    y = draw_paragraph(c, text, MARGIN, y, CONTENT_W, font="Lora", size=9.3,
                        leading=12, color=BLACK)
    y -= 2
    set_fill(c, LGRAY); c.setFont("Lora", 8)
    c.drawString(MARGIN, y, "Pre-Lecture")
    xx = MARGIN + 62
    c.setFont("Lora", 9)
    set_fill(c, BLACK)
    for n in range(1, 6):
        c.drawString(xx, y, str(n))
        xx += 17
    set_fill(c, LGRAY); c.setFont("Lora", 8)
    c.drawString(MARGIN + 300, y, "Post")
    xx = MARGIN + 335
    c.setFont("Lora", 9)
    set_fill(c, BLACK)
    for n in range(1, 6):
        c.drawString(xx, y, str(n))
        xx += 17
    y -= 8
    hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=(0.85, 0.85, 0.82), w=0.6)
    return y - 14

def write_box(c, y, w, h, x=MARGIN, gold_bar=True, fill=CARD_BG, n_lines=0):
    if gold_bar:
        set_fill(c, GOLD)
        c.rect(x, y - h, 3, h, stroke=0, fill=1)
    box(c, x + 3, y, w - 3, h, fill)
    if n_lines:
        ly = y - 16
        for i in range(n_lines):
            hairline(c, x + 12, ly, x + w - 10, rgb=(0.78, 0.72, 0.55), w=0.6)
            ly -= 18
    return y - h

def fill_blank_line(c, text_before, blank_w, text_after, x, y, size=9.3):
    """Draw a connect-the-dots sentence with an underscored blank."""
    c.setFont("Lora", size)
    set_fill(c, BLACK)
    c.drawString(x, y, text_before)
    bw = pdfmetrics.stringWidth(text_before + " ", "Lora", size)
    hairline(c, x + bw, y - 1, x + bw + blank_w, rgb=BLACK, w=0.6)
    c.drawString(x + bw + blank_w + 4, y, text_after)
    return y

def vocab_table_header(c, y):
    set_fill(c, GRAY); c.setFont("Lora-Bold", 8.5)
    c.drawString(MARGIN, y, "PINYIN")
    c.drawString(MARGIN + 190, y, "ENGLISH")
    c.drawString(MARGIN + 340, y, "MY DEFINITION / CLINICAL NOTE")
    y -= 6
    hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=NAVY, w=1)
    return y - 14

def vocab_row(c, y, pinyin, english, shaded):
    if shaded:
        box(c, MARGIN, y + 10, CONTENT_W, 20, CARD_BG)
    set_fill(c, BLACK); c.setFont("Lora", 9)
    c.drawString(MARGIN, y, pinyin)
    c.drawString(MARGIN + 190, y, english)
    hairline(c, MARGIN + 340, y - 3, PAGE_W - MARGIN, rgb=(0.8, 0.8, 0.76), w=0.5)
    return y - 20

def anticipatory_q(c, y, qnum, star, topic, question):
    label = f"Q{qnum}{'*' if star else ''}"
    set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 9.5)
    c.drawString(MARGIN, y, label)
    set_fill(c, BLACK); c.setFont("Lora-Bold", 9)
    c.drawString(MARGIN + 34, y, topic.upper())
    y -= 14
    y = draw_paragraph(c, question, MARGIN + 16, y, CONTENT_W - 16, size=9, leading=12)
    y -= 4
    y = write_box(c, y, CONTENT_W - 16, 20, x=MARGIN + 16, gold_bar=True, fill=CARD_BG)
    return y - 12

def checkpoint_header(c, y, n, item_range):
    set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 10.5)
    c.drawString(MARGIN, y, f"CHECKPOINT {n}  (items {item_range})")
    return y - 16

def checkpoint_item(c, y, num, tag, text):
    set_fill(c, NAVY); c.setFont("Lora-Bold", 9)
    c.drawString(MARGIN, y, str(num))
    set_fill(c, LGRAY); c.setFont("Lora-Italic", 7.3)
    c.drawString(MARGIN + 16, y, tag)
    set_fill(c, BLACK); c.setFont("Lora", 9)
    y2 = draw_paragraph(c, text, MARGIN + 58, y, CONTENT_W - 58, size=9, leading=12)
    return min(y2, y - 12) - 3

def selfcheck_line(c, y, n_items):
    h = 16
    box(c, MARGIN, y, CONTENT_W, h, CARD_BG)
    set_fill(c, GRAY); c.setFont("Lora-Italic", 8)
    c.drawString(MARGIN + 10, y - 11, f"Self-check now (answers below) \u2014 score this block: ___/{n_items} before moving on.")
    return y - h - 10
