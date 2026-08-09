import sys
sys.path.insert(0, "/home/claude/ac300wk6")
from common_remarkable import *

OUT = "/home/claude/ac300wk6/out/AC300_Week6_PrepGuide_reMarkable.pdf"

# Provenance note: Sections A-F + Inter-Quiz (ACQ/MAINT) is Jon's own behavioral-
# interteaching study framework, not sourced from Dr. Zhang's course materials.
# Content WITHIN each section is drawn from and verified against Lecture 6 slides
# (Lecture_61102.pdf, 70 slides) + AC300 Channel Workbook (CAM 4th Ed. / MOA 3rd Ed.).
# Anything not directly confirmed against a source is flagged inline.

c = new_canvas_rm(OUT)
ivory_page(c)

# ============================================================= COVER
set_fill(c, NAVY)
c.rect(0, PAGE_H - 80, PAGE_W, 80, stroke=0, fill=1)
set_fill(c, GOLD_TAB)
c.rect(0, PAGE_H - 83, PAGE_W, 3, stroke=0, fill=1)
set_fill(c, WHITE)
c.setFont("Lora-Bold", 20)
c.drawCentredString(PAGE_W / 2, PAGE_H - 40, "AC300/375 \u00b7 Pre-Lecture Analysis Sheet")
c.setFont("Lora-Italic", 12)
c.drawCentredString(PAGE_W / 2, PAGE_H - 62, "Week 6 \u00b7 Pericardium, San Jiao, Gallbladder & Liver \u00b7 Interteaching Prep Guide")

y = PAGE_H - 108
set_fill(c, RED2)
c.setFont("Lora-BoldItalic", 13)
c.drawCentredString(PAGE_W / 2, y, "Sections A\u2013F + Inter-Quiz")
y -= 15
set_fill(c, GRAY)
c.setFont("Lora", 9.5)
c.drawCentredString(PAGE_W / 2, y, "PC (9) + SJ (23) + GB (44) + LR (14) = 90 points  \u00b7  Middle Circuit complete this week")
y -= 26

y = draw_paragraph_rm(c,
    "This prep guide follows the behavioral interteaching model: complete it BEFORE lecture, using the "
    "Study Guide / Cram Sheet / assigned reading (CAM p.77-82, MOA p.367-370, 387-390, 417-421, 469-472) "
    "as source material. Bring your answers and your Section E confusion points to class \u2014 interteaching "
    "pairs/groups are built to target exactly those gaps.",
    MARGIN, y, CONTENT_W, size=9.5, leading=13.5)
y -= 16

box_top = y
lines_map = [
    "Section Map:",
    "\u2022 A \u2014 Factual Recall (terminology, counts, first/last points, special points)",
    "\u2022 B \u2014 Conceptual Understanding (pathway logic, branches, function)",
    "\u2022 C \u2014 Clinical Application (trap notes, indications, scenarios)",
    "\u2022 D \u2014 Synthesis & Connections (Middle Circuit, prior weeks)",
    "\u2022 E \u2014 Points of Confusion (muddiest-point \u2014 bring to class)",
    "\u2022 F \u2014 Discussion / Pair-Share Prompts",
    "\u2022 Inter-Quiz \u2014 ACQ (new PC/SJ/GB/LR content) + MAINT (retention check, Wk 1\u20135)",
]
box_h = 16 + len(lines_map[1:]) * 15 + 14
callout_box_rm(c, MARGIN, box_top, CONTENT_W, box_h, rgb_fill=LIGHTBLUE)
ty = box_top - 16
set_fill(c, GOLD)
c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN + 12, ty, lines_map[0])
ty -= 15
set_fill(c, BLACK)
c.setFont("Lora", 8.8)
for ln in lines_map[1:]:
    c.drawString(MARGIN + 14, ty, ln)
    ty -= 15
y = box_top - box_h - 20

# Quiz timing note (verified from A+ Routine week-by-week plan)
y = draw_paragraph_rm(c,
    "Quiz timing note: Quiz 4 (given THIS week, in class) covers BL/KI (Week 5) material \u2014 the MAINT "
    "items below reinforce that. Quiz 5 (given next week, Week 7) covers this week's PC/SJ/GB/LR content, "
    "so treat this sheet as direct Quiz 5 prep.",
    MARGIN, y, CONTENT_W, size=8.5, leading=12, color=GRAY)
