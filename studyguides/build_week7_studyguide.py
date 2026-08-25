#!/usr/bin/env python3
"""AC300 Week 7 Study Guide Classic -- The Eight Extraordinary Vessels.
Reference only (no quiz content, per Study Guide architecture rule). Each
vessel gets its own dedicated page (hard page break), grouped consecutively.
Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk7")
from common_wk7 import (DocBuilder, studyguide_cover, setfill, setstroke, box, hairline,
                         draw_paragraph, wrap_words, section_label, pathway_strip,
                         draw_image_contain, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK,
                         RED, LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM)
from wk7_content import (ALL_VESSELS, GV, CV, CHONG, DAI, YANG_QIAO, YIN_QIAO, YANG_WEI,
                          YIN_WEI, CONFLUENT_PAIRS, ONE_SOURCE_THREE_BRANCHES, NO_ORGAN_NOTE,
                          READING_ASSIGNMENT)

OUT = f"/mnt/user-data/outputs/AC300_Week7_StudyGuide_Classic_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 7 Study Guide"
FOOTER = "AC300/AC375 | Week 7 | Eight Extraordinary Vessels | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def vessel_header(vessel, subtitle_extra=""):
    accent = vessel["accent"]
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, accent); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 15)
    c.drawString(ML + 14, bar_bot + 9, f"{vessel['name']}  ({vessel['pinyin']})")
    sub = vessel["sea"] or subtitle_extra
    if sub:
        c.setFont("Lora-Italic", 9)
        c.drawRightString(RX - 6, bar_bot + 11, sub)
    return bar_bot - 22


def vessel_page(vessel):
    db.new_page()
    y = vessel_header(vessel)
    accent = vessel["accent"]
    tint_c = tint(accent, 0.85)

    # quick-facts pill row
    facts = []
    if vessel["own_points"]:
        facts.append(("Points", str(vessel["n_points"])))
    else:
        facts.append(("Points", "shares w/ primary meridians"))
    facts.append(("Coalescent pts", str(len(vessel["coalescent_points"]))))
    facts.append(("Confluent pt", vessel["confluent_point"]))
    setfill(c, tint_c); c.rect(ML, y - 16, CW, 16, fill=1, stroke=0)
    xx = ML + 8
    for label, val in facts:
        setfill(c, GRAY); c.setFont("Lora", 7.2)
        c.drawString(xx, y - 11, label + ":  ")
        lw = c.stringWidth(label + ":  ", "Lora", 7.2)
        setfill(c, DARK); c.setFont("Lora-Bold", 7.2)
        c.drawString(xx + lw, y - 11, val)
        xx += lw + c.stringWidth(val, "Lora-Bold", 7.2) + 26
    y -= 30

    col_w = (CW - 20) / 2
    left_x, right_x = ML, ML + col_w + 20

    # LEFT: course + first/last points
    ly = section_label(c, y, "Running Course", accent, x=left_x)
    if vessel["figure"]:
        ly = draw_image_contain(c, vessel["figure"], left_x, ly, col_w, 380, accent)
        setfill(c, GRAY); c.setFont("Lora-Italic", 7.3)
        c.drawCentredString(left_x + col_w / 2, ly - 11, f"Lecture Fig. \u2014 {vessel['name']}")
        ly -= 10
        setfill(c, LGRAY); c.setFont("Lora-Italic", 6.6)
        c.drawCentredString(left_x + col_w / 2, ly - 9, vessel.get("figure_source", ""))
        ly -= 22
        ly = section_label(c, ly, "Course Summary", accent, size=8.5, x=left_x)
        for step in vessel["course"]:
            lines = wrap_words("\u2022 " + step, "Lora", 7.6, col_w - 4)
            for ln in lines:
                c.setFont("Lora", 7.6); setfill(c, DARK)
                c.drawString(left_x, ly, ln)
                ly -= 10
            ly -= 1
    else:
        ly = pathway_strip(c, vessel["course"], left_x, ly, col_w, accent, size=9.5, node_r=8)

    if vessel["first_point"]:
        ly -= 6
        ly = section_label(c, ly, "First & Last Points", accent, size=8.5, x=left_x)
        setfill(c, DARK); c.setFont("Lora", 7.8)
        ly = draw_paragraph(c, "First: " + vessel["first_point"], left_x, ly, col_w, size=7.6, leading=9.8)
        ly -= 2
        ly = draw_paragraph(c, "Last: " + vessel["last_point"], left_x, ly, col_w, size=7.6, leading=9.8)

    # RIGHT: coalescent pts, confluent pt, functions, pathology
    ry = section_label(c, y, "Coalescent Points (Jiao Hui Xue)", accent, x=right_x)
    setfill(c, DARK); c.setFont("Lora", 8)
    coal_text = "  \u00b7  ".join(vessel["coalescent_points"])
    ry = draw_paragraph(c, coal_text, right_x, ry, col_w, size=8, leading=11)
    if vessel.get("coalescent_flag"):
        ry -= 4
        box_lines = wrap_words(vessel["coalescent_flag"], "Lora-Italic", 7.2, col_w - 16)
        bh = len(box_lines) * 9.4 + 8
        box(c, right_x, ry, col_w, bh, tint(RED, 0.85))
        setfill(c, RED); c.setFont("Lora-Italic", 7.2)
        ty = ry - 9
        for ln in box_lines:
            c.drawString(right_x + 8, ty, ln)
            ty -= 9.4
        ry -= bh
    ry -= 12

    ry = section_label(c, ry, "Confluent (Opening) Point", accent, x=right_x)
    setfill(c, accent); c.setFont("Lora-Bold", 9.5)
    c.drawString(right_x, ry, vessel["confluent_point"])
    ry -= 12
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.8)
    ry = draw_paragraph(c, "Pairs with " + vessel["confluent_partner"], right_x, ry, col_w,
                         font="Lora-Italic", size=7.8, leading=10)
    ry -= 10

    ry = section_label(c, ry, "Physiological Functions", accent, x=right_x)
    setfill(c, DARK); c.setFont("Lora", 7.9)
    for f in vessel["functions"]:
        lines = wrap_words("\u2022 " + f, "Lora", 7.9, col_w - 4)
        for ln in lines:
            c.drawString(right_x, ry, ln)
            ry -= 10.3
        ry -= 2
    ry -= 6

    ry = section_label(c, ry, "Pathological Symptoms", accent, x=right_x)
    bh = 10.3 * sum(len(wrap_words(p, "Lora", 7.9, col_w - 18)) for p in vessel["pathology"]) + len(vessel["pathology"]) * 2 + 10
    box(c, right_x, ry, col_w, bh, CARD_BG)
    ty = ry - 10
    for p in vessel["pathology"]:
        setfill(c, accent); c.circle(right_x + 6, ty + 2, 1.6, fill=1, stroke=0)
        setfill(c, DARK); c.setFont("Lora", 7.9)
        lines = wrap_words(p, "Lora", 7.9, col_w - 18)
        for ln in lines:
            c.drawString(right_x + 12, ty, ln)
            ty -= 10.3
        ty -= 2
    ry -= bh + 14

    # Clinical Pearl / mnemonic box -- fills remaining right-column space
    if vessel.get("mnemonic"):
        ry = section_label(c, ry, "Clinical Pearl / Memory Aid", accent, x=right_x)
        pearl_tint = tint(accent, 0.88)
        pearl_lines = wrap_words(vessel["mnemonic"], "Lora-Italic", 8, col_w - 20)
        ph = len(pearl_lines) * 10.8 + 14
        box(c, right_x, ry, col_w, ph, pearl_tint)
        setstroke(c, accent); c.setLineWidth(1.4)
        c.line(right_x, ry - ph, right_x, ry)
        ty = ry - 12
        setfill(c, DARK); c.setFont("Lora-Italic", 8)
        for ln in pearl_lines:
            c.drawString(right_x + 10, ty, ln)
            ty -= 10.8
        ry -= ph

    # LEFT column: confluent point location detail -- fills remaining left space
    if vessel.get("confluent_location"):
        ly -= 14
        ly = section_label(c, ly, "Locating the Confluent Point", accent, x=left_x)
        setfill(c, DARK)
        ly = draw_paragraph(c, f"{vessel['confluent_point']}: " + vessel["confluent_location"],
                             left_x, ly, col_w, size=8, leading=10.8)

    db.end_page()


# ============================================================
# COVER
# ============================================================
studyguide_cover(
    db,
    title="Week 7 Study Guide",
    subtitle="The Eight Extraordinary Vessels \u2014 Qi Jing Ba Mai",
    points_line="GV (28 pts) + CV (24 pts) + Chong, Dai, Yang/Yin Qiao, Yang/Yin Wei (share primary-meridian points)",
    covers_bullets=[
        "Governor Vessel (GV/Du Mai) and Conception Vessel (CV/Ren Mai) \u2014 the only two vessels with their own dedicated points",
        "Thoroughfare Vessel (Chong Mai) \u2014 sea of the 12 meridians, sea of blood, sea of the zang-fu organs",
        "Belt Vessel (Dai Mai) \u2014 the only vessel running horizontally around the waist",
        "Yang Qiao Mai + Yin Qiao Mai \u2014 the Heel vessel pair (limb movement, sleep/wake balance)",
        "Yang Wei Mai + Yin Wei Mai \u2014 the Link vessel pair (exterior/interior yin-yang regulation)",
        "\u201cOne source, three branches\u201d \u2014 how Du, Ren, and Chong all arise from the lower abdomen",
        "The Eight Confluent (Master-Couple) Points \u2014 all 4 opening-point pairings",
        "Two coalescent-point-count discrepancies flagged for Dr. Zhang (Yang Qiao, Yang Wei)",
    ],
    info_lines=[
        "QUIZ 5 (this week) covers: the Eight Extraordinary Vessels + cumulative Middle Circuit review.",
        f"{READING_ASSIGNMENT}",
        "Slides: Dr. Vivian Zhang, Lecture_7vivian11_12.pdf (76 slides)",
    ],
)

# ============================================================
# ONE SOURCE, THREE BRANCHES + STRUCTURAL OVERVIEW PAGE
# ============================================================
db.new_page()
y = H - 60
setfill(c, NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, "Structural Overview: What Makes a Vessel \u201cExtraordinary\u201d")
y -= 10
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 22

y = section_label(c, y, "The Defining Trait", NAVY, size=10.5)
setfill(c, DARK)
y = draw_paragraph(c, NO_ORGAN_NOTE, ML, y, CW, size=9.3, leading=13)
y -= 16

y = section_label(c, y, "\u201cOne Source, Three Branches\u201d (Yi Yuan San Qi)", NAVY, size=10.5)
y = draw_paragraph(c, ONE_SOURCE_THREE_BRANCHES, ML, y, CW, size=9.3, leading=13)
y -= 12

# small diagram: 3 vessels branching from lower abdomen
setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 8.5)
c.drawString(ML, y, "Du Mai (posterior spine)   <-   Perineum / Lower Abdomen   ->   Ren Mai (anterior midline)")
y -= 14
c.drawString(ML, y, "                                                        \u2193")
y -= 14
c.drawString(ML, y, "                                            Chong Mai (internal + beside Kidney meridian)")
y -= 24

y = section_label(c, y, "\u201cSea\u201d Titles at a Glance", NAVY, size=10.5)
sea_rows = [
    ("Du Mai (GV)", "Sea of the yang meridians", GV["accent"]),
    ("Ren Mai (CV)", "Sea of the yin meridians", CV["accent"]),
    ("Chong Mai", "Sea of the 12 meridians \u00b7 Sea of blood \u00b7 Sea of the zang-fu organs", CHONG["accent"]),
]
for name, title, accent in sea_rows:
    setfill(c, accent); c.circle(ML + 4, y - 3, 3, fill=1, stroke=0)
    setfill(c, DARK); c.setFont("Lora-Bold", 9)
    c.drawString(ML + 14, y, name)
    setfill(c, GRAY); c.setFont("Lora-Italic", 9)
    c.drawString(ML + 130, y, title)
    y -= 16
y -= 8

y = section_label(c, y, "Only Two Vessels Have Their Own Points", NAVY, size=10.5)
y = draw_paragraph(c,
    "GV (28 points) and CV (24 points) are the only Extraordinary Vessels with dedicated acupuncture "
    "points of their own. The other six -- Chong, Dai, Yang Qiao, Yin Qiao, Yang Wei, and Yin Wei -- "
    "share points with the primary meridians they cross. Those shared points are called coalescent "
    "points (Jiao Hui Xue), distinct from the confluent (opening) points used to clinically access "
    "each vessel.", ML, y, CW, size=9.3, leading=13)

db.end_page()

# ============================================================
# CONFLUENT POINTS OVERVIEW PAGE
# ============================================================
db.new_page()
y = H - 60
setfill(c, NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, "The Eight Confluent Points (Ba Mai Jiao Hui Xue)")
y -= 10
hairline(c, ML, y, RX, rgb=GOLD, w=1)
y -= 20
y = draw_paragraph(c,
    "Confluent points are special acupuncture points -- one per vessel, always located on a primary "
    "meridian -- that connect each Extraordinary Vessel to the 12 regular meridians and are the "
    "clinical \u201copening\u201d points used to access that vessel. The 8 confluent points pair up into 4 "
    "\u201cmaster-couple\u201d combinations, each used together to treat a shared symptom picture.",
    ML, y, CW, size=9.3, leading=13)
y -= 14

for pair_name, master, couple, note in CONFLUENT_PAIRS:
    box_h = 58
    setfill(c, LBLUE); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
    setfill(c, GOLD); c.rect(ML, y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 14, y - 15, pair_name)
    setfill(c, RED); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 14, y - 30, master + "   \u00d7   " + couple)
    setfill(c, GRAY); c.setFont("Lora-Italic", 8)
    ny = draw_paragraph(c, note, ML + 14, y - 44, CW - 24, font="Lora-Italic", size=8, leading=10.5)
    y -= box_h + 10

db.end_page()

# ============================================================
# VESSEL PAGES (each starts on its own page, per architecture rule)
# ============================================================
for vessel in ALL_VESSELS:
    vessel_page(vessel)

db.save()
