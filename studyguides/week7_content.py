"""Shared content for the Week 7 PLA -- The Eight Extraordinary Vessels
(Qi Jing Ba Mai). Confirmed via Jon's written syllabus table: 'Week 7 (CLO 2,4)
Eight Extraordinary Meridians -- QUIZ 5 -- Homework 5 (material from week 6-7)
-- CAM p.82-89 -- MOA p.17-25, 495-497, 529-533.' This matches the reading
assignments on the closing slide of Lecture_7vivian11_12.pdf exactly, confirming
that deck as this week's correct source (76 slides: GV, CV, Chong, Dai, Yang/Yin
Qiao, Yang/Yin Wei, plus a 12-meridian review section).

NOTE: An earlier build of this file assumed Week 7 = Divergent/Sinew/Cutaneous
Channels based on Dr. Zhang's verbal Week 1 walkthrough. The written syllabus
table overrides that -- Divergent/Sinew/Cutaneous's actual week is unconfirmed
and should be re-checked before that week is built.
"""

NAVY = (0.114, 0.227, 0.369)
ACCENT_GV = (0.114, 0.227, 0.369)      # navy -- Du Mai, sea of yang
ACCENT_CV = (0.753, 0.224, 0.169)      # red -- Ren Mai, sea of yin
ACCENT_CHONG = (0.55, 0.38, 0.16)      # amber/brown -- Chong, sea of blood/12 meridians
ACCENT_DAI = (0.16, 0.44, 0.46)        # slate teal -- Dai, the horizontal vessel
ACCENT_QIAO = (0.20, 0.48, 0.27)       # green -- the two Heel vessels
ACCENT_WEI = (0.45, 0.30, 0.55)        # muted purple -- the two Link vessels (distinct
                                        # from element-coding purple ban, which applies to
                                        # PC/SJ Ministerial Fire specifically, not vessels)
GRAY = (0.40, 0.40, 0.40)

READING_ASSIGNMENT = "CAM p.82-89 \u00b7 MOA p.17-25, 495-497, 529-533 (per written syllabus, Week 7)"

# Structural parallel to the "6 Confluences" table used in the Week 7 Divergent-Channel
# draft -- here, the 4 Confluent (Opening/Master-Couple) Point pairs that link each
# Extraordinary Vessel to a Primary Meridian point, used clinically to "open" the vessel.
CONFLUENT_PAIRS = [
    ("Chong Mai + Yin Wei Mai", "SP 4  Gongsun", "PC 6  Neiguan"),
    ("Du Mai + Yang Qiao Mai", "SI 3  Houxi", "BL 62  Shenmai"),
    ("Ren Mai + Yin Qiao Mai", "LU 7  Lieque", "KI 6  Zhaohai"),
    ("Dai Mai + Yang Wei Mai", "GB 41  Zulinqi", "SJ 5  Waiguan"),
]

VOCAB = [
    ("Qi Jing Ba Mai", "The Eight Extraordinary Vessels", None),
    ("Du Mai", "Governor Vessel (GV)", ACCENT_GV),
    ("Ren Mai", "Conception Vessel (CV)", ACCENT_CV),
    ("Chong Mai", "Thoroughfare Vessel", ACCENT_CHONG),
    ("Dai Mai", "Belt / Girdling Vessel", ACCENT_DAI),
    ("Qiao Mai", "Heel Vessel", ACCENT_QIAO),
    ("Wei Mai", "Link Vessel", ACCENT_WEI),
    ("Jiao Hui Xue", "Coalescent Point", None),
    ("Ba Mai Jiao Hui Xue", "Eight Confluent Points", None),
    ("Yi Yuan San Qi", "One Source, Three Branches", ACCENT_CHONG),
]

