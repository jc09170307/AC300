#!/usr/bin/env python3
"""AC300 Week 4 Cram Sheet - HT & SI. 4pp night-before density sheet.
Matches Week 3 Cram Sheet design exactly. Builds Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from week4_sg_content import (HT_POINTS, SI_POINTS, HT_COURSE, SI_COURSE, HT_META, SI_META,
                               HT_HIGHEST_YIELD, SI_HIGHEST_YIELD, HT_FIVE_SHU, SI_FIVE_SHU)

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.976, 0.965, 0.929)

HT_COLOR = (0.627, 0.220, 0.180)
HT_TINT = (0.976, 0.928, 0.919)
SI_COLOR = (0.784, 0.353, 0.294)
SI_TINT = (0.983, 0.948, 0.938)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    OUT = "/mnt/user-data/outputs/AC300_Week4_CramSheet_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week4_CramSheet_Print.pdf"
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
            if cur: lines.append(cur)
            cur = wd
    if cur: lines.append(cur)
    return lines


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]
F_SMALL = 8.3
F_SMALL_LH = 10.6

WEEK_LABEL = "AC300/AC375 | Week 4 Cram Sheet | HT & SI | VUIM Summer 2026"


def simple_header():
    setfill(DARK); c.setFont("Lora", 9)
    c.drawString(ML, H - 30, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 9)
    c.drawRightString(W - MR, H - 30, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6)
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


def channel_title(text, subtitle_right, color):
    y = H - 60
    setfill(color); c.setFont("Lora-Bold", 15)
    c.drawString(ML, y, text)
    setfill(color); c.setFont("Lora-Italic", 10)
    c.drawRightString(W - MR, y, subtitle_right)
    y -= 10
    setstroke(GOLD); c.setLineWidth(1)
    c.line(ML, y, W - MR, y)
    return y - 22


def box_header(x, y, w, title, color):
    setfill(color); c.rect(x, y - 15, w, 15, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawString(x + 5, y - 11.5, title)
    return y - 15 - 8


def id_card(x, y, w, rows, color):
    y = box_header(x, y, w, "Channel ID Card", color)
    setfill(DARK); c.setFont("Lora", F_SMALL)
    for label, val in rows:
        setfill(NAVY); c.setFont("Lora-Bold", F_SMALL)
        c.drawString(x, y, label)
        setfill(DARK); c.setFont("Lora", F_SMALL)
        lines = wrap_words(val, "Lora", F_SMALL, w - 120)
        c.drawString(x + 118, y, lines[0])
        y -= F_SMALL_LH
        for extra in lines[1:]:
            c.drawString(x + 118, y, extra)
            y -= F_SMALL_LH
    return y - 6


def pathway_8beats(x, y, w, title, beats, color):
    y = box_header(x, y, w, title, color)
    setfill(DARK); c.setFont("Lora", F_SMALL)
    for i, beat in enumerate(beats, 1):
        lines = wrap_words(beat, "Lora", F_SMALL, w - 16)
        setfill(color); c.setFont("Lora-Bold", F_SMALL)
        c.drawString(x, y, f"{i}.")
        setfill(DARK); c.setFont("Lora", F_SMALL)
        c.drawString(x + 14, y, lines[0])
        y -= F_SMALL_LH
        for extra in lines[1:]:
            c.drawString(x + 14, y, extra)
            y -= F_SMALL_LH
    return y - 4


def five_shu_table(x, y, w, five_shu, color, tint):
    y = box_header(x, y, w, "Five-Shu (Antique) Points", color)
    col2, col3 = 100, 175
    setfill(tint); c.rect(x, y - 12, w, 12, fill=1, stroke=0)
    setfill(color); c.setFont("Lora-Bold", F_SMALL)
    c.drawString(x + 2, y - 9.5, "Shu Point"); c.drawString(x + col2, y - 9.5, "Element"); c.drawString(x + col3, y - 9.5, "Pt")
    y -= 15
    for i, (shu, elem, pt, use) in enumerate(five_shu):
        if i % 2 == 0:
            setfill(tint); c.rect(x, y - 9, w, 12, fill=1, stroke=0)
        setfill(DARK); c.setFont("Lora", F_SMALL)
        pt_short = pt.split(" (")[0]
        c.drawString(x + 2, y - 6.5, shu); c.drawString(x + col2, y - 6.5, elem); c.drawString(x + col3, y - 6.5, pt_short)
        y -= 12
    return y - 6


def two_col_table(x, y, w, title, headers, col_widths, rows, color, tint):
    y = box_header(x, y, w, title, color)
    setfill(tint); c.rect(x, y - 12, w, 12, fill=1, stroke=0)
    setfill(color); c.setFont("Lora-Bold", F_SMALL)
    cx = x + 2
    for h_, cw_ in zip(headers, col_widths):
        c.drawString(cx, y - 9.5, h_)
        cx += cw_
    y -= 15
    row_i = 0
    for row in rows:
        cell_lines = [wrap_words(str(cell), "Lora", F_SMALL, col_widths[i] - 4) for i, cell in enumerate(row)]
        n = max(len(cl) for cl in cell_lines)
        row_h = n * F_SMALL_LH
        if row_i % 2 == 0:
            setfill(tint); c.rect(x, y - row_h + 2, w, row_h, fill=1, stroke=0)
        row_i += 1
        cx = x
        for i, cl in enumerate(cell_lines):
            setfill(color if i == 0 else DARK)
            c.setFont("Lora-Bold" if i == 0 else "Lora", F_SMALL)
            for j, l in enumerate(cl):
                c.drawString(cx + 2, y - j * F_SMALL_LH - 8, l)
            cx += col_widths[i]
        y -= row_h
    return y - 6


def callout_box(x, y, w, title, lines, color, tint):
    y = box_header(x, y, w, title, color)
    box_lines = []
    for l in lines:
        box_lines.extend(wrap_words(l, "Lora", F_SMALL, w - 12))
        box_lines.append("")  # spacer between bullets
    if box_lines and box_lines[-1] == "":
        box_lines.pop()
    box_h = len(box_lines) * F_SMALL_LH + 10
    setfill(tint); c.rect(x, y - box_h, w, box_h, fill=1, stroke=0)
    yy = y - 10
    setfill(DARK); c.setFont("Lora", F_SMALL)
    for l in box_lines:
        if l:
            c.drawString(x + 4, yy, l)
        yy -= F_SMALL_LH
    return y - box_h - 8


# ============================================================
# PAGE 1: COVER
# ============================================================
page_bg()
simple_header()
y = H - 90
setfill(GOLD); c.setFont("Lora-Bold", 11)
c.drawCentredString(W / 2, y, "WEEK 4")
y -= 46
setfill(NAVY); c.setFont("Lora-Bold", 30)
c.drawCentredString(W / 2, y, "CRAM SHEET")
y -= 22
setfill(HT_COLOR); c.setFont("Lora-BoldItalic", 15)
c.drawCentredString(W / 2, y, "Heart & Small Intestine Channels")
y -= 26
setstroke(GOLD); c.setLineWidth(1)
c.line(W / 2 - 190, y, W / 2 + 190, y)
y -= 22
setfill(GOLD); c.setFont("Lora-Italic", 11)
c.drawCentredString(W / 2, y, "HT (9 pts) + SI (19 pts) = 28 Points")
y -= 20
setfill(HT_COLOR); c.setFont("Lora-Italic", 10.5)
c.drawCentredString(W / 2, y, "Quiz 4 Ready  |  HT & SI Channels")

y -= 50
box_w, box_h, gap = 155, 62, 12
bx = W / 2 - (3 * box_w + 2 * gap) / 2
boxes = [
    ("Special Points", "HT7, SI3, SI4", "and all categories"),
    ("Five-Shu Tables", "Both HT and SI", "Well to Sea sequences"),
    ("Crossing Points", "HT 0, SI 2", "zero vs. facial branch"),
]
for title, l1, l2 in boxes:
    setfill((0.94, 0.94, 0.95)); c.rect(bx, y - box_h, box_w, box_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawCentredString(bx + box_w / 2, y - 20, title)
    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawCentredString(bx + box_w / 2, y - 34, l1)
    c.drawCentredString(bx + box_w / 2, y - 46, l2)
    bx += box_w + gap

y -= box_h + 30
setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawCentredString(W / 2, y, "+ Dr. Zhang's Clinical Pearls   +   HT & SI Crossing Points   +   Posterior Circuit Begins")

y -= 60
setstroke(GOLD); c.setLineWidth(1)
c.line(70, y, W - 70, y)
y -= 22
setfill(GRAY); c.setFont("Lora", 9.5)
c.drawCentredString(W / 2, y, "AC300/AC375 | Acupuncture Channels & Points I | VUIM Summer 2026")
y -= 15
c.drawCentredString(W / 2, y, "Dr. Vivian Zhang, Ph.D. | Jon Centeno | D.AcHM Candidate | VUIM")

end_page()


# ============================================================
# PAGE 2: HEART
# ============================================================
new_page()
y = channel_title("HEART  -  Hand Shaoyin", "9 points  |  Yin  |  Fire  |  11 AM-1 PM  |  Chest to Hand", HT_COLOR)

col_gap = 20
col_w = (CW - col_gap) / 2
lx, rx = ML, ML + col_w + col_gap
top_y = y

ID_ROWS_HT = [
    ("Full name", "Heart Meridian of Hand-Shaoyin"),
    ("Points / Clock", "9 pts | 11 AM-1 PM"),
    ("Element / Polarity", "Fire | Yin"),
    ("Direction", "Chest -> Hand (interior/medial)"),
    ("Pertains / Connects", "Heart / Small Intestine"),
    ("Back-Shu / Front-Mu", "BL15 Xinshu / CV14 Juque"),
    ("Yuan-Source", "HT7 Shenmen"),
    ("Luo-Connecting", "HT5 Tongli"),
    ("Xi-Cleft", "HT6 Yinxi"),
    ("He-Sea", "HT3 Shaohai"),
    ("Crossing points", "0 - the ONLY channel with none"),
    ("First / Last", "HT1 Jiquan / HT9 Shaochong"),
]
ly = id_card(lx, top_y, col_w, ID_ROWS_HT, HT_COLOR)
ly = pathway_8beats(lx, ly, col_w, "Pathway in 8 Beats", HT_COURSE, HT_COLOR)
ly = five_shu_table(lx, ly, col_w, HT_FIVE_SHU, HT_COLOR, HT_TINT)

ry = callout_box(rx, top_y, col_w,
    "HT has ZERO Crossing Points",
    ["This is a genuinely unique, exam-critical fact: HT is the only one of the 12 primary "
     "channels with no crossing (jiaohui) points anywhere on its external pathway.",
     "Because of this, every HT symptom traces directly back to the Heart itself or its own "
     "pathway - there is no 'borrowed' symptom picture from another channel to confuse it with."],
    HT_COLOR, HT_TINT)
ry = two_col_table(rx, ry, col_w, "Highest-Yield Points", ["Pt", "Category", "Use"], [42, 118, col_w - 160],
    [(pt, cat, use) for pt, cat, use in HT_HIGHEST_YIELD], HT_COLOR, HT_TINT)

end_page()


# ============================================================
# PAGE 3: SMALL INTESTINE
# ============================================================
new_page()
y = channel_title("SMALL INTESTINE  -  Hand Taiyang", "19 points  |  Yang  |  Fire  |  1-3 PM  |  Hand to Head", SI_COLOR)

top_y = y
ID_ROWS_SI = [
    ("Full name", "Small Intestine Meridian of Hand-Taiyang"),
    ("Points / Clock", "19 pts | 1-3 PM"),
    ("Element / Polarity", "Fire | Yang"),
    ("Direction", "Hand -> Head (posterolateral)"),
    ("Pertains / Connects", "Small Intestine / Heart"),
    ("Back-Shu / Front-Mu", "BL27 Xiaochangshu / CV4 Guanyuan"),
    ("Yuan-Source", "SI4 Wangu"),
    ("Luo-Connecting", "SI7 Zhizheng"),
    ("Xi-Cleft", "SI6 Yanglao"),
    ("He-Sea", "SI8 Xiaohai"),
    ("Confluent", "SI3 - opens Du Mai (w/ BL62)"),
    ("Crossing points", "2 - BL1, GB14 (facial branch)"),
    ("First / Last", "SI1 Shaoze / SI19 Tinggong"),
]
ly = id_card(lx, top_y, col_w, ID_ROWS_SI, SI_COLOR)
ly = pathway_8beats(lx, ly, col_w, "Pathway in 8 Beats", SI_COURSE, SI_COLOR)
ly = five_shu_table(lx, ly, col_w, SI_FIVE_SHU, SI_COLOR, SI_TINT)

SI_CROSSING_ROWS = [
    ("BL1", "Jingming", "inner canthus of eye; all eye disorders"),
    ("GB14", "Yangbai", "forehead; frontal headache, eyebrow pain"),
]
ry = two_col_table(rx, top_y, col_w, "The 2 Crossing Points", ["Pt", "Pinyin", "Why it matters"], [38, 68, col_w - 106],
    SI_CROSSING_ROWS, SI_COLOR, SI_TINT)
ry = two_col_table(rx, ry, col_w, "Highest-Yield Points", ["Pt", "Category", "Use"], [42, 118, col_w - 160],
    [(pt, cat, use) for pt, cat, use in SI_HIGHEST_YIELD], SI_COLOR, SI_TINT)

end_page()


# ============================================================
# PAGE 4: RAPID RECALL
# ============================================================
new_page()
y = H - 60
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, "Rapid Recall  -  HT & SI")
setfill(GRAY); c.setFont("Lora-Italic", 10)
c.drawRightString(W - MR, y, "Read this one last, on the way in")
y -= 10
setstroke(GOLD); c.setLineWidth(1)
c.line(ML, y, W - MR, y)
y -= 22
top_y = y

ONLY_LIST = [
    ("ONLY channel with ZERO crossing points", "HT"),
    ("Fewest points of any primary channel (9)", "HT"),
    ("ONLY Confluent point this week (opens Du Mai)", "SI3"),
    ("SI's Lower He-Sea sits on a DIFFERENT channel", "ST39"),
    ("Emergency point: revives consciousness, severe heart pain", "HT9"),
    ("Point specifically noted for lactation problems", "SI1"),
]
ly = two_col_table(lx, top_y, col_w, "The \"ONLY\" List  -  guaranteed points", ["Fact", "Answer"],
    [col_w - 60, 60], ONLY_LIST, NAVY, (0.94, 0.94, 0.95))

LIMB_DIST = [
    ("Anterior", "Taiyin (yin)", "Yangming (yang)"),
    ("Middle", "Jueyin (yin)", "Shaoyang (yang)"),
    ("Posterior", "Shaoyin (yin)  <- HT/SI", "Taiyang (yang)  <- HT/SI"),
]
ly = two_col_table(lx, ly, col_w, "Limb Distribution Rule", ["Position", "Yin", "Yang"],
    [70, (col_w - 70) / 2, (col_w - 70) / 2], LIMB_DIST, NAVY, (0.94, 0.94, 0.95))

ly = callout_box(lx, ly, col_w, "Forbidden in Pregnancy (cumulative reference)",
    ["SP6 Sanyinjiao - strong descending/moving action on the uterus",
     "LI4 Hegu - moves Qi and Blood downward",
     "BL60 Kunlun - promotes labor",
     "BL67 Zhiyin - used for malposition/moxa, contraindicated by needle"],
    GOLD, CREAM)

CLOCK_ROWS = [
    ("LU", "3-5 AM"), ("LI", "5-7 AM"), ("ST", "7-9 AM"), ("SP", "9-11 AM"),
    ("HT", "11 AM-1 PM"), ("SI", "1-3 PM"), ("BL", "3-5 PM"), ("KI", "5-7 PM"),
    ("PC", "7-9 PM"), ("SJ", "9-11 PM"), ("GB", "11 PM-1 AM"), ("LR", "1-3 AM"),
]
ry = two_col_table(rx, top_y, col_w, "Meridian Clock  -  full 24 hours", ["Ch", "Peak"],
    [70, col_w - 70], CLOCK_ROWS, NAVY, (0.94, 0.94, 0.95))

ry = callout_box(rx, ry, col_w, "Last 60 Seconds",
    ["HT = 9 pts, 11 AM-1 PM, Yin Fire, ZERO crossings, Back-Shu BL15, Front-Mu CV14.",
     "SI = 19 pts, 1-3 PM, Yang Fire, 2 crossings (BL1, GB14), Back-Shu BL27, Front-Mu CV4.",
     "HT7 Shenmen = Shu-Stream + Yuan, calms Shen. SI3 Houxi = Shu-Stream + Confluent, opens Du Mai (pairs BL62).",
     "SI's Lower He-Sea = ST39 - not on SI itself. True for all six Fu organs.",
     "Posterior Circuit (also called Inner Circuit) begins: HT -> SI, continues next week BL -> KI."],
    GOLD, CREAM)

y = min(ly, ry) - 12

CONFUSED_ROWS = [
    ("HT3 vs SI8", "Both He-Sea. HT3 Shaohai (Heart, elbow) vs SI8 Xiaohai (Small Intestine, elbow) - similar names, different channels."),
    ("HT7 vs SI4", "Both Yuan-Source. HT7 Shenmen (wrist, calms Shen) vs SI4 Wangu (ulnar wrist)."),
    ("HT5 vs SI7", "Both Luo-Connecting. HT5 Tongli vs SI7 Zhizheng - each links its own pair partner."),
    ("HT6 vs SI6", "Both Xi-Cleft. HT6 Yinxi (acute heart pain) vs SI6 Yanglao (acute eye/vision issues)."),
    ("HT9 vs SI1", "Adjacent fingertip Jing-Wells. HT9 Shaochong = RADIAL side of little finger (HT ends). SI1 Shaoze = ULNAR side (SI begins)."),
    ("SI3 vs BL62", "SI3 Houxi opens the Du Mai; BL62 Shenmai is its Confluent PAIR point, not the same channel."),
    ("Window of Heaven", "SI16 Tianchuang is a Window of Heaven point. HT has none - zero crossings, zero WoH points."),
    ("Circuit hand-offs", "SP->HT (internal, via diaphragm). HT->SI (external, at HT9/SI1). SI->BL (external, facial branch to BL1)."),
]
y = two_col_table(ML, y, CW, "Commonly Confused  -  know both sides", ["Pair", "The distinction"],
    [100, CW - 100], CONFUSED_ROWS, NAVY, (0.94, 0.94, 0.95))

end_page()

c.save()
print("SAVED:", OUT)
