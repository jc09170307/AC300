"""Week 9 -- Acupuncture Points: General Functions & Categories + Final Exam
Master Review + Clinical Evidence. Data sourced and verified against
2026AC300Lecture_9Vivian.pdf (86 slides, current-year deck, CONFIRMED LIVE
per in-class transcript AC300_Week_9_Transcript.txt) and cross-checked
against the prior-year deck Lecture_9_Vivian1125.pdf (76 slides). Meeting
(Crossing) Points table sourced from Lecture_9Meeting_Points_List_.pdf
(MOA-style appendix table, pp.52-55).

THIS WEEK IS FINAL-EXAM REVIEW WEEK. Per the transcript and both decks'
own "For Next Week" slide: next week is the comprehensive final exam
(material from Weeks 1-9), no new quiz or homework this week.

CONFIRMATION -- resolves a flag carried over from Week 8:
Week 8's materials flagged the Gallbladder/Liver collateral + divergent-
channel narration and ALL 12 Muscle Region / Cutaneous Region slides as
"self-study, not reached live" (Dr. Zhang had said she would pick these up
"next week" from the middle circuit). The Week 9 slide deck's own agenda
slide (slide 3: "Review -- Collaterals, Divergent Channels, Muscle/Sinew
channels; 12 Cutaneous regions") and the Week 9 transcript confirm this
content WAS delivered live this week. The [self-study] flags on GB/LR
collateral, divergent, and muscle-region content, and on all 12 Cutaneous
Regions, are treated as RESOLVED as of this week -- see CONFIRMATION_NOTE.
"""

NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.10, 0.10, 0.10)
GRAY = (0.40, 0.40, 0.40)

# Accent colors -- consistent with the course-wide element system (never
# gray/purple fallback for a "real" category)
ACCENT_FIVESHU = (0.55, 0.20, 0.55)      # muted purple/violet -- Five Shu Points (new master treatment)
ACCENT_CONFLUENT = (0.16, 0.44, 0.46)    # slate teal -- Eight Confluent Points
ACCENT_LUO = (0.55, 0.38, 0.16)          # amber-brown -- 15 Collaterals
ACCENT_MEETING = (0.75, 0.20, 0.16)      # deep red -- Meeting/Crossing Points
ACCENT_EXAM = (0.114, 0.227, 0.369)      # navy -- Final Exam Master Review
ACCENT_CLINICAL = (0.20, 0.48, 0.27)     # green -- Clinical Evidence
ACCENT_MIDDLE = (0.85, 0.42, 0.38)       # coral -- Ministerial Fire (PC/SJ)
ACCENT_MIDDLE_WOOD = (0.20, 0.48, 0.27)  # green -- Wood (GB/LR)
ACCENT_OUTER = (0.616, 0.478, 0.216)     # amber/ochre -- anterior circuit
ACCENT_INNER = (0.75, 0.20, 0.16)        # deep red -- posterior circuit (Fire half)

CONFIRMATION_NOTE = (
    "CONFIRMED this week: Week 8's materials flagged the GB/LR collateral + divergent-channel "
    "narration and all 12 Muscle Region / Cutaneous Region slides as \u201cself-study, not reached live\u201d "
    "(Dr. Zhang said she would cover the middle circuit \u201cnext week\u201d). The Week 9 deck's own agenda "
    "(slide 3) and the Week 9 live transcript confirm this content WAS delivered live this week -- "
    "GB/LR collaterals, GB/LR divergent channels, and all 12 Muscle + 12 Cutaneous Regions are no "
    "longer self-study. Full diagrams for GB/LR muscle regions are included below; see the Week 8 "
    "Study Guide for the complete diagram set covering the anterior and posterior circuits."
)

HOMEWORK_QUIZ_NOTE = (
    "CONFIRMED via both the live transcript and the 2026 slide deck's own final slide: NEXT WEEK IS "
    "THE COMPREHENSIVE FINAL EXAM (material from Weeks 1-9, 30 questions per Dr. Zhang's verbal "
    "answer in class). No new quiz or homework was assigned this week -- Dr. Zhang stated in lecture "
    "that Homework 5 (from Week 7/8) was still outstanding for some students and reminded the class "
    "to submit it before the final, since grades close after the exam. This Quiz Kit and Cram Sheet "
    "are self-test review material for that comprehensive final, not a stand-in for a new graded quiz."
)

READING_NOTE = (
    "No new CAM or MOA reading pages are assigned for Week 9 in the slide deck or transcript. Dr. "
    "Zhang's own instruction is to \"review according to the slide I prepared\" -- i.e., the Week 9 "
    "deck itself, plus cumulative review of all prior weeks' lecture notes and reading assignments, "
    "is the assigned final-exam preparation material."
)

# ---------------------------------------------------------------------------
# ACUPOINT CATEGORIES -- this week's organizing framework (slide 46, 2026 deck)
# ---------------------------------------------------------------------------
ACUPOINT_DEFINITION = (
    "Acupoints are specific sites on the human body where the Qi and Blood of the Zang-Fu organs and "
    "meridians are transported and infused. They also serve as reflection points for diseases and "
    "stimulation points for treatment."
)
ACUPOINT_NAME_CATEGORIES = ["Fourteen Meridian Point", "Extra Point", "Ouch (Ashi) Point"]
ACUPOINT_PHYSIO_FUNCTION = "Infusion of Qi and Blood, nourishing the entire body (Physiology)."
ACUPOINT_PATHO_FUNCTION = "Clearing the Meridians and Harmonizing Yin and Yang (Pathology)."
ACUPOINT_APPLICATION_CATEGORIES = [
    ("15 Collaterals", "Where a Luo-vessel branches off to its paired meridian.", ACCENT_LUO),
    ("Eight Confluent Points", "Connect the 8 Extraordinary Vessels to the 12 Regular Meridians.", ACCENT_CONFLUENT),
    ("Five Shu (Transport) Points", "5 points per primary meridian, distal to elbow/knee -- 60 points total.", ACCENT_FIVESHU),
]

