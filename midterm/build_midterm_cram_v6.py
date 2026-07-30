#!/usr/bin/env python3
"""AC300 Midterm Cram Sheet (Weeks 1-4 cumulative) - Print edition v2, prettier"""
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
LIGHTBLUE = (0.929, 0.949, 0.965)
CREAM = (0.961, 0.941, 0.918)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
LIGHTGRAY = (0.90,0.90,0.90)

# element accent colors (darkened for contrast on white)
METAL = (0.365, 0.408, 0.451)   # slate gray-blue
EARTH = (0.663, 0.478, 0.169)   # amber/ochre
FIRE  = (0.690, 0.204, 0.169)   # deep red (HT/SI, primary fire)
WATER = (0.220, 0.400, 0.580)   # blue (BL/KI)
MINFIRE = (0.831, 0.475, 0.412) # lighter red/coral (PC/SJ, ministerial fire - distinct tint of FIRE, not purple)
WOOD = (0.294, 0.478, 0.271)    # green (LR/GB)

MUTED = (0.82, 0.82, 0.82)   # not-yet-covered organs
MUTED_TXT = (0.45, 0.45, 0.45)
NEARBLACK = (0.10, 0.10, 0.10)  # for text on pastel-tinted (not-yet-covered) wedges/boxes

def tint(col, white_ratio=0.55):
    """Blend a color toward white to make a lighter/muted pastel version
    that still reads as its own hue (distinguishing Water/Fire-Min/Wood)
    rather than collapsing every not-yet-covered element into flat gray."""
    return tuple(v*(1-white_ratio) + white_ratio for v in col)

def clock_point(cx, cy, r, clock_deg):
    """clock_deg measured clockwise from top (12 o'clock = 0)"""
    rad = math.radians(90 - clock_deg)
    return cx + r*math.cos(rad), cy + r*math.sin(rad)

def draw_organ_clock(cx, cy, R_out, R_in, top_y):
    """Draws a 24hr organ-clock wheel (12 x 2hr wedges) centered at cx,cy.
    top_y is the y-coordinate of the top of the diagram (for reference only)."""
    segments = [
        ("LU","3-5 AM",  METAL, True),
        ("LI","5-7 AM",  METAL, True),
        ("ST","7-9 AM",  EARTH, True),
        ("SP","9-11 AM", EARTH, True),
        ("HT","11AM-1PM",FIRE,  True),
        ("SI","1-3 PM",  FIRE,  True),
        ("BL","3-5 PM",  WATER, False),
        ("KI","5-7 PM",  WATER, False),
        ("PC","7-9 PM",  MINFIRE, False),
        ("SJ","9-11 PM", MINFIRE, False),
        ("GB","11PM-1AM",WOOD, False),
        ("LR","1-3 AM",  WOOD, False),
    ]
    for i,(ab,tm,col,covered) in enumerate(segments):
        clock_start = i*30
        clock_end = clock_start+30
        startAng = 90 - clock_end
        setfill(col if covered else tint(col))
        setstroke((1,1,1)); c.setLineWidth(1.5)
        c.wedge(cx-R_out, cy-R_out, cx+R_out, cy+R_out, startAng, 30, fill=1, stroke=1)
    # punch hole for donut look
    setfill((1,1,1))
    c.circle(cx, cy, R_in, fill=1, stroke=0)
    setstroke(GOLD); c.setLineWidth(1.2)
    c.circle(cx, cy, R_in, fill=0, stroke=1)
    c.circle(cx, cy, R_out, fill=0, stroke=1)
    # labels
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
        # tick mark at boundary
        b1 = clock_point(cx,cy,R_out,i*30)
        b2 = clock_point(cx,cy,R_out+5,i*30)
        setstroke((0.6,0.6,0.6)); c.setLineWidth(0.7)
        c.line(b1[0],b1[1],b2[0],b2[1])
    # center hub
    setfill(NAVY)
    c.setFont("Lora-Bold", 8.5)
    c.drawCentredString(cx, cy+7, "24-HR")
    c.drawCentredString(cx, cy-5, "QI CYCLE")

OUT = "/mnt/user-data/outputs/AC300_MidtermCramSheet_Wk1-4_Print.pdf"
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
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def header(subtitle):
    setfill(NAVY)
    c.rect(0, H-44, W, 44, fill=1, stroke=0)
    setfill(GOLD)
    c.rect(0, H-44, W, 3, fill=1, stroke=0)
    setfill((1,1,1))
    c.setFont("Lora-Bold", 12)
    c.drawString(36, H-29, "AC300 MIDTERM CRAM SHEET")
    c.setFont("Lora-Italic", 9.5)
    c.drawRightString(W-36, H-29, subtitle)

def footer(page_label):
    setstroke(GOLD); c.setLineWidth(0.6)
    c.line(36, 34, W-36, 34)
    setfill(GRAY)
    c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W/2, 22, f"AC300/AC375 Midterm Cram Sheet (Wk 1-4)  \u00b7  VUIM Summer 2026  \u00b7  {page_label}")

def callout_height(w, lines, heading=None, font_size=8.3, line_h=11):
    pad = 8
    n_lines = sum(len(wrap_words(l, "Lora", font_size, w-pad*2-6)) for l in lines)
    return pad*2 + (14 if heading else 0) + n_lines*line_h

