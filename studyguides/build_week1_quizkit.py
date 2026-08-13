#!/usr/bin/env python3
"""AC300 Week 1 Quiz Kit - Channel Theory (Concept, Nomenclature, Flow of Qi).
30-question practice set, closed book, varying difficulty. Matches Week 4
Quiz Kit design pattern. Builds Print + reMarkable.
All facts verified against week1_content.py (itself verified against
AC300Week1.txt, the Week 1 lecture transcript)."""
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

RED = (0.627, 0.220, 0.180)
RED_TINT = (0.976, 0.928, 0.919)
BLUE = (0.204, 0.361, 0.541)
BLUE_TINT = (0.925, 0.941, 0.957)
MINT = (0.933, 0.958, 0.941)
LAV = (0.965, 0.941, 0.965)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"

if IS_RM:
    PAGE_BG = (0.973, 0.953, 0.902)
    OUT = "/mnt/user-data/outputs/AC300_Week1_QuizKit_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week1_QuizKit_Print.pdf"
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

WEEK_LABEL = "AC300/AC375 | Week 1 Quiz Kit | Channel Theory | VUIM Summer 2026"


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


DIFF_COLOR = {"easy": (0.318, 0.573, 0.345), "medium": (0.729, 0.573, 0.184), "hard": RED}
DIFF_TINT = {"easy": MINT, "medium": (0.976, 0.953, 0.902), "hard": RED_TINT}


