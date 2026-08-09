#!/usr/bin/env python3
"""AC300 Week 4 Quiz Kit - HT & SI. 30-question practice exam, closed book,
varying difficulty. Matches Week 3 Quiz Kit design. Builds Print + reMarkable."""
import sys
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
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.976, 0.965, 0.929)

HT_COLOR = (0.627, 0.220, 0.180)
HT_TINT = (0.976, 0.928, 0.919)
SI_COLOR = (0.784, 0.353, 0.294)
SI_TINT = (0.983, 0.948, 0.938)
MINT = (0.933, 0.958, 0.941)
LAV = (0.965, 0.941, 0.965)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    OUT = "/mnt/user-data/outputs/AC300_Week4_QuizKit_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week4_QuizKit_Print.pdf"
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


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]

WEEK_LABEL = "AC300/AC375 | Week 4 Quiz Kit | HT & SI | VUIM Summer 2026"


def simple_header():
    setfill(DARK); c.setFont("Lora", 9)
    c.drawString(ML, H - 30, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
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
    page_bg()
    simple_header()


def end_page():
    simple_footer()
    c.showPage()
    page_num[0] += 1


def section_bar(y, title, right_text, color, size=13):
    bar_h = 26
    setfill(color); c.rect(ML - 4, y - bar_h, CW + 8, bar_h, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", size)
    c.drawString(ML + 6, y - bar_h + 8, title)
    c.setFont("Lora-Italic", 10)
    c.drawRightString(W - MR - 2, y - bar_h + 9, right_text)
    return y - bar_h - 14


DIFF_COLOR = {"easy": (0.318, 0.573, 0.345), "medium": (0.729, 0.573, 0.184), "hard": HT_COLOR}
DIFF_TINT = {"easy": MINT, "medium": (0.976, 0.953, 0.902), "hard": HT_TINT}


# ============================================================
# 30 QUESTIONS - same verified set built for the Study Guide draft,
# cross-checked against HT_POINTS/SI_POINTS/META/FIVE_SHU/HIGHEST_YIELD/
# CLINICAL_PEARLS/COMPARISON_HT_SI in week4_sg_content.py
# ============================================================
QUIZ4_PRACTICE = [
    ("How many points does the HT channel have?",
     ["9", "11", "19", "20"], "A",
     "HT has 9 points (HT1-HT9) - the fewest of any primary channel.", "easy"),
    ("How many points does the SI channel have?",
     ["9", "11", "19", "20"], "C",
     "SI has 19 points (SI1-SI19) - more than double HT's count.", "easy"),
    ("What element do HT and SI both belong to?",
     ["Earth", "Fire", "Water", "Wood"], "B",
     "HT and SI are the Primary Fire pair (not to be confused with PC/SJ, the Ministerial Fire pair).", "easy"),
    ("HT is classified as which Yin/Yang type?",
     ["Yin (Hand-Shaoyin)", "Yang (Hand-Taiyang)", "Yin (Foot-Shaoyin)", "Yang (Foot-Taiyang)"], "A",
     "HT = Heart Meridian of Hand-Shaoyin - a Yin, Zang (organ) channel.", "easy"),
    ("SI is classified as which Yin/Yang type?",
     ["Yin (Hand-Shaoyin)", "Yang (Hand-Taiyang)", "Yin (Foot-Taiyin)", "Yang (Foot-Yangming)"], "B",
     "SI = Small Intestine Meridian of Hand-Taiyang - a Yang, Fu (bowel) channel.", "easy"),
    ("Peak Qi activity of the Heart meridian is:",
     ["9-11 AM", "11 AM-1 PM", "1-3 PM", "3-5 PM"], "B",
     "HT peaks 11 AM-1 PM, immediately after SP (9-11 AM) and before SI (1-3 PM).", "easy"),
    ("Peak Qi activity of the Small Intestine meridian is:",
     ["11 AM-1 PM", "1-3 PM", "3-5 PM", "5-7 PM"], "B",
     "SI peaks 1-3 PM, immediately after HT.", "easy"),
    ("The CONNECTING organ of the Heart meridian is:",
     ["Lung", "Stomach", "Small Intestine", "Bladder"], "C",
     "Pertaining = Heart, Connecting = Small Intestine (interior-exterior pair).", "easy"),
    ("HT's Back-Shu point is:",
     ["BL14", "BL15", "BL20", "BL27"], "B",
     "BL15 Xinshu is HT's Back-Shu point. (SI's is BL27 Xiaochangshu.)", "easy"),
    ("SI's Front-Mu point is:",
     ["CV12", "CV14", "CV4", "CV3"], "C",
     "CV4 Guanyuan is SI's Front-Mu point. (HT's is CV14 Juque.)", "easy"),
    ("HT7 Shenmen holds which special point categories?",
     ["He-Sea + Luo-Connecting", "Shu-Stream + Yuan-Source", "Jing-Well + Xi-Cleft", "Front-Mu + Back-Shu"], "B",
     "HT7 is both the Shu-Stream and Yuan-Source point - the single most important point for calming Shen.", "medium"),
    ("Which HT point is the He-Sea?",
     ["HT3 Shaohai", "HT7 Shenmen", "HT9 Shaochong", "HT1 Jiquan"], "A",
     "HT3 Shaohai is the He-Sea point, at the elbow crease.", "medium"),
    ("SI3 Houxi holds which special categories?",
     ["Yuan-Source only", "He-Sea + Xi-Cleft", "Shu-Stream + Confluent (opens Du Mai)", "Jing-Well + Luo"], "C",
     "SI3 is Shu-Stream and also a Confluent point opening the Du Mai.", "medium"),
    ("SI3's Confluent action opens the Du Mai in combination with which point?",
     ["LU7", "BL62 Shenmai", "KI6", "SP4"], "B",
     "SI3 (Houxi) pairs with BL62 (Shenmai) to open the Du Mai - one of the 8 Confluent point pairs.", "medium"),
    ("HT9 Shaochong is which Five-Shu category?",
     ["Jing-Well", "Ying-Spring", "Shu-Stream", "He-Sea"], "A",
     "HT9 is the Jing-Well point - the last point of HT, on the radial side of the little finger.", "medium"),
    ("SI's Lower He-Sea point is located on which channel?",
     ["SI itself", "BL", "ST", "GB"], "C",
     "SI's Lower He-Sea is ST39 Xiajuxu - on the STOMACH channel, not SI. True for all six Fu organs.", "medium"),
    ("Which point is SI's Xi-Cleft?",
     ["SI4 Wangu", "SI6 Yanglao", "SI7 Zhizheng", "SI8 Xiaohai"], "B",
     "SI6 Yanglao is the Xi-Cleft point, dorsal to the head of the ulna.", "medium"),
    ("HT5 Tongli's special category is:",
     ["Luo-Connecting", "Xi-Cleft", "Yuan-Source", "He-Sea"], "A",
     "HT5 Tongli is the Luo-Connecting point, linking HT to SI.", "medium"),
    ("SI16 Tianchuang is classified as:",
     ["Window of Heaven", "Confluent", "Front-Mu", "Back-Shu"], "A",
     "SI16 is a Window of Heaven point, near the laryngeal prominence - needle with care (carotid region).", "medium"),
    ("Per Dr. Zhang's lecture, which point is specifically noted for breast milk / lactation problems?",
     ["HT8 Shaofu", "SI1 Shaoze", "SI19 Tinggong", "HT3 Shaohai"], "B",
     "Dr. Zhang highlighted SI1 (Shaoze) specifically for lactation problems.", "medium"),
    ("How many crossing points does the HT channel have?",
     ["0", "2", "4", "6"], "A",
     "HT is the only one of the 12 primary channels with ZERO crossing points anywhere on its pathway.", "hard"),
    ("How many crossing points does SI have, and with which channels?",
     ["0", "2 (BL1, GB14)", "6 (mostly abdomen/chest)", "11 (mostly face/head)"], "B",
     "SI crosses only twice: BL1 (Jingming) and GB14 (Yangbai), both on its facial branch.", "hard"),
    ("SI's facial branch crosses BL1 Jingming en route to:",
     ["The ear", "The inner canthus of the eye", "The nose", "The mouth"], "B",
     "BL1 sits at the inner canthus; SI's ascending branch crosses it heading toward the eye.", "hard"),
    ("Which statement about HT is exam-critical and TRUE?",
     ["HT has the most points of any channel", "HT is the only channel with zero crossing points",
      "HT connects internally to the Lung", "HT's Back-Shu is CV14"], "B",
     "HT's zero crossing points is one of the highest-yield unique-feature facts in the Weeks 1-4 scope.", "hard"),
    ("Per Dr. Zhang's circuit-continuity trap, SI connects internally to which organ NEXT?",
     ["Pericardium", "San Jiao", "Bladder", "Kidney"], "C",
     "SI connects to BLADDER next (not PC/SJ) via its facial branch to BL1 - a classic exam trap.", "hard"),
    ("HT and SI together open which circuit?",
     ["Anterior Circuit", "Posterior Circuit (also called Inner Circuit)",
      "Ministerial Fire Circuit", "Middle Circuit"], "B",
     "HT -> SI opens the Posterior Circuit (also called Inner Circuit on the revised Lecture 4 slide).", "hard"),
    ("The Primary Fire pair (HT/SI) should not be confused with which other Fire pair?",
     ["LU/LI", "ST/SP", "PC/SJ (Ministerial Fire)", "BL/KI"], "C",
     "PC and SJ are Ministerial Fire, a separate pair with their own circuit taught in Week 6.", "hard"),
    ("EXCEPT: all of the following are TRUE about SI EXCEPT:",
     ["SI has more than double HT's points", "SI3 opens the Du Mai",
      "SI's Lower He-Sea is on the SI channel itself", "SI crosses BL1 and GB14"], "C",
     "SI's Lower He-Sea is ST39, on the STOMACH channel - not on SI itself. The trap answer.", "hard"),
    ("Which HT point is the emergency point for severe heart pain and revives consciousness?",
     ["HT7 Shenmen", "HT9 Shaochong", "HT3 Shaohai", "HT5 Tongli"], "B",
     "HT9 (Jing-Well) is HT's emergency point - severe heart pain, palpitations, revives consciousness.", "hard"),
    ("HT6 Yinxi (Xi-Cleft) is clinically noted for:",
     ["Anxiety and insomnia only", "Night sweats and acute heart pain", "Voice disorders", "Arm pain only"], "B",
     "As HT's Xi-Cleft (acute) point, HT6 treats night sweats and acute heart pain.", "hard"),
]

assert len(QUIZ4_PRACTICE) == 30


# ============================================================
# PAGE 1: COVER
# ============================================================
page_bg()
simple_header()
y = H - 70
setfill(NAVY); c.rect(ML - 4, y - 130, CW + 8, 130, fill=1, stroke=0)
setfill(GOLD); c.setFont("Lora", 11)
c.drawString(ML + 8, y - 24, "WEEK 4   |   QUIZ KIT")
setfill((1, 1, 1)); c.setFont("Lora-Bold", 26)
c.drawString(ML + 8, y - 58, "30-Question Practice Quiz")
setfill((0.9, 0.9, 0.92)); c.setFont("Lora-Italic", 12.5)
c.drawString(ML + 8, y - 84, "Heart & Small Intestine Channels - closed book")
setfill((1, 1, 1)); c.setFont("Lora-Italic", 9.5)
c.drawRightString(W - MR - 8, y - 24, EDLABEL)
y -= 150

col_w = (CW - 20) / 2
box_h = 62
setfill(HT_TINT); c.rect(ML, y - box_h, col_w, box_h, fill=1, stroke=0)
setstroke(HT_COLOR); c.setLineWidth(2)
c.line(ML, y - box_h, ML, y)
setfill(HT_COLOR); c.setFont("Lora-Bold", 13)
c.drawString(ML + 10, y - 22, "HEART  (HT)")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawString(ML + 10, y - 38, "Yin | Fire | 11 AM-1 PM | 9 points")
setfill(GRAY); c.setFont("Lora-Italic", 8.8)
c.drawString(ML + 10, y - 52, "Hand Shaoyin | 0 crossing points")

x2 = ML + col_w + 20
setfill(SI_TINT); c.rect(x2, y - box_h, col_w, box_h, fill=1, stroke=0)
setstroke(SI_COLOR); c.setLineWidth(2)
c.line(x2, y - box_h, x2, y)
setfill(SI_COLOR); c.setFont("Lora-Bold", 13)
c.drawString(x2 + 10, y - 22, "SMALL INTESTINE  (SI)")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawString(x2 + 10, y - 38, "Yang | Fire | 1-3 PM | 19 points")
setfill(GRAY); c.setFont("Lora-Italic", 8.8)
c.drawString(x2 + 10, y - 52, "Hand Taiyang | 2 crossing points")

y -= box_h + 30
setfill(NAVY); c.setFont("Lora-Bold", 12)
setstroke(NAVY); c.setLineWidth(2.2)
c.line(ML - 4, y - 3, ML - 4, y + 13)
c.drawString(ML + 6, y, "Coverage")
y -= 22
setfill(DARK); c.setFont("Lora", 10.5)
c.drawString(ML + 6, y, "10 easier recall questions (concepts, point counts, clock times)")
c.drawRightString(W - MR, y, "Q1-Q10")
y -= 16
c.drawString(ML + 6, y, "10 applied questions (point categories, locations, syndromes)")
c.drawRightString(W - MR, y, "Q11-Q20")
y -= 16
c.drawString(ML + 6, y, "10 trap/nuance questions (exceptions, circuit traps, EXCEPT format)")
c.drawRightString(W - MR, y, "Q21-Q30")
y -= 16
c.drawString(ML + 6, y, "Full answer key with explanations for all 30")
c.drawRightString(W - MR, y, "at the back")

y -= 30
box_h2 = 96
setfill(MINT); c.rect(ML, y - box_h2, col_w, box_h2, fill=1, stroke=0)
setfill((0.196, 0.412, 0.325)); c.rect(ML, y - 15, col_w, 15, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
c.drawString(ML + 6, y - 11.5, "How to use this")
setfill(DARK); c.setFont("Lora", 9)
lines = ["Close the book. No notes, no app.", "Take it in one sitting, ~25 min.",
         "Mark every guess, even correct ones.", "Score, then re-drill ONLY the misses.",
         "Green = easy, gold = applied, red = trap."]
yy = y - 28
for l in lines:
    setfill(DARK); c.circle(ML + 8, yy + 3, 1.6, fill=1, stroke=0)
    c.drawString(ML + 15, yy, l)
    yy -= 13.5

setfill(LAV); c.rect(x2, y - box_h2, col_w, box_h2, fill=1, stroke=0)
setfill((0.392, 0.161, 0.412)); c.rect(x2, y - 15, col_w, 15, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
c.drawString(x2 + 6, y - 11.5, "Scoring guide")
setfill(DARK); c.setFont("Lora", 9)
score_lines = [("27-30", "Exam ready. Preview Week 5 midterm."), ("23-26", "Solid. Drill missed categories."),
               ("18-22", "Re-read the Study Guide pathway pages."), ("Below 18", "Full re-study before Quiz 4.")]
yy = y - 28
for score, desc in score_lines:
    setfill(SI_COLOR); c.setFont("Lora-Bold", 9)
    c.drawString(x2 + 6, yy, score)
    setfill(DARK); c.setFont("Lora", 9)
    for l in wrap_words(desc, "Lora", 9, col_w - 70):
        c.drawString(x2 + 68, yy, l)
        yy -= 12.5
    yy -= 3

y -= box_h2 + 24
setfill(CREAM); c.rect(ML - 4, y - 40, CW + 8, 40, fill=1, stroke=0)
setstroke(GOLD); c.setLineWidth(2.2)
c.line(ML - 4, y - 40, ML - 4, y)
setfill(HT_COLOR); c.setFont("Lora-Italic", 9.5)
c.drawString(ML + 6, y - 16, "30 questions, 10 easy + 10 medium + 10 hard - covers HT & SI comprehensively.")
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawString(ML + 6, y - 30, "Cross-checked against the Week 4 Study Guide's verified point data - nothing invented.")

y -= 90
setfill(GRAY); c.setFont("Lora-Italic", 9.5)
c.drawCentredString(W / 2, y, "Dr. Vivian Zhang, Ph.D.  |  Jon Centeno, D.AcHM Candidate  |  VUIM")

end_page()


# ============================================================
# QUESTION PAGES
# ============================================================
def question_card(y, num, q, opts, diff):
    q_lines = wrap_words(q, "Lora", 10.3, CW - 60)
    opt_lines = [(f"A. {opts[0]}", f"B. {opts[1]}"), (f"C. {opts[2]}", f"D. {opts[3]}")]
    card_h = len(q_lines) * 13 + len(opt_lines) * 13 + 16
    tint = DIFF_TINT[diff]
    setfill(tint); c.rect(ML - 4, y - card_h, CW + 8, card_h, fill=1, stroke=0)
    setfill(DIFF_COLOR[diff]); c.circle(ML + 12, y - 13, 9, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9)
    c.drawCentredString(ML + 12, y - 16, str(num))
    setfill(DARK); c.setFont("Lora-Bold", 10.3)
    yy = y - 10
    for l in q_lines:
        c.drawString(ML + 30, yy, l)
        yy -= 13
    setfill(DARK); c.setFont("Lora", 9.6)
    col2 = ML + CW / 2
    for left, right in opt_lines:
        c.drawString(ML + 30, yy, left)
        c.drawString(col2, yy, right)
        yy -= 13
    return y - card_h - 10


SET_LABEL = "HT & SI  |  no notes"
new_page()
y = H - 46
y = section_bar(y, "Questions 1-15", SET_LABEL, NAVY, size=14)
for i in range(15):
    q, opts, correct, expl, diff = QUIZ4_PRACTICE[i]
    needed_est = 70
    if y - needed_est < 45:
        end_page()
        new_page()
        y = H - 46
        y = section_bar(y, "Questions 1-15 (continued)", SET_LABEL, NAVY, size=14)
    y = question_card(y, i + 1, q, opts, diff)
end_page()

new_page()
y = H - 46
y = section_bar(y, "Questions 16-30", SET_LABEL, NAVY, size=14)
for i in range(15, 30):
    q, opts, correct, expl, diff = QUIZ4_PRACTICE[i]
    needed_est = 70
    if y - needed_est < 45:
        end_page()
        new_page()
        y = H - 46
        y = section_bar(y, "Questions 16-30 (continued)", SET_LABEL, NAVY, size=14)
    y = question_card(y, i + 1, q, opts, diff)
end_page()


# ============================================================
# ANSWER KEY
# ============================================================
new_page()
y = H - 46
y = section_bar(y, "Answer Key  -  All 30 Questions", "score, then re-drill only the misses", NAVY, size=14)

for i, (q, opts, correct, expl, diff) in enumerate(QUIZ4_PRACTICE, 1):
    q_lines = wrap_words(q, "Lora-Bold", 9.6, CW - 40)
    expl_lines = wrap_words(expl, "Lora", 9.3, CW - 40)
    needed = len(q_lines) * 12 + len(expl_lines) * 11.5 + 12
    if y - needed < 45:
        end_page()
        new_page()
        y = H - 46
        y = section_bar(y, "Answer Key (continued)", "score, then re-drill only the misses", NAVY, size=14)
    setstroke(DIFF_COLOR[diff]); c.setLineWidth(2.4)
    c.line(ML - 4, y - needed + 8, ML - 4, y + 2)
    setfill(NAVY); c.setFont("Lora-Bold", 9.8)
    c.drawString(ML + 4, y, f"{i}   {correct}")
    setfill(DARK); c.setFont("Lora-Bold", 9.6)
    lead = pdfmetrics.stringWidth(f"{i}   {correct}   ", "Lora-Bold", 9.8) + 4
    yy = y
    for j, l in enumerate(q_lines):
        c.drawString(ML + 4 + (lead if j == 0 else 0), yy, l)
        yy -= 12
    setfill(DARK); c.setFont("Lora", 9.3)
    for l in expl_lines:
        c.drawString(ML + 4, yy, l)
        yy -= 11.5
    y = yy - 4

end_page()

c.save()
print("SAVED:", OUT)
