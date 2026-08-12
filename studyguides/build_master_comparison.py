#!/usr/bin/env python3
"""AC300 Master Channel Comparison -- Through Week 6 (all 12 primary channels
now covered). Extends the established Wk1-5 pattern with PC/SJ/GB/LR columns,
completes the Middle Circuit, and finalizes the 4 confluent points that were
placeholder rows in the Week 5 version. Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = "/home/claude/work/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.176, 0.271, 0.412)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.12, 0.12, 0.12)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.945, 0.937, 0.906)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_MasterComparison_ThruWeek6_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_MasterComparison_ThruWeek6_Print.pdf"
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


ML, MR = 42, 42
RX = W - MR
CW = RX - ML
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def top_bar():
    setfill(DARK); c.setFont("Lora", 8.5)
    c.drawString(ML, H - 30.3, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(RX, H - 30.3, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6 * LW_MULT)
    c.line(ML, H - 38, RX, H - 38)


def bottom_bar(label):
    setfill(NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora", 8)
    c.drawString(ML, 10, label)
    c.drawRightString(RX, 10, f"p.{page_num[0]}")


def new_page():
    page_bg(); top_bar()


def end_page(label):
    bottom_bar(label); c.showPage(); page_num[0] += 1


WEEK_LABEL = "AC300/AC375 | Master Comparison | Weeks 1-6 (12 Channels) | VUIM Summer 2026"


def section_bar(y, title, color=NAVY, size=11.5):
    bar_h = 20
    setfill(color); c.rect(ML, y - bar_h, CW, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", size)
    c.drawString(ML + 8, y - bar_h + 6, title)
    return y - bar_h - 8


# ============================================================
# COVER
# ============================================================
new_page()
y = H - 60
setfill(NAVY); c.setFont("Lora-Bold", 26)
c.drawCentredString(W / 2, y, "Master Channel Comparison")
y -= 26
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-BoldItalic", 15)
c.drawCentredString(W / 2, y, "All 12 Primary Channels -- Through Week 6 (COMPLETE)")
y -= 20
setfill(DARK); c.setFont("Lora", 11)
c.drawCentredString(W / 2, y, "LU+LI+ST+SP+HT+SI+BL+KI+PC+SJ+GB+LR  =  361 points")
y -= 18
setstroke(GOLD); c.setLineWidth(1.2)
c.line(ML + 40, y, RX - 40, y)
y -= 26
setfill(DARK); c.setFont("Lora", 10)
for l in wrap_words("This is a CUMULATIVE reference -- it grows every week. Use it to keep the whole map straight once individual weekly Study Guides start blurring together. As of Week 6, all three circuits and all 12 primary channels are complete.", "Lora", 10, CW - 10):
    c.drawString(ML, y, l); y -= 13
y -= 8

y = section_bar(y, "This Document Covers")
setfill(DARK); c.setFont("Lora", 9.5)
bullets = [
    "Full attribute table -- all 12 channels, side by side (element, peak, points, special points)",
    "Anterior (LU-LI-ST-SP), Posterior/Inner (HT-SI-BL-KI), and Middle (PC-SJ-GB-LR) circuit maps -- all 3 now complete",
    "Cross-week trap notes -- recurring connection/circuit errors across all 12 channels",
    "Forbidden-in-pregnancy points, consolidated across all channels taught",
    "All 8 Confluent points (Eight Extraordinary Vessels) -- now fully paired and finalized",
]
for b in bullets:
    setfill(GOLD); c.circle(ML + 3, y + 3, 1.6, fill=1, stroke=0)
    setfill(DARK)
    lines = wrap_words(b, "Lora", 9.5, CW - 20)
    for i, l in enumerate(lines):
        c.drawString(ML + 14, y - i * 12, l)
    y -= 12 * max(1, len(lines)) + 4

y -= 10
box_h = 42
setfill(CREAM); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(DARK); c.setFont("Lora-Italic", 8.6)
c.drawString(ML + 14, y - 16, "Content verified against AC300 Channel Workbook v28, Weeks 2-6 lecture transcripts/slides,")
c.drawString(ML + 14, y - 29, "and this project's own Study Guide data. Nothing here is guessed -- flag any discrepancy for Dr. Zhang.")
y -= box_h + 20

setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300 Master Comparison \u00b7 Cumulative \u00b7 Update after each new channel week")
end_page(WEEK_LABEL)


# ============================================================
# FULL ATTRIBUTE TABLE -- 12 columns
# ============================================================
new_page()
y = H - 46
y = section_bar(y, "Full Attribute Table -- All 12 Channels", NAVY, 13)

CHANNELS = ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "SJ", "GB", "LR"]
COLORS = [
    (0.32, 0.42, 0.53), (0.40, 0.48, 0.58),           # Metal
    (0.706, 0.518, 0.204), (0.780, 0.612, 0.294),      # Earth
    (0.627, 0.220, 0.180), (0.784, 0.353, 0.294),      # Fire
    (0.118, 0.435, 0.400), (0.180, 0.494, 0.482),      # Water
    (0.80, 0.40, 0.36), (0.85, 0.50, 0.46),            # Ministerial Fire
    (0.20, 0.48, 0.27), (0.30, 0.56, 0.36),            # Wood
]

ROWS = [
    ("Week", ["Wk2", "Wk2", "Wk3", "Wk3", "Wk4", "Wk4", "Wk5", "Wk5", "Wk6", "Wk6", "Wk6", "Wk6"]),
    ("Yin/Yang", ["Yin", "Yang", "Yang", "Yin", "Yin", "Yang", "Yang", "Yin", "Yin", "Yang", "Yang", "Yin"]),
    ("Element", ["Metal", "Metal", "Earth", "Earth", "Fire", "Fire", "Water", "Water", "Fire (Min)", "Fire (Min)", "Wood", "Wood"]),
    ("Peak", ["3-5AM", "5-7AM", "7-9AM", "9-11AM", "11AM-1P", "1-3PM", "3-5PM", "5-7PM", "7-9PM", "9-11PM", "11P-1AM", "1-3AM"]),
    ("Points", ["11", "20", "45", "21", "9", "19", "67", "27", "9", "23", "44", "14"]),
    ("First pt", ["LU1", "LI1", "ST1", "SP1", "HT1", "SI1", "BL1", "KI1", "PC1", "SJ1", "GB1", "LR1"]),
    ("Last pt", ["LU11", "LI20", "ST45", "SP21", "HT9", "SI19", "BL67", "KI27", "PC9", "SJ23", "GB44", "LR14"]),
    ("Pertains", ["Lung", "Lg Int", "Stomach", "Spleen", "Heart", "Sm Int", "Bladder", "Kidney", "Pericard", "San Jiao", "G.Blad", "Liver"]),
    ("Connects", ["Lg Int", "Lung", "Spleen", "Stomach", "Sm Int", "Heart", "Kidney", "Bladder", "San Jiao", "Pericard", "Liver", "G.Blad"]),
    ("Yuan-Src", ["LU9", "LI4", "ST42", "SP3", "HT7", "SI4", "BL64", "KI3", "PC7", "SJ4", "GB40", "LR3"]),
    ("Luo", ["LU7", "LI6", "ST40", "SP4", "HT5", "SI7", "BL58", "KI4", "PC6", "SJ5", "GB37", "LR5"]),
    ("Xi-Cleft", ["LU6", "LI7", "ST34", "SP8", "HT6", "SI6", "BL63", "KI5", "PC4", "SJ7", "GB36", "LR6"]),
    ("Front-Mu", ["LU1", "ST25", "CV12", "LR13", "CV14", "CV4", "CV3", "GB25", "CV17", "CV5", "GB24", "LR14"]),
    ("Back-Shu", ["BL13", "BL25", "BL21", "BL20", "BL15", "BL27", "BL28", "BL23", "BL14", "BL22", "BL19", "BL18"]),
    ("Confluent", ["LU7", "--", "--", "SP4", "--", "SI3", "BL62", "KI6", "PC6", "SJ5", "GB41", "--"]),
    ("Command", ["LU7", "LI4", "ST36", "--", "--", "--", "BL40", "--", "--", "--", "--", "--"]),
]

label_w = 62
n = len(CHANNELS)
col_w = (CW - label_w) / n
hdr_h = 14
setfill(NAVY); c.rect(ML, y - hdr_h, label_w, hdr_h, fill=1, stroke=0)
for i, ch in enumerate(CHANNELS):
    setfill(COLORS[i]); c.rect(ML + label_w + i * col_w, y - hdr_h, col_w, hdr_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 6.6)
    c.drawCentredString(ML + label_w + i * col_w + col_w / 2, y - hdr_h + 4, ch)
y -= hdr_h

row_h = 14.5
for ridx, (label, vals) in enumerate(ROWS):
    bg = (0.958, 0.958, 0.958) if ridx % 2 == 0 else (1, 1, 1)
    setfill(NAVY); c.rect(ML, y - row_h, label_w, row_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 6.6)
    c.drawString(ML + 3, y - row_h + 4.5, label)
    for i, v in enumerate(vals):
        setfill(bg); c.rect(ML + label_w + i * col_w, y - row_h, col_w, row_h, fill=1, stroke=0)
        setfill(DARK); c.setFont("Lora", 6.0)
        c.drawCentredString(ML + label_w + i * col_w + col_w / 2, y - row_h + 4.5, v)
    y -= row_h

y -= 18
y = section_bar(y, "Circuits Mapped -- All 3 Complete", NAVY, 11)
setfill(NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "Anterior Circuit (Weeks 2-3)")
y -= 12
setfill(DARK); c.setFont("Lora", 8.6)
c.drawString(ML, y, "LU -> LI -> ST -> SP   \u2014   chest->hand->head->foot->chest")
y -= 18
setfill(NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "Posterior (Inner) Circuit (Weeks 4-5)")
y -= 12
setfill(DARK); c.setFont("Lora", 8.6)
c.drawString(ML, y, "HT -> SI -> BL -> KI   \u2014   chest->hand->head->foot->chest")
y -= 18
setfill((0.80, 0.40, 0.36)); c.setFont("Lora-Bold", 9.5)
c.drawString(ML, y, "Middle Circuit (Week 6) -- NEW, completes all 12 channels")
y -= 12
setfill(DARK); c.setFont("Lora", 8.6)
c.drawString(ML, y, "PC -> SJ -> GB -> LR   \u2014   chest->hand->head->foot->chest (transcript: 'a totally middle circuit')")
end_page(WEEK_LABEL)


# ============================================================
# TRAP NOTES + FORBIDDEN PREGNANCY + CONFLUENT POINTS
# ============================================================
new_page()
y = H - 46
y = section_bar(y, "Cross-Week Trap Notes  &  Forbidden-in-Pregnancy", (0.753, 0.224, 0.161), 13)

trap_box_h = 178
setfill((0.980, 0.930, 0.925)); c.rect(ML, y - trap_box_h, CW, trap_box_h, fill=1, stroke=0)
setstroke((0.753, 0.224, 0.161)); c.setLineWidth(2 * LW_MULT)
c.line(ML, y - trap_box_h, ML, y)
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-Bold", 9.5)
c.drawString(ML + 10, y - 14, "Recurring Connection Traps")
ty = y - 28
setfill(DARK); c.setFont("Lora", 8.4)
traps = [
    "LI connects to STOMACH (not Spleen) -- LI's branch ends beside the nose (LI20) where ST begins.",
    "SP connects to HEART (not LI) -- SP's internal branch goes stomach->diaphragm->heart, linking HT.",
    "BL connects to KIDNEY (not Lung) -- confirmed exam trap; do not confuse with the Metal-element pathway.",
    "KI connects to PERICARDIUM (not Lung) -- KI's branch from the Lung joins the Heart then links PC, opening Week 6.",
    "Only ST passes through the NIPPLE. Only SP spreads over the LOWER surface of the tongue. Only KI reaches the tongue ROOT via a re-emerging branch.",
    "UPPER teeth/gums = ST channel. LOWER teeth/gums = LI channel. Reversing these is a classic trap.",
    "SP is the ONLY channel with a distribution exception (crosses in front of LR above 8 cun from medial malleolus).",
    "PC and HT are the ONLY 2 primary channels with ZERO crossing points.",
    "GB and SJ (both Shaoyang) cross each other TWICE at the shoulder -- GB in front, then behind.",
    "GB and LR belong to the MIDDLE Circuit (Week 6) -- NOT the Posterior Circuit (HT/SI/BL/KI). Easy to mix up.",
    "Yuan-Source = Shu-Stream on every YIN channel (LU9, SP3, HT7, KI3, PC7, LR3) -- never true on Yang channels.",
]
for t in traps:
    lines = wrap_words("! " + t, "Lora", 8.4, CW - 20)
    for l in lines:
        c.drawString(ML + 10, ty, l); ty -= 10.4
y -= trap_box_h + 12

y = section_bar(y, "Forbidden in Pregnancy -- All Channels Taught So Far", NAVY, 10.5)
preg = [
    ("LI4", "Hegu", "Command point face/mouth; strong descending/moving action"),
    ("SP6", "Sanyinjiao", "3-Yin meeting point; strong descending/moving action on the uterus"),
    ("BL60", "Kunlun", "Historically listed forbidden; strong distal action"),
    ("BL67", "Zhiyin", "Used deliberately to correct fetal malposition/induce labor -- forbidden otherwise"),
    ("GB21", "Jianjing", "Strong descending action, can induce labor -- new this week (Wk6)"),
]
for i, (pt, pin, note) in enumerate(preg):
    row_h = 13.5
    bg = (0.976, 0.965, 0.938) if i % 2 == 0 else (1, 1, 1)
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill((0.80, 0.55, 0.15)); c.setFont("Lora-Bold", 8.6)
    c.drawString(ML + 6, y - 10, pt)
    setfill(DARK); c.setFont("Lora-Italic", 8.3)
    c.drawString(ML + 46, y - 10, pin)
    c.setFont("Lora", 8.1)
    c.drawString(ML + 130, y - 10, note)
    y -= row_h

y -= 14
y = section_bar(y, "Confluent Points -- Eight Extraordinary Vessels -- ALL 8 NOW COMPLETE", NAVY, 10.5)
conf = [
    ("LU7 Lieque", "Ren Mai (Conception Vessel)", "Paired with KI6"),
    ("KI6 Zhaohai", "Yin Qiao Mai (Yin Heel Vessel)", "Paired with LU7"),
    ("SI3 Houxi", "Du Mai (Governing Vessel)", "Paired with BL62"),
    ("BL62 Shenmai", "Yang Qiao Mai (Yang Heel Vessel)", "Paired with SI3"),
    ("SP4 Gongsun", "Chong Mai (Penetrating Vessel)", "Paired with PC6"),
    ("PC6 Neiguan", "Yin Wei Mai (Yin Linking Vessel)", "Paired with SP4"),
    ("SJ5 Waiguan", "Yang Wei Mai (Yang Linking Vessel)", "Paired with GB41"),
    ("GB41 Zulinqi", "Dai Mai (Belt Vessel)", "Paired with SJ5"),
]
for i, (pt, vessel, pair) in enumerate(conf):
    row_h = 15
    bg = (0.945, 0.947, 0.963) if i % 2 else (1, 1, 1)
    setfill(bg); c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setfill(NAVY); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML + 6, y - 11, pt)
    setfill(DARK); c.setFont("Lora", 8.6)
    c.drawString(ML + 110, y - 11, vessel)
    setfill(GRAY); c.setFont("Lora-Italic", 8.2)
    c.drawRightString(RX - 6, y - 11, pair)
    y -= row_h

end_page(WEEK_LABEL)

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
