#!/usr/bin/env python3
"""AC300 Week 8 Study Guide Classic -- 15 Collaterals, 12 Divergent Channels,
12 Muscle/Sinew Regions, 12 Cutaneous Regions. Reference only (no quiz
content, per Study Guide architecture rule). Organized by TOPIC SYSTEM
(not organ), since this week's content is structural/conceptual rather
than point-by-point. Print + reMarkable via sys.argv[1]."""
import sys
sys.path.insert(0, "/home/claude/ac300wk8")
from reportlab.pdfbase import pdfmetrics
from common_wk8 import (DocBuilder, studyguide_cover, setfill, setstroke, box, hairline,
                         draw_paragraph, wrap_words, section_label, pathway_strip,
                         draw_image_contain, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK,
                         RED, LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM)
from wk8_content import (CIRCUITS, THREE_CIRCUITS_RULE, LUO_POINTS, LUO_EXTRA, LUO_DEFINITION,
                          LUO_WHY_15_LOGIC, LUO_FUNCTION, DIVERGENT_DEFINITION, DIVERGENT_FEATURES,
                          LI_HE_CHU_MERGE, DIVERGENT_CHANNELS, SINEW_DEFINITION, SINEW_FUNCTIONS,
                          SINEW_PATTERN_RULES, SINEW_CLINICAL_NOTE, SINEW_REGIONS,
                          CUTANEOUS_DEFINITION, CUTANEOUS_FUNCTIONS, CUTANEOUS_DIVISIONS,
                          WEEK7_REVIEW_QA, FINAL_EXAM_SUMMARY, READING_NOTE, HOMEWORK_QUIZ_NOTE,
                          ACCENT_LUO, ACCENT_DIVERGENT, ACCENT_SINEW, DIVERGENT_PAIR_NOTES)

OUT = f"/mnt/user-data/outputs/AC300_Week8_StudyGuide_Classic_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 8 Study Guide"
FOOTER = "AC300/AC375 | Week 8 | Collaterals, Divergent, Sinew & Cutaneous | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def page_title(title, accent=NAVY):
    y = H - 60
    setfill(c, accent); c.setFont("Lora-Bold", 15)
    c.drawString(ML, y, title)
    y -= 10
    hairline(c, ML, y, RX, rgb=GOLD, w=1)
    return y - 20


def flag_box(y, lines, w=CW, x=ML):
    bh = len(wrap_words(lines[0], "Lora-Italic", 7.4, w - 16)) * 9.6 + 8
    total_lines = []
    for ln in lines:
        total_lines += wrap_words(ln, "Lora-Italic", 7.4, w - 16)
    bh = len(total_lines) * 9.6 + 10
    box(c, x, y, w, bh, tint(RED, 0.87))
    ty = y - 10
    setfill(c, RED); c.setFont("Lora-Italic", 7.4)
    for ln in total_lines:
        c.drawString(x + 8, ty, ln)
        ty -= 9.6
    return y - bh


# ============================================================
# COVER
# ============================================================
studyguide_cover(
    db,
    title="Week 8 Study Guide",
    subtitle="15 Collaterals \u00b7 12 Divergent Channels \u00b7 12 Muscle Regions \u00b7 12 Cutaneous Regions",
    points_line="No new organ acupoints this week -- structural/conceptual layer built on top of the 12 Primary Meridians",
    covers_bullets=[
        "The Three Circuits framework (Outer/Anterior, Inner/Posterior, Middle) organizing the whole lecture",
        "The 15 Collaterals (Luo-Connecting points) -- all 12 paired points + the 3 that bring the total to 15",
        "The 12 Divergent Channels -- the Li-He-Chu-merge (beginning/organs/exiting/merging) framework, all 6 confluence pairs",
        "The 12 Muscle (Sinew) Regions -- pathway, binding points, and the 4 structural pattern rules",
        "The 12 Cutaneous Regions -- theory, function, and the 3-Yang / 3-Yin lecture diagrams",
        "Week 7 confluent-points review + Dr. Zhang's own exam-focus summary (verbatim, slide 84)",
        "Flagged: homework/quiz status discrepancy (slide text vs. verbal statement) -- see notes",
    ],
    info_lines=[
        f"{HOMEWORK_QUIZ_NOTE}",
        f"{READING_NOTE}",
        "Slides: Dr. Vivian Zhang, Lecture8vivian1119.pdf (85 slides; 1-61 delivered live, 62-85 self-study)",
    ],
)

# ============================================================
# PAGE: THREE CIRCUITS OVERVIEW
# ============================================================
db.new_page()
y = page_title("The Three Circuits -- Dr. Zhang's Organizing Structure")
y = draw_paragraph(c, THREE_CIRCUITS_RULE, ML, y, CW, size=9.3, leading=13)
y -= 16

