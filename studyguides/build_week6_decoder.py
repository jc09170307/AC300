#!/usr/bin/env python3
"""AC300 Week 6 Special Points Decoder -- standalone drillable reference.
Covers all special point categories with PC/SJ/GB/LR examples. Print + reMarkable."""
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
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    ROW_TINT = (0.925, 0.902, 0.855)
    OUT = "/mnt/user-data/outputs/AC300_Week6_SpecialPointsDecoder_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    ROW_TINT = (0.965, 0.967, 0.972)
    OUT = "/mnt/user-data/outputs/AC300_Week6_SpecialPointsDecoder_Print.pdf"
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


ML, MR = 32, 32
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle):
    page_bg()
    setfill(NAVY); c.rect(0, H - 46, W, 46, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 15)
    c.drawString(ML, H - 30, "Week 6 Special Points Decoder")
    setfill(GOLD); c.setFont("Lora-Italic", 9)
    c.drawRightString(W - MR, H - 30, EDLABEL)
    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawString(ML, H - 60, subtitle)
    return H - 76


def footer():
    setstroke(GRAY); c.setLineWidth(0.4 * LW_MULT)
    c.line(ML, 24, W - MR, 24)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawString(ML, 12, "AC300/AC375 \u00b7 Special Points Decoder \u00b7 VUIM Summer 2026")
    c.drawRightString(W - MR, 12, f"p.{page_num[0]}")


def end_page():
    footer(); c.showPage(); page_num[0] += 1


def category_block(y, cat, definition, examples, color):
    lines_def = wrap_words(definition, "Lora", 8.6, CW - 130)
    ex_lines = []
    for ex in examples:
        ex_lines.extend(wrap_words(ex, "Lora", 8.3, CW - 130))
    # If the category label itself is too wide for the label column, push the
    # body text down to the next line instead of overlapping it.
    label_w = pdfmetrics.stringWidth(cat, "Lora-Bold", 10.5)
    label_wraps = label_w > 118
    total_lines = max(len(lines_def), 1) + len(ex_lines) + 1 + (1 if label_wraps else 0)
    row_h = 13 + total_lines * 10.6
    if y - row_h < 55:
        end_page()
        y = header("(continued)")
    setfill(tuple(min(1, ch + 0.88) for ch in color))
    c.rect(ML, y - row_h, CW, row_h, fill=1, stroke=0)
    setstroke(color); c.setLineWidth(2.4 * LW_MULT)
    c.line(ML, y - row_h, ML, y)
    setfill(color); c.setFont("Lora-Bold", 10.5)
    c.drawString(ML + 10, y - 14, cat)
    setfill(DARK); c.setFont("Lora", 8.6)
    yy = y - 14 - (14 if label_wraps else 0)
    body_x = ML + 10 if label_wraps else ML + 130
    for l in lines_def:
        c.drawString(body_x, yy, l); yy -= 10.6
    yy -= 2
    setfill(color); c.setFont("Lora-Bold", 8.3)
    c.drawString(body_x, yy, "This week's examples:")
    yy -= 10.6
    setfill(DARK); c.setFont("Lora", 8.3)
    for l in ex_lines:
        c.drawString(body_x, yy, l); yy -= 10.6
    return y - row_h - 8