def callout(x, y, w, lines, heading=None, accent=GOLD, font_size=8.3, line_h=11, force_h=None):
    """Cream callout box with gold left bar, returns new y below box"""
    pad = 8
    n_lines = sum(len(wrap_words(l, "Lora", font_size, w-pad*2-6)) for l in lines)
    h = force_h if force_h is not None else pad*2 + (14 if heading else 0) + n_lines*line_h
    setfill(CREAM); c.rect(x, y-h, w, h, fill=1, stroke=0)
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
            setfill((0.965,0.967,0.972)); c.rect(x,y-13.5,w,13.5,fill=1,stroke=0)
        setfill(DARK)
        c.drawString(x+4, y-10.3, cat)
        setfill(FIRE); c.setFont("Lora-Bold", 8.3)
        c.drawString(x+150, y-10.3, pt)
        setfill(DARK); c.setFont("Lora", 8.3)
        c.drawString(x+205, y-10.3, note)
        y -= 13.5
    return y

# ============= COVER =============
c.setFillColorRGB(1,1,1); c.rect(0,0,W,H,fill=1,stroke=0)
setfill(NAVY); c.rect(0, H-80, W, 80, fill=1, stroke=0)
setfill(GOLD); c.rect(0, H-80, W, 3, fill=1, stroke=0)
setfill((1,1,1)); c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W/2, H-45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")

bx, by, bs = W/2-34, H-165, 68
setfill(LIGHTBLUE); c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD); c.rect(bx, by+bs-8, bs, 8, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 7)
c.drawCentredString(W/2, by+bs-22, "MIDTERM")
c.setFont("Lora-Bold", 20)
c.drawCentredString(W/2, by+18, "1-4")

c.setFont("Lora-Bold", 30); setfill(NAVY)
c.drawCentredString(W/2, H-227, "MIDTERM CRAM SHEET")
c.setFont("Lora-BoldItalic", 13); setfill(RED)
c.drawCentredString(W/2, H-250, "Channel Theory + LU \u00b7 LI \u00b7 ST \u00b7 SP \u00b7 HT \u00b7 SI")
c.setFont("Lora", 10.5); setfill(DARK)
c.drawCentredString(W/2, H-268, "155 points cumulative  \u00b7  Weeks 1-4  \u00b7  Midterm covers this material")

setstroke(GOLD); c.setLineWidth(1)
c.line(W/2-140, H-282, W/2-40, H-282)
c.line(W/2+40, H-282, W/2+140, H-282)
setfill(GOLD); c.circle(W/2, H-282, 2.5, fill=1, stroke=0)

box_w, box_h, gap = 150, 66, 15
total = box_w*3 + gap*2
bx0 = (W-total)/2
by0 = H-378
labels = [("CHANNELS", "6 channels, 155 pts", "Circadian clock order", (0.157,0.302,0.541)),
          ("SPECIAL PTS", "Yuan/Luo/Xi-Cleft", "Front-Mu/Back-Shu/He-Sea", (0.380,0.180,0.522)),
          ("HIGH-YIELD", "Forbidden pregnancy", "Commonly confused pairs", (0.106,0.369,0.353))]
for i,(t,l1,l2,col) in enumerate(labels):
    x = bx0 + i*(box_w+gap)
    setfill((0.933,0.937,0.949)); c.rect(x, by0, box_w, box_h, fill=1, stroke=0)
    c.setFillColorRGB(*col); c.rect(x, by0+box_h-3, box_w, 3, fill=1, stroke=0)
    c.setFont("Lora-Bold", 10)
    c.drawCentredString(x+box_w/2, by0+box_h-20, t)
    c.setFont("Lora-Italic", 8); c.setFillColorRGB(*DARK)
    c.drawCentredString(x+box_w/2, by0+box_h-35, l1)
    c.drawCentredString(x+box_w/2, by0+box_h-48, l2)

# channel badge row - element color coded
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

setfill(GRAY); c.setFont("Lora-Italic", 8)
c.drawCentredString(W/2, cby-40, "+ circadian clock \u00b7 confluent/command points \u00b7 special-point category legend \u00b7 forbidden-pregnancy flags")

setstroke(GOLD); c.setLineWidth(1)
c.line(50, 70, W-50, 70)
c.setFont("Lora-Italic", 8.5); setfill(GRAY)
c.drawCentredString(W/2, 50, "Jonathan Centeno \u00b7 D.AcHM Candidate \u00b7 Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")
c.showPage()

# ============= PAGE 2: Channel Theory + Circadian Clock =============
header("Channel Theory + Circadian Clock")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 14)
c.drawString(36, y, "CHANNEL THEORY \u2014 CORE RULES"); y -= 8
setstroke(GOLD); c.setLineWidth(1.2); c.line(36, y, 220, y); y -= 16