for circ in CIRCUITS:
    accent = circ["accent"]
    bh = 46
    box(c, ML, y, CW, bh, tint(accent, 0.87))
    setfill(c, accent); c.rect(ML, y - bh, 4, bh, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 14, y - 15, f"{circ['name']}  ({circ['pinyin']})")
    setfill(c, DARK); c.setFont("Lora", 8.4)
    c.drawString(ML + 14, y - 29, "Pairs: " + "   |   ".join(circ["pairs"]))
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.8)
    draw_paragraph(c, circ["note"], ML + 14, y - 41, CW - 28, font="Lora-Italic", size=7.6, leading=9.6)
    y -= bh + 10

y -= 10
y = section_label(c, y, "This Week's Four New Layers (all built on TOP of the 12 primary meridians)", NAVY, size=10)
layer_rows = [
    ("15 Collaterals (Luo Mai)", ACCENT_LUO, "ON the surface -- links each paired meridian via one Luo-Connecting point."),
    ("12 Divergent Channels (Jing Bie)", ACCENT_DIVERGENT, "run DEEP inside -- no points, no pertaining organ; reinforce the organ relationship."),
    ("12 Muscle/Sinew Regions (Jing Jin)", ACCENT_SINEW, "cover a WIDE band along each meridian's course -- muscle/joint function only, no organs."),
    ("12 Cutaneous Regions (Pi Bu)", (0.35, 0.35, 0.35), "the OUTERMOST layer -- where meridian qi is reflected on the skin surface."),
]
for name, accent, desc in layer_rows:
    setfill(c, accent); c.circle(ML + 4, y - 3, 3.4, fill=1, stroke=0)
    setfill(c, DARK); c.setFont("Lora-Bold", 9)
    c.drawString(ML + 15, y, name + ":")
    lw = c.stringWidth(name + ":  ", "Lora-Bold", 9)
    setfill(c, GRAY); c.setFont("Lora-Italic", 8.6)
    rest = wrap_words(desc, "Lora-Italic", 8.6, CW - 15 - lw - 4)
    c.drawString(ML + 15 + lw, y, rest[0])
    y -= 13
    for extra in rest[1:]:
        c.drawString(ML + 15, y, extra)
        y -= 13
y -= 14

y = section_label(c, y, "Depth Progression -- Surface to Core", NAVY, size=10)
setfill(c, DARK); c.setFont("Lora", 8.6)
y = draw_paragraph(c, "Su Wen's disease-transmission order (used again on the Cutaneous Regions page) doubles "
                       "as a map of how deep each of this week's four systems sits, from the skin inward:",
                       ML, y, CW, size=8.6, leading=11.6)
y -= 8
depth_steps = [
    ("1. Cutaneous Regions", (0.35, 0.35, 0.35), "outermost -- qi reflected on the skin surface (Pi Bu)"),
    ("2. Collaterals", ACCENT_LUO, "surface -- links paired meridians via one point each (Luo Mai)"),
    ("3. Primary Meridians", NAVY, "the main channels themselves, with their full point sets"),
    ("4. Divergent Channels", ACCENT_DIVERGENT, "deepest -- no points, reinforce organ links (Jing Bie)"),
]
step_w = (CW - 3 * 14) / 4
for i, (label, accent, note) in enumerate(depth_steps):
    x0 = ML + i * (step_w + 14)
    bh = 62
    box(c, x0, y, step_w, bh, tint(accent, 0.88))
    setfill(c, accent); c.rect(x0, y - bh, step_w, 3, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 7.6)
    ty = y - 13
    for ln in wrap_words(label, "Lora-Bold", 7.6, step_w - 12):
        c.drawString(x0 + 6, ty, ln); ty -= 9.4
    ty -= 3
    setfill(c, DARK); c.setFont("Lora-Italic", 6.8)
    for ln in wrap_words(note, "Lora-Italic", 6.8, step_w - 12):
        c.drawString(x0 + 6, ty, ln); ty -= 8.6
    if i < 3:
        setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 11)
        c.drawCentredString(x0 + step_w + 7, y - bh / 2, "->")
y -= bh + 14

y = section_label(c, y, "Note: Muscle/Sinew Regions Sit Outside This Ladder", GOLD_DARK, size=9)
setfill(c, DARK); c.setFont("Lora", 8.4)
y = draw_paragraph(c, "Muscle Regions (Jing Jin) don't fit neatly into the surface-to-core depth ladder above -- "
                       "they cover a WIDE BAND along each meridian's course (muscle/joint tissue specifically), "
                       "rather than sitting at one consistent depth. Think of them as a separate, parallel layer "
                       "keyed to function (movement) rather than to depth.",
                       ML, y, CW, size=8.4, leading=11.2)
db.end_page()

