#!/usr/bin/env python3
"""AC300 Midterm Study Guide (Weeks 1-4 cumulative) - reMarkable edition
Forked from build_studyguide_wk1-4_print.py. Same structural deltas as the
Midterm Cram Sheet reMarkable fork: ivory page background, taller header bars,
bolder hairlines, tinted parchment row backgrounds, double gold rule on cover.
Reference-only document: nomenclature/circuits recap, per-channel deep dives
(MOA image + pathway + full special-points table + clinical pearls) for all
6 channels (LU/LI/ST/SP/HT/SI), special-point category legend, and a
Zang-Fu pairing summary. No quiz questions per current Study Guide content rule.
"""
import math
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
COVER_RED = (0.753, 0.224, 0.169)     # #c0392b - locked cover subtitle color per Week 2 cover spec
GOLD_TAB = (0.784, 0.576, 0.227)      # #c8933a - locked WEEK/MIDTERM badge gold tab color
LIGHTBLUE = (0.929, 0.949, 0.965)     # #edf2f6 - locked cover info-box color
CREAM = (0.961, 0.941, 0.918)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
LIGHTGRAY = (0.90, 0.90, 0.90)

# element accent colors
METAL = (0.365, 0.408, 0.451)
EARTH = (0.663, 0.478, 0.169)
FIRE  = (0.690, 0.204, 0.169)
WATER = (0.220, 0.400, 0.580)
MINFIRE = (0.831, 0.475, 0.412)
WOOD = (0.294, 0.478, 0.271)

MUTED = (0.82, 0.82, 0.82)
MUTED_TXT = (0.45, 0.45, 0.45)
NEARBLACK = (0.10, 0.10, 0.10)

# --- reMarkable-specific edition deltas ---
IVORY = (0.973, 0.953, 0.902)          # warm ivory page background (RGB 248,243,230)
ROW_TINT = (0.925, 0.902, 0.855)       # distinctly tinted parchment row background
CALLOUT_TINT = (0.918, 0.886, 0.816)   # deeper parchment for callout boxes (CREAM ~ IVORY, would blend in)
LW_MULT = 1.35                          # bolder hairline weights on Kaleido 3 e-ink

def tint(col, white_ratio=0.55):
    return tuple(v*(1-white_ratio) + white_ratio for v in col)

MOA_DIR = "/home/claude/moa_images"

OUT = "/mnt/user-data/outputs/AC300_MidtermStudyGuide_Wk1-4_reMarkable.pdf"
c = canvas.Canvas(OUT, pagesize=letter)

def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)

def paint_bg():
    """Fill the current page with the warm ivory reMarkable background."""
    setfill(IVORY); c.rect(0, 0, W, H, fill=1, stroke=0)

def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def header(subtitle):
    setfill(NAVY)
    c.rect(0, H-51, W, 51, fill=1, stroke=0)
    setfill(GOLD)
    c.rect(0, H-51, W, 3, fill=1, stroke=0)
    setfill((1,1,1))
    c.setFont("Lora-Bold", 12)
    c.drawString(36, H-33, "AC300 MIDTERM STUDY GUIDE")
    c.setFont("Lora-Italic", 9.5)
    c.drawRightString(W-36, H-33, subtitle)

def footer(page_label):
    setstroke(GOLD); c.setLineWidth(0.6*LW_MULT)
    c.line(36, 34, W-36, 34)
    setfill(GRAY)
    c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W/2, 22, f"AC300/AC375 Midterm Study Guide (Wk 1-4)  \u00b7  VUIM Summer 2026  \u00b7  {page_label}")

def callout_height(w, lines, heading=None, font_size=8.3, line_h=11):
    pad = 8
    n_lines = sum(len(wrap_words(l, "Lora", font_size, w-pad*2-6)) for l in lines)
    return pad*2 + (14 if heading else 0) + n_lines*line_h

def callout(x, y, w, lines, heading=None, accent=GOLD, font_size=8.3, line_h=11, force_h=None):
    pad = 8
    n_lines = sum(len(wrap_words(l, "Lora", font_size, w-pad*2-6)) for l in lines)
    h = force_h if force_h is not None else pad*2 + (14 if heading else 0) + n_lines*line_h
    setfill(CALLOUT_TINT); c.rect(x, y-h, w, h, fill=1, stroke=0)
    setfill(accent); c.rect(x, y-h, 3, h, fill=1, stroke=0)
    ty = y - pad - 9
    if heading:
        setfill(NAVY); c.setFont("Lora-Bold", 9.5)
        c.drawString(x+pad+6, ty, heading)
        ty -= 15
    setfill(DARK); c.setFont("Lora", font_size)
    for l in lines:
        for line in wrap_words(l, "Lora", font_size, w-pad*2-6):
            c.drawString(x+pad+6, ty, line)
            ty -= line_h
    return y - h - 10

