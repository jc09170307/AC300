#!/usr/bin/env python3
"""AC300 Week 6 Study Guide -- PC, SJ, GB, LR. Classic edition (MOA+CAM figures).
Reuses the Week 4 v3 design system (colored channel cards, pill badges, two-column
meta/pathway pages, point tables, crossing/functions pages). Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

sys.path.insert(0, "/home/claude/work")
from wk6_content import (PC_META, SJ_META, GB_META, LR_META, PC_COURSE, SJ_COURSE,
                          GB_COURSE, LR_COURSE, PC_POINTS, SJ_POINTS, GB_POINTS_GROUPED,
                          LR_POINTS, PC_FUNCTIONS, SJ_FUNCTIONS, GB_FUNCTIONS, LR_FUNCTIONS,
                          CIRCUITS_NOTE, QUIZ4_RECAP)

FIGS_DIR = "/home/claude/work/figs"
FONT_DIR = "/home/claude/work/fonts"

pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.976, 0.965, 0.929)

MINISTER = (0.80, 0.40, 0.36)   # PC/SJ - Ministerial Fire (never purple)
MIN_TINT = (0.976, 0.938, 0.930)
WOOD = (0.20, 0.48, 0.27)       # GB/LR - Wood
WOOD_TINT = (0.925, 0.958, 0.928)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_Week6_StudyGuide_Classic_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week6_StudyGuide_Classic_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


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


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]

WEEK_LABEL = "AC300/AC375 | Week 6 | PC, SJ, GB, LR Channels | VUIM Summer 2026"


def simple_header():
    setfill(DARK); c.setFont("Lora", 9)
    c.drawString(ML, H - 30, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 9)
    c.drawRightString(W - MR, H - 30, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6 * LW_MULT)
    c.line(ML, H - 38, W - MR, H - 38)


def simple_footer():
    setfill(NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora", 8)
    c.drawString(ML, 10, WEEK_LABEL)
    c.drawRightString(W - MR, 10, f"p.{page_num[0]}")


def new_page():
    page_bg()
    simple_header()


def end_page():
    simple_footer()
    c.showPage()
    page_num[0] += 1


_img_size_cache = {}


def get_img_size(fig_key):
    if fig_key not in _img_size_cache:
        with Image.open(f"{FIGS_DIR}/{fig_key}.jpeg") as im:
            _img_size_cache[fig_key] = im.size
    return _img_size_cache[fig_key]


IMG_FOOTER_CLEAR = 45


def draw_image_contain(fig_key, x, y_top, box_w, box_h, border_color):
    iw, ih = get_img_size(fig_key)
    box_h = min(box_h, y_top - IMG_FOOTER_CLEAR)
    scale = min(box_w / iw, box_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (box_w - dw) / 2
    dy = y_top - dh
    setstroke(border_color); c.setLineWidth(0.8)
    c.rect(dx - 3, dy - 3, dw + 6, dh + 6, fill=0, stroke=1)
    c.drawImage(ImageReader(f"{FIGS_DIR}/{fig_key}.jpeg"), dx, dy, width=dw, height=dh)
    return dy


def channel_card(title, subtitle_right, color, pills, y_top=None):
    if y_top is None:
        y_top = H - 46
    bar_h = 30
    setfill(color); c.rect(ML - 4, y_top - bar_h, CW + 8, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1))
    title_size = 14
    sub_w = pdfmetrics.stringWidth(subtitle_right, "Lora-Italic", 9.5) + 14
    max_title_w = CW - sub_w
    while pdfmetrics.stringWidth(title, "Lora-Bold", title_size) > max_title_w and title_size > 9.5:
        title_size -= 0.5
    c.setFont("Lora-Bold", title_size)
    c.drawString(ML + 6, y_top - bar_h + 9, title)
    c.setFont("Lora-Italic", 9.5)
    c.drawRightString(W - MR - 2, y_top - bar_h + 10, subtitle_right)
    y = y_top - bar_h - 2

    if not pills:
        return y - 15
    pill_h = 19
    darker = tuple(max(0, ch - 0.06) for ch in color)
    lighter = tuple(min(1, ch + 0.10) for ch in darker)
    c.setFont("Lora-Bold", 7.6)
    rows = [[]]
    px = ML + 4
    max_pill_w = (W - MR - 4) - (ML + 4) - 12
    for label, val in pills:
        txt = f"{label} {val}"
        tw = pdfmetrics.stringWidth(txt, "Lora-Bold", 7.6) + 12
        if tw > max_pill_w:
            while pdfmetrics.stringWidth(txt + "...", "Lora-Bold", 7.6) + 12 > max_pill_w and len(txt) > 10:
                txt = txt[:-1]
            txt = txt + "..."
            tw = pdfmetrics.stringWidth(txt, "Lora-Bold", 7.6) + 12
        if px + tw > W - MR - 4:
            rows.append([])
            px = ML + 4
        rows[-1].append((txt, tw))
        px += tw + 6
    for row in rows:
        setfill(darker); c.rect(ML - 4, y - pill_h, CW + 8, pill_h, fill=1, stroke=0)
        px = ML + 4
        for txt, tw in row:
            setfill(lighter)
            c.roundRect(px, y - pill_h + 3, tw, pill_h - 6, 5, fill=1, stroke=0)
            setfill((1, 1, 1))
            c.drawString(px + 6, y - pill_h + 6.5, txt)
            px += tw + 6
        y -= pill_h + 1
    return y - 15


def section_bar(y, title, color, size=13):
    bar_h = 24
    setfill(color); c.rect(ML - 4, y - bar_h, CW + 8, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", size)
    c.drawString(ML + 6, y - bar_h + 7, title)
    return y - bar_h - 14


def quote_box(y, lines, color, tint):
    box_h = len(lines) * 12.5 + 12
    setfill(tint); c.rect(ML - 4, y - box_h, CW + 8, box_h, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(2.2)
    c.line(ML - 4, y - box_h, ML - 4, y)
    setfill(DARK); c.setFont("Lora-Italic", 9)
    yy = y - 10
    for l in lines:
        c.drawString(ML + 8, yy, l)
        yy -= 12.5
    return y - box_h - 14


def bullet_list(y, items, color, font="Lora", size=9.5, lh=12.5, max_w=None):
    if max_w is None:
        max_w = CW - 20
    setfill(DARK); c.setFont(font, size)
    for it in items:
        setfill(color); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
        setfill(DARK)
        lines = wrap_words(it, font, size, max_w)
        for i, l in enumerate(lines):
            c.drawString(ML + 14, y - i * lh, l)
        y -= lh * max(1, len(lines))
        y -= 3
    return y


# ============================================================
# COVER (matches Week 2 spec: navy masthead, WEEK badge, title, subtitle,
# gold rule, light-blue "This Week Covers" box, quiz-date box, credit line)
# ============================================================
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 18)
c.drawCentredString(W / 2, H - 48, "AC300/AC375: Acupuncture Channels & Points I")

badge_cx, badge_cy = W / 2, H - 122
setfill((0.898, 0.945, 0.965))
c.roundRect(badge_cx - 34, badge_cy - 34, 68, 68, 8, fill=1, stroke=0)
setfill(GOLD); c.rect(badge_cx - 34, badge_cy - 34, 6, 68, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 7); c.drawCentredString(badge_cx + 3, badge_cy + 14, "WEEK")
c.setFont("Lora-Bold", 22); c.drawCentredString(badge_cx + 3, badge_cy - 10, "6")

y = H - 178
setfill((0.114, 0.227, 0.369)); c.setFont("Lora-Bold", 32)
c.drawCentredString(W / 2, y, "Week 6 Study Guide")
y -= 30
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-BoldItalic", 18)
c.drawCentredString(W / 2, y, "Pericardium, San Jiao, Gallbladder & Liver Channels")
y -= 24
setfill(GRAY); c.setFont("Lora", 11)
c.drawCentredString(W / 2, y, "PC (9) + SJ (23) + GB (44) + LR (14) = 90 Points  \u00b7  Classic Edition (MOA + CAM Figures)")
y -= 20
setstroke(GOLD); c.setLineWidth(1.4)
c.line(ML + 40, y, W - MR - 40, y)
y -= 28

box_h = 168
setfill((0.898, 0.945, 0.965)); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML + 16, y - 22, "This Week Covers:")
setfill(DARK); c.setFont("Lora", 9.5)
bullets = [
    "Full pathway (internal + external) for all 4 channels, verified against Week 6 lecture transcript",
    "Complete point tables with categories: Yuan-Source, Luo, Xi-Cleft, He-Sea, Confluent, Front-Mu, Back-Shu",
    "PC + SJ = zero and 10+ crossing points respectively -- classic exam contrast with GB's unresolved count",
    "GB's confluent point (GB41, Dai Mai) paired with SJ's (SJ5, Yang Wei Mai) -- both new Extraordinary Vessel links",
    "LR3 + LI4 'Four Gates' combination; LR is the only channel reaching the vertex (GV20)",
    "Three Circuits note: this week spans the Middle, Posterior/Inner, and Anterior Circuits",
    "MOA channel figures + CAM color figures for PC, SJ, GB, LR",
]
yy = y - 40
for b in bullets:
    setfill(GOLD); c.circle(ML + 20, yy + 3, 1.6, fill=1, stroke=0)
    lines = wrap_words(b, "Lora", 9.5, CW - 50)
    for i, l in enumerate(lines):
        c.drawString(ML + 30, yy - i * 12, l)
    yy -= 12 * max(1, len(lines)) + 5
y -= box_h + 14

box2_h = 46
setfill((0.898, 0.945, 0.965)); c.rect(ML, y - box2_h, CW, box2_h, fill=1, stroke=0)
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-Bold", 10.5)
c.drawString(ML + 16, y - 20, "Quiz 5 (Week 7): PC + SJ + GB + LR material")
setfill(DARK); c.setFont("Lora", 9)
c.drawString(ML + 16, y - 35, "Reading: CAM p.77-82  \u00b7  MOA p.367-472")
y -= box2_h + 20

setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300 Study Guide \u00b7 Compiled from Dr. Vivian Zhang's lecture + CAM 4th Ed. + Deadman's Manual of Acupuncture")
c.drawCentredString(W / 2, 28, EDLABEL)
c.showPage()
page_num[0] += 1


# ============================================================
# CIRCUITS NOTE PAGE
# ============================================================
new_page()
y = H - 60
y = section_bar(y, "THREE CIRCUITS -- WHERE THIS WEEK FITS", NAVY)
setfill(DARK); c.setFont("Lora", 10)
for l in wrap_words(CIRCUITS_NOTE, "Lora", 10, CW - 10):
    c.drawString(ML, y, l); y -= 14
y -= 10
y = section_bar(y, "QUIZ 4 RECAP (BL/KI material, covered live this week)", GOLD)
setfill(DARK)
for qid, fact, note in QUIZ4_RECAP:
    c.setFont("Lora-Bold", 9.5); c.drawString(ML, y, qid + ":")
    c.setFont("Lora", 9.5)
    lines = wrap_words(fact, "Lora", 9.5, CW - 60)
    c.drawString(ML + 50, y, lines[0])
    y -= 12
    for extra in lines[1:]:
        c.drawString(ML + 50, y, extra); y -= 12
    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    for l in wrap_words(note, "Lora-Italic", 8.5, CW - 60):
        c.drawString(ML + 50, y, l); y -= 11
    setfill(DARK)
    y -= 4
end_page()


# ============================================================
# CHANNEL PAGES
# ============================================================
def meta_pathway_page(name, subtitle, color, tint, meta, course, fig_moa, fig_cam):
    new_page()
    pills = [(k + ":", v) for k, v in meta[:6]]
    y = channel_card(name, subtitle, color, pills)
    y = section_bar(y, "INTERNAL + EXTERNAL RUNNING COURSE", color, size=11.5)
    setfill(DARK); c.setFont("Lora", 9.3)
    for i, step in enumerate(course, 1):
        lines = wrap_words(f"{i}. {step}", "Lora", 9.3, CW - 10)
        for j, l in enumerate(lines):
            c.drawString(ML, y, l); y -= 12
        y -= 2
    end_page()

    new_page()
    y = channel_card(name + " -- Figures & Remaining Categories", subtitle, color, [(k + ":", v) for k, v in meta[6:]])
    half = (CW - 12) / 2
    y2 = draw_image_contain(fig_moa, ML, y, half, 320, color)
    draw_image_contain(fig_cam, ML + half + 12, y, half, 320, color)
    setfill(GRAY); c.setFont("Lora-Italic", 7.8)
    c.drawCentredString(ML + half / 2, y2 - 10, "MOA Channel Figure")
    c.drawCentredString(ML + half + 12 + half / 2, y2 - 10, "CAM Color Figure")
    end_page()


def points_page(name, subtitle, color, tint, points_rows, headers=("Pt", "Pinyin", "Category", "Location / Notes")):
    new_page()
    y = channel_card(name + " -- Point Reference", subtitle, color, [])
    colw = [34, 62, 130, CW - 34 - 62 - 130]
    setfill(color); c.rect(ML - 4, y, CW + 8, 16, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 8)
    x = ML
    for h, w in zip(headers, colw):
        c.drawString(x + 3, y + 4, h); x += w
    y -= 4
    row_i = 0
    for pt, pin, cat, loc in points_rows:
        lines = wrap_words(loc, "Lora", 7.6, colw[3] - 6)
        row_h = max(13, 10 * len(lines) + 4)
        if y - row_h < 55:
            end_page()
            new_page()
            y = channel_card(name + " -- Point Reference (cont.)", subtitle, color, [])
            setfill(color); c.rect(ML - 4, y, CW + 8, 16, fill=1, stroke=0)
            setfill((1, 1, 1)); c.setFont("Lora-Bold", 8)
            x = ML
            for h, w in zip(headers, colw):
                c.drawString(x + 3, y + 4, h); x += w
            y -= 4
            row_i = 0
        bg = tint if row_i % 2 == 0 else (1, 1, 1)
        setfill(bg); c.rect(ML - 4, y - row_h, CW + 8, row_h, fill=1, stroke=0)
        setfill(DARK); c.setFont("Lora-Bold", 7.8)
        c.drawString(ML + 3, y - 9, pt)
        c.setFont("Lora-Italic", 7.6)
        c.drawString(ML + colw[0] + 3, y - 9, pin)
        c.setFont("Lora", 7.2)
        cat_lines = wrap_words(cat, "Lora", 7.2, colw[2] - 6)
        for i, l in enumerate(cat_lines[:2]):
            c.drawString(ML + colw[0] + colw[1] + 3, y - 9 - i * 8.5, l)
        c.setFont("Lora", 7.6)
        for i, l in enumerate(lines):
            c.drawString(ML + colw[0] + colw[1] + colw[2] + 3, y - 9 - i * 10, l)
        y -= row_h
        row_i += 1
    end_page()


def functions_page(name, subtitle, color, tint, functions, extra_title=None, extra_items=None):
    new_page()
    y = channel_card(name + " -- Functions & Key Exam Facts", subtitle, color, [])
    y = bullet_list(y, functions, color, size=9.6, lh=13)
    if extra_items:
        y -= 8
        y = section_bar(y, extra_title, color, size=11)
        y = bullet_list(y, extra_items, color, size=9.3, lh=12.5)
    end_page()


PC_CLINICAL = [
    "Mental/emotional disorders -- PTSD, anxiety, panic attacks (per class discussion: students correctly linked PC to these symptoms from its running course + Heart relationship)",
    "Chest dysfunction -- palpitations, chest oppression, nausea/vomiting; PC6 is the classic point for motion sickness and nausea",
    "Running-course symptoms: stiff neck, flushed face, arm/elbow spasm or pain along the channel",
    "Safety note from lecture: chest points (PC1) are used cautiously (pneumothorax risk); hand/forearm points (PC6, PC7, PC8) are used freely -- 'the safe is very important'",
]
SJ_CLINICAL = [
    "Exterior wind-heat / early-stage common cold -- via SJ5's Yang Wei Mai connection",
    "Ear disorders -- tinnitus, deafness (SJ17, SJ21, SJ19 all cluster around the ear)",
    "Lateral head pain / one-sided headache -- shares this territory with GB; the two Shaoyang channels are often needled together for headache 'on the network side' (lateral) per lecture",
    "San Jiao dysfunction -- abdominal distension, fluid retention/edema, urinary difficulty (governs water passage)",
]

meta_pathway_page("PC \u00b7 Pericardium", "Ministerial Fire", MINISTER, MIN_TINT, PC_META, PC_COURSE, "MOA_PC", "CAM_PC")
points_page("PC \u00b7 Pericardium", "9 points", MINISTER, MIN_TINT, PC_POINTS)
functions_page("PC \u00b7 Pericardium", "Ministerial Fire", MINISTER, MIN_TINT, PC_FUNCTIONS,
               "CLINICAL INDICATIONS (from lecture)", PC_CLINICAL)

meta_pathway_page("SJ \u00b7 San Jiao (Triple Energizer)", "Ministerial Fire", MINISTER, MIN_TINT, SJ_META, SJ_COURSE, "MOA_SJ", "CAM_SJ")
points_page("SJ \u00b7 San Jiao", "23 points", MINISTER, MIN_TINT, SJ_POINTS)
functions_page("SJ \u00b7 San Jiao", "Ministerial Fire", MINISTER, MIN_TINT, SJ_FUNCTIONS,
               "CLINICAL INDICATIONS (from lecture)", SJ_CLINICAL)

meta_pathway_page("GB \u00b7 Gallbladder", "Wood", WOOD, WOOD_TINT, GB_META, GB_COURSE, "MOA_GB", "CAM_GB")
new_page()
y = channel_card("GB \u00b7 Gallbladder -- Point Reference (Selected/Grouped)", "44 points -- Wood", WOOD, [])
setfill(GRAY); c.setFont("Lora-Italic", 8)
for l in wrap_words("GB has 44 points across 3 anatomical zones. Full sequential numbering GB1-GB44 runs head->trunk->leg. High-yield points detailed below; full names for every point are in the reMarkable/print MOA figure.", "Lora-Italic", 8, CW - 10):
    c.drawString(ML, y, l); y -= 10
y -= 8
for zone, pts in GB_POINTS_GROUPED:
    y = section_bar(y, zone, WOOD, size=10.5)
    colw = [50, 70, 120, CW - 50 - 70 - 120]
    for pt, pin, cat, loc in pts:
        lines = wrap_words(loc, "Lora", 7.6, colw[3] - 6)
        row_h = max(13, 10 * len(lines) + 4)
        if y - row_h < 55:
            end_page(); new_page()
            y = channel_card("GB \u00b7 Gallbladder -- Point Reference (cont.)", "44 points -- Wood", WOOD, [])
        bg = WOOD_TINT
        setfill(bg); c.rect(ML - 4, y - row_h, CW + 8, row_h, fill=1, stroke=0)
        setfill(DARK); c.setFont("Lora-Bold", 7.8); c.drawString(ML + 3, y - 9, pt)
        c.setFont("Lora-Italic", 7.4); c.drawString(ML + colw[0] + 3, y - 9, pin)
        c.setFont("Lora", 7.0)
        cat_lines = wrap_words(cat, "Lora", 7.0, colw[2] - 6)
        for i, l in enumerate(cat_lines[:2]):
            c.drawString(ML + colw[0] + colw[1] + 3, y - 9 - i * 8.2, l)
        c.setFont("Lora", 7.4)
        for i, l in enumerate(lines):
            c.drawString(ML + colw[0] + colw[1] + colw[2] + 3, y - 9 - i * 9.6, l)
        y -= row_h
    y -= 6
end_page()
GB_CLINICAL = [
    "Shaoyang syndrome (classic pattern taught this week): alternating fever and chills, bitter taste in the mouth, chest/hypochondriac fullness, nausea, dizziness -- 'specific for Shaoyang', per lecture",
    "Lateral headache/migraine, one-sided head pain -- GB's zigzag head course makes it the primary channel for this presentation",
    "Tendon/sinew disorders -- GB34 as Hui-Meeting point",
    "Jaundice, hypochondriac (rib-side) pain -- Gallbladder organ dysfunction",
]
functions_page("GB \u00b7 Gallbladder", "Wood", WOOD, WOOD_TINT, GB_FUNCTIONS,
               "CLINICAL INDICATIONS (from lecture)", GB_CLINICAL)

meta_pathway_page("LR \u00b7 Liver", "Wood", WOOD, WOOD_TINT, LR_META, LR_COURSE, "MOA_LR", "CAM_LR")
points_page("LR \u00b7 Liver", "14 points", WOOD, WOOD_TINT, LR_POINTS)
LR_CLINICAL = [
    "Vertex headache -- uniquely a Liver-channel presentation (transcript Q&A: 'if patients have a headache in the vertex, we will use Liver channel points')",
    "Menstrual/gynecological disorders -- Liver stores Blood and governs the smooth flow of Qi, central to the reproductive/menstrual cycle",
    "Genital region disorders -- LR channel circles the external genitalia directly",
    "Emotional constraint / irritability -- classic Liver Qi stagnation presentation, treated via LR3",
]
functions_page("LR \u00b7 Liver", "Wood", WOOD, WOOD_TINT, LR_FUNCTIONS,
               "CLINICAL INDICATIONS (from lecture)", LR_CLINICAL)

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0] - 1}")
