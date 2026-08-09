import sys
sys.path.insert(0, "/home/claude/ac300wk6")
from common_v2 import *

OUT = "/home/claude/ac300wk6/out/AC300_Week6_PrepGuide_v2_Print.pdf"
TOTAL_PAGES = 10

c = new_canvas(OUT)

# ============================================================= COVER
set_fill(c, GOLD)
c.rect(0, PAGE_H - 5, PAGE_W, 5, stroke=0, fill=1)

y = PAGE_H - 80
set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 12)
c.drawCentredString(PAGE_W / 2, y, "WEEK 6  \u00b7  v1")
y -= 46
set_fill(c, NAVY); c.setFont("Lora", 28)
c.drawCentredString(PAGE_W / 2, y, "PRE-LECTURE ANALYSIS SHEET")
y -= 34
set_fill(c, NAVY); c.setFont("Lora-Italic", 15)
c.drawCentredString(PAGE_W / 2, y, "Pericardium, San Jiao, Gallbladder & Liver Channels")
y -= 28
set_fill(c, GOLD_DARK); c.setFont("Lora-Italic", 11)
c.drawCentredString(PAGE_W / 2, y, "Shou Jueyin  /  Shou Shaoyang  /  Zu Shaoyang  /  Zu Jueyin")
y -= 24
set_fill(c, BLACK); c.setFont("Lora", 10)
c.drawCentredString(PAGE_W / 2, y, "Prof. (Dr.) Vivian Zhang, Ph.D.  |  PC (9) + SJ (23) + GB (44) + LR (14) = 90 Points")
y -= 38

y = purpose_box(c, y, [
    "BEFORE lecture: Complete Sections A\u2013D and pre-lecture case questions. Rate confidence and expectancy honestly.",
    "DURING lecture: Annotate directly on this sheet as Dr. Zhang covers material.",
    "AFTER lecture: Complete Section F within 24 hours. Update confidence, finish the case, run the Inter-Quiz.",
    "NEW THIS WEEK: this lecture completes ALL 12 primary channels \u2014 Section B bridges the full-circuit picture.",
])
y -= 6