def channel_bar(x, y, w, accent, ch_title, subtitle):
    setfill(accent); c.rect(x, y-4, w, 4, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 13)
    c.drawString(x, y-20, ch_title)
    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawString(x, y-32, subtitle)
    return y - 42

def special_table(x, w, rows, y):
    setfill(LIGHTBLUE); c.rect(x, y-15, w, 15, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 8.3)
    c.drawString(x+4, y-11, "Category")
    c.drawString(x+150, y-11, "Point")
    c.drawString(x+205, y-11, "Notes")
    y -= 15
    c.setFont("Lora", 8.3)
    for i,(cat,pt,note) in enumerate(rows):
        if i%2==0:
            setfill(ROW_TINT); c.rect(x,y-13.5,w,13.5,fill=1,stroke=0)
        setfill(DARK)
        c.drawString(x+4, y-10.3, cat)
        setfill(FIRE); c.setFont("Lora-Bold", 8.3)
        c.drawString(x+150, y-10.3, pt)
        setfill(DARK); c.setFont("Lora", 8.3)
        c.drawString(x+205, y-10.3, note)
        y -= 13.5
    return y

def clock_point(cx, cy, r, clock_deg):
    rad = math.radians(90 - clock_deg)
    return cx + r*math.cos(rad), cy + r*math.sin(rad)

def draw_organ_clock(cx, cy, R_out, R_in):
    segments = [
        ("LU","3-5 AM",  METAL, True), ("LI","5-7 AM",  METAL, True),
        ("ST","7-9 AM",  EARTH, True), ("SP","9-11 AM", EARTH, True),
        ("HT","11AM-1PM",FIRE,  True), ("SI","1-3 PM",  FIRE,  True),
        ("BL","3-5 PM",  WATER, False), ("KI","5-7 PM",  WATER, False),
        ("PC","7-9 PM",  MINFIRE, False), ("SJ","9-11 PM", MINFIRE, False),
        ("GB","11PM-1AM",WOOD, False), ("LR","1-3 AM",  WOOD, False),
    ]
    for i,(ab,tm,col,covered) in enumerate(segments):
        clock_start = i*30
        startAng = 90 - (clock_start+30)
        setfill(col if covered else tint(col))
        setstroke((1,1,1)); c.setLineWidth(1.5*LW_MULT)
        c.wedge(cx-R_out, cy-R_out, cx+R_out, cy+R_out, startAng, 30, fill=1, stroke=1)
    setfill((1,1,1)); c.circle(cx, cy, R_in, fill=1, stroke=0)
    setstroke(GOLD); c.setLineWidth(1.2*LW_MULT)
    c.circle(cx, cy, R_in, fill=0, stroke=1)
    c.circle(cx, cy, R_out, fill=0, stroke=1)
    R_lab = (R_out+R_in)/2
    for i,(ab,tm,col,covered) in enumerate(segments):
        mid = i*30+15
        lx,ly = clock_point(cx,cy,R_lab,mid)
        setfill((1,1,1) if covered else NEARBLACK)
        c.setFont("Lora-Bold", 10)
        c.drawCentredString(lx, ly+3, ab)
        tx,ty = clock_point(cx,cy,R_out+13,mid)
        setfill(DARK if covered else MUTED_TXT)
        c.setFont("Lora-Italic" if covered else "Lora", 6.6)
        c.drawCentredString(tx, ty-1, tm)
        b1 = clock_point(cx,cy,R_out,i*30)
        b2 = clock_point(cx,cy,R_out+5,i*30)
        setstroke((0.6,0.6,0.6)); c.setLineWidth(0.7*LW_MULT)
        c.line(b1[0],b1[1],b2[0],b2[1])
    setfill(NAVY); c.setFont("Lora-Bold", 8.5)
    c.drawCentredString(cx, cy+7, "24-HR")
    c.drawCentredString(cx, cy-5, "QI CYCLE")

