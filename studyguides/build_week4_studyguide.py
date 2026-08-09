#!/usr/bin/env python3
"""AC300 Week 4 Study Guide - HT & SI. Builds BOTH Print and reMarkable editions."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

FIGS_DIR = "/home/claude/figs_final"

from week4_sg_content import (HT_POINTS, SI_POINTS, HT_COURSE, SI_COURSE, HT_META, SI_META,
                               HT_FUNCTIONS, SI_FUNCTIONS, SYNDROMES_HT, SYNDROMES_SI,
                               HT_HIGHEST_YIELD, SI_HIGHEST_YIELD, HT_FIVE_SHU, SI_FIVE_SHU,
                               CLINICAL_PEARLS_WK4, QUIZ4_FUNDAMENTALS, COMPARISON_HT_SI)

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Week4_StudyGuide_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Week4_StudyGuide_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


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


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]

# Consistent type scale for this document
F_BODY = 10.0
F_BODY_LH = 13.0
F_TABLE = 9.3
F_TABLE_LH = 12.0
F_SMALL = 8.6
F_SMALL_LH = 11.0


def header(subtitle):
    setfill(NAVY)
    c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD)
    c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 11)
    c.drawString(36, H - HEADER_H + 15, "AC300/AC375  |  Week 4  |  HT & SI Channels  |  VUIM Summer 2026")
    c.setFont("Lora-Italic", 9)
    c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer():
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, 34, W - MR, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Week 4 Study Guide  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}  \u00b7  {EDLABEL}")


def new_page(subtitle):
    page_bg()
    header(subtitle)


def end_page():
    footer()
    c.showPage()
    page_num[0] += 1


def section_rule(y, title, width=240, size=12.5):
    setfill(NAVY); c.setFont("Lora-Bold", size)
    c.drawString(ML, y, title)
    y -= 5
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, y, ML + width, y)
    return y - 16


row_num = [0]


_img_size_cache = {}


FOOTER_CLEAR = 56  # reserve above the gold footer rule (y=34) for caption+source+margin

def figure_space_needed(fig_key, max_w, max_h):
    path = f"{FIGS_DIR}/{fig_key}.jpeg"
    if fig_key not in _img_size_cache:
        with Image.open(path) as im:
            _img_size_cache[fig_key] = im.size
    iw, ih = _img_size_cache[fig_key]
    scale = min(max_w / iw, max_h / ih)
    dw, dh = iw * scale, ih * scale
    return dw, dh


def figure_block(y_top, fig_key, caption, source_label, max_w=380, max_h=340):
    """Draws a centered figure with caption+source line, top-anchored at y_top.
    Shrinks to fit whatever vertical space remains above the footer.
    Returns the y position after the block."""
    path = f"{FIGS_DIR}/{fig_key}.jpeg"
    if fig_key not in _img_size_cache:
        with Image.open(path) as im:
            _img_size_cache[fig_key] = im.size
    iw, ih = _img_size_cache[fig_key]
    # cap image height so caption+source+margin still clears the footer
    available_h = max(60, (y_top - FOOTER_CLEAR) - 26)
    eff_max_h = min(max_h, available_h)
    scale = min(max_w / iw, eff_max_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = ML + (CW - dw) / 2
    dy = y_top - dh
    setstroke(GOLD); c.setLineWidth(HAIRLINE)
    c.rect(dx - 4, dy - 4, dw + 8, dh + 8, fill=0, stroke=1)
    c.drawImage(ImageReader(path), dx, dy, width=dw, height=dh)
    y = dy - 14
    setfill(NAVY); c.setFont("Lora-BoldItalic", 9.5)
    c.drawCentredString(W / 2, y, caption)
    y -= 12
    setfill(GRAY); c.setFont("Lora-Italic", 7.8)
    c.drawCentredString(W / 2, y, source_label)
    return y - 10


def def_list(y, rows, col1_w=165):
    for label, val in rows:
        lbl_lines = wrap_words(label, "Lora-Bold", F_BODY, col1_w - 6)
        val_lines = wrap_words(val, "Lora", F_BODY, CW - col1_w - 6)
        n = max(len(lbl_lines), len(val_lines))
        row_h = n * F_BODY_LH
        if row_num[0] % 2 == 0:
            setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 9, CW + 8, row_h, fill=1, stroke=0)
        row_num[0] += 1
        setfill(NAVY); c.setFont("Lora-Bold", F_BODY)
        for i, l in enumerate(lbl_lines):
            c.drawString(ML, y - i * F_BODY_LH, l)
        setfill(DARK); c.setFont("Lora", F_BODY)
        for i, l in enumerate(val_lines):
            c.drawString(ML + col1_w, y - i * F_BODY_LH, l)
        y -= row_h
    return y


# ============= PAGE 1: COVER =============
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 80, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - 45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 62, EDLABEL)

bx, by, bs = W / 2 - 34, H - 165, 68
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD); c.rect(bx, by + bs - 8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 8)
c.drawCentredString(W / 2, by + bs - 24, "WEEK")
c.setFont("Lora-Bold", 26)
c.drawCentredString(W / 2, by + 16, "4")

c.setFont("Lora-Bold", 26); setfill(NAVY)
c.drawCentredString(W / 2, H - 227, "Week 4 Study Guide")
c.setFont("Lora-BoldItalic", 14); setfill(RED)
c.drawCentredString(W / 2, H - 252, "Heart & Small Intestine Channels")
c.setFont("Lora", 11); setfill(DARK)
c.drawCentredString(W / 2, H - 270, "HT (9 pts) + SI (19 pts) = 28 Points")

y = H - 310
setfill(NAVY); c.setFont("Lora-Bold", 11.5)
c.drawCentredString(W / 2, y, "This Document Contains:")
y -= 20
setfill(DARK); c.setFont("Lora", 10.5)
for b in [
    "Full internal & external running course for HT and SI, with MOA pathway figures",
    "Complete point-location table for all 28 points, with CAM color figures",
    "SI's crossing points detailed (HT has none - unique feature)",
    "Syndromes, high-yield points, and Five-Shu tables",
    "Dr. Zhang's Clinical Pearls direct from lecture",
    "Quiz 4 Fundamentals + HT vs SI comparison table",
]:
    c.drawCentredString(W / 2, y, b)
    y -= 15

y -= 16
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
box_w = 480
c.rect(W / 2 - box_w / 2, y - 62, box_w, 62, fill=1, stroke=0)
setfill(RED); c.setFont("Lora-Bold", 10)
c.drawCentredString(W / 2, y - 19, "QUIZ 4 (next class) covers: HT & SI channels")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawCentredString(W / 2, y - 35, "MIDTERM (Week 5) covers Weeks 1-4 cumulative")
c.drawCentredString(W / 2, y - 50, "MOA: HT pp.208-221 | SI pp.222-249  \u00b7  CAM: Deadman, HT/SI chapters")

y -= 92
setstroke(GOLD); c.setLineWidth(1)
c.line(50, y, W - 50, y)
y -= 22
c.setFont("Lora-Italic", 9); setfill(GRAY)
c.drawCentredString(W / 2, y, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's lectures, CAM (Deadman), MOA (Deadman 3rd)")

end_page()


def channel_meta_page(name, subtitle_full, meta_rows, course_beats, functions,
                       moa_key=None, moa_caption=None, moa_source=None):
    row_num[0] = 0
    new_page(f"{name} \u2014 {subtitle_full}  \u00b7  {EDLABEL}")
    y = H - HEADER_H - 26
    setfill(NAVY); c.setFont("Lora-Bold", 17)
    c.drawString(ML, y, f"{name} Meridian of {subtitle_full}")
    y -= 20
    y = section_rule(y, "Channel Attributes")
    y = def_list(y, meta_rows)
    y -= 16
    y = section_rule(y, "Internal & External Running Course")
    setfill(DARK); c.setFont("Lora", F_BODY)
    for i, beat in enumerate(course_beats, 1):
        lines = wrap_words(beat, "Lora", F_BODY, CW - 24)
        setfill(RED); c.setFont("Lora-Bold", F_BODY)
        c.drawString(ML, y, f"{i}")
        setfill(DARK); c.setFont("Lora", F_BODY)
        for j, l in enumerate(lines):
            c.drawString(ML + 20, y - j * F_BODY_LH, l)
        y -= len(lines) * F_BODY_LH + 6
    y -= 10
    y = section_rule(y, "Functions & Key Notes")
    setfill(DARK); c.setFont("Lora", F_BODY)
    for f in functions:
        lines = wrap_words("\u2022 " + f, "Lora", F_BODY, CW - 4)
        for l in lines:
            c.drawString(ML, y, l)
            y -= F_BODY_LH
        y -= 3

    if moa_key:
        y -= 8
        # if under ~230pt remains, the image would be squashed - start a fresh page for it
        if y - FOOTER_CLEAR < 230:
            end_page()
            row_num[0] = 0
            new_page(f"{name} \u2014 {subtitle_full}  \u00b7  {EDLABEL}")
            y = H - HEADER_H - 30
        y = section_rule(y, "Channel Pathway (MOA)", width=220, size=12.5)
        figure_block(y, moa_key, moa_caption, moa_source, max_w=400, max_h=560)

    end_page()


channel_meta_page("Heart", "Hand-Shaoyin (HT)", HT_META, HT_COURSE, HT_FUNCTIONS,
                   moa_key="MOA_HT", moa_caption="MOA \u2014 Heart Channel (primary pathway)",
                   moa_source="Manual of Acupuncture (Deadman), 3rd Ed. \u00b7 Heart Channel, p.209")
channel_meta_page("Small Intestine", "Hand-Taiyang (SI)", SI_META, SI_COURSE, SI_FUNCTIONS,
                   moa_key="MOA_SI", moa_caption="MOA \u2014 Small Intestine Channel (primary pathway)",
                   moa_source="Manual of Acupuncture (Deadman), 3rd Ed. \u00b7 Small Intestine Channel, p.227")


def location_table_page(name, abbrev, points, five_shu, extra_note=None,
                         cam_key=None, cam_caption=None, cam_source=None):
    row_num[0] = 0
    new_page(f"{name} ({abbrev})  \u2014  Point Locations  \u00b7  {EDLABEL}")
    y = H - HEADER_H - 26
    y = section_rule(y, f"{name} ({abbrev})  \u2014  Full Point-Location Table", width=320, size=13)
    setfill(NAVY); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y, "Pt"); c.drawString(ML + 42, y, "Chinese"); c.drawString(ML + 140, y, "Location & Notes")
    y -= 14
    setfill(DARK); c.setFont("Lora", F_TABLE)
    for pt, py, loc in points:
        lines = wrap_words(loc, "Lora", F_TABLE, CW - 140)
        row_h = len(lines) * F_TABLE_LH
        if row_num[0] % 2 == 0:
            setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
        row_num[0] += 1
        setfill(RED); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, pt)
        setfill(NAVY); c.setFont("Lora-Italic", F_TABLE); c.drawString(ML + 42, y, py)
        setfill(DARK); c.setFont("Lora", F_TABLE)
        for i, l in enumerate(lines):
            c.drawString(ML + 140, y - i * F_TABLE_LH, l)
        y -= row_h
    y -= 8
    if extra_note:
        lines = wrap_words(extra_note, "Lora-Italic", F_SMALL, CW - 4)
        setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
        for l in lines:
            c.drawString(ML, y, l)
            y -= F_SMALL_LH
        y -= 10

    y = section_rule(y, "Five-Shu (Antique) Points", width=240, size=12.5)
    setfill(NAVY); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y, "Shu Point"); c.drawString(ML + 100, y, "Element"); c.drawString(ML + 170, y, "Pt"); c.drawString(ML + 310, y, "Clinical Use")
    y -= 14
    for shu, elem, pt, use in five_shu:
        lines = wrap_words(use, "Lora", F_TABLE, CW - 310)
        row_h = len(lines) * F_TABLE_LH
        if row_num[0] % 2 == 0:
            setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
        row_num[0] += 1
        setfill(DARK); c.setFont("Lora", F_TABLE)
        c.drawString(ML, y, shu); c.drawString(ML + 100, y, elem); c.drawString(ML + 170, y, pt)
        for i, l in enumerate(lines):
            c.drawString(ML + 310, y - i * F_TABLE_LH, l)
        y -= row_h

    if cam_key:
        y -= 14
        if y - FOOTER_CLEAR < 230:
            end_page()
            row_num[0] = 0
            new_page(f"{name} ({abbrev})  \u2014  Point Locations  \u00b7  {EDLABEL}")
            y = H - HEADER_H - 30
        y = section_rule(y, "Channel Figure (CAM)", width=220, size=12.5)
        figure_block(y, cam_key, cam_caption, cam_source, max_w=380, max_h=560)

    end_page()


location_table_page("Heart", "HT", HT_POINTS, HT_FIVE_SHU,
                     extra_note="CAM (Deadman): Heart Channel, pp.209-221. Locations cross-verified against source text (HE1, HE2, HE9 confirmed via direct OCR extraction).",
                     cam_key="CAM_HT", cam_caption="CAM \u2014 Heart Meridian of Hand-Shaoyin (color figure)",
                     cam_source="CAM (Deadman) \u00b7 Col. Fig. 6, p.209")
location_table_page("Small Intestine", "SI", SI_POINTS, SI_FIVE_SHU,
                     extra_note="CAM (Deadman): Small Intestine Channel, pp.222-249. Locations cross-verified against source text (SI1, SI4, SI8, SI15, SI16 confirmed via direct OCR extraction).",
                     cam_key="CAM_SI", cam_caption="CAM \u2014 Small Intestine Meridian of Hand-Taiyang (color figure)",
                     cam_source="CAM (Deadman) \u00b7 Col. Fig. 7, p.227")


def syndromes_page(name, abbrev, syn, high_yield, extra_boxes=None):
    row_num[0] = 0
    new_page(f"{abbrev}  \u2014  Syndromes & High-Yield Points  \u00b7  {EDLABEL}")
    y = H - HEADER_H - 26
    y = section_rule(y, f"{abbrev}  \u2014  Syndromes & High-Yield Points", width=300, size=13)
    col_w = (CW - 24) / 2
    top_y = y
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML, y, "A. External Course Symptoms")
    y -= 15
    setfill(DARK); c.setFont("Lora", F_TABLE)
    for s in syn['external']:
        lines = wrap_words(s, "Lora", F_TABLE, col_w - 4)
        for l in lines:
            c.drawString(ML, y, l); y -= F_TABLE_LH
        y -= 4
    left_bottom = y

    y2 = top_y
    x2 = ML + col_w + 24
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(x2, y2, f"B. Internal Organ ({name})")
    y2 -= 15
    setfill(DARK); c.setFont("Lora", F_TABLE)
    for s in syn['internal']:
        lines = wrap_words(s, "Lora", F_TABLE, col_w - 4)
        for l in lines:
            c.drawString(x2, y2, l); y2 -= F_TABLE_LH
        y2 -= 4
    right_bottom = y2
    y = min(left_bottom, right_bottom) - 12

    lines = wrap_words(syn['note'], "Lora-Italic", F_SMALL, CW - 4)
    setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
    for l in lines:
        c.drawString(ML, y, l); y -= F_SMALL_LH
    y -= 14

    y = section_rule(y, f"High-Yield {abbrev} Points", width=220, size=12.5)
    setfill(NAVY); c.setFont("Lora-Bold", F_TABLE)
    c.drawString(ML, y, "Pt"); c.drawString(ML + 42, y, "Category"); c.drawString(ML + 190, y, "Key Indications")
    y -= 14
    for pt, cat, use in high_yield:
        lines = wrap_words(use, "Lora", F_TABLE, CW - 190)
        row_h = len(lines) * F_TABLE_LH
        if row_num[0] % 2 == 0:
            setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
        row_num[0] += 1
        setfill(RED); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, pt)
        setfill(NAVY); c.setFont("Lora-Italic", 8.8); c.drawString(ML + 42, y, cat)
        setfill(DARK); c.setFont("Lora", F_TABLE)
        for i, l in enumerate(lines):
            c.drawString(ML + 190, y - i * F_TABLE_LH, l)
        y -= row_h
    y -= 10

    if extra_boxes:
        y = section_rule(y, extra_boxes['title'], width=280, size=12.5)
        setfill(DARK); c.setFont("Lora", F_BODY)
        for l in extra_boxes['lines']:
            for ll in wrap_words(l, "Lora", F_BODY, CW - 4):
                c.drawString(ML, y, ll); y -= F_BODY_LH

    end_page()


syndromes_page("Heart", "HT", SYNDROMES_HT, HT_HIGHEST_YIELD, extra_boxes=dict(
    title="Quick Notes \u2014 HT",
    lines=[
        "HT is the smallest channel (9 pts) but the clinical center of gravity for Shen (mind/spirit) disturbance.",
        "Because HT has zero crossing points, every HT symptom traces directly back to the Heart or its own pathway - there's no 'borrowed' symptom picture from another channel to confuse it with.",
    ]))

# SI crossing points detailed page (HT has none, so only SI gets this page) - merged with syndromes
row_num[0] = 0
new_page(f"SI  \u2014  Crossing Points & Syndromes  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "SI \u2014 The 2 Crossing Points (Detailed)", width=300, size=13)
setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
note_lines = wrap_words(
    "Dr. Zhang: HT has zero crossing points. SI crosses only twice, both on its facial branch near the eye and forehead - "
    "far fewer than ST (11) or SP (6), but still tested.", "Lora-Italic", F_SMALL, CW - 4)
for l in note_lines:
    c.drawString(ML, y, l); y -= F_SMALL_LH
y -= 14

crossing_detail = [
    ("BL1 Jingming", "Bridge of the Nose / Inner Canthus",
     "Inner canthus of the eye, ~0.1 cun above the medial canthus.",
     "SI's ascending facial branch crosses BL here en route toward the eye. Treats all eye disorders: redness, pain, "
     "myopia, night blindness. Same crossing point used by the ST and BL channels themselves."),
    ("GB14 Yangbai", "Forehead",
     "1 cun above the midpoint of the eyebrow, directly above the pupil.",
     "SI's branch also crosses GB14 as it continues toward the forehead. Used for frontal headache, eyebrow pain, "
     "eyelid twitching, and eye disorders."),
]
for pt, loc_title, loc, clinical in crossing_detail:
    setfill(RED); c.setFont("Lora-Bold", 11)
    c.drawString(ML, y, f"{pt} \u2014 {loc_title}")
    y -= 15
    setfill(NAVY); c.setFont("Lora-Bold", F_BODY)
    c.drawString(ML, y, "Location: ")
    setfill(DARK); c.setFont("Lora", F_BODY)
    loc_lines = wrap_words(loc, "Lora", F_BODY, CW - 62)
    c.drawString(ML + 60, y, loc_lines[0])
    y -= F_BODY_LH
    for extra in loc_lines[1:]:
        c.drawString(ML + 60, y, extra); y -= F_BODY_LH
    setfill(NAVY); c.setFont("Lora-Bold", F_BODY)
    c.drawString(ML, y, "Clinical: ")
    setfill(DARK); c.setFont("Lora", F_BODY)
    cl_lines = wrap_words(clinical, "Lora", F_BODY, CW - 62)
    c.drawString(ML + 60, y, cl_lines[0])
    y -= F_BODY_LH
    for extra in cl_lines[1:]:
        c.drawString(ML + 60, y, extra); y -= F_BODY_LH
    y -= 16

y = section_rule(y, "Why SI Has So Few Crossing Points", width=260, size=12.5)
setfill(DARK); c.setFont("Lora", F_BODY)
for l in wrap_words(
    "Unlike ST (11 crossings, mostly facial) or SP (6 crossings, mostly abdominal), SI's pathway is largely "
    "self-contained along the arm and shoulder, only crossing other channels once it reaches the face. "
    "Combined with HT's zero crossings, this Fire pair is the most 'independent' pairing covered so far.",
    "Lora", F_BODY, CW - 4):
    c.drawString(ML, y, l); y -= F_BODY_LH

end_page()

syndromes_page("Small Intestine", "SI", SYNDROMES_SI, SI_HIGHEST_YIELD, extra_boxes=dict(
    title="Quick Notes \u2014 SI",
    lines=[
        "SI has more than double HT's points (19 vs. 9) - the same Yin/Yang point-count pattern seen with LU(11)/LI(20).",
        "SI's Lower He-Sea is ST39, located on the STOMACH channel - a frequent point of confusion on exams.",
    ]))

# ============= CLINICAL PEARLS =============
row_num[0] = 0
new_page(f"Dr. Zhang's Clinical Pearls  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Dr. Zhang's Clinical Pearls \u2014 Direct from Lecture", width=360, size=13)
setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
c.drawString(ML, y, "Highest exam probability")
y -= 18
for title, body in CLINICAL_PEARLS_WK4:
    lines_t = wrap_words(title, "Lora-Bold", 10.5, CW - 4)
    lines_b = wrap_words(body, "Lora", F_BODY, CW - 4)
    needed = len(lines_t) * 13.5 + len(lines_b) * F_BODY_LH + 12
    if y - needed < 50:
        end_page()
        row_num[0] = 0
        new_page(f"Dr. Zhang's Clinical Pearls (cont.)  \u00b7  {EDLABEL}")
        y = H - HEADER_H - 26
    setfill(RED); c.setFont("Lora-Bold", 10.5)
    for l in lines_t:
        c.drawString(ML, y, l); y -= 13.5
    setfill(DARK); c.setFont("Lora", F_BODY)
    for l in lines_b:
        c.drawString(ML, y, l); y -= F_BODY_LH
    y -= 10
end_page()

# ============= QUIZ 4 FUNDAMENTALS =============
row_num[0] = 0
new_page(f"Quiz 4 Fundamentals  \u00b7  {EDLABEL}")
y = H - HEADER_H - 26
y = section_rule(y, "Quiz 4 Fundamentals \u2014 Distribution, Circuits & Nomenclature", width=400, size=13)
setfill(GRAY); c.setFont("Lora-Italic", F_SMALL)
c.drawString(ML, y, "From Dr. Zhang's review slides")
y -= 18

col_w = (CW - 24) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Distribution of the 12 Main Meridians")
y -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['distribution']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(ML, y, ll); y -= F_TABLE_LH
left_bottom = y

y2 = top_y
x2 = ML + col_w + 24
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "Circulation of the 12 Meridians")
y2 -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['circulation']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(x2, y2, ll); y2 -= F_TABLE_LH
right_bottom = y2
y = min(left_bottom, right_bottom) - 16

y = section_rule(y, "Circuit Connections \u2014 exactly what links to what (exam trap)", width=430, size=12.5)
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['circuit_connections']:
    for ll in wrap_words(l, "Lora", F_TABLE, CW - 4):
        c.drawString(ML, y, ll); y -= F_TABLE_LH
y -= 14

top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Nomenclature")
y -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['nomenclature']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(ML, y, ll); y -= F_TABLE_LH
left_bottom = y

y2 = top_y
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "Meridian Clock \u2014 HT & SI peak times")
y2 -= 15
setfill(DARK); c.setFont("Lora", F_TABLE)
for l in QUIZ4_FUNDAMENTALS['clock']:
    for ll in wrap_words(l, "Lora", F_TABLE, col_w - 4):
        c.drawString(x2, y2, ll); y2 -= F_TABLE_LH
right_bottom = y2
y = min(left_bottom, right_bottom) - 16

setfill(RED); c.setFont("Lora-BoldItalic", 10)
for l in wrap_words(QUIZ4_FUNDAMENTALS['homework_rule'], "Lora-BoldItalic", 10, CW - 4):
    c.drawString(ML, y, l); y -= 13

y -= 20
setstroke(GOLD); c.setLineWidth(HAIRLINE)
c.line(ML, y, ML + CW, y)
y -= 22

# ============= COMPARISON TABLE (merged onto same page if room) =============
comparison_needed = 30 + 15 + len(COMPARISON_HT_SI) * 13.5 + 20
if y < comparison_needed + 50:
    end_page()
    row_num[0] = 0
    new_page(f"HT vs SI \u2014 Quick Reference  \u00b7  {EDLABEL}")
    y = H - HEADER_H - 26

y = section_rule(y, "HT vs SI \u2014 Quick Reference Comparison", width=320, size=13)
setfill(NAVY); c.setFont("Lora-Bold", F_TABLE)
c.drawString(ML, y, "Attribute"); c.drawString(ML + 135, y, "HT  |  Heart (Hand Shaoyin)"); c.drawString(ML + 350, y, "SI  |  Small Intestine (Hand Taiyang)")
y -= 15
for attr, ht_val, si_val in COMPARISON_HT_SI:
    if row_num[0] % 2 == 0:
        setfill(ROW_TINT); c.rect(ML - 4, y - 8, CW + 8, 13.5, fill=1, stroke=0)
    row_num[0] += 1
    setfill(NAVY); c.setFont("Lora-Bold", F_TABLE); c.drawString(ML, y, attr)
    setfill(DARK); c.setFont("Lora", F_TABLE)
    c.drawString(ML + 135, y, ht_val)
    c.drawString(ML + 350, y, si_val)
    y -= 13.5

end_page()

c.save()
print("SAVED:", OUT)
