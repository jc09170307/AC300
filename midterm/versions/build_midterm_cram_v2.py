#!/usr/bin/env python3
"""AC300 Midterm Cram Sheet (Weeks 1-4 cumulative) - Print edition v2, prettier"""
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
FIRE  = (0.690, 0.204, 0.169)   # deep red

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

def callout(x, y, w, lines, heading=None, accent=GOLD, font_size=8.3, line_h=11):
    """Cream callout box with gold left bar, returns new y below box"""
    pad = 8
    n_lines = sum(len(wrap_words(l, "Lora", font_size, w-pad*2-6)) for l in lines)
    h = pad*2 + (14 if heading else 0) + n_lines*line_h
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
for i,(label, txt) in enumerate(rules):
    x = 36 + (i%2)*(col_w+16)
    if i%2==0: row_y = y
    lines = wrap_words(txt, "Lora", 8.2, col_w-16)
    y2 = callout(x, row_y, col_w, [txt], heading=label, accent=GOLD, font_size=8.2, line_h=10.5)
    if i%2==1: y = min(y, y2)
y -= 6

setfill(NAVY); c.setFont("Lora-Bold", 14)
c.drawString(36, y, "CIRCADIAN CLOCK \u2014 WEEKS 1-4 CHANNELS"); y -= 8
setstroke(GOLD); c.line(36, y, 220, y); y -= 20

clock = [("LU","3-5 AM",METAL),("LI","5-7 AM",METAL),("ST","7-9 AM",EARTH),
         ("SP","9-11 AM",EARTH),("HT","11 AM-1 PM",FIRE),("SI","1-3 PM",FIRE)]
col_w2 = (W-72)/6
setfill(NAVY); c.rect(36, y-42, W-72, 4, fill=1, stroke=0)
for i,(ch,tm,col) in enumerate(clock):
    x = 36 + i*col_w2 + col_w2/2
    c.setFillColorRGB(*col); c.circle(x, y-24, 17, fill=1, stroke=0)
    setfill((1,1,1)); c.setFont("Lora-Bold", 12)
    c.drawCentredString(x, y-29, ch)
    setfill(DARK); c.setFont("Lora", 8)
    c.drawCentredString(x, y-58, tm)
    if i < 5:
        setstroke(GOLD); c.setLineWidth(1.2)
        c.line(x+20, y-24, x+col_w2-20, y-24)
y -= 78
callout(36, y+12, W-72, ["Paired organs sit in adjacent clock slots (LU/LI, ST/SP, HT/SI) \u2014 this continues the Qi circulation chain from one channel straight into the next."], accent=GOLD, font_size=8.3)
y -= 42

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
    setfill(DARK)
    for val,x in zip(row,xs):
        c.drawString(x, y-11, val)
    y -= 15
footer("Page 2 of 5")
c.showPage()

# ============= PAGES 3-5: Channel tables + pearls =============
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
      ("Front-Mu","CV12",""),("Back-Shu","BL21",""),("Command","ST36","abdomen"),("Lower He-Sea","ST37","")]
sp = [("Jing-Well","SP1",""),("Ying-Spring","SP2",""),("Shu-Stream","SP3","also Yuan-Source"),
      ("Jing-River","SP5",""),("He-Sea","SP9","resolves dampness"),("Luo","SP4","also Confluent (Chong Mai)"),
      ("Xi-Cleft","SP8",""),("Front-Mu","LR13",""),("Back-Shu","BL20",""),
      ("Confluent","SP4","opens Chong Mai"),("Sea of Blood","SP10","cools blood, skin/menstrual")]
ht = [("Jing-Well","HT9",""),("Ying-Spring","HT8","clears heart fire"),("Shu-Stream","HT7","also Yuan-Source"),
      ("Jing-River","HT4",""),("He-Sea","HT3","clears heart fire, fear/arm pain"),("Luo","HT5",""),
      ("Xi-Cleft","HT6","night sweats, acute heart pain"),("Front-Mu","CV14",""),("Back-Shu","BL15","")]
si = [("Jing-Well","SI1",""),("Ying-Spring","SI2",""),("Shu-Stream","SI3","also Confluent"),
      ("Jing-River","SI5",""),("He-Sea","SI8",""),("Yuan-Source","SI4","wrist/finger pain, febrile disease"),
      ("Luo","SI7",""),("Xi-Cleft","SI6",""),("Front-Mu","CV4",""),("Back-Shu","BL27",""),
      ("Confluent","SI3","opens Du Mai")]

# Page 3: LU + LI (Metal)
header("Special Points \u2014 LU / LI  (Metal)")
y = H - 62
y = channel_section(36, W-72, "LU", "Lung", "Hand Taiyin \u00b7 Yin \u00b7 Metal \u00b7 Peak 3-5AM \u00b7 Paired: LI \u00b7 11 pts", lu, METAL, y)
y = channel_section(36, W-72, "LI", "Large Intestine", "Hand Yangming \u00b7 Yang \u00b7 Metal \u00b7 Peak 5-7AM \u00b7 Paired: LU \u00b7 20 pts", li, METAL, y)
footer("Page 3 of 5")
c.showPage()

# Page 4: ST + SP (Earth)
header("Special Points \u2014 ST / SP  (Earth)")
y = H - 62
y = channel_section(36, W-72, "ST", "Stomach", "Foot Yangming \u00b7 Yang \u00b7 Earth \u00b7 Peak 7-9AM \u00b7 Paired: SP \u00b7 45 pts", st, EARTH, y)
y = channel_section(36, W-72, "SP", "Spleen", "Foot Taiyin \u00b7 Yin \u00b7 Earth \u00b7 Peak 9-11AM \u00b7 Paired: ST \u00b7 21 pts", sp, EARTH, y)
setfill(RED); c.setFont("Lora-Bold", 9)
c.drawString(36, y-2, "\u26a0  FORBIDDEN IN PREGNANCY (Wk 1-4): LI4, SP6")
footer("Page 4 of 5")
c.showPage()

# Page 5: HT + SI (Fire) + recall
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

setfill(NAVY); c.setFont("Lora-Bold", 11)
c.drawString(36, y-4, "SPECIAL POINT CATEGORY LEGEND"); y -= 10
setstroke(GOLD); c.line(36, y-4, 220, y-4); y -= 18
legend = [
    "Jing-Well: distal-most point, channel start/end; treats acute/mental disturbance",
    "Yuan-Source: reflects/regulates original Qi; primary diagnostic + treatment point",
    "Luo-Connecting: links paired Yin/Yang channels; treats both channels' symptoms",
    "Xi-Cleft: accumulation point; treats acute pain/bleeding of that channel",
    "He-Sea: Qi enters deepest; treats organ-level/internal disorders",
    "Front-Mu / Back-Shu: diagnostic/treatment points on chest/back for the organ",
    "Confluent: opens one of the 8 Extraordinary Vessels",
    "Command: broad regional treatment authority (face, head/neck, abdomen, back)",
]
half = len(legend)//2
callout(36, y, (W-72-16)/2, legend[:half], accent=GOLD, font_size=7.8, line_h=10)
callout(36+(W-72-16)/2+16, y, (W-72-16)/2, legend[half:], accent=GOLD, font_size=7.8, line_h=10)

footer("Page 5 of 5")
c.showPage()
c.save()
print("SAVED:", OUT)