cards = [
    ("A", "Learning Targets \u2014 I Can Statements", "Pre/post confidence ratings 1-5 for 11 learning outcomes"),
    ("B", "Activate \u2014 Connect to What You Know", "Bridge from Week 5 BL/KI to PC/SJ/GB/LR; fill-in prompts"),
    ("C", "Vocabulary Pre-Load", "20 key terms: Pinyin, English, space for your definition"),
    ("D", "Anticipatory Questions", "11 questions (PC+SJ+GB+LR); starred = high-challenge/high-yield"),
    ("IQ", "Inter-Quiz: Mid-Study Probe", "16 items, 4 checkpoints; mastery \u2265 14/16 x3"),
    ("E", "Clinical Case \u2014 Mr. Alvarez", "Pre-lecture guessing + post-lecture treatment protocol"),
    ("F", "After-Lecture Synthesis", "Concept map fill-in + synthesis columns + review notes"),
]
col_w = (CONTENT_W - 14) / 2
row_h = 40
gap = 8
positions = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3)]
for (col, row), (letter, title, desc) in zip(positions, cards):
    x = MARGIN + col * (col_w + 14)
    ty = y - row * (row_h + gap)
    set_fill(c, GOLD)
    c.rect(x, ty - row_h, 26, row_h, stroke=0, fill=1)
    set_fill(c, WHITE); c.setFont("Lora-Bold", 10)
    c.drawCentredString(x + 13, ty - row_h / 2 - 3, letter)
    box(c, x + 26, ty, col_w - 26, row_h, CARD_BG)
    set_fill(c, NAVY); c.setFont("Lora", 10.5)
    c.drawString(x + 36, ty - 16, title)
    set_fill(c, GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawString(x + 36, ty - 29, desc)
y -= 4 * (row_h + gap) + 14

y = draw_element_key(c, y)

hairline(c, MARGIN, y, PAGE_W - MARGIN, rgb=GOLD, w=1.2)
y -= 18
set_fill(c, GRAY); c.setFont("Lora", 9)
c.drawCentredString(PAGE_W / 2, y, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")

c.showPage()

# ============================================================= SECTION A
y = section_header(c, "A", "Learning Targets -- I Can Statements")
y = purpose_box(c, y, [
    "Purpose: These outcomes define exactly what you are expected to do after this lecture \u2014 not just know, but perform.",
    "How to use: Before lecture: circle your Pre score honestly. After lecture: circle Post score.",
    "Goal: All 11 targets at 4-5 by end of your Week 6 review session. Below 3 = highest review priority.",
])
y = purpose_box(c, y, [
    "Mindset: Every target below has 3 sessions to reach mastery. A low Pre score or a rough first attempt isn't a "
    "failing grade \u2014 it's today's starting point. Track your Pre-to-Post movement, not a single number.",
])

targets = [
    "Trace the Pericardium meridian (PC1-PC9) from the chest to the tip of the middle finger, naming all 3 branches.",
    "Trace the San Jiao meridian (TE1-TE23) from the ring finger to the outer canthus, naming all 3 branches.",
    "Trace the Gallbladder meridian (GB1-GB44) from the outer canthus to the 4th toe, naming all 5 branches/segments.",
    "Trace the Liver meridian (LR1-LR14) from the great toe to the chest, naming all 4 branches.",
    "Explain the Three Main Circuits framework and state which two circuits are completed by today's lecture "
    "(Outer via Shaoyang, Middle via Jueyin).",
    "State the element, polarity, and peak two-hour window for all four channels covered this week.",
    "Identify high-yield PC/SJ points: PC6, PC7 (Yuan-Source + Ghost Point), SJ5, SJ17, SJ21 -- categories and key indications.",
    "Identify high-yield GB/LR points: GB20, GB21 (FORBIDDEN in pregnancy), GB34, GB40, GB41, LR3, LR8 -- categories and key indications.",
    "Apply the PC-SJ and GB-LR interior-exterior paired relationships: give one clinical example in each direction.",
    "Distinguish Ministerial Fire (PC/SJ) from Sovereign Fire (HT/SI, Week 4), and state each channel's "
    "crossing-point count -- flagging PC's trap (zero).",
    "Distinguish LR13 (Front-Mu of SPLEEN + Hui-Meeting of the Zang organs) from LR14 (Front-Mu of the Liver "
    "itself) -- and explain why LR13 also appears on GB's crossing-point list.",
]
for t in targets:
    y = confidence_row(c, y, t)

y -= 2
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.3)
c.drawString(MARGIN, y, "Quiz 5 covers PC/SJ/GB/LR: same 5-question format + 1 bonus (20 pts). Targets at 4-5 = quiz-ready.")

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 2, TOTAL_PAGES)
c.showPage()

# ============================================================= SECTION B
y = section_header(c, "B", "Activate -- Connect to What You Know")
y = purpose_box(c, y, [
    "Purpose: Activating prior knowledge before new input improves encoding. This section bridges Week 5 to Week 6.",
    "B1: Write whatever you already know \u2014 no wrong answers. B2: Complete each fill-in before lecture.",
])

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B1 . From Week 5 to Today")
y -= 16
y = draw_paragraph(c,
    "Week 5 completed BL/KI \u2014 finishing the Inner Circuit (Taiyin+Shaoyin) and bringing the Outer Circuit to "
    "2 of its 3 yang stages (Yangming, Taiyang) already done. Today adds the final piece of each remaining "
    "circuit: Shaoyang (SJ/GB) completes the Outer Circuit, and Jueyin (PC/LR) completes the Middle Circuit. "
    "After today, all 12 primary channels have been introduced.",
    MARGIN, y, CONTENT_W, size=9.3, leading=12.5)
y -= 4
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.5)
c.drawString(MARGIN, y, "What do you already know about PC, SJ, GB, and LR? Write whatever comes to mind:")
y -= 10
y = write_box(c, y, CONTENT_W, 80, gold_bar=True, fill=CARD_BG, n_lines=4)
y -= 20

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "B2 . Connect the Dots -- complete before lecture")
y -= 20

