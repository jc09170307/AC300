#!/usr/bin/env python3
"""AC300 Comprehensive Final Study Guide (Weeks 1-9, cumulative) -- v2, with figures.
Usage: python3 build_final_studyguide_v2.py <print|remarkable>
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

sys.path.insert(0, '/home/claude/final')
from final_content import (
    NAVY, GOLD, RED, DARK, GRAY, METAL, EARTH, FIRE, WATER, FIREMIN, WOOD, EXTRA, TEAL, AMBER_LUO,
    ZHANG_FINAL_FACTS, TWELVE_MERIDIANS, DIRECTION_RULES, CIRCUITS, HANDOFF_POINTS,
    CHANNEL_META, CHANNEL_ORDER, CHANNEL_CONTENT, FIVE_SHU_DEFINITION, FIVE_SHU_MASTER, FIVE_SHU_COLS, FIVE_SHU_YUAN_NOTE,
    EXTRAORDINARY_VESSELS, CONFLUENT_PAIRS_QUICK, LUO_15, LUO_RULE, LOW_PRIORITY_NOTE,
    DIVERGENT_SUMMARY, SINEW_SUMMARY, CUTANEOUS_SUMMARY, EXAM_TRAPS, WEEKLY_MAP,
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
    W, H = 400, 690   # phone-width page -- "fit to screen" already reads comfortably, no pinch-zoom needed
else:
    W, H = letter

if IS_MOBILE:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.955, 0.958, 0.966)
    CALLOUT_TINT = (0.961, 0.941, 0.918)
    HEADER_H = 46
    COVER_MASTHEAD_H = 70
    HAIRLINE = 0.6
    OUT = "/mnt/user-data/outputs/AC300_Final_StudyGuide_Wk1-9_Mobile.pdf"
    EDLABEL = "Mobile Edition -- reads at 100% zoom, no pinch-zoom needed"
elif IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    CALLOUT_TINT = (0.918, 0.886, 0.816)
    HEADER_H = 51
    COVER_MASTHEAD_H = 86
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Final_StudyGuide_Wk1-9_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    CALLOUT_TINT = (0.961, 0.941, 0.918)
    HEADER_H = 44
    COVER_MASTHEAD_H = 80
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Final_StudyGuide_Wk1-9_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=(W, H))
ML, MR = (16, 16) if IS_MOBILE else (36, 36)
CW = W - ML - MR
page_num = [1]

# Font-size multiplier -- mobile uses noticeably larger absolute point sizes so
# that "fit width" zoom on a phone is already comfortably readable.
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


def block_height(text, font, size, max_width, leading=None):
    leading = leading or size * 1.28
    return len(wrap_words(text, font, size, max_width)) * leading


_img_cache = {}
def img_size(path):
    if path not in _img_cache:
        with Image.open(path) as im:
            _img_cache[path] = im.size
    return _img_cache[path]


def draw_image_fit(path, x, top_y, max_w, max_h, align="center"):
    """Draw image fit within max_w x max_h box whose TOP-LEFT is (x, top_y). Returns height used."""
    iw, ih = img_size(path)
    scale = min(max_w / iw, max_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (max_w - dw) / 2 if align == "center" else x
    dy = top_y - dh
    c.drawImage(path, dx, dy, width=dw, height=dh, preserveAspectRatio=True, mask='auto')
    return dh


def header(subtitle):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    title_size = 12 * FS
    setfill((1, 1, 1)); c.setFont("Lora-Bold", title_size)
    title = "AC300 STUDY GUIDE" if IS_MOBILE else "AC300 FINAL STUDY GUIDE"
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
    foot_text = f"AC300 Final SG (Wk 1-9) \u00b7 {label}" if IS_MOBILE else f"AC300/AC375 Final Study Guide (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  {label}"
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


def section_bar(text, accent=NAVY, sub=""):
    title_size = 13 * FS
    title_lines = wrap_words(text, "Lora-Bold", title_size, CW - 10)
    title_line_h = title_size * 1.15
    sub_line_h = 11 * FS
    sub_inline = False
    sub_fs = 8.5 * FS
    if sub and len(title_lines) == 1:
        title_w = pdfmetrics.stringWidth(title_lines[0], "Lora-Bold", title_size)
        avail = CW - 10 - title_w - 12
        if avail > 60:
            sw = pdfmetrics.stringWidth(sub, "Lora-Italic", sub_fs)
            while sw > avail and sub_fs > 6.0 * FS:
                sub_fs -= 0.5
                sw = pdfmetrics.stringWidth(sub, "Lora-Italic", sub_fs)
            if sw <= avail:
                sub_inline = True
    sub_lines = [] if (sub_inline or not sub) else wrap_words(sub, "Lora-Italic", 8 * FS, CW - 10)

    # Estimate needed space up front (for pagination) -- exact positioning below
    # uses the running pen position, not this estimate, so no mismatch is possible.
    est_h = len(title_lines) * title_line_h + len(sub_lines) * sub_line_h
    ensure_space(est_h + 24 * FS, text)

    bar_top = y[0]
    yy = y[0] - 15 * FS
    setfill(NAVY); c.setFont("Lora-Bold", title_size)
    for ln in title_lines:
        c.drawString(ML + 10, yy, ln)
        yy -= title_line_h
    if sub_inline:
        setfill(GRAY); c.setFont("Lora-Italic", sub_fs)
        c.drawRightString(ML + CW, y[0] - 15 * FS, sub)
    elif sub_lines:
        setfill(GRAY); c.setFont("Lora-Italic", 8 * FS)
        for ln in sub_lines:
            c.drawString(ML + 10, yy, ln)
            yy -= sub_line_h
    # yy is now positioned one line-height below the last line actually drawn --
    # exactly where the rule should go, with a small extra buffer for descenders.
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


def bullet(label, text, accent=NAVY, size=8.6):
    size = size * FS
    if IS_MOBILE:
        lab_lines = wrap_words(label, "Lora-Bold", size, CW - 8)
        txt_lines = wrap_words(text, "Lora", size, CW - 8)
        needed = (len(lab_lines) + len(txt_lines)) * (size * 1.3) + 6
        ensure_space(needed, "")
        setfill(accent); c.rect(ML, y[0] - needed + 6, 3, needed - 6, fill=1, stroke=0)
        yy = y[0]
        setfill(NAVY); c.setFont("Lora-Bold", size)
        for ln in lab_lines:
            c.drawString(ML + 8, yy, ln); yy -= size * 1.3
        setfill(DARK); c.setFont("Lora", size)
        for ln in txt_lines:
            c.drawString(ML + 8, yy, ln); yy -= size * 1.3
        y[0] -= needed
        return
    label_w = 132
    lab_lines = wrap_words(label, "Lora-Bold", size, label_w)
    txt_lines = wrap_words(text, "Lora", size, CW - label_w - 10)
    n = max(len(lab_lines), len(txt_lines))
    needed = n * (size * 1.3) + 6
    ensure_space(needed, "")
    bar_pad = size * 0.8  # shift bar up so its top visually aligns with the text's cap-height, not its baseline
    setfill(accent); c.rect(ML, y[0] - needed + 6 + bar_pad, 3, needed - 6, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", size)
    for ln in lab_lines:
        c.drawString(ML + 8, yy, ln); yy -= size * 1.3
    yy2 = y[0]
    setfill(DARK); c.setFont("Lora", size)
    for ln in txt_lines:
        c.drawString(ML + 8 + label_w, yy2, ln); yy2 -= size * 1.3
    y[0] -= needed


def bullet_line(text, accent=NAVY, size=8.6):
    size = size * FS
    """A single flowing bulleted sentence (no label column) -- for Functions/Indications/Pearls."""
    lines = wrap_words(text, "Lora", size, CW - 16)
    needed = len(lines) * (size * 1.32) + 5
    ensure_space(needed, "")
    setfill(accent); c.circle(ML + 3, y[0] + size * 0.28, 1.8, fill=1, stroke=0)
    setfill(DARK); c.setFont("Lora", size)
    yy = y[0]
    for i, ln in enumerate(lines):
        c.drawString(ML + 12, yy, ln)
        yy -= size * 1.32
    y[0] -= needed


def record_block(title, fields, accent=NAVY, title_size=9.3, field_size=8.0):
    title_size = title_size * FS; field_size = field_size * FS
    """Narrow, phone-friendly replacement for wide (5+ column) tables.
    One record per channel/item: bold title line, then wrapped 'Label: value' pairs
    below, in a single narrow column -- never requires horizontal scrolling."""
    field_text = "   \u00b7   ".join(f"{lab}: {val}" for lab, val in fields)
    field_lines = wrap_words(field_text, "Lora", field_size, CW - 14)
    title_line_h = title_size * 1.4
    field_line_h = field_size * 1.4
    needed = title_line_h + len(field_lines) * field_line_h + 6
    ensure_space(needed, "")
    bar_pad = title_size * 0.8
    setfill(accent); c.rect(ML, y[0] - needed + 6 + bar_pad, 3, needed - 10, fill=1, stroke=0)
    yy = y[0]
    setfill(accent); c.setFont("Lora-Bold", title_size)
    c.drawString(ML + 10, yy, title)
    yy -= title_line_h
    setfill(DARK); c.setFont("Lora", field_size)
    for ln in field_lines:
        c.drawString(ML + 10, yy, ln)
        yy -= field_line_h
    y[0] -= needed


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
            # page broke mid-table -- repeat the header so the continuation
            # page isn't headerless
            draw_header()
        if striped and ridx % 2 == 0:
            row_pad = size * 0.8
            setfill(ROW_TINT); c.rect(ML, y[0] - rh + 3 + row_pad, total_w, rh - 3, fill=1, stroke=0)
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


def callout_box(title, lines, accent=GOLD, size=8.6):
    size = size * FS
    """A box sized dynamically to its content -- never overflows."""
    pad = 10
    title_h = 15
    line_h = size * 1.35
    wrapped = []
    for ln in lines:
        wrapped.extend(wrap_words(ln, "Lora", size, CW - 2 * pad) or [""])
    box_h = pad * 2 + title_h + len(wrapped) * line_h
    ensure_space(box_h + 8, "")
    setfill(CALLOUT_TINT); c.rect(ML, y[0] - box_h, CW, box_h, fill=1, stroke=0)
    setfill(accent); c.rect(ML, y[0] - 4, CW, 4, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + pad, y[0] - pad - 11, title)
    yy = y[0] - pad - 11 - title_h
    setfill(DARK); c.setFont("Lora", size)
    for ln in wrapped:
        c.drawString(ML + pad, yy, ln)
        yy -= line_h
    y[0] -= (box_h + 10)


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
    c.setFont("Lora-Bold", 22); setfill(NAVY)
    for ln in wrap_words("COMPREHENSIVE FINAL STUDY GUIDE", "Lora-Bold", 22, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 26
    yy -= 6
    c.setFont("Lora-BoldItalic", 11); setfill(RED)
    for ln in wrap_words("Weeks 1-9, Cumulative -- with MOA + Lecture Figures", "Lora-BoldItalic", 11, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 15
    yy -= 4
    c.setFont("Lora", 9.5); setfill(DARK)
    for ln in wrap_words("Built around Dr. Zhang's live Final Exam Review -- 30 questions -- reuses quiz material",
                         "Lora", 9.5, CW):
        c.drawCentredString(W / 2, yy, ln); yy -= 13
    yy -= 14
    setstroke(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 60, yy, W / 2 - 15, yy)
    c.line(W / 2 + 15, yy, W / 2 + 60, yy)
    setfill(GOLD); c.circle(W / 2, yy, 2, fill=1, stroke=0)
    yy -= 22

    covers = [
        "All 12 primary meridians -- ID cards + real MOA + CAM channel figures",
        "The 3 Circuits, 24-hr clock, direction rules -- Dr. Zhang's #1 review emphasis",
        "All 8 Extraordinary Vessels with figures + Confluent Point pairs",
        "15 Collaterals + low-priority Divergent/Sinew/Cutaneous summary",
        "Full Five Shu Points master table -- all 60 points",
        "Exam Traps page from every weekly Cram Sheet",
    ]
    box_x, box_w2 = ML, CW
    pad, item_size = 12, 9.3
    wrapped_items = [wrap_words(item, "Lora", item_size, box_w2 - 34) for item in covers]
    box_h2 = pad * 2 + 18 + sum(len(w) for w in wrapped_items) * (item_size * 1.4) + len(covers) * 3
    box_y = yy - box_h2
    setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
    c.rect(box_x, box_y, box_w2, box_h2, fill=1, stroke=0)
    setfill(GOLD); c.rect(box_x, box_y + box_h2 - 4, box_w2, 4, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(box_x + pad, box_y + box_h2 - pad - 11, "This Guide Covers:")
    zz = box_y + box_h2 - pad - 11 - 18
    c.setFont("Lora", item_size); setfill(DARK)
    for wlines in wrapped_items:
        setfill(GOLD); c.circle(box_x + pad + 4, zz + 3, 1.5, fill=1, stroke=0)
        setfill(DARK)
        for ln in wlines:
            c.drawString(box_x + pad + 12, zz, ln)
            zz -= item_size * 1.4
        zz -= 3

    box2_y = box_y - 12 - 44
    setfill((0.961, 0.941, 0.918) if not IS_RM else (0.918, 0.886, 0.816))
    c.rect(box_x, box2_y, box_w2, 44, fill=1, stroke=0)
    setfill(RED); c.rect(box_x, box2_y + 40, box_w2, 4, fill=1, stroke=0)
    c.setFont("Lora-Bold", 9.3); setfill(NAVY)
    for i, ln in enumerate(wrap_words("FINAL EXAM: Week 10 -- 30 Qs -- cumulative, reuses Quiz 1-6", "Lora-Bold", 9.3, box_w2 - 24)):
        c.drawString(box_x + 12, box2_y + 30 - i * 12, ln)

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
    c.drawCentredString(W / 2, by + bs - 22, "WEEK")
    c.setFont("Lora-Bold", 20)
    c.drawCentredString(W / 2, by + 18, "10")

    c.setFont("Lora-Bold", 27); setfill(NAVY)
    c.drawCentredString(W / 2, H - 222, "COMPREHENSIVE FINAL STUDY GUIDE")
    c.setFont("Lora-BoldItalic", 12.5); setfill(RED)
    c.drawCentredString(W / 2, H - 245, "Weeks 1-9, Cumulative -- with MOA + Lecture Figures")
    c.setFont("Lora", 10.5); setfill(DARK)
    c.drawCentredString(W / 2, H - 263, "Built around Dr. Zhang's live Final Exam Review \u00b7 30 questions \u00b7 reuses quiz material")

    setstroke(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 120, H - 277, W / 2 - 40, H - 277)
    c.line(W / 2 + 40, H - 277, W / 2 + 120, H - 277)
    setfill(GOLD); c.circle(W / 2, H - 277, 2.5, fill=1, stroke=0)

    # ---- dynamic "This Guide Covers" box (never overflows) ----
    covers = [
        "All 12 primary meridians -- full ID cards + real MOA (Deadman) channel figures, one per page",
        "The 3 Circuits (Outer/Inner/Middle), 24-hr clock, direction rules -- Dr. Zhang's #1 review emphasis",
        "GV, CV, and all 8 Extraordinary Vessels -- with lecture-sourced vessel figures + Confluent Point pairs",
        "The 15 Collaterals (Luo-Connecting points) + a low-priority summary of Divergent/Sinew/Cutaneous material",
        "Full Five Shu (Transport) Points master table -- all 60 points, all 12 meridians",
        "A dedicated Exam Traps page consolidating every verified fact from every weekly Cram Sheet",
    ]
    box_x, box_w2 = 60, W - 120
    pad, title_h2, item_gap = 14, 20, 3
    item_size = 9.1
    wrapped_items = []
    for item in covers:
        wrapped_items.append(wrap_words(item, "Lora", item_size, box_w2 - 40))
    box_h2 = pad * 2 + title_h2 + sum(len(w) for w in wrapped_items) * (item_size * 1.35) + len(covers) * item_gap
    box_y = H - 300 - box_h2
    setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
    c.rect(box_x, box_y, box_w2, box_h2, fill=1, stroke=0)
    setfill(GOLD); c.rect(box_x, box_y + box_h2 - 4, box_w2, 4, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 11)
    c.drawString(box_x + pad, box_y + box_h2 - pad - 11, "This Guide Covers:")
    yy = box_y + box_h2 - pad - 11 - title_h2
    c.setFont("Lora", item_size); setfill(DARK)
    for wlines in wrapped_items:
        setfill(GOLD); c.circle(box_x + pad + 4, yy + 3, 1.6, fill=1, stroke=0)
        setfill(DARK)
        for ln in wlines:
            c.drawString(box_x + pad + 12, yy, ln)
            yy -= item_size * 1.35
        yy -= item_gap

    # quiz-date / reading box below, with its own gap
    box2_y = box_y - 14 - 50
    setfill((0.961, 0.941, 0.918) if not IS_RM else (0.918, 0.886, 0.816))
    c.rect(box_x, box2_y, box_w2, 50, fill=1, stroke=0)
    setfill(RED); c.rect(box_x, box2_y + 46, box_w2, 4, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(box_x + 14, box2_y + 30, "FINAL EXAM: Week 10  \u00b7  30 questions  \u00b7  cumulative, reuses Quiz 1-6 material")
    c.setFont("Lora", 8.8); setfill(DARK)
    c.drawString(box_x + 14, box2_y + 14, "Per Dr. Zhang, live in Week 9: divergent channels / collaterals detail NOT covered in her review.")

    setstroke(GOLD); c.setLineWidth(1)
    c.line(50, 55, W - 50, 55)
    c.setFont("Lora-Italic", 8.5); setfill(GRAY)
    c.drawCentredString(W / 2, 38, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM \u00b7 Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")
    c.showPage(); page_num[0] += 1

# =====================================================================
# PAGE: WHAT DR. ZHANG SAID
# =====================================================================
new_page("What Dr. Zhang Said Is On The Final")
y[0] = H - HEADER_H - 24
section_bar("WHAT DR. ZHANG SAID IS ON THE FINAL", accent=RED, sub="Sourced directly from the Week 9 live transcript")
for label, text in ZHANG_FINAL_FACTS:
    bullet(label, text, accent=RED, size=8.7)
end_page()

# =====================================================================
# PAGE: MASTER PATHWAY TABLE + CIRCUITS
# =====================================================================
new_page("Master Pathway Table & The 3 Circuits")
y[0] = H - HEADER_H - 24
section_bar("MASTER PATHWAY TABLE -- ALL 12 PRIMARY MERIDIANS", accent=NAVY,
            sub="Dr. Zhang's #1 review emphasis")
para("Narrow record format -- built to read cleanly on any screen, no horizontal scrolling needed.",
     size=7.8, color=GRAY, gap=8)
_pathway_accents = {"Outer / Anterior": METAL, "Inner / Posterior": FIRE, "Middle": FIREMIN}
for a, o, cl, yy_, d, ci, cl2 in TWELVE_MERIDIANS:
    record_block(f"{a} -- {o}",
                 [("Class", cl), ("Y/Y", yy_), ("Direction", d), ("Circuit", ci), ("Clock", cl2)],
                 accent=_pathway_accents.get(ci, NAVY))

section_bar("DIRECTION-OF-FLOW RULES", accent=GOLD)
mini_table(["Rule", "Direction"], DIRECTION_RULES, [0.34 * CW, 0.66 * CW], accent=GOLD, size=8.2)

section_bar("HAND-OFF POINTS BETWEEN CIRCUITS", accent=GOLD)
mini_table(["Transition", "Location", "Example"], HANDOFF_POINTS, [0.26 * CW, 0.17 * CW, 0.57 * CW], accent=GOLD, size=7.8)

section_bar("THE THREE CIRCUITS, DETAILED", accent=NAVY)
for name, pos, chain, poles, accent in CIRCUITS:
    bullet(f"{name} ({pos})", f"{' -> '.join(chain)}   |   {poles}", accent=accent, size=8.3)
end_page()

# ---- SIX DIVISIONS OVERVIEW -- Taiyin/Yangming/Shaoyin/Taiyang/Jueyin/Shaoyang
# tied directly to the 3 circuits (Week 1 lecture deck) ----
new_page("Six Divisions & The 3 Circuits -- Overview")
y[0] = H - HEADER_H - 24
section_bar("SIX DIVISIONS -- TAIYIN/YANGMING/SHAOYIN/TAIYANG/JUEYIN/SHAOYANG", accent=NAVY,
            sub="How the six divisions map onto the 3 circuits")
six_div_path = f"{FIGS}/SIX_DIVISIONS.jpeg"
iw, ih = img_size(six_div_path)
img_h = CW * ih / iw
img_top = y[0]
used_h = draw_image_fit(six_div_path, ML, img_top, CW, img_h)
y[0] = img_top - used_h - 14
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, y[0], "Source: Dr. Zhang's Week 1 lecture deck -- \"Three Main Circuits in the Flow of Qi\"")
y[0] -= 26
para("Each ROW is one circuit (Outer/Anterior, Inner/Posterior, Middle), and each row pairs a Yin division on "
     "the left (Taiyin, Shaoyin, Jueyin) with its Yang partner on the right (Yangming, Taiyang, Shaoyang) -- "
     "exactly the same Yin/Yang channel pairs from the Master Pathway Table, just visualized with the element "
     "colors and hand-off arrows (chest -> hand -> face -> foot -> chest) laid out together.", size=9.5, color=DARK, gap=14)

section_bar("HOW TO READ THIS DIAGRAM", accent=GOLD)
for label, txt in [
    ("Rows = Circuits", "Top row is the Outer/Anterior Circuit, middle row the Inner/Posterior Circuit, bottom "
     "row the Middle Circuit -- the exact same 3 circuits from the Master Pathway Table, in the same order."),
    ("Left column = Yin", "Taiyin (LU/SP), Shaoyin (HT/KI), Jueyin (PC/LR) -- each is the FIRST channel Qi "
     "reaches when a circuit begins at the chest."),
    ("Right column = Yang", "Yangming (LI/ST), Taiyang (SI/BL), Shaoyang (SJ/GB) -- each receives Qi from its "
     "Yin partner at the hand, then carries it up to the face before handing off to the foot."),
    ("Colored arrows = the Five-Phase link", "Metal (LU-LI), Earth (SP-ST), Fire (HT-SI), Water (KI-BL), "
     "Ministerial Fire (PC-SJ), Wood (LR-GB) -- the internal-external pair for each row shares one Element."),
    ("Bottom arrow band", "Chest -> Hands/Fingers -> Face/Head -> Foot/Toes -> Chest -- the SAME 4-stage "
     "hand-off sequence that repeats identically across all 3 circuits, just with different channels."),
]:
    bullet(label, txt, accent=GOLD, size=8.6)
end_page()

# ---- CIRCUIT DIAGRAMS -- real lecture figures (Week 1 deck), one per circuit ----
new_page("Circuit Diagrams -- Anterior / Posterior / Middle")
y[0] = H - HEADER_H - 24
section_bar("CIRCUIT DIAGRAMS -- LECTURE FIGURES", accent=NAVY,
            sub="Each circuit's 4 channels, in sequence")
for circuit_key, circuit_name, accent in [
    ("CIRCUIT_ANTERIOR", "Anterior Circuit -- LU -> LI -> ST -> SP", METAL),
    ("CIRCUIT_POSTERIOR", "Posterior Circuit -- HT -> SI -> BL -> KI", FIRE),
    ("CIRCUIT_MIDDLE", "Middle Circuit -- PC -> SJ -> GB -> LR", FIREMIN),
]:
    img_path = f"{FIGS}/{circuit_key}.jpeg"
    iw, ih = img_size(img_path)
    img_h = CW * ih / iw
    label_h = 16 * FS
    caption_h = 18 * FS
    needed = label_h + img_h + 10 + caption_h
    ensure_space(needed, "Circuit Diagrams -- Anterior / Posterior / Middle")
    setfill(accent); c.setFont("Lora-Bold", 10 * FS)
    c.drawString(ML, y[0], circuit_name)
    y[0] -= label_h
    img_top = y[0]
    used_h = draw_image_fit(img_path, ML, img_top, CW, img_h + 10)
    y[0] = img_top - used_h - 10
    setfill(GRAY); c.setFont("Lora-Italic", 7.2 * FS)
    c.drawCentredString(W / 2, y[0], "Source: Dr. Zhang's Week 1 lecture deck")
    y[0] -= caption_h
end_page()

# =====================================================================
# CHANNEL ID CARDS -- 12 primary meridians, ONE PER PAGE with MOA figure
# =====================================================================
def channel_page(abbr):
    d = CHANNEL_META[abbr]
    cc = CHANNEL_CONTENT[abbr]
    # ---- PAGE A: ID card + Functions + Indications + Highest-Yield + Pearls (all on one dense page) ----
    new_page(f"{abbr} {d['name']} -- Full Reference")
    y[0] = H - HEADER_H - 24
    section_bar(f"{abbr} -- {d['name'].upper()}", accent=d['accent'],
                sub=f"{d['n_points']} pts | {d['element']} | {d['polarity']} | {d['clock']} | {d['direction']}")
    rows = [
        ("Full name", d['full']),
        ("Pertains / Connects", f"{d['pertains']} / {d['connects']}"),
        ("Back-Shu / Front-Mu", f"{d['back_shu']} / {d['front_mu']}"),
        ("Yuan-Source", d['yuan']),
        ("Luo-Connecting", d['luo']),
        ("He-Sea", d['he_sea']),
        ("Xi-Cleft", d['xi_cleft']),
        ("Confluent", d['confluent']),
        ("Command Point", d['command']),
        ("Crossing Points", d['crossing']),
        ("First / Last Point", d['first_last']),
    ]
    mini_table(["Category", "Detail"], rows, [0.24 * CW, 0.76 * CW], accent=d['accent'], size=7.2, header_size=7.4, striped=True)

    section_bar("FUNCTIONS", accent=d['accent'])
    for f in cc['functions']:
        bullet_line(f, accent=d['accent'], size=7.9)

    section_bar("CLINICAL INDICATIONS", accent=d['accent'])
    for ind in cc['indications']:
        bullet_line(ind, accent=d['accent'], size=7.9)

    section_bar("HIGHEST-YIELD POINTS", accent=d['accent'])
    hy_rows = [(p, cat, use) for p, cat, use in cc['highest_yield']]
    mini_table(["Point", "Category", "Clinical Use"], hy_rows, [0.10 * CW, 0.27 * CW, 0.63 * CW], accent=d['accent'], size=7.3, header_size=7.5)

    section_bar("CLINICAL PEARLS & EXAM TRAPS", accent=RED)
    for pearl in cc['pearls']:
        bullet_line(pearl, accent=RED, size=7.9)

    # ---- MOA (internal pathway) figure -- flows onto same page if room remains,
    # otherwise starts fresh. This avoids stranding 1-2 leftover bullets on a
    # near-blank page. ----
    moa_path = f"{FIGS}/MOA_{abbr}.jpeg"
    remaining_h = y[0] - 60
    if remaining_h < 260:
        end_page()
        new_page(f"Channel ID Card -- {abbr} {d['name']} (MOA Internal)")
        y[0] = H - HEADER_H - 24
        remaining_h = y[0] - 60
    section_bar(f"MOA -- INTERNAL PATHWAY (Deadman)", accent=d['accent'],
                sub="Organ-level course: chest/abdomen branches, internal connections")
    cap_h = 14
    img_top = y[0]
    used_h = draw_image_fit(moa_path, ML, img_top, CW, remaining_h - cap_h - 20)
    y[0] = img_top - used_h - cap_h
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, y[0], f"Source: A Manual of Acupuncture (Deadman, 3rd Ed.) -- {d['name']} Meridian")
    end_page()

    # ---- PAGE C: CAM (external surface points) figure ----
    cam_path = f"{FIGS}/CAM_{abbr}.jpeg"
    import os
    if os.path.exists(cam_path):
        new_page(f"Channel Surface Points -- {abbr} {d['name']} (CAM External)")
        y[0] = H - HEADER_H - 24
        section_bar(f"{abbr} -- CAM EXTERNAL POINT MAP", accent=d['accent'],
                    sub="Every point, numbered and located on the body surface")
        img_top = y[0]
        remaining_h = y[0] - 60
        used_h = draw_image_fit(cam_path, ML, img_top, CW, remaining_h - 20)
        y[0] = img_top - used_h - 14
        setfill(GRAY); c.setFont("Lora-Italic", 7.5)
        c.drawCentredString(W / 2, y[0], f"Source: Chinese Acupuncture and Moxibustion (CAM, Cheng Xinnong, 4th Ed.) -- {d['name']} Meridian")
        end_page()


for abbr in CHANNEL_ORDER:
    channel_page(abbr)

# =====================================================================
# EXTRAORDINARY VESSELS -- with lecture figures, 2 per page
# =====================================================================
VESSEL_IMG_MAP = {
    "GV": "VESSEL_GV", "CV": "VESSEL_CV", "Chong": "VESSEL_CHONG", "Dai": "VESSEL_DAI",
    "Yang Qiao": "VESSEL_YANG_QIAO", "Yin Qiao": "VESSEL_YIN_QIAO",
    "Yang Wei": "VESSEL_YANG_WEI", "Yin Wei": "VESSEL_YIN_WEI",
}

new_page("Eight Extraordinary Vessels")
y[0] = H - HEADER_H - 24
section_bar("EIGHT EXTRAORDINARY VESSELS", accent=EXTRA, sub="Week 7 -- confluent points started live in Week 9 review")


def vessel_block(v):
    imgkey = VESSEL_IMG_MAP.get(v['abbr'])
    img_path = f"{FIGS}/{imgkey}.jpeg" if imgkey else None
    npts = f"{v['n_points']} pts" if v['n_points'] else "no own points (except GV/CV)"
    label = f"{v['abbr']} -- {v['name']}"
    detail = (f"{npts} | Sea: {v['sea']} | Confluent: {v['confluent']} (partner: {v['partner']}) | "
              f"Course: {v['course']} | Function: {v['function']}")
    indications = f"Indications: {v['indications']}"
    text_lines = wrap_words(label, "Lora-Bold", 10, CW - 150)
    detail_lines = wrap_words(detail, "Lora", 8.6, CW - 150)
    ind_lines = wrap_words(indications, "Lora", 8.6, CW - 150)
    img_h = 170
    text_block_h = (len(text_lines) * 13 + len(detail_lines) * 11.8 + len(ind_lines) * 11.8) + 14
    needed = max(img_h, text_block_h) + 16
    ensure_space(needed, f"Eight Extraordinary Vessels -- {v['abbr']}")
    top = y[0]
    if img_path:
        draw_image_fit(img_path, ML, top, 138, img_h)
    setfill(v['accent']); c.setFont("Lora-Bold", 10)
    yy = top - 4
    for ln in text_lines:
        c.drawString(ML + 150, yy, ln); yy -= 13
    setfill(DARK); c.setFont("Lora", 8.6)
    yy -= 3
    for ln in detail_lines:
        c.drawString(ML + 150, yy, ln); yy -= 11.8
    yy -= 4
    setfill(NAVY); c.setFont("Lora-BoldItalic", 8.6)
    for i, ln in enumerate(ind_lines):
        c.drawString(ML + 150, yy, ln); yy -= 11.8
    y[0] = top - needed + 6
    setstroke((0.85, 0.85, 0.85)); c.setLineWidth(0.5)
    c.line(ML, y[0] + 4, ML + CW, y[0] + 4)


for v in EXTRAORDINARY_VESSELS:
    vessel_block(v)
end_page()

# =====================================================================
# CONFLUENT POINTS -- with point-location images
# =====================================================================
CONF_IMG_MAP = {
    "SI3 Houxi": "CONF_HOUXI", "BL62 Shenmai": "CONF_SHENMAI",
    "LU7 Lieque": "CONF_LIEQUE", "KI6 Zhaohai": "CONF_ZHAOHAI",
    "SP4 Gongsun": "CONF_GONGSUN", "PC6 Neiguan": "CONF_NEIGUAN",
    "GB41 Zulinqi": "CONF_ZULINQI", "SJ5 Waiguan": "CONF_WAIGUAN",
}

new_page("Confluent Point Pairings -- With Locations")
y[0] = H - HEADER_H - 24
section_bar("EIGHT CONFLUENT POINTS -- LOCATIONS", accent=TEAL, sub="Connect the 8 EVs to the 12 regular meridians")
for a, b, opens, use, note in CONFLUENT_PAIRS_QUICK:
    img_a = CONF_IMG_MAP.get(a)
    img_b = CONF_IMG_MAP.get(b)
    note_lines = wrap_words(note, "Lora-Italic", 8.2, CW - 210)
    row_h = 122
    needed = row_h + 16 + len(note_lines) * 11.5
    ensure_space(needed, "Confluent Point Pairings -- With Locations")
    top = y[0]
    if img_a:
        draw_image_fit(f"{FIGS}/{img_a}.jpeg", ML, top, 110, row_h)
    if img_b:
        draw_image_fit(f"{FIGS}/{img_b}.jpeg", ML + 120, top, 110, row_h)
    setfill(TEAL); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 242, top - 13, f"{a}  +  {b}")
    setfill(NAVY); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML + 242, top - 29, f"Opens: {opens}")
    setfill(DARK); c.setFont("Lora", 8.6)
    for i, ln in enumerate(wrap_words(f"Use: {use}", "Lora", 8.6, CW - 250)):
        c.drawString(ML + 242, top - 45 - i * 11.8, ln)
    y[0] = top - row_h - 8
    setfill(GRAY); c.setFont("Lora-Italic", 8.2)
    for ln in note_lines:
        c.drawString(ML, y[0], ln)
        y[0] -= 11.5
    y[0] -= 10
    setstroke((0.85, 0.85, 0.85)); c.setLineWidth(0.5)
    c.line(ML, y[0] + 6, ML + CW, y[0] + 6)
end_page()

# =====================================================================
# 15 COLLATERALS
# =====================================================================
new_page("15 Collaterals (Luo-Connecting Points)")
y[0] = H - HEADER_H - 24
section_bar("15 COLLATERALS -- LUO-CONNECTING POINTS", accent=AMBER_LUO, sub="Week 8")
mini_table(["Luo Point", "Connection", "Note"], LUO_15, [0.18 * CW, 0.18 * CW, 0.64 * CW], accent=AMBER_LUO, size=7.8)
para(LUO_RULE, size=8.4, color=GRAY)

section_bar("DIVERGENT / SINEW / CUTANEOUS -- LOW PRIORITY FOR THE FINAL", accent=WOOD)
para(LOW_PRIORITY_NOTE, size=8.6, color=RED)
bullet("12 Divergent Channels", DIVERGENT_SUMMARY, accent=WOOD, size=8.3)
bullet("12 Sinew (Muscle) Regions", SINEW_SUMMARY, accent=WOOD, size=8.3)
bullet("12 Cutaneous Regions (-> 6 named)", CUTANEOUS_SUMMARY, accent=WOOD, size=8.3)
end_page()

# =====================================================================
# FIVE SHU MASTER TABLE
# =====================================================================
new_page("Five Shu (Transport) Points -- Master Table")
y[0] = H - HEADER_H - 24
section_bar("FIVE SHU POINTS -- MASTER TABLE (60 POINTS)", accent=NAVY, sub="Week 9 -- all 12 meridians")
para(FIVE_SHU_DEFINITION, size=8.3, color=GRAY)
para("Split into two narrower tables (Jing-Well/Ying-Spring/Shu-Stream, then Jing-River/He-Sea) so neither "
     "requires horizontal scrolling on a phone or tablet.", size=7.8, color=GRAY, gap=8)
section_bar("Jing-Well -> Ying-Spring -> Shu-Stream", accent=NAVY, sub="")
headers_a = ["Meridian"] + FIVE_SHU_COLS[:3]
col_w_a = [96, (CW - 96) // 3, (CW - 96) // 3, (CW - 96) // 3]
rows_a = [[d['m']] + d['pts'][:3] for d in FIVE_SHU_MASTER]
mini_table(headers_a, rows_a, col_w_a, accent=NAVY, size=7.4, header_size=7.6)

section_bar("Jing-River -> He-Sea", accent=NAVY, sub="")
headers_b = ["Meridian"] + FIVE_SHU_COLS[3:]
col_w_b = [96, (CW - 96) // 2, (CW - 96) // 2]
rows_b = [[d['m']] + d['pts'][3:] for d in FIVE_SHU_MASTER]
mini_table(headers_b, rows_b, col_w_b, accent=NAVY, size=7.4, header_size=7.6)
para(FIVE_SHU_YUAN_NOTE, size=8.2, color=GRAY)
end_page()

# =====================================================================
# EXAM TRAPS
# =====================================================================
new_page("Exam Traps -- Consolidated \"Read These Last\"")
y[0] = H - HEADER_H - 24
section_bar("EXAM TRAPS -- CONSOLIDATED FROM EVERY WEEK", accent=RED,
            sub="Read this page last, right before the final")
for label, text in EXAM_TRAPS:
    bullet(label, text, accent=RED, size=8.0)
end_page()

# =====================================================================
# WEEKLY MAP
# =====================================================================
new_page("Course Map -- Weeks 1-10")
y[0] = H - HEADER_H - 24
section_bar("COURSE MAP -- WEEKS 1-10", accent=GOLD, sub="Syllabus reference")
mini_table(["Week", "Topic", "Notes"], WEEKLY_MAP, [0.11 * CW, 0.37 * CW, 0.52 * CW], accent=GOLD, size=8.0)
end_page()

c.save()
print("SAVED:", OUT)
