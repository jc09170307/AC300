#!/usr/bin/env python3
"""AC300 Final Cram Sheet (Weeks 1-9, cumulative). Usage: python3 build_final_cramsheet.py <print|remarkable>"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, '/home/claude/final')
from final_content import (
    NAVY, GOLD, RED, DARK, GRAY, METAL, EARTH, FIRE, WATER, FIREMIN, WOOD, EXTRA, TEAL, AMBER_LUO,
    TWELVE_MERIDIANS, CHANNEL_META, CHANNEL_ORDER, FIVE_SHU_MASTER, FIVE_SHU_COLS,
    EXTRAORDINARY_VESSELS, CONFLUENT_PAIRS_QUICK, LUO_15, EXAM_TRAPS, ZHANG_FINAL_FACTS,
)

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
    HEADER_H = 46
    COVER_MASTHEAD_H = 70
    HAIRLINE = 0.6
    OUT = "/mnt/user-data/outputs/AC300_Final_CramSheet_Wk1-9_Mobile.pdf"
    EDLABEL = "Mobile Edition -- reads at 100% zoom, no pinch-zoom needed"
elif IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    HEADER_H = 51
    COVER_MASTHEAD_H = 86
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Final_CramSheet_Wk1-9_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    HEADER_H = 44
    COVER_MASTHEAD_H = 80
    HAIRLINE = 0.5
    OUT = "/mnt/user-data/outputs/AC300_Final_CramSheet_Wk1-9_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=(W, H))
ML, MR = (14, 14) if IS_MOBILE else (30, 30)
CW = W - ML - MR
page_num = [1]
FS = 1.3 if IS_MOBILE else 1.0


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
    title_size = 11.5 * FS
    setfill((1, 1, 1)); c.setFont("Lora-Bold", title_size)
    title = "AC300 CRAM SHEET" if IS_MOBILE else "AC300 FINAL CRAM SHEET"
    c.drawString(ML, H - HEADER_H + 15, title)
    title_w = pdfmetrics.stringWidth(title, "Lora-Bold", title_size)
    avail = (W - ML) - (ML + title_w) - 10
    fs = 9 * FS
    sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    while sw > avail and fs > 6.5:
        fs -= 0.5
        sw = pdfmetrics.stringWidth(subtitle, "Lora-Italic", fs)
    if avail > 40:
        c.setFont("Lora-Italic", fs)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle)


def footer(label):
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(ML, 24, W - ML, 24)
    setfill(GRAY); c.setFont("Lora-Italic", 7 * FS)
    foot_text = f"AC300 Cram (Wk 1-9) \u00b7 {label}" if IS_MOBILE else f"AC300/AC375 Final Cram Sheet (Wk 1-9)  \u00b7  VUIM Summer 2026  \u00b7  {label}"
    c.drawCentredString(W / 2, 14, foot_text)


def new_page(subtitle):
    page_bg(); header(subtitle)


def end_page():
    footer(f"Page {page_num[0]}")
    c.showPage(); page_num[0] += 1


y = [H]


def ensure_space(needed, subtitle):
    if y[0] - needed < 30:
        end_page(); new_page(subtitle); y[0] = H - HEADER_H - 14


def section_bar(text, accent=NAVY):
    title_size = 10.5 * FS
    title_lines = wrap_words(text, "Lora-Bold", title_size, CW)
    title_line_h = title_size * 1.15
    est_h = len(title_lines) * title_line_h
    ensure_space(est_h + 20 * FS, text)
    setfill(accent); c.rect(ML, y[0] - 2, CW, 2.5, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", title_size)
    yy = y[0] - 14 * FS
    for ln in title_lines:
        c.drawString(ML, yy, ln)
        yy -= title_line_h
    y[0] = yy - 13 * FS


def mini_table(headers, rows, col_w, accent=NAVY, size=6.6, header_size=6.9, striped=True):
    size = size * FS; header_size = header_size * FS
    total_w = sum(col_w)
    needed_header = header_size * 1.9 + 6

    def draw_header():
        ensure_space(needed_header + 10, "")
        setfill(accent); c.rect(ML, y[0] - needed_header + 3, total_w, needed_header - 3, fill=1, stroke=0)
        setfill((1, 1, 1)); c.setFont("Lora-Bold", header_size)
        xx = ML
        for h, w in zip(headers, col_w):
            c.drawString(xx + 3, y[0] - needed_header + 9, h)
            xx += w
        y[0] -= (needed_header + 2)

    draw_header()
    for ridx, row in enumerate(rows):
        cell_lines = []
        for cell, w in zip(row, col_w):
            cl = wrap_words(str(cell), "Lora", size, w - 6)
            cell_lines.append(cl if cl else [""])
        nlines = max(len(cl) for cl in cell_lines)
        rh = nlines * (size * 1.35) + 4.5
        y_before = y[0]
        ensure_space(rh, "")
        if y[0] > y_before:
            draw_header()
        if striped and ridx % 2 == 0:
            setfill(ROW_TINT); c.rect(ML, y[0] - rh + 2, total_w, rh - 2, fill=1, stroke=0)
        xx = ML
        setfill(DARK); c.setFont("Lora", size)
        for cl, w in zip(cell_lines, col_w):
            yy = y[0] - 1.5
            for ln in cl:
                c.drawString(xx + 3, yy, ln)
                yy -= size * 1.2
            xx += w
        y[0] -= rh
    y[0] -= 3


def tight_bullets(items, accent=NAVY, size=7.0):
    size = size * FS
    if IS_MOBILE:
        for label, text in items:
            lab_lines = wrap_words(label, "Lora-Bold", size, CW - 8)
            txt_lines = wrap_words(text, "Lora", size, CW - 8)
            needed = (len(lab_lines) + len(txt_lines)) * (size * 1.3) + 5
            ensure_space(needed, "")
            setfill(accent); c.rect(ML, y[0] - needed + 4, 2, needed - 7, fill=1, stroke=0)
            yy = y[0]
            setfill(NAVY); c.setFont("Lora-Bold", size)
            for ln in lab_lines:
                c.drawString(ML + 7, yy, ln); yy -= size * 1.3
            setfill(DARK); c.setFont("Lora", size)
            for ln in txt_lines:
                c.drawString(ML + 7, yy, ln); yy -= size * 1.3
            y[0] -= needed
        return
    for label, text in items:
        lab_lines = wrap_words(label, "Lora-Bold", size, 105)
        txt_lines = wrap_words(text, "Lora", size, CW - 115)
        n = max(len(lab_lines), len(txt_lines))
        needed = n * (size * 1.35) + 4
        ensure_space(needed, "")
        setfill(accent); c.rect(ML, y[0] - 1, 2, needed - 4, fill=1, stroke=0)
        yy = y[0]
        setfill(NAVY); c.setFont("Lora-Bold", size)
        for ln in lab_lines:
            c.drawString(ML + 6, yy, ln); yy -= size * 1.22
        yy2 = y[0]
        setfill(DARK); c.setFont("Lora", size)
        for ln in txt_lines:
            c.drawString(ML + 116, yy2, ln); yy2 -= size * 1.22
        y[0] -= needed


def record_block(title, fields, accent=NAVY, title_size=8.0, field_size=6.8):
    """Narrow, phone-friendly replacement for wide (5+ column) tables -- cram-sheet density."""
    title_size = title_size * FS; field_size = field_size * FS
    field_text = "  \u00b7  ".join(f"{lab}: {val}" for lab, val in fields)
    field_lines = wrap_words(field_text, "Lora", field_size, CW - 12)
    title_line_h = title_size * 1.35
    field_line_h = field_size * 1.35
    needed = title_line_h + len(field_lines) * field_line_h + 4
    ensure_space(needed, "")
    setfill(accent); c.rect(ML, y[0] - needed + 4, 2, needed - 7, fill=1, stroke=0)
    yy = y[0]
    setfill(accent); c.setFont("Lora-Bold", title_size)
    c.drawString(ML + 7, yy, title)
    yy -= title_line_h
    setfill(DARK); c.setFont("Lora", field_size)
    for ln in field_lines:
        c.drawString(ML + 7, yy, ln)
        yy -= field_line_h
    y[0] -= needed


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
c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 35, "AC300/AC375" if IS_MOBILE else "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - COVER_MASTHEAD_H + 18, EDLABEL)

if IS_MOBILE:
    yy = H - COVER_MASTHEAD_H - 40
    c.setFont("Lora-Bold", 24); setfill(NAVY)
    c.drawCentredString(W / 2, yy, "FINAL CRAM SHEET"); yy -= 28
    c.setFont("Lora-Italic", 11.5); setfill(RED)
    c.drawCentredString(W / 2, yy, "Weeks 1-9 -- night-before density reference"); yy -= 18
    c.setFont("Lora", 9.5); setfill(DARK)
    c.drawCentredString(W / 2, yy, "30 Qs \u00b7 Cumulative \u00b7 Reuses Quiz Material"); yy -= 22
    setstroke(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 50, yy, W / 2 - 15, yy)
    c.line(W / 2 + 15, yy, W / 2 + 50, yy)
    setfill(GOLD); c.circle(W / 2, yy, 2, fill=1, stroke=0)
    yy -= 26
    labels = [
        ("SCOPE", "All 12 meridians -- 8 EVs, 15 Luo, 60 Five Shu", (0.157, 0.302, 0.541)),
        ("FORMAT", "One glance per fact -- pairs with the Study Guide", (0.380, 0.180, 0.522)),
        ("PRIORITY", "Zhang's exam focus flagged throughout", (0.106, 0.369, 0.353)),
    ]
    for t, desc, col in labels:
        desc_lines = wrap_words(desc, "Lora-Italic", 8.3, CW - 20)
        box_h = 20 + len(desc_lines) * 11
        setfill((0.933, 0.937, 0.949) if not IS_RM else (0.902, 0.878, 0.816))
        c.rect(ML, yy - box_h, CW, box_h, fill=1, stroke=0)
        c.setFillColorRGB(*col); c.rect(ML, yy - 3, CW, 3, fill=1, stroke=0)
        c.setFont("Lora-Bold", 10); setfill(NAVY)
        c.drawString(ML + 10, yy - 16, t)
        c.setFont("Lora-Italic", 8.3); setfill(DARK)
        zz = yy - 29
        for ln in desc_lines:
            c.drawString(ML + 10, zz, ln); zz -= 11
        yy -= box_h + 10

    setstroke(GOLD); c.setLineWidth(1)
    c.line(20, 40, W - 20, 40)
    c.setFont("Lora-Italic", 7.5); setfill(GRAY)
    c.drawCentredString(W / 2, 26, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM")
    c.showPage(); page_num[0] += 1
else:
    c.setFont("Lora-Bold", 28); setfill(NAVY)
    c.drawCentredString(W / 2, H - 130, "FINAL CRAM SHEET")
    c.setFont("Lora-Italic", 13); setfill(RED)
    c.drawCentredString(W / 2, H - 153, "Weeks 1-9 -- night-before density reference")
    c.setFont("Lora", 10.5); setfill(DARK)
    c.drawCentredString(W / 2, H - 172, "30 Qs \u00b7 Cumulative \u00b7 Reuses Quiz Material \u00b7 Quiz Ready")

    setstroke(GOLD); c.setLineWidth(1)
    c.line(W / 2 - 100, H - 186, W / 2 - 30, H - 186)
    c.line(W / 2 + 30, H - 186, W / 2 + 100, H - 186)
    setfill(GOLD); c.circle(W / 2, H - 186, 2.2, fill=1, stroke=0)

    box_w, box_h, gap = 155, 52, 12
    total = box_w * 3 + gap * 2
    bx0 = (W - total) / 2
    by0 = H - 264
    labels = [
        ("SCOPE", "All 12 meridians", "8 EVs, 15 Luo, 60 Five Shu", (0.157, 0.302, 0.541)),
        ("FORMAT", "One glance per fact", "Pairs with the Study Guide", (0.380, 0.180, 0.522)),
        ("PRIORITY", "Zhang's exam focus", "flagged throughout", (0.106, 0.369, 0.353)),
    ]
    for i, (t, l1, l2, col) in enumerate(labels):
        x = bx0 + i * (box_w + gap)
        setfill((0.933, 0.937, 0.949) if not IS_RM else (0.902, 0.878, 0.816))
        c.rect(x, by0, box_w, box_h, fill=1, stroke=0)
        c.setFillColorRGB(*col); c.rect(x, by0 + box_h - 3, box_w, 3, fill=1, stroke=0)
        c.setFont("Lora-Bold", 9.5)
        c.drawCentredString(x + box_w / 2, by0 + box_h - 18, t)
        c.setFont("Lora-Italic", 7.6); c.setFillColorRGB(*DARK)
        c.drawCentredString(x + box_w / 2, by0 + box_h - 30, l1)
        c.drawCentredString(x + box_w / 2, by0 + box_h - 41, l2)

    setstroke(GOLD); c.setLineWidth(1)
    c.line(50, 55, W - 50, 55)
    c.setFont("Lora-Italic", 8.5); setfill(GRAY)
    c.drawCentredString(W / 2, 38, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 VUIM \u00b7 Dr. Zhang's Lecture 1-9 + CAM 4th Ed. + MOA 3rd Ed.")
    c.showPage(); page_num[0] += 1

# =====================================================================
# PAGE: WHAT ZHANG SAID (condensed)
# =====================================================================
new_page("What Dr. Zhang Said")
y[0] = H - HEADER_H - 14
section_bar("WHAT DR. ZHANG SAID (VERBATIM-SOURCED)", accent=RED)
tight_bullets(ZHANG_FINAL_FACTS, accent=RED, size=7.1)

section_bar("MASTER PATHWAY TABLE", accent=NAVY)
_pw_accents = {"Outer / Anterior": METAL, "Inner / Posterior": FIRE, "Middle": FIREMIN}
for a, o, cl, yy_, d, ci, cl2 in TWELVE_MERIDIANS:
    record_block(f"{a} -- {o}", [("Class", cl), ("Y/Y", yy_), ("Dir", d), ("Circuit", ci), ("Clock", cl2)],
                 accent=_pw_accents.get(ci, NAVY))
end_page()

# =====================================================================
# PAGE: CHANNEL QUICK-SCAN GRID (all 12, narrow records)
# =====================================================================
new_page("All 12 Channels -- Quick-Scan Records")
y[0] = H - HEADER_H - 14
section_bar("ALL 12 PRIMARY MERIDIANS -- QUICK-SCAN RECORDS", accent=NAVY)
_qs_accents = {"LU": METAL, "LI": METAL, "ST": EARTH, "SP": EARTH, "HT": FIRE, "SI": FIRE,
               "BL": WATER, "KI": WATER, "PC": FIREMIN, "SJ": FIREMIN, "GB": WOOD, "LR": WOOD}
for abbr in CHANNEL_ORDER:
    d = CHANNEL_META[abbr]
    conf_cmd = d['confluent'] if d['confluent'] != "none" else d['command']
    record_block(f"{abbr} -- {d['n_points']} pts", [
        ("Back-Shu", d['back_shu']), ("Front-Mu", d['front_mu']), ("Yuan", d['yuan']),
        ("Luo", d['luo']), ("He-Sea", d['he_sea']), ("Xi-Cleft", d['xi_cleft']),
        ("Confluent/Cmd", conf_cmd), ("Crossing", d['crossing'][:50])],
        accent=_qs_accents.get(abbr, NAVY))
end_page()

# =====================================================================
# PAGE: EXTRAORDINARY VESSELS + CONFLUENT + LUO (condensed)
# =====================================================================
new_page("Extraordinary Vessels, Confluent & Luo Points")
y[0] = H - HEADER_H - 14
section_bar("8 EXTRAORDINARY VESSELS -- QUICK MAP", accent=EXTRA)
headers = ["Vessel", "Pts", "Confluent (Partner)", "Function"]
col_w = [0.22 * CW, 0.07 * CW, 0.30 * CW, 0.41 * CW]
ev_rows = []
for v in EXTRAORDINARY_VESSELS:
    npts = str(v['n_points']) if v['n_points'] else "--"
    ev_rows.append((v['abbr'], npts, f"{v['confluent'].split()[0]} ({v['partner'].split()[0]})", v['function'][:70]))
mini_table(headers, ev_rows, col_w, accent=EXTRA, size=6.6, header_size=6.9)

section_bar("CONFLUENT POINT PAIRS", accent=TEAL)
conf_rows = [(a, b, opens, use) for a, b, opens, use, note in CONFLUENT_PAIRS_QUICK]
mini_table(["Pt A", "Pt B", "Opens", "Use"], conf_rows, [0.12 * CW, 0.12 * CW, 0.20 * CW, 0.56 * CW],
           accent=TEAL, size=6.6, header_size=6.9)

section_bar("15 LUO-CONNECTING POINTS", accent=AMBER_LUO)
mini_table(["Point", "Connection", "Note"], LUO_15, [0.14 * CW, 0.14 * CW, 0.72 * CW], accent=AMBER_LUO, size=6.4, header_size=6.7)
end_page()

# =====================================================================
# PAGE: FIVE SHU MASTER GRID
# =====================================================================
new_page("Five Shu Master Grid")
y[0] = H - HEADER_H - 14
section_bar("FIVE SHU POINTS -- FULL 60-POINT GRID", accent=NAVY)
section_bar("Jing-Well -> Ying-Spring -> Shu-Stream", accent=NAVY)
headers_a = ["Meridian"] + FIVE_SHU_COLS[:3]
col_w_a = [0.14 * CW] + [0.287 * CW] * 3
rows_a = [[d['m'].split(' (')[0]] + d['pts'][:3] for d in FIVE_SHU_MASTER]
mini_table(headers_a, rows_a, col_w_a, accent=NAVY, size=6.2, header_size=6.5)

section_bar("Jing-River -> He-Sea", accent=NAVY)
headers_b = ["Meridian"] + FIVE_SHU_COLS[3:]
col_w_b = [0.14 * CW] + [0.43 * CW] * 2
rows_b = [[d['m'].split(' (')[0]] + d['pts'][3:] for d in FIVE_SHU_MASTER]
mini_table(headers_b, rows_b, col_w_b, accent=NAVY, size=6.2, header_size=6.5)
end_page()

# =====================================================================
# PAGE: EXAM TRAPS
# =====================================================================
new_page("Exam Traps")
y[0] = H - HEADER_H - 14
section_bar("EXAM TRAPS -- READ THIS PAGE LAST", accent=RED)
tight_bullets(EXAM_TRAPS, accent=RED, size=6.7)
end_page()

c.save()
print("SAVED:", OUT)