blanks = [
    ("BL/KI (Week 5) completed the Inner Circuit -> today's SJ/GB completes the", 80, "Circuit."),
    ("PC and LR share the Jueyin stage, making them together the", 80, "Circuit."),
    ("HT/SI (Week 4) is Sovereign Fire -> PC/SJ (this week) is", 80, "Fire."),
    ("LR3 pairs with LI4 (Week 2) to form the classic", 80, "combination."),
    ("SP crosses in front of LR at", 60, "cun above the medial malleolus (Week 3 recall)."),
    ("GB41 opens the Dai Mai -> PC6 (this week's PC point) opens the", 80, "Mai."),
]
for before, bw, after in blanks:
    y = fill_blank_line(c, before, bw, after, MARGIN, y)
    y -= 22

y -= 4
set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "Notes -- other connections you're noticing")
y -= 12
y = write_box(c, y, CONTENT_W, 200, gold_bar=True, fill=CARD_BG, n_lines=9)

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 3, TOTAL_PAGES)
c.showPage()

# ============================================================= SECTION C
y = section_header(c, "C", "Vocabulary Pre-Load -- Define Before Class")
y = purpose_box(c, y, [
    "Purpose: Pre-loading key terms primes semantic memory so lecture content attaches to existing scaffolding.",
    "Before lecture: fill in 'My Definition' with whatever you know or can infer. Blank = learn live.",
])
y = vocab_table_header(c, y)

vocab = [
    ("Shou Jueyin", "Hand Jueyin (PC)", None),
    ("Shou Shaoyang", "Hand Shaoyang (SJ)", None),
    ("Zu Shaoyang", "Foot Shaoyang (GB)", None),
    ("Zu Jueyin", "Foot Jueyin (LR)", None),
    ("Tian Chi \u00b7 PC1", "Celestial Pool", MINISTER),
    ("Nei Guan \u00b7 PC6", "Inner Pass", MINISTER),
    ("Zhong Chong \u00b7 PC9", "Middle Rushing", MINISTER),
    ("Da Ling \u00b7 PC7", "Yuan-Source of PC (Ghost Point)", MINISTER),
    ("Guan Chong \u00b7 TE1", "Gate Rushing", MINISTER),
    ("Wai Guan \u00b7 TE5", "Outer Pass", MINISTER),
    ("Si Zhu Kong \u00b7 TE23", "Silk Bamboo Hollow", MINISTER),
    ("Tong Zi Liao \u00b7 GB1", "Pupil Bone-Hole", WOOD),
    ("Feng Shi \u00b7 GB31", "Wind Market", WOOD),
    ("Yang Ling Quan \u00b7 GB34", "Yang Mound Spring", WOOD),
    ("Zu Qiao Yin \u00b7 GB44", "Foot Portal Yin", WOOD),
    ("Qiu Xu \u00b7 GB40", "Yuan-Source of GB", WOOD),
    ("Da Dun \u00b7 LR1", "Great Mound", WOOD),
    ("Tai Chong \u00b7 LR3", "Supreme Rushing", WOOD),
    ("Qi Men \u00b7 LR14", "Cycle Gate (Front-Mu of Liver)", WOOD),
    ("Zhang Men \u00b7 LR13", "Front-Mu of SP + Hui-Meeting of Zang", WOOD),
]
for py, en, accent in vocab:
    y = vocab_row(c, y, py, en, accent=accent)

y -= 6
set_fill(c, MINISTER)
c.circle(MARGIN + 4, y + 2.5, 3.5, stroke=0, fill=1)
c.setFont("Lora", 7.5)
c.drawString(MARGIN + 12, y, "PC / SJ (Fire, Minister)")
set_fill(c, WOOD)
c.circle(MARGIN + 154, y + 2.5, 3.5, stroke=0, fill=1)
c.drawString(MARGIN + 162, y, "GB / LR (Wood)")
y -= 14
set_fill(c, GRAY); c.setFont("Lora-Italic", 8)
c.drawString(MARGIN, y, "Blank rows below: add any extra terms Dr. Zhang emphasizes in lecture.")
y -= 16
row_h = 20
for i in range(8):
    shaded = (i % 2 == 0)
    row_top = y
    row_bottom = y - row_h
    if shaded:
        box(c, MARGIN, row_top, CONTENT_W, row_h, CARD_BG)
    line_y = row_bottom + 6
    hairline(c, MARGIN, line_y, MARGIN + 170, rgb=(0.7, 0.7, 0.64), w=0.6)
    hairline(c, MARGIN + 190, line_y, MARGIN + 320, rgb=(0.7, 0.7, 0.64), w=0.6)
    hairline(c, MARGIN + 340, line_y, PAGE_W - MARGIN, rgb=(0.7, 0.7, 0.64), w=0.6)
    y = row_bottom

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 4, TOTAL_PAGES)
c.showPage()