# ---------------------------------------------------------------------------
# FIVE SHU POINTS -- master table, all 12 meridians x 5 points (slides 50-55)
# ---------------------------------------------------------------------------
FIVE_SHU_DEFINITION = (
    "The term \u2018Five Shu Points\u2019 (Wu Shu Xue) collectively refers to a specific group of five "
    "acupoints on each of the twelve main Meridians, situated distal to the elbows and knees. They are "
    "individually named Jing-Well (Jing), Ying-Spring (Ying), Shu-Stream (Shu), Jing-River (Jing), and "
    "He-Sea (He)."
)
FIVE_SHU_ROWS = [
    ("Jing-Well", "\u201cWhere it emerges is the Jing-Well\u201d", "Tips of fingers and toes",
     "First aid, clearing heat, consciousness disorders"),
    ("Ying-Spring", "\u201cWhere it flows is the Ying-Spring\u201d", "Before the MCP/MTP joints",
     "Feverish diseases, heat-related disorders"),
    ("Shu-Stream", "\u201cWhere it pours is the Shu-Stream\u201d", "After the MCP/MTP joints",
     "Heaviness in the body, pain/stiffness in joints"),
    ("Jing-River", "\u201cWhere it travels is the Jing-River\u201d", "Forearms or lower legs",
     "Externally contracted diseases (colds, flu), meridian regulation"),
    ("He-Sea", "\u201cWhere it enters is the He-Sea\u201d", "Near the elbow or knee joints",
     "Disorders of the six Fu (hollow) organs"),
]
FIVE_SHU_CLASSIC = (
    "Classic of Difficult Questions, Ch. 68: \u201cThe well points govern fullness below the heart, the "
    "spring points govern fever, the stream points govern heaviness of the body and joint pain, the "
    "river points govern asthma, cough, chills, and fever, and the sea points govern rebellious qi and "
    "diarrhea.\u201d"
)

# Master table: meridian -> [Jing-Well, Ying-Spring, Shu-Stream, Jing-River, He-Sea]
FIVE_SHU_MASTER = [
    # Anterior (External/Outer) Cycle -- LU/LI/ST/SP
    dict(meridian="Lung (LU)", abbr="LU", cycle="Anterior", accent=ACCENT_OUTER,
         pts=["Shaoshang LU11", "Yuji LU10", "Taiyuan LU9", "Jingqu LU8", "Chize LU5"]),
    dict(meridian="Large Intestine (LI)", abbr="LI", cycle="Anterior", accent=ACCENT_OUTER,
         pts=["Shangyang LI1", "Erjian LI2", "Sanjian LI3", "Yangxi LI5", "Quchi LI11"]),
    dict(meridian="Stomach (ST)", abbr="ST", cycle="Anterior", accent=ACCENT_OUTER,
         pts=["Lidui ST45", "Neiting ST44", "Xiangu ST43", "Jiexi ST41", "Zusanli ST36"]),
    dict(meridian="Spleen (SP)", abbr="SP", cycle="Anterior", accent=ACCENT_OUTER,
         pts=["Yinbai SP1", "Dadu SP2", "Taibai SP3", "Shangqiu SP5", "Yinlingquan SP9"]),
    # Posterior (Internal/Inner) Cycle -- HT/SI/BL/KI
    dict(meridian="Heart (HT)", abbr="HT", cycle="Posterior", accent=ACCENT_INNER,
         pts=["Shaochong HT9", "Shaofu HT8", "Shenmen HT7", "Lingdao HT4", "Shaohai HT3"]),
    dict(meridian="Small Intestine (SI)", abbr="SI", cycle="Posterior", accent=ACCENT_INNER,
         pts=["Shaoze SI1", "Qiangu SI2", "Houxi SI3", "Yanggu SI5", "Xiaohai SI8"]),
    dict(meridian="Bladder (BL)", abbr="BL", cycle="Posterior", accent=ACCENT_INNER,
         pts=["Zhiyin BL67", "Zutonggu BL66", "Shugu BL65", "Kunlun BL60", "Weizhong BL40"]),
    dict(meridian="Kidney (KI)", abbr="KI", cycle="Posterior", accent=ACCENT_INNER,
         pts=["Yongquan KI1", "Rangu KI2", "Taixi KI3", "Fuliu KI7", "Yingu KI10"]),
    # Middle (Lateral) Cycle -- PC/SJ/GB/LR
    dict(meridian="Pericardium (PC)", abbr="PC", cycle="Middle", accent=ACCENT_MIDDLE,
         pts=["Zhongchong PC9", "Laogong PC8", "Daling PC7", "Jianshi PC5", "Quze PC3"]),
    dict(meridian="Triple Energizer (SJ/TE)", abbr="SJ", cycle="Middle", accent=ACCENT_MIDDLE,
         pts=["Guanchong SJ1", "Yemen SJ2", "Zhongzhu SJ3", "Zhigou SJ6", "Tianjing SJ10"]),
    dict(meridian="Gallbladder (GB)", abbr="GB", cycle="Middle", accent=ACCENT_MIDDLE_WOOD,
         pts=["Zuqiaoyin GB44", "Xiaxi GB43", "Zulinqi GB41", "Yangfu GB38", "Yanglingquan GB34"]),
    dict(meridian="Liver (LR)", abbr="LR", cycle="Middle", accent=ACCENT_MIDDLE_WOOD,
         pts=["Dadun LR1", "Xingjian LR2", "Taichong LR3", "Zhongfeng LR4", "Ququan LR8"]),
]

FIVE_SHU_YUAN_NOTE = (
    "Yin meridians have no separate Yuan-Source point -- the Shu-Stream point IS the Yuan point "
    "(e.g., Taiyuan LU9 is both Shu-Stream and Yuan for the Lung). Yang meridians have a 6th, "
    "separate Yuan-Source point beyond the 5 Shu points (e.g., Chongyang ST42 for the Stomach)."
)

