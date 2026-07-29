#!/usr/bin/env python3
"""AC300 Midterm Cram Sheet (Weeks 1-4 cumulative) - Print edition"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)      # #1d3a5e
GOLD = (0.616, 0.478, 0.216)      # #9c7a37 (darkened from #c8933a for contrast)
RED = (0.627, 0.220, 0.180)       # #a0382e (darkened from #c0392b)
LIGHTBLUE = (0.929, 0.949, 0.965) # #edf2f6
CREAM = (0.961, 0.941, 0.918)     # #f5f0ea
DARK = (0.15, 0.15, 0.15)
GRAY = (0.35, 0.35, 0.35)

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

def header(title, subtitle):
    setfill(NAVY)
    c.rect(0, H-40, W, 40, fill=1, stroke=0)
    setfill((1,1,1))
    c.setFont("Lora-Bold", 11)
    c.drawString(36, H-27, title)
    c.setFont("Lora-Italic", 9)
    c.drawRightString(W-36, H-27, subtitle)

def footer(page_label):
    setfill(GRAY)
    c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W/2, 24, f"AC300/AC375 Midterm Cram Sheet (Wk 1-4) - VUIM Summer 2026 - {page_label}")

# ---------------- COVER ----------------
c.setFillColorRGB(1,1,1); c.rect(0,0,W,H,fill=1,stroke=0)
setfill(NAVY)
c.rect(0, H-80, W, 80, fill=1, stroke=0)
setfill((1,1,1))
c.setFont("Lora-Bold", 10.5)
c.drawCentredString(W/2, H-45, "AC300/AC375 - Acupuncture Channels & Points I | VUIM Summer 2026")

# badge
bx, by, bs = W/2-34, H-165, 68
setfill((0.929,0.949,0.965))
c.rect(bx, by, bs, bs, fill=1, stroke=0)
setfill(GOLD)
c.rect(bx, by+bs-8, bs, 8, fill=1, stroke=0)
setfill(NAVY)
c.setFont("Lora-Bold", 7)
c.drawCentredString(W/2, by+bs-22, "MIDTERM")
c.setFont("Lora-Bold", 20)
c.drawCentredString(W/2, by+18, "1-4")

c.setFont("Lora-Bold", 28)
setfill(NAVY)
c.drawCentredString(W/2, H-225, "MIDTERM CRAM SHEET")
c.setFont("Lora-BoldItalic", 13)
setfill(RED)
c.drawCentredString(W/2, H-248, "Channel Theory + LU - LI - ST - SP - HT - SI")
c.setFont("Lora", 10.5)
setfill(DARK)
c.drawCentredString(W/2, H-266, "155 points cumulative  -  Weeks 1-4  -  Midterm covers this material")

setstroke(GOLD); c.setLineWidth(2)
c.line(W/2-120, H-282, W/2+120, H-282)

# three boxes
box_w, box_h, gap = 150, 62, 15
total = box_w*3 + gap*2
bx0 = (W-total)/2
by0 = H-370
labels = [("CHANNELS", "6 channels, 155 pts", "Circadian clock order", (0.157,0.302,0.541)),
          ("SPECIAL PTS", "Yuan/Luo/Xi-Cleft", "Front-Mu/Back-Shu/He-Sea", (0.380,0.180,0.522)),
          ("HIGH-YIELD", "Forbidden pregnancy", "Commonly confused pairs", (0.106,0.369,0.353))]
for i,(t,l1,l2,col) in enumerate(labels):
    x = bx0 + i*(box_w+gap)
    setfill((0.933,0.937,0.949))
    c.rect(x, by0, box_w, box_h, fill=1, stroke=0)
    c.setFillColorRGB(*col)
    c.setFont("Lora-Bold", 10)
    c.drawCentredString(x+box_w/2, by0+box_h-18, t)
    c.setFont("Lora-Italic", 8)
    c.setFillColorRGB(*DARK)
    c.drawCentredString(x+box_w/2, by0+box_h-33, l1)
    c.drawCentredString(x+box_w/2, by0+box_h-46, l2)

setfill(GRAY)
c.setFont("Lora-Italic", 8)
c.drawCentredString(W/2, by0-30, "+ circadian clock, confluent/command points, ACQ/MAINT quiz-ready recall")

setstroke(GOLD); c.setLineWidth(1)
c.line(50, 70, W-50, 70)
c.setFont("Lora-Italic", 8.5)
setfill(GRAY)
c.drawCentredString(W/2, 50, "Jonathan Centeno - D.AcHM Candidate - Sourced from Dr. Zhang's lectures, CAM 4th Ed., MOA (Deadman 3rd)")
c.showPage()

# ---------------- PAGE 2: Channel Theory + Circadian Clock ----------------
header("MIDTERM CRAM SHEET", "Channel Theory + Circadian Clock")
y = H - 65
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(36, y, "CHANNEL THEORY - CORE RULES"); y -= 20

rules = [
    ("Nomenclature (3 parts)", "Hand/Foot (location) + Yin/Yang (medial/lateral, nature) + Zang/Fu (pertaining organ, function)"),
    ("Qi circulation direction", "Hand Yin: chest -> hand  |  Hand Yang: hand -> head  |  Foot Yang: head -> foot  |  Foot Yin: foot -> abdomen/chest"),
    ("Hand Yin / Hand Yang meet", "At the fingers (e.g. LU7->LI1 branch meets at index finger)"),
    ("12 Primary Meridians", "3 Hand Yin + 3 Hand Yang + 3 Foot Yin + 3 Foot Yang = 12. Plus 8 Extraordinary Vessels, 15 Luo-connecting, divergent + sinew + cutaneous."),
    ("Zang-Fu pairing logic", "Each Yin (zang) channel pairs with one Yang (fu) channel; paired channels treat each other's organ symptoms (e.g. LU constipation -> use LI points)."),
    ("Hand Yang distribution", "Anterior = Yangming, Middle = Shaoyang, Posterior = Taiyang (also applies conceptually to Foot Yang)."),
]
for label, txt in rules:
    setfill(RED); c.setFont("Lora-Bold", 9.5)
    c.drawString(36, y, label + ":")
    y -= 12
    setfill(DARK); c.setFont("Lora", 9)
    for line in wrap_words(txt, "Lora", 9, W-90):
        c.drawString(46, y, line); y -= 11
    y -= 5

y -= 6
setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(36, y, "CIRCADIAN CLOCK - WEEKS 1-4 CHANNELS"); y -= 18
clock = [("LU","3-5 AM"),("LI","5-7 AM"),("ST","7-9 AM"),("SP","9-11 AM"),("HT","11 AM-1 PM"),("SI","1-3 PM")]
col_w = (W-72)/6
setfill(LIGHTBLUE); c.rect(36, y-38, W-72, 34, fill=1, stroke=0)
for i,(ch,tm) in enumerate(clock):
    x = 36 + i*col_w + col_w/2
    setfill(NAVY); c.setFont("Lora-Bold", 12)
    c.drawCentredString(x, y-16, ch)
    setfill(DARK); c.setFont("Lora", 8)
    c.drawCentredString(x, y-30, tm)
y -= 55
setfill(GRAY); c.setFont("Lora-Italic", 8)
c.drawString(36, y, "Remember: paired organs sit in adjacent clock slots (LU/LI, ST/SP, HT/SI) - continues the Qi circulation chain.")
y -= 25

setfill(NAVY); c.setFont("Lora-Bold", 13)
c.drawString(36, y, "6 CHANNELS AT A GLANCE"); y -= 18
setfill(LIGHTBLUE); c.rect(36, y-16, W-72, 16, fill=1, stroke=0)
setfill(NAVY); c.setFont("Lora-Bold", 8.5)
heads = ["Ch","Full name","Type","Element","Pts","Paired","Front-Mu","Back-Shu"]
xs = [40, 65, 175, 220, 275, 305, 350, 420]
for h,x in zip(heads,xs): c.drawString(x, y-12, h)
y -= 16
rows = [
    ("LU","Hand Taiyin","Yin","Metal","11","LI","LU1","BL13"),
    ("LI","Hand Yangming","Yang","Metal","20","LU","ST25","BL25"),
    ("ST","Foot Yangming","Yang","Earth","45","SP","CV12","BL21"),
    ("SP","Foot Taiyin","Yin","Earth","21","ST","LR13","BL20"),
    ("HT","Hand Shaoyin","Yin","Fire","9","SI","CV14","BL15"),
    ("SI","Hand Taiyang","Yang","Fire","19","HT","CV4","BL27"),
]
c.setFont("Lora", 8.5)
for i,row in enumerate(rows):
    if i%2==0:
        setfill((0.973,0.973,0.976)); c.rect(36,y-14,W-72,14,fill=1,stroke=0)
    setfill(DARK)
    for val,x in zip(row,xs):
        c.drawString(x, y-11, val)
    y -= 14
footer("Page 2 of 5")
c.showPage()
print("Page 2 done, y ended at", y)

# ---------------- PAGE 3: LU/LI + ST/SP Special Points ----------------
header("MIDTERM CRAM SHEET", "Special Points - LU / LI / ST / SP")
y = H - 65

def special_table(title, subtitle, rows, y, color):
    c.setFillColorRGB(*color); c.setFont("Lora-Bold", 12)
    c.drawString(36, y, title)
    c.setFillColorRGB(*GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawString(36, y-13, subtitle)
    y -= 28
    setfill(LIGHTBLUE); c.rect(36, y-14, W-72, 14, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 8)
    c.drawString(40, y-11, "Category")
    c.drawString(180, y-11, "Point")
    c.drawString(240, y-11, "Notes")
    y -= 14
    c.setFont("Lora", 8.3)
    for i,(cat,pt,note) in enumerate(rows):
        if i%2==0:
            setfill((0.973,0.973,0.976)); c.rect(36,y-13,W-72,13,fill=1,stroke=0)
        setfill(DARK)
        c.drawString(40, y-10, cat)
        setfill(RED); c.setFont("Lora-Bold", 8.3)
        c.drawString(180, y-10, pt)
        setfill(DARK); c.setFont("Lora", 8.3)
        c.drawString(240, y-10, note)
        y -= 13
    return y - 10

lu = [("Jing-Well","LU11",""),("Ying-Spring","LU10",""),("Shu-Stream","LU9","also Yuan-Source"),
      ("Jing-River","LU8",""),("He-Sea","LU5","clears heat, descends Qi"),("Luo","LU7","also Confluent + Command"),
      ("Xi-Cleft","LU6",""),("Front-Mu","LU1","chest fullness, grief"),("Back-Shu","BL13",""),
      ("Confluent","LU7","opens Ren Mai"),("Command","LU7","head/neck")]
y = special_table("LU - Lung (11 pts)", "Hand Taiyin - Yin - Metal - Peak 3-5AM - Paired: LI", lu, y, NAVY)

li = [("Jing-Well","LI1",""),("Ying-Spring","LI2",""),("Shu-Stream","LI3",""),("Jing-River","LI5",""),
      ("He-Sea","LI11","clears heat in blood"),("Yuan-Source","LI4","FORBIDDEN in pregnancy"),
      ("Luo","LI6",""),("Xi-Cleft","LI7",""),("Front-Mu","ST25","of Large Intestine"),
      ("Back-Shu","BL25",""),("Command","LI4","face/mouth")]
y = special_table("LI - Large Intestine (20 pts)", "Hand Yangming - Yang - Metal - Peak 5-7AM - Paired: LU", li, y, NAVY)
footer("Page 3 of 5")
c.showPage()

# ---------------- PAGE 4: ST / SP ----------------
header("MIDTERM CRAM SHEET", "Special Points - ST / SP")
y = H - 65
st = [("Jing-Well","ST45",""),("Ying-Spring","ST44","clears Yangming heat"),("Shu-Stream","ST43",""),
      ("Jing-River","ST41",""),("He-Sea","ST36","command abdomen, most important tonic pt"),
      ("Yuan-Source","ST42",""),("Luo","ST40","resolves phlegm-dampness anywhere"),("Xi-Cleft","ST34",""),
      ("Front-Mu","CV12",""),("Back-Shu","BL21",""),("Command","ST36","abdomen"),("Lower He-Sea","ST37","")]
y = special_table("ST - Stomach (45 pts)", "Foot Yangming - Yang - Earth - Peak 7-9AM - Paired: SP", st, y, NAVY)

sp = [("Jing-Well","SP1",""),("Ying-Spring","SP2",""),("Shu-Stream","SP3","also Yuan-Source"),
      ("Jing-River","SP5",""),("He-Sea","SP9","resolves dampness"),("Luo","SP4","also Confluent (Chong Mai)"),
      ("Xi-Cleft","SP8",""),("Front-Mu","LR13",""),("Back-Shu","BL20",""),
      ("Confluent","SP4","opens Chong Mai"),("Sea of Blood","SP10","cools blood, skin/menstrual")]
y = special_table("SP - Spleen (21 pts)", "Foot Taiyin - Yin - Earth - Peak 9-11AM - Paired: ST", sp, y, NAVY)

setfill(RED); c.setFont("Lora-Bold", 9)
c.drawString(36, y-6, "FORBIDDEN IN PREGNANCY (Wk 1-4): LI4, SP6")
footer("Page 4 of 5")
c.showPage()

# ---------------- PAGE 5: HT / SI + Commonly Confused + Legend ----------------
header("MIDTERM CRAM SHEET", "Special Points - HT / SI + High-Yield Recall")
y = H - 65
ht = [("Jing-Well","HT9",""),("Ying-Spring","HT8","clears heart fire"),("Shu-Stream","HT7","also Yuan-Source"),
      ("Jing-River","HT4",""),("He-Sea","HT3","clears heart fire, fear/arm pain"),("Luo","HT5",""),
      ("Xi-Cleft","HT6","night sweats, acute heart pain"),("Front-Mu","CV14",""),("Back-Shu","BL15","")]
y = special_table("HT - Heart (9 pts)", "Hand Shaoyin - Yin - Fire - Peak 11AM-1PM - Paired: SI", ht, y, NAVY)

si = [("Jing-Well","SI1",""),("Ying-Spring","SI2",""),("Shu-Stream","SI3","also Confluent"),
      ("Jing-River","SI5",""),("He-Sea","SI8",""),("Yuan-Source","SI4","wrist/finger pain, febrile disease"),
      ("Luo","SI7",""),("Xi-Cleft","SI6",""),("Front-Mu","CV4",""),("Back-Shu","BL27",""),
      ("Confluent","SI3","opens Du Mai")]
y = special_table("SI - Small Intestine (19 pts)", "Hand Taiyang - Yang - Fire - Peak 1-3PM - Paired: HT", si, y, NAVY)

y -= 4
setfill(NAVY); c.setFont("Lora-Bold", 11)
c.drawString(36, y, "COMMONLY CONFUSED / HIGH-YIELD PAIRS"); y -= 15
pairs = [
    "LU7 vs LI4 - both treat face/head; LU7 = command head/neck + opens Ren Mai; LI4 = command face/mouth, FORBIDDEN in pregnancy",
    "ST36 vs SP6 - both abdominal; ST36 = command abdomen, tonifies Qi/Blood; SP6 = 3-Yin crossing, FORBIDDEN in pregnancy, gynecology",
    "SI3 vs LI4 - both hand points treating head/neck; SI3 = confluent opens Du Mai (spine); LI4 = command face/mouth",
    "LU9 vs LI4 vs SP3 vs HT7 vs SI4 - all Yuan-Source points of their channel; each also has a distinct secondary role (see tables above)",
]
setfill(DARK); c.setFont("Lora", 8.3)
for p in pairs:
    for line in wrap_words(p, "Lora", 8.3, W-90):
        c.drawString(40, y, line); y -= 10.5
    y -= 3

y -= 6
setfill(NAVY); c.setFont("Lora-Bold", 11)
c.drawString(36, y, "SPECIAL POINT CATEGORY LEGEND"); y -= 15
legend = [
    "Jing-Well: distal-most pt, each channel's start/end; treats acute/mental disturbance",
    "Yuan-Source: reflects/regulates the organ's original Qi; primary diagnostic + treatment pt",
    "Luo-Connecting: links paired Yin/Yang channels; treats both channels' symptoms",
    "Xi-Cleft: accumulation pt; treats acute pain/bleeding of that channel",
    "He-Sea: where Qi enters deepest; treats organ-level/internal disorders",
    "Front-Mu / Back-Shu: diagnostic/treatment pts on chest/back for the paired organ",
    "Confluent: opens one of the 8 Extraordinary Vessels",
    "Command: broad regional treatment authority (face, head/neck, abdomen, back)",
]
c.setFont("Lora", 8.3)
for l in legend:
    setfill(DARK)
    for line in wrap_words(l, "Lora", 8.3, W-90):
        c.drawString(40, y, line); y -= 10.5
    y -= 2

footer("Page 5 of 5")
c.showPage()
c.save()
print("SAVED:", OUT)
