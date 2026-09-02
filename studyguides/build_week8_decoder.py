#!/usr/bin/env python3
"""AC300 Week 8 Special Points Decoder -- standalone. This week's special-
point category IS the 15 Luo-Connecting points (the first week they get a
full drillable treatment of their own, rather than being introduced
alongside an organ meridian). Leads with Luo points in full, then gives a
cumulative recap of every other special-point category, with an A/B/C
tiering pass per Jon's rolling-tiering plan (piloted Week 6). Print +
reMarkable."""
import sys
sys.path.insert(0, "/home/claude/ac300wk8")
from common_wk8 import (DocBuilder, setfill, setstroke, box, hairline, draw_paragraph,
                         wrap_words, W, H, ML, MR, RX, CW, NAVY, GOLD, GOLD_DARK, RED,
                         LBLUE, DARK, GRAY, LGRAY, WHITE, CARD_BG, tint, EDITION, IS_RM,
                         EDLABEL)
from wk8_content import (LUO_POINTS, LUO_EXTRA, LUO_DEFINITION, LUO_WHY_15_LOGIC,
                          LUO_FUNCTION, ACCENT_LUO)

OUT = f"/mnt/user-data/outputs/AC300_Week8_SpecialPointsDecoder_{'reMarkable' if IS_RM else 'Print'}.pdf"
DOC_LABEL = "Week 8 Special Points Decoder"
FOOTER = "AC300/AC375 | Week 8 Special Points Decoder | Luo-Connecting Points | VUIM Summer 2026"

db = DocBuilder(OUT, DOC_LABEL, FOOTER)
c = db.c


def title_bar(title, subtitle_right=None):
    bar_top, bar_bot = H - 46, H - 74
    setfill(c, ACCENT_LUO); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 14)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        c.setFont("Lora-Italic", 8.5)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot - 12


def _short(full):
    return full.split(",")[0].replace(" Meridian", "").strip()


# ============================================================
# COVER
# ============================================================
db.new_page(bare=True)
y = H - 60
setfill(c, GOLD); c.setFont("Lora-Bold", 11)
c.drawString(ML, y, "WEEK 8")
c.setFont("Lora-Italic", 10)
c.drawRightString(RX, y, EDLABEL)
y -= 40
setfill(c, NAVY); c.setFont("Lora-Bold", 28)
c.drawString(ML, y, "Special Points Decoder")
y -= 28
setfill(c, ACCENT_LUO); c.setFont("Lora-Bold", 17)
c.drawString(ML, y, "The 15 Collaterals \u2014 Luo-Connecting Points, in Full")
y -= 22
setfill(c, GRAY); c.setFont("Lora-Italic", 11)
c.drawString(ML, y, "Standalone reference \u2014 pairs with the Week 8 Study Guide")
y -= 18
hairline(c, ML, y, RX, rgb=GOLD, w=1.2)
y -= 28
setfill(c, ACCENT_LUO); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "This Decoder Covers:")
y -= 20
setfill(c, DARK); c.setFont("Lora", 10.5)
bullets = [
    "All 15 Luo-Connecting Points, in full \u2014 the star special-point category this week",
    "The \u201cwhy 15, not 12\u201d structural logic, and the front/back/side coverage principle",
    "Special-point identity overlaps \u2014 points that are BOTH a Luo point AND a Confluent point",
    "A/B/C tiered cumulative recap of every other special-point category (Yuan-Source through Crossing Points), rolled forward from the Week 6 pilot",
]
for b in bullets:
    setfill(c, GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(c, DARK)
    lines = wrap_words(b, "Lora", 10.5, CW - 20)
    for i, l in enumerate(lines):
        c.drawString(ML + 14, y - i * 13, l)
    y -= 13 * max(1, len(lines)) + 4

y -= 8
box_h = 54
box(c, ML, y, CW, box_h, tint(ACCENT_LUO, 0.88))
setfill(c, DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 16, y - 18, "The Luo-Connecting point IS the special-point content for this week --")
c.drawString(ML + 16, y - 32, "no new organ-based categories (Yuan-Source, He-Sea, etc.) are introduced.")
c.drawString(ML + 16, y - 46, "GB/LR Luo points are self-study slide content, flagged accordingly below.")
y -= box_h + 40
setfill(c, GRAY); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, 40, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno  |  D.AcHM Candidate  |  VUIM")
db.end_page()

# ============================================================
# PAGE: Luo Points -- full drillable content, all 15
# ============================================================
db.new_page()
y = title_bar("The 15 Luo-Connecting Points (Luo Mai)", "This week's star category")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c, LUO_DEFINITION, ML, y, CW, size=9.1, leading=12.3)
y -= 6
y = draw_paragraph(c, LUO_FUNCTION, ML, y, CW, size=9.1, leading=12.3)
y -= 12