# ---------------------------------------------------------------------------
# EIGHT CONFLUENT POINTS -- detailed cards (slides 48-49, 2026 deck). This
# content was already built in Week 8 (CONFLUENT_DETAIL); reproduced here in
# the richer card format Week 9's deck uses, for a standalone consolidated
# treatment alongside Five Shu and Meeting Points.
# ---------------------------------------------------------------------------
CONFLUENT_DEFINITION = (
    "Confluent points are special acupuncture points that connect the Eight Extraordinary Vessels "
    "with the Twelve Regular Meridians. Function: helping to regulate the body's energy, connect "
    "related meridians, and treat specific patterns."
)
CONFLUENT_POINTS = [
    dict(point="Houxi (SI 3)", vessel="Du Vessel", partner="Shenmai (BL 62)", accent=ACCENT_INNER,
         location="On the ulnar side of the hand, proximal to the 5th metacarpophalangeal joint, at "
                  "the border of the red and white skin.",
         function="Benefits the spine and neck; clears heat; treats febrile disease and back pain."),
    dict(point="Lieque (LU 7)", vessel="Ren Vessel", partner="Zhaohai (KI 6)", accent=ACCENT_OUTER,
         location="On the radial forearm, 1.5 cun proximal to the wrist crease, superior to the "
                  "styloid process of the radius.",
         function="Releases the exterior, benefits the throat and lungs, and regulates the Ren Vessel."),
    dict(point="Gongsun (SP 4)", vessel="Chong Vessel", partner="Neiguan (PC 6)", accent=ACCENT_OUTER,
         location="On the medial foot, distal and inferior to the base of the 1st metatarsal bone.",
         function="Harmonizes the middle jiao, regulates the Chong Vessel, and treats abdominal or "
                  "menstrual disorders."),
    dict(point="Zulinqi (GB 41)", vessel="Dai Vessel", partner="Waiguan (SJ 5)", accent=ACCENT_MIDDLE_WOOD,
         location="On the dorsum of the foot, distal to the junction of the 4th and 5th metatarsal bones.",
         function="Spreads Liver qi, regulates the Dai Vessel, benefits the breasts, and treats pelvic "
                  "or lateral-body pain."),
    dict(point="Zhaohai (KI 6)", vessel="Yin Qiao Vessel", partner="Lieque (LU 7)", accent=ACCENT_INNER,
         location="In the depression directly below the medial malleolus.",
         function="Nourishes yin, benefits the throat, regulates sleep; governs movement."),
    dict(point="Shenmai (BL 62)", vessel="Yang Qiao Vessel", partner="Houxi (SI 3)", accent=ACCENT_INNER,
         location="In the depression directly below the lateral malleolus.",
         function="Regulates the Yang Qiao Vessel, benefits the eyes, calms the spirit, and governs "
                  "motor function."),
    dict(point="Neiguan (PC 6)", vessel="Yin Wei Vessel", partner="Gongsun (SP 4)", accent=ACCENT_MIDDLE,
         location="2 cun proximal to the wrist crease, between the tendons of palmaris longus and "
                  "flexor carpi radialis.",
         function="Opens the chest, regulates the Heart, calms the spirit, harmonizes the Stomach, and "
                  "relieves nausea."),
    dict(point="Waiguan (SJ 5)", vessel="Yang Wei Vessel", partner="Zulinqi (GB 41)", accent=ACCENT_MIDDLE,
         location="2 cun proximal to the dorsal wrist crease, between the radius and ulna.",
         function="Releases the exterior, clears heat, benefits the head and ears, and relieves pain "
                  "along the yang channels."),
]
CONFLUENT_PAIR_NOTE = (
    "The 8 points form 4 master couples (each couple treats a shared body region): Houxi+Shenmai "
    "(inner canthus, ear, shoulder, neck -- Yang); Lieque+Zhaohai (lung, throat, chest -- Yin); "
    "Gongsun+Neiguan (heart, chest, stomach -- Yin); Zulinqi+Waiguan (outer canthus, ear, cheek, neck, "
    "shoulder -- Yang)."
)

# ---------------------------------------------------------------------------
# 15 COLLATERALS -- summary table (slides 31-36, 2026 deck). Full detailed
# treatment (clinical indications, diagrams) lives in the Week 8 Decoder;
# this is the consolidated master table for cumulative final-exam review.
# ---------------------------------------------------------------------------
LUO_DEFINITION = (
    "The twelve Primary Meridians and the Conception and Governor Vessels each give off a collateral "
    "branch, totaling fifteen when combined with the major collateral of the Spleen -- collectively "
    "known as the fifteen collaterals. These are named after the acupoints from which they originate."
)
LUO_COURSE = (
    "The twelve collateral channels branch out from the Luo-Connecting points of their respective "
    "meridians and travel toward their internally-externally related paired meridians. The major "
    "collateral channels of the Ren, Du, and Spleen meridians branch out from their own Luo-Connecting "
    "points, spreading across the abdomen, back of the head, and chest-rib regions."
)
LUO_MASTER = [
    dict(cycle="Anterior", meridian="Lung", abbr="LU", point="Lieque LU7", partner="Large Intestine", accent=ACCENT_OUTER),
    dict(cycle="Anterior", meridian="Large Intestine", abbr="LI", point="Pianli LI6", partner="Lung", accent=ACCENT_OUTER),
    dict(cycle="Anterior", meridian="Stomach", abbr="ST", point="Fenglong ST40", partner="Spleen", accent=ACCENT_OUTER),
    dict(cycle="Anterior", meridian="Spleen", abbr="SP", point="Gongsun SP4", partner="Stomach", accent=ACCENT_OUTER),
    dict(cycle="Posterior", meridian="Heart", abbr="HT", point="Tongli HT5", partner="Small Intestine", accent=ACCENT_INNER),
    dict(cycle="Posterior", meridian="Small Intestine", abbr="SI", point="Zhizheng SI7", partner="Heart", accent=ACCENT_INNER),
    dict(cycle="Posterior", meridian="Bladder", abbr="BL", point="Feiyang BL58", partner="Kidney", accent=ACCENT_INNER),
    dict(cycle="Posterior", meridian="Kidney", abbr="KI", point="Dazhong KI4", partner="Bladder", accent=ACCENT_INNER),
    dict(cycle="Middle", meridian="Pericardium", abbr="PC", point="Neiguan PC6", partner="Triple Energizer", accent=ACCENT_MIDDLE),
    dict(cycle="Middle", meridian="Triple Energizer", abbr="SJ", point="Waiguan SJ5", partner="Pericardium", accent=ACCENT_MIDDLE),
    dict(cycle="Middle", meridian="Gallbladder", abbr="GB", point="Guangming GB37", partner="Liver", accent=ACCENT_MIDDLE_WOOD),
    dict(cycle="Middle", meridian="Liver", abbr="LR", point="Ligou LR5", partner="Gallbladder", accent=ACCENT_MIDDLE_WOOD),
]
LUO_EXTRA = [
    dict(name="Conception Vessel (Ren)", point="Jiuwei CV15",
         course="Separates from the Governor Vessel at the lower end of the sternum; from CV15 it spreads over the abdomen."),
    dict(name="Governor Vessel (Du)", point="Changqiang GV1",
         course="Arises in the perineum, runs upward along both sides of the spine to the nape, spreads over the top "
                "of the head; at the scapular region it connects with the Bladder meridian and pierces through the spine."),
    dict(name="Major Collateral of the Spleen", point="Dabao SP21",
         course="Begins from Dabao SP21, emerges 3 cun below Yuanye GB22, and spreads through the chest and "
                "hypochondriac region, gathering blood all over the body."),
]

