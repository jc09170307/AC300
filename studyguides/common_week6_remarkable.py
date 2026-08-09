"""reMarkable Paper Pro edition of the Week 6 PLA v2 design system.
Forked from common_v2.py per the established transformation pattern: ivory background,
thicker hairlines/write-lines for stylus visibility, taller header bars."""
from common_v2 import *  # noqa: F401,F403
from common_v2 import (PAGE_W, PAGE_H, MARGIN, CONTENT_W, NAVY, GOLD, GOLD_DARK, MINT,
                        CARD_BG, GRAY, LGRAY, WHITE, BLACK, MINISTER, WOOD, tint,
                        set_fill, set_stroke, wrap_text, pdfmetrics, box as _box,
                        draw_paragraph as _draw_paragraph)

IVORY = (248/255, 243/255, 230/255)
LW_MULT = 1.35

def ivory_page(c):
    set_fill(c, IVORY)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

def hairline(c, x1, y, x2, rgb=GOLD, w=0.75):
    set_stroke(c, rgb)
    c.setLineWidth(w * LW_MULT)
    c.line(x1, y, x2, y)

def footer(c, meta, page_num, total):
    hairline(c, MARGIN, 34, PAGE_W - MARGIN, rgb=LGRAY, w=0.5)
    set_fill(c, LGRAY)
    c.setFont("Lora-Italic", 7.8)
    c.drawString(MARGIN, 22, meta)
    c.drawRightString(PAGE_W - MARGIN, 22, f"p.{page_num}/{total}")

TOP_OFFSET = 34

def section_header(c, letter, title, subtitle=None):
    bar_h = 44
    bar_top = PAGE_H - TOP_OFFSET
    set_fill(c, GOLD)
    c.rect(0, bar_top - bar_h, 7, bar_h, stroke=0, fill=1)
    set_fill(c, NAVY)
    c.rect(7, bar_top - bar_h, PAGE_W - 7, bar_h, stroke=0, fill=1)
    set_fill(c, WHITE)
    c.setFont("Lora-Bold", 10.5)
    c.drawString(MARGIN, bar_top - 17, letter)
    c.setFont("Lora-Bold", 14.5)
    c.drawString(MARGIN + 26, bar_top - 29, title.upper())
    y = bar_top - bar_h - 20
    if subtitle:
        set_fill(c, GRAY)
        c.setFont("Lora-Italic", 8.5)
        y = _draw_paragraph(c, subtitle, MARGIN, y, CONTENT_W, font="Lora-Italic",
                             size=8.5, leading=11.5, color=GRAY)
        y -= 4
    return y

def purpose_box(c, y, lines, fill=MINT):
    wrapped = []
    for ln in lines:
        wrapped.extend(wrap_text(ln, "Lora-Italic", 8.3, CONTENT_W - 24))
    h = 14 + len(wrapped) * 12.5
    _box(c, MARGIN, y, CONTENT_W, h, fill)
    ty = y - 12
    set_fill(c, (0.30, 0.34, 0.30))
    c.setFont("Lora-Italic", 8.3)
    for ln in wrapped:
        c.drawString(MARGIN + 12, ty, ln)
        ty -= 12.5
    return y - h - 12

def confidence_row(c, y, text):
    y = _draw_paragraph(c, text, MARGIN, y, CONTENT_W, font="Lora", size=9.3,
                         leading=12, color=BLACK)
    y -= 2
    set_fill(c, LGRAY); c.setFont("Lora", 8)
    c.drawString(MARGIN, y, "Pre-Lecture")
    xx = MARGIN + 62
    c.setFont("Lora", 9); set_fill(c, BLACK)
    for n in range(1, 6):
        c.drawString(xx, y, str(n)); xx += 17
    set_fill(c, LGRAY); c.setFont("Lora", 8)
    c.drawString(MARGIN + 300, y, "Post")
    xx = MARGIN + 335
    c.setFont("Lora", 9); set_fill(c, BLACK)
    for n in range(1, 6):
        c.drawString(xx, y, str(n)); xx += 17
    y -= 8
    hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=(0.80, 0.76, 0.60), w=0.6)
    return y - 14