# ============================================================
# 30 QUESTIONS - verified against week1_content.py, itself checked
# against AC300Week1.txt (Dr. Zhang's Week 1 lecture transcript)
# ============================================================
QUIZ1_PRACTICE = [
    ("How many Primary Meridians (Jing) does the body have?",
     ["8", "12", "14", "15"], "B",
     "12 Primary Meridians - the main 'rivers' of the channel system.", "easy"),
    ("How many Collaterals (Luo) does the body have?",
     ["8", "12", "15", "20"], "C",
     "15 Collaterals: one Luo-connecting point per primary meridian (12) plus the Luo of Du Mai, Ren Mai, and the Spleen's Great Luo (Dabao).", "easy"),
    ("How many Zang (Yin) organs pair with primary meridians?",
     ["4", "5", "6", "8"], "C",
     "6 Zang organs: Lung, Spleen, Heart, Liver, Kidney, Pericardium.", "easy"),
    ("How many Fu (Yang) organs pair with primary meridians?",
     ["4", "5", "6", "8"], "C",
     "6 Fu organs: Large Intestine, Stomach, Small Intestine, Bladder, Gallbladder, San Jiao.", "easy"),
    ("'Channels' (Jing-Luo) as a term refers to:",
     ["The 12 Primary Meridians only", "Meridians AND Collaterals together", "Only the Extraordinary Vessels", "Only the Divergent Meridians"], "B",
     "Dr. Zhang directly clarified this in lecture: 'channels' is the bigger, umbrella term - Meridians (Jing) plus Collaterals (Luo).", "easy"),
    ("Yin meridians of the HAND flow in which direction?",
     ["Chest -> Hand", "Hand -> Head", "Head -> Foot", "Foot -> Chest"], "A",
     "Yin meridians of the hand (LU, HT, PC) all flow chest -> hand.", "easy"),
    ("Yang meridians of the HAND flow in which direction?",
     ["Chest -> Hand", "Hand -> Head", "Head -> Foot", "Foot -> Chest"], "B",
     "Yang meridians of the hand (LI, SI, SJ) all flow hand -> head.", "easy"),
    ("Yang meridians of the FOOT flow in which direction?",
     ["Chest -> Hand", "Hand -> Head", "Head -> Foot", "Foot -> Chest"], "C",
     "Yang meridians of the foot (ST, BL, GB) all flow head -> foot.", "easy"),
    ("Yin meridians of the FOOT flow in which direction?",
     ["Chest -> Hand", "Hand -> Head", "Head -> Foot", "Foot -> Chest/Abdomen"], "D",
     "Yin meridians of the foot (SP, KI, LR) all flow foot -> chest/abdomen, completing the loop.", "easy"),
    ("The Lung (LU) meridian's peak two-hour period on the meridian clock is:",
     ["1-3 AM", "3-5 AM", "5-7 AM", "7-9 AM"], "B",
     "LU peaks 3-5 AM, the very start of the 12-meridian clock cycle.", "easy"),
    ("A meridian's full 3-part name is built from which three features?",
     ["Hand/Foot + Yin/Yang + Zang/Fu", "Element + Season + Organ", "Anterior/Posterior + Zang/Fu + Number", "Yin/Yang + Element + Direction"], "A",
     "Every meridian name states its location (Hand or Foot), its nature (Yin or Yang), and its pertaining organ (Zang or Fu).", "medium"),
    ("Which sequence correctly lists the Outer/Anterior Circuit?",
     ["LU -> LI -> ST -> SP", "HT -> SI -> BL -> KI", "PC -> SJ -> GB -> LR", "SP -> ST -> LI -> LU"], "A",
     "Outer/Anterior Circuit (Taiyin/Yangming): LU -> LI -> ST -> SP.", "medium"),
    ("Which sequence correctly lists the Inner/Posterior Circuit?",
     ["LU -> LI -> ST -> SP", "HT -> SI -> BL -> KI", "PC -> SJ -> GB -> LR", "KI -> BL -> SI -> HT"], "B",
     "Inner/Posterior Circuit (Shaoyin/Taiyang): HT -> SI -> BL -> KI. 'Posterior' and 'Inner' name the same circuit across different slide versions.", "medium"),
    ("Which sequence correctly lists the Middle Circuit?",
     ["LU -> LI -> ST -> SP", "HT -> SI -> BL -> KI", "PC -> SJ -> GB -> LR", "GB -> LR -> PC -> SJ"], "C",
     "Middle Circuit (Jueyin/Shaoyang): PC -> SJ -> GB -> LR.", "medium"),
    ("The three Yin naming terms (by location on the limb) are:",
     ["Taiyin, Shaoyin, Jueyin", "Yangming, Taiyang, Shaoyang", "Taiyin, Yangming, Shaoyang", "Jueyin, Taiyang, Shaoyin"], "A",
     "Taiyin (Anterior), Shaoyin (Posterior), Jueyin (Middle) - the three Yin position names.", "medium"),
    ("The three Yang naming terms (by location on the limb) are:",
     ["Taiyin, Shaoyin, Jueyin", "Yangming, Taiyang, Shaoyang", "Taiyin, Yangming, Shaoyang", "Jueyin, Taiyang, Shaoyin"], "B",
     "Yangming (Anterior), Taiyang (Posterior), Shaoyang (Middle) - the three Yang position names.", "medium"),
    ("Hand Yin meridians meet Hand Yang meridians where on the body?",
     ["The fingers", "The face", "The toes", "The chest"], "A",
     "Hand Yin meets Hand Yang at the fingers (e.g. LU's branch meets LI1 at the index finger).", "medium"),
    ("Hand Yang meridians meet Foot Yang meridians where on the body?",
     ["The fingers", "The face", "The toes", "The chest"], "B",
     "Hand Yang meets Foot Yang at the face (e.g. LI ends at LI20, ST begins there).", "medium"),
    ("Foot Yang meridians meet Foot Yin meridians where on the body?",
     ["The fingers", "The face", "The toes", "The chest"], "C",
     "Foot Yang meets Foot Yin at the toes (e.g. ST ends at ST45, SP begins at SP1).", "medium"),
    ("Foot Yin meridians meet Hand Yin meridians where on the body, completing the full loop?",
     ["The fingers", "The face", "The toes", "The chest"], "D",
     "Foot Yin meets Hand Yin at the chest - this closes the loop and hands off into the next circuit.", "medium"),
    ("Beyond the 12 Luo points on the primary meridians, which THREE additional collaterals bring the total to 15?",
     ["Du Mai Luo, Ren Mai Luo, Spleen's Great Luo (Dabao)", "LU Luo, SP Luo, HT Luo (duplicated)", "3 unnamed 'extra' meridian branches", "The 3 Yang divergent channels"], "A",
     "15 = 12 primary Luo points + the Luo of Du Mai + the Luo of Ren Mai + the Spleen's Great Luo (Dabao).", "hard"),
    ("Per Dr. Zhang's direct clarification in lecture, if an exam question says 'channels' rather than 'meridians,' you should assume it means:",
     ["Only the 12 Primary Meridians", "Meridians AND Collaterals together - the whole system", "Only the Extraordinary Vessels", "It is interchangeable with 'points'"], "B",
     "A student asked this directly; Dr. Zhang confirmed 'meridians' = the 12 Primary only, while 'channels' is the whole system.", "hard"),
    ("How many Divergent Meridians branch from the 12 Primary Meridians?",
     ["8", "12", "15", "24"], "B",
     "12 Divergent Meridians - one per primary meridian, distributing on chest/abdomen/head and deepening the Zang-Fu relationship (full detail covered later in the course).", "hard"),
    ("How many Muscle (Sinew) Regions and how many Cutaneous Regions exist?",
     ["8 and 8", "12 and 12", "15 and 15", "12 and 15"], "B",
     "12 Muscle/Sinew Regions and 12 Cutaneous Regions - one of each per primary meridian.", "hard"),
    ("How many Extraordinary Vessels are there, and which organ are they most closely tied to?",
     ["6 vessels, tied to the Liver", "8 vessels, tied to the Kidney", "8 vessels, tied to the Spleen", "12 vessels, tied to the Heart"], "B",
     "8 Extraordinary Vessels (Du, Ren, Chong, Dai, Yinwei, Yangwei, Yinqiao, Yangqiao), acting as reservoirs of Qi and Blood closely connected to the Kidney.", "hard"),
    ("Which of the following is TRUE about same-named channels on opposite limbs (e.g. Hand Taiyin LU and Foot Taiyin SP)?",
     ["They have no functional relationship", "They communicate with one another; a problem in one can sometimes be addressed via the other", "They are identical pathways duplicated on the leg", "They only relate to each other during extraordinary vessel activity"], "B",
     "Per lecture: arm and leg channels of the same name communicate with one another - a clinically useful relationship.", "hard"),
    ("Dr. Zhang's Week 1 homework assignment specifically required drawing:",
     ["All 12 meridians at once, in one sitting", "The circulation, direction, and distribution of the Lung Meridian of Hand-Taiyin specifically", "The 8 Extraordinary Vessels", "The Five Shu points of every channel"], "B",
     "The Week 1 homework was to draw the circulation, direction, and distribution of the LU meridian specifically - the same drawing standard applies to every meridian going forward.", "hard"),
    ("Which of the following is NOT one of the three core functions of the meridians?",
     ["Transporting Qi and Blood to nourish tissues", "Resisting (defending against disease, reflecting symptoms)", "Treatment (transmitting needling sensation, regulating deficiency/excess)", "Synthesizing new Qi from food and air"], "D",
     "The three functions are Transporting, Resisting, and Treatment. 'Synthesizing Qi from food and air' is a distractor - that role belongs to Spleen/Stomach digestive theory, not the meridian system itself.", "hard"),
    ("EXCEPT question: All of the following are TRUE about the channel system EXCEPT:",
     ["Meridians run deep; collaterals branch more superficially", "There are 12 Primary Meridians and 15 Collaterals", "The Extraordinary Vessels are each directly paired with one Zang-Fu organ, exactly like the 12 Primary Meridians", "Meridians and Collaterals together form the channel system's core network"], "C",
     "Trap: the Extraordinary Vessels are NOT organ-paired like the 12 Primary Meridians - they act as reservoirs, closely tied to the Kidney but not owned by any single Zang-Fu organ.", "hard"),
    ("Which statement correctly distinguishes 'meridians' from 'collaterals' as Dr. Zhang described them?",
     ["Meridians are superficial branches; collaterals run deep like a river", "Meridians run deep like a river; collaterals are more superficial branches spreading from Luo-connecting points", "There is no functional distinction - the terms are interchangeable in all contexts", "Collaterals outnumber meridians 20 to 12"], "B",
     "Dr. Zhang's river/branch metaphor: meridians (Jing) run deep like a river; collaterals (Luo) are the more superficial branches, spreading from each meridian's Luo-connecting point.", "hard"),
]