y -= 10

# Element / channel snapshot table
set_fill(c, NAVY)
c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "This Week's Four Channels")
y -= 14
headers = ["Channel", "Element/Polarity", "Peak", "Pts", "Paired", "Front-Mu", "Back-Shu"]
rows = [
    ("PC \u2014 Pericardium", "Fire (Minister) \u00b7 Yin", "7\u20139 PM", "9", "SJ", "CV17", "BL14"),
    ("SJ \u2014 San Jiao", "Fire (Minister) \u00b7 Yang", "9\u201311 PM", "23", "PC", "CV5", "BL22"),
    ("GB \u2014 Gallbladder", "Wood \u00b7 Yang", "11 PM\u20131 AM", "44", "LR", "GB24", "BL19"),
    ("LR \u2014 Liver", "Wood \u00b7 Yin", "1\u20133 AM", "14", "GB", "LR14", "BL18"),
]
colw = [118, 118, 68, 30, 45, 55, 55]
x0 = MARGIN
set_fill(c, LIGHTBLUE)
c.rect(MARGIN, y - 13, CONTENT_W, 13, stroke=0, fill=1)
set_fill(c, NAVY)
c.setFont("Lora-Bold", 7.6)
xx = x0
for h, w in zip(headers, colw):
    c.drawString(xx + 3, y - 10, h)
    xx += w
y -= 13
for row in rows:
    xx = x0
    accent = MINISTER if row[0].startswith(("PC", "SJ")) else WOOD
    set_fill(c, tint(accent, 0.75))
    c.rect(MARGIN, y - 13, CONTENT_W, 13, stroke=0, fill=1)
    set_fill(c, BLACK)
    c.setFont("Lora", 7.6)
    for val, w in zip(row, colw):
        c.drawString(xx + 3, y - 10, str(val))
        xx += w
    y -= 13
y -= 20

# How to use this sheet
set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "How to Use This Sheet")
y -= 16
steps = [
    ("BEFORE lecture", "Complete Sections A\u2013D from memory using the Study Guide, Cram Sheet, and "
     "assigned reading. Rate your confidence honestly \u2014 the point is to expose gaps now, not in class."),
    ("DURING lecture", "Annotate directly on this sheet as Dr. Zhang covers material. Correct anything "
     "you got wrong in Sections A\u2013D in a different color if possible."),
    ("AFTER lecture", "Complete Section F with your interteaching pair. Run the Inter-Quiz self-check "
     "within 24 hours, and again before Wednesday's Quiz 4 and before Lecture 7."),
]
for phase, desc in steps:
    set_fill(c, RED2); c.setFont("Lora-Bold", 8.5)
    c.drawString(MARGIN, y, phase + ":")
    lbl_w = pdfmetrics.stringWidth(phase + ":  ", "Lora-Bold", 8.5)
    y = draw_paragraph_rm(c, desc, MARGIN + lbl_w, y, CONTENT_W - lbl_w, size=8.5, leading=11.5, color=BLACK)
    y -= 8

y -= 8
hairline_rm(c, MARGIN, y, PAGE_W - MARGIN, rgb=GOLD, w=0.6)
y -= 16

# Source / provenance note
set_fill(c, GRAY); c.setFont("Lora-Bold", 8.5)
c.drawString(MARGIN, y, "Source Note")
y -= 13
y = draw_paragraph_rm(c,
    "This week's channel-fact content is sourced from Lecture_61102.pdf (70-slide deck) and the AC300 Channel "
    "Workbook (CAM 4th Ed. / MOA 3rd Ed.). The Sections A\u2013F + Inter-Quiz interteaching structure is Jon's "
    "own study framework, not part of Dr. Zhang's course materials. Two items below are flagged as unresolved "
    "against source: PC's crossing-point count (0, per slide 70 recap) and GB's crossing-point count (slide 51 "
    "states \"12 points 6 meridians\" but names only 9 points \u2014 confirm with Dr. Zhang).",
    MARGIN, y, CONTENT_W, size=8, leading=11, color=GRAY)