# One-line key fact per vessel, shown as a reference key below the vocab table --
# the ENGLISH column stays a short gloss so it never collides with the ruled
# "MY DEFINITION / CLINICAL NOTE" column, which is meant for the student's own words.
VOCAB_KEY_FACTS = [
    ("Du Mai (GV)", "posterior midline, \"sea of the yang meridians,\" 28 points"),
    ("Ren Mai (CV)", "anterior midline, \"sea of the yin meridians,\" 24 points"),
    ("Chong Mai", "\"sea of 12 meridians,\" \"sea of blood\" -- shares points with primary meridians"),
    ("Dai Mai", "the only vessel running horizontally around the waist"),
    ("Qiao Mai", "Yang + Yin pair -- balance limb movement and sleep/wake"),
    ("Wei Mai", "Yang + Yin pair -- link all yang meridians / all yin meridians"),
    ("Jiao Hui Xue", "where a vessel crosses a primary meridian along its course"),
    ("Ba Mai Jiao Hui Xue", "8 points, 4 pairs -- the classic \"master-couple\" opening points"),
    ("Yi Yuan San Qi", "Du, Ren, and Chong all arise from the lower abdomen"),
]

LEARNING_TARGETS = [
    "Name all 8 Extraordinary Vessels and state which two have their OWN dedicated acupuncture points (GV, CV) versus the six that share points with primary meridians.",
    "State the \u201csea\u201d designation for GV (sea of yang meridians), CV (sea of yin meridians), and Chong (sea of the 12 meridians / sea of blood / sea of the zang-fu organs).",
    "Trace the basic course of the Governor Vessel (GV1 Changqiang to GV28 Yinjiao) and Conception Vessel (CV1 Huiyin to CV24 Chengjiang), including point totals (28 and 24).",
    "Explain \u201cone source, three branches\u201d -- how Du, Ren, and Chong all arise from the lower abdomen before diverging.",
    "Identify each vessel's confluent (opening) point and correctly pair all 4 master-couple combinations (SP4/PC6, SI3/BL62, LU7/KI6, GB41/SJ5).",
    "State the core physiological function of the Belt Vessel (Dai) and explain why it is structurally unique among the 8 (horizontal, not vertical).",
    "Contrast the Yang Qiao / Yin Qiao pair (limb movement, sleep-wake balance) with the Yang Wei / Yin Wei pair (exterior/interior yang-yin regulation).",
    "Recognize characteristic pathological symptom patterns for each vessel (e.g. spinal stiffness = GV, infertility/urogenital = CV, waist pain with no clear direction = Dai) and explain why the extraordinary vessels lack a pertaining zang/fu organ.",
]

CONNECT_BLANKS = [
    ("Only GV and CV have their own dedicated acupuncture", 60, "-- the other six share points."),
    ("The Governor Vessel is described as the sea of the", 50, "meridians."),
    ("The Conception Vessel is described as the sea of the", 50, "meridians."),
    ("The Chong Vessel is the sea of the 12 meridians, of blood, and of the", 90, "organs."),
    ("Du, Ren, and Chong share a lower-abdomen origin -- \u201cone source,", 60, "branches.\u201d"),
    ("The Belt (Dai) Vessel is the only vessel that runs", 70, "the body rather than up and down."),
    ("Yang Qiao's confluent point is Shenmai,", 60, "-- and Yin Qiao's is Zhaohai, KI 6."),
    ("None of the Eight Extraordinary Vessels pertain to a", 90, "organ, unlike the 12 primary meridians."),
]

ANTICIPATORY_SEA_VESSELS = [
    (1, True, "GV Course", "Trace the Governor Vessel from the lower abdomen to its ending point at the columnella of the nose. Where does it enter the brain along the way?"),
    (2, True, "CV Course", "Trace the Conception Vessel from Huiyin (CV1) to Chengjiang (CV24). What structure does it pass through near the lips (hint: it shares a point with GV)?"),
    (3, False, "GV Pathology", "Name at least 3 pathological symptoms associated with Governor Vessel disorder."),
    (4, False, "CV Pathology", "Name at least 3 pathological symptoms associated with Conception Vessel disorder, especially involving the Liver/Kidney."),
]
ANTICIPATORY_CHONG_DAI = [
    (5, True, "One Source, Three Branches", "Explain what \u201cone source, three branches\u201d means for Du, Ren, and Chong. Why might this matter clinically?"),
    (6, False, "Chong's Three Titles", "Chong Mai carries three \u201csea of...\u201d titles. Name all three."),
    (7, True, "Dai's Uniqueness", "Why is the Belt Vessel structurally different from all 7 other extraordinary vessels? What is its core physiological function?"),
]
ANTICIPATORY_QIAO_WEI = [
    (8, True, "Qiao vs Wei", "Yang Qiao/Yin Qiao and Yang Wei/Yin Wei both come in yang/yin pairs. What is the FUNCTIONAL difference between what the Qiao pair regulates versus the Wei pair?"),
    (9, False, "Sleep-Wake", "Which vessel keeps the body awake and active, and which promotes calm and restful sleep? Why might Dr. Zhang connect this to insomnia treatment?"),
    (10, False, "Wei Function Overlap", "Yang Wei and Yin Wei are described as having a \u201cjoint function.\u201d What is it?"),
]
ANTICIPATORY_COMPARE = [
    (11, True, "Confluent Point Pairing", "Without looking, try to pair all 4 master-couple confluent points (8 points total, 4 pairs). Which pairing do you feel least confident about?"),
    (12, False, "Structural Trap", "State the one structural feature ALL 8 Extraordinary Vessels share that distinguishes them from the 12 primary meridians (hint: organs)."),
]