rules = [
    ("Nomenclature (3 parts)", "Hand/Foot (location) + Yin/Yang (medial/lateral, nature) + Zang/Fu (pertaining organ, function)"),
    ("Qi circulation direction", "Hand Yin: chest -> hand   |   Hand Yang: hand -> head   |   Foot Yang: head -> foot   |   Foot Yin: foot -> abdomen/chest"),
    ("Hand Yin / Hand Yang meet", "At the fingers (e.g. LU7 -> LI1 branch meets at index finger)"),
    ("12 Primary Meridians", "3 Hand Yin + 3 Hand Yang + 3 Foot Yin + 3 Foot Yang = 12. Plus 8 Extraordinary Vessels, 15 Luo-connecting, divergent + sinew + cutaneous channels."),
    ("Zang-Fu pairing logic", "Each Yin (zang) channel pairs with one Yang (fu) channel; paired channels treat each other's organ symptoms (e.g. LU constipation -> use LI points)."),
    ("Hand Yang distribution", "Anterior = Yangming, Middle = Shaoyang, Posterior = Taiyang (also applies conceptually to Foot Yang)."),
]
col_w = (W-72-16)/2
for i in range(0, len(rules), 2):
    row_y = y
    pair = rules[i:i+2]
    heights = [callout_height(col_w, [txt], heading=label, font_size=8.2, line_h=10.5) for label,txt in pair]
    row_h = max(heights)
    for j,(label, txt) in enumerate(pair):
        x = 36 + j*(col_w+16)
        callout(x, row_y, col_w, [txt], heading=label, accent=GOLD, font_size=8.2, line_h=10.5, force_h=row_h)
    y = row_y - row_h - 10
y -= 6

setfill(NAVY); c.setFont("Lora-Bold", 14)
c.drawString(36, y, "CIRCADIAN CLOCK \u2014 24-HOUR QI CYCLE"); y -= 8
setstroke(GOLD); c.line(36, y, 220, y); y -= 12

R_out, R_in = 92, 42
cx = W/2
clock_top = y
cy = y - R_out - 6
draw_organ_clock(cx, cy, R_out, R_in, clock_top)
y = cy - R_out - 22

# legend row
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
y = callout(36, y+8, W-72, ["Paired organs sit in adjacent clock slots (LU/LI, ST/SP, HT/SI) \u2014 the Qi circulation chain flows straight from one into the next. Muted wedges (BL/KI/PC/SJ/GB/LR) are covered in later weeks."], accent=GOLD, font_size=8.2)
y -= 4

setfill(NAVY); c.setFont("Lora-Bold", 14)
c.drawString(36, y, "6 CHANNELS AT A GLANCE"); y -= 8
setstroke(GOLD); c.line(36, y, 220, y); y -= 18
setfill(LIGHTBLUE); c.rect(36, y-16, W-72, 16, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 8.5)
heads = ["Ch","Full name","Type","Element","Pts","Paired","Front-Mu","Back-Shu"]
xs = [40, 65, 178, 225, 280, 310, 355, 425]
for h,x in zip(heads,xs): c.drawString(x, y-12, h)
y -= 16
rows = [
    ("LU","Hand Taiyin","Yin","Metal","11","LI","LU1","BL13",METAL),
    ("LI","Hand Yangming","Yang","Metal","20","LU","ST25","BL25",METAL),
    ("ST","Foot Yangming","Yang","Earth","45","SP","CV12","BL21",EARTH),
    ("SP","Foot Taiyin","Yin","Earth","21","ST","LR13","BL20",EARTH),
    ("HT","Hand Shaoyin","Yin","Fire","9","SI","CV14","BL15",FIRE),
    ("SI","Hand Taiyang","Yang","Fire","19","HT","CV4","BL27",FIRE),
]
c.setFont("Lora", 8.5)
for i,row in enumerate(rows):
    col = row[-1]; row = row[:-1]
    if i%2==0:
        setfill((0.973,0.973,0.976)); c.rect(36,y-15,W-72,15,fill=1,stroke=0)
    setfill(col); c.rect(36, y-15, 3, 15, fill=1, stroke=0)
    for idx,(val,x) in enumerate(zip(row,xs)):
        if idx == 3:  # Element column
            setfill(col); c.setFont("Lora-Bold", 8.5)
            c.drawString(x, y-11, val)
            c.setFont("Lora", 8.5)
        else:
            setfill(DARK)
            c.drawString(x, y-11, val)
    y -= 15
footer("Page 2 of 8")
c.showPage()

# ============= PAGE 3: Six-Channel Nomenclature / Three Circuits (NEW) =============