# ============================================================= SECTION D (page 1: PC + SJ)
y = section_header(c, "D", "Anticipatory Questions", subtitle="* = high-challenge / high-yield")
header_swatch(c, MINISTER, "FIRE (MINISTER)")
y = purpose_box(c, y, [
    "Purpose: Generating answers before instruction improves retention. Starred items are matched to your growing "
    "skill level \u2014 they're harder because they're the ones most worth the stretch, not just exam bait.",
])

set_fill(c, MINISTER); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Pericardium Meridian -- PC1 to PC9 (9 points | Hand Jueyin | 7-9 PM)")
y -= 18
y = anticipatory_q(c, y, 1, True, "Origin & Branches",
                   "PC starts at the chest, connecting successively with the upper, middle, and lower jiao. "
                   "Describe all 3 branches in order.", accent=MINISTER)
y = anticipatory_q(c, y, 2, False, "First & Last Point",
                   "Name PC1 and PC9 with their locations.", accent=MINISTER)
y = anticipatory_q(c, y, 3, True, "PC6 -- The Key Point",
                   "What extraordinary vessel does PC6 open, and what 3 clinical presentations is it used for?", accent=MINISTER)

set_fill(c, MINISTER); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "San Jiao Meridian -- TE1 to TE23 (23 points | Hand Shaoyang | 9-11 PM)")
y -= 18
y = anticipatory_q(c, y, 4, True, "The Three Branches",
                   "Sketch all 3 branches of SJ. Which branch links SJ to the Gallbladder channel, and at which point?", accent=MINISTER)

y -= 4
box_h = 66
set_fill(c, tint(MINISTER, 0.85))
c.rect(MARGIN, y - box_h, CONTENT_W, box_h, stroke=0, fill=1)
ty = y - 14
set_fill(c, MINISTER); c.setFont("Lora-Bold", 8.8)
c.drawString(MARGIN + 10, ty, "Also High-Yield This Week (per your A+ Routine)")
ty -= 13
set_fill(c, BLACK); c.setFont("Lora", 8)
c.drawString(MARGIN + 10, ty, "SJ17 (Yifeng) / SJ21 (Ermen): ear-region cluster \u2014 deafness, tinnitus, ear pain/discharge.")
ty -= 12
c.drawString(MARGIN + 10, ty, "GB20 (Fengchi, next page): headache, one-sided headache, dizziness, insomnia.")
ty -= 12
c.drawString(MARGIN + 10, ty, "GB21 (Jianjing, next page): FORBIDDEN in pregnancy \u2014 same trap category as LI4 / SP6 / BL60 / BL67.")
y -= box_h + 12

set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "Notes / Sketch Space")
y -= 12
y = write_box(c, y, CONTENT_W, 80, gold_bar=True, fill=CARD_BG, n_lines=3)

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 5, TOTAL_PAGES)
c.showPage()

# ============================================================= SECTION D (page 2: SJ cont + GB + LR)
y = section_header(c, "D", "Anticipatory Questions (continued)")
header_swatch(c, WOOD, "WOOD")

y = anticipatory_q(c, y, 5, True, "Crossing Points",
                   "SJ has 10 crossing points across 3 meridians. Name at least 4 of the actual points.", accent=MINISTER)
y = anticipatory_q(c, y, 6, False, "SJ5 -- The Confluent Point",
                   "What extraordinary vessel does SJ5 open?", accent=MINISTER)

set_fill(c, WOOD); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Gallbladder Meridian -- GB1 to GB44 (44 points | Foot Shaoyang | 11 PM-1 AM)")
y -= 18
y = anticipatory_q(c, y, 7, True, "The Five Branches",
                   "Sketch all 5 segments of GB's pathway. Which is the 'straight portion' that carries most of "
                   "the numbered points?", accent=WOOD)