def moa_image(ch, x, y_top, max_w, max_h):
    """Draws the MOA channel image, top-anchored at (x, y_top), scaled to
    fit within max_w x max_h keeping aspect ratio. Returns the y of the
    bottom edge of the drawn image."""
    path = f"{MOA_DIR}/MOA_{ch}.jpeg"
    img = ImageReader(path)
    iw, ih = img.getSize()
    scale = min(max_w/iw, max_h/ih)
    dw, dh = iw*scale, ih*scale
    dx = x + (max_w-dw)/2
    dy = y_top - dh
    c.drawImage(img, dx, dy, width=dw, height=dh)
    return dy

# ============= COVER =============
setfill(IVORY); c.rect(0,0,W,H,fill=1,stroke=0)
setfill(NAVY); c.rect(0, H-86, W, 86, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H-86, W, 3, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H-90, W, 1.5, fill=1, stroke=0)
setfill((1,1,1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W/2, H-48, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")

bx, by, bs = W/2-34, H-165, 68
setfill(LIGHTBLUE); c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD_TAB); c.rect(bx, by+bs-8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 7)
c.drawCentredString(W/2, by+bs-22, "MIDTERM")
c.setFont("Lora-Bold", 20)
c.drawCentredString(W/2, by+18, "1-4")

c.setFont("Lora-Bold", 32); setfill(NAVY)
c.drawCentredString(W/2, H-227, "MIDTERM STUDY GUIDE")
c.setFont("Lora-BoldItalic", 18); setfill(COVER_RED)
c.drawCentredString(W/2, H-253, "LU \u00b7 LI \u00b7 ST \u00b7 SP \u00b7 HT \u00b7 SI")
c.setFont("Lora", 11); setfill(DARK)
c.drawCentredString(W/2, H-272, "155 points cumulative  \u00b7  Weeks 1-4  \u00b7  Comprehensive Reference (not a cram sheet)")

setstroke(GOLD); c.setLineWidth(1*LW_MULT)
c.line(W/2-160, H-288, W/2+160, H-288)

box1_w, box2_w, box_h, gap = 250, 250, 150, 20
total = box1_w + box2_w + gap
bx0 = (W-total)/2
by0 = H-460

# Box 1: "This Guide Covers"
setfill(LIGHTBLUE); c.rect(bx0, by0, box1_w, box_h, fill=1, stroke=0)
c.setFont("Lora-Bold", 10.5); setfill(GOLD)
c.drawString(bx0+14, by0+box_h-20, "This Guide Covers:")
bullets1 = [
    "All 6 primary channels: LU, LI, ST, SP, HT, SI",
    "Full pathway (exterior course + interior branch)",
    "Complete special-points table per channel",
    "MOA channel diagrams (Deadman 3rd Ed.)",
    "Circadian clock + Zang-Fu pairing summary",
]
c.setFont("Lora", 8.5); setfill(DARK)
ty = by0+box_h-38
for b in bullets1:
    for line in wrap_words(b, "Lora", 8.5, box1_w-28):
        c.drawString(bx0+14, ty, line)
        ty -= 11.5

# Box 2: info block
bx1 = bx0 + box1_w + gap
setfill(LIGHTBLUE); c.rect(bx1, by0, box2_w, box_h, fill=1, stroke=0)
c.setFont("Lora-Bold", 10.5); setfill(COVER_RED)
c.drawString(bx1+14, by0+box_h-20, "Midterm covers Weeks 1-4")
c.setFont("Lora", 8.5); setfill(DARK)
info_lines = [
    "MOA (Deadman) pages: LU 76, LI 100, ST 130, SP 182, HT 212, SI 231",
    "This guide is reference-only \u2014 no quiz questions.",
    "For self-testing, use the Week 1-4 Quiz Kits and the",
    "Midterm Cram Sheet (Wk 1-4) instead.",
]
ty = by0+box_h-38
for l in info_lines:
    for line in wrap_words(l, "Lora", 8.5, box2_w-28):
        c.drawString(bx1+14, ty, line)
        ty -= 11.5

# channel badge row
setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W/2, by0-26, "6 channels, color-coded by element")
chans = [("LU","Metal",METAL),("LI","Metal",METAL),("ST","Earth",EARTH),
         ("SP","Earth",EARTH),("HT","Fire",FIRE),("SI","Fire",FIRE)]