CATS = [
    ("JING-WELL", "1st/last point of each channel (start of Yin channels, end of Yang). Clears heat, restores consciousness -- emergency/resuscitation use.",
     ["PC9 Zhongchong (last, PC), SJ1 Guanchong (first, SJ), GB44 Zuqiaoyin (last, GB), LR1 Dadun (first, LR)"], NAVY),
    ("YING-SPRING", "2nd point on each channel. Clears heat in the body, used for febrile disease.",
     ["PC8 Laogong, SJ2 Yemen, LR2 Xingjian"], NAVY),
    ("SHU-STREAM", "3rd point (also Yuan-Source on Yin channels). Treats heaviness, joint pain, intermittent disorders.",
     ["PC7 Daling (=Yuan), SJ3 Zhongzhu, GB41 Zulinqi (=Confluent), LR3 Taichong (=Yuan)"], NAVY),
    ("JING-RIVER", "4th point. Treats cough, dyspnea, throat disorders, chills & fever.",
     ["PC5 Jianshi, SJ6 Zhigou, LR4 Zhongfeng"], NAVY),
    ("HE-SEA", "At elbow/knee. Treats counterflow Qi, diarrhea, and organ-level disorders of the associated Zang/Fu.",
     ["PC3 Quze, SJ10 Tianjing, GB34 Yanglingquan (also Hui-Meeting Sinews), LR8 Ququan"], (0.62, 0.22, 0.18)),
    ("YUAN-SOURCE", "Where the Source (Yuan) Qi of the channel/organ is accessed. Primary diagnostic + treatment point for the Zang/Fu.",
     ["PC7 Daling, SJ4 Yangchi, GB40 Qiuxu, LR3 Taichong"], (0.62, 0.22, 0.18)),
    ("LUO-CONNECTING", "Where a channel's Luo-vessel branches to its paired channel. Treats psycho-emotional issues + disorders on the paired channel.",
     ["PC6 Neiguan, SJ5 Waiguan, GB37 Guangming, LR5 Ligou"], (0.62, 0.22, 0.18)),
    ("XI-CLEFT", "Cleft point where Qi/Blood gather deeply. Used for ACUTE conditions/pain of the channel or organ.",
     ["PC4 Ximen, SJ7 Huizong, GB36 Waiqiu, LR6 Zhongdu"], (0.62, 0.22, 0.18)),
    ("FRONT-MU", "On the chest/abdomen; where the Qi of a Zang/Fu organ gathers. Used diagnostically (palpation) and therapeutically.",
     ["PC = CV17 Danzhong, SJ = CV5 Shimen, GB = GB24 Riyue, LR = LR14 Qimen (note: LR13 Zhangmen is Front-Mu of SPLEEN, not Liver -- classic mix-up)"], (0.20, 0.40, 0.55)),
    ("BACK-SHU", "On the Bladder channel, 1.5 cun lateral to the spine. Transport points for each Zang/Fu's Qi.",
     ["PC = BL14 Jueyinshu, SJ = BL22 Sanjiaoshu, GB = BL19 Danshu, LR = BL18 Ganshu"], (0.20, 0.40, 0.55)),
    ("CONFLUENT", "Opens one of the 8 Extraordinary Vessels; 8 points total, paired across upper/lower body.",
     ["SJ5 Waiguan opens Yang Wei Mai (pairs GB41); GB41 Zulinqi opens Dai Mai (pairs SJ5) -- BOTH new this week, PC/LR have no confluent point this week"], (0.62, 0.22, 0.18)),
    ("HUI-MEETING (INFLUENTIAL)", "8 points, each the 'meeting place' of Qi for a tissue/substance category (Zang, Fu, Qi, Blood, Sinews, Vessels, Marrow, Bones).",
     ["GB34 = Hui-Meeting of SINEWS/TENDONS; LR13 Zhangmen = Hui-Meeting of ZANG (all 5 solid organs) + also Front-Mu of Spleen"], (0.20, 0.48, 0.27)),
    ("CROSSING POINTS", "A point on one channel that is also crossed by one or more OTHER channels' pathways.",
     ["PC + LR: ZERO/minimal crossing points this week (PC has none). SJ + GB: extensive overlap around the head/ear/shoulder (both Shaoyang channels) -- GB's exact count is flagged/unresolved pending Dr. Zhang"], GOLD),
    ("COMMAND POINTS", "4 master points: abdomen (ST36), back/lumbar (BL40 Weizhong), head/face (LI4), face (LI4 shared). Not introduced fresh this week but relevant when combining with PC/SJ/GB/LR points for full-body treatment plans.",
     ["No new Command points this week -- reference only"], GRAY),
    ("LOWER HE-SEA", "Special He-Sea points for the 6 Fu organs, located on the leg (used even for Fu organs whose main channel is on the arm).",
     ["SJ's Lower He-Sea is BL39 Weiyang (NOT on the SJ channel itself) -- exam trap identical in structure to LI/SI/ST's lower he-sea points from earlier weeks; GB's Lower He-Sea is its own He-Sea, GB34"], GOLD),
]

y = header("All special point categories \u00b7 examples drawn from PC, SJ, GB, LR (Week 6)")
for cat, definition, examples, color in CATS:
    y = category_block(y, cat, definition, examples, color)
end_page()

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