def circuit_box(x, y, w, h, title, top_pair, bot_pair, covered_top, covered_bot):
    """pair = (hand_organ, hand_lbl, element, color, yang_organ, yang_lbl, direction)"""
    setfill((0.973,0.974,0.978)); c.roundRect(x, y-h, w, h, 6, fill=1, stroke=0)
    setstroke(GOLD); c.setLineWidth(1); c.roundRect(x, y-h, w, h, 6, fill=0, stroke=1)
    setfill(NAVY); c.setFont("Lora-Bold", 11)
    c.drawString(x+14, y-18, title)
    row_y = y - 46
    bw, bh = 112, 30
    gap_arrow = 76
    total_w = bw*2 + gap_arrow
    start_x = x + (w - total_w)/2
    for pair, covered in [(top_pair, covered_top), (bot_pair, covered_bot)]:
        hand_org, hand_lbl, elem, col, yang_org, yang_lbl, direction = pair
        fill_col = col if covered else MUTED
        txt_col = (1,1,1) if covered else MUTED_TXT
        bx1 = start_x
        c.setFillColorRGB(*fill_col); c.roundRect(bx1, row_y-bh/2, bw, bh, 5, fill=1, stroke=0)
        c.setFillColorRGB(*txt_col); c.setFont("Lora-Bold", 10)
        c.drawCentredString(bx1+bw/2, row_y-2, hand_org)
        c.setFont("Lora-Italic", 6.8)
        c.drawCentredString(bx1+bw/2, row_y-12, hand_lbl)
        ax1, ax2 = bx1+bw+6, bx1+bw+gap_arrow-6
        setstroke(fill_col if covered else MUTED); c.setLineWidth(1.6)
        c.line(ax1, row_y+3, ax2-6, row_y+3)
        c.setFillColorRGB(*(fill_col if covered else MUTED))
        c.line(ax2-6, row_y+3, ax2-12, row_y+7); c.line(ax2-6, row_y+3, ax2-12, row_y-1)
        c.setFillColorRGB(*(col if covered else MUTED_TXT)); c.setFont("Lora-Bold", 7.6)
        c.drawCentredString((ax1+ax2)/2, row_y+10, elem)
        c.setFillColorRGB(*(GRAY if covered else MUTED_TXT)); c.setFont("Lora-Italic", 6.3)
        c.drawCentredString((ax1+ax2)/2, row_y-8, direction)
        bx2 = bx1 + bw + gap_arrow
        c.setFillColorRGB(*fill_col); c.roundRect(bx2, row_y-bh/2, bw, bh, 5, fill=1, stroke=0)
        c.setFillColorRGB(*txt_col); c.setFont("Lora-Bold", 10)
        c.drawCentredString(bx2+bw/2, row_y-2, yang_org)
        c.setFont("Lora-Italic", 6.8)
        c.drawCentredString(bx2+bw/2, row_y-12, yang_lbl)
        row_y -= 50

header("Six-Channel Nomenclature \u2014 The Three Circuits")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 17)
c.drawString(36, y, "TAIYIN, YANGMING, SHAOYIN, TAIYANG, JUEYIN, SHAOYANG"); y -= 11
setstroke(GOLD); c.setLineWidth(1.2); c.line(36, y, 280, y); y -= 12
setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawString(36, y, "The 3 circuits from Week 1, and where Weeks 1-4 sit inside the full 12-channel picture.")
y -= 22

y = callout(36, y, W-72, [
    "Dr. Zhang's slides use \u201cAnterior/Posterior/Middle Circuit\u201d as the primary names, but the Posterior Circuit has also been labeled \u201cInner Circuit\u201d on earlier slide versions \u2014 both terms may come up verbally or on the exam, so know both.",
], heading="Posterior Circuit = also called Inner Circuit", accent=GOLD, font_size=8.6, line_h=11)
y -= 12

box_h = 128
circuit_box(36, y, W-72, box_h,
    "ANTERIOR CIRCUIT  (Taiyin / Yangming)  \u2014 fully covered, Weeks 1-4",
    ("LU", "Hand Taiyin", "Metal", METAL, "LI", "Hand Yangming", "chest to hand / hand to face"),
    ("SP", "Foot Taiyin", "Earth", EARTH, "ST", "Foot Yangming", "foot to chest / face to foot"),
    True, True)
y -= box_h + 14

circuit_box(36, y, W-72, box_h,
    "POSTERIOR CIRCUIT  (Shaoyin / Taiyang)  \u2014 half covered: HT/SI now, BL/KI Week 5",
    ("HT", "Hand Shaoyin", "Fire", FIRE, "SI", "Hand Taiyang", "chest to hand / hand to face"),
    ("KI", "Foot Shaoyin", "Water", WATER, "BL", "Foot Taiyang", "foot to chest / face to foot"),
    True, False)
y -= box_h + 14

circuit_box(36, y, W-72, box_h,
    "MIDDLE CIRCUIT  (Jueyin / Shaoyang)  \u2014 not yet covered, Week 6",
    ("PC", "Hand Jueyin", "Min. Fire", MINFIRE, "SJ", "Hand Shaoyang", "chest to hand / hand to face"),
    ("LR", "Foot Jueyin", "Wood", WOOD, "GB", "Foot Shaoyang", "foot to chest / face to foot"),
    False, False)
y -= box_h + 16

setfill(NAVY); c.setFont("Lora-Bold", 12)
c.drawString(36, y, "WHAT EACH NAME MEANS"); y -= 8
setstroke(GOLD); c.line(36, y, 220, y); y -= 16
defs = [
    ("Taiyin", "Greater Yin", "Anterior", "LU / SP"),
    ("Yangming", "Yang Brightness", "Anterior", "LI / ST"),
    ("Shaoyin", "Lesser Yin", "Posterior", "HT / KI"),
    ("Taiyang", "Greater Yang", "Posterior", "SI / BL"),
    ("Jueyin", "Terminal / Reverting Yin", "Middle", "PC / LR"),
    ("Shaoyang", "Lesser Yang", "Middle", "SJ / GB"),
]
setfill(LIGHTBLUE); c.rect(36, y-15, W-72, 15, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 8.3)
xs2 = [42, 130, 280, 400]
for h_,x in zip(["Term","Literal meaning","Circuit","Hand/Foot organs"], xs2):
    c.drawString(x, y-11, h_)