cb_w, cb_gap = 78, 10
total_cb = cb_w*6 + cb_gap*5
cbx0 = (W-total_cb)/2
cby = by0 - 90
for i,(ab,el,col) in enumerate(chans):
    x = cbx0 + i*(cb_w+cb_gap)
    c.setFillColorRGB(*col); c.circle(x+cb_w/2, cby+16, 16, fill=1, stroke=0)
    setfill((1,1,1)); c.setFont("Lora-Bold", 11)
    c.drawCentredString(x+cb_w/2, cby+11, ab)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(x+cb_w/2, cby-8, el)

setstroke(GOLD); c.setLineWidth(1*LW_MULT)
c.line(50, 70, W-50, 70)
c.setFont("Lora-Italic", 8.5); setfill(GRAY)
c.drawCentredString(W/2, 50, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")
c.showPage()
paint_bg()

# ============= PAGE 2: Theory Recap + Circadian Clock =============
header("Channel Theory Recap + Circadian Clock")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(36, y, "NOMENCLATURE & CORE RULES"); y -= 9
setstroke(GOLD); c.setLineWidth(1.2*LW_MULT); c.line(36, y, 280, y); y -= 14

col_w = (W-72-16)/2
y_top_boxes = y
boxes = [
    ("Nomenclature (3 parts)", "Hand/Foot (location) + Yin/Yang (medial/lateral, nature) + Zang/Fu (pertaining organ, function)."),
    ("Qi circulation direction", "Hand Yin: chest -> hand  |  Hand Yang: hand -> head  |  Foot Yang: head -> foot  |  Foot Yin: foot -> abdomen/chest"),
    ("Zang-Fu pairing logic", "Each Yin (zang) channel pairs with one Yang (fu) channel; paired channels treat each other's organ symptoms (e.g. LU constipation -> use LI points)."),
    ("The Three Circuits", "Anterior = Yangming (LI/ST), Middle = Shaoyang (SJ/GB, weeks 7-9), Posterior = Taiyang (SI/BL, week 5) -- also called the Inner Circuit on earlier slide versions."),
]
bh = 62
for i,(head,body) in enumerate(boxes):
    bx = 36 + (i%2)*(col_w+16)
    by = y_top_boxes - (i//2)*(bh+12)
    y_box = callout(bx, by, col_w, [body], heading=head, accent=GOLD, font_size=8.4, line_h=10.8, force_h=bh)
y = y_top_boxes - 2*(bh+12) - 6

setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(36, y, "CIRCADIAN CLOCK \u2014 24-HOUR QI CYCLE"); y -= 9
setstroke(GOLD); c.setLineWidth(1.2*LW_MULT); c.line(36, y, 280, y); y -= 20

cx, cy = W/2, y - 130
draw_organ_clock(cx, cy, 92, 42)
y = cy - 92 - 22

leg_items = [("Metal (LU/LI)", METAL, True), ("Earth (ST/SP)", EARTH, True),
             ("Fire (HT/SI)", FIRE, True), ("Water (BL/KI)", WATER, False),
             ("Fire-Min. (PC/SJ)", MINFIRE, False), ("Wood (LR/GB)", WOOD, False)]
lx = 36
c.setFont("Lora", 8)
for label, col, covered in leg_items:
    c.setFillColorRGB(*col); c.circle(lx+5, y+3, 5, fill=1, stroke=0)
    setfill(DARK if covered else MUTED_TXT)
    c.drawString(lx+15, y, label)
    lx += 15 + pdfmetrics.stringWidth(label, "Lora", 8) + 14
y -= 20

y = callout(36, y, W-72, [
    "Paired organs sit in adjacent clock slots (LU/LI, ST/SP, HT/SI) \u2014 the Qi circulation chain flows straight from one into the next around the full 24-hour cycle. Muted wedges (BL/KI/PC/SJ/GB/LR) are covered in later weeks.",
    "Clinical use: a patient waking at a specific hour night after night may point to dysfunction in that hour's organ \u2014 diagnostic, not a treatment rule.",
], accent=GOLD, font_size=8.6, line_h=11)

footer("Page 2 of 16")
c.showPage()
paint_bg()


# ============= PER-CHANNEL DATA (reused/verified from Midterm Cram Sheet v6) =============
channels_meta = {
 "LU": dict(full="Lung", nom="Hand Taiyin \u00b7 Yin \u00b7 Metal \u00b7 Peak 3-5AM \u00b7 Paired: LI \u00b7 11 pts", accent=METAL,
    pathway="Exterior course: begins at the underarm (LU1), runs down the arm through the elbow (LU5) and wrist (LU9), ending at the thumb tip (LU11). Interior branch (no points): connects Lung to Large Intestine.",
    organs=("Lung","Large Intestine"), moa_page=76),
 "LI": dict(full="Large Intestine", nom="Hand Yangming \u00b7 Yang \u00b7 Metal \u00b7 Peak 5-7AM \u00b7 Paired: LU \u00b7 20 pts", accent=METAL,
    pathway="Exterior course: begins at the index finger (LI1), runs up through the elbow (LI11) and shoulder (LI15), ending at the nose (LI20). Interior branch (no points): connects Large Intestine to Lung.",
    organs=("Large Intestine","Lung"), moa_page=100),
 "ST": dict(full="Stomach", nom="Foot Yangming \u00b7 Yang \u00b7 Earth \u00b7 Peak 7-9AM \u00b7 Paired: SP \u00b7 45 pts", accent=EARTH,
    pathway="Exterior course: begins at the face (ST1), passes the clavicle (ST12) and umbilicus (ST25), ending at the toe (ST45). Interior branch (no points): connects Stomach to Spleen. A separate lower-orifice branch runs from the abdomen, through the diaphragm, to the Spleen.",
    organs=("Stomach","Spleen"), moa_page=130),
 "SP": dict(full="Spleen", nom="Foot Taiyin \u00b7 Yin \u00b7 Earth \u00b7 Peak 9-11AM \u00b7 Paired: ST \u00b7 21 pts", accent=EARTH,
    pathway="Exterior course: begins at the big toe (SP1), passes the ankle (SP6) and thigh (SP10), ending at the chest (SP21). Interior branch (no points): connects Spleen to Stomach. A separate branch runs from the stomach, through the diaphragm, to the Heart.",
    organs=("Spleen","Stomach"), moa_page=182),
 "HT": dict(full="Heart", nom="Hand Shaoyin \u00b7 Yin \u00b7 Fire \u00b7 Peak 11AM-1PM \u00b7 Paired: SI \u00b7 9 pts", accent=FIRE,
    pathway="Exterior course: begins at the axilla (HT1), passes the elbow (HT3) and wrist (HT7), ending at the pinky tip (HT9). Interior branch (no points): connects Heart to Small Intestine. A separate branch runs from the heart system to the eye system.",
    organs=("Heart","Small Intestine"), moa_page=212),
 "SI": dict(full="Small Intestine", nom="Hand Taiyang \u00b7 Yang \u00b7 Fire \u00b7 Peak 1-3PM \u00b7 Paired: HT \u00b7 19 pts", accent=FIRE,
    pathway="Exterior course: begins at the pinky finger (SI1), passes the elbow (SI8) and scapula (SI11), ending at the ear (SI19). Interior branch (no points): connects Small Intestine to Heart.",
    organs=("Small Intestine","Heart"), moa_page=231),
}

pearls_data = {
 "LU": ["LU7: command for head/neck; opens Ren Mai; #1 point for exterior wind",
        "LU9: Yuan-source; influential for vessels; tonifies Lung Qi and Yin",
        "LU5: He-Sea; clears heat, descends Qi; treats cough/asthma/hemoptysis",
        "LU1: Front-Mu; chest fullness, grief, chronic cough"],
 "LI": ["LI4: command for face/mouth; clears wind-heat; FORBIDDEN in pregnancy",
        "LI11: He-Sea; clears heat in blood; skin disorders, high fever",
        "LI20: local for nasal disorders; reunion point with ST channel",
        "LI10: empirical for GI complaints; shoulder/arm pain"],
 "ST": ["ST36: command for abdomen; tonifies Qi and Blood; most important tonic point",
        "ST40: Luo; resolves phlegm-dampness anywhere in the body",
        "ST25: Front-Mu of LI; regulates intestines, transforms stagnation",
        "ST44: clears Yangming heat; toothache, epistaxis, fever"],
 "SP": ["SP6: crossing of 3 Yin channels; regulates menstruation, calms mind; FORBIDDEN in pregnancy",
        "SP9: He-Sea; resolves dampness; edema, diarrhea, knee pain",
        "SP10: Sea of Blood; cools blood; skin disorders, irregular menstruation",
        "SP4: Luo + Confluent (Chong Mai); GI disorders, menstrual issues"],
 "HT": ["HT7: Yuan-source; calms shen; insomnia, anxiety, palpitations",
        "HT3: He-Sea; clears heart fire; fear, arm pain",
        "HT6: Xi-Cleft; night sweats, acute heart pain",
        "HT8: Ying-Spring; clears heart fire; oral ulcers, urinary urgency"],
 "SI": ["SI3: confluent (Du Mai); neck/spine disorders; opens governing vessel",
        "SI11: most important local point for frozen shoulder",
        "SI19: local point for tinnitus and deafness",
        "SI4: Yuan-source; wrist and finger pain; febrile diseases"],
}

special_rows = {
 "LU": [("Jing-Well","LU11",""),("Ying-Spring","LU10",""),("Shu-Stream","LU9","also Yuan-Source"),
      ("Jing-River","LU8",""),("He-Sea","LU5","clears heat, descends Qi"),("Luo","LU7","also Confluent + Command"),
      ("Xi-Cleft","LU6",""),("Front-Mu","LU1","chest fullness, grief"),("Back-Shu","BL13",""),
      ("Confluent","LU7","opens Ren Mai"),("Command","LU7","head/neck")],
 "LI": [("Jing-Well","LI1",""),("Ying-Spring","LI2",""),("Shu-Stream","LI3",""),("Jing-River","LI5",""),
      ("He-Sea","LI11","clears heat in blood"),("Yuan-Source","LI4","FORBIDDEN in pregnancy"),
      ("Luo","LI6",""),("Xi-Cleft","LI7",""),("Front-Mu","ST25","of Large Intestine"),
      ("Back-Shu","BL25",""),("Command","LI4","face/mouth")],
 "ST": [("Jing-Well","ST45",""),("Ying-Spring","ST44","clears Yangming heat"),("Shu-Stream","ST43",""),
      ("Jing-River","ST41",""),("He-Sea","ST36","command abdomen, most important tonic pt"),
      ("Yuan-Source","ST42",""),("Luo","ST40","resolves phlegm-dampness anywhere"),("Xi-Cleft","ST34",""),
      ("Front-Mu","CV12",""),("Back-Shu","BL21",""),("Command","ST36","abdomen"),("Lower He-Sea","ST37","of Large Intestine")],
 "SP": [("Jing-Well","SP1",""),("Ying-Spring","SP2",""),("Shu-Stream","SP3","also Yuan-Source"),
      ("Jing-River","SP5",""),("He-Sea","SP9","resolves dampness"),("Luo","SP4","also Confluent (Chong Mai)"),
      ("Xi-Cleft","SP8",""),("Front-Mu","LR13",""),("Back-Shu","BL20",""),
      ("Confluent","SP4","opens Chong Mai"),("Sea of Blood","SP10","cools blood, skin/menstrual")],
 "HT": [("Jing-Well","HT9",""),("Ying-Spring","HT8","clears heart fire"),("Shu-Stream","HT7","also Yuan-Source"),
      ("Jing-River","HT4",""),("He-Sea","HT3","clears heart fire, fear/arm pain"),("Luo","HT5",""),
      ("Xi-Cleft","HT6","night sweats, acute heart pain"),("Front-Mu","CV14",""),("Back-Shu","BL15","")],
 "SI": [("Jing-Well","SI1",""),("Ying-Spring","SI2",""),("Shu-Stream","SI3","also Confluent"),
      ("Jing-River","SI5",""),("He-Sea","SI8",""),("Yuan-Source","SI4","wrist/finger pain, febrile disease"),
      ("Luo","SI7",""),("Xi-Cleft","SI6",""),("Front-Mu","CV4",""),("Back-Shu","BL27",""),
      ("Confluent","SI3","opens Du Mai")],
}

page_num = 3
def deepdive_page_A(ch):
    global page_num
    m = channels_meta[ch]
    header(f"{ch} \u2014 {m['full']}  \u2014  Pathway & MOA Diagram")
    y = H - 62
    y = channel_bar(36, y, W-72, m['accent'], f"{ch} \u2014 {m['full']}", m['nom'])
    y -= 8

    img_w = 200
    img_top = y
    img_bottom = moa_image(ch, 36, img_top, img_w, 400)
    setfill(GRAY); c.setFont("Lora-Italic", 7)
    c.drawCentredString(36+img_w/2, img_bottom-11, f"MOA (Deadman 3rd Ed.), p.{m['moa_page']}")

    rx = 36 + img_w + 20
    rw = (W-36) - rx
    ry = y
    ry = callout(rx, ry, rw, [
        f"Pertains: {m['organs'][0]}",
        f"Connects: {m['organs'][1]}",
        m['nom'],
    ], heading="Quick Facts", accent=m['accent'], font_size=8.6, line_h=12)
    ry -= 6
    ry = callout(rx, ry, rw, [m['pathway']], heading="Pathway (Exterior + Interior)", accent=m['accent'], font_size=8.6, line_h=11.5)

    footer(f"Page {page_num} of 16")
    page_num += 1
    c.showPage()
    paint_bg()

def deepdive_page_B(ch):
    global page_num
    m = channels_meta[ch]
    header(f"{ch} \u2014 {m['full']}  \u2014  Special Points & Clinical Pearls")
    y = H - 62
    y = channel_bar(36, y, W-72, m['accent'], f"{ch} \u2014 {m['full']}", m['nom'])
    y = special_table(36, W-72, special_rows[ch], y) - 8
    y = callout(36, y+8, W-72, pearls_data[ch], heading="Clinical Pearls", accent=m['accent'], font_size=8.6, line_h=11.5)
    footer(f"Page {page_num} of 16")
    page_num += 1
    c.showPage()
    paint_bg()

for ch in ["LU","LI","ST","SP","HT","SI"]:
    deepdive_page_A(ch)
    deepdive_page_B(ch)

# ============= PAGE 15: Special Point Category Reference =============
header("Special Point Category Reference")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(36, y, "WHAT EACH CATEGORY MEANS"); y -= 9
setstroke(GOLD); c.setLineWidth(1.2*LW_MULT); c.line(36, y, 280, y); y -= 6
y = callout(36, y, W-72, [
    "For a fully drillable, standalone version of this material with worked examples, see the Special Points Decoder for each week.",
], accent=GOLD, font_size=8.2, line_h=10.5)
y -= 4

cat_rows = [
    ("Category","What it means","Examples (Wk 1-4)"),
]
setfill(LIGHTBLUE); c.rect(36, y-15, W-72, 15, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 8.3)
c.drawString(40, y-11, "Category"); c.drawString(160, y-11, "What it means"); c.drawString(400, y-11, "Examples (Wk 1-4)")
y -= 15
rows = [
    ("Jing-Well","\"Where it emerges\" - distal-most point; channel's start/end; first aid, clears heat, relieves pain","LU11, HT9, LI1, ST45, SP1, SI1"),
    ("Ying-Spring","\"Where it flows\" - before the MCP/MTP joint; treats feverish diseases, heat-related disorders","LU10, LI2, ST44, SP2, HT8, SI2"),
    ("Shu-Stream","\"Where it pours\" - after the MCP/MTP joint; treats heaviness in the body, joint pain","LU9(Yuan), LI3, ST43, SP3(Yuan), HT7(Yuan), SI3(Confluent)"),
    ("Jing-River","\"Where it travels\" - forearm/lower leg; treats externally contracted disease, cough, asthma","LU8, LI5, ST41, SP5, HT4, SI5"),
    ("He-Sea","\"Where it enters\" - near elbow/knee; where Qi enters deepest; treats organ-level disorders","LU5, LI11, ST36, SP9, HT3, SI8"),
    ("Yuan-Source","Reflects/regulates the organ's original Qi; primary diagnostic + treatment point","LU9, LI4, ST42, SP3, HT7, SI4"),
    ("Luo-Connecting","Links each paired Yin/Yang channel; treats symptoms of both channels in the pair","LU7, LI6, ST40, SP4, HT5, SI7"),
    ("Xi-Cleft","Accumulation point; treats acute pain, bleeding, or crisis flare of that channel","LU6, LI7, ST34, SP8, HT6, SI6"),
    ("Front-Mu","Diagnostic/treatment point on chest/abdomen for the paired organ","LU1, ST25(LI), CV12(ST), LR13(SP), CV14(HT), CV4(SI)"),
    ("Back-Shu","Diagnostic/treatment point on the back for the paired organ","BL13(LU), BL25(LI), BL21(ST), BL20(SP), BL15(HT), BL27(SI)"),
    ("Confluent","Opens one of the 8 Extraordinary Vessels","LU7(Ren Mai), SP4(Chong Mai), SI3(Du Mai)"),
    ("Command","Broad regional treatment authority over a body area","LU7(head/neck), LI4(face/mouth), ST36(abdomen)"),
]
c.setFont("Lora", 7.6)
for i,(cat,meaning,ex) in enumerate(rows):
    row_h = max(11, len(wrap_words(meaning,"Lora",7.6,230))*10)
    if i%2==0:
        setfill(ROW_TINT); c.rect(36,y-row_h,W-72,row_h,fill=1,stroke=0)
    setfill(COVER_RED); c.setFont("Lora-Bold", 7.8)
    c.drawString(40, y-10, cat)
    setfill(DARK); c.setFont("Lora", 7.6)
    ty = y-10
    for line in wrap_words(meaning, "Lora", 7.6, 230):
        c.drawString(160, ty, line); ty -= 10
    ty2 = y-10
    for line in wrap_words(ex, "Lora", 7.3, 165):
        setfill(GRAY); c.drawString(400, ty2, line); ty2 -= 9.5
    y -= row_h

footer("Page 15 of 16")
c.showPage()
paint_bg()

# ============= PAGE 16: Zang-Fu Pairing Summary =============
header("Zang-Fu Pairing Summary \u2014 All 3 Pairs (Wk 1-4)")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(36, y, "THE THREE INTERIOR-EXTERIOR PAIRS"); y -= 9
setstroke(GOLD); c.setLineWidth(1.2*LW_MULT); c.line(36, y, 280, y); y -= 6
y = callout(36, y, W-72, [
    "Each Yin (Zang, solid organ) channel pairs with one Yang (Fu, hollow organ) channel. They share an element, sit in adjacent circadian-clock slots, and their special points cross-reference each other (paired organ's Front-Mu/Back-Shu, Luo-connecting points).",
], accent=GOLD, font_size=8.4, line_h=11)
y -= 6

pairs = [
    ("LU \u2014 LI  (Metal)", METAL, [
        ("Zang (Yin)","Lung (LU) \u00b7 11 pts \u00b7 3-5 AM"),
        ("Fu (Yang)","Large Intestine (LI) \u00b7 20 pts \u00b7 5-7 AM"),
        ("Shared function","Both regulate descending/clearing of Qi and fluids; LU governs Qi + skin, LI governs transmission/excretion."),
        ("Cross-reference","LU1 = Front-Mu of LU itself; ST25 = Front-Mu of LI; BL13/BL25 = Back-Shu pair on Bladder channel."),
    ]),
    ("ST \u2014 SP  (Earth)", EARTH, [
        ("Zang (Yin)","Spleen (SP) \u00b7 21 pts \u00b7 9-11 AM"),
        ("Fu (Yang)","Stomach (ST) \u00b7 45 pts \u00b7 7-9 AM"),
        ("Shared function","Both govern digestion/transformation of food and fluids; ST 'rots and ripens', SP transforms and transports."),
        ("Cross-reference","LR13 = Front-Mu of SP (not ST's own channel); CV12 = Front-Mu of ST; BL20/BL21 = Back-Shu pair."),
    ]),
    ("HT \u2014 SI  (Fire)", FIRE, [
        ("Zang (Yin)","Heart (HT) \u00b7 9 pts \u00b7 11 AM-1 PM"),
        ("Fu (Yang)","Small Intestine (SI) \u00b7 19 pts \u00b7 1-3 PM"),
        ("Shared function","HT governs Shen (mind) and blood; SI 'separates the pure from the turbid' in digestion."),
        ("Cross-reference","CV14 = Front-Mu of HT; CV4 = Front-Mu of SI; BL15/BL27 = Back-Shu pair."),
    ]),
]
col_w = W-72
for title, accent, rows in pairs:
    y = channel_bar(36, y, col_w, accent, title, "")
    for label, val in rows:
        setfill(NAVY); c.setFont("Lora-Bold", 8.5)
        c.drawString(36, y-10, label+":")
        setfill(DARK); c.setFont("Lora", 8.3)
        lines = wrap_words(val, "Lora", 8.3, col_w-140)
        ty = y-10
        for line in lines:
            c.drawString(170, ty, line); ty -= 10.5
        y -= max(14, len(lines)*10.5+4)
    y -= 8

footer("Page 16 of 16")
c.showPage()

c.save()
print("SAVED:", OUT)