IQ_CHECKPOINTS = [
    ("1-4", [
        (1, "ACQ", "What are the two \u201csea\u201d titles for GV and CV respectively?"),
        (2, "ACQ", "How many points does the Governor Vessel have in total? The Conception Vessel?"),
        (3, "ACQ", "What is Chong Mai's confluent (opening) point, and which primary meridian is it on?"),
        (4, "MAINT", "Name the Pertaining Organ and Connecting Organ for the Lung meridian. (Wk 1-2 review)"),
    ]),
    ("5-8", [
        (5, "ACQ", "What makes the Belt (Dai) Vessel structurally unique among the 8 extraordinary vessels?"),
        (6, "ACQ", "Name the confluent point pairing for Du Mai + Yang Qiao Mai."),
        (7, "ACQ", "Which vessel governs sleep/wake balance along with limb movement -- Qiao or Wei?"),
        (8, "MAINT", "PC has zero of what, matching the same trap pattern as HT? (Wk 6 review)"),
    ]),
    ("9-12", [
        (9, "ACQ", "What do all 8 Extraordinary Vessels lack that the 12 primary meridians have?"),
        (10, "ACQ", "What does \u201cone source, three branches\u201d refer to?"),
        (11, "MAINT", "Which 4 acupuncture points are forbidden in pregnancy through Week 5? (cumulative review)"),
        (12, "ACQ", "Name the confluent point pairing for Ren Mai + Yin Qiao Mai."),
    ]),
]

IQ_ANSWERS = [
    "GV = \u201csea of the yang meridians.\u201d CV = \u201csea of the yin meridians.\u201d",
    "Governor Vessel: 28 points (GV1 Changqiang to GV28 Yinjiao). Conception Vessel: 24 points (CV1 Huiyin to CV24 Chengjiang).",
    "Chong Mai's confluent point is Gongsun, SP 4 -- on the Spleen Meridian of Foot-Taiyin. It is also the Luo-Connecting point of the Spleen meridian.",
    "Pertaining Organ = Lung; Connecting Organ = Large Intestine (per the paired Yin-Yang / Interior-Exterior relationship).",
    "The Dai (Belt) Vessel is the only one of the 8 that runs horizontally around the waist/body rather than vertically up and down; it controls/binds all the other longitudinally-running meridians.",
    "Du Mai + Yang Qiao Mai confluent pair: Houxi (SI 3) with Shenmai (BL 62).",
    "The Qiao (Heel) vessels govern sleep/wake balance -- Yang Qiao keeps the body awake/active, Yin Qiao promotes calm and restful sleep -- in addition to balancing limb movement.",
    "PC has zero crossing points, the same trap pattern confirmed for HT in the Week 4/6 recap -- watch for this on quiz questions asking which channel(s) have no crossing points.",
    "All 8 Extraordinary Vessels lack a pertaining zang/fu organ -- this is the core structural feature distinguishing them from the 12 primary meridians.",
    "\u201cOne source, three branches\u201d describes how Du Mai, Ren Mai, and Chong Mai all arise together from the lower abdomen before diverging into their separate pathways.",
    "Forbidden-in-pregnancy points through Week 5: LI4, SP6, BL60, BL67. (GB21 is added once Week 6 GB material is covered.)",
    "Ren Mai + Yin Qiao Mai confluent pair: Lieque (LU 7) with Zhaohai (KI 6).",
]