y -= 15
c.setFont("Lora", 8.3)
for i,(term, meaning, circ, orgs) in enumerate(defs):
    if i%2==0:
        setfill((0.973,0.973,0.976)); c.rect(36,y-14,W-72,14,fill=1,stroke=0)
    setfill(RED); c.setFont("Lora-Bold", 8.3)
    c.drawString(42, y-10.5, term)
    setfill(DARK); c.setFont("Lora", 8.3)
    c.drawString(130, y-10.5, meaning)
    c.drawString(280, y-10.5, circ)
    c.drawString(400, y-10.5, orgs)
    y -= 14

footer("Page 3 of 8")
c.showPage()

# ============= PAGE 4: Special Point Category Legend =============
header("Special Point Category Legend + Worked Examples")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 17)
c.drawString(36, y, "SPECIAL POINT CATEGORIES"); y -= 11
setstroke(GOLD); c.setLineWidth(1.2); c.line(36, y, 280, y); y -= 14
setfill(GRAY); c.setFont("Lora-Italic", 10)
c.drawString(36, y, "What each category means, and where you've already seen it in Weeks 1-4.")
y -= 34

setfill(RED); c.setFont("Lora-BoldItalic", 9)
c.drawString(36, y, "The Five Shu Points \u2014 Jing-Well through He-Sea below \u2014 are their own named group per Dr. Zhang's slides.")
y -= 18

