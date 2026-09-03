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
    FRONT_MU_TABLE, XI_CLEFT_TABLE, HE_SEA_TABLE,
)

FIGS = '/home/claude/final/figs'
EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter

if IS_RM:
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

c = canvas.Canvas(OUT, pagesize=letter)
ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]


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
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    title = "AC300 MASTER DECODER"
    c.drawString(36, H - HEADER_H + 15, title)
    title_w = pdfmetrics.stringWidth(title, "Lora-Bold", 12)
    avail = (W - 36) - (36 + title_w) - 10
    fs = 9.5
    sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    while sw > avail and fs > 6.5:
        fs -= 0.5
        sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    if avail > 40:
        c.setFont("Lora-Italic", fs)
        c.drawRightString(W - 36, H - HEADER_H + 15, subtitle)


def footer(label):
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(36, 34, W - 36, 34)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Master Special Points Decoder (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  {label}")


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
    tw = pdfmetrics.stringWidth(txt, "Lora-Bold", 8) + 12
    x = ML + CW - tw
    setfill(accent); c.roundRect(x, y[0] - 17, tw, 14, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 8)
    c.drawCentredString(x + tw / 2, y[0] - 13, txt)


def section_bar(text, accent=NAVY, sub="", tier=None):
    ensure_space(34, text)
    setfill(accent); c.rect(ML, y[0] - 20, 3, 18, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 13)
    c.drawString(ML + 10, y[0] - 15, text)
    title_w = pdfmetrics.stringWidth(text, "Lora-Bold", 13)
    avail = CW - 10 - title_w - 12
    if tier:
        tier_label, tier_accent, _ = tier
        tw = pdfmetrics.stringWidth(tier_label, "Lora-Bold", 8) + 12
        if avail > tw:
            tier_chip(tier_label, tier_accent)
    elif sub and avail > 60:
        fs = 8.5
        sw = pdfmetrics.stringWidth(sub, "Lora-Italic", fs)
        while sw > avail and fs > 6.0:
            fs -= 0.5
            sw = pdfmetrics.stringWidth(sub, "Lora-Italic", fs)
        if sw <= avail:
            setfill(GRAY); c.setFont("Lora-Italic", fs)
            c.drawRightString(ML + CW, y[0] - 15, sub)
        else:
            # doesn't fit even at min size -- drop it below the title instead of overlapping
            setfill(GRAY); c.setFont("Lora-Italic", 8)
            c.drawString(ML + 10, y[0] - 30, sub)
            y[0] -= 12
    elif sub:
        # title too long to share the line -- place subtitle on its own line below
        setfill(GRAY); c.setFont("Lora-Italic", 8)
        c.drawString(ML + 10, y[0] - 30, sub)
        y[0] -= 12
    y[0] -= 22
    setstroke(accent); c.setLineWidth(1.2)
    c.line(ML, y[0], ML + CW, y[0])
    y[0] -= 14


def para(text, size=9, font="Lora", color=DARK, indent=0, leading=None, gap=6):
    leading = leading or size * 1.28
    lines = wrap_words(text, font, size, CW - indent)
    ensure_space(len(lines) * leading + gap, "")
    setfill(color); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML + indent, y[0], ln)
        y[0] -= leading
    y[0] -= gap