# ============================================================
# PAGE: 15 COLLATERALS -- THEORY + TABLE (12 paired)
# ============================================================
db.new_page()
y = page_title("The 15 Collaterals (Luo Mai) -- Definition & Logic", ACCENT_LUO)
y = draw_paragraph(c, LUO_DEFINITION, ML, y, CW, size=9, leading=12.4)
y -= 10
y = section_label(c, y, "Why 15, Not 12?", ACCENT_LUO, size=9.5)
y = draw_paragraph(c, LUO_WHY_15_LOGIC, ML, y, CW, size=8.6, leading=11.6)
y -= 8
y = section_label(c, y, "Function -- What a Luo-Connecting Point Does", ACCENT_LUO, size=9.5)
y = draw_paragraph(c, LUO_FUNCTION, ML, y, CW, size=8.6, leading=11.6)
y -= 12

y = section_label(c, y, "The 12 Paired-Meridian Luo-Connecting Points", ACCENT_LUO, size=10)
hdr_h = 14
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(ML + 6, y - hdr_h + 4, "MERIDIAN")
c.drawString(ML + 130, y - hdr_h + 4, "LUO POINT")
c.drawString(ML + 240, y - hdr_h + 4, "CONNECTS TO (PAIR)")
y -= hdr_h
row_h = 16.5


def _short_name(full):
    return full.split(",")[0].replace(" Meridian", "").strip()