hdr_h = 14
setfill(c, NAVY); c.rect(ML, y - hdr_h, CW, hdr_h, fill=1, stroke=0)
setfill(c, WHITE); c.setFont("Lora-Bold", 7.4)
c.drawString(ML + 6, y - hdr_h + 4, "MERIDIAN")
c.drawString(ML + 145, y - hdr_h + 4, "LUO POINT")
c.drawString(ML + 260, y - hdr_h + 4, "CONNECTS TO")
y -= hdr_h
row_h = 17
for i, luo in enumerate(LUO_POINTS):
    bg = tint(luo["accent"], 0.9) if i % 2 == 0 else WHITE
    box(c, ML, y, CW, row_h, bg)
    setfill(c, DARK); c.setFont("Lora", 7.8)
    c.drawString(ML + 6, y - row_h + 5.5, f"{_short(luo['meridian'])} ({luo['abbr']})")
    setfill(c, luo["accent"]); c.setFont("Lora-Bold", 8)
    c.drawString(ML + 145, y - row_h + 5.5, luo["point"])
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.3)
    partner_txt = _short(luo["partner"]) + ("  [self-study]" if luo.get("self_study") else "")
    c.drawString(ML + 260, y - row_h + 5.5, partner_txt)
    y -= row_h
for extra in LUO_EXTRA:
    box(c, ML, y, CW, row_h, tint(GOLD, 0.88))
    setfill(c, DARK); c.setFont("Lora", 7.8)
    c.drawString(ML + 6, y - row_h + 5.5, extra["name"])
    setfill(c, GOLD_DARK); c.setFont("Lora-Bold", 8)
    c.drawString(ML + 260, y - row_h + 5.5, extra["point"])
    y -= row_h
y -= 10
setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
c.drawString(ML, y, "[self-study] = GB/LR collaterals were slide-deck content Dr. Zhang did not reach live.")
db.end_page()

# ============================================================
# PAGE: Why 15 + Course details for the 3 extras
# ============================================================
db.new_page()
y = title_bar("Why 15, Not 12? -- The Structural Logic", None)
y -= 6
setfill(c, DARK)
y = draw_paragraph(c, LUO_WHY_15_LOGIC, ML, y, CW, size=9.3, leading=12.6)
y -= 16

y = draw_paragraph(c, "Full course detail for each of the 3 \u201cextra\u201d collaterals:", ML, y, CW, size=9.3, leading=12)
y -= 8
for extra in LUO_EXTRA:
    course_lines = wrap_words(extra["course"], "Lora", 8.4, CW - 24)
    why_lines = wrap_words("Why it exists: " + extra["why"], "Lora-Italic", 7.8, CW - 24)
    box_h = 34 + len(course_lines) * 10.8 + 6 + len(why_lines) * 10
    box(c, ML, y, CW, box_h, LBLUE)
    setfill(c, GOLD); c.rect(ML, y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 14, y - 15, extra["name"] + "  --  " + extra["point"])
    setfill(c, DARK); c.setFont("Lora", 8.4)
    ty = y - 30
    for ln in course_lines:
        c.drawString(ML + 14, ty, ln); ty -= 10.8
    ty -= 6
    setfill(c, GOLD_DARK); c.setFont("Lora-Italic", 7.8)
    for ln in why_lines:
        c.drawString(ML + 14, ty, ln); ty -= 10
    y -= box_h + 10