y = anticipatory_q(c, y, 8, False, "GB21 Caution",
                   "What explicit clinical caution applies to GB21, and what is the point otherwise used for?", accent=WOOD)
y = anticipatory_q(c, y, 9, True, "GB34 -- The Influential Point",
                   "What tissue is GB34 Influential for, and what 2 conditions does it treat?", accent=WOOD)

set_fill(c, WOOD); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Liver Meridian -- LR1 to LR14 (14 points | Foot Jueyin | 1-3 AM)")
y -= 18
y = anticipatory_q(c, y, 10, True, "LR3 -- The Most Important LR Point",
                   "What does LR3 treat, and what classic 2-point combination pairs it with LI4?", accent=WOOD)
y = anticipatory_q(c, y, 11, True, "LR13 vs LR14 -- Don't Mix These Up",
                   "LR13 and LR14 are both special points on the Liver channel, but neither is a simple "
                   "'Liver Front-Mu.' State exactly what each one is, and why LR13 also shows up on GB's "
                   "crossing-point list from Q7's slide.", accent=WOOD)

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 6, TOTAL_PAGES)
c.showPage()

# ============================================================= IQ (Inter-Quiz)
y = section_header(c, "IQ", "Inter-Quiz -- Mid-Study Probe", subtitle="(checkpoint format)")
y = purpose_box(c, y, [
    "Purpose: Spaced retrieval is the single most evidence-based study technique. Flow theory addition: you "
    "self-check after every 4 items instead of waiting until the end \u2014 a tighter feedback loop keeps difficulty "
    "matched to skill.",
    "Mastery: \u2265 14/16 across 3 separate sessions on different days.",
])
set_fill(c, GRAY); c.setFont("Lora", 8.5)
c.drawString(MARGIN, y, "Date: ______________   Start: ______   End: ______   Session score: ___/16")
y -= 20

y = checkpoint_header(c, y, 1, "1-4")
qs = [
    (1, "ACQ", "PC has ___ points; SJ has ___ points."),
    (2, "MAINT", "HT has ___ pts; SI has ___ pts. (Week 4)"),
    (3, "ACQ", "First point of PC: name + location."),
    (4, "ACQ", "First point of SJ: name + location."),
]
for n, tag, t in qs:
    y = checkpoint_item(c, y, n, tag, t)
y = selfcheck_line(c, y, 4)

y = checkpoint_header(c, y, 2, "5-8")
qs = [
    (5, "ACQ", "PC6 (Neiguan): category + primary use."),
    (6, "ACQ", "SJ5 (Waiguan): category + why it treats exterior wind-heat."),
    (7, "ACQ", "GB34 (Yanglingquan): category + primary function."),
    (8, "ACQ", "LR3 (Taichong): which 2 special-point categories does it hold?"),
]
for n, tag, t in qs:
    y = checkpoint_item(c, y, n, tag, t)
y = selfcheck_line(c, y, 4)

y = checkpoint_header(c, y, 3, "9-12")
qs = [
    (9, "ACQ", "GB41 opens which extraordinary vessel?"),
    (10, "ACQ", "SJ has ___ crossing points across ___ meridians."),
    (11, "ACQ", "GB's crossing-point slide states ___ points / ___ meridians, but only ___ are actually named."),
    (12, "ACQ", "LR13 vs LR14: which is Front-Mu of Liver, and which is Front-Mu of SP + Hui-Meeting of Zang?"),
]
for n, tag, t in qs:
    y = checkpoint_item(c, y, n, tag, t)
y = selfcheck_line(c, y, 4)

y = checkpoint_header(c, y, 4, "13-16")
qs = [
    (13, "MAINT", "Direction of qi flow in hand-yin meridians (Week 1 rule)?"),
    (14, "MAINT", "Direction of qi flow in foot-yang meridians (Week 1 rule)?"),
    (15, "MAINT", "PC clock: ___PM-___PM. LR clock: ___AM-___AM."),
    (16, "MAINT", "Name the Confluent point of KI and the extraordinary vessel it opens. (Week 5)"),
]
for n, tag, t in qs:
    y = checkpoint_item(c, y, n, tag, t)