set_fill(c, GRAY)
c.setFont("Lora-Italic", 8)
c.drawCentredString(PAGE_W / 2, 40, "AC300 Pre-Lecture Analysis \u00b7 Week 6 \u00b7 Interteaching format \u00b7 Complete before Lecture 6")
c.showPage()
ivory_page(c)

# ============================================================= SECTION A
y = header_bar_rm(c, "A", "Factual Recall", subtitle="Answer from memory first; check against the Study Guide only after.")
y -= 8
qA = [
    ("How many points on the Pericardium channel? San Jiao channel? Gallbladder channel? Liver channel? "
     "What is the combined total for the week?", 2),
    ("Name the first and last point of PC, of SJ, of GB, and of LR (name + number for each).", 3),
    ("State the element, polarity, and peak two-hour window for all four channels covered this week.", 2),
    ("Name each channel's pertaining organ and connecting organ (PC, SJ, GB, LR).", 2),
    ("Which point is the Confluent point of SJ, and which extraordinary vessel does it open? Same question for GB.", 2),
    ("Name the Front-Mu and Back-Shu point for each of the four channels.", 2),
    ("How many crossing points does SJ have, and with how many other meridians? Name at least six of the actual points.", 2),
    ("How many crossing points does PC have? (Check the Week 6 slide recap list carefully before answering.)", 1),
]
for i, (q, lines) in enumerate(qA, 1):
    y = numbered_question_rm(c, i, q, MARGIN, y, CONTENT_W, lines=lines + 1, gap=17)

y -= 6
box_h = 92
callout_box_rm(c, MARGIN, y, CONTENT_W, box_h, rgb_fill=tint(MINISTER, 0.82))
ty = y - 16
set_fill(c, RED2); c.setFont("Lora-Bold", 9)
c.drawString(MARGIN + 12, ty, "Quick-Reference: Special Points This Week")
ty -= 14
set_fill(c, BLACK); c.setFont("Lora", 8)
refs = [
    "PC: Confluent+Luo PC6 (Yinwei Mai) \u00b7 Yuan-Source+Shu-Stream PC7 \u00b7 Xi-Cleft PC4 \u00b7 He-Sea PC3",
    "SJ: Confluent SJ5 (Yangwei Mai) \u00b7 Luo SJ5 \u00b7 Yuan-Source SJ4 \u00b7 Xi-Cleft SJ7 \u00b7 He-Sea SJ10",
    "GB: Confluent GB41 (Dai Mai) \u00b7 Luo GB37 \u00b7 Yuan-Source GB40 \u00b7 Xi-Cleft GB36 \u00b7 He-Sea+Influential(sinews) GB34",
    "LR: Yuan-Source+Shu-Stream LR3 \u00b7 Luo LR5 \u00b7 Xi-Cleft LR6 \u00b7 He-Sea LR8 \u00b7 Command(face) LR3",
]
for r in refs:
    c.drawString(MARGIN + 12, ty, r)
    ty -= 12.5

footer_rm(c, "PLA Sheet", 1)
c.showPage()
ivory_page(c)

# ============================================================= SECTION B
y = header_bar_rm(c, "B", "Conceptual Understanding", subtitle="Explain the logic, not just the list \u2014 this maps to the running-course quiz format.")
y -= 8
qB = [
    ("Sketch (in words) all 3 branches of the Pericardium channel in order, starting from the chest. "
     "Where does each branch terminate?", 3),
    ("Sketch (in words) all 3 branches of the San Jiao channel. Which branch links SJ to the Gallbladder "
     "channel, and at which point?", 3),
    ("Sketch (in words) all 5 branches/segments of the Gallbladder channel, in the order the lecture "
     "presented them. Which branch is the 'straight portion' that carries most of the numbered points?", 3),
    ("Sketch (in words) all 4 branches of the Liver channel. Which branch links LR back to the Lung "
     "channel, completing the full 12-channel qi cycle?", 3),
    ("Explain the Three Main Circuits framework from this week's review slide: Outer Circuit (Yangming, "
     "Taiyang, Shaoyang), Inner Circuit (Taiyin, Shaoyin), and Middle Circuit (Jueyin). Which two channels "
     "finish the Middle Circuit this week, and why does that make sense given hand-Jueyin runs chest-to-hand "
     "while foot-Jueyin runs foot-to-abdomen?", 4),
    ("Note: this 'Outer/Inner/Middle Circuit' framework (by yin-yang stage) is a DIFFERENT model from the "
     "'Posterior Circuit / Inner Circuit' body-region terminology used in Weeks 1\u20134 for HT/SI/BL/KI. "
     "Do not conflate the two \u2014 explain the difference in your own words.", 3),
]
for i, (q, lines) in enumerate(qB, 1):
    y = numbered_question_rm(c, i, q, MARGIN, y, CONTENT_W, lines=lines, gap=16)

