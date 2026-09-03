#!/usr/bin/env python3
"""AC300 MASTER SPECIAL POINTS DECODER (Weeks 1-9, cumulative, tiered A/B/C).
Standalone document -- organized BY POINT CATEGORY, not by channel.
Usage: python3 build_final_decoder.py <print|remarkable>
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, '/home/claude/final')
from final_content import (
    NAVY, GOLD, RED, DARK, GRAY, METAL, EARTH, FIRE, WATER, FIREMIN, WOOD, EXTRA, TEAL, AMBER_LUO,
    CHANNEL_META, CHANNEL_ORDER, FIVE_SHU_DEFINITION, FIVE_SHU_MASTER, FIVE_SHU_COLS, FIVE_SHU_YUAN_NOTE,
    EXTRAORDINARY_VESSELS, CONFLUENT_PAIRS_QUICK, LUO_15, LUO_RULE,
    DECODER_TIERS, LOWER_HE_SEA, LOWER_HE_SEA_NOTE, HUI_MEETING_POINTS, HUI_MEETING_NOTE,
    COMMAND_POINTS_CLASSICAL, COMMAND_POINTS_NOTE, MEETING_CROSSING_SUMMARY,
    YUAN_SOURCE_TABLE, LUO_CONNECTING_TABLE, BACK_SHU_SERIES, BACK_SHU_NOTE,
    FRONT_MU_TABLE, XI_CLEFT_TABLE, HE_SEA_TABLE, CATEGORY_DEFINITIONS,
)

FIGS = '/home/claude/final/figs'
EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
IS_MOBILE = EDITION == "mobile"

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

if IS_MOBILE:
    W, H = 400, 690
else:
    W, H = letter

if IS_MOBILE:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.955, 0.958, 0.966)
    CALLOUT_TINT = (0.961, 0.941, 0.918)
    HEADER_H = 46
    COVER_MASTHEAD_H = 70
    HAIRLINE = 0.6
    OUT = "/mnt/user-data/outputs/AC300_Final_MasterDecoder_Wk1-9_Mobile.pdf"
    EDLABEL = "Mobile Edition -- reads at 100% zoom, no pinch-zoom needed"
elif IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    CALLOUT_TINT = (0.918, 0.886, 0.816)
    HEADER_H = 51
    COVER_MASTHEAD_H = 86
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Final_MasterDecoder_Wk1-9_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    CALLOUT_TINT = (0.961, 0.941, 0.918)
    HEADER_H = 44
    COVER_MASTHEAD_H = 80
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Final_MasterDecoder_Wk1-9_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=(W, H))
ML, MR = (16, 16) if IS_MOBILE else (36, 36)
CW = W - ML - MR
page_num = [1]
FS = 1.35 if IS_MOBILE else 1.0


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)
def page_bg(): setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def header(subtitle):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    title_size = 12 * FS
    setfill((1, 1, 1)); c.setFont("Lora-Bold", title_size)
    title = "AC300 DECODER" if IS_MOBILE else "AC300 MASTER DECODER"
    c.drawString(ML, H - HEADER_H + 15, title)
    title_w = pdfmetrics.stringWidth(title, "Lora-Bold", title_size)
    avail = (W - ML) - (ML + title_w) - 10
    fs = 9.5 * FS
    sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    while sw > avail and fs > 6.5:
        fs -= 0.5
        sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    if avail > 40:
        c.setFont("Lora-Italic", fs)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle)


def footer(label):
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, 34, W - ML, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5 * FS)
    foot_text = f"AC300 Decoder (Wk 1-9) \u00b7 {label}" if IS_MOBILE else f"AC300/AC375 Master Special Points Decoder (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  {label}"
    c.drawCentredString(W / 2, 22, foot_text)


def new_page(subtitle):
    page_bg(); header(subtitle)


def end_page():
    footer(f"Page {page_num[0]}")
    c.showPage(); page_num[0] += 1


y = [H]


def ensure_space(needed, subtitle):
    if y[0] - needed < 55:
        end_page()
        new_page(subtitle)
        y[0] = H - HEADER_H - 24


def tier_chip(tier_label, accent):
    """Small inline tier badge drawn at the right edge of a section bar."""
    txt = tier_label
    fs = 8 * FS
    tw = pdfmetrics.stringWidth(txt, "Lora-Bold", fs) + 12
    x = ML + CW - tw
    setfill(accent); c.roundRect(x, y[0] - 17 * FS, tw, 14 * FS, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", fs)
    c.drawCentredString(x + tw / 2, y[0] - 13 * FS, txt)


def section_bar(text, accent=NAVY, sub="", tier=None):
    title_size = 13 * FS
    title_lines = wrap_words(text, "Lora-Bold", title_size, CW - 10)
    title_line_h = title_size * 1.15
    sub_line_h = 11 * FS
    sub_inline = False
    tier_inline = False
    sub_fs = 8.5 * FS
    if len(title_lines) == 1:
        title_w = pdfmetrics.stringWidth(title_lines[0], "Lora-Bold", title_size)
        avail = CW - 10 - title_w - 12
        if tier:
            tw = pdfmetrics.stringWidth(tier[0], "Lora-Bold", 8 * FS) + 12
            if avail > tw:
                tier_inline = True
        elif sub and avail > 60:
            sw = pdfmetrics.stringWidth(sub, "Lora-Italic", sub_fs)
            while sw > avail and sub_fs > 6.0 * FS:
                sub_fs -= 0.5
                sw = pdfmetrics.stringWidth(sub, "Lora-Italic", sub_fs)
            if sw <= avail:
                sub_inline = True
    sub_lines = [] if (tier or sub_inline or not sub) else wrap_words(sub, "Lora-Italic", 8 * FS, CW - 10)

    est_h = len(title_lines) * title_line_h + len(sub_lines) * sub_line_h
    ensure_space(est_h + 24 * FS, text)

    bar_top = y[0]
    yy = y[0] - 15 * FS
    setfill(NAVY); c.setFont("Lora-Bold", title_size)
    for ln in title_lines:
        c.drawString(ML + 10, yy, ln)
        yy -= title_line_h
    if tier and tier_inline:
        tier_label, tier_accent, _ = tier
        tier_chip(tier_label, tier_accent)
    elif sub_inline:
        setfill(GRAY); c.setFont("Lora-Italic", sub_fs)
        c.drawRightString(ML + CW, y[0] - 15 * FS, sub)
    elif sub_lines:
        setfill(GRAY); c.setFont("Lora-Italic", 8 * FS)
        for ln in sub_lines:
            c.drawString(ML + 10, yy, ln)
            yy -= sub_line_h
    y[0] = yy - 2 * FS
    setfill(accent); c.rect(ML, y[0], 3, bar_top - y[0], fill=1, stroke=0)
    setstroke(accent); c.setLineWidth(1.2)
    c.line(ML, y[0], ML + CW, y[0])
    y[0] -= 14 * FS


def para(text, size=9, font="Lora", color=DARK, indent=0, leading=None, gap=6):
    size = size * FS
    leading = leading or size * 1.28
    lines = wrap_words(text, font, size, CW - indent)
    ensure_space(len(lines) * leading + gap, "")
    setfill(color); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML + indent, y[0], ln)
        y[0] -= leading
    y[0] -= gap


def mini_table(headers, rows, col_w, accent=NAVY, size=7.8, header_size=8.0, striped=True):
    size = size * FS; header_size = header_size * FS
    total_w = sum(col_w)
    needed_header = header_size * 1.9 + 6

    def draw_header():
        ensure_space(needed_header + 10, "")
        setfill(accent); c.rect(ML, y[0] - needed_header + 3, total_w, needed_header - 3, fill=1, stroke=0)
        setfill((1, 1, 1)); c.setFont("Lora-Bold", header_size)
        xx = ML
        for h, w in zip(headers, col_w):
            c.drawString(xx + 4, y[0] - needed_header + 9, h)
            xx += w
        y[0] -= (needed_header + 2)

    draw_header()
    for ridx, row in enumerate(rows):
        cell_lines = []
        for cell, w in zip(row, col_w):
            cl = wrap_words(str(cell), "Lora", size, w - 8)
            cell_lines.append(cl if cl else [""])
        nlines = max(len(cl) for cl in cell_lines)
        rh = nlines * (size * 1.35) + 5
        y_before = y[0]
        ensure_space(rh, "")
        if y[0] > y_before:
            draw_header()
        if striped and ridx % 2 == 0:
            setfill(ROW_TINT); c.rect(ML, y[0] - rh + 3, total_w, rh - 3, fill=1, stroke=0)
        xx = ML
        setfill(DARK); c.setFont("Lora", size)
        for cl, w in zip(cell_lines, col_w):
            yy = y[0] - 2
            for ln in cl:
                c.drawString(xx + 4, yy, ln)
                yy -= size * 1.35
            xx += w
        y[0] -= rh
    y[0] -= 6


def two_col_table(pairs, accent=NAVY, size=8.2, col_gap=16):
    """Render a list of (abbr, value) pairs as a 2-column x 6-row grid (for 12-channel data)."""
    size = size * FS
    n = len(pairs)
    half = (n + 1) // 2
    col_w = (CW - col_gap) / 2
    left = pairs[:half]
    right = pairs[half:]
    value_w = col_w - 46
    line_h = size * 1.3

    def lines_for(col_data):
        return [wrap_words(str(val), "Lora", size, value_w) or [""] for _, val in col_data]

    left_lines = lines_for(left)
    right_lines = lines_for(right)
    n_rows = max(len(left), len(right))
    row_hs = []
    for i in range(n_rows):
        l_n = len(left_lines[i]) if i < len(left_lines) else 0
        r_n = len(right_lines[i]) if i < len(right_lines) else 0
        row_hs.append(max(l_n, r_n, 1) * line_h + size * 0.7)
    needed = sum(row_hs) + 10
    ensure_space(needed, "")
    top = y[0]
    for col_idx, (col_data, col_lines) in enumerate([(left, left_lines), (right, right_lines)]):
        xx = ML + col_idx * (col_w + col_gap)
        yy = top
        for idx, (abbr, val) in enumerate(col_data):
            rh = row_hs[idx]
            if idx % 2 == 0:
                setfill(ROW_TINT); c.rect(xx, yy - rh + 3, col_w, rh - 3, fill=1, stroke=0)
            setfill(accent); c.setFont("Lora-Bold", size)
            c.drawString(xx + 4, yy - line_h + 2, abbr)
            setfill(DARK); c.setFont("Lora", size)
            zz = yy - line_h + 2
            for ln in col_lines[idx]:
                c.drawString(xx + 46, zz, ln)
                zz -= line_h
            yy -= rh
    y[0] = top - needed
    y[0] -= 4


def record_block(title, fields, accent=NAVY, title_size=9.3, field_size=8.0):
    """Narrow, phone-friendly replacement for wide (5+ column) tables."""
    title_size = title_size * FS; field_size = field_size * FS
    field_text = "   \u00b7   ".join(f"{lab}: {val}" for lab, val in fields)
    field_lines = wrap_words(field_text, "Lora", field_size, CW - 14)
    title_line_h = title_size * 1.4
    field_line_h = field_size * 1.4
    needed = title_line_h + len(field_lines) * field_line_h + 6
    ensure_space(needed, "")
    setfill(accent); c.rect(ML, y[0] - needed + 6, 3, needed - 10, fill=1, stroke=0)
    yy = y[0]
    setfill(accent); c.setFont("Lora-Bold", title_size)
    c.drawString(ML + 10, yy, title)
    yy -= title_line_h
    setfill(DARK); c.setFont("Lora", field_size)
    for ln in field_lines:
        c.drawString(ML + 10, yy, ln)
        yy -= field_line_h
    y[0] -= needed


# =====================================================================
# COVER
# =====================================================================
page_bg()
if IS_MOBILE:
    setfill(NAVY); c.rect(0, H - COVER_MASTHEAD_H, W, COVER_MASTHEAD_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - COVER_MASTHEAD_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 11)
    c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 38, "AC300/AC375")
    c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 22, EDLABEL)

    yy = H - COVER_MASTHEAD_H - 40
    c.setFont("Lora-Bold", 20); setfill(NAVY)
    for ln in wrap_words("MASTER SPECIAL POINTS DECODER", "Lora-Bold", 20, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 24
    yy -= 6
    c.setFont("Lora-BoldItalic", 10.5); setfill(RED)
    for ln in wrap_words("Every Special-Point Category, Cumulative, Tiered A/B/C", "Lora-BoldItalic", 10.5, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 14
    yy -= 4
    c.setFont("Lora", 9); setfill(DARK)
    for ln in wrap_words("Five Shu - Yuan - Luo - Back-Shu - Front-Mu - Xi-Cleft - He-Sea - Confluent - Command - Hui-Meeting",
                         "Lora", 9, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 12
    yy -= 16
    setstroke(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 50, yy, W / 2 - 15, yy)
    c.line(W / 2 + 15, yy, W / 2 + 50, yy)
    setfill(GOLD); c.circle(W / 2, yy, 2, fill=1, stroke=0)
    yy -= 22

    for label, accent, desc in DECODER_TIERS:
        box_w2 = CW
        desc_lines = wrap_words(desc, "Lora-Italic", 8, box_w2 - 20)
        box_h = 34 + len(desc_lines) * 11
        setfill((0.933, 0.937, 0.949) if not IS_RM else (0.902, 0.878, 0.816))
        c.rect(ML, yy - box_h, box_w2, box_h, fill=1, stroke=0)
        c.setFillColorRGB(*accent); c.rect(ML, yy - 4, box_w2, 4, fill=1, stroke=0)
        c.setFont("Lora-Bold", 11); setfill(NAVY)
        c.drawString(ML + 10, yy - 18, label)
        c.setFont("Lora-Italic", 8); setfill(DARK)
        zz = yy - 32
        for ln in desc_lines:
            c.drawString(ML + 10, zz, ln); zz -= 11
        yy -= box_h + 10

    yy -= 6
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    for ln in wrap_words("This is NOT the weekly Study Guide -- organized BY POINT CATEGORY, not by channel.",
                         "Lora-Italic", 8, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 11

    setstroke(GOLD); c.setLineWidth(1)
    c.line(20, 40, W - 20, 40)
    c.setFont("Lora-Italic", 7.5); setfill(GRAY)
    c.drawCentredString(W / 2, 26, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM")
    c.showPage(); page_num[0] += 1
else:
    setfill(NAVY); c.rect(0, H - COVER_MASTHEAD_H, W, COVER_MASTHEAD_H, fill=1, stroke=0)
    setfill(GOLD)
    if IS_RM:
        c.rect(0, H - COVER_MASTHEAD_H, W, 3, fill=1, stroke=0)
        c.rect(0, H - COVER_MASTHEAD_H - 5, W, 2, fill=1, stroke=0)
    else:
        c.rect(0, H - COVER_MASTHEAD_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
    c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 35, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
    c.setFont("Lora-Italic", 9)
    c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 18, EDLABEL)

    bx, by, bs = W / 2 - 34, H - 160, 68
    setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
    c.rect(bx, by, bs, bs, fill=1, stroke=0)
    setfill(GOLD); c.rect(bx, by + bs - 8, bs, 8, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 7)
    c.drawCentredString(W / 2, by + bs - 22, "DECODER")
    c.setFont("Lora-Bold", 18)
    c.drawCentredString(W / 2, by + 18, "1-9")

    c.setFont("Lora-Bold", 27); setfill(NAVY)
    c.drawCentredString(W / 2, H - 222, "MASTER SPECIAL POINTS DECODER")
    c.setFont("Lora-BoldItalic", 12.5); setfill(RED)
    c.drawCentredString(W / 2, H - 245, "Every Special-Point Category, Cumulative, Tiered A/B/C")
    c.setFont("Lora", 10.5); setfill(DARK)
    c.drawCentredString(W / 2, H - 263, "Five Shu \u00b7 Yuan \u00b7 Luo \u00b7 Back-Shu \u00b7 Front-Mu \u00b7 Xi-Cleft \u00b7 He-Sea \u00b7 Confluent \u00b7 Command \u00b7 Hui-Meeting")

    setstroke(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 120, H - 277, W / 2 - 40, H - 277)
    c.line(W / 2 + 40, H - 277, W / 2 + 120, H - 277)
    setfill(GOLD); c.circle(W / 2, H - 277, 2.5, fill=1, stroke=0)

    box_w, box_h, gap = 155, 62, 12
    total = box_w * 3 + gap * 2
    bx0 = (W - total) / 2
    by0 = H - 380
    for i, (label, accent, desc) in enumerate(DECODER_TIERS):
        x = bx0 + i * (box_w + gap)
        setfill((0.933, 0.937, 0.949) if not IS_RM else (0.902, 0.878, 0.816))
        c.rect(x, by0, box_w, box_h, fill=1, stroke=0)
        c.setFillColorRGB(*accent); c.rect(x, by0 + box_h - 4, box_w, 4, fill=1, stroke=0)
        c.setFont("Lora-Bold", 11)
        c.drawCentredString(x + box_w / 2, by0 + box_h - 20, label)
        c.setFont("Lora-Italic", 7.4); c.setFillColorRGB(*DARK)
        for li, ln in enumerate(wrap_words(desc, "Lora-Italic", 7.4, box_w - 16)):
            c.drawCentredString(x + box_w / 2, by0 + box_h - 33 - li * 9.5, ln)

    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawCentredString(W / 2, by0 - 24, "This is NOT the weekly Study Guide -- it is organized BY POINT CATEGORY, not by channel.")
    c.setFont("Lora", 9); setfill(DARK)
    howto = [
        "Use it to cross-check: \"what are ALL the Yuan-Source points?\" instead of \"what is LU's Yuan-Source?\"",
        "Every category is cross-referenced back to the per-channel ID cards in the Final Study Guide.",
    ]
    yy = by0 - 42
    for line in howto:
        c.drawCentredString(W / 2, yy, line)
        yy -= 13

    setstroke(GOLD); c.setLineWidth(1)
    c.line(50, 55, W - 50, 55)
    c.setFont("Lora-Italic", 8.5); setfill(GRAY)
    c.drawCentredString(W / 2, 38, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM \u00b7 Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")
    c.showPage(); page_num[0] += 1

# =====================================================================
# DEFINITIONS -- what each category actually MEANS (the page that was
# missing entirely from v1)
# =====================================================================
new_page("What Each Point Category Means")
y[0] = H - HEADER_H - 24
section_bar("SPECIAL POINT CATEGORY DEFINITIONS", accent=NAVY,
            sub="Read this page FIRST -- every table after assumes you know these terms")
for name, accent, definition in CATEGORY_DEFINITIONS:
    if IS_MOBILE:
        name_size = 10.5 * FS; def_size = 9 * FS
        lab_lines = wrap_words(name, "Lora-Bold", name_size, CW - 12)
        txt_lines = wrap_words(definition, "Lora", def_size, CW - 12)
        needed = len(lab_lines) * (name_size * 1.3) + len(txt_lines) * (def_size * 1.35) + 12
        ensure_space(needed, "What Each Point Category Means")
        setfill(accent); c.rect(ML, y[0] - needed + 6, 3, needed - 10, fill=1, stroke=0)
        yy = y[0]
        setfill(NAVY); c.setFont("Lora-Bold", name_size)
        for ln in lab_lines:
            c.drawString(ML + 10, yy, ln); yy -= name_size * 1.3
        yy -= 2
        setfill(DARK); c.setFont("Lora", def_size)
        for ln in txt_lines:
            c.drawString(ML + 10, yy, ln); yy -= def_size * 1.35
        y[0] -= needed
        continue
    label_w = 158
    lab_lines = wrap_words(name, "Lora-Bold", 9.3, label_w)
    txt_lines = wrap_words(definition, "Lora", 8.5, CW - label_w - 12)
    n = max(len(lab_lines), len(txt_lines))
    needed = n * 12.2 + 8
    ensure_space(needed, "What Each Point Category Means")
    setfill(accent); c.rect(ML, y[0] - needed + 6, 3, needed - 6, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", 9.3)
    for ln in lab_lines:
        c.drawString(ML + 10, yy, ln); yy -= 12.2
    yy2 = y[0]
    setfill(DARK); c.setFont("Lora", 8.5)
    for ln in txt_lines:
        c.drawString(ML + 10 + label_w, yy2, ln); yy2 -= 12.2
    y[0] -= needed
end_page()

# =====================================================================
# FIVE SHU MASTER TABLE (Tier A)
# =====================================================================
new_page("Five Shu (Transport) Points -- Master Table")
y[0] = H - HEADER_H - 24
section_bar("FIVE SHU (TRANSPORT) POINTS -- 60-POINT MASTER TABLE", accent=NAVY, tier=DECODER_TIERS[0])
para(FIVE_SHU_DEFINITION, size=8.6, color=GRAY)
para("Split into two narrower tables so neither requires horizontal scrolling on a phone or tablet.",
     size=8.0, color=GRAY, gap=8)
section_bar("Jing-Well -> Ying-Spring -> Shu-Stream", accent=NAVY)
headers_a = ["Meridian"] + FIVE_SHU_COLS[:3]
col_w_a = [0.20 * CW, 0.27 * CW, 0.27 * CW, 0.27 * CW]
rows_a = [[d['m']] + d['pts'][:3] for d in FIVE_SHU_MASTER]
mini_table(headers_a, rows_a, col_w_a, accent=NAVY, size=7.4, header_size=7.6)

section_bar("Jing-River -> He-Sea", accent=NAVY)
headers_b = ["Meridian"] + FIVE_SHU_COLS[3:]
col_w_b = [0.20 * CW, 0.40 * CW, 0.40 * CW]
rows_b = [[d['m']] + d['pts'][3:] for d in FIVE_SHU_MASTER]
mini_table(headers_b, rows_b, col_w_b, accent=NAVY, size=7.4, header_size=7.6)
para(FIVE_SHU_YUAN_NOTE, size=8.4, color=GRAY)
end_page()

# =====================================================================
# YUAN-SOURCE (Tier A)
# =====================================================================
new_page("Yuan-Source Points -- All 12")
y[0] = H - HEADER_H - 24
section_bar("YUAN-SOURCE POINTS -- ALL 12 MERIDIANS", accent=NAVY, tier=DECODER_TIERS[0])
two_col_table(YUAN_SOURCE_TABLE, accent=NAVY, size=8.6)
para("On YIN channels, the Yuan-Source point IS the Shu-Stream point (dual role, same point). On YANG "
     "channels, Yuan-Source is a separate 6th point beyond the 5 Shu points.", size=8.6, color=GRAY)

# LUO-CONNECTING (Tier A)
section_bar("LUO-CONNECTING POINTS -- ALL 15", accent=AMBER_LUO, tier=DECODER_TIERS[0])
mini_table(["Luo Point", "Connection", "Note"], LUO_15, [0.18 * CW, 0.18 * CW, 0.64 * CW], accent=AMBER_LUO, size=7.8)
para(LUO_RULE, size=8.4, color=GRAY)
end_page()

# =====================================================================
# BACK-SHU / FRONT-MU (Tier A)
# =====================================================================
new_page("Back-Shu & Front-Mu Points")
y[0] = H - HEADER_H - 24
section_bar("BACK-SHU POINTS -- ORGAN TRANSPORT SERIES (BL13-BL28)", accent=WATER, tier=DECODER_TIERS[0])
mini_table(["Point", "Organ Treated"], BACK_SHU_SERIES, [0.26 * CW, 0.74 * CW], accent=WATER, size=8.2)
para(BACK_SHU_NOTE, size=8.4, color=GRAY)

section_bar("FRONT-MU POINTS -- ALL 12 MERIDIANS", accent=EARTH, tier=DECODER_TIERS[0])
two_col_table(FRONT_MU_TABLE, accent=EARTH, size=8.6)
para("Front-Mu points are scattered across several channels (CV, ST, LR, GB) rather than clustered on one "
     "channel like Back-Shu -- the classic Front-Mu exam trap is assuming a point sits on its own channel "
     "(e.g. ST25 is Front-Mu of LARGE INTESTINE, not Stomach).", size=8.4, color=GRAY)
end_page()

# =====================================================================
# XI-CLEFT / HE-SEA / LOWER HE-SEA (Tier B)
# =====================================================================
new_page("Xi-Cleft, He-Sea & Lower He-Sea Points")
y[0] = H - HEADER_H - 24
section_bar("XI-CLEFT POINTS -- ALL 12 MERIDIANS", accent=FIREMIN, tier=DECODER_TIERS[1])
two_col_table(XI_CLEFT_TABLE, accent=FIREMIN, size=8.6)
para("Xi-Cleft points are the go-to for ACUTE presentations of that channel's pathology (acute pain, acute "
     "bleeding, acute spasm) -- contrast with He-Sea points, used more for chronic/Fu-organ disorders.",
     size=8.4, color=GRAY)

section_bar("HE-SEA POINTS -- ALL 12 MERIDIANS", accent=FIRE, tier=DECODER_TIERS[1])
two_col_table(HE_SEA_TABLE, accent=FIRE, size=8.6)

section_bar("LOWER HE-SEA POINTS -- THE 6 FU ORGANS", accent=FIRE, tier=DECODER_TIERS[1])
mini_table(["Point", "Fu Organ", "Use"], LOWER_HE_SEA, [0.22 * CW, 0.18 * CW, 0.60 * CW], accent=FIRE, size=7.8)
para(LOWER_HE_SEA_NOTE, size=8.4, color=RED)
end_page()

# =====================================================================
# CONFLUENT POINTS (Tier A) -- with images
# =====================================================================
CONF_IMG_MAP = {
    "SI3 Houxi": "CONF_HOUXI", "BL62 Shenmai": "CONF_SHENMAI",
    "LU7 Lieque": "CONF_LIEQUE", "KI6 Zhaohai": "CONF_ZHAOHAI",
    "SP4 Gongsun": "CONF_GONGSUN", "PC6 Neiguan": "CONF_NEIGUAN",
    "GB41 Zulinqi": "CONF_ZULINQI", "SJ5 Waiguan": "CONF_WAIGUAN",
}
from PIL import Image
_img_cache = {}
def img_size(path):
    if path not in _img_cache:
        with Image.open(path) as im:
            _img_cache[path] = im.size
    return _img_cache[path]

def draw_image_fit(path, x, top_y, max_w, max_h):
    iw, ih = img_size(path)
    scale = min(max_w / iw, max_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (max_w - dw) / 2
    dy = top_y - dh
    c.drawImage(path, dx, dy, width=dw, height=dh, preserveAspectRatio=True, mask='auto')
    return dh


new_page("Eight Confluent Points -- With Locations")
y[0] = H - HEADER_H - 24
section_bar("EIGHT CONFLUENT POINTS -- OPEN THE 8 EXTRAORDINARY VESSELS", accent=TEAL, tier=DECODER_TIERS[0])
for a, b, opens, use in CONFLUENT_PAIRS_QUICK:
    img_a = CONF_IMG_MAP.get(a); img_b = CONF_IMG_MAP.get(b)
    if IS_MOBILE:
        img_h = 110 * FS
        use_lines = wrap_words(f"Use: {use}", "Lora", 9 * FS, CW)
        needed = img_h + (3 + len(use_lines)) * 13 * FS + 20
        ensure_space(needed, "Eight Confluent Points -- With Locations")
        top = y[0]
        half_w = (CW - 10) / 2
        if img_a:
            draw_image_fit(f"{FIGS}/{img_a}.jpeg", ML, top, half_w, img_h)
        if img_b:
            draw_image_fit(f"{FIGS}/{img_b}.jpeg", ML + half_w + 10, top, half_w, img_h)
        yy = top - img_h - 8
        setfill(TEAL); c.setFont("Lora-Bold", 10.5 * FS)
        c.drawString(ML, yy, f"{a} + {b}"); yy -= 14 * FS
        setfill(NAVY); c.setFont("Lora-Bold", 9.5 * FS)
        c.drawString(ML, yy, f"Opens: {opens}"); yy -= 13 * FS
        setfill(DARK); c.setFont("Lora", 9 * FS)
        for ln in use_lines:
            c.drawString(ML, yy, ln); yy -= 12.5 * FS
        y[0] = yy - 8
        setstroke((0.85, 0.85, 0.85)); c.setLineWidth(0.5)
        c.line(ML, y[0] + 4, ML + CW, y[0] + 4)
        continue
    row_h = 92
    ensure_space(row_h + 24, "Eight Confluent Points -- With Locations")
    top = y[0]
    if img_a:
        draw_image_fit(f"{FIGS}/{img_a}.jpeg", ML, top, 86, row_h)
    if img_b:
        draw_image_fit(f"{FIGS}/{img_b}.jpeg", ML + 96, top, 86, row_h)
    setfill(TEAL); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 194, top - 12, f"{a}  +  {b}")
    setfill(NAVY); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + 194, top - 28, f"Opens: {opens}")
    setfill(DARK); c.setFont("Lora", 8.4)
    for i, ln in enumerate(wrap_words(f"Use: {use}", "Lora", 8.4, CW - 202)):
        c.drawString(ML + 194, top - 44 - i * 11.5, ln)
    y[0] = top - row_h - 12
    setstroke((0.85, 0.85, 0.85)); c.setLineWidth(0.5)
    c.line(ML, y[0] + 6, ML + CW, y[0] + 6)
end_page()

# =====================================================================
# COMMAND POINTS (Tier B)
# =====================================================================
new_page("Command Points & Hui-Meeting Points")
y[0] = H - HEADER_H - 24
section_bar("FOUR COMMAND POINTS (SI ZONG XUE)", accent=GOLD, tier=DECODER_TIERS[1])
mini_table(["Point", "Governs Region", "Note"], COMMAND_POINTS_CLASSICAL, [0.22 * CW, 0.18 * CW, 0.60 * CW], accent=GOLD, size=8.0)
para(COMMAND_POINTS_NOTE, size=8.4, color=GRAY)

section_bar("EIGHT HUI-MEETING (INFLUENTIAL) POINTS", accent=WOOD, tier=DECODER_TIERS[2])
mini_table(["Point", "Governs", "Use"], HUI_MEETING_POINTS, [0.22 * CW, 0.18 * CW, 0.60 * CW], accent=WOOD, size=8.0)
para(HUI_MEETING_NOTE, size=8.4, color=GRAY)
end_page()

# =====================================================================
# CROSSING/MEETING POINTS (Tier C)
# =====================================================================
new_page("Crossing / Meeting Points Summary")
y[0] = H - HEADER_H - 24
section_bar("CROSSING (MEETING) POINTS -- BY CHANNEL", accent=GRAY, tier=DECODER_TIERS[2])
mini_table(["Channel", "Count", "Note"], MEETING_CROSSING_SUMMARY, [0.16 * CW, 0.10 * CW, 0.74 * CW], accent=GRAY, size=8.2)
para("Per Dr. Zhang's Week 9 review, deep crossing-point memorization is lower priority than the pathway "
     "and special-point material above -- know the notable counts (ST=11 most, HT/PC=0) rather than every "
     "individual crossing point.", size=8.4, color=RED)
end_page()

# =====================================================================
# CROSS-REFERENCE INDEX -- by channel, all categories at a glance
# =====================================================================
new_page("Cross-Reference Index -- All 12 Channels")
y[0] = H - HEADER_H - 24
section_bar("CROSS-REFERENCE INDEX -- ONE RECORD PER CHANNEL", accent=NAVY,
            sub="Every category, in narrow record format -- no horizontal scrolling")
_pivot_accents = {"LU": METAL, "LI": METAL, "ST": EARTH, "SP": EARTH, "HT": FIRE, "SI": FIRE,
                  "BL": WATER, "KI": WATER, "PC": FIREMIN, "SJ": FIREMIN, "GB": WOOD, "LR": WOOD}
for abbr in CHANNEL_ORDER:
    d = CHANNEL_META[abbr]
    conf_cmd = d['confluent'] if d['confluent'] != "none" else d['command']
    record_block(f"{abbr} -- {d['name']}",
                 [("Yuan", d['yuan']), ("Luo", d['luo']), ("Xi-Cleft", d['xi_cleft']),
                  ("He-Sea", d['he_sea']), ("Back-Shu", d['back_shu']), ("Front-Mu", d['front_mu']),
                  ("Confluent/Cmd", conf_cmd)],
                 accent=_pivot_accents.get(abbr, NAVY))
end_page()

c.save()
print("SAVED:", OUT)