# ---------------------------------------------------------------------------
# MEETING (CROSSING) POINTS -- table sourced from Lecture_9Meeting_Points_
# List_.pdf (MOA-style appendix, pp.52-55). Embedded as source images rather
# than fully re-transcribed (90 rows x 17 columns) -- see decoder pages.
# ---------------------------------------------------------------------------
MEETING_POINTS_NOTE = (
    "\u201cMeeting Points of the Channels\u201d -- a point is a Crossing/Meeting Point when more than one "
    "channel's pathway passes through it. This full appendix table (Lecture_9Meeting_Points_List_.pdf, "
    "pp.52-55, MOA-style) is reproduced as source images below rather than re-typed, to preserve exact "
    "accuracy across all ~90 listed points and 17 channel/vessel columns."
)
MEETING_POINTS_HIGHLIGHTS = [
    ("GB20 (Fengchi)", "Gallbladder, Sanjiao, Yang Linking Vessel, Yang Motility Vessel -- 4-way meeting point; "
     "resolves the previously flagged \u201cGB crossing-point\u201d discrepancy from Week 6 for this specific point."),
    ("GB1 (Tongziliao)", "Small Intestine + Sanjiao + Gallbladder -- outer canthus, where 3 Yang channels of the "
     "head converge."),
    ("BL1 (Jingming)", "Stomach, Small Intestine, Bladder, Sanjiao, Gallbladder, Yang Linking, Yang Motility, "
     "Yin Motility -- the single busiest meeting point in the whole table (8 channels/vessels)."),
    ("ST12 (Quepen)", "Lung, Large Intestine, Bladder, Sanjiao, Gallbladder -- supraclavicular fossa, a major "
     "confluence point for channels descending into the chest."),
    ("SP6 (Sanyinjiao)", "Spleen, Liver, Kidney -- the classic \u201c3 Yin meeting\u201d point of the leg, the origin "
     "of its name (San Yin Jiao = \u201cThree Yin Intersection\u201d)."),
    ("CV3/CV4 (Zhongji/Guanyuan)", "Conception Vessel + Spleen/Liver/Kidney (the 3 leg Yin meridians) -- lower "
     "abdomen, reproductive/urinary point cluster."),
]

# ---------------------------------------------------------------------------
# FINAL EXAM MASTER REVIEW -- the comprehensive per-meridian table Dr. Zhang
# built live in lecture (slides 58-72). This is the single highest-value
# page for final exam prep.
# ---------------------------------------------------------------------------
CIRCULATION_RULES = [
    "3 Yin meridians of the hand run chest -> hand, converging with the 3 Yang meridians of the hand "
    "(exterior-interior pairs) at the fingertips.",
    "3 Yang meridians of the hand ascend from the fingertips to the head, where they connect with the "
    "3 Yang meridians of the foot.",
    "3 Yang meridians of the foot descend from the head to the toes, where they join the 3 Yin "
    "meridians of the foot.",
    "3 Yin meridians of the foot ascend from the toes to the abdomen and chest, meeting the 3 Yin "
    "meridians of the hand -- closing the full circuit.",
]
QI_FLOW_DIRECTIONS = [
    ("Yin meridians of the Hand", "Chest -> Hand"),
    ("Yang meridians of the Hand", "Hand -> Head"),
    ("Yang meridians of the Foot", "Head -> Foot"),
    ("Yin meridians of the Foot", "Foot -> Abdomen/Chest"),
]
DISTRIBUTION_RULES = [
    ("Limbs -- medial aspect", "Yin meridians: Anterior=Taiyin, Middle=Jueyin, Posterior=Shaoyin"),
    ("Limbs -- lateral aspect", "Yang meridians: Anterior=Yangming, Middle=Shaoyang, Posterior=Taiyang"),
    ("Head & Trunk", "Anterior=Yangming, Posterior=Taiyang, Lateral=Shaoyang"),
]