y -= 4
box_h = 60
callout_box_rm(c, MARGIN, y, CONTENT_W, box_h, rgb_fill=LIGHTBLUE)
ty = y - 14
set_fill(c, NAVY); c.setFont("Lora-Bold", 8.5)
c.drawString(MARGIN + 12, ty, "Reminder \u2014 Running-Course Numbering Convention")
ty -= 12
ty = draw_paragraph_rm(c,
    "The lecture slides number each segment of a channel's course sequentially in parentheses, e.g. (1), (2), "
    "(3)... reflecting the exact order Dr. Zhang presents branches on the diagram. Use that numbering when you "
    "sketch a pathway from memory.",
    MARGIN + 12, ty, CONTENT_W - 24, size=7.6, leading=10, color=BLACK)

footer_rm(c, "PLA Sheet", 2)
c.showPage()
ivory_page(c)

# ============================================================= SECTION C
y = header_bar_rm(c, "C", "Clinical Application")
y -= 8
qC = [
    ("A patient presents with nausea, vomiting, and cardiac-type chest discomfort. Which point is described "
     "as the single most important PC point for this presentation, and which extraordinary vessel does it open?", 2),
    ("A patient needs emergency resuscitation (loss of consciousness). Name a PC point and a KI point "
     "traditionally paired for this purpose (recall from Week 5).", 2),
    ("GB21 carries an explicit clinical caution from lecture and workbook. What is it, and what is the "
     "point otherwise used for?", 2),
    ("Name the point that is Influential point for the sinews, and state two clinical uses.", 2),
    ("A patient has one-sided (migraine-type) headache with a bitter taste in the mouth. Which channel's "
     "pathway and internal-organ association explain both symptoms together?", 3),
    ("LR3 is described as the single most important LR point. What does it treat, and what special-point "
     "category makes it useful 'for the face'?", 2),
    ("Name the classic two-point combination ('Four Gates') that combines an LR point with an LI point, "
     "and state its general function.", 2),
]
for i, (q, lines) in enumerate(qC, 1):
    y = numbered_question_rm(c, i, q, MARGIN, y, CONTENT_W, lines=lines, gap=16)

y -= 4
box_h = 50
callout_box_rm(c, MARGIN, y, CONTENT_W, box_h, rgb_fill=tint(WOOD, 0.85))
ty = y - 14
set_fill(c, WOOD); c.setFont("Lora-Bold", 8.5)
c.drawString(MARGIN + 12, ty, "Trap Note")
ty -= 12
ty = draw_paragraph_rm(c,
    "PC (like HT in Week 4) is flagged with ZERO crossing points on the lecture-slide recap \u2014 a favorite "
    "exam trap. Don't assume every channel shares points with others just because SJ and GB have long lists.",
    MARGIN + 12, ty, CONTENT_W - 24, size=7.6, leading=10, color=BLACK)

footer_rm(c, "PLA Sheet", 3)
c.showPage()
ivory_page(c)

# ============================================================= SECTION D
y = header_bar_rm(c, "D", "Synthesis & Connections")
y -= 8
qD = [
    ("Dr. Zhang's Week 6 review slide states this lecture completes the Middle Circuit (Jueyin). Name the "
     "hand-Jueyin and foot-Jueyin channels and briefly state how their directions of flow (chest to hand, "
     "foot to abdomen) fit the general nomenclature rule from Week 1.", 3),
    ("PC/SJ share the Ministerial Fire element with no other channel pair in the course. Compare Ministerial "
     "Fire (PC/SJ) to the Sovereign/Emperor Fire pairing you learned in Week 4 (HT/SI) \u2014 what is the "
     "conceptual difference?", 3),
    ("GB/LR are both Wood-element channels, like ST/SP were Earth in Week 3. Restate what Wood governs "
     "physiologically and how that shows up in GB and LR clinical pearls.", 3),
    ("By end of this week, all 12 primary channels have been introduced. Using the 12-channel circulation-"
     "sequence slide, write the full Qi-flow order from LU through LR from memory.", 4),
    ("Compare SJ's 23-point count and complex 3-branch pathway (hand to head) to another 'long' Yang "
     "channel you already know (e.g. BL, Week 5). What do long Yang channels tend to have in common "
     "(crossing points, syndrome breadth)?", 3),
]
for i, (q, lines) in enumerate(qD, 1):
    y = numbered_question_rm(c, i, q, MARGIN, y, CONTENT_W, lines=lines, gap=16)