y -= 6
setfill(c, ACCENT_LUO); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "MEMORY AID")
y -= 13
setfill(c, DARK); c.setFont("Lora-Italic", 8.6)
y = draw_paragraph(c,
    "The 12 paired-meridian Luo points all sit on the LIMBS (wrist for Hand meridians, ankle for Foot "
    "meridians). The 3 extra Luo points are the exception -- all three sit on the TRUNK (sternum, "
    "perineum, lateral chest), because their entire purpose is to cover trunk surface area no "
    "limb-based point could reach.",
    ML, y, CW, font="Lora-Italic", size=8.6, leading=11.4)
db.end_page()

# ============================================================
# PAGE: Special-point identity overlaps -- full drillable content
# ============================================================
db.new_page()
y = title_bar("Special-Point Identity Overlaps", "Points that carry more than one function")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c,
    "Some acupoints carry more than one special-point identity at once. Below: every Luo-Connecting "
    "point that ALSO serves as the Confluent (opening) point of an Extraordinary Vessel -- all four "
    "were reviewed in Week 7 and recur here as the clearest examples of this principle. A point with "
    "multiple special-point identities has a broader, stronger clinical reach than a single-purpose point.",
    ML, y, CW, size=9.2, leading=12.6)
y -= 16

overlap_rows = [
    ("LU 7 Lieque", "Luo-Connecting point of Lung", "Confluent (opening) point of Ren Mai (CV)",
     "Cough, sore throat, chest tightness (Luo function) + regulates all yin meridians via Ren Mai (Confluent function)."),
    ("SP 4 Gongsun", "Luo-Connecting point of Spleen", "Confluent (opening) point of Chong Mai",
     "Digestive/abdominal disorders (Luo function) + Sea-of-Blood/12-meridian regulation via Chong Mai (Confluent function)."),
    ("PC 6 Neiguan", "Luo-Connecting point of Pericardium", "Confluent (opening) point of Yin Wei Mai",
     "Chest/heart symptoms (Luo function) + dominates the interior, links all yin meridians via Yin Wei Mai (Confluent function)."),
    ("SJ 5 Waiguan", "Luo-Connecting point of Sanjiao", "Confluent (opening) point of Yang Wei Mai",
     "Exterior/febrile symptoms (Luo function) + dominates the exterior, links all yang meridians via Yang Wei Mai (Confluent function)."),
]
for pt, luo_role, other_role, clinical in overlap_rows:
    clinical_lines = wrap_words(clinical, "Lora-Italic", 7.4, CW - 24)
    box_h = 44 + len(clinical_lines) * 9.4
    box(c, ML, y, CW, box_h, tint(GOLD, 0.9))
    setfill(c, GOLD_DARK); c.rect(ML, y - box_h, 4, box_h, fill=1, stroke=0)
    setfill(c, NAVY); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 14, y - 15, pt)
    setfill(c, DARK); c.setFont("Lora", 8.4)
    c.drawString(ML + 14, y - 29, "As Luo point: " + luo_role)
    setfill(c, RED); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML + 14, y - 41, "Also: " + other_role)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.4)
    ty = y - 53
    for ln in clinical_lines:
        c.drawString(ML + 14, ty, ln); ty -= 9.4
    y -= box_h + 10

db.end_page()

