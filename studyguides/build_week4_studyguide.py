#!/usr/bin/env python3
"""AC300 Week 4 Study Guide - Heart & Small Intestine Channels. Both editions."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
LIGHTBLUE = (0.929, 0.949, 0.965)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
FIRE = (0.690, 0.204, 0.169)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    ROW_TINT = (0.925, 0.902, 0.855)
    LIGHTBLUE_RM = (0.902, 0.878, 0.816)
    HEADER_H = 51
    HAIRLINE = 1.0
    OUT = "/mnt/user-data/outputs/AC300_Week4_StudyGuide_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    LIGHTBLUE_RM = LIGHTBLUE
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


page_num = [1]


def header():
    setfill(NAVY)
    c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD)
    c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawString(36, H - HEADER_H + 15, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    c.setFont("Lora-Italic", 8.5)
    c.drawRightString(W - 36, H - HEADER_H + 15, EDLABEL)
    c.setFont("Lora", 8)
    c.drawString(36, H - HEADER_H + 3, "AC300/AC375  |  Week 4  |  HT & SI Channels  |  VUIM Summer 2026")
    c.drawRightString(W - 36, H - HEADER_H + 3, f"p.{page_num[0]}")


def footer():
    setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2)
    c.line(36, 30, W - 36, 30)


def new_page():
    page_bg()
    header()


def end_page():
    footer()
    c.showPage()
    page_num[0] += 1


ML, MR = 36, 36
CW = W - ML - MR


def meta_box(x, y, w, rows):
    """Pertaining/Connecting/special-points sidebar box"""
    setfill(LIGHTBLUE_RM); c.rect(x, y - 2, w, 2, fill=1, stroke=0)
    yy = y - 14
    for label, val in rows:
        setfill(NAVY); c.setFont("Lora-Bold", 8.3)
        c.drawString(x, yy, label)
        yy -= 10.5
        setfill(DARK); c.setFont("Lora", 8.3)
        for l in wrap_words(val, "Lora", 8.3, w - 4):
            c.drawString(x, yy, l)
            yy -= 10.5
        yy -= 3
    return yy


# ============= PAGE 1: COVER =============
page_bg()
setfill(NAVY); c.rect(0, H - 80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H - 80, W, 3, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W / 2, H - 45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")
c.setFont("Lora-Italic", 9)
c.drawCentredString(W / 2, H - 62, EDLABEL)

bx, by, bs = W / 2 - 34, H - 165, 68
setfill(LIGHTBLUE_RM); c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD); c.rect(bx, by + bs - 8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 7)
c.drawCentredString(W / 2, by + bs - 22, "WEEK")
c.setFont("Lora-Bold", 20)
c.drawCentredString(W / 2, by + 18, "4")

c.setFont("Lora-Bold", 32); setfill(NAVY)
c.drawCentredString(W / 2, H - 227, "Week 4 Study Guide")
c.setFont("Lora-BoldItalic", 18); setfill(RED)
c.drawCentredString(W / 2, H - 250, "Heart & Small Intestine Channels")
c.setFont("Lora", 11); setfill(DARK)
c.drawCentredString(W / 2, H - 268, "HT (9 pts) + SI (19 pts) = 28 Points")

setstroke(GOLD); c.setLineWidth(1)
c.line(W / 2 - 140, H - 282, W / 2 - 40, H - 282)
c.line(W / 2 + 40, H - 282, W / 2 + 140, H - 282)
setfill(GOLD); c.circle(W / 2, H - 282, 2.5, fill=1, stroke=0)

box_w, box_h, gap = 220, 90, 20
by0 = H - 400
setfill(LIGHTBLUE_RM); c.rect((W - box_w) / 2, by0, box_w, box_h, fill=1, stroke=0)
setfill(GOLD); c.rect((W - box_w) / 2, by0 + box_h - 3, box_w, 3, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 9.5)
c.drawCentredString(W / 2, by0 + box_h - 18, "This Document Contains:")
setfill(DARK); c.setFont("Lora", 8.3)
bullets = [
    "Internal + external running course for HT & SI",
    "Full point location table for all 28 points",
    "Syndromes & high-yield points per channel",
    "Dr. Zhang's Clinical Pearls, direct from lecture",
    "Quiz 4 Fundamentals + HT vs SI comparison table",
]
yy = by0 + box_h - 34
for b in bullets:
    c.drawCentredString(W / 2, yy, "\u2022  " + b)
    yy -= 12

y = by0 - 30
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, y, "Dr. Vivian Zhang, Ph.D.  \u00b7  Jon Centeno, D.AcHM Candidate  \u00b7  VUIM")

end_page()

# ============= PAGE 2: HT META + INTERNAL RUNNING COURSE =============
new_page()
y = H - HEADER_H - 26
setfill(FIRE); c.rect(ML, y - 3, CW, 3, fill=1, stroke=0)
y -= 18
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, "Heart Meridian of Hand-Shaoyin (HT)")
y -= 14
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawString(ML, y, "Yin  \u00b7  Fire  \u00b7  11 AM-1 PM  \u00b7  9 Points")
y -= 20

sidebar_x = ML + CW - 150
sidebar_w = 150
meta_rows = [
    ("Pertaining", "Heart"), ("Connecting", "Small Intestine"),
    ("Back-Shu", "BL15"), ("Front-Mu", "CV14 Juque"),
    ("Yuan-Source", "HT7 (also Shu-Stream)"), ("Luo", "HT5 Tongli"),
    ("He-Sea", "HT3 Shaohai"), ("Xi-Cleft", "HT6 Yinxi"),
]
main_w = CW - 170
top_y = y
meta_box(sidebar_x, top_y, sidebar_w, meta_rows)

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, top_y, "Internal Running Course")
yy = top_y - 16
beats = [
    "Originates in the Heart, spreads to the 'Heart system' - the network of vessels linking heart to other organs",
    "Descending branch: through the diaphragm, connects with the Small Intestine (CONNECTING organ) - no other organ is linked",
    "Ascending branch: alongside the esophagus, connects with the 'eye system' - Dr. Zhang: \"The eye is the window of the Heart\"",
    "Main pathway (straight portion): emerges from the heart system, ascends to the lung, emerges from the axilla - HT1 Jiquan, the first point",
    "Descends along the medial aspect of the upper arm, on the POSTERIOR side - behind the Lung meridian, behind the Pericardium meridian (most posterior of the three)",
    "Crosses the elbow and forearm on the ulnar/posterior side",
    "Reaches the wrist, continues to the palm",
    "Ends at the RADIAL side of the little finger tip - HT9 Shaochong, hands off to Small Intestine",
]
setfill(DARK); c.setFont("Lora", 8.4)
for i, beat in enumerate(beats, 1):
    lines = wrap_words(beat, "Lora", 8.4, main_w - 16)
    setfill(RED); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML, yy, f"{i}")
    setfill(DARK); c.setFont("Lora", 8.4)
    for j, l in enumerate(lines):
        c.drawString(ML + 14, yy - j * 10.3, l)
    yy -= len(lines) * 10.3 + 4

y = min(yy, meta_box.__defaults__ or yy) - 10
# recompute bottom using sidebar end (approx) - just use yy since sidebar box is short
y = yy - 8

# MOA figure - fills remaining space on this page
try:
    img = ImageReader('/home/claude/MOA_HT.jpeg')
    iw, ih = img.getSize()
    target_h = min(y - 60, 300)
    target_w = target_h * iw / ih
    if target_w > CW:
        target_w = CW
        target_h = target_w * ih / iw
    img_x = ML + (CW - target_w) / 2
    img_y = y - target_h
    c.drawImage(img, img_x, img_y, width=target_w, height=target_h)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, img_y - 12, "MOA \u2014 Heart Meridian (internal pathway)")
    y = img_y - 26
except Exception as e:
    pass

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Functions (per Dr. Zhang + MOA)")
y -= 4
setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2); c.line(ML, y, ML + 200, y)
y -= 13
funcs = [
    "Governs the Blood and Blood vessels - treats palpitations, chest pain, blood pressure disorders, poor circulation",
    "Houses the Mind (Shen) - Dr. Zhang: \"Heart is the house of the mind.\" Treats insomnia, poor memory, anxiety, depression, mental-emotional disorders",
    "Connects to the 'eye system' via its ascending internal branch - relevant for some eye disorders",
    "ONLY the Heart channel has ZERO external crossing points - the most 'self-contained' primary channel",
]
setfill(DARK); c.setFont("Lora", 8.5)
for f in funcs:
    for l in wrap_words(f, "Lora", 8.5, CW - 4):
        c.drawString(ML, y, l)
        y -= 10.8
    y -= 2

end_page()

# ============= PAGE 3: HT EXTERNAL RUNNING COURSE / POINT TABLE =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Heart Meridian (HT)  \u2014  Full Point Location Table")
y -= 18

setfill(NAVY); c.setFont("Lora-Bold", 8)
c.drawString(ML, y, "Pt"); c.drawString(ML + 45, y, "Chinese")
c.drawString(ML + 130, y, "Location & Notes")
y -= 4
setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2); c.line(ML, y, ML + CW, y)
y -= 12

HT_POINTS = [
    ("HT1", "Jiquan", "In the centre of the axilla, medial to the axillary artery - first point; also used for stroke emergencies"),
    ("HT2", "Qingling", "3 cun proximal to the medial end of the elbow crease, in the groove medial to biceps brachii"),
    ("HT3", "Shaohai", "Midway between the medial end of the elbow crease and the medial epicondyle of the humerus, elbow flexed - HE-SEA"),
    ("HT4", "Lingdao", "On the radial side of flexor carpi ulnaris tendon, 1.5 cun proximal to HT7 - JING-RIVER"),
    ("HT5", "Tongli", "On the radial side of flexor carpi ulnaris tendon, 1 cun proximal to HT7 - LUO-CONNECTING"),
    ("HT6", "Yinxi", "On the radial side of flexor carpi ulnaris tendon, 0.5 cun proximal to HT7 - XI-CLEFT"),
    ("HT7", "Shenmen", "At the wrist crease, radial side of flexor carpi ulnaris tendon, at the proximal border of the pisiform bone - SHU-STREAM / YUAN-SOURCE"),
    ("HT8", "Shaofu", "On the palm, between the 4th and 5th metacarpal bones, where the little fingertip rests in a closed fist - YING-SPRING"),
    ("HT9", "Shaochong", "On the radial side of the little finger, 0.1 cun from the corner of the nail - JING-WELL, last point"),
]
setfill(DARK); c.setFont("Lora", 8.3)
for i, (pt, ch_name, loc) in enumerate(HT_POINTS):
    lines = wrap_words(loc, "Lora", 8.3, CW - 130)
    n = len(lines)
    row_h = n * 10.8 + 4
    if i % 2 == 0:
        setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 8, CW + 8, row_h, fill=1, stroke=0)
    setfill(RED); c.setFont("Lora-Bold", 8.3); c.drawString(ML, y, pt)
    setfill(DARK); c.setFont("Lora", 8.3); c.drawString(ML + 45, y, ch_name)
    for j, l in enumerate(lines):
        c.drawString(ML + 130, y - j * 10.8, l)
    y -= row_h

y -= 8
setfill(GRAY); c.setFont("Lora-Italic", 8)
c.drawString(ML, y, "CAM: HT color figure (AC300_CAM_HTSI.pdf, Deadman 3rd Ed.)  \u00b7  MOA anchor: HT1 = p.212")
y -= 20

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Special Points Summary")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 180, y)
y -= 13
special_ht = [
    ("Jing-Well", "HT9", ""), ("Ying-Spring", "HT8", "clears heart fire"),
    ("Shu-Stream", "HT7", "also Yuan-Source"), ("Jing-River", "HT4", ""),
    ("He-Sea", "HT3", "clears heart fire, fear/arm pain"), ("Luo", "HT5", ""),
    ("Xi-Cleft", "HT6", "night sweats, acute heart pain"), ("Front-Mu", "CV14", ""),
    ("Back-Shu", "BL15", ""),
]
setfill(DARK); c.setFont("Lora", 8.3)
col_w2 = CW / 3
for i, (cat, pt, note) in enumerate(special_ht):
    col = i % 3
    row = i // 3
    x = ML + col * col_w2
    yy = y - row * 22
    setfill(NAVY); c.setFont("Lora-Bold", 8.3); c.drawString(x, yy, cat)
    setfill(RED); c.setFont("Lora-Bold", 8.3); c.drawString(x, yy - 10.5, pt)
    if note:
        setfill(GRAY); c.setFont("Lora-Italic", 7.5)
        c.drawString(x + 30, yy - 10.5, note)
y -= (3 * 22) + 6

end_page()

# ============= PAGE 4: HT SYNDROMES & HIGH-YIELD (no crossing-pts page - HT has none) =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "HT  \u2014  Syndromes & High-Yield Points")
y -= 18

col_w = (CW - 20) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "A. External Course Symptoms")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
for s in ["Pain along the medial-posterior arm (HT's own pathway)",
          "Palpitations felt along the running course",
          "Pain/warmth in the palm along the pathway"]:
    for l in wrap_words(s, "Lora", 8.5, col_w - 4):
        c.drawString(ML, y, l)
        y -= 10.8
left_bottom = y

y2 = top_y
x2 = ML + col_w + 20
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "B. Internal Organ (Heart)")
y2 -= 4
setstroke(GOLD); c.line(x2, y2, x2 + 160, y2)
y2 -= 13
setfill(DARK); c.setFont("Lora", 8.5)
for s in ["Palpitations, disorders of Heart rhythm",
          "Chest pain, blood pressure disorders (governs Blood/vessels)",
          "Insomnia, poor memory, anxiety, depression (houses the Mind)",
          "Dr. Zhang: emergency stroke presentation \u2014 HT9 as a first-aid point"]:
    for l in wrap_words(s, "Lora", 8.5, col_w - 4):
        c.drawString(x2, y2, l)
        y2 -= 10.8
right_bottom = y2
y = min(left_bottom, right_bottom) - 14

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "High-Yield HT Points")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(NAVY); c.setFont("Lora-Bold", 8); c.drawString(ML, y, "Pt")
c.drawString(ML + 40, y, "Category"); c.drawString(ML + 150, y, "Key Indications")
y -= 12
hy_ht = [
    ("HT1", "First point", "Emergency point for stroke; axilla/chest disorders"),
    ("HT7", "Shu-Stream + Yuan", "Calms Shen; #1 for anxiety, insomnia, palpitations"),
    ("HT3", "He-Sea", "Clears heart fire; fear, arm pain along channel"),
    ("HT6", "Xi-Cleft", "Night sweats, acute heart pain"),
    ("HT9", "Jing-Well, last point", "Emergency: severe heart pain, revives consciousness"),
    ("HT5", "Luo-Connecting", "Links to SI; disorders of both channels; speech disorders"),
]
setfill(DARK); c.setFont("Lora", 8.3)
for pt, cat, use in hy_ht:
    setfill(RED); c.setFont("Lora-Bold", 8.3); c.drawString(ML, y, pt)
    setfill(NAVY); c.setFont("Lora-Italic", 8); c.drawString(ML + 40, y, cat)
    setfill(DARK); c.setFont("Lora", 8.3)
    lines = wrap_words(use, "Lora", 8.3, CW - 155)
    c.drawString(ML + 150, y, lines[0])
    y -= 10.8
    for extra in lines[1:]:
        c.drawString(ML + 150, y, extra)
        y -= 10.8

y -= 8
setfill(RED); c.setFont("Lora-Bold", 9)
c.drawString(ML, y, "Dr. Zhang: \"Heart is the house of the mind.\" Points around the wrist (HT7 especially) treat mental-emotional")
y -= 11
c.drawString(ML, y, "disorders in clinic. This is exam-testable.")

end_page()

# ============= PAGE 5: SI META + INTERNAL RUNNING COURSE =============
new_page()
y = H - HEADER_H - 26
setfill(FIRE); c.rect(ML, y - 3, CW, 3, fill=1, stroke=0)
y -= 18
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(ML, y, "Small Intestine Meridian of Hand-Taiyang (SI)")
y -= 14
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawString(ML, y, "Yang  \u00b7  Fire  \u00b7  1-3 PM  \u00b7  19 Points")
y -= 20

sidebar_x = ML + CW - 150
sidebar_w = 150
meta_rows = [
    ("Pertaining", "Small Intestine"), ("Connecting", "Heart"),
    ("Back-Shu", "BL27"), ("Front-Mu", "CV4 Guanyuan"),
    ("Yuan-Source", "SI4 Wangu"), ("Luo", "SI7 Zhizheng"),
    ("Shu-Stream", "SI3 (also Confluent)"), ("Xi-Cleft", "SI6 Yanglao"),
]
main_w = CW - 170
top_y = y
meta_box(sidebar_x, top_y, sidebar_w, meta_rows)

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, top_y, "Internal Running Course")
yy = top_y - 16
beats = [
    "Begins at the ulnar side of the little finger tip - SI1 Shaoze, where HT's branch terminates",
    "Runs along the ulnar/posterior border of the hand and forearm, crosses the elbow (SI8 Xiaohai, He-Sea)",
    "Ascends the posterior aspect of the upper arm, circles around the shoulder, zigzags across the scapula",
    "Crosses GV14 Dazhui (meeting of all Yang channels), enters supraclavicular fossa",
    "Descends internally, connects with the HEART (Dr. Zhang: 'no other organ is connected' besides HT), through diaphragm, PERTAINS Small Intestine",
    "BRANCH: from the neck, ascends the cheek to the outer canthus, enters the ear at SI19 Tinggong - the LAST point",
    "Second BRANCH: from the cheek, ascends to the inner canthus of the eye (crosses BL1 Jingming)",
    "Also crosses GB14 near the forehead - two facial crossing points total",
]
setfill(DARK); c.setFont("Lora", 8.4)
for i, beat in enumerate(beats, 1):
    lines = wrap_words(beat, "Lora", 8.4, main_w - 16)
    setfill(RED); c.setFont("Lora-Bold", 8.4)
    c.drawString(ML, yy, f"{i}")
    setfill(DARK); c.setFont("Lora", 8.4)
    for j, l in enumerate(lines):
        c.drawString(ML + 14, yy - j * 10.3, l)
    yy -= len(lines) * 10.3 + 4

y = yy - 8

# MOA figure - fills remaining space on this page
try:
    img = ImageReader('/home/claude/MOA_SI.jpeg')
    iw, ih = img.getSize()
    target_h = min(y - 60, 300)
    target_w = target_h * iw / ih
    if target_w > CW:
        target_w = CW
        target_h = target_w * ih / iw
    img_x = ML + (CW - target_w) / 2
    img_y = y - target_h
    c.drawImage(img, img_x, img_y, width=target_w, height=target_h)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, img_y - 12, "MOA \u2014 Small Intestine Meridian (internal pathway)")
    y = img_y - 26
except Exception as e:
    pass

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Functions (per Dr. Zhang + MOA)")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 200, y)
y -= 13
funcs = [
    "Receives, transforms, and separates 'clear from turbid' (fluids/food) - the Fu organ function",
    "Symptoms are based on TWO principles: (1) external course - numbness of mouth, cheek, throat, neck, upper arm; (2) internal organ - digestive disorders (constipation, lower abdominal distension) and, per Dr. Zhang, some mental disorders",
    "Notably, despite connecting to the diaphragm and Stomach internally, very few SI points are indicated for digestive disorders directly - most SI points treat the external pathway (shoulder, neck, ear) instead",
    "SI1 Shaoze is specifically noted for excess breast milk / lactation problems",
]
setfill(DARK); c.setFont("Lora", 8.5)
for f in funcs:
    for l in wrap_words(f, "Lora", 8.5, CW - 4):
        c.drawString(ML, y, l)
        y -= 10.8
    y -= 2

end_page()

# ============= PAGE 6: SI POINT TABLE =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Small Intestine Meridian (SI)  \u2014  Full Point Location Table")
y -= 18
setfill(NAVY); c.setFont("Lora-Bold", 8)
c.drawString(ML, y, "Pt"); c.drawString(ML + 45, y, "Chinese")
c.drawString(ML + 130, y, "Location & Notes")
y -= 4
setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2); c.line(ML, y, ML + CW, y)
y -= 12

SI_POINTS = [
    ("SI1", "Shaoze", "Ulnar side of little finger, 0.1 cun from nail corner - JING-WELL, first point"),
    ("SI2", "Qiangu", "Ulnar border of little finger, distal to MCP joint, red/white skin junction - YING-SPRING"),
    ("SI3", "Houxi", "Ulnar side, proximal to 5th MCP joint, end of transverse crease, red/white skin junction (loose fist) - SHU-STREAM / CONFLUENT (Du Mai)"),
    ("SI4", "Wangu", "Ulnar side of hand, between base of 5th metacarpal and triquetral bone - YUAN-SOURCE"),
    ("SI5", "Yanggu", "Ulnar side of wrist, between styloid process of ulna and triquetral bone - JING-RIVER"),
    ("SI6", "Yanglao", "Dorsal to head of ulna; palm on chest, in bony cleft radial to the styloid process - XI-CLEFT"),
    ("SI7", "Zhizheng", "On line connecting SI5 and SI8, 5 cun proximal to SI5 - LUO-CONNECTING"),
    ("SI8", "Xiaohai", "Between olecranon of ulna and medial epicondyle of humerus, elbow flexed - HE-SEA"),
    ("SI9", "Jianzhen", "1 cun superior to posterior axillary crease, arm adducted"),
    ("SI10", "Naoshu", "Directly above SI9, in depression inferior to the scapular spine"),
    ("SI11", "Tianzong", "Center of the infrascapular fossa"),
    ("SI12", "Bingfeng", "Center of the suprascapular fossa, directly above SI11, arm lifted"),
    ("SI13", "Quyuan", "Medial end of suprascapular fossa, midway between SI10 and spinous process of T2"),
    ("SI14", "Jianwaishu", "3 cun lateral to spinous process of T1, medial border of scapula"),
    ("SI15", "Jianzhongshu", "2 cun lateral to spinous process of C7 (GV14 Dazhui) - crossing point"),
    ("SI16", "Tianchuang", "Posterior to sternocleidomastoid, level with the laryngeal prominence"),
    ("SI17", "Tianrong", "Posterior to angle of mandible, anterior to sternocleidomastoid"),
    ("SI18", "Quanliao", "Directly below outer canthus, depression on lower border of zygoma"),
    ("SI19", "Tinggong", "Anterior to tragus, posterior to condyloid process of mandible, mouth open - LAST point"),
]
setfill(DARK); c.setFont("Lora", 7.8)
for i, (pt, ch_name, loc) in enumerate(SI_POINTS):
    lines = wrap_words(loc, "Lora", 7.8, CW - 130)
    n = len(lines)
    row_h = n * 9.6 + 3
    if i % 2 == 0:
        setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 7, CW + 8, row_h, fill=1, stroke=0)
    setfill(RED); c.setFont("Lora-Bold", 7.8); c.drawString(ML, y, pt)
    setfill(DARK); c.setFont("Lora", 7.8); c.drawString(ML + 45, y, ch_name)
    for j, l in enumerate(lines):
        c.drawString(ML + 130, y - j * 9.6, l)
    y -= row_h

y -= 6
setfill(GRAY); c.setFont("Lora-Italic", 7.5)
c.drawString(ML, y, "CAM: SI color figure (SI_CAM.pdf, Deadman 3rd Ed.)  \u00b7  MOA anchor: SI1 = p.231")

end_page()

# ============= PAGE 7: SI CROSSING POINTS (light - only 2) =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "SI  \u2014  Crossing Points (Detailed)")
y -= 16
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
for l in wrap_words("Dr. Zhang: SI crosses BL1 and GB14 on its facial branch. Unlike HT (zero crossing points), SI does connect externally with other channels near the face/eye.", "Lora-Italic", 8.5, CW):
    c.drawString(ML, y, l)
    y -= 11
y -= 14

crossings = [
    ("BL1 Jingming", "Inner canthus of eye",
     "SI's facial branch ascends to the inner canthus and crosses the Bladder channel here. BL1 itself treats all eye disorders: redness, pain, myopia, night blindness. This is the same crossing point used by ST and GB elsewhere in the course - a genuinely 'busy' facial point."),
    ("GB14 Yangbai", "Forehead, above midpupil",
     "SI's ascending branch also reaches the forehead region, crossing the Gallbladder channel at GB14. Used for frontal headache, eye disorders, facial paralysis - a point taught more fully when GB is covered later in the course."),
]
for pt, loc, clinical in crossings:
    setfill(NAVY); c.setFont("Lora-Bold", 10)
    c.drawString(ML, y, pt)
    setfill(GRAY); c.setFont("Lora-Italic", 8.3)
    c.drawRightString(ML + CW, y, loc)
    y -= 13
    setfill(DARK); c.setFont("Lora", 8.5)
    for l in wrap_words(clinical, "Lora", 8.5, CW):
        c.drawString(ML, y, l)
        y -= 11
    y -= 14

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Why SI has so few crossing points compared to ST/LI")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 260, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
note = "SI's pathway is dominated by shoulder/scapula points (SI9-SI15) that don't cross other channels - it's a channel that runs largely 'alone' along the posterior shoulder before reaching the two facial crossings near the eye/forehead at the very end of its course."
for l in wrap_words(note, "Lora", 8.5, CW):
    c.drawString(ML, y, l)
    y -= 11

end_page()

# ============= PAGE 8: SI SYNDROMES & HIGH-YIELD =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "SI  \u2014  Syndromes & High-Yield Points")
y -= 18

col_w = (CW - 20) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "A. External Course Symptoms")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
for s in ["Numbness/pain of the mouth, cheek, throat, neck, upper arm",
          "Shoulder and scapula pain along the pathway",
          "Ear disorders (tinnitus, deafness) near SI19",
          "Deviation/pain along the posterior arm"]:
    for l in wrap_words(s, "Lora", 8.5, col_w - 4):
        c.drawString(ML, y, l)
        y -= 10.8
left_bottom = y

y2 = top_y
x2 = ML + col_w + 20
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(x2, y2, "B. Internal Organ (Small Intestine)")
y2 -= 4
setstroke(GOLD); c.line(x2, y2, x2 + 160, y2)
y2 -= 13
setfill(DARK); c.setFont("Lora", 8.5)
for s in ["Constipation, distension in the lower abdomen",
          "Digestive disorders generally (though few SI points target these directly)",
          "Some mental disorders, per Dr. Zhang's clinical note",
          "SI1 specifically: excess breast milk / lactation problems"]:
    for l in wrap_words(s, "Lora", 8.5, col_w - 4):
        c.drawString(x2, y2, l)
        y2 -= 10.8
right_bottom = y2
y = min(left_bottom, right_bottom) - 14

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "High-Yield SI Points")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(NAVY); c.setFont("Lora-Bold", 8); c.drawString(ML, y, "Pt")
c.drawString(ML + 40, y, "Category"); c.drawString(ML + 150, y, "Key Indications")
y -= 12
hy_si = [
    ("SI3", "Shu-Stream + Confluent", "Opens Du Mai (pairs with BL62); spine, neck, febrile disease"),
    ("SI4", "Yuan-Source", "Wrist/finger pain, febrile disease"),
    ("SI8", "He-Sea", "Elbow/arm disorders; also regulates its coupled Heart organ"),
    ("SI19", "Last point, near ear", "Tinnitus, deafness, ear disorders"),
    ("SI1", "Jing-Well, first point", "Excess breast milk / lactation problems (Dr. Zhang's clinical example)"),
    ("SI11", "Scapula region", "Shoulder/scapula pain, also treats Heart via coupling"),
]
setfill(DARK); c.setFont("Lora", 8.3)
for pt, cat, use in hy_si:
    setfill(RED); c.setFont("Lora-Bold", 8.3); c.drawString(ML, y, pt)
    setfill(NAVY); c.setFont("Lora-Italic", 8); c.drawString(ML + 40, y, cat)
    setfill(DARK); c.setFont("Lora", 8.3)
    lines = wrap_words(use, "Lora", 8.3, CW - 155)
    c.drawString(ML + 150, y, lines[0])
    y -= 10.8
    for extra in lines[1:]:
        c.drawString(ML + 150, y, extra)
        y -= 10.8

end_page()

# ============= PAGE 9: CLINICAL PEARLS =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Dr. Zhang's Clinical Pearls  \u2014  Direct from Lecture")
y -= 16
setfill(GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(ML, y, "Highest exam probability")
y -= 16

pearls = [
    ("HT is the ONLY Channel with Zero Crossing Points",
     "Confirmed unique feature - HT's entire pathway runs from chest to little finger without crossing another named channel point. Contrast directly with SI, which crosses BL1 and GB14."),
    ("\u201cThe Eye is the Window of the Heart\u201d",
     "Dr. Zhang's own phrase. HT's ascending internal branch connects to the 'eye system' - both HT and SI (per their internal branches) connect to the eye, which is why eye disorders can sometimes be treated via Heart-related points."),
    ("Heart's Two Main Functions",
     "(1) Governs Blood and the Blood vessels - palpitations, chest pain, blood pressure, circulation. (2) Houses the Mind (Shen) - Dr. Zhang: 'Heart is the house of the mind.' Points near the wrist (especially HT7) are chosen clinically to treat mental-emotional disorders: insomnia, poor memory, anxiety, depression."),
    ("HT9 as an Emergency / Stroke Point",
     "Dr. Zhang highlighted HT9 (and the Jing-Well category generally) for emergency presentations - severe heart pain, palpitations, and reviving consciousness, including stroke scenarios."),
    ("SI's Two Symptom Principles",
     "Dr. Zhang: SI symptoms follow two tracks - (1) External course: numbness of mouth, cheek, throat, neck, upper arm. (2) Internal organ: digestive issues (constipation, lower abdominal distension) and, notably, some mental disorders as well."),
    ("SI Points Rarely Target Digestion Directly",
     "Despite SI's internal pathway passing through the diaphragm and connecting to the Stomach on its way to the Small Intestine, very few SI points are actually indicated for digestive disorders - most of the channel's clinical use is for the shoulder, neck, and ear along its external course."),
    ("SI1 and Lactation",
     "Dr. Zhang specifically noted SI1 (Shaoze) for excess/insufficient breast milk and lactation problems - a distinctive, specific clinical example worth remembering."),
    ("No Worries About the Midterm",
     "Dr. Zhang, discussing the upcoming midterm: many questions will be reused directly from Quiz 1, 2, and 3 material. Review those quiz kits alongside this material."),
    ("Homework Reminder \u2014 Draw BOTH Pathways",
     "Dr. Zhang repeated her standing instruction: draw both the internal AND external pathway for every meridian. 'Some students only draw external - the internal pathway is also important.'"),
]
setfill(DARK)
for title, body in pearls:
    setfill(NAVY); c.setFont("Lora-Bold", 9.3)
    for l in wrap_words(title, "Lora-Bold", 9.3, CW):
        c.drawString(ML, y, l)
        y -= 11.5
    setfill(DARK); c.setFont("Lora", 8.3)
    for l in wrap_words(body, "Lora", 8.3, CW):
        c.drawString(ML, y, l)
        y -= 10.5
    y -= 8

end_page()

# ============= PAGE 10: QUIZ 4 FUNDAMENTALS =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "Quiz 4 Fundamentals  \u2014  Circuits & Cumulative Review")
y -= 14
setfill(GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(ML, y, "From Dr. Zhang's review slides")
y -= 18

col_w = (CW - 20) / 2
top_y = y
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(ML, y, "Posterior Circuit Opens This Week")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.3)
for l in wrap_words("HT and SI are the first two channels of the Posterior Circuit (also called Inner Circuit on earlier slide versions), which continues with BL and KI next week. Peak times run consecutively: HT 11-1PM, SI 1-3PM, BL 3-5PM, KI 5-7PM.", "Lora", 8.3, col_w - 4):
    c.drawString(ML, y, l)
    y -= 10.5
left_bottom = y

y2 = top_y
x2 = ML + col_w + 20
setfill(NAVY); c.setFont("Lora-Bold", 10)
c.drawString(x2, y2, "Circuit Hand-Offs \u2014 exam trap")
y2 -= 4
setstroke(GOLD); c.line(x2, y2, x2 + 160, y2)
y2 -= 13
setfill(DARK); c.setFont("Lora", 8.3)
for l in ["SP (Spleen) -> connects to HT, NOT LI -> via internal branch to heart",
          "HT (Heart) -> connects to SI at HT9 -> radial little finger (SI1)",
          "SI (Small Intestine) -> connects to BL (next week) -> near the eye"]:
    for ll in wrap_words(l, "Lora", 8.3, col_w - 4):
        c.drawString(x2, y2, ll)
        y2 -= 10.5
right_bottom = y2
y = min(left_bottom, right_bottom) - 14

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Nomenclature Recap")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 160, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
c.drawString(ML, y, "Meridian Name = 3 parts: (1) Hand or Foot, (2) Yin or Yang, (3) Zang or Fu organ.")
y -= 11
c.drawString(ML, y, "e.g. \"Heart Meridian of Hand-Shaoyin\" | \"Small Intestine Meridian of Hand-Taiyang\"")
y -= 18

setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(ML, y, "Meridian Clock \u2014 HT & SI in context")
y -= 4
setstroke(GOLD); c.line(ML, y, ML + 200, y)
y -= 13
setfill(DARK); c.setFont("Lora", 8.5)
c.drawString(ML, y, "Preceded by: SP 9-11 AM  |  HT 11 AM-1 PM  |  SI 1-3 PM  |  Followed by: BL 3-5 PM")
y -= 11
c.drawString(ML, y, "Full order: LU LI ST SP HT SI BL KI PC SJ GB LR - 24-hr cycle, 2 hrs each")
y -= 18

setfill(RED); c.setFont("Lora-Bold", 9)
c.drawString(ML, y, "Midterm reminder (Week 5): covers Weeks 1-4 cumulative. Dr. Zhang confirmed many questions will")
y -= 11
c.drawString(ML, y, "reuse Quiz 1-3 material directly - review those quiz kits, not just this Study Guide.")

end_page()

# ============= PAGE 11: HT vs SI COMPARISON =============
new_page()
y = H - HEADER_H - 22
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(ML, y, "HT vs SI  \u2014  Quick Reference Comparison")
y -= 18

setfill(NAVY); c.setFont("Lora-Bold", 8.3)
c.drawString(ML, y, "Attribute")
c.drawString(ML + 150, y, "HT  |  Heart (Hand Shaoyin)")
c.drawString(ML + 340, y, "SI  |  Small Intestine (Hand Taiyang)")
y -= 4
setstroke(GOLD); c.setLineWidth(HAIRLINE * 1.2); c.line(ML, y, ML + CW, y)
y -= 12

rows = [
    ("Yin / Yang", "Yin (postero-medial)", "Yang (postero-lateral)"),
    ("Element", "Fire", "Fire"),
    ("Circuit", "Posterior - Chest to Hand", "Posterior - Hand to Head"),
    ("Clock", "11 AM-1 PM", "1-3 PM"),
    ("Points", "9 (HT1-HT9)", "19 (SI1-SI19)"),
    ("Start", "HT1 Jiquan (axilla)", "SI1 Shaoze (little finger)"),
    ("End", "HT9 Shaochong (little finger)", "SI19 Tinggong (near ear)"),
    ("Pertaining", "Heart", "Small Intestine"),
    ("Connecting", "Small Intestine", "Heart"),
    ("Back-Shu", "BL15", "BL27"),
    ("Front-Mu", "CV14 Juque", "CV4 Guanyuan"),
    ("Yuan-Source", "HT7 Shenmen", "SI4 Wangu"),
    ("Luo", "HT5 Tongli", "SI7 Zhizheng"),
    ("Xi-Cleft", "HT6 Yinxi", "SI6 Yanglao"),
    ("He-Sea", "HT3 Shaohai", "SI8 Xiaohai"),
    ("Confluent Pt", "\u2014", "SI3 (opens Du Mai)"),
    ("Lower He-Sea", "\u2014 (HT is Zang, not Fu)", "ST39 (on the ST channel)"),
    ("Crossing Pts", "ZERO \u2014 only channel with none", "2 (BL1, GB14)"),
    ("Unique Feature", "Only channel w/ 0 crossings", "Connects to eye AND ear"),
    ("Ext Symptoms", "Pain along medial-posterior arm", "Numbness mouth/cheek/throat/neck/arm"),
    ("Int Symptoms", "Palpitations, insomnia, anxiety", "Constipation, lower abd. distension"),
    ("Organ Function", "Governs Blood; houses the Mind", "Receives/transforms/separates fluids"),
    ("Special Clinical Note", "HT9 for emergency/stroke", "SI1 for lactation problems"),
]
setfill(DARK); c.setFont("Lora", 8.2)
for i, (attr, ht_val, si_val) in enumerate(rows):
    h_lines = wrap_words(ht_val, "Lora", 8.2, 175)
    s_lines = wrap_words(si_val, "Lora", 8.2, CW - 340)
    n = max(len(h_lines), len(s_lines), 1)
    row_h = n * 10.5 + 3
    if i % 2 == 0:
        setfill(ROW_TINT); c.rect(ML - 4, y - row_h + 7, CW + 8, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 8.2)
    c.drawString(ML, y, attr)
    setfill(DARK); c.setFont("Lora", 8.2)
    for j, l in enumerate(h_lines):
        c.drawString(ML + 150, y - j * 10.5, l)
    for j, l in enumerate(s_lines):
        c.drawString(ML + 340, y - j * 10.5, l)
    y -= row_h

end_page()

c.save()
print("SAVED:", OUT)