# Per-meridian master review row: (meridian, pertaining, connecting, first pt,
# last pt, total pts, direction, special-area note)
EXAM_MASTER_TABLE = [
    dict(m="Lung (LU)", pert="Lung", conn="Large Intestine", first="Zhongfu LU1 (chest)",
         last="Shaoshang LU11 (thumb, radial)", total="11", dirn="Chest -> Hand",
         special="Passes through the medial anterior border of the upper limb."),
    dict(m="Large Intestine (LI)", pert="Large Intestine", conn="Lung", first="Shangyang LI1 (index finger)",
         last="Yingxiang LI20 (nasolabial groove)", total="20", dirn="Hand -> Head",
         special="Ends beside the nose, linking to the Stomach meridian."),
    dict(m="Stomach (ST)", pert="Stomach", conn="Spleen", first="Chengqi ST1 (below pupil)",
         last="Lidui ST45 (2nd toe)", total="45", dirn="Head -> Foot",
         special="Starts lateral to the ala nasi; links to Spleen at the great toe (SP1)."),
    dict(m="Spleen (SP)", pert="Spleen", conn="Stomach", first="Yinbai SP1 (great toe)",
         last="Dabao SP21 (lateral chest, Major Luo)", total="21", dirn="Foot -> Chest/Abdomen",
         special="Ascends alongside the esophagus, reaches the tongue (connects to Heart via internal branch)."),
    dict(m="Heart (HT)", pert="Heart", conn="Small Intestine", first="Jiquan HT1 (axilla)",
         last="Shaochong HT9 (little finger, radial)", total="9", dirn="Chest -> Hand",
         special="Connects to the \u2018Eye System\u2019 via the throat."),
    dict(m="Small Intestine (SI)", pert="Small Intestine", conn="Heart", first="Shaoze SI1 (little finger, ulnar)",
         last="Tinggong SI19 (anterior to tragus)", total="19", dirn="Hand -> Head",
         special="Only meridian connecting BOTH inner and outer canthus of the eye."),
    dict(m="Bladder (BL)", pert="Bladder", conn="Kidney", first="Jingming BL1 (inner canthus)",
         last="Zhiyin BL67 (small toe, lateral)", total="67", dirn="Head -> Foot",
         special="Largest meridian in the body (67 points, 4 branches); starts at inner canthus."),
    dict(m="Kidney (KI)", pert="Kidney", conn="Bladder", first="Yongquan KI1 (sole)",
         last="Shufu KI27 (below clavicle)", total="27", dirn="Foot -> Chest",
         special="Connecting organs also include Liver and Lung; links with Pericardium at the chest."),
    dict(m="Pericardium (PC)", pert="Pericardium", conn="Triple Energizer (Sanjiao)", first="Tianchi PC1 (4th ICS)",
         last="Zhongchong PC9 (middle finger tip)", total="9", dirn="Chest -> Hand",
         special="Links with Sanjiao at the ring finger via a branch from Laogong PC8."),
    dict(m="Triple Energizer (SJ/TE)", pert="Sanjiao (Upper/Middle/Lower Jiao)", conn="Pericardium",
         first="Guanchong SJ1 (ring finger)", last="Sizhukong SJ23 (lateral eyebrow)", total="23",
         dirn="Hand -> Head", special="Runs in front of the ear; terminates at the outer canthus, links to Gallbladder."),
    dict(m="Gallbladder (GB)", pert="Gallbladder", conn="Liver", first="Tongziliao GB1 (outer canthus)",
         last="Zuqiaoyin GB44 (4th toe)", total="44", dirn="Head -> Foot",
         special="Zig-zag pathway across the head; only meridian to trace this shape."),
    dict(m="Liver (LR)", pert="Liver", conn="Gallbladder", first="Dadun LR1 (great toe, dorsal hairy region)",
         last="Qimen LR14 (Front-Mu of Liver, 6th ICS)", total="14", dirn="Foot -> Chest",
         special="Passes through the external genitalia and the \u2018Eye System\u2019; links to Lung at the chest, closing the 12-meridian cycle."),
]

EXAM_EXTRAORDINARY_NOTE = (
    "The 8 Extraordinary Vessels have NO internal Zang-Fu connections (no pertaining/connecting "
    "organ) -- their only running course is superficial (nape, vertex, hip, etc.), which is precisely "
    "what makes them different from the 12 Primary Meridians. Du, Ren, and Chong all begin in the "
    "lower abdomen -- \u2018one source, three branches.\u2019 The Belt (Dai) Vessel is the only vessel that "
    "runs horizontally around the waist rather than up/down the body. Yin Qiao and Yang Qiao both "
    "begin at their respective Confluent points (KI6 / BL62)."
)

FINAL_EXAM_SUMMARY = (
    "Dr. Zhang's own exam-focus summary (slide 57, 2026 deck): \u201cThe exam focuses on the pathways, "
    "connections, distribution, and special features of the meridians. You should know which organs "
    "each meridian is associated with, their starting and ending points, and key landmarks they pass "
    "-- such as the ear, nose, inner canthus, external genitalia, pubic region, and waist. Pay "
    "attention to the unique traits of certain meridians, the running course of the channel, the "
    "direction of Qi flow. Also review paired relationships between meridians, the composition of the "
    "fifteen collaterals, and how channels connect with each other.\u201d Keyword list from the same slide: "
    "12 primary Meridians, Belt Vessel, GV, 15 Collaterals."
)

EYE_RELATIONSHIP_TABLE = [
    ("Bladder (BL)", "Starts at the inner canthus (BL1 Jingming)."),
    ("Gallbladder (GB)", "Starts at the outer canthus (GB1 Tongziliao)."),
    ("Small Intestine (SI)", "A branch goes to the outer canthus; another travels below the eye to the inner canthus (only meridian connecting BOTH)."),
    ("Sanjiao (SJ)", "A branch runs from behind the ear to the outer canthus."),
    ("Liver (LR)", "Follows the throat upward, connects to the \u2018Eye System.\u2019"),
    ("Heart (HT)", "A branch links the heart to the \u2018Eye System\u2019 via the throat."),
    ("Stomach (ST)", "Ascends to the bridge of the nose, where it meets the Bladder meridian at the inner canthus."),
]