# ============================================================
# PAGE: Cumulative recap of every other special-point category (A/B/C tiered)
# ============================================================
db.new_page()
y = title_bar("Cumulative Recap \u2014 All Other Special-Point Categories", "Tiered A/B/C, per the Week 6 pilot")
y -= 6
setfill(c, DARK)
y = draw_paragraph(c,
    "No organ-based special-point categories are newly introduced this week (Week 8's own content is "
    "the Luo-Connecting points above). The categories below stay exactly as covered previously -- "
    "listed here for cumulative review, with the A/B/C exam-priority tiering piloted in the Week 6 "
    "Decoder, rolled forward as planned.",
    ML, y, CW, size=8.8, leading=12)
y -= 6

setfill(c, GRAY); c.setFont("Lora-Italic", 7.6)
y = draw_paragraph(c,
    "Tier key: A = high-yield, drill to automaticity. B = know the definition + 1 example cold. "
    "C = recognize the name and general function only.",
    ML, y, CW, font="Lora-Italic", size=7.6, leading=10)
y -= 12

RECAP = [
    ("A", "YUAN-SOURCE", "Where the Source (Yuan) Qi is accessed.", "Last new examples: Week 6 (PC7, SJ4, GB40, LR3)"),
    ("A", "LUO-CONNECTING", "Where a Luo-vessel branches to the paired channel.", "THIS WEEK -- see full treatment above."),
    ("A", "HE-SEA", "At elbow/knee; treats counterflow Qi and organ-level disorders.", "Last new examples: Week 6 (PC3, SJ10, GB34, LR8)"),
    ("B", "XI-CLEFT", "Cleft point for acute conditions/pain.", "Last new examples: Week 6 (PC4, SJ7, GB36, LR6)"),
    ("B", "FRONT-MU", "Where a zang/fu organ's Qi gathers anteriorly.", "Last new examples: Week 6 (CV17, CV5, GB24, LR14)"),
    ("B", "BACK-SHU", "Bladder-channel transport points for each organ.", "Last new examples: Week 6 (BL14, BL22, BL19, BL18)"),
    ("B", "CONFLUENT (OPENING) POINTS", "Access point for each Extraordinary Vessel.", "Full treatment: Week 7 Decoder (all 4 master-couple pairs)"),
    ("C", "HUI-MEETING (INFLUENTIAL)", "8 points, meeting place for a tissue/substance category.", "Last new examples: Week 6 (GB34 = Sinews; LR13 = Zang)"),
    ("C", "JING-WELL / YING-SPRING / SHU-STREAM / JING-RIVER", "The Five-Shu points along each channel.", "Last new examples: Week 6"),
    ("C", "LOWER HE-SEA", "Special He-Sea points for the 6 Fu organs, on the leg.", "Last new examples: Week 6 (SJ's is BL39, off-channel)"),
    ("C", "COALESCENT POINTS (JIAO HUI XUE)", "Meeting points between an Extraordinary Vessel and a primary meridian.", "Full treatment: Week 7 Decoder"),
    ("C", "CROSSING POINTS", "A point crossed by more than one channel's pathway.", "GB count still flagged/unresolved (Week 6)"),
]
tier_colors = {"A": RED, "B": GOLD_DARK, "C": GRAY}
for tier, cat, defn, last in RECAP:
    row_h = 15 + 10 + 10
    box(c, ML, y, CW, row_h, CARD_BG)
    setfill(c, tier_colors[tier]); c.rect(ML, y - row_h, 20, row_h, fill=1, stroke=0)
    setfill(c, WHITE); c.setFont("Lora-Bold", 10)
    c.drawCentredString(ML + 10, y - row_h / 2 - 3.5, tier)
    setfill(c, NAVY); c.setFont("Lora-Bold", 8.2)
    c.drawString(ML + 28, y - 12, cat)
    setfill(c, DARK); c.setFont("Lora", 7.6)
    c.drawString(ML + 28, y - 23, defn)
    setfill(c, GRAY); c.setFont("Lora-Italic", 7.2)
    c.drawString(ML + 28, y - 33, last)
    y -= row_h + 4

db.end_page()
db.save()