legend_rows = [
    ("Jing-Well", "\"Where it emerges\" \u2014 distal-most point (fingertip/toenail); channel's start/end; first aid, clears heat, relieves pain", "LU11, HT9, LI1, ST45, SP1, SI1"),
    ("Ying-Spring", "\"Where it flows\" \u2014 before the MCP/MTP joint; treats feverish diseases, heat-related disorders", "LU10, LI2, ST44, SP2, HT8, SI2"),
    ("Shu-Stream", "\"Where it pours\" \u2014 after the MCP/MTP joint; treats heaviness in the body, joint pain, pain syndromes", "LU9(Yuan), LI3, ST43, SP3(Yuan), HT7(Yuan), SI3(Confluent)"),
    ("Jing-River", "\"Where it travels\" \u2014 on the forearm/lower leg; treats externally contracted disease (colds, flu), cough, asthma", "LU8, LI5, ST41, SP5, HT4, SI5"),
    ("He-Sea", "\"Where it enters\" \u2014 near elbow/knee joints; where Qi enters deepest; treats organ-level / six Fu-organ disorders", "LU5, LI11, ST36, SP9, HT3, SI8"),
    ("Yuan-Source", "Reflects and regulates the organ's original Qi; primary diagnostic + treatment point for that organ", "LU9, LI4, ST42, SP3, HT7, SI4"),
    ("Luo-Connecting", "Links each paired Yin/Yang channel; treats symptoms of both channels in the pair", "LU7, LI6, ST40, SP4, HT5, SI7"),
    ("Xi-Cleft", "Accumulation point; treats acute pain, bleeding, or crisis flare of that channel", "LU6, LI7, ST34, SP8, HT6, SI6"),
    ("Front-Mu", "Diagnostic/treatment point on the chest or abdomen for the paired organ", "LU1, ST25(LI), CV12(ST), LR13(SP), CV14(HT), CV4(SI)"),
    ("Back-Shu", "Diagnostic/treatment point on the back for the paired organ", "BL13(LU), BL25(LI), BL21(ST), BL20(SP), BL15(HT), BL27(SI)"),
    ("Confluent", "Opens one of the 8 Extraordinary Vessels", "LU7(Ren Mai), SP4(Chong Mai), SI3(Du Mai)"),
    ("Command", "Broad regional treatment authority over a body area", "LU7(head/neck), LI4(face/mouth), ST36(abdomen)"),
]
setfill(LIGHTBLUE); c.rect(36, y-21, W-72, 21, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(44, y-15, "Category")
c.drawString(155, y-15, "What it means")
c.drawString(410, y-15, "Examples (Wk 1-4)")
y -= 21
for i,(cat, meaning, ex) in enumerate(legend_rows):
    m_lines = wrap_words(meaning, "Lora", 9.5, 410-155-10)
    e_lines = wrap_words(ex, "Lora", 9.2, W-36-410-6)
    n = max(len(m_lines), len(e_lines), 1)
    row_h = 17 + (n-1)*13
    if i%2==0:
        setfill((0.967,0.969,0.974)); c.rect(36, y-row_h, W-72, row_h, fill=1, stroke=0)
    setfill(RED); c.setFont("Lora-Bold", 10.2)
    c.drawString(44, y-14, cat)
    setfill(DARK); c.setFont("Lora", 9.5)
    ty = y-14
    for l in m_lines:
        c.drawString(155, ty, l); ty -= 13
    setfill(GRAY); c.setFont("Lora-Italic", 9.2)
    ty = y-14
    for l in e_lines:
        c.drawString(410, ty, l); ty -= 13
    y -= row_h
    setstroke(LIGHTGRAY); c.setLineWidth(0.5)
    c.line(36, y, W-36, y)

y -= 26
y = callout(36, y, W-72, [
    "Front-Mu and Back-Shu points are especially high-yield for the midterm since they cross-reference organs you haven't studied yet (e.g. SP's Front-Mu is LR13, LU/LI/ST/SP/HT/SI's Back-Shu points are all on BL) \u2014 know the pairing, not just the point code.",
], heading="Study tip", accent=GOLD, font_size=9.5, line_h=13)
y -= 10
callout(36, y, W-72, [
    "All 6 channels' Back-Shu points live on the Bladder channel in spinal order (BL13 LU, BL15 HT, BL18 LR, BL20 SP, BL21 ST, BL25 LI, BL27 SI) \u2014 you'll meet BL properly in Week 5, but recognizing this row now makes that channel far easier to learn.",
], heading="Looking ahead", accent=RED, font_size=9.5, line_h=13)

footer("Page 4 of 8")
c.showPage()

# ============= PAGE 5: Channel Pathways - Exterior vs Interior (NEW) =============
def pathway_diagram(x, y, w, h, title, color, waypoints, organs, note=None):
    """waypoints = list of (label, point_code) tuples along the exterior course.
       organs = (pertaining, connecting) organ names for the interior branch."""
    setfill((0.973,0.974,0.978)); c.roundRect(x, y-h, w, h, 6, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(1.3); c.roundRect(x, y-h, w, h, 6, fill=0, stroke=1)

    # --- precompute every y-position up front (top to bottom) ---
    bar_h = 18
    y_bar_bottom   = y - bar_h
    y_ext_label    = y_bar_bottom - 12
    y_ptcode       = y_ext_label - 16
    y_line         = y_ptcode - 14
    y_desc         = y_line - 15
    y_divider      = y_desc - 20
    y_int_label    = y_divider - 14
    org_w, org_h   = w - 60, 22
    y_box_top      = y_int_label - 16
    y_box_bottom   = y_box_top - org_h
    y_note         = y_box_bottom - 12
    center_x = x + w/2

    n = len(waypoints)
    margin_in = 18
    usable = w - 2*margin_in
    xs_pts = [x + margin_in + i*(usable/(n-1)) for i in range(n)]

    # --- background: the single continuous dashed interior-branch connector ---
    c.setDash(3, 2); setstroke(GRAY); c.setLineWidth(1.2)
    c.line(center_x, y_line - 7, center_x, y_box_top + 2)
    c.setDash()

    # --- title bar ---
    setfill(color); c.rect(x, y_bar_bottom, w, bar_h, fill=1, stroke=0)
    setfill((1,1,1)); c.setFont("Lora-Bold", 10)
    c.drawString(x+10, y-13, title)

    # --- exterior label ---
    setfill(GRAY); c.setFont("Lora-Bold", 7)
    c.drawCentredString(center_x, y_ext_label, "EXTERIOR COURSE (has points)")

    # --- point codes ---
    setfill(NAVY); c.setFont("Lora-Bold", 8.5)
    for i,(lbl, pt) in enumerate(waypoints):
        c.drawCentredString(xs_pts[i], y_ptcode, pt)

    # --- the line + circles + arrowhead ---
    setstroke(color); c.setLineWidth(2)
    c.line(xs_pts[0], y_line, xs_pts[-1], y_line)
    c.line(xs_pts[-1], y_line, xs_pts[-1]-7, y_line+4)
    c.line(xs_pts[-1], y_line, xs_pts[-1]-7, y_line-4)
    for px in xs_pts:
        c.setFillColorRGB(*color); c.circle(px, y_line, 4.5, fill=1, stroke=0)

    # --- waypoint descriptions ---
    setfill(GRAY); c.setFont("Lora-Italic", 6.8)
    for i,(lbl, pt) in enumerate(waypoints):
        c.drawCentredString(xs_pts[i], y_desc, lbl)

    # --- divider (drawn on top of the dashed line, leaving a visible gap either side) ---
    setfill((0.973,0.974,0.978))
    c.rect(center_x-10, y_divider-3, 20, 6, fill=1, stroke=0)
    setstroke((0.85,0.85,0.85)); c.setLineWidth(0.7)
    c.line(x+14, y_divider, center_x-10, y_divider)
    c.line(center_x+10, y_divider, x+w-14, y_divider)

    # --- interior branch label (drawn over the dashed line, with a clear background patch) ---
    setfill((0.973,0.974,0.978))
    label_w = pdfmetrics.stringWidth("INTERIOR branch (no points) connects to:", "Lora-Italic", 6.8)
    c.rect(center_x-label_w/2-4, y_int_label-2, label_w+8, 10, fill=1, stroke=0)
    setfill(GRAY); c.setFont("Lora-Italic", 6.8)
    c.drawCentredString(center_x, y_int_label, "INTERIOR branch (no points) connects to:")

    # --- organ box ---
    ox = x + (w - org_w)/2
    setfill((0.933,0.937,0.949)); c.roundRect(ox, y_box_bottom, org_w, org_h, 4, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 8)
    c.drawCentredString(center_x, y_box_bottom+9, f"Pertains: {organs[0]}   \u00b7   Connects: {organs[1]}")

    if note:
        setfill(RED); c.setFont("Lora-Italic", 6.8)
        c.drawCentredString(center_x, y_note, note)

header("Channel Pathways \u2014 Exterior Course vs. Interior Branch")
y = H - 62
setfill(NAVY); c.setFont("Lora-Bold", 15)
c.drawString(36, y, "WHERE THE POINTS ARE vs. WHERE THE CHANNEL JUST CONNECTS"); y -= 9
setstroke(GOLD); c.setLineWidth(1.2); c.line(36, y, 280, y); y -= 14
y = callout(36, y, W-72, [
    "Every channel has an EXTERIOR course (solid line) running along the limb/trunk/face where the acupuncture points actually sit, and an INTERIOR branch (dashed line) that dives into the body to reach the Zang-Fu organs \u2014 the interior branch has no points on it.",
], accent=GOLD, font_size=8.6, line_h=11)
y -= 8

diag_w = (W-72-16)/2
diag_h = 172
row1_y = y
pathway_diagram(36, row1_y, diag_w, diag_h, "LU \u2014 Lung (Metal)", METAL,
    [("underarm","LU1"),("elbow","LU5"),("wrist","LU9"),("thumb tip","LU11")],
    ("Lung","Large Intestine"))
pathway_diagram(36+diag_w+16, row1_y, diag_w, diag_h, "LI \u2014 Large Intestine (Metal)", METAL,
    [("index finger","LI1"),("elbow","LI11"),("shoulder","LI15"),("nose","LI20")],
    ("Large Intestine","Lung"))
row2_y = row1_y - diag_h - 14
pathway_diagram(36, row2_y, diag_w, diag_h, "ST \u2014 Stomach (Earth)", EARTH,
    [("face","ST1"),("clavicle","ST12"),("umbilicus","ST25"),("toe","ST45")],
    ("Stomach","Spleen"), note="Also: lower orifice -> diaphragm -> Spleen")
pathway_diagram(36+diag_w+16, row2_y, diag_w, diag_h, "SP \u2014 Spleen (Earth)", EARTH,
    [("big toe","SP1"),("ankle","SP6"),("thigh","SP10"),("chest","SP21")],
    ("Spleen","Stomach"), note="Branch: stomach -> diaphragm -> Heart")
row3_y = row2_y - diag_h - 14
pathway_diagram(36, row3_y, diag_w, diag_h, "HT \u2014 Heart (Fire)", FIRE,
    [("axilla","HT1"),("elbow","HT3"),("wrist","HT7"),("pinky tip","HT9")],
    ("Heart","Small Intestine"), note="Branch: heart system -> eye system")
pathway_diagram(36+diag_w+16, row3_y, diag_w, diag_h, "SI \u2014 Small Intestine (Fire)", FIRE,
    [("pinky finger","SI1"),("elbow","SI8"),("scapula","SI11"),("ear","SI19")],
    ("Small Intestine","Heart"))

footer("Page 5 of 8")
c.showPage()

# ============= PAGES 4-6: Channel tables + pearls =============
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
        "HT8: Ying-Spring; clears heart fire; oral ulcers, urinary urgency",
        "HT1: first point of the channel; used for stroke",
        "HT9: Jing-Well; emergency point for severe heart pain, difficulty breathing, palpitations"],
 "SI": ["SI3: confluent (Du Mai); neck/spine disorders; opens governing vessel",
        "SI11: most important local point for frozen shoulder",
        "SI19: local point for tinnitus and deafness",
        "SI4: Yuan-source; wrist and finger pain; febrile diseases"],
}