for i, luo in enumerate(LUO_POINTS):
    bg = tint(luo["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, DARK); c.setFont("Lora", 7.6)
    c.drawString(ML + 6, y - row_h + 5, f"{_short_name(luo['meridian'])} ({luo['abbr']})")
    setfill(c, luo["accent"]); c.setFont("Lora-Bold", 7.8)
    c.drawString(ML + 130, y - row_h + 5, luo["point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    partner_txt = _short_name(luo["partner"]) + ("  [self-study]" if luo.get("self_study") else "")
    c.drawString(ML + 240, y - row_h + 5, partner_txt)
    y -= row_h
y -= 8
setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
c.drawString(ML, y, "[self-study] = GB/LR collaterals were slide-deck content Dr. Zhang did not reach live this lecture.")
y -= 16

y = section_label(c, y, "Rule of Thumb (from lecture)", ACCENT_LUO, size=9)
setfill(c, DARK); c.setFont("Lora", 8.2)
y = draw_paragraph(c, "Luo-Connecting points of HAND meridians cluster around the wrist. Luo-Connecting "
                       "points of FOOT meridians cluster around the ankle (malleolus). Use this to "
                       "sanity-check any point location you're unsure of.", ML, y, CW, size=8.2, leading=11)
y -= 14

y = section_label(c, y, "Special-Point Identity Overlaps (from Week 7 -- these are the same points!)", ACCENT_LUO, size=9)
overlap_rows = [
    ("LU 7 Lieque", "Luo-Connecting point of Lung", "Confluent (opening) point of Ren Mai (CV)"),
    ("SP 4 Gongsun", "Luo-Connecting point of Spleen", "Confluent (opening) point of Chong Mai"),
    ("PC 6 Neiguan", "Luo-Connecting point of Pericardium", "Confluent (opening) point of Yin Wei Mai"),
    ("SJ 5 Waiguan", "Luo-Connecting point of Sanjiao", "Confluent (opening) point of Yang Wei Mai"),
]
hdr_h2 = 13
setfill(c, GOLD_DARK); c.rect(ML, y - hdr_h2, CW, hdr_h2, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7)
c.drawString(ML + 6, y - hdr_h2 + 3.5, "POINT")
c.drawString(ML + 90, y - hdr_h2 + 3.5, "AS A LUO POINT")
c.drawString(ML + 300, y - hdr_h2 + 3.5, "ALSO SERVES AS")
y -= hdr_h2
row_h2 = 15
for i, (pt, luo_role, other_role) in enumerate(overlap_rows):
    bg = tint(GOLD, 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h2, bg)
    setfill(c, DARK); c.setFont("Lora-Bold", 7.4)
    c.drawString(ML + 6, y - row_h2 + 4.5, pt)
    c.setFont("Lora", 7.2)
    c.drawString(ML + 90, y - row_h2 + 4.5, luo_role)
    setfill(c, RED); c.setFont("Lora-Italic", 7.2)
    c.drawString(ML + 300, y - row_h2 + 4.5, other_role)
    y -= row_h2
y -= 8
setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
y = draw_paragraph(c, "This is exactly the \u201cone point, multiple jobs\u201d principle Dr. Zhang flagged in "
                       "Week 7 -- a point's clinical reach grows with each special-point identity it carries.",
                       ML, y, CW, font="Lora-Italic", size=7.4, leading=9.6)
db.end_page()

# ============================================================
# PAGES: COLLATERAL PATHWAY DIAGRAMS -- Dr. Zhang's own lecture figures,
# one per meridian (slides 19-20, 29-30, 39-40, 47-48, 58-59, 66-67)
# ============================================================

def collateral_diagram_page(title, abbrs, slide_note):
    db.new_page()
    y = page_title(title, ACCENT_LUO)
    col_w = (CW - 16) / 2
    cell_h = 218
    for i, abbr in enumerate(abbrs):
        luo = next(l for l in LUO_POINTS if l["abbr"] == abbr)
        col, row = i % 2, i // 2
        x0 = ML + col * (col_w + 16)
        y0 = y - row * (cell_h + 10)
        draw_image_contain(c, f"LUO_{abbr}", x0, y0, col_w, 190, luo["accent"])
        setfill(c, NAVY); c.setFont("Lora-Bold", 10)
        c.drawCentredString(x0 + col_w / 2, y0 - 202, f"{_short_name(luo['meridian'])} ({abbr})")
        setfill(c, luo["accent"]); c.setFont("Lora-Bold", 8.6)
        c.drawCentredString(x0 + col_w / 2, y0 - 215, luo["point"])
    y -= 3 * (cell_h + 10) + 10
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    draw_paragraph(c, slide_note, ML, y, CW, font="Lora-Italic", size=7.2, leading=9.4)
    db.end_page()


collateral_diagram_page(
    "Collateral Pathway Diagrams -- Outer & Inner Circuit",
    ["LU", "LI", "ST", "SP", "HT", "SI"],
    "Lecture Fig. -- Lecture8vivian1119.pdf, slides 19-20 (LU/LI), 29-30 (ST/SP), 39-40 (HT/SI). Dr. Zhang.",
)
collateral_diagram_page(
    "Collateral Pathway Diagrams -- Inner & Middle Circuit",
    ["BL", "KI", "PC", "SJ", "GB", "LR"],
    "Lecture Fig. -- Lecture8vivian1119.pdf, slides 47-48 (BL/KI), 58-59 (PC/SJ), 66-67 (GB/LR, self-study). Dr. Zhang.",
)

# ============================================================
# PAGE: 15 COLLATERALS -- THE 3 EXTRA
# ============================================================
db.new_page()
y = page_title("The 3 \u201cExtra\u201d Collaterals -- Completing the Set of 15", ACCENT_LUO)
for extra in LUO_EXTRA:
    bh = 92
    box(c, ML, y, CW, bh, tint(ACCENT_LUO, 0.9))
    setfill(c, ACCENT_LUO); c.rect(ML, y - bh, 4, bh, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 14, y - 16, extra["name"])
    setfill(c, RED); c.setFont("Lora-Bold", 9.5)
    c.drawString(ML + 14, y - 30, extra["point"])
    setfill(c, DARK); c.setFont("Lora", 8.2)
    ny = draw_paragraph(c, "Course: " + extra["course"], ML + 14, y - 44, CW - 28, size=8.2, leading=10.6)
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 7.8)
    draw_paragraph(c, "Why it exists: " + extra["why"], ML + 14, ny - 4, CW - 28, font="Lora-Italic", size=7.8, leading=10)
    y -= bh + 12

y -= 4
y = section_label(c, y, "Picture It", ACCENT_LUO, size=9.5)
setfill(c, DARK); c.setFont("Lora", 8.6)
y = draw_paragraph(c,
    "CV's collateral covers the FRONT midline of the trunk. GV's collateral covers the BACK midline "
    "of the trunk. The Spleen's Great Collateral covers the LATERAL side of the chest -- the one "
    "region the other 14 collaterals leave unguarded. Front + Back + Side = complete surface coverage, "
    "which is the whole point of a system meant to \u201ckeep the whole body harmony\u201d (Dr. Zhang, live).",
    ML, y, CW, size=8.6, leading=11.6)
y -= 16

col_w3 = (CW - 24) / 3
trio = [("FRONT", "CV 15 Jiuwei", "Ren Mai collateral", ACCENT_LUO),
        ("BACK", "GV 1 Changqiang", "Du Mai collateral", ACCENT_LUO),
        ("SIDE", "SP 21 Dabao", "Spleen Great Collateral", ACCENT_LUO)]
for i, (dir_label, pt, desc, accent) in enumerate(trio):
    x0 = ML + i * (col_w3 + 12)
    bh = 62
    box(c, x0, y, col_w3, bh, tint(accent, 0.87))
    setfill(c, accent); c.rect(x0, y - bh, col_w3, 3, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 11)
    c.drawCentredString(x0 + col_w3 / 2, y - 20, dir_label)
    setfill(c, RED); c.setFont("Lora-Bold", 9)
    c.drawCentredString(x0 + col_w3 / 2, y - 36, pt)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawCentredString(x0 + col_w3 / 2, y - 50, desc)
y -= bh + 16

y = section_label(c, y, "Memory Aid", GOLD_DARK, size=9.5)
setfill(c, DARK); c.setFont("Lora-Italic", 8.4)
y = draw_paragraph(c,
    "The 12 paired-meridian Luo points are ALL located on the LIMBS (wrist or ankle region, per the "
    "\u201crule of thumb\u201d above). The 3 extra Luo points are the exception -- all three are located on "
    "the TRUNK (sternum/Jiuwei, perineum/Changqiang, lateral chest/Dabao), because their job is to "
    "cover trunk surface area no limb-based point could reach.",
    ML, y, CW, font="Lora-Italic", size=8.4, leading=11.2)
db.end_page()

# ============================================================
# PAGE: 12 DIVERGENT CHANNELS -- DEFINITION, FEATURES, TABLE
# ============================================================
db.new_page()
y = page_title("The 12 Divergent Channels (Jing Bie)", ACCENT_DIVERGENT)
y = draw_paragraph(c, DIVERGENT_DEFINITION, ML, y, CW, size=8.8, leading=12)
y -= 8
y = section_label(c, y, "Key Features", ACCENT_DIVERGENT, size=9.5)
setfill(c, DARK); c.setFont("Lora", 8.2)
for f in DIVERGENT_FEATURES:
    lines = wrap_words("\u2022 " + f, "Lora", 8.2, CW - 6)
    for ln in lines:
        c.drawString(ML, y, ln); y -= 10.6
    y -= 1
y -= 6
y = section_label(c, y, "The Li - He - Chu - Merge Framework", ACCENT_DIVERGENT, size=9.5)
y = draw_paragraph(c, LI_HE_CHU_MERGE, ML, y, CW, size=8.2, leading=11)
y -= 10

y = section_label(c, y, "Master Table -- All 12 at a Glance", ACCENT_DIVERGENT, size=10)
hdr_h = 14
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 6.8)
c.drawString(ML + 5, y - hdr_h + 4, "MERIDIAN")
c.drawString(ML + 95, y - hdr_h + 4, "BEGINNING")
c.drawString(ML + 230, y - hdr_h + 4, "EXITING")
c.drawString(ML + 330, y - hdr_h + 4, "MERGES INTO")
y -= hdr_h
row_h = 15.5


def _fit(text, font, size, maxw):
    if pdfmetrics.stringWidth(text, font, size) <= maxw:
        return text
    while text and pdfmetrics.stringWidth(text + "...", font, size) > maxw:
        text = text[:-1]
    return text + "..."


def _clip_paren(text):
    return text.split(" (")[0].strip()


for i, d in enumerate(DIVERGENT_CHANNELS):
    bg = tint(d["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, d["accent"]); c.setFont("Lora-Bold", 6.8)
    c.drawString(ML + 5, y - row_h + 4.5, d["meridian"] + (" *" if d.get("self_study") else ""))
    setfill(c, DARK); c.setFont("Lora", 6.5)
    c.drawString(ML + 95, y - row_h + 4.5, _fit(_clip_paren(d["beginning"]), "Lora", 6.5, 130))
    c.drawString(ML + 230, y - row_h + 4.5, _fit(_clip_paren(d["exiting"]), "Lora", 6.5, 95))
    c.drawString(ML + 330, y - row_h + 4.5, _fit(d["merging"], "Lora", 6.5, RX - ML - 330 - 4))
    y -= row_h
setfill(c, GRAY); c.setFont("Lora-Italic", 7)
c.drawString(ML, y - 9, "* GB/LR divergent channels: self-study slide content, not reached live.")
y -= 24

y = section_label(c, y, "Why the Divergent Channels Matter Clinically", ACCENT_DIVERGENT, size=9.5)
setfill(c, DARK); c.setFont("Lora", 8.4)
y = draw_paragraph(c,
    "Because a Divergent Channel runs DEEPER than its primary meridian and reaches organs/systems the "
    "primary meridian's own course doesn't directly pass through, it explains symptom patterns that "
    "otherwise look like they \u201cshouldn't\u201d belong to a given channel -- e.g. why Stomach-channel "
    "points can address disorders of the eye (ST divergent channel reaches the eye), or why "
    "Small-Intestine points can be chosen for heart-adjacent chest symptoms (SI divergent channel "
    "reaches the heart).",
    ML, y, CW, size=8.4, leading=11.4)
y -= 10
y = section_label(c, y, "6 Confluence Pairs at a Glance", ACCENT_DIVERGENT, size=9.5)
setfill(c, DARK); c.setFont("Lora", 8.2)
pair_summary = "  \u00b7  ".join(["LU + LI", "ST + SP", "HT + SI", "BL + KI", "PC + SJ", "GB + LR"])
y = draw_paragraph(c, pair_summary, ML, y, CW, size=8.2, leading=11)
db.end_page()

# ============================================================
# PAGES: DIVERGENT CHANNEL CONFLUENCE PAIRS (6 pages)
# ============================================================
PAIR_GROUPS = [
    ("LU + LI Divergent Confluence", DIVERGENT_CHANNELS[0], DIVERGENT_CHANNELS[1]),
    ("ST + SP Divergent Confluence", DIVERGENT_CHANNELS[2], DIVERGENT_CHANNELS[3]),
    ("HT + SI Divergent Confluence", DIVERGENT_CHANNELS[4], DIVERGENT_CHANNELS[5]),
    ("BL + KI Divergent Confluence", DIVERGENT_CHANNELS[6], DIVERGENT_CHANNELS[7]),
    ("PC + SJ Divergent Confluence", DIVERGENT_CHANNELS[8], DIVERGENT_CHANNELS[9]),
    ("GB + LR Divergent Confluence", DIVERGENT_CHANNELS[10], DIVERGENT_CHANNELS[11]),
]


def divergent_pair_page(title, a, b):
    db.new_page()
    accent = a["accent"]
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, accent); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 15)
    c.drawString(ML + 14, bar_bot + 9, title)
    if a.get("self_study"):
        c.setFont("Lora-Italic", 8.5)
        c.drawRightString(RX - 6, bar_bot + 11, "Self-study slide content (not reached live)")
    y = bar_bot - 22
    col_w = (CW - 20) / 2
    left_x, right_x = ML, ML + col_w + 20
    bottoms = []

    for meridian, x0 in [(a, left_x), (b, right_x)]:
        yy = y
        setfill(c, meridian["accent"]); c.setFont("Lora-Bold", 11)
        c.drawString(x0, yy, meridian["meridian"])
        yy -= 16
        facts = [("Beginning", meridian["beginning"]), ("Organs/Systems", meridian["organs"]),
                 ("Exiting", meridian["exiting"]), ("Merges Into", meridian["merging"])]
        for label, val in facts:
            setfill(c, GRAY); c.setFont("Lora-Bold", 7.6)
            c.drawString(x0, yy, label + ":")
            yy -= 10.5
            setfill(c, DARK); c.setFont("Lora", 8)
            lines = wrap_words(val, "Lora", 8, col_w)
            for ln in lines:
                c.drawString(x0, yy, ln); yy -= 10.6
            yy -= 4
        yy -= 6
        setfill(c, meridian["accent"]); c.setFont("Lora-Bold", 8.5)
        c.drawString(x0, yy, "Course, Step by Step")
        yy -= 16
        # Break the narrative into a numbered pathway strip using the "->" arrows
        raw_steps = [s.strip() for s in meridian["narrative"].replace("Deriving from", "").split(".") if s.strip()]
        # Prefer splitting on the arrow chain when present for cleaner steps
        if "->" in meridian["narrative"]:
            chain = meridian["narrative"]
            # Split into sentence-level chunks, each chunk may itself contain arrows
            sentences = [s.strip() for s in chain.split(".") if s.strip()]
            steps = sentences
        else:
            steps = raw_steps
        yy = pathway_strip(c, steps, x0, yy, col_w, meridian["accent"], size=8.6, node_r=7.5)
        bottoms.append(yy)

    y = min(bottoms) - 16
    hairline(c, ML, y, RX, rgb=GOLD, w=0.7)
    y -= 16
    note = DIVERGENT_PAIR_NOTES.get(title.split(" Divergent")[0], "")
    if note:
        y = section_label(c, y, "Clinical Relevance", accent, size=9.5)
        setfill(c, DARK); c.setFont("Lora-Italic", 8.6)
        y = draw_paragraph(c, note, ML, y, CW, font="Lora-Italic", size=8.6, leading=11.6)
    y -= 14

    # Compare-the-pair box: shared exiting/merging structure
    y = section_label(c, y, "Compare the Pair", accent, size=9.5)
    same_exit = a["exiting"].split(" (")[0].strip().lower() == b["exiting"].split(" (")[0].strip().lower()
    compare_lines = []
    if same_exit:
        compare_lines.append(f"Both channels exit to the surface at the same landmark: {a['exiting'].split(' (')[0].strip()}.")
    else:
        compare_lines.append(f"{a['meridian'].split(' (')[0]} exits at {a['exiting'].split(' (')[0].strip()}; "
                              f"{b['meridian'].split(' (')[0]} exits at {b['exiting'].split(' (')[0].strip()} -- different surface landmarks.")
    yang_side = a if "itself" in a["merging"] else b
    yang_organ = yang_side["meridian"].split(" (")[0]
    compare_lines.append(f"Both ultimately merge into the {yang_organ} channel -- every Yin "
                          f"divergent channel merges into its paired Yang channel, never resurfacing as a "
                          f"separate Yin pathway.")
    setfill(c, DARK); c.setFont("Lora", 8.4)
    for cl in compare_lines:
        lines = wrap_words("\u2022 " + cl, "Lora", 8.4, CW - 6)
        for ln in lines:
            c.drawString(ML, y, ln); y -= 11
        y -= 2

    db.end_page()


for title, a, b in PAIR_GROUPS:
    divergent_pair_page(title, a, b)

# ============================================================
# PAGES: 12 MUSCLE/SINEW REGIONS (by circuit, 3 pages)
# ============================================================
SINEW_BY_CIRCUIT = {"outer": [], "inner": [], "middle": []}
for s in SINEW_REGIONS:
    SINEW_BY_CIRCUIT[s["circuit"]].append(s)

db.new_page()
y = page_title("The 12 Muscle (Sinew) Regions -- Definition & Rules", ACCENT_SINEW)
y = draw_paragraph(c, SINEW_DEFINITION, ML, y, CW, size=8.8, leading=12)
y -= 8
y = section_label(c, y, "Functions", ACCENT_SINEW, size=9.5)
setfill(c, DARK); c.setFont("Lora", 8.2)
for f in SINEW_FUNCTIONS:
    lines = wrap_words("\u2022 " + f, "Lora", 8.2, CW - 6)
    for ln in lines:
        c.drawString(ML, y, ln); y -= 10.6
    y -= 1
y -= 8
y = section_label(c, y, "The 4 Structural Pattern Rules", ACCENT_SINEW, size=9.5)
for r in SINEW_PATTERN_RULES:
    lines = wrap_words("\u2022 " + r, "Lora", 8.4, CW - 6)
    for ln in lines:
        setfill(c, DARK); c.setFont("Lora", 8.4)
        c.drawString(ML, y, ln); y -= 11
    y -= 1
y -= 8
y = section_label(c, y, "Clinical Note (from live Q&A)", ACCENT_SINEW, size=9.5)
y = draw_paragraph(c, SINEW_CLINICAL_NOTE, ML, y, CW, size=8.2, leading=11)
db.end_page()


def sinew_circuit_page(circuit_key, circuit_label):
    db.new_page()
    circ = next(cc for cc in CIRCUITS if cc["key"] == circuit_key)
    y = page_title(f"Muscle Regions -- {circuit_label}", circ["accent"])
    regions = SINEW_BY_CIRCUIT[circuit_key]
    img_w = 210
    for s in regions:
        bh = 148
        text_w = CW - img_w - 30
        box(c, ML, y, CW, bh, tint(s["accent"], 0.9))
        setfill(c, s["accent"]); c.rect(ML, y - bh, 4, bh, fill=1, stroke=0)
        setfill(c, NAVY); c.setFont("Lora-Bold", 12)
        title_txt = s["meridian"] + (" [self-study]" if s.get("self_study") else "")
        c.drawString(ML + 16, y - 20, title_txt)
        setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 9)
        by = draw_paragraph(c, "Binds at: " + s["binds"], ML + 16, y - 38, text_w, font="Lora-Bold", size=9, leading=11.5)
        setfill(c, DARK); c.setFont("Lora", 9)
        draw_paragraph(c, "Pathway: " + s["path"], ML + 16, by - 6, text_w, size=9, leading=12)
        draw_image_contain(c, f"SINEW_{s['abbr']}", ML + CW - img_w, y - 6, img_w, bh - 12, s["accent"])
        y -= bh + 12
    if circuit_key == "inner":
        setfill(c, GRAY); c.setFont("Lora-Italic", 6.8)
        draw_paragraph(c,
            "Note: the source lecture slide for the Kidney diagram above is mistitled \u201cMuscle Region of "
            "Foot Taiyang (Bladder)\u201d in Dr. Zhang's deck, but its body text and image content are the "
            "Kidney muscle region -- a source-slide labeling error, flagged here rather than silently "
            "corrected in the image itself. The text card is labeled correctly (Kidney).",
            ML, y, CW, font="Lora-Italic", size=6.8, leading=8.8)
        y -= 22
    db.end_page()


sinew_circuit_page("outer", "Outer Circuit (LU/LI, ST/SP)")
sinew_circuit_page("inner", "Inner Circuit (HT/SI, BL/KI)")
sinew_circuit_page("middle", "Middle Circuit (PC/SJ, GB/LR)")

# ============================================================
# PAGE: 12 CUTANEOUS REGIONS
# ============================================================
db.new_page()
y = page_title("The 12 Cutaneous Regions (Pi Bu)", NAVY)
y -= 2
setfill(c, RED); c.setFont("Lora-Italic", 8)
c.drawString(ML, y, "Self-study slide content (slides 79-83) -- not reached live this lecture.")
y -= 14
y = draw_paragraph(c, CUTANEOUS_DEFINITION, ML, y, CW, size=8.8, leading=12)
y -= 10
y = section_label(c, y, "Three Functions (Su Wen, Chapter 56)", NAVY, size=9.5)
for title, detail in CUTANEOUS_FUNCTIONS:
    setfill(c, DARK); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML, y, title); y -= 11
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.8)
    y = draw_paragraph(c, detail, ML + 10, y, CW - 10, font="Lora-Italic", size=7.8, leading=10.2)
    y -= 6