# ---------------------------------------------------------------------------
# COLLATERALS / DIVERGENT / SINEW / CUTANEOUS -- Middle Circuit new-content
# recap (slides 4-42, 2026 deck) -- confirms + completes Week 8's flagged
# self-study material for PC/SJ/GB/LR + all 12 Cutaneous Regions.
# ---------------------------------------------------------------------------
DIVERGENT_MIDDLE = [
    dict(meridian="Pericardium (PC)", accent=ACCENT_MIDDLE,
         beginning="Chest / 3 cun below the axilla", organs="Sanjiao, throat", exiting="Behind the ear",
         merging="Sanjiao meridian (Hand-Shaoyang)"),
    dict(meridian="Triple Energizer (SJ)", accent=ACCENT_MIDDLE,
         beginning="Vertex / supraclavicular fossa", organs="Chest, upper/middle/lower jiao", exiting="Supraclavicular fossa",
         merging="Rejoins its own primary meridian"),
    dict(meridian="Gallbladder (GB)", accent=ACCENT_MIDDLE_WOOD,
         beginning="Lateral thigh / lower abdomen (pelvic region)", organs="Gallbladder, Liver, Heart, esophagus, eye",
         exiting="Face / outer canthus", merging="Gallbladder meridian of Foot-Shaoyang"),
    dict(meridian="Liver (LR)", accent=ACCENT_MIDDLE_WOOD,
         beginning="Instep of the foot / pelvic region", organs="Pubic region", exiting="Pubic region",
         merging="Converges with the Gallbladder divergent meridian"),
]
SINEW_MIDDLE = [
    dict(meridian="Hand Jueyin (Pericardium)", accent=ACCENT_MIDDLE, fig="MUSCLE_PC",
         path="Middle finger -> elbow -> axilla -> ribs -> chest -> axilla -> spreads over the chest -> thoracic diaphragm.",
         binds="Medial side of elbow, axilla, diaphragm"),
    dict(meridian="Hand Shaoyang (Sanjiao)", accent=ACCENT_MIDDLE, fig="MUSCLE_SJ",
         path="4th finger -> wrist -> forearm -> olecranon -> upper arm -> shoulder -> neck -> joins Hand-Taiyang "
              "sinew -> angle of mandible -> root of tongue -> in front of the ear -> outer canthus -> temple -> "
              "corner of the forehead.",
         binds="Dorsum of wrist, posterior elbow, corner of forehead"),
    dict(meridian="Foot Shaoyang (Gallbladder)", accent=ACCENT_MIDDLE_WOOD, fig="MUSCLE_GB",
         path="4th toe -> external malleolus -> tibia -> knee -> fibula -> thigh (Futu ST32) -> sacrum. Straight "
              "branch: ribs -> axilla -> breast -> Quepen ST12 -> behind the ear -> temple -> vertex. Branch: "
              "temple -> cheek -> bridge of nose -> outer canthus.",
         binds="Outer canthus & side of nose, SC fossa (ST12), sacrum, above ST32, lateral malleolus & lateral knee"),
    dict(meridian="Foot Jueyin (Liver)", accent=ACCENT_MIDDLE_WOOD, fig="MUSCLE_LR",
         path="Dorsum of the great toe -> medial malleolus -> tibia -> knee -> thigh -> genital region -> joins "
              "the other Muscle Regions.",
         binds="Medial malleolus (anterior), tibia (medial condyle), genitals"),
]
SINEW_FUNCTIONS = [
    "Connects all the bones and joints of the body and maintains normal range of motion.",
    "Originates from the extremities of the limbs and ascends to the head and trunk, but does not "
    "reach the internal organs.",
    "Clinical significance: muscular problems -- Bi syndrome, contracture, stiffness, spasm, muscular atrophy.",
]
SINEW_PATTERN_RULES = [
    "All 3 Yang Muscle Regions of the foot connect with the eyes.",
    "All 3 Yin Muscle Regions of the foot connect with the genital region.",
    "All 3 Yang Muscle Regions of the hand connect with the angle of the forehead.",
    "All 3 Yin Muscle Regions of the hand connect with the thoracic cavity.",
]

CUTANEOUS_DEFINITION = (
    "The twelve cutaneous parts are the parts of the twelve meridians reflected on the body surface, "
    "where the Qi of the meridians is distributed -- the outermost layer of the human body."
)
CUTANEOUS_SOURCE_QUOTE = (
    "Su Wen (Plain Questions, Ch. 56): \u201cThe Cutaneous Regions are the part of the meridian system "
    "located in the superficial layers of the body. The Cutaneous Regions are marked by the regular "
    "meridians.\u201d Transmitting order of a disease: \u201cSkin -> Collaterals -> Meridians -> Fu organs -> "
    "Zang organs.\u201d Diagnostic color rule: \u201cBlue-colored skin signifies local pain. Dark-colored skin "
    "indicates blockage of qi and blood. Yellow to red colored skin refers to heat syndromes, and white "
    "colored skin to cold syndromes.\u201d"
)
CUTANEOUS_FUNCTIONS = [
    "Protects the organism from exogenous pathogen invasion -- the first line of defense.",
    "Projects symptoms and signs of internal disease onto the body surface (diagnostic skin-color rule).",
    "Interacts diagnostically and therapeutically -- the theoretical basis for gua sha, cupping, and "
    "intradermal/press needles.",
]
CUTANEOUS_DIVISIONS = [
    dict(group="Taiyang", members=["BL (foot)", "SI (hand)"], accent=ACCENT_INNER, fig="CUTANEOUS_YANG"),
    dict(group="Shaoyang", members=["GB (foot)", "SJ (hand)"], accent=ACCENT_MIDDLE, fig="CUTANEOUS_YANG"),
    dict(group="Yangming", members=["ST (foot)", "LI (hand)"], accent=ACCENT_OUTER, fig="CUTANEOUS_YANG"),
    dict(group="Taiyin", members=["SP (foot)", "LU (hand)"], accent=ACCENT_OUTER, fig="CUTANEOUS_YIN"),
    dict(group="Shaoyin", members=["KI (foot)", "HT (hand)"], accent=ACCENT_INNER, fig="CUTANEOUS_YIN"),
    dict(group="Jueyin", members=["LR (foot)", "PC (hand)"], accent=ACCENT_MIDDLE_WOOD, fig="CUTANEOUS_YIN"),
]
CUTANEOUS_EXCEPTION = (
    "Exception to the normal rule: Cutaneous Regions are the one structure that connects the Hand and "
    "Foot meridians of the SAME name together (e.g., Taiyang of the hand + Taiyang of the foot form "
    "one continuous Taiyang cutaneous region) -- this is why there are only 6 cutaneous regions, not 12."
)