def mini_table(headers, rows, col_w, accent=NAVY, size=7.8, header_size=8.0, striped=True):
    total_w = sum(col_w)
    needed_header = header_size * 1.9 + 6
    ensure_space(needed_header + 10, "")
    setfill(accent); c.rect(ML, y[0] - needed_header + 3, total_w, needed_header - 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", header_size)
    xx = ML
    for h, w in zip(headers, col_w):
        c.drawString(xx + 4, y[0] - needed_header + 9, h)
        xx += w
    y[0] -= (needed_header + 2)
    for ridx, row in enumerate(rows):
        cell_lines = []
        for cell, w in zip(row, col_w):
            cl = wrap_words(str(cell), "Lora", size, w - 8)
            cell_lines.append(cl if cl else [""])
        nlines = max(len(cl) for cl in cell_lines)
        rh = nlines * (size * 1.35) + 5
        ensure_space(rh, "")
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
    n = len(pairs)
    half = (n + 1) // 2
    col_w = (CW - col_gap) / 2
    left = pairs[:half]
    right = pairs[half:]
    row_h = size * 2.0
    needed = max(len(left), len(right)) * row_h + 10
    ensure_space(needed, "")
    top = y[0]
    for col_idx, col_data in enumerate([left, right]):
        xx = ML + col_idx * (col_w + col_gap)
        yy = top
        for idx, (abbr, val) in enumerate(col_data):
            if idx % 2 == 0:
                setfill(ROW_TINT); c.rect(xx, yy - row_h + 4, col_w, row_h - 4, fill=1, stroke=0)
            setfill(accent); c.setFont("Lora-Bold", size)
            c.drawString(xx + 4, yy - row_h + 12, abbr)
            setfill(DARK); c.setFont("Lora", size)
            c.drawString(xx + 46, yy - row_h + 12, str(val))
            yy -= row_h
    y[0] = top - needed
    y[0] -= 4


# =====================================================================
# COVER
# =====================================================================
page_bg()
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
# FIVE SHU MASTER TABLE (Tier A)
# =====================================================================
new_page("Five Shu (Transport) Points -- Master Table")
y[0] = H - HEADER_H - 24
section_bar("FIVE SHU (TRANSPORT) POINTS -- 60-POINT MASTER TABLE", accent=NAVY, tier=DECODER_TIERS[0])
para(FIVE_SHU_DEFINITION, size=8.6, color=GRAY)
headers = ["Meridian"] + FIVE_SHU_COLS
col_w = [110] + [(CW - 110) // 5] * 5
rows = [[d['m']] + d['pts'] for d in FIVE_SHU_MASTER]
mini_table(headers, rows, col_w, accent=NAVY, size=7.2, header_size=7.6)
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
mini_table(["Luo Point", "Connection", "Note"], LUO_15, [90, 90, CW - 180], accent=AMBER_LUO, size=7.8)
para(LUO_RULE, size=8.4, color=GRAY)
end_page()

# =====================================================================
# BACK-SHU / FRONT-MU (Tier A)
# =====================================================================
new_page("Back-Shu & Front-Mu Points")
y[0] = H - HEADER_H - 24
section_bar("BACK-SHU POINTS -- ORGAN TRANSPORT SERIES (BL13-BL28)", accent=WATER, tier=DECODER_TIERS[0])
mini_table(["Point", "Organ Treated"], BACK_SHU_SERIES, [130, CW - 130], accent=WATER, size=8.2)
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
mini_table(["Point", "Fu Organ", "Use"], LOWER_HE_SEA, [110, 90, CW - 200], accent=FIRE, size=7.8)
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
mini_table(["Point", "Governs Region", "Note"], COMMAND_POINTS_CLASSICAL, [110, 90, CW - 200], accent=GOLD, size=8.0)
para(COMMAND_POINTS_NOTE, size=8.4, color=GRAY)

section_bar("EIGHT HUI-MEETING (INFLUENTIAL) POINTS", accent=WOOD, tier=DECODER_TIERS[2])
mini_table(["Point", "Governs", "Use"], HUI_MEETING_POINTS, [110, 90, CW - 200], accent=WOOD, size=8.0)
para(HUI_MEETING_NOTE, size=8.4, color=GRAY)
end_page()

# =====================================================================
# CROSSING/MEETING POINTS (Tier C)
# =====================================================================
new_page("Crossing / Meeting Points Summary")
y[0] = H - HEADER_H - 24
section_bar("CROSSING (MEETING) POINTS -- BY CHANNEL", accent=GRAY, tier=DECODER_TIERS[2])
mini_table(["Channel", "Count", "Note"], MEETING_CROSSING_SUMMARY, [80, 50, CW - 130], accent=GRAY, size=8.2)
para("Per Dr. Zhang's Week 9 review, deep crossing-point memorization is lower priority than the pathway "
     "and special-point material above -- know the notable counts (ST=11 most, HT/PC=0) rather than every "
     "individual crossing point.", size=8.4, color=RED)
end_page()

# =====================================================================
# CROSS-REFERENCE INDEX -- by channel, all categories at a glance
# =====================================================================
new_page("Cross-Reference Index -- All 12 Channels")
y[0] = H - HEADER_H - 24
section_bar("CROSS-REFERENCE INDEX -- ONE ROW PER CHANNEL", accent=NAVY,
            sub="Every category, side by side -- the fastest lookup in this document")
headers = ["Ch", "Yuan", "Luo", "Xi-Cleft", "He-Sea", "Back-Shu", "Front-Mu", "Confluent/Cmd"]
col_w = [24, 66, 62, 58, 58, 62, 62, 118]
rows = []
for abbr in CHANNEL_ORDER:
    d = CHANNEL_META[abbr]
    conf_cmd = d['confluent'] if d['confluent'] != "none" else d['command']
    conf_cmd = conf_cmd[:44].rstrip(" -") if len(conf_cmd) > 44 else conf_cmd
    rows.append((abbr, d['yuan'], d['luo'], d['xi_cleft'], d['he_sea'], d['back_shu'], d['front_mu'], conf_cmd))
mini_table(headers, rows, col_w, accent=NAVY, size=6.6, header_size=7.0)
end_page()

c.save()
print("SAVED:", OUT)