y -= 4
box_h = 66
callout_box_rm(c, MARGIN, y, CONTENT_W, box_h, rgb_fill=LIGHTBLUE)
ty = y - 14
set_fill(c, NAVY); c.setFont("Lora-Bold", 8.5)
c.drawString(MARGIN + 12, ty, "Circuit Terminology \u2014 Keep These Straight")
ty -= 12
ty = draw_paragraph_rm(c,
    "Two frameworks use the word 'circuit': (1) the Anterior/Posterior body-region terms from Weeks 1\u20134 "
    "('Posterior Circuit,' also called 'Inner Circuit' on an earlier slide, for HT/SI/BL/KI), and (2) this "
    "week's Outer/Inner/Middle Circuit-by-yin-yang-stage model. Identify which one a question means before answering.",
    MARGIN + 12, ty, CONTENT_W - 24, size=7.6, leading=10, color=BLACK)

footer_rm(c, "PLA Sheet", 4)
c.showPage()
ivory_page(c)

# ============================================================= SECTION E
y = header_bar_rm(c, "E", "Points of Confusion (Muddiest Point)")
y -= 8
y = draw_paragraph_rm(c,
    "Interteaching works because YOUR confusion drives the in-class discussion groups. Be specific \u2014 "
    "\"I don't understand X because Y\" is more useful to your pair than \"I'm confused about SJ.\" Bring "
    "this page to class.",
    MARGIN, y, CONTENT_W, size=9.5, leading=13)
y -= 18
prompts = [
    "The single most confusing pathway detail this week:",
    "The single most confusing point-category / special-points detail this week:",
    "A clinical application I still can't confidently explain:",
    "The part of the Middle Circuit / Three Circuits framework I'm least sure about:",
    "A specific question I want answered in lecture:",
]
for p in prompts:
    set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(MARGIN, y, p)
    y -= 16
    y = write_lines_rm(c, MARGIN + 10, y, CONTENT_W - 10, n=3, gap=22)
    y -= 20
footer_rm(c, "PLA Sheet", 5)
c.showPage()
ivory_page(c)

# ============================================================= SECTION F
y = header_bar_rm(c, "F", "Discussion / Pair-Share Prompts")
y -= 8
y = draw_paragraph_rm(c, "For use in class with your interteaching pair or small group.",
                    MARGIN, y, CONTENT_W, size=9.5, leading=13)
y -= 16
qF = [
    ("Compare your Section E confusion points with your partner's. Where do they overlap? Where do they diverge?", 2),
    ("Teach your partner the 3 PC branches and the 5 GB branches from memory, in order, without notes. "
     "Have them check you against the Study Guide.", 2),
    ("Quiz each other on the crossing-point counts: SJ (10 pts/3 meridians), GB (per the slide's stated "
     "12 pts/6 meridians \u2014 note only 9 are actually named; flag this as unresolved), LR (6 pts/2 meridians). "
     "Which count is hardest to remember and why?", 3),
    ("Discuss: if you were writing a Quiz 5 question designed to catch the 'PC has zero crossing points' "
     "trap (like HT in Week 4), what would it look like?", 2),
    ("Trade Middle Circuit explanations (Section D, Q1) verbally. Does your partner's phrasing make it "
     "click any better than yours did?", 2),
]
for i, (q, lines) in enumerate(qF, 1):
    y = numbered_question_rm(c, i, q, MARGIN, y, CONTENT_W, lines=lines, gap=16)

