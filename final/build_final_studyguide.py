#!/usr/bin/env python3
"""AC300 Comprehensive Final Study Guide (Weeks 1-9, cumulative).
Usage: python3 build_final_studyguide.py <print|remarkable>
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, '/home/claude/final')
from final_content import (
    NAVY, GOLD, RED, DARK, GRAY, METAL, EARTH, FIRE, WATER, FIREMIN, WOOD, EXTRA, TEAL, AMBER_LUO,
    ZHANG_FINAL_FACTS, TWELVE_MERIDIANS, DIRECTION_RULES, CIRCUITS, HANDOFF_POINTS,
    CHANNEL_META, CHANNEL_ORDER, FIVE_SHU_DEFINITION, FIVE_SHU_MASTER, FIVE_SHU_COLS, FIVE_SHU_YUAN_NOTE,
    EXTRAORDINARY_VESSELS, CONFLUENT_PAIRS_QUICK, LUO_15, LUO_RULE, LOW_PRIORITY_NOTE,
    DIVERGENT_SUMMARY, SINEW_SUMMARY, CUTANEOUS_SUMMARY, EXAM_TRAPS, WEEKLY_MAP,
)

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


def header(subtitle, section_label=""):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    title = "AC300 FINAL STUDY GUIDE"
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
    c.drawCentredString(W / 2, 22, f"AC300/AC375 Final Study Guide (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  {label}")


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
        y[0] = H - HEADER_H - 22


def section_bar(text, accent=NAVY, sub=""):
    ensure_space(28, text)
    setfill(accent); c.rect(ML, y[0] - 3, CW, 3, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 13)
    c.drawString(ML, y[0] - 19, text)
    if sub:
        setfill(GRAY); c.setFont("Lora-Italic", 8.5)
        c.drawRightString(ML + CW, y[0] - 19, sub)
    y[0] -= 32


def para(text, size=9, font="Lora", color=DARK, indent=0, leading=None, gap=6):
    leading = leading or size * 1.28
    lines = wrap_words(text, font, size, CW - indent)
    ensure_space(len(lines) * leading + gap, "")
    setfill(color); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML + indent, y[0], ln)
        y[0] -= leading
    y[0] -= gap


def bullet(label, text, accent=NAVY, size=8.6):
    label_w = 132
    lab_lines = wrap_words(label, "Lora-Bold", size, label_w)
    txt_lines = wrap_words(text, "Lora", size, CW - label_w - 10)
    n = max(len(lab_lines), len(txt_lines))
    needed = n * (size * 1.3) + 5
    ensure_space(needed, "")
    setfill(accent); c.rect(ML, y[0] - 2, 3, needed - 6, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", size)
    for ln in lab_lines:
        c.drawString(ML + 8, yy, ln); yy -= size * 1.3
    yy2 = y[0]
    setfill(DARK); c.setFont("Lora", size)
    for ln in txt_lines:
        c.drawString(ML + 8 + label_w, yy2, ln); yy2 -= size * 1.3
    y[0] -= needed


def mini_table(headers, rows, col_w, accent=NAVY, size=7.8, header_size=8.0, row_h=None, striped=True):
    total_w = sum(col_w)
    row_h = row_h or (size * 1.9)
    n_header_lines = 1
    needed_header = header_size * 1.6 + 4
    ensure_space(needed_header + row_h * min(len(rows), 3), "")
    # header row
    setfill(accent); c.rect(ML, y[0] - needed_header + 4, total_w, needed_header - 4, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", header_size)
    xx = ML
    for h, w in zip(headers, col_w):
        c.drawString(xx + 4, y[0] - needed_header + 9, h)
        xx += w
    y[0] -= needed_header
    for ridx, row in enumerate(rows):
        # compute needed height for this row (wrap each cell)
        cell_lines = []
        for cell, w in zip(row, col_w):
            cl = wrap_words(str(cell), "Lora", size, w - 8)
            cell_lines.append(cl if cl else [""])
        nlines = max(len(cl) for cl in cell_lines)
        rh = nlines * (size * 1.25) + 5
        ensure_space(rh, "")
        if striped and ridx % 2 == 0:
            setfill(ROW_TINT); c.rect(ML, y[0] - rh + 3, total_w, rh - 3, fill=1, stroke=0)
        xx = ML
        setfill(DARK); c.setFont("Lora", size)
        for cl, w in zip(cell_lines, col_w):
            yy = y[0] - 2
            for ln in cl:
                c.drawString(xx + 4, yy, ln)
                yy -= size * 1.25
            xx += w
        y[0] -= rh
    y[0] -= 6


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

bx, by, bs = W / 2 - 34, H - 165, 68
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD); c.rect(bx, by + bs - 8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 7)
c.drawCentredString(W / 2, by + bs - 22, "WEEK")
c.setFont("Lora-Bold", 20)
c.drawCentredString(W / 2, by + 18, "10")

c.setFont("Lora-Bold", 30); setfill(NAVY)
c.drawCentredString(W / 2, H - 227, "COMPREHENSIVE FINAL STUDY GUIDE")
c.setFont("Lora-BoldItalic", 13); setfill(RED)
c.drawCentredString(W / 2, H - 250, "Weeks 1-9, Cumulative -- Channel Theory through Cutaneous Regions")
c.setFont("Lora", 10.5); setfill(DARK)
c.drawCentredString(W / 2, H - 268, "Built around Dr. Zhang's live Final Exam Review \u00b7 30 questions \u00b7 reuses quiz material")

setstroke(GOLD); c.setLineWidth(1)
c.line(W / 2 - 120, H - 282, W / 2 - 40, H - 282)
c.line(W / 2 + 40, H - 282, W / 2 + 120, H - 282)
setfill(GOLD); c.circle(W / 2, H - 282, 2.5, fill=1, stroke=0)

# This-week-covers box
box_x, box_y, box_w2, box_h2 = 60, H - 470, W - 120, 130
setfill((0.929, 0.949, 0.965) if not IS_RM else (0.902, 0.878, 0.816))
c.rect(box_x, box_y, box_w2, box_h2, fill=1, stroke=0)
setfill(GOLD); c.rect(box_x, box_y + box_h2 - 4, box_w2, 4, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 11)
c.drawString(box_x + 14, box_y + box_h2 - 22, "This Guide Covers:")
c.setFont("Lora", 9.3); setfill(DARK)
covers = [
    "All 12 primary meridians -- full ID cards (points, Back-Shu/Front-Mu, Yuan/Luo/Xi-Cleft/He-Sea, crossing points)",
    "The 3 Circuits (Outer/Inner/Middle), 24-hr clock, and direction-of-flow rules -- Dr. Zhang's #1 review emphasis",
    "GV, CV, and all 8 Extraordinary Vessels with their Confluent Point pairings",
    "The 15 Collaterals (Luo-Connecting points) and a low-priority summary of Divergent/Sinew/Cutaneous material",
    "Full Five Shu (Transport) Points master table -- all 60 points, all 12 meridians",
    "A dedicated Exam Traps page consolidating every verified \u201cread this last\u201d fact from every weekly Cram Sheet",
]
yy = box_y + box_h2 - 40
for item in covers:
    c.setFillColorRGB(*GOLD); c.circle(box_x + 16, yy + 3, 1.6, fill=1, stroke=0)
    setfill(DARK)
    lines = wrap_words(item, "Lora", 9.3, box_w2 - 40)
    for ln in lines:
        c.drawString(box_x + 24, yy, ln)
        yy -= 12.5

# quiz-date / reading box
box2_y = box_y - 62
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
y[0] = H - HEADER_H - 22
section_bar("WHAT DR. ZHANG SAID IS ON THE FINAL", accent=RED, sub="Sourced directly from the Week 9 live transcript")
for label, text in ZHANG_FINAL_FACTS:
    bullet(label, text, accent=RED, size=8.7)
end_page()

# =====================================================================
# PAGE: MASTER PATHWAY TABLE + CIRCUITS
# =====================================================================
new_page("Master Pathway Table & The 3 Circuits")
y[0] = H - HEADER_H - 22
section_bar("MASTER PATHWAY TABLE -- ALL 12 PRIMARY MERIDIANS", accent=NAVY,
            sub="Dr. Zhang's #1 review emphasis")
headers = ["Ch", "Organ", "Classification", "Y/Y", "Direction", "Circuit", "Clock"]
col_w = [28, 108, 78, 26, 96, 90, 62]
rows = [(a, o, cl, yy_, d, ci, cl2) for a, o, cl, yy_, d, ci, cl2 in TWELVE_MERIDIANS]
mini_table(headers, rows, col_w, accent=NAVY, size=7.6)

section_bar("DIRECTION-OF-FLOW RULES", accent=GOLD)
mini_table(["Rule", "Direction"], DIRECTION_RULES, [280, CW - 280], accent=GOLD, size=8.2)

section_bar("HAND-OFF POINTS BETWEEN CIRCUITS", accent=GOLD)
mini_table(["Transition", "Location", "Example"], HANDOFF_POINTS, [140, 90, CW - 230], accent=GOLD, size=7.8)
end_page()

new_page("The 3 Circuits, Detailed")
y[0] = H - HEADER_H - 22
section_bar("THE THREE CIRCUITS", accent=NAVY)
for name, pos, chain, poles, accent in CIRCUITS:
    bullet(f"{name} ({pos})", f"{' -> '.join(chain)}   |   {poles}", accent=accent, size=8.6)
para("Course sequence: Outer/Anterior completes first (Weeks 2-3), then Inner/Posterior (Weeks 4-5), then "
     "Middle (Week 6). Each circuit's 4 channels hand off Qi in the same chest->hand->head->foot->chest pattern.",
     size=8.6, color=GRAY)
end_page()

# =====================================================================
# CHANNEL ID CARDS -- 12 primary meridians, 2 per page
# =====================================================================
def channel_card(abbr):
    d = CHANNEL_META[abbr]
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
    mini_table(["Category", "Detail"], rows, [128, CW - 128], accent=d['accent'], size=7.9, striped=True)


new_page("Channel ID Cards -- LU / LI")
y[0] = H - HEADER_H - 22
channel_card("LU")
channel_card("LI")
end_page()

new_page("Channel ID Cards -- ST / SP")
y[0] = H - HEADER_H - 22
channel_card("ST")
channel_card("SP")
end_page()

new_page("Channel ID Cards -- HT / SI")
y[0] = H - HEADER_H - 22
channel_card("HT")
channel_card("SI")
end_page()

new_page("Channel ID Cards -- BL / KI")
y[0] = H - HEADER_H - 22
channel_card("BL")
channel_card("KI")
end_page()

new_page("Channel ID Cards -- PC / SJ")
y[0] = H - HEADER_H - 22
channel_card("PC")
channel_card("SJ")
end_page()

new_page("Channel ID Cards -- GB / LR")
y[0] = H - HEADER_H - 22
channel_card("GB")
channel_card("LR")
end_page()

# =====================================================================
# EXTRAORDINARY VESSELS
# =====================================================================
new_page("Eight Extraordinary Vessels")
y[0] = H - HEADER_H - 22
section_bar("EIGHT EXTRAORDINARY VESSELS", accent=EXTRA, sub="Week 7 -- confluent points started live in Week 9 review")
for v in EXTRAORDINARY_VESSELS:
    npts = f"{v['n_points']} pts" if v['n_points'] else "no own points (except GV/CV)"
    label = f"{v['abbr']} -- {v['name']}"
    detail = (f"{npts} | Sea: {v['sea']} | Confluent: {v['confluent']} (partner: {v['partner']}) | "
              f"Course: {v['course']} | Function: {v['function']}")
    bullet(label, detail, accent=v['accent'], size=8.0)
end_page()

new_page("Confluent Point Pairings -- Quick Map")
y[0] = H - HEADER_H - 22
section_bar("EIGHT CONFLUENT POINTS -- PAIRED QUICK MAP", accent=TEAL,
            sub="Connect the 8 EVs to the 12 regular meridians")
mini_table(["Point A", "Point B", "Vessels Opened", "Clinical Use"], CONFLUENT_PAIRS_QUICK,
           [86, 86, 130, CW - 302], accent=TEAL, size=7.8)
para("Rule: Confluent points always pair one Hand channel point with one Foot channel point, and the pairing "
     "is fixed -- these four pairs never mix.", size=8.4, color=GRAY)
end_page()

# =====================================================================
# 15 COLLATERALS
# =====================================================================
new_page("15 Collaterals (Luo-Connecting Points)")
y[0] = H - HEADER_H - 22
section_bar("15 COLLATERALS -- LUO-CONNECTING POINTS", accent=AMBER_LUO, sub="Week 8")
mini_table(["Luo Point", "Connection", "Note"], LUO_15, [90, 90, CW - 180], accent=AMBER_LUO, size=7.8)
para(LUO_RULE, size=8.4, color=GRAY)
end_page()

# =====================================================================
# LOW-PRIORITY: DIVERGENT / SINEW / CUTANEOUS
# =====================================================================
new_page("Divergent Channels, Sinew & Cutaneous Regions (Low-Priority)")
y[0] = H - HEADER_H - 22
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
y[0] = H - HEADER_H - 22
section_bar("FIVE SHU POINTS -- MASTER TABLE (60 POINTS)", accent=NAVY, sub="Week 9 -- all 12 meridians")
para(FIVE_SHU_DEFINITION, size=8.3, color=GRAY)
headers = ["Meridian"] + FIVE_SHU_COLS
col_w = [110] + [(CW - 110) // 5] * 5
rows = [[d['m']] + d['pts'] for d in FIVE_SHU_MASTER]
mini_table(headers, rows, col_w, accent=NAVY, size=7.0, header_size=7.4)
para(FIVE_SHU_YUAN_NOTE, size=8.2, color=GRAY)
end_page()

# =====================================================================
# EXAM TRAPS
# =====================================================================
new_page("Exam Traps -- Consolidated \"Read These Last\"")
y[0] = H - HEADER_H - 22
section_bar("EXAM TRAPS -- CONSOLIDATED FROM EVERY WEEK", accent=RED,
            sub="Read this page last, right before the final")
for label, text in EXAM_TRAPS:
    bullet(label, text, accent=RED, size=8.0)
end_page()

# =====================================================================
# WEEKLY MAP
# =====================================================================
new_page("Course Map -- Weeks 1-10")
y[0] = H - HEADER_H - 22
section_bar("COURSE MAP -- WEEKS 1-10", accent=GOLD, sub="Syllabus reference")
mini_table(["Week", "Topic", "Notes"], WEEKLY_MAP, [56, 190, CW - 246], accent=GOLD, size=8.0)
end_page()

c.save()
print("SAVED:", OUT)