assert len(QUIZ1_PRACTICE) == 30

# ============================================================
# COVER PAGE
# ============================================================
new_page()
y = H - 60
setfill(NAVY); c.rect(0, H - 140, W, 140, fill=1, stroke=0)
setfill((1, 1, 1)); c.setFont("Lora-Bold", 26)
c.drawString(ML + 8, y - 40, "WEEK 1 QUIZ KIT")
setfill((0.9, 0.9, 0.92)); c.setFont("Lora-Italic", 12.5)
c.drawString(ML + 8, y - 64, "Channel Theory: Concept, Nomenclature, Flow of Qi - closed book")
setfill((1, 1, 1)); c.setFont("Lora-Italic", 9.5)
c.drawRightString(W - MR - 8, y - 24, EDLABEL)
y -= 150

col_w = (CW - 20) / 2
box_h = 62
setfill(BLUE_TINT); c.rect(ML, y - box_h, col_w, box_h, fill=1, stroke=0)
setstroke(BLUE); c.setLineWidth(2)
c.line(ML, y - box_h, ML, y)
setfill(BLUE); c.setFont("Lora-Bold", 13)
c.drawString(ML + 10, y - 22, "12 PRIMARY MERIDIANS")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawString(ML + 10, y - 38, "3 Circuits | 6 Zang + 6 Fu | Hand/Foot x Yin/Yang")
setfill(GRAY); c.setFont("Lora-Italic", 8.8)
c.drawString(ML + 10, y - 52, "Foundational theory - no individual points yet")

