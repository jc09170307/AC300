"""reMarkable Paper Pro edition design system for AC300 Week 6 documents.
Forked from common.py per the established transformation pattern: ivory background,
taller header bars, thicker hairlines/write-lines for stylus visibility, parchment-tinted
callout boxes. Re-fork from the current Print common.py each time rather than maintaining
this independently.
"""
from common import *  # noqa: F401,F403
from common import (PAGE_W, PAGE_H, MARGIN, CONTENT_W, NAVY, GOLD, GOLD_TAB, RED2,
                     LIGHTBLUE, GRAY, LGRAY, WHITE, BLACK, MINISTER, WOOD, tint,
                     set_fill, set_stroke, wrap_text, pdfmetrics)

IVORY = (248/255, 243/255, 230/255)
ROW_TINT = (0.976, 0.960, 0.925)  # warm parchment
LW_MULT = 1.35
RM_TOP_BAR_H = 51

def new_canvas_rm(path):
    return new_canvas(path)

def ivory_page(c):
    set_fill(c, IVORY)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

def hairline_rm(c, x1, y, x2, rgb=GOLD, w=0.75):
    set_stroke(c, rgb)
    c.setLineWidth(w * LW_MULT)
    c.line(x1, y, x2, y)

def draw_paragraph_rm(c, text, x, y, max_width, font="Lora", size=9, leading=12,
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

def header_bar_rm(c, section_letter, title, subtitle=None):
    label = f"Section {section_letter} \u2014 {title}" if section_letter else title
    size = 15
    while pdfmetrics.stringWidth(label, "Lora-Bold", size) > CONTENT_W and size > 9:
        size -= 0.5
    bar_h = RM_TOP_BAR_H if not subtitle else RM_TOP_BAR_H + 16
    set_fill(c, NAVY)
    c.rect(0, PAGE_H - bar_h, PAGE_W, bar_h, stroke=0, fill=1)
    set_fill(c, GOLD_TAB)
    c.rect(0, PAGE_H - bar_h - 4, PAGE_W, 4, stroke=0, fill=1)
    set_fill(c, WHITE)
    c.setFont("Lora-Bold", size)
    c.drawString(MARGIN, PAGE_H - 33, label)
    if subtitle:
        sub_size = 9.5
        while pdfmetrics.stringWidth(subtitle, "Lora-Italic", sub_size) > CONTENT_W and sub_size > 7:
            sub_size -= 0.5
        c.setFont("Lora-Italic", sub_size)
        set_fill(c, (0.78, 0.84, 0.91))
        c.drawString(MARGIN, PAGE_H - 51, subtitle)
    return PAGE_H - bar_h - 24

def footer_rm(c, page_label, page_num):
    hairline_rm(c, MARGIN, 42, PAGE_W - MARGIN, rgb=LGRAY, w=0.5)
    set_fill(c, LGRAY)
    c.setFont("Lora-Italic", 7.5)
    c.drawString(MARGIN, 30, f"AC300/375 \u00b7 Week 6 \u00b7 PC/SJ/GB/LR \u00b7 {page_label}")
    c.drawRightString(PAGE_W - MARGIN, 30, f"p.{page_num}")

def write_lines_rm(c, x, y, width, n=1, gap=26, rgb=GOLD, w=0.6):
    for i in range(n):
        hairline_rm(c, x, y - i * gap, x + width, rgb=rgb, w=w)
    return y - (n - 1) * gap

def numbered_question_rm(c, num, text, x, y, width, lines=1, size=9, leading=12.5,
                          gap=24, font="Lora", label_color=NAVY):
    set_fill(c, label_color)
    c.setFont("Lora-Bold", size)
    num_str = f"{num}."
    c.drawString(x, y, num_str)
    num_w = pdfmetrics.stringWidth(num_str + " ", "Lora-Bold", size)
    y2 = draw_paragraph_rm(c, text, x + num_w, y, width - num_w, font=font,
                            size=size, leading=leading, color=BLACK)
    y2 -= 6
    y2 = write_lines_rm(c, x + 10, y2, width - 10, n=lines, gap=gap)
    return y2 - gap + 4

def tag_badge_rm(c, x, y, label, rgb):
    c.setFont("Lora-Bold", 7.5)
    w = pdfmetrics.stringWidth(label, "Lora-Bold", 7.5) + 10
    set_fill(c, rgb)
    c.roundRect(x, y - 2, w, 12, 2, stroke=0, fill=1)
    set_fill(c, WHITE)
    c.drawCentredString(x + w / 2, y + 1, label)
    return w

def callout_box_rm(c, x, y, w, h, rgb_fill=None):
    set_fill(c, rgb_fill if rgb_fill else ROW_TINT)
    c.rect(x, y - h, w, h, stroke=0, fill=1)
    return y - h
