#!/usr/bin/env python3
"""AC300 Week 1 COMBINED Study Guide - Dr. Zhang (registered instructor) + Dr. Flinner
(parallel section). Channel Theory foundations, cross-referenced. Builds Print + reMarkable.
Zhang content verified against week1_content.py / AC300Week1.txt.
Flinner content verified against the Flinner Week 1 otter.ai transcript, as previously
extracted and QA'd in the AC300 Flinner Study Guide project (Four Functions, Ying/Wei,
Three Jiao, Internal-External vs Six-Meridian pairing systems)."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, "/home/claude/work/repo")
from week1_content import TWELVE_MERIDIANS, CIRCUITS, DIRECTION_RULES, MEETING_POINTS, MERIDIAN_CLOCK

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
CREAM = (0.976, 0.965, 0.929)

ZHANG_BLUE = (0.204, 0.361, 0.541)
ZHANG_TINT = (0.925, 0.941, 0.957)
FLINNER_GREEN = (0.259, 0.482, 0.318)
FLINNER_TINT = (0.925, 0.953, 0.933)
BOTH_GOLD = (0.616, 0.478, 0.216)
BOTH_TINT = (0.976, 0.961, 0.925)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    OUT = "/mnt/user-data/outputs/AC300_Week1_ZhangFlinner_Combined_StudyGuide_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week1_ZhangFlinner_Combined_StudyGuide_Print.pdf"
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


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]
WEEK_LABEL = "AC300/AC375 | Week 1 Combined Study Guide | Zhang + Flinner | VUIM Summer 2026"


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def simple_header(subtitle=""):
    setfill(DARK); c.setFont("Lora", 9)
    c.drawString(ML, H - 30, "AC300/AC375  |  Week 1 - Zhang + Flinner Combined  |  VUIM Summer 2026")
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
    page_bg(); simple_header()


def end_page():
    simple_footer(); c.showPage(); page_num[0] += 1


def section_header(y, title, subtitle=None):
    setfill(NAVY); c.setFont("Lora-Bold", 15)
    c.drawString(ML, y, title)
    setstroke(GOLD); c.setLineWidth(1.4)
    c.line(ML, y - 6, W - MR, y - 6)
    y -= 22
    if subtitle:
        setfill(GRAY); c.setFont("Lora-Italic", 9.5)
        c.drawString(ML, y, subtitle)
        y -= 16
    return y


def source_tag_standalone(y, label, color, tint):
    """Draws a source pill on its own line at ML and returns the y BELOW it (with clearance)."""
    tw = pdfmetrics.stringWidth(label, "Lora-Bold", 8) + 14
    setfill(tint); c.roundRect(ML, y - 15, tw, 16, 3, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(0.8); c.roundRect(ML, y - 15, tw, 16, 3, fill=0, stroke=1)
    setfill(color); c.setFont("Lora-Bold", 8)
    c.drawCentredString(ML + tw / 2, y - 10.5, label)
    return y - 26


def source_tag(x, y, label, color, tint):
    tw = pdfmetrics.stringWidth(label, "Lora-Bold", 8) + 14
    setfill(tint); c.roundRect(x, y - 11, tw, 15, 3, fill=1, stroke=0)
    setfill(color); c.setFont("Lora-Bold", 8)
    c.drawCentredString(x + tw / 2, y - 6, label)
    return tw


def callout(y, title, lines, color, tint, tag=None):
    body_lines = []
    for l in lines:
        body_lines.extend(wrap_words(l, "Lora", 9.2, CW - 26))
    box_h = 22 + len(body_lines) * 12.5
    setfill(tint); c.rect(ML - 4, y - box_h, CW + 8, box_h, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(2.2)
    c.line(ML - 4, y - box_h, ML - 4, y)
    setfill(color); c.setFont("Lora-Bold", 10)
    c.drawString(ML + 10, y - 15, title)
    if tag:
        source_tag(W - MR - 60, y - 6, tag, color, (1, 1, 1))
    setfill(DARK); c.setFont("Lora", 9.2)
    yy = y - 30
    for l in body_lines:
        c.drawString(ML + 10, yy, l)
        yy -= 12.5
    return y - box_h - 12


def table(y, col_widths, rows, header=True, row_h=17, font_size=9):
    total_w = sum(col_widths)
    for ri, row in enumerate(rows):
        is_h = header and ri == 0
        setfill(NAVY if is_h else (CREAM if ri % 2 == 0 else (1, 1, 1)))
        c.rect(ML, y - row_h, total_w, row_h, fill=1, stroke=0)
        cx = ML
        for ci, cell in enumerate(row):
            setfill((1, 1, 1) if is_h else DARK)
            c.setFont("Lora-Bold" if is_h else "Lora", font_size)
            c.drawString(cx + 5, y - row_h + (row_h - font_size) / 2 + 1, str(cell))
            cx += col_widths[ci]
        setstroke((0.6, 0.6, 0.6)); c.setLineWidth(0.4)
        c.rect(ML, y - row_h, total_w, row_h, fill=0, stroke=1)
        y -= row_h
    return y


def img_block(y, path, caption, max_h=170):
    from PIL import Image
    im = Image.open(path)
    iw, ih = im.size
    disp_w = CW
    disp_h = disp_w * ih / iw
    if disp_h > max_h:
        disp_h = max_h
        disp_w = disp_h * iw / ih
    x = ML + (CW - disp_w) / 2
    c.drawImage(path, x, y - disp_h, width=disp_w, height=disp_h)
    y -= disp_h + 12
    setfill(GRAY); c.setFont("Lora-Italic", 8)
    c.drawCentredString(W / 2, y, caption)
    return y - 16


# ============================================================
# COVER
# ============================================================
new_page()
setfill(NAVY); c.rect(0, H - 150, W, 150, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 25)
c.drawCentredString(W / 2, H - 62, "WEEK 1 - COMBINED STUDY GUIDE")
setfill((0.9, 0.9, 0.92)); c.setFont("Lora-Italic", 13)
c.drawCentredString(W / 2, H - 84, "Channel Theory: Concept, Nomenclature, Flow of Qi")
setfill(GOLD); c.setFont("Lora-Bold", 11)
c.drawCentredString(W / 2, H - 108, "Dr. Vivian Zhang  (your registered instructor)  +  Dr. Justin Flinner  (parallel section)")
setfill((1, 1, 1)); c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 126, EDLABEL)

y = H - 180
warn = ("Dr. Zhang is your registered AC300/AC375 instructor - her framing is what your own "
        "quizzes, midterm, and final will use. Dr. Flinner's material comes from a parallel "
        "section's transcripts and is included here as supplementary cross-reference, not as "
        "a substitute for Zhang's course.")
y = callout(y, "Read this first", [warn], RED, (0.976, 0.928, 0.919))

y -= 6
setfill(NAVY); c.setFont("Lora-Bold", 12)
c.drawString(ML, y, "This Guide Contains:")
y -= 18
contents = [
    "The 12 Primary Meridians - full reference table (identical in both sources)",
    "Zhang's Three Circuits framework, with the real lecture-slide diagrams",
    "Direction-of-flow rules and the 4 meeting-point locations",
    "The Meridian Clock (both instructors teach the same 24-hour cycle)",
    "Where the two sources agree, and where their framing genuinely differs",
    "Flinner-only material: the Four Functions, Ying/Wei, Three Jiao, and the Two Pairing Systems",
]
setfill(DARK); c.setFont("Lora", 10)
for item in contents:
    c.circle(ML + 4, y + 3, 1.6, fill=1, stroke=0)
    for l in wrap_words(item, "Lora", 10, CW - 20):
        c.drawString(ML + 14, y, l)
        y -= 13.5

y -= 10
col_w = (CW - 20) / 2
setfill(ZHANG_TINT); c.rect(ML, y - 40, col_w, 40, fill=1, stroke=0)
setstroke(ZHANG_BLUE); c.setLineWidth(2); c.line(ML, y - 40, ML, y)
setfill(ZHANG_BLUE); c.setFont("Lora-Bold", 10)
c.drawString(ML + 8, y - 16, "ZHANG SOURCE")
setfill(DARK); c.setFont("Lora", 8.5)
c.drawString(ML + 8, y - 30, "AC300Week1.txt otter.ai transcript + lecture slides")

x2 = ML + col_w + 20
setfill(FLINNER_TINT); c.rect(x2, y - 40, col_w, 40, fill=1, stroke=0)
setstroke(FLINNER_GREEN); c.setLineWidth(2); c.line(x2, y - 40, x2, y)
setfill(FLINNER_GREEN); c.setFont("Lora-Bold", 10)
c.drawString(x2 + 8, y - 16, "FLINNER SOURCE")
setfill(DARK); c.setFont("Lora", 8.5)
c.drawString(x2 + 8, y - 30, "Flinner Week 1 otter.ai transcript (parallel section, no slides available)")

y -= 60
setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawCentredString(W / 2, y, "Jon Centeno, D.AcHM Candidate  |  VUIM Summer 2026")
end_page()

# ============================================================
# PAGE: WHAT BOTH CONFIRM - 12 MERIDIANS TABLE
# ============================================================
new_page()
y = H - 50
y = section_header(y, "What Both Instructors Confirm", "Same textbook, same 12 channels - this table is identical in both sources")
y = callout(y, "Agreement", ["Both sources use the same 3-part naming convention (Hand/Foot + Yin/Yang + Zang/Fu), "
            "the same 12 meridians, and the same direction-of-flow rules. This table is safe to treat as "
            "universally exam-relevant, regardless of which section's quiz you're taking."],
            BOTH_GOLD, BOTH_TINT, tag="BOTH")

rows = [["Ab", "Name", "Classification", "Direction", "Circuit"]]
for ab, name, cls, yy, direction, circuit in TWELVE_MERIDIANS:
    rows.append([ab, name, cls, direction, circuit])
y = table(y, [32, 92, 90, 82, 100], rows, row_h=16, font_size=8.6) - 14

y = section_header(y, "Direction-of-Flow Rules")
for label, direction in DIRECTION_RULES:
    setfill(DARK); c.setFont("Lora", 9.5)
    c.drawString(ML + 6, y, label)
    setfill(NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawRightString(W - MR - 6, y, direction)
    y -= 15
end_page()

# ============================================================
# PAGE: ZHANG'S THREE CIRCUITS (with real slide diagrams)
# ============================================================
new_page()
y = H - 50
y = section_header(y, "Zhang's Three Circuits Framework", "Groups all 12 channels into 3 circuits of 4 - the primary organizing structure for your own course")
y = source_tag_standalone(y, "ZHANG", ZHANG_BLUE, ZHANG_TINT)

y = img_block(y, "/home/claude/wk1slides/anterior.jpg", "The Anterior Circuit - Source: Dr. Zhang's Week 1 lecture slides", max_h=225)
y = img_block(y, "/home/claude/wk1slides/posterior.jpg", "The Posterior Circuit (also called Inner Circuit) - Source: Dr. Zhang's Week 1 lecture slides", max_h=225)
end_page()

new_page()
y = H - 50
y = section_header(y, "Zhang's Three Circuits, continued")
y = img_block(y, "/home/claude/wk1slides/middle.jpg", "The Middle Circuit - Source: Dr. Zhang's Week 1 lecture slides", max_h=225)
y = img_block(y, "/home/claude/wk1slides/three_circuits_summary.jpg", "Three Main Circuits Summary - Source: Dr. Zhang's Week 1 lecture slides", max_h=225)

not_used = ("Flinner's available transcripts introduce each Six-Meridian pair individually as its two "
            "member channels come up in sequence, rather than grouping all four-channel circuits together "
            "up front. No Three Circuits macro-structure appears in the Flinner Week 1 transcript.")
y = callout(y, "Not used by Flinner", [not_used], FLINNER_GREEN, FLINNER_TINT, tag="FLINNER")
end_page()

# ============================================================
# PAGE: MEETING POINTS + MERIDIAN CLOCK (shared)
# ============================================================
new_page()
y = H - 50
y = section_header(y, "Meeting Points & The Meridian Clock", "Both instructors teach the same 24-hour circulation cycle")
y = source_tag_standalone(y, "BOTH", BOTH_GOLD, BOTH_TINT)
for stage, location, note in MEETING_POINTS:
    setfill(NAVY); c.setFont("Lora-Bold", 9.8)
    c.drawString(ML + 4, y, f"{stage}  ->  {location}")
    y -= 13
    setfill(GRAY); c.setFont("Lora-Italic", 8.6)
    for l in wrap_words(note, "Lora-Italic", 8.6, CW - 10):
        c.drawString(ML + 14, y, l)
        y -= 11
    y -= 4

y -= 10
y = section_header(y, "The Meridian Clock - All 12 Channels")
header_row = ["Channel", "Peak Window"]
left_rows = [header_row] + [[ab, t] for ab, t in MERIDIAN_CLOCK[:6]]
right_rows = [header_row] + [[ab, t] for ab, t in MERIDIAN_CLOCK[6:]]
col_w = (CW - 24) / 2
y_top = y
table(y, [col_w * 0.35, col_w * 0.65], left_rows, row_h=17, font_size=9.2)
x_save = ML
# draw right table at offset x by temporarily shifting ML
def table_at(x0, y0, col_widths, rows, row_h=17, font_size=9):
    tot = sum(col_widths)
    yy = y0
    for ri, row in enumerate(rows):
        is_h = ri == 0
        setfill(NAVY if is_h else (CREAM if ri % 2 == 0 else (1, 1, 1)))
        c.rect(x0, yy - row_h, tot, row_h, fill=1, stroke=0)
        cx = x0
        for ci, cell in enumerate(row):
            setfill((1, 1, 1) if is_h else DARK)
            c.setFont("Lora-Bold" if is_h else "Lora", font_size)
            c.drawString(cx + 5, yy - row_h + (row_h - font_size) / 2 + 1, str(cell))
            cx += col_widths[ci]
        setstroke((0.6, 0.6, 0.6)); c.setLineWidth(0.4)
        c.rect(x0, yy - row_h, tot, row_h, fill=0, stroke=1)
        yy -= row_h
    return yy

y_left_end = table_at(ML, y_top, [col_w * 0.35, col_w * 0.65], left_rows, row_h=17, font_size=9.2)
y_right_end = table_at(ML + col_w + 24, y_top, [col_w * 0.35, col_w * 0.65], right_rows, row_h=17, font_size=9.2)
y = min(y_left_end, y_right_end) - 16

pearl = ("Dr. Zhang's own clinical example: if you want to treat a Large Intestine dysfunction, "
         "consider timing treatment around 5-7 AM, LI's active period. Symptoms that flare at a "
         "specific time of day can point directly to which channel is involved.")
y = callout(y, "Clinical pearl - using the clock", [pearl], ZHANG_BLUE, ZHANG_TINT, tag="ZHANG")

system = ("Beyond the 12 Primary Meridians, the full channel system both sources describe includes: "
          "15 Collaterals (the 12 primary Luo points, plus the Luo of Du Mai, Ren Mai, and the "
          "Spleen's Great Luo/Dabao), 12 Divergent Meridians, 12 Muscle/Sinew Regions, 12 Cutaneous "
          "Regions, and 8 Extraordinary Vessels - full detail on each arrives in later weeks.")
y = callout(y, "The full system, at a glance", [system], BOTH_GOLD, BOTH_TINT, tag="BOTH")
end_page()

# ============================================================
# PAGE: FOUR FUNCTIONS COMPARISON
# ============================================================
new_page()
y = H - 50
y = section_header(y, "The Functions of Channels & Points", "Same underlying idea, different number of buckets - know both framings")

y = callout(y, "Zhang - Three Functions", [
    "1. Transporting - carries Qi and Blood to nourish organs, skin, muscles, tendons, and bones; keeps Yin-Yang in harmony.",
    "2. Resisting (Defending) - defends against disease and reflects symptoms/signs when something is wrong.",
    "3. Treatment - transmits needling sensation and regulates deficiency and excess conditions.",
], ZHANG_BLUE, ZHANG_TINT, tag="ZHANG")

y = callout(y, "Flinner - Four Functions", [
    "1. Transportation - moves Qi and Blood to maintain homeostasis, understood through Ying (nutritive, interior) and Wei (defensive, exterior) qi.",
    "2. Defense - resistance to external pathogenic factors (wind, cold, summer-heat, dampness) and internal factors (emotions become pathogenic only when they overwhelm the system).",
    "3. Transmission of De Qi - the arrival of qi: a mild ache or gentle tension (not pain) signaling the needle has engaged the channel.",
    "4. Rectification of Imbalances - the treatment function: using channels and points to correct excess, deficiency, or blockage once diagnosed.",
], FLINNER_GREEN, FLINNER_TINT, tag="FLINNER")

note = ("These aren't contradictory - Flinner's #1 (Transportation) and #3 (Transmission of De Qi) "
        "together cover roughly the same ground as Zhang's #1 (Transporting) and #3 (Treatment). "
        "Flinner's Ying/Wei lens and his explicit De Qi/needling-sensation function are the two "
        "genuinely new pieces not spelled out in Zhang's Week 1 framing.")
y = callout(y, "How to reconcile them", [note], BOTH_GOLD, BOTH_TINT, tag="BOTH")
end_page()

# ============================================================
# PAGE: FLINNER-ONLY - YING/WEI, ZANG/FU, THREE JIAO
# ============================================================
new_page()
y = H - 50
y = section_header(y, "Flinner-Only: Ying/Wei & the Three Jiao", "Not covered in Zhang's available Week 1 transcript - useful supplementary framing")
y = source_tag_standalone(y, "FLINNER", FLINNER_GREEN, FLINNER_TINT)

rows = [["Term", "Domain", "Function"],
        ["Ying qi", "Interior", "Nutritive - nourishes organs and tissues via circulation"],
        ["Wei qi", "Exterior", "Defensive - protects against external pathogenic invasion"],
        ["Zang", "Solid organs", "Yin organ systems (e.g. Lung, Heart, Spleen)"],
        ["Fu", "Hollow organs", "Yang organ systems (e.g. Large Intestine, Stomach, Small Intestine)"]]
y = table(y, [70, 90, CW - 160], rows, row_h=16, font_size=8.8) - 12

note = ("Every organ system can be viewed through more than one lens at once: zang/fu, yin/yang, "
        "internal-external pairing, AND six-meridian pairing. Track which lens you're using - it "
        "matters most once you begin pattern differentiation later in the program.")
y = callout(y, "Flinner's framing note", [note], FLINNER_GREEN, FLINNER_TINT)

y = section_header(y, "The Three Jiao (Sanjiao)")
rows2 = [["Jiao", "Boundary", "Organ systems"],
         ["Upper Jiao", "Above the diaphragm", "Lung, Heart, Pericardium"],
         ["Middle Jiao", "Diaphragm to umbilicus", "Stomach, Spleen, Liver, Gallbladder"],
         ["Lower Jiao", "Umbilicus to pelvic floor", "Kidney, Large Intestine, Small Intestine, Bladder"]]
y = table(y, [80, 150, CW - 230], rows2, row_h=16, font_size=8.8) - 10
note2 = ("San Jiao (Triple Burner) is unusual: as a channel and organ system, it is its own entity - "
         "but as a spatial region, it spans all three jiao at once.")
setfill(GRAY); c.setFont("Lora-Italic", 8.6)
for l in wrap_words(note2, "Lora-Italic", 8.6, CW - 10):
    c.drawString(ML + 4, y, l); y -= 11
y -= 12

y = section_header(y, "Flinner-Only: Two Pairing Systems", "Do not conflate these - they answer different questions")
body = ("Internal-External pairing follows circulation order (a Yin channel hands off to its paired "
        "Yang channel, back and forth around the body). Six-Meridian pairing groups channels by "
        "physiological relationship, independent of circulation order - e.g. Lung's Six-Meridian "
        "partner is Spleen (both Tai Yin), NOT Large Intestine.")
for l in wrap_words(body, "Lora", 9.1, CW - 10):
    c.drawString(ML, y, l); y -= 12.5
y -= 6

rows = [["Internal-External Pair", "Six-Meridian Name", "Element"],
        ["Lung / Large Intestine", "Tai Yin (LU) / Yang Ming (LI)", "Metal"],
        ["Stomach / Spleen", "Yang Ming (ST) / Tai Yin (SP)", "Earth"],
        ["Heart / Small Intestine", "Shao Yin (HT) / Tai Yang (SI)", "Fire"]]
y = table(y, [150, 170, CW - 320], rows, row_h=17, font_size=8.7) - 12

trap = ("Exam trap either instructor could use: don't assume 'Internal-External partner' and "
        "'Six-Meridian partner' are the same channel. Lung's Internal-External partner is Large "
        "Intestine; Lung's Six-Meridian (same-name, opposite-limb) partner is Spleen.")
y = callout(y, "Trap to watch for", [trap], RED, (0.976, 0.928, 0.919), tag="BOTH")
end_page()

# ============================================================
# CLOSING: STUDY STRATEGY
# ============================================================
new_page()
y = H - 50
y = section_header(y, "Study Strategy for Week 1", "How to use this combined guide")
strategy = [
    "Your own quizzes, midterm, and final use Dr. Zhang's framing - the Three Circuits structure "
    "and Three Functions are what you'll be tested on directly.",
    "Flinner's Ying/Wei, Three Jiao, and Two-Pairing-Systems material won't appear on your exam by "
    "name, but they're useful memory scaffolds and worth knowing if you ever cross-reference with "
    "classmates in Flinner's section.",
    "Treat any point-level fact that only appears in one source as unconfirmed until checked against "
    "the textbook (CAM 4th Ed. / Deadman's MOA 3rd Ed.) - this guide flags source for every claim so "
    "nothing gets silently blended.",
    "Draw it, don't just read it - both instructors independently emphasize hand-drawing each "
    "circuit's four meridians as the actual retention method, not rereading.",
]
setfill(DARK); c.setFont("Lora", 10)
for i, s in enumerate(strategy, 1):
    lines = wrap_words(f"{i}. {s}", "Lora", 10, CW - 10)
    for l in lines:
        c.drawString(ML, y, l); y -= 13.5
    y -= 6

y -= 6
y = section_header(y, "Vocabulary Crosswalk", "Chinese-Pinyin terms used across both sources")
vocab_rows = [["Term", "Meaning"],
              ["Jing (\u7ecf)", "Meridian - a primary pathway, 'like a river'"],
              ["Luo (\u7edc)", "Collateral - a branch off a meridian, 'like a branch'"],
              ["Jing-Luo", "Channels - the umbrella term for Meridians + Collaterals together"],
              ["Zang", "Yin, solid organ (Lung, Spleen, Heart, Liver, Kidney, Pericardium)"],
              ["Fu", "Yang, hollow organ (Large Intestine, Stomach, Small Intestine, Bladder, Gallbladder, San Jiao)"],
              ["Ying qi", "Nutritive qi - interior, nourishing (Flinner framing)"],
              ["Wei qi", "Defensive qi - exterior, protective (Flinner framing)"],
              ["Sanjiao", "Triple Burner/Energizer - both a channel AND a 3-part spatial region (Flinner framing)"]]
y = table(y, [90, CW - 90], vocab_rows, row_h=17, font_size=8.8) - 14

y -= 4
setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawCentredString(W / 2, y, "Dr. Vivian Zhang, Ph.D. (AC300/AC375)  |  Dr. Justin Flinner (parallel section, cross-reference only)")
y -= 14
c.drawCentredString(W / 2, y, "Jon Centeno, D.AcHM Candidate  |  VUIM")
end_page()

c.save()
print("SAVED:", OUT)