x2 = ML + col_w + 20
setfill(RED_TINT); c.rect(x2, y - box_h, col_w, box_h, fill=1, stroke=0)
setstroke(RED); c.setLineWidth(2)
c.line(x2, y - box_h, x2, y)
setfill(RED); c.setFont("Lora-Bold", 13)
c.drawString(x2 + 10, y - 22, "THE FULL SYSTEM")
setfill(DARK); c.setFont("Lora", 9.5)
c.drawString(x2 + 10, y - 38, "15 Collaterals | 12 Divergent | 12 Sinew | 12 Cutaneous")
setfill(GRAY); c.setFont("Lora-Italic", 8.8)
c.drawString(x2 + 10, y - 52, "8 Extraordinary Vessels")

y -= box_h + 30
setfill(NAVY); c.setFont("Lora-Bold", 12)
setstroke(NAVY); c.setLineWidth(2.2)
c.line(ML - 4, y - 3, ML - 4, y + 13)
c.drawString(ML + 6, y, "Coverage")
y -= 22
setfill(DARK); c.setFont("Lora", 10.5)
c.drawString(ML + 6, y, "10 easier recall questions (counts, direction rules, clock times)")
c.drawRightString(W - MR, y, "Q1-Q10")
y -= 16
c.drawString(ML + 6, y, "10 applied questions (naming convention, circuits, meeting points)")
c.drawRightString(W - MR, y, "Q11-Q20")
y -= 16
c.drawString(ML + 6, y, "10 trap/nuance questions (exceptions, EXCEPT format, exact terminology)")
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
lines = ["Close the book. No notes, no app.", "Take it in one sitting, ~20 min.",
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
score_lines = [("27-30", "Exam ready. This is the foundation - move to Week 2 drilling."),
               ("23-26", "Solid. Re-drill circuits and meeting points."),
               ("18-22", "Re-read the Study Guide's direction/circuit pages."),
               ("Below 18", "Full re-study before building on Week 2 content.")]
yy = y - 28
for score, desc in score_lines:
    setfill(RED); c.setFont("Lora-Bold", 9)
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
setfill(RED); c.setFont("Lora-Italic", 9.5)
c.drawString(ML + 6, y - 16, "30 questions, 10 easy + 10 medium + 10 hard - covers Week 1 channel theory comprehensively.")
setfill(GRAY); c.setFont("Lora-Italic", 9)
c.drawString(ML + 6, y - 30, "Cross-checked against the Week 1 Study Guide's verified content - nothing invented.")

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


SET_LABEL = "Channel Theory  |  no notes"
new_page()
y = H - 46
y = section_bar(y, "Questions 1-15", SET_LABEL, NAVY, size=14)
for i in range(15):
    q, opts, correct, expl, diff = QUIZ1_PRACTICE[i]
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
    q, opts, correct, expl, diff = QUIZ1_PRACTICE[i]
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

for i, (q, opts, correct, expl, diff) in enumerate(QUIZ1_PRACTICE, 1):
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