y -= 4
box_h = 52
callout_box_rm(c, MARGIN, y, CONTENT_W, box_h, rgb_fill=tint(MINISTER, 0.82))
ty = y - 14
set_fill(c, RED2); c.setFont("Lora-Bold", 8.5)
c.drawString(MARGIN + 12, ty, "Pair-Share Facilitation Tip")
ty -= 12
ty = draw_paragraph_rm(c,
    "If your pair finishes early, swap roles for a Section D synthesis question \u2014 have the less-confident "
    "partner explain first, then the other corrects/adds detail. This surfaces gaps neither would catch alone.",
    MARGIN + 12, ty, CONTENT_W - 24, size=7.6, leading=10, color=BLACK)

footer_rm(c, "PLA Sheet", 6)
c.showPage()
ivory_page(c)

# ============================================================= INTER-QUIZ
y = header_bar_rm(c, None, "Inter-Quiz",
               subtitle="ACQ = new PC/SJ/GB/LR content \u00b7 MAINT = retention check, Wk 1\u20135")
y -= 8
y = draw_paragraph_rm(c,
    "Self-score honestly before lecture. MAINT items pull from LU/LI/ST/SP/HT/SI/BL/KI (Weeks 1\u20135) to "
    "keep prior channels active in memory ahead of the Week 7 quiz on this material.",
    MARGIN, y, CONTENT_W, size=9, leading=12.5)
y -= 16

pairs = [
    ("Name the point that is both Confluent AND Luo point on the Pericardium channel, and the extraordinary "
     "vessel it opens.",
     "Name the point that is both Confluent AND Luo point on the Kidney channel, and the extraordinary "
     "vessel it opens. (Week 5)"),
    ("Which SJ point is Confluent, and which extraordinary vessel does it open?",
     "Which SI point is Confluent, and which extraordinary vessel does it open? (Week 4)"),
    ("Which GB point is both He-Sea AND Influential point for the sinews?",
     "Which BL point is both He-Sea AND Command point for the back? (Week 5)"),
    ("Name LR's Yuan-Source point (it shares its number with Shu-Stream \u2014 name both categories).",
     "Name LU's Yuan-Source point (it also shares its number with Shu-Stream). (Week 2)"),
    ("State the Front-Mu point for GB and for LR.",
     "State the Front-Mu point for HT and for SI. (Week 4)"),
    ("How many total points does this week add across all four channels (PC+SJ+GB+LR)?",
     "How many total points did BL+KI add together? (Week 5)"),
    ("Which point is Influential point for the sinews, and which channel is it on?",
     "Name one other Influential point you already know and what it governs. (any prior week)"),
    ("Name the two channels that complete the Middle Circuit (Jueyin) this week.",
     "Name the four channels that make up the Posterior/Inner Circuit from Weeks 1\u20134."),
]
for acq, maint in pairs:
    tag_badge_rm(c, MARGIN, y, "ACQ", MINISTER)
    y2 = draw_paragraph_rm(c, acq, MARGIN + 42, y + 1, CONTENT_W - 42, size=8.8, leading=11.5)
    y = min(y2, y - 12) - 4
    tag_badge_rm(c, MARGIN, y, "MAINT", GOLD)
    y2 = draw_paragraph_rm(c, maint, MARGIN + 50, y + 1, CONTENT_W - 50, size=8.8, leading=11.5, color=GRAY)
    y = min(y2, y - 12) - 12

y -= 4
box_h = 56
callout_box_rm(c, MARGIN, y, CONTENT_W, box_h, rgb_fill=LIGHTBLUE)
ty = y - 16
set_fill(c, NAVY); c.setFont("Lora-Bold", 9)
c.drawString(MARGIN + 12, ty, "Mastery Criterion")
ty -= 14
ty = draw_paragraph_rm(c,
    "Score yourself: count correct ACQ + MAINT answers out of 16 total. Aim for \u226514/16 across three "
    "spaced self-testing sessions (e.g. today, Wednesday before Quiz 4, and the morning of Lecture 7) "
    "before Quiz 5.",
    MARGIN + 12, ty, CONTENT_W - 24, size=8, leading=11, color=BLACK)

footer_rm(c, "PLA Sheet \u00b7 Inter-Quiz", 7)
c.showPage()

c.save()
print("wrote", OUT)