y = selfcheck_line(c, y, 4)

y -= 4
set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "Prediction Notes -- jot your answers before checking the key")
y -= 12
y = write_box(c, y, CONTENT_W, 120, gold_bar=True, fill=CARD_BG, n_lines=5)

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 7, TOTAL_PAGES)
c.showPage()

# ============================================================= IQ Answer Key
y = section_header(c, "IQ", "Inter-Quiz Answer Key", subtitle="check each block right after attempting it")

answers = [
    "9; 23",
    "9; 19",
    "PC1 Tianchi \u2014 4th ICS, 1 cun lateral to the nipple",
    "TE1 Guanchong \u2014 lateral side of the ring finger",
    "Luo point; opens Yinwei Mai; nausea, vomiting, cardiac-type chest pain",
    "Xi-Cleft; treats acute exterior wind-heat / fever with chills",
    "He-Sea + Influential (sinews); knee/hip pain, sinew disorders",
    "Yuan-Source + Shu-Stream",
    "Dai Mai (Girdle Vessel)",
    "10 crossing points; 3 meridians",
    "12 points / 6 meridians stated on slide; only 9 actually named \u2014 unresolved, confirm with Dr. Zhang",
    "LR14 = Front-Mu of the Liver; LR13 = Front-Mu of the Spleen + Hui-Meeting of the Zang organs",
    "Chest to hand",
    "Head to foot",
    "PC 7-9 PM; LR 1-3 AM",
    "KI6 \u2014 opens Yinqiao Mai",
]
set_fill(c, BLACK); c.setFont("Lora", 9.5)
for i, a in enumerate(answers, 1):
    set_fill(c, BLACK); c.setFont("Lora-Bold", 9.5)
    c.drawString(MARGIN, y, f"{i}.")
    c.setFont("Lora", 9.5)
    y = draw_paragraph(c, a, MARGIN + 22, y, CONTENT_W - 22, size=9.5, leading=13)
    y -= 3

y -= 10
set_fill(c, GRAY); c.setFont("Lora-Italic", 8.5)
c.drawString(MARGIN, y, "Session 1: ___/16    Session 2: ___/16    Session 3: ___/16    Criterion met (\u226514/16 x3): [ ]")

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 8, TOTAL_PAGES)
c.showPage()

# ============================================================= SECTION E
y = section_header(c, "E", "Clinical Case -- Apply It Before & After")
y = purpose_box(c, y, [
    "Purpose: Case-based reasoning bridges textbook knowledge to clinical reality. Struggling before lecture is the point.",
])

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Case Vignette: Mr. Alvarez, 45 years old")
y -= 16
y = draw_paragraph(c,
    "Mr. Alvarez is a 45-year-old accountant presenting with a 3-week history of irritability and one-sided "
    "(temporal) headache. He reports a bitter taste in the mouth, rib-side/hypochondriac distention that "
    "worsens with stress, and occasional dizziness. In the days before tax deadlines he also notices mild "
    "chest tightness and anxious palpitations. Tongue red on the sides with a thin yellow coating. Pulse wiry.",
    MARGIN, y, CONTENT_W, size=9.3, leading=12.5)
y -= 6

set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "Pre-Lecture Questions")
y -= 16
set_fill(c, BLACK); c.setFont("Lora", 9)
c.drawString(MARGIN + 8, y, "PRE Q1: Which channel(s) are most likely involved? List the specific signs that led you there.")
y -= 8
y = write_box(c, y, CONTENT_W - 8, 40, x=MARGIN + 8, n_lines=2)
y -= 16
set_fill(c, BLACK); c.setFont("Lora", 9)
c.drawString(MARGIN + 8, y, "PRE Q2: The bitter taste and rib-side distention point to internal-organ dysfunction of which Fu organ?")
y -= 8
y = write_box(c, y, CONTENT_W - 8, 40, x=MARGIN + 8, n_lines=2)
y -= 16
set_fill(c, BLACK); c.setFont("Lora", 9)
c.drawString(MARGIN + 8, y, "PRE Q3: The pre-deadline chest tightness and palpitations suggest involvement of which additional")
y -= 12
c.drawString(MARGIN + 8, y, "channel from this week?")
y -= 8
y = write_box(c, y, CONTENT_W - 8, 40, x=MARGIN + 8, n_lines=2)
y -= 22