# ---------------------------------------------------------------------------
# CLINICAL EVIDENCE -- PCOS/PMOS, urinary incontinence, EMMA robotic massage
# (slides 74-85, 2026 deck)
# ---------------------------------------------------------------------------
PCOS_INTRO = (
    "Polycystic Ovary Syndrome (PCOS) is the most common cause of anovulatory infertility, affecting "
    "an estimated 170 million women worldwide. In 2026, PCOS was renamed PMOS (Polyendocrine "
    "Metabolic Ovarian Syndrome), highlighting the central role of metabolic dysfunction -- "
    "particularly insulin resistance (IR) -- rather than treating it as a purely reproductive/ovarian "
    "condition. It is a common metabolic AND reproductive disorder: menstrual irregularity, hirsutism, "
    "sleep disruption, and a strong tendency toward obesity. No single first-line treatment currently "
    "addresses PCOS/PMOS's multisystem dysfunction, and adherence to first-line treatment is poor -- "
    "motivating an AI-enabled, acupuncture-based intervention targeting the metabolic mechanism directly."
)
PCOS_PROTOCOL = dict(
    design="International multicenter RCT + case-control collaboration (first industry-standard "
           "registration in this area; protocol validated through 3 Delphi rounds, adopted by the "
           "Karolinska Institutet research team).",
    dosing="Manual acupuncture combined with electroacupuncture, 5 sessions/week, 30 min/session "
           "(2-3x/week is also effective per Dr. Zhang's clinical experience); 3-4 months total "
           "treatment, since one menstrual cycle = one treatment unit for reproductive/gynecological cases.",
    points_1="Protocol 1: CV4-CV6, ST29-ST29, ST32-ST34 (bilateral). Needles placed in muscle (15-35mm), "
             "manually stimulated to de qi. Electrical stimulation as high as tolerable without pain "
             "(Program 10). Needle gauge scaled to patient BMI (0.25x30mm low BMI -> 0.30x50/75mm obese).",
    points_2="Protocol 2: CV6-CV10, ST27-ST27, SP10 + an extra point 6 cun cranial in vastus lateralis. "
             "Same stimulation parameters as Protocol 1. The two protocols are ALTERNATED across the "
             "treatment course (\u201cPhlegm-Dampness Obesity\u201d framework): Sanyinjiao/Xuehai (activate blood, "
             "resolve stasis), Zhongwan/Zusanli/Fenglong (strengthen Spleen, drain dampness).",
    outcomes="BMI: 30.18 -> 26.57 (p<0.01). Insulin resistance (HOMA-IR): 5.26 -> 2.89 (p<0.05). "
             "Hyperandrogenism (SHBG/FAI): 12.76 -> 7.46 (p<0.01). No rebound at 4-month follow-up "
             "(effect held with zero further treatment during the follow-up window).",
    basic_set="Basic reference acupuncture protocol for infertility/gynecology cases (Dr. Zhang's own "
              "clinical framework): GV20, CV20, CV12, CV6, GV4, PC6, ST16, ST6, SP6. Can be expanded or "
              "reduced by symptom and patient presentation; typical dosing 2x/week for 3 weeks.",
)
PCOS_DISCLAIMER = (
    "TEACHING ACUPOINT SET -- NOT A PRESCRIPTION. Acupoints may support comfort, but no point set is "
    "proven to improve IVF live-birth rates. ST36/SP6 support general constitutional/menstrual "
    "symptoms; PC6 supports nausea/anxiety-related symptoms; CV3/CV4/CV6 are lower-abdominal points "
    "used in some fertility protocols. Classroom orientation only -- point selection, depth, "
    "stimulation, and timing require individualized clinical assessment."
)

INCONTINENCE_TYPES = [
    ("Stress incontinence", "Leakage with coughing, sneezing, running, jumping, or lifting."),
    ("Urgency incontinence", "A sudden compelling urge followed by leakage; may include frequency and nocturia."),
    ("Mixed incontinence", "Stress and urgency symptoms occur together."),
]
INCONTINENCE_FIRSTLINE = [
    "Keep a 3-day bladder diary; review fluid, caffeine, constipation, and triggers.",
    "Stress/mixed: supervised pelvic floor muscle training for at least 3 months.",
    "Urgency/mixed: bladder training for at least 6 weeks.",
    "Refer to pelvic-floor physiotherapy if correct contraction is uncertain -- do not repeatedly "
    "practice by stopping urine flow.",
]
INCONTINENCE_RED_FLAGS = (
    "Prompt assessment needed for: blood in urine, pain/fever, recurrent urinary infection, voiding "
    "difficulty or retention, neurological symptoms, a vaginal bulge, or sudden marked worsening."
)
INCONTINENCE_STUDY = dict(
    citation="Liu Z, et al. JAMA. 2017;317(24):2493-2501. doi:10.1001/jama.2017.7220",
    design="Multicenter RCT, 12 hospitals, 504 women, ages 40-75. Electroacupuncture vs. sham "
           "electroacupuncture (blunt placebo needles, no penetration/current/de qi).",
    points="Bilateral Zhongliao (BL33) + Huiyang (BL35), lumbosacral electroacupuncture.",
    technique="0.30 x 75mm needles, depth approx. 50-60mm. BL33 inserted 30\u00b0-45\u00b0 inferomedially; BL35 "
              "slightly superolaterally. Twirl/lift-thrust to de qi, then attach paired electrodes. "
              "Continuous wave, 50Hz, 1-5mA, 30 min/session.",
    course="3 sessions/week (ideally every other day) x 6 consecutive weeks = 18 sessions total.",
    outcome="Primary outcome: change in urine leakage at week 6, measured by the standardized 1-hour pad test.",
    caution="Research points, not a substitute for pelvic-floor training. NICE does not recommend "
            "complementary therapies routinely for urinary incontinence or overactive bladder. Avoid "
            "home needling or direct moxibustion at the sacrum -- burns, smoke exposure, and delayed "
            "diagnosis are real risks.",
)

EMMA_DATA = dict(
    intro="EMMA (Expert Manipulative Massage Automation) is a robot designed to deliver Tuina-style "
          "manipulative massage, developed in collaboration with a Singapore-based team; Dr. Zhang "
          "uses a version of this technology in her own clinic (gynecology focus: qi/pelvic pain).",
    cohort="22 registered records; 21 participants treated. Course maturity at data cut (15 Aug 2026): "
           "22 registered -> 21 started -> 18 reached >=3 sessions -> 13 reached >=5 sessions -> 10 "
           "completed all 6 sessions. Data instruments: 96 paired pre/post VAS records; NRS, McGill "
           "Pain Questionnaire, SF-36, and mood measures at checkpoints; 126 thermography file/range "
           "references linked to pain phenotype, menstrual context, and height/weight.",
    results="Fixed 6-session completer cohort (n=10, 60 paired treatment visits). Mean VAS fell from "
            "6.2 pre-treatment (Session 1) to 1.8 post-treatment (Session 6) -- a 71.9% reduction "
            "(6.22 -> 1.75 course average, -4.47 points). 57/60 visits showed a lower post-session VAS "
            "than pre-session. 10/10 participants (100%) achieved >=30% reduction; 9/10 (90%) achieved "
            ">=50% reduction.",
    takeaway="The repeated within-patient signal is strong enough to justify prospective controlled "
             "validation with predefined responder endpoints -- translating established manual "
             "treatment approaches into robotic interventions, not replacing the clinician's "
             "assessment and point selection.",
)