def channel_section(x, w, ab, full, subtitle, rows, accent, y):
    y = channel_bar(x, y, w, accent, f"{ab} \u2014 {full}", subtitle)
    y = special_table(x, w, rows, y) - 8
    y = callout(x, y+8, w, pearls_data[ab], heading="Clinical Pearls", accent=accent, font_size=8.0, line_h=10.2)
    return y - 4

lu = [("Jing-Well","LU11",""),("Ying-Spring","LU10",""),("Shu-Stream","LU9","also Yuan-Source"),
      ("Jing-River","LU8",""),("He-Sea","LU5","clears heat, descends Qi"),("Luo","LU7","also Confluent + Command"),
      ("Xi-Cleft","LU6",""),("Front-Mu","LU1","chest fullness, grief"),("Back-Shu","BL13",""),
      ("Confluent","LU7","opens Ren Mai"),("Command","LU7","head/neck")]
li = [("Jing-Well","LI1",""),("Ying-Spring","LI2",""),("Shu-Stream","LI3",""),("Jing-River","LI5",""),
      ("He-Sea","LI11","clears heat in blood"),("Yuan-Source","LI4","FORBIDDEN in pregnancy"),
      ("Luo","LI6",""),("Xi-Cleft","LI7",""),("Front-Mu","ST25","of Large Intestine"),
      ("Back-Shu","BL25",""),("Command","LI4","face/mouth")]