set_fill(c, GOLD_DARK); c.setFont("Lora-Bold", 9.5)
c.drawString(MARGIN, y, "Post-Lecture Questions (within 24 hrs)")
y -= 16
set_fill(c, BLACK); c.setFont("Lora", 9)
c.drawString(MARGIN + 8, y, "POST Q1: Name 3 GB/LR points for Mr. Alvarez's protocol -- code, category, one-sentence")
y -= 12
c.drawString(MARGIN + 8, y, "justification each.")
y -= 8
y = write_box(c, y, CONTENT_W - 8, 56, x=MARGIN + 8, n_lines=3)
y -= 16
set_fill(c, BLACK); c.setFont("Lora", 9)
c.drawString(MARGIN + 8, y, "POST Q2: Include a PC point for the stress-related chest tightness. Apply the paired PC-SJ logic")
y -= 12
c.drawString(MARGIN + 8, y, "with a specific point.")
y -= 8
y = write_box(c, y, CONTENT_W - 8, 56, x=MARGIN + 8, n_lines=3)

footer(c, "AC300/AC375 | Week 6 | PC/SJ/GB/LR Channels | VUIM Summer 2026", 9, TOTAL_PAGES)
c.showPage()

# ============================================================= SECTION F
y = section_header(c, "F", "After-Lecture Synthesis & Self-Monitoring")
y = purpose_box(c, y, [
    "When: Complete within 24 hrs \u2014 optimal consolidation window. Fill without notes first; gaps are data, not failure.",
])

col_w3 = (CONTENT_W - 24) / 3
headers3 = ["I Can Now Confidently...", "Still Unclear -- Review...", "Connected to Other Learning..."]
for i, h in enumerate(headers3):
    x = MARGIN + i * (col_w3 + 12)
    set_fill(c, NAVY); c.setFont("Lora-Bold", 9.5)
    c.drawString(x, y, h)
y -= 16
top3 = y
for i in range(3):
    x = MARGIN + i * (col_w3 + 12)
    write_box(c, top3, col_w3, 130, x=x, gold_bar=True, fill=CARD_BG, n_lines=7)
y = top3 - 130 - 22

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Concept Map -- PC/SJ/GB/LR Quick Review")
y -= 18
lines = [
    "PC - Pericardium (Zang/Yin): ___ pts   Clock ___-___ PM   Dir ___ -> ___",
    "SJ - San Jiao (Fu/Yang): ___ pts   Clock ___-___ PM   Dir ___ -> ___",
    "GB - Gallbladder (Fu/Yang): ___ pts   Clock ___ PM-___ AM   Dir ___ -> ___",
    "LR - Liver (Zang/Yin): ___ pts   Clock ___-___ AM   Dir ___ -> ___",
    "PC start: PC1 Tianchi (___________)     PC end: PC9 Zhongchong (___________)",
    "PC6 opens: ___________ Vessel     SJ5 opens: ___________ Vessel     GB41 opens: ___________ Vessel",
    "GB34: Influential for ___________          LR3: Command point for ___________",
]
set_fill(c, BLACK); c.setFont("Lora", 9.3)
for ln in lines:
    c.drawString(MARGIN, y, ln)
    y -= 16
y -= 6

set_fill(c, NAVY); c.setFont("Lora-Bold", 10.5)
c.drawString(MARGIN, y, "Review Notes -- Insights, Connections & Questions for Dr. Zhang")
y -= 12
y = write_box(c, y, CONTENT_W, 105, gold_bar=True, fill=CARD_BG, n_lines=6)
y -= 20

set_fill(c, GRAY); c.setFont("Lora-Italic", 8)
c.drawString(MARGIN, y, "AC300 Week 6 Pre-Lecture Analysis Sheet v1 | Sources: Dr. Vivian Zhang | CAM 4th ed. | Manual of Acupuncture | VUIM Summer 2026")

c.showPage()
c.save()
print("wrote", OUT)