# ---------------------------------------------------------------------------
# PLA CONTENT -- Sections A-F + Inter-Quiz (Behavioral Interteaching structure)
# ---------------------------------------------------------------------------
VOCAB = [
    ("Wu Shu Xue", "Five Shu (Transport) Points", ACCENT_FIVESHU),
    ("Jing (Well)", "Well -- \u201cwhere it emerges\u201d, fingertip/toe-tip point", ACCENT_FIVESHU),
    ("Ying (Spring)", "Spring -- \u201cwhere it flows\u201d, before the MCP/MTP joint", ACCENT_FIVESHU),
    ("Shu (Stream)", "Stream -- \u201cwhere it pours\u201d, after the MCP/MTP joint", ACCENT_FIVESHU),
    ("Jing (River)", "River -- \u201cwhere it travels\u201d, forearm/lower leg", ACCENT_FIVESHU),
    ("He (Sea)", "Sea -- \u201cwhere it enters\u201d, near elbow/knee", ACCENT_FIVESHU),
    ("Jiao Hui Xue", "Confluent (opening) point of an Extraordinary Vessel", ACCENT_CONFLUENT),
    ("Luo Mai", "Collateral (connecting) vessel", ACCENT_LUO),
    ("Ashi", "\u201cOuch\u201d point -- located by tenderness, not fixed anatomy", None),
    ("PMOS", "Polyendocrine Metabolic Ovarian Syndrome (2026 renaming of PCOS)", ACCENT_CLINICAL),
]
LEARNING_TARGETS = [
    "Recite all 60 Five Shu Points (5 per meridian x 12 meridians) with correct Jing/Ying/Shu/Jing/He sequencing.",
    "State all 8 Confluent Points, their paired vessel, and their master-couple partner point.",
    "Reproduce the 15-Collateral master table (meridian -> Luo point -> partner meridian) from memory.",
    "Explain why Cutaneous Regions form only 6 groups (not 12), and name the Hand+Foot pair in each group.",
    "Reproduce the Final Exam Master Table: pertaining/connecting organ, first/last point, total points, "
    "direction of flow, and one special-area landmark, for all 12 primary meridians.",
]
ANTICIPATORY_QUESTIONS = [
    (1, True, "Five Shu", "Which Five Shu point category treats disorders of the six Fu organs, and why does its location (near elbow/knee) support that function?"),
    (2, True, "Confluent Points", "Name the 4 master couples of the Eight Confluent Points and the body region each couple treats."),
    (3, False, "Collaterals", "Why are there 15 Collaterals rather than 12 -- what gap do the 3 extra ones (CV/GV/Spleen Great Luo) fill?"),
    (4, True, "Cutaneous Regions", "What is the one exception to the usual Yin/Yang, Hand/Foot organization that makes Cutaneous Regions form only 6 groups?"),
    (5, False, "Final Exam", "For the Kidney meridian, state its pertaining organ, connecting organ, first point, last point, and direction of Qi flow."),
]
IQ_CHECKPOINTS = [
    (1, "ACQ", "Which meridian's Luo point is Fenglong ST40, and which meridian does it connect to?"),
    (2, "ACQ", "Name the Jing-Well point of the Liver meridian."),
    (3, "MAINT", "Which Confluent point pairs with Shenmai (BL62), and which vessel does that pair open?"),
    (4, "ACQ", "How many total points does the Bladder meridian have, and why is it called the largest meridian?"),
    (5, "ACQ", "Name the 3 extra Collaterals (not tied to a paired organ meridian) and their originating points."),
    (6, "MAINT", "State the qi-flow direction rule for the Yin meridians of the hand."),
]
IQ_ANSWERS = [
    "Fenglong ST40 is the Luo point of the Stomach meridian; it connects to the Spleen meridian.",
    "Dadun LR1.",
    "Houxi (SI3) pairs with Shenmai (BL62); together they open the Du Vessel (Houxi) / Yang Qiao Vessel (Shenmai) -- Houxi opens Du Mai, Shenmai opens Yang Qiao Mai.",
    "67 points -- the largest meridian in the body, with 4 branches, running from the inner canthus (BL1) to the lateral small toe (BL67).",
    "Conception Vessel (from Jiuwei CV15), Governor Vessel (from Changqiang GV1), and the Major Collateral of the Spleen (from Dabao SP21).",
    "Yin meridians of the hand flow chest -> hand.",
]
CLINICAL_CASE = (
    "A 29-year-old woman presents with irregular menses (cycles 45-60 days), hirsutism, recent weight "
    "gain, and difficulty conceiving after 14 months of trying. Labs show elevated fasting insulin and "
    "an elevated LH:FSH ratio consistent with PCOS/PMOS. She has tried metformin with limited "
    "tolerance (GI side effects) and asks about acupuncture as an adjunct."
)
CLINICAL_CASE_PRE_Q = (
    "Before reading the protocol: which basic acupoint set would you reach for first, and what is your "
    "reasoning for choosing points that address BOTH the metabolic (insulin resistance) and "
    "reproductive (menstrual/ovulatory) dimensions of this presentation?"
)
CLINICAL_CASE_POST_Q = (
    "After reviewing Dr. Zhang's protocol: how does alternating Protocol 1 and Protocol 2 across the "
    "treatment course address the \u201cPhlegm-Dampness Obesity\u201d framework specifically, and why does she "
    "emphasize a 3-4 month minimum course length for reproductive/gynecological cases?"
)