st = [("Jing-Well","ST45",""),("Ying-Spring","ST44","clears Yangming heat"),("Shu-Stream","ST43",""),
      ("Jing-River","ST41",""),("He-Sea","ST36","command abdomen, most important tonic pt"),
      ("Yuan-Source","ST42",""),("Luo","ST40","resolves phlegm-dampness anywhere"),("Xi-Cleft","ST34",""),
      ("Front-Mu","CV12",""),("Back-Shu","BL21",""),("Command","ST36","abdomen"),("Lower He-Sea","ST37","of Large Intestine")]
sp = [("Jing-Well","SP1",""),("Ying-Spring","SP2",""),("Shu-Stream","SP3","also Yuan-Source"),
      ("Jing-River","SP5",""),("He-Sea","SP9","resolves dampness"),("Luo","SP4","also Confluent (Chong Mai)"),
      ("Xi-Cleft","SP8",""),("Front-Mu","LR13",""),("Back-Shu","BL20",""),
      ("Confluent","SP4","opens Chong Mai"),("Sea of Blood","SP10","cools blood, skin/menstrual")]
ht = [("Jing-Well","HT9","emergency: severe heart pain, palpitations"),("Ying-Spring","HT8","clears heart fire"),("Shu-Stream","HT7","also Yuan-Source"),
      ("Jing-River","HT4",""),("He-Sea","HT3","clears heart fire, fear/arm pain"),("Luo","HT5",""),
      ("Xi-Cleft","HT6","night sweats, acute heart pain"),("Front-Mu","CV14",""),("Back-Shu","BL15","")]
si = [("Jing-Well","SI1",""),("Ying-Spring","SI2",""),("Shu-Stream","SI3","also Confluent"),
      ("Jing-River","SI5",""),("He-Sea","SI8",""),("Yuan-Source","SI4","wrist/finger pain, febrile disease"),
      ("Luo","SI7",""),("Xi-Cleft","SI6",""),("Front-Mu","CV4",""),("Back-Shu","BL27",""),
      ("Confluent","SI3","opens Du Mai")]

# Page 4: LU + LI (Metal)
header("Special Points \u2014 LU / LI  (Metal)")
y = H - 62
y = channel_section(36, W-72, "LU", "Lung", "Hand Taiyin \u00b7 Yin \u00b7 Metal \u00b7 Peak 3-5AM \u00b7 Paired: LI \u00b7 11 pts", lu, METAL, y)
y = channel_section(36, W-72, "LI", "Large Intestine", "Hand Yangming \u00b7 Yang \u00b7 Metal \u00b7 Peak 5-7AM \u00b7 Paired: LU \u00b7 20 pts", li, METAL, y)
footer("Page 6 of 8")
c.showPage()

# Page 5: ST + SP (Earth)
header("Special Points \u2014 ST / SP  (Earth)")
y = H - 62
y = channel_section(36, W-72, "ST", "Stomach", "Foot Yangming \u00b7 Yang \u00b7 Earth \u00b7 Peak 7-9AM \u00b7 Paired: SP \u00b7 45 pts", st, EARTH, y)
y = channel_section(36, W-72, "SP", "Spleen", "Foot Taiyin \u00b7 Yin \u00b7 Earth \u00b7 Peak 9-11AM \u00b7 Paired: ST \u00b7 21 pts", sp, EARTH, y)
setfill(RED); c.setFont("Lora-Bold", 9)
c.drawString(36, y-2, "\u26a0  FORBIDDEN IN PREGNANCY (Wk 1-4): LI4, SP6")
footer("Page 7 of 8")
c.showPage()

# Page 6: HT + SI (Fire) + recall
header("Special Points \u2014 HT / SI  (Fire) + High-Yield Recall")
y = H - 62
y = channel_section(36, W-72, "HT", "Heart", "Hand Shaoyin \u00b7 Yin \u00b7 Fire \u00b7 Peak 11AM-1PM \u00b7 Paired: SI \u00b7 9 pts", ht, FIRE, y)
y = channel_section(36, W-72, "SI", "Small Intestine", "Hand Taiyang \u00b7 Yang \u00b7 Fire \u00b7 Peak 1-3PM \u00b7 Paired: HT \u00b7 19 pts", si, FIRE, y)

setfill(NAVY); c.setFont("Lora-Bold", 11)
c.drawString(36, y, "COMMONLY CONFUSED / HIGH-YIELD PAIRS"); y -= 6
setstroke(GOLD); c.line(36, y, 220, y); y -= 14
pairs = [
    "LU7 vs LI4 \u2014 both treat face/head; LU7 = command head/neck + opens Ren Mai; LI4 = command face/mouth, FORBIDDEN in pregnancy",
    "ST36 vs SP6 \u2014 both abdominal; ST36 = command abdomen, tonifies Qi/Blood; SP6 = 3-Yin crossing, FORBIDDEN in pregnancy",
    "SI3 vs LI4 \u2014 both treat head/neck; SI3 = confluent opens Du Mai (spine); LI4 = command face/mouth",
]
y = callout(36, y+10, W-72, pairs, accent=RED, font_size=8.2, line_h=10.5)

footer("Page 8 of 8")
c.showPage()

c.save()
print("SAVED:", OUT)