col_w = (CW - 20) / 2
iy = draw_image_contain(c, "CUTANEOUS_YANG", ML, y, col_w, 190, NAVY)
setfill(c, GRAY); c.setFont("Lora-Italic", 7.3)
c.drawCentredString(ML + col_w / 2, iy - 11, "Lecture Fig. \u2014 3 Yang Cutaneous Regions")
setfill(c, LGRAY); c.setFont("Lora-Italic", 6.6)
c.drawCentredString(ML + col_w / 2, iy - 21, "Lecture8vivian1119.pdf, slide 82 (Dr. Zhang)")
db.end_page()

# ============================================================
# PAGE: CUTANEOUS REGIONS PT 2 + WEEK 7 RECAP + EXAM SUMMARY
# ============================================================
db.new_page()
y = page_title("Cutaneous Regions (cont.) + Week 7 Recap + Exam Focus", NAVY)
col_w = (CW - 20) / 2
iy = draw_image_contain(c, "CUTANEOUS_YIN", ML, y, col_w, 175, NAVY)
setfill(c, GRAY); c.setFont("Lora-Italic", 7.3)
c.drawCentredString(ML + col_w / 2, iy - 11, "Lecture Fig. \u2014 3 Yin Cutaneous Regions")
setfill(c, LGRAY); c.setFont("Lora-Italic", 6.6)
c.drawCentredString(ML + col_w / 2, iy - 21, "Lecture8vivian1119.pdf, slide 83 (Dr. Zhang)")