def write_box(c, y, w, h, x=MARGIN, gold_bar=True, fill=CARD_BG, n_lines=0, bar_color=None):
    if gold_bar:
        set_fill(c, bar_color if bar_color is not None else GOLD)
        c.rect(x, y - h, 3, h, stroke=0, fill=1)
    _box(c, x + 3, y, w - 3, h, fill)
    if n_lines:
        ly = y - 16
        for i in range(n_lines):
            hairline(c, x + 12, ly, x + w - 10, rgb=(0.72, 0.64, 0.42), w=0.6)
            ly -= 18
    return y - h

def fill_blank_line(c, text_before, blank_w, text_after, x, y, size=9.3):
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

def vocab_row(c, y, pinyin, english, accent=None):
    if accent is not None:
        _box(c, MARGIN, y + 10, CONTENT_W, 20, tint(accent, 0.82))
    set_fill(c, BLACK); c.setFont("Lora", 9)
    c.drawString(MARGIN, y, pinyin)
    c.drawString(MARGIN + 190, y, english)
    hairline(c, MARGIN + 340, y - 3, PAGE_W - MARGIN, rgb=(0.75, 0.68, 0.50), w=0.5)
    return y - 20

def anticipatory_q(c, y, qnum, star, topic, question, accent=GOLD):
    label = f"Q{qnum}{'*' if star else ''}"
    set_fill(c, accent); c.setFont("Lora-Bold", 9.5)
    c.drawString(MARGIN, y, label)
    set_fill(c, BLACK); c.setFont("Lora-Bold", 9)
    c.drawString(MARGIN + 34, y, topic.upper())
    y -= 14
    y = _draw_paragraph(c, question, MARGIN + 16, y, CONTENT_W - 16, size=9, leading=12)
    y -= 4
    y = write_box(c, y, CONTENT_W - 16, 46, x=MARGIN + 16, gold_bar=True, fill=CARD_BG, n_lines=2, bar_color=accent)
    return y - 12

def draw_element_key(c, y):
    set_fill(c, GRAY); c.setFont("Lora-Bold", 8.5)
    c.drawCentredString(PAGE_W / 2, y, "ELEMENT KEY")
    y -= 20
    entries = [
        (MINISTER, "Fire (Minister)", "PC + SJ"),
        (WOOD, "Wood", "GB + LR"),
    ]
    total_w = 300
    x0 = (PAGE_W - total_w) / 2
    gap = total_w / 2
    for i, (color, label, chans) in enumerate(entries):
        cx = x0 + i * gap
        set_fill(c, color)
        c.circle(cx + 7, y - 4, 6, stroke=0, fill=1)
        set_fill(c, BLACK); c.setFont("Lora-Bold", 9.5)
        c.drawString(cx + 20, y - 1, label)
        set_fill(c, GRAY); c.setFont("Lora-Italic", 8.5)
        c.drawString(cx + 20, y - 13, chans)
    return y - 34

def header_swatch(c, color, label):
    bar_top = PAGE_H - TOP_OFFSET
    w = pdfmetrics.stringWidth(label, "Lora-Bold", 7.5) + 20
    x = PAGE_W - MARGIN - w
    y = bar_top - 29
    set_fill(c, color)
    c.roundRect(x, y - 2, w, 13, 3, stroke=0, fill=1)
    set_fill(c, WHITE); c.setFont("Lora-Bold", 7.5)
    c.drawCentredString(x + w / 2, y + 1.5, label)

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
    y2 = _draw_paragraph(c, text, MARGIN + 58, y, CONTENT_W - 58, size=9, leading=12)
    return min(y2, y - 12) - 3

def selfcheck_line(c, y, n_items):
    h = 16
    _box(c, MARGIN, y, CONTENT_W, h, CARD_BG)
    set_fill(c, GRAY); c.setFont("Lora-Italic", 8)
    c.drawString(MARGIN + 10, y - 11, f"Self-check now (answers below) \u2014 score this block: ___/{n_items} before moving on.")
    return y - h - 10