right_x = ML + col_w + 20
ry = y
ry = section_label(c, ry, "The 6 Divisions", NAVY, size=9.5, x=right_x)
for div in CUTANEOUS_DIVISIONS:
    setfill(c, DARK); c.setFont("Lora-Bold", 8); c.drawString(right_x, ry, div["group"]); ry -= 11
    setfill(c, GRAY); c.setFont("Lora", 7.6)
    for m in div["members"]:
        c.drawString(right_x + 8, ry, "\u2022 " + m); ry -= 10
    ry -= 4
ry -= 4
setfill(c, RED); c.setFont("Lora-Italic", 7.4)
ry = draw_paragraph(c, "Transmission order (disease): Skin -> Collaterals -> Meridians -> Fu organs -> "
                       "Zang organs -- deeper each step, matching how superficial-to-deep these four new "
                       "systems (Cutaneous -> Collaterals -> Divergent -> organs) are taught this week.",
                       right_x, ry, col_w, font="Lora-Italic", size=7.4, leading=9.6)

y = min(iy, ry) - 22
hairline(c, ML, y, RX, rgb=GOLD, w=0.8)
y -= 16
y = section_label(c, y, "Week 7 Recap \u2014 the 8 Confluent Points (bridge review)", GOLD_DARK, size=9.5)
setfill(c, DARK); c.setFont("Lora-Italic", 7.8)
y = draw_paragraph(c, "Dr. Zhang opened Lecture 8 with a live Q&A review of the 8 Extraordinary Vessels' "
                       "confluent points before starting new content -- see the Week 8 Cram Sheet / PLA for "
                       "the full Q&A. Reference table (Dr. Zhang's own review slide):",
                       ML, y, CW, font="Lora-Italic", size=7.8, leading=10.2)
y -= 6
iy2 = draw_image_contain(c, "CONFLUENT_REVIEW", ML, y, CW, 175, GOLD_DARK)
setfill(c, LGRAY); c.setFont("Lora-Italic", 6.6)
c.drawCentredString(ML + CW / 2, iy2 - 10, "Lecture8vivian1119.pdf, slide 78 (Dr. Zhang) \u2014 Week 7 confluent points review")
y = iy2 - 26
hairline(c, ML, y, RX, rgb=GOLD, w=0.8)
y -= 18
y = section_label(c, y, "Dr. Zhang's Own Exam-Focus Summary (verbatim, slide 84)", RED, size=10)
setfill(c, DARK); c.setFont("Lora-Italic", 8.6)
y = draw_paragraph(c, FINAL_EXAM_SUMMARY, ML, y, CW, font="Lora-Italic", size=8.6, leading=11.6)
db.end_page()

db.save()
