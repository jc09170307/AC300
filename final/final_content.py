"""
AC300/AC375 Final Exam (Weeks 1-9, cumulative) -- content data module.
Sourced from: verified weekly Study Guides/Cram Sheets/Special Points Decoders
already pushed to jc09170307/AC300, cross-checked against the 2026 Zhang slide
decks and the raw class transcripts (esp. AC300_Week_9_Transcript.txt, which is
Dr. Zhang's own live Final Exam Review). Divergent/Collateral/Muscle/Cutaneous
detail is included for completeness (comprehensive request) but flagged as
LOW-PRIORITY per Dr. Zhang's explicit statement that the review does not cover
that material in depth for the exam.
"""

NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)

METAL = (0.365, 0.408, 0.451)      # LU/LI
EARTH = (0.663, 0.478, 0.169)      # ST/SP
FIRE = (0.690, 0.204, 0.169)       # HT/SI
WATER = (0.176, 0.310, 0.541)      # BL/KI
FIREMIN = (0.850, 0.420, 0.380)    # PC/SJ -- coral, never purple
WOOD = (0.200, 0.480, 0.270)       # GB/LR
EXTRA = (0.380, 0.180, 0.522)      # GV/CV/8 vessels -- purple ok for extraordinary category only
TEAL = (0.16, 0.44, 0.46)          # confluent points
AMBER_LUO = (0.55, 0.38, 0.16)     # 15 collaterals

# ---------------------------------------------------------------------------
# WHAT DR. ZHANG SAID -- verbatim-sourced guidance for the final (Week 9 live
# transcript, "review for the final examination" segment + Week 6/8 quotes)
# ---------------------------------------------------------------------------
ZHANG_FINAL_FACTS = [
    ("30 questions total", "Confirmed verbally in the Week 9 live class when a student asked directly: "
     "\"how many questions we have in final exam\" -> \"30 questions.\""),
    ("Cumulative, reuses quiz material", "Per Week 6: \"the final exam mentions all the questions, including in "
     "the final examination, [are] concerns from each quiz, not new question.\" The final draws from Quiz 1-6 "
     "content directly -- review EVERY quiz you've taken, not just lecture notes."),
    ("No new content Week 9->10", "Week 9 had no new quiz or homework -- it was 100% review. Week 10 is the "
     "final exam itself. Homework 5 must be submitted before the final or the grade cannot be entered."),
    ("Review = pathways, not divergent/collateral detail", "Direct quote, Week 9: a student asked whether the "
     "final \"will include the last week and this week's lecture regarding collaterals and divergent points\" -- "
     "Dr. Zhang answered \"No, no. In the review part, all the content included in the review part, we will not "
     "tell you about the divergent and collaterals.\" Muscle Regions and Cutaneous Regions were also not part of "
     "her review slides. Know the concepts, but they are LOW-YIELD for the final vs. primary pathways."),
    ("Her review slides emphasized", "(1) All 12 primary meridian pathways -- start point, end point, direction, "
     "pertaining organ, connecting organ, and the region(s) each crosses (ear, nose, eye, genitals, tongue). "
     "(2) The three Circuits (Anterior/Outer, Posterior/Inner, Middle) and their sequence. (3) Five Shu (Transport) "
     "Points -- full master table, all 12 meridians. (4) Eight Confluent Points and their Extraordinary Vessel "
     "pairings. (5) The Eight Extraordinary Vessels themselves (started via their confluent points, e.g. "
     "\"Yin Chao and Yang Chao [start] at BL62 and KI6\")."),
    ("Clinical evidence content is NOT exam material", "The PCOS/PMOS acupuncture protocol, the JAMA urinary "
     "incontinence RCT, and the EMMA robotic-massage pilot data were presented as clinical context/enrichment, "
     "separate from \"the review for the final examination\" segment -- do not spend final-prep time memorizing "
     "these numbers."),
    ("\"If you understand the slides, you can pass the final exam very easily.\"", "Dr. Zhang's own closing "
     "framing of the Week 9 review lecture -- her review deck (not the raw transcript detail) is the single best "
     "final-prep source, supplemented by re-drilling each week's Quiz Kit."),
]

# ---------------------------------------------------------------------------
# MASTER PATHWAY TABLE -- the #1 highest-yield table per Dr. Zhang's review
# ---------------------------------------------------------------------------
# (abbr, organ, classification, yin/yang, direction, circuit, clock)
TWELVE_MERIDIANS = [
    ("LU", "Lung", "Hand Taiyin", "Yin", "Chest -> Hand", "Outer / Anterior", "3-5 AM"),
    ("LI", "Large Intestine", "Hand Yangming", "Yang", "Hand -> Head", "Outer / Anterior", "5-7 AM"),
    ("ST", "Stomach", "Foot Yangming", "Yang", "Head -> Foot", "Outer / Anterior", "7-9 AM"),
    ("SP", "Spleen", "Foot Taiyin", "Yin", "Foot -> Chest", "Outer / Anterior", "9-11 AM"),
    ("HT", "Heart", "Hand Shaoyin", "Yin", "Chest -> Hand", "Inner / Posterior", "11 AM-1 PM"),
    ("SI", "Small Intestine", "Hand Taiyang", "Yang", "Hand -> Head", "Inner / Posterior", "1-3 PM"),
    ("BL", "Bladder", "Foot Taiyang", "Yang", "Head -> Foot", "Inner / Posterior", "3-5 PM"),
    ("KI", "Kidney", "Foot Shaoyin", "Yin", "Foot -> Chest", "Inner / Posterior", "5-7 PM"),
    ("PC", "Pericardium", "Hand Jueyin", "Yin", "Chest -> Hand", "Middle", "7-9 PM"),
    ("SJ", "San Jiao (Triple Burner)", "Hand Shaoyang", "Yang", "Hand -> Head", "Middle", "9-11 PM"),
    ("GB", "Gallbladder", "Foot Shaoyang", "Yang", "Head -> Foot", "Middle", "11 PM-1 AM"),
    ("LR", "Liver", "Foot Jueyin", "Yin", "Foot -> Chest", "Middle", "1-3 AM"),
]

DIRECTION_RULES = [
    ("Yin meridians of the HAND", "Chest -> Hand"),
    ("Yang meridians of the HAND", "Hand -> Head"),
    ("Yang meridians of the FOOT", "Head -> Foot"),
    ("Yin meridians of the FOOT", "Foot -> Chest/Abdomen"),
]

CIRCUITS = [
    ("Outer Circuit", "Anterior", ["LU (chest->hand)", "LI (hand->head)", "ST (head->foot)", "SP (foot->chest)"],
     "Taiyin / Yangming", METAL),
    ("Inner Circuit", "Posterior (also called \"Posterior Circuit\")",
     ["HT (chest->hand)", "SI (hand->head)", "BL (head->foot)", "KI (foot->chest)"], "Shaoyin / Taiyang", FIRE),
    ("Middle Circuit", "Middle/Lateral", ["PC (chest->hand)", "SJ (hand->head)", "GB (head->foot)", "LR (foot->chest)"],
     "Jueyin / Shaoyang", FIREMIN),
]

HANDOFF_POINTS = [
    ("Hand Yin -> Hand Yang", "at the FINGERS", "LU7 branch meets LI1 (index finger)"),
    ("Hand Yang -> Foot Yang", "at the FACE", "LI20 meets ST1/BL1 area"),
    ("Foot Yang -> Foot Yin", "at the TOES", "ST42/SP1 (great toe)"),
    ("Foot Yin -> Hand Yin", "internally, at the CHEST", "SP -> HT (diaphragm); same pattern for KI->PC, LR->LU"),
]

# ---------------------------------------------------------------------------
# CHANNEL META -- full ID-card data per primary meridian + GV/CV, verified
# against each week's Special Points Decoder / Cram Sheet.
# ---------------------------------------------------------------------------
CHANNEL_META = {
    "LU": dict(name="Lung", full="Lung Meridian of Hand-Taiyin", n_points=11, element="Metal", polarity="Yin",
               clock="3-5 AM", direction="Chest -> Hand", pertains="Lung", connects="Large Intestine",
               back_shu="BL13 Feishu", front_mu="LU1 Zhongfu (own -- unusual)", yuan="LU9 Taiyuan",
               luo="LU7 Lieque", he_sea="LU5 Chize", xi_cleft="LU6 Kongzui",
               confluent="LU7 -- opens Ren Mai (paired w/ KI6)", command="LU7 -- head/neck",
               crossing="none named (terminal Yin channel)", first_last="LU1 Zhongfu / LU11 Shaoshang",
               accent=METAL),
    "LI": dict(name="Large Intestine", full="Large Intestine Meridian of Hand-Yangming", n_points=20, element="Metal",
               polarity="Yang", clock="5-7 AM", direction="Hand -> Head", pertains="Large Intestine", connects="Lung",
               back_shu="BL25 Dachangshu", front_mu="ST25 Tianshu (on ST channel)", yuan="LI4 Hegu -- FORBIDDEN in pregnancy",
               luo="LI6 Pianli", he_sea="LI11 Quchi", xi_cleft="LI7 Wenliu",
               confluent="none", command="LI4 -- face/mouth",
               crossing="crosses GV14, ST/SI region near shoulder/neck", first_last="LI1 Shangyang / LI20 Yingxiang",
               accent=METAL),
    "ST": dict(name="Stomach", full="Stomach Meridian of Foot-Yangming", n_points=45, element="Earth", polarity="Yang",
               clock="7-9 AM", direction="Head -> Foot", pertains="Stomach", connects="Spleen",
               back_shu="BL21 Weishu", front_mu="CV12 Zhongwan", yuan="ST42 Chongyang",
               luo="ST40 Fenglong", he_sea="ST36 Zusanli", xi_cleft="ST34 Liangqiu",
               confluent="none", command="ST36 -- abdomen; Lower He-Sea ST37 (LI) / ST39 (SI)",
               crossing="11 -- the MOST of any primary channel (LI20, BL1, GB3/4/6, SP1, GV24, GV26, CV12/13/24)",
               first_last="LI20 Yingxiang is the true origin; ST1 Chengqi / ST45 Lidui",
               accent=EARTH),
    "SP": dict(name="Spleen", full="Spleen Meridian of Foot-Taiyin", n_points=21, element="Earth", polarity="Yin",
               clock="9-11 AM", direction="Foot -> Chest", pertains="Spleen", connects="Stomach",
               back_shu="BL20 Pishu", front_mu="LR13 Zhangmen (on LR channel)", yuan="SP3 Taibai",
               luo="SP4 Gongsun", he_sea="SP9 Yinlingquan", xi_cleft="SP8 Diji",
               confluent="SP4 -- opens Chong Mai (paired w/ PC6)", command="Great Luo SP21 Dabao",
               crossing="6 -- abdomen/chest (CV3, CV4, CV10, GB24, LR14, LU1)",
               first_last="SP1 Yinbai / SP21 Dabao", accent=EARTH),
    "HT": dict(name="Heart", full="Heart Meridian of Hand-Shaoyin", n_points=9, element="Fire", polarity="Yin",
               clock="11 AM-1 PM", direction="Chest -> Hand", pertains="Heart", connects="Small Intestine",
               back_shu="BL15 Xinshu", front_mu="CV14 Juque", yuan="HT7 Shenmen",
               luo="HT5 Tongli", he_sea="HT3 Shaohai", xi_cleft="HT6 Yinxi",
               confluent="none", command="none", crossing="none (fewest of any primary channel, tied w/ PC)",
               first_last="HT1 Jiquan / HT9 Shaochong", accent=FIRE),
    "SI": dict(name="Small Intestine", full="Small Intestine Meridian of Hand-Taiyang", n_points=19, element="Fire",
               polarity="Yang", clock="1-3 PM", direction="Hand -> Head", pertains="Small Intestine", connects="Heart",
               back_shu="BL27 Xiaochangshu", front_mu="CV4 Guanyuan", yuan="SI4 Wangu",
               luo="SI7 Zhizheng", he_sea="SI8 Xiaohai", xi_cleft="SI6 Yanglao",
               confluent="SI3 Houxi -- opens Du Mai (paired w/ BL62)", command="none",
               crossing="crosses GV14, cheek/eye region", first_last="SI1 Shaoze / SI19 Tinggong",
               accent=FIRE),
    "BL": dict(name="Bladder", full="Bladder Meridian of Foot-Taiyang", n_points=67, element="Water", polarity="Yang",
               clock="3-5 PM", direction="Head -> Foot", pertains="Bladder", connects="Kidney",
               back_shu="BL28 Pangguangshu (own)", front_mu="CV3 Zhongji", yuan="BL64 Jinggu",
               luo="BL58 Feiyang", he_sea="BL40 Weizhong (Command, back)", xi_cleft="BL63 Jinmen",
               confluent="BL62 Shenmai -- opens Yang Qiao Mai (paired w/ SI3)",
               command="BL40 -- back; hosts Back-Shu series BL13-BL28 for ALL 12 zang-fu organs",
               crossing="14, shared with GV and GB, concentrated around the head",
               first_last="BL1 Jingming / BL67 Zhiyin -- LARGEST channel in the body, 5 branches",
               accent=WATER),
    "KI": dict(name="Kidney", full="Kidney Meridian of Foot-Shaoyin", n_points=27, element="Water", polarity="Yin",
               clock="5-7 PM", direction="Foot -> Chest", pertains="Kidney", connects="Bladder",
               back_shu="BL23 Shenshu", front_mu="GB25 Jingmen", yuan="KI3 Taixi (also Shu-Stream -- dual role)",
               luo="KI4 Dazhong", he_sea="KI10 Yingu", xi_cleft="KI5 Shuiquan",
               confluent="KI6 Zhaohai -- opens Yin Qiao Mai (paired w/ LU7)", command="none",
               crossing="crosses SP at SP6 (Sanyinjiao); internally connects Lung, Liver, Heart",
               first_last="KI1 Yongquan / KI27 Shufu -- 3 branches, terminates at root of tongue",
               accent=WATER),
    "PC": dict(name="Pericardium", full="Pericardium Meridian of Hand-Jueyin", n_points=9, element="Fire (Ministerial)",
               polarity="Yin", clock="7-9 PM", direction="Chest -> Hand", pertains="Pericardium", connects="San Jiao",
               back_shu="BL14 Jueyinshu", front_mu="CV17 Danzhong", yuan="PC7 Daling",
               luo="PC6 Neiguan", he_sea="PC3 Quze", xi_cleft="PC4 Ximen",
               confluent="PC6 -- opens Yin Wei Mai (paired w/ SP4) -- most-used confluent pairing in clinic",
               command="none", crossing="NONE -- exam trap, matches HT (only 2 primary channels w/ zero crossing points)",
               first_last="PC1 Tianchi / PC9 Zhongchong", accent=FIREMIN),
    "SJ": dict(name="San Jiao / Triple Energizer", full="San Jiao (Triple Energizer) Meridian of Hand-Shaoyang",
               n_points=23, element="Fire (Ministerial)", polarity="Yang", clock="9-11 PM", direction="Hand -> Head",
               pertains="San Jiao (Triple Burner)", connects="Pericardium",
               back_shu="BL22 Sanjiaoshu", front_mu="CV5 Shimen", yuan="SJ4 Yangchi",
               luo="SJ5 Waiguan", he_sea="SJ10 Tianjing", xi_cleft="SJ7 Huizong",
               confluent="SJ5 -- opens Yang Wei Mai (paired w/ GB41)",
               command="none", crossing="10+ -- shares crossing points with GB around head/ear/shoulder, plus GV14, SI12",
               first_last="SJ1 Guanchong / SJ23 Sizhukong", accent=FIREMIN),
    "GB": dict(name="Gallbladder", full="Gallbladder Meridian of Foot-Shaoyang", n_points=44, element="Wood",
               polarity="Yang", clock="11 PM-1 AM", direction="Head -> Foot", pertains="Gallbladder", connects="Liver",
               back_shu="BL19 Danshu", front_mu="GB24 Riyue (own)", yuan="GB40 Qiuxu",
               luo="GB37 Guangming", he_sea="GB34 Yanglingquan (also Hui-Meeting Sinews)", xi_cleft="GB36 Waiqiu",
               confluent="GB41 Zulinqi -- opens Dai Mai (paired w/ SJ5)",
               command="none",
               crossing="12, across 6 meridians (SJ, LR, PC, SI, ST, GV) -- unique zig-zag \"Z-shape\" head course",
               first_last="GB1 Tongziliao / GB44 Zuqiaoyin", accent=WOOD),
    "LR": dict(name="Liver", full="Liver Meridian of Foot-Jueyin", n_points=14, element="Wood", polarity="Yin",
               clock="1-3 AM", direction="Foot -> Chest", pertains="Liver", connects="Gallbladder",
               back_shu="BL18 Ganshu", front_mu="LR14 Qimen (own)", yuan="LR3 Taichong",
               luo="LR5 Ligou", he_sea="LR8 Ququan", xi_cleft="LR6 Zhongdu",
               confluent="none directly (LR13 is the SP Front-Mu; LR14 is LR's own Front-Mu)",
               command="none",
               crossing="6, shared with CV (2) and SP (1) around the genital/abdomen region",
               first_last="LR1 Dadun / LR14 Qimen -- smallest Yin channel of the foot, crosses IN FRONT of SP at 8 cun above medial malleolus (the one exception)",
               accent=WOOD),
}

CHANNEL_ORDER = ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "SJ", "GB", "LR"]

# ---------------------------------------------------------------------------
# CHANNEL CONTENT -- the actual teaching content (functions, indications,
# highest-yield points explained, clinical pearls) that a real Study Guide
# needs beyond the bare ID-card facts above. Sourced from each week's
# verified Study Guide content module / Cram Sheet, not re-derived from
# CHANNEL_META.
# ---------------------------------------------------------------------------
CHANNEL_CONTENT = {
    "LU": dict(
        functions=["Governs Qi and respiration (\"the Lung governs Qi\")",
                   "Diffuses and descends Lung Qi; regulates the water passages",
                   "Controls the skin and body hair (the exterior defense layer)",
                   "LU1 is the Lung's OWN Front-Mu -- unusual, since most Front-Mu points sit on the Ren Mai or another channel",
                   "Internally, LU connects to the Middle Jiao/Stomach -- this is why cough is sometimes treated by needling ST or SP points"],
        indications=["Cough, wheezing, shortness of breath, chest fullness and distension, asthma",
                     "Sore throat, nasal congestion, voice/throat disorders",
                     "Pain along the channel: chest, shoulder, medial arm to thumb",
                     "Edema (Lung governs the upper water passages)",
                     "Susceptibility to external pathogenic invasion (Wind-Cold/Wind-Heat) via the skin/exterior"],
        highest_yield=[("LU7", "Luo + Confluent + Command", "Opens Ren Mai; commands head/neck; cough, headache, stiff neck -- most loaded point on LU"),
                       ("LU9", "Yuan-Source + Shu-Stream", "Radial pulse site; tonifies Lung Qi, chronic cough/asthma"),
                       ("LU5", "He-Sea", "Clears heat, descends rebellious Lung Qi; cough, asthma, acute throat"),
                       ("LU1", "Front-Mu (own)", "Chest fullness, grief/sadness, cough -- diagnostic point for Lung"),
                       ("LU11", "Jing-Well", "Sore throat, fever, loss of consciousness -- emergency point")],
        pearls=["LU1 is the Lung's own Front-Mu -- most channels' Front-Mu sits elsewhere; this is an unusual, high-yield exam fact.",
                "LU7 carries THREE roles at once (Luo + Confluent opening Ren Mai + Command head/neck) -- one of the most heavily-loaded points in the whole course.",
                "LU and LI have an internal-organ link through the Middle Jiao/Stomach -- cough unresponsive to normal treatment can respond to LI points, and vice versa for constipation.",
                "Point-count asymmetry is a pattern, not an exception: LI (20 pts) nearly doubles LU (11 pts) -- the same pattern repeats HT(9)/SI(19)."]),
    "LI": dict(
        functions=["Governs transmission and transformation -- moves waste through the digestive tract",
                   "Has nearly DOUBLE the points of LU (20 vs. 11) despite being the Yang/Fu partner",
                   "Connects to LOWER teeth and gums specifically (upper teeth/gums = ST channel)",
                   "Has multiple crossing points (GV14, GV26, ST4, and an SI point near the face) -- more than most channels covered early in the course",
                   "Back-Shu: BL25 Dachangshu | Front-Mu: ST25 Tianshu (on the ST channel, not LI's own)"],
        indications=["Toothache (especially LOWER teeth) -- near-immediate relief documented for LI4",
                     "Sore/swollen throat, nasal problems, facial paralysis, loss of smell",
                     "Pain along the channel: index finger, wrist, forearm, shoulder, neck",
                     "Abdominal pain, borborygmus, constipation or diarrhea",
                     "Constipation unresponsive to normal treatment can respond to LU points (interior-exterior pair)"],
        highest_yield=[("LI4", "Yuan-Source + Command (face/mouth)", "FORBIDDEN in pregnancy; near-immediate toothache relief; general analgesic point"),
                       ("LI11", "He-Sea", "Clears heat, especially heat in the Blood; fever, skin disorders, hypertension"),
                       ("LI20", "Last point, crossing to ST", "Nasal congestion, loss of smell, facial paralysis"),
                       ("LI1", "Jing-Well", "Sore throat, fever, loss of consciousness")],
        pearls=["LI4 Hegu and toothache: near-immediate relief of lower-tooth pain is a real, citable clinical application.",
                "Upper vs. lower teeth is one of the most commonly tested facial-anatomy facts: LI = LOWER teeth/gums, ST = UPPER.",
                "The interior-exterior pair in practice: cough that won't resolve can respond to LI points; constipation that won't resolve can respond to LU points.",
                "Point-count asymmetry: LI (20) nearly doubles LU (11) -- the Yang/Fu channel consistently carries more points than its Yin/Zang partner."]),
    "ST": dict(
        functions=["Governs \"reception and ripening\" of food -- the root of Postnatal Qi and Blood production together with SP",
                   "Descends turbid Qi (opposite of SP, which ascends the clear) -- ST pathology often shows REBELLIOUS/ascending symptoms (vomiting, belching, nausea)",
                   "Only channel to pass through the NIPPLE -- ST17 Ruzhong is a landmark only, never needled",
                   "Has 11 crossing points -- the MOST of any single primary channel",
                   "True pathway origin is LI20 (a crossing point of the LI channel) -- ST1 is only the first NUMBERED point"],
        indications=["Facial pain, toothache (UPPER teeth specifically), facial paralysis/deviation, sore throat",
                     "Abdominal distension, pain, vomiting, belching -- Stomach-Qi rebelling upward",
                     "Mania/agitation along the Yangming excess-heat pattern (classic \"Yangming madness\")",
                     "Pain along the channel: face, chest, abdomen, anterior leg, dorsum of foot",
                     "Mastitis and breast disorders (ST passes directly through breast tissue)"],
        highest_yield=[("ST36", "He-Sea + Command Abdomen + Lower He-Sea (own)", "#1 tonic point in TCM; immunity, anti-inflammation, digestion"),
                       ("ST40", "Luo-Connecting", "#1 phlegm-resolving point in all of TCM"),
                       ("ST25", "Front-Mu of LARGE INTESTINE (not Stomach)", "diarrhea, constipation, borborygmus"),
                       ("ST44", "Ying-Spring", "Yangming heat; UPPER toothache specifically"),
                       ("ST34", "Xi-Cleft", "ACUTE stomach pain, gastritis"),
                       ("ST9", "Window of Heaven", "blood pressure, goiter -- carotid region, needle with care"),
                       ("ST42", "Yuan-Source", "dorsum of foot, the highest point on the foot")],
        pearls=["ST begins at LI20, not ST1 -- ST1 Chengqi is only the first NUMBERED point along the pathway.",
                "UPPER teeth/gums = ST channel. LOWER teeth/gums = LI channel -- a direct, frequently-tested distinction.",
                "ST25 is the Front-Mu of the LARGE INTESTINE, not Stomach -- Stomach's own Front-Mu is CV12 Zhongwan, on a completely different channel.",
                "ONLY the Stomach channel passes through the nipple -- nipple pain or numbness points to ST.",
                "LI hands off to ST, not to SP -- a classic circuit-continuity trap when reciting the Outer Circuit."]),
    "SP": dict(
        functions=["Governs transportation and transformation of food/fluids -- produces Qi and Blood together with ST",
                   "Ascends the clear (opposite of ST, which descends the turbid) -- SP pathology often shows sinking/prolapse symptoms",
                   "Controls the Blood -- keeps Blood within the vessels (SP deficiency -> bleeding disorders)",
                   "Governs the muscles and four limbs; opens into the mouth, manifests in the lips",
                   "ONLY channel that spreads across the LOWER surface of the tongue"],
        indications=["Abdominal distension, poor appetite, loose stools, fatigue/heaviness of the limbs",
                     "Edema, especially of the lower body (SP governs transformation of dampness)",
                     "Irregular or heavy menstruation, easy bruising, bleeding disorders (Spleen not controlling Blood)",
                     "Prolapse-type conditions (organ prolapse, hemorrhoids) -- Sinking of Spleen Qi",
                     "Pain along the channel: medial leg, knee, groin"],
        highest_yield=[("SP6", "3-Yin Crossing (SP/LR/KI)", "gynecological disorders; FORBIDDEN IN PREGNANCY"),
                       ("SP9", "He-Sea", "#1 dampness-resolving point in TCM; edema, knee disorders"),
                       ("SP10", "Sea of Blood", "skin disorders, itching, irregular menstruation"),
                       ("SP4", "Luo-Connecting + Confluent", "opens Chong Mai; pairs with PC6"),
                       ("SP3", "Shu-Stream + Yuan-Source", "tonifies Spleen Qi; heaviness, fatigue"),
                       ("SP8", "Xi-Cleft", "ACUTE dysmenorrhea, abdominal pain"),
                       ("SP21", "Great (Major) Luo", "whole-body pain, weak limbs")],
        pearls=["The 8-cun crossover with LR is the ONLY distribution exception among all 12 meridians -- below 8 cun above the medial malleolus SP runs posterior to LR; above it, SP moves anterior.",
                "ONLY the Spleen channel spreads over the LOWER surface of the tongue (Kidney reaches the ROOT of the tongue -- a related but distinct fact).",
                "SP connects internally to HT, not to LI -- SP hands off to Heart at the end of the Outer Circuit, opening the Inner/Posterior Circuit.",
                "SP4 opens the Chong Mai specifically -- not Ren, not Du -- paired with PC6.",
                "The Front-Mu of Spleen is LR13 Zhangmen -- it sits on the LIVER channel, not SP's own pathway."]),
    "HT": dict(
        functions=["Governs Blood and the vessels (\"the Heart controls the pulse\")",
                   "Houses the Shen (spirit/mind) -- the Heart \"stores the Shen\"",
                   "Has ZERO crossing points -- the only primary channel (tied with PC) with none",
                   "Fewest total points of any primary channel (9)",
                   "Back-Shu: BL15 Xinshu | Front-Mu: CV14 Juque"],
        indications=["Palpitations, chest pain (Heart itself)",
                     "Insomnia, excessive dreaming, poor memory",
                     "Mental-emotional disturbance: anxiety, mania, incoherent speech, loss of consciousness (Shen disturbance)",
                     "Pain along the channel: axilla, medial arm, elbow, forearm to little finger",
                     "Heat in the palms, dry throat, thirst"],
        highest_yield=[("HT7", "Shu-Stream + Yuan-Source", "calms Shen; #1 point for anxiety, insomnia, palpitations"),
                       ("HT3", "He-Sea", "clears heart fire; fear, arm pain along the channel"),
                       ("HT6", "Xi-Cleft", "night sweats, acute heart pain"),
                       ("HT9", "Jing-Well", "emergency point: severe heart pain, palpitations, revives consciousness"),
                       ("HT5", "Luo-Connecting", "links to SI; treats disorders of both channels")],
        pearls=["HT is the smallest channel (9 points) but governs the Shen -- clinically central for anxiety, insomnia, and emotional disorders despite its small point count.",
                "HT has ZERO crossing points -- the only one of the 12 primary channels with none on its external pathway, tied with PC.",
                "HT7 Shenmen literally means \"Spirit Gate\" -- as both Shu-Stream and Yuan-Source, it's the single most important point for calming an agitated Shen.",
                "Primary Fire (HT/SI) vs. Ministerial Fire (PC/SJ): do not conflate these -- they open different circuits (Posterior vs. Middle)."]),
    "SI": dict(
        functions=["Governs \"separation of the pure from the impure\" in digestion (receives food from Stomach, separates nutrients from waste)",
                   "More than double HT's point count (19 vs. 9), same pattern as LU(11)/LI(20)",
                   "Crosses BL1 and GB14 on its facial branches -- unlike HT, which has none",
                   "SI3 opens the Du Mai (paired with BL62) -- the only confluent point on this channel",
                   "Back-Shu: BL27 Xiaochangshu | Front-Mu: CV4 Guanyuan"],
        indications=["Swelling of the cheek and neck, jaw pain, deafness, tinnitus",
                     "Pain along the postero-lateral shoulder, arm, and elbow; stiff neck, sore throat",
                     "Abdominal pain and distension, borborygmus, diarrhea or constipation",
                     "Excess breast milk / lactation problems",
                     "Mental disorders -- SI's internal course also links to Shen disturbance via the Heart"],
        highest_yield=[("SI3", "Shu-Stream + Confluent", "opens Du Mai (pairs with BL62); spine, neck, febrile disease"),
                       ("SI4", "Yuan-Source", "wrist/finger pain, febrile disease"),
                       ("SI8", "He-Sea", "elbow/arm disorders, mental-emotional Fire patterns"),
                       ("SI19", "Last point", "tinnitus, deafness, ear disorders"),
                       ("SI1", "Jing-Well", "excess breast milk / lactation problems")],
        pearls=["SI's Lower He-Sea sits on a DIFFERENT channel (ST39 Xiajuxu, on the Stomach channel) -- true for all six Fu organs.",
                "SI3 Houxi is both Shu-Stream AND a Confluent point opening the Du Mai (paired with BL62) -- key for spine/neck disorders and febrile disease.",
                "SI point count mirrors the LU/LI pattern: SI (19) more than doubles HT (9), just as LI (20) nearly doubles LU (11).",
                "The Posterior/Inner Circuit begins this pairing: HT (chest to hand) -> SI (hand to head), continuing next with BL and KI."]),
    "BL": dict(
        functions=["Running-course function: two branches cross the head/brain -> headache; two long parallel lines run the ENTIRE back -> low back pain, sciatica-type pain",
                   "Internal-organ function: pertains to the Bladder -> urination disorders; acupuncture is particularly effective for urinary retention",
                   "Back-Shu bridge function: BL13-BL28 are the Back-Shu (transport) points for ALL 12 zang-fu organs",
                   "The two parallel lines on the back (1.5 cun and 3 cun lateral to the spine) run SIMULTANEOUSLY, not as a sequential loop",
                   "Largest channel in the body: 67 points, 5 branches"],
        indications=["Headache (from the two branches crossing the head/brain)",
                     "Low back pain, sciatica-type leg pain, calf pain, stiff leg (from the long parallel back lines)",
                     "Urination disorders -- retention, incontinence (Bladder's internal organ function)",
                     "Virtually any organ disorder, treated via the corresponding Back-Shu point (BL13-BL28)",
                     "Eye disorders (BL1 region), difficult labor and fetal malposition (BL60, BL67)"],
        highest_yield=[("BL40", "He-Sea + Command (back)", "clears summer-heat; low back pain"),
                       ("BL60", "Jing-River", "called the \"aspirin of acupuncture\" -- headache, pain anywhere along the pathway, difficult labor"),
                       ("BL67", "Jing-Well", "corrects fetal malposition with moxibustion; labor induction"),
                       ("BL62", "Confluent (Yang Qiao Mai)", "sits close to BL63 Xi-Cleft below the lateral malleolus"),
                       ("BL13-BL28", "Back-Shu series", "organ transport points -- treat the corresponding zang-fu organ directly")],
        pearls=["TRAP: BL does NOT connect to the Lung -- its only internal connection is Kidney. Do not confuse with the Metal pathway.",
                "The two parallel back lines run SIMULTANEOUSLY, confirmed directly in Q&A -- not a sequential up-then-down loop.",
                "BL has 14 crossing points total, shared specifically with GV and GB, concentrated around the head.",
                "BL7 (Tongtian) is NOT the vertex-joining point -- that's GV20 (Baihui), which BL merely joins at the vertex.",
                "BL40 -> BL54 -> BL57 sequence matters for running-course quiz questions: popliteal crease -> upper thigh/sacrum -> calf belly (8 cun below BL40)."]),
    "KI": dict(
        functions=["Stores Essence (Jing) and grasps Qi (governs respiration at its root) -- treats asthma-type presentations via the internal Lung connection",
                   "Governs water metabolism, bone, marrow, and hearing",
                   "Running-course function: pathway curves behind the medial malleolus/heel -> heel pain is a direct clinical cue",
                   "Terminates at the root of the tongue -> dry mouth, sore throat, tongue-root diagnostic signs",
                   "27 points, 3 branches -- fewer points than BL despite connecting to more internal organs (Lung, Liver, Heart, plus Bladder)"],
        indications=["Heel pain, lower back pain, weak knees (classic Kidney-deficiency pattern)",
                     "Asthma-type breathing difficulty (Kidney \"grasps\" Qi at its root)",
                     "Dry mouth, sore throat, tongue-root symptoms",
                     "Hearing disorders, bone/marrow disorders",
                     "Reproductive and urogenital disorders, edema (water metabolism)"],
        highest_yield=[("KI1", "Jing-Well", "resuscitation, calms the spirit; used in hypertension"),
                       ("KI3", "Yuan-Source + Shu-Stream", "the key tonic point for Kidney Yin AND Yang"),
                       ("KI6", "Confluent (Yin Qiao Mai)", "insomnia, sore throat, irregular menstruation"),
                       ("KI7", "Jing-River", "tonifies Kidney Yang; edema; night sweats (often paired with HT6)"),
                       ("KI27", "Last point", "final point of the channel, inferior border of the clavicle -- links functionally into the chest before Pericardium begins")],
        pearls=["CLINICAL TEACHING POINT (verbatim emphasis): heel pain -- think Kidney first. The channel curves directly behind the medial malleolus and through the heel.",
                "KI intersects the Spleen channel at SP6 (Sanyinjiao) on the medial leg -- a shared crossing point, not a KI-numbered point.",
                "Do not confuse KI3 (Taixi, Yuan-Source AND Shu-Stream -- dual role) with KI7 (Fuliu, Jing-River only), 2 cun proximal, anterior to the Achilles tendon.",
                "KI6 (Zhaohai) is the Confluent point opening the Yin Qiao Mai -- do not mix up with KI7, a Jing-River point with a different clinical profile.",
                "Week 5 completes the Posterior/Inner Circuit: HT+SI (Week 4) plus BL+KI (this week) form the full four-channel circuit."]),
    "PC": dict(
        functions=["Protects the Heart -- shares many indications with HT (palpitations, chest/mental disorders)",
                   "Governs Blood circulation and the vessels alongside HT; regulates sexual/reproductive function via the San Jiao lower-jiao connection",
                   "ZERO crossing points -- exam trap identical to HT (the only two channels with none)",
                   "Runs on the MIDDLE line of the arm, between LU (anterior) and HT (posterior)",
                   "PC6 and PC8 are the most clinically-used points (safe, effective, hand/forearm); points on the chest (PC1) are used cautiously due to pneumothorax risk"],
        indications=["Palpitations, chest pain, angina-type presentations (shares much of HT's territory)",
                     "Mental-emotional disturbance: anxiety, irritability, mania (PC8 Laogong is a classical Ghost Point for severe presentations)",
                     "Stomach/epigastric disorders (via PC6's action on the Middle Jiao)",
                     "Nausea, vomiting, morning sickness (PC6 is a first-line anti-nausea point)",
                     "Insomnia, poor memory -- Shen-related, similar to HT"],
        highest_yield=[("PC6", "Luo-Connecting + Confluent", "opens Yin Wei Mai (paired w/ SP4) -- most-used confluent pairing in clinic; nausea, chest, stomach"),
                       ("PC7", "Yuan-Source", "wrist pulse-adjacent tonic point"),
                       ("PC3", "He-Sea", "clears heat, descends rebellious Qi from the chest"),
                       ("PC8", "Ghost Point (classical)", "one of Sun Simiao's 13 Ghost Points -- severe mental-emotional disturbance"),
                       ("PC4", "Xi-Cleft", "acute chest pain, acute palpitations")],
        pearls=["PC and HT are the ONLY two primary channels with zero crossing points -- a classic paired exam trap.",
                "PC6 + SP4 is the most-used confluent pairing in clinic -- both Luo AND Confluent points, opening Yin Wei Mai + Chong Mai together.",
                "PC runs the MIDDLE line of the arm -- between LU (anterior) and HT (posterior) -- an easy \"which channel is this\" positional trap.",
                "Ministerial Fire (PC/SJ) is a separate pairing from Primary Fire (HT/SI) -- different circuit, different clinical character."]),
    "SJ": dict(
        functions=["No physical organ -- a \"function organ\" governing the Upper/Middle/Lower Jiao (fluid pathways and overall Qi transformation)",
                   "Governs water passage/metabolism -- controls the movement of water through the three jiao",
                   "Shares extensive crossing points with GB around the head, ear, and shoulder (both are Shaoyang channels)",
                   "SJ5 opens the Yang Wei Mai (paired with GB41) -- treats exterior wind-heat / alternating chills and fever",
                   "Active 9-11 PM -- the San Jiao \"connects all organs\" and is classically associated with rest during this window"],
        indications=["Ear disorders: tinnitus, deafness, ear pain/fullness (SJ reaches deep around the ear)",
                     "Lateral head and temple pain, alongside GB",
                     "Alternating chills and fever, exterior Wind-Heat presentations (via SJ5/Yang Wei Mai)",
                     "Edema and water-metabolism disorders (SJ governs fluid pathways)",
                     "Throat and eye-region disorders on the lateral face"],
        highest_yield=[("SJ5", "Luo-Connecting + Confluent", "opens Yang Wei Mai (paired w/ GB41); exterior Wind-Heat, alternating chills/fever"),
                       ("SJ4", "Yuan-Source", "wrist disorders, general Qi regulation"),
                       ("SJ10", "He-Sea", "clears heat, ear disorders"),
                       ("SJ17", "Crossing point (shared with GB)", "deep ear point, facial paralysis, tinnitus"),
                       ("SJ23", "Last point", "lateral eyebrow -- headache, eye disorders")],
        pearls=["SJ has no corresponding physical organ in Western anatomy -- it's a classical \"function\" governing fluid pathways across all three jiao.",
                "SJ and GB share extensive crossing points around the head/ear/shoulder because both are Shaoyang channels -- the \"same-name channel\" rule.",
                "SJ5 opening the Yang Wei Mai (paired with GB41 opening Dai Mai) is the Middle Circuit's confluent pairing -- contrast with PC6+SP4 from the other circuit.",
                "Active 9-11 PM -- classic sleep-hygiene teaching point tied directly to this channel's clock position."]),
    "GB": dict(
        functions=["3rd largest channel (44 points) after BL (67) and ST (45)",
                   "Unique zigzag (\"Z-shape\") course on the head -- an exam-testable visual signature unlike any other channel",
                   "GB34 is the Hui-Meeting Point for sinews/tendons -- master point for tendon/ligament disorders",
                   "GB41 opens the Dai Mai (paired with SJ5) -- the only channel whose confluent point connects to an EV that encircles the waist",
                   "Alternating fever/chills + bitter taste in the mouth = classic Shaoyang syndrome, specific to GB"],
        indications=["Lateral headache, migraine, dizziness/vertigo (GB's zigzag head course)",
                     "Hypochondriac (rib-side) pain, alternating fever and chills, bitter taste in the mouth (Shaoyang syndrome)",
                     "Tendon/sinew disorders, muscle cramping and spasm (GB34, Hui-Meeting of Sinews)",
                     "Lateral-body and hip pain along the long leg pathway",
                     "Eye disorders (GB begins at the outer canthus)"],
        highest_yield=[("GB34", "He-Sea + Hui-Meeting (Sinews)", "master point for tendon/ligament/muscle-spasm disorders"),
                       ("GB20", "high clinical use (not a special point)", "head/neck tension, headache -- one of the most-used GB points in clinic"),
                       ("GB41", "Confluent (Dai Mai)", "paired with SJ5; flank/waist and lateral-body disorders"),
                       ("GB24", "Front-Mu (own)", "hypochondriac pain, Liver-Gallbladder disharmony"),
                       ("GB21", "high clinical use -- FORBIDDEN in pregnancy", "strong descending/labor-inducing action")],
        pearls=["GB has 12 crossing points across 6 meridians (SJ, LR, PC, SI, ST, GV) -- the full 2026-deck-confirmed list resolved an earlier discrepancy.",
                "GB21 is FORBIDDEN in pregnancy -- a strong descending, labor-inducing action consistent with GB's overall \"descending\" channel character.",
                "GB34 + LR3 is a classic combination for tendon disorders with a Liver-Qi component (tight, spasming muscles).",
                "GB's unique Z-shape head course is its own visual identifier -- no other channel zigzags this way."]),
    "LR": dict(
        functions=["Governs the smooth flow of Qi throughout the body -- Liver Qi stagnation is the most common TCM pattern taught from this channel",
                   "Stores Blood; opens into the eyes (Liver Blood nourishes the eyes) -- explains why LR reaches the eye system and the vertex",
                   "ONLY primary channel to reach the VERTEX (GV20) -- vertex headache points to Liver",
                   "Crosses IN FRONT of SP at 8 cun above the medial malleolus -- the single exception to the standard leg-Yin ordering rule",
                   "Completes the 12-channel Qi cycle by connecting back to LU internally -- \"the total basic circulation of the 12 primary meridians\""],
        indications=["Vertex headache, dizziness, eye disorders (blurry vision, red/dry eyes) -- Liver Blood/Qi disorders",
                     "Emotional disorders: irritability, depression, mood swings (Liver Qi stagnation)",
                     "Menstrual irregularity, genital/reproductive disorders (LR pathway reaches the genitals)",
                     "Hypochondriac/rib-side pain, distension",
                     "Muscle cramping, tremor (Liver governs the sinews together with GB)"],
        highest_yield=[("LR3", "Yuan-Source", "the single most important point on LR -- smooths Liver Qi, used in \"Four Gates\" with LI4"),
                       ("LR13", "Front-Mu of SPLEEN + Hui-Meeting of Zang", "DOUBLE designation -- easy exam mix-up, sits on LR channel but serves SP"),
                       ("LR14", "Front-Mu of LIVER (own)", "Liver-Spleen disharmony, hypochondriac pain"),
                       ("LR8", "He-Sea", "nourishes Liver Blood/Yin, paired with KI10"),
                       ("LR1", "Jing-Well", "first point; uterine bleeding, emergency use")],
        pearls=["LR3 + LI4 = the \"Four Gates\" (Si Guan) -- classic combination that smooths Qi and moves Blood broadly, used for pain of many origins.",
                "LR13 carries a DOUBLE special-point designation (Front-Mu of SP + Hui-Meeting of all Zang organs) -- easy to mix up on an exam with LR14 (LR's own Front-Mu).",
                "LR is the ONLY primary channel reaching the vertex (GV20) -- vertex headache is a Liver-pattern clinical cue.",
                "The 8-cun SP/LR crossover is the single exception to the standard leg-Yin ordering -- LR crosses in FRONT of SP at that point."]),
}

# ---------------------------------------------------------------------------
# SPECIAL POINT CATEGORY DEFINITIONS -- what each category actually MEANS,
# for the Master Decoder's missing "glossary" page.
# ---------------------------------------------------------------------------
CATEGORY_DEFINITIONS = [
    ("Five Shu (Transport) Points", NAVY,
     "A set of 5 points on each of the 12 primary meridians, located distal to the elbows/knees, through which "
     "Qi is said to flow like water: Jing-Well (emerges) -> Ying-Spring (flows) -> Shu-Stream (pours) -> "
     "Jing-River (travels) -> He-Sea (enters). Each stage has a distinct clinical application (first aid, "
     "febrile disease, joint pain, externally-contracted disease, and Fu-organ disorders, respectively)."),
    ("Yuan-Source Point", NAVY,
     "The point where a channel's \"Source Qi\" (Yuan Qi) is most concentrated and accessible -- effectively "
     "the primary tonification/regulation point for that channel's associated organ. On Yin channels it "
     "coincides with the Shu-Stream point; on Yang channels it is a separate 6th point."),
    ("Luo-Connecting (Luo) Point", AMBER_LUO,
     "The point where a small branch (\"Luo-vessel\") splits off from the main channel and runs to its "
     "internally-externally paired channel, physically linking the two. Used to treat either channel from "
     "one point, and clinically significant for chronic/deficiency patterns of the paired organ."),
    ("Back-Shu (Transport) Point", WATER,
     "One of 12 points on the Bladder channel's inner back line, each directly overlying/associated with a "
     "specific Zang-Fu organ. Back-Shu points are the most direct route to influence an organ's Qi from the "
     "body's posterior surface -- used heavily in both diagnosis (palpation tenderness) and treatment."),
    ("Front-Mu (Alarm) Point", EARTH,
     "A point on the chest or abdomen, on the front of the body, most closely associated with a specific "
     "Zang-Fu organ -- often located near that organ's physical location. Front-Mu points are especially "
     "useful for ACUTE organ disorders and, like Back-Shu points, are diagnostically tender on palpation."),
    ("Xi-Cleft (Accumulation) Point", FIREMIN,
     "A point where a channel's Qi and Blood pool or \"accumulate\" more deeply than usual. The go-to point "
     "category for ACUTE, often painful presentations of that channel's pathology -- acute pain, acute "
     "bleeding, or acute spasm -- distinct from the more chronic focus of He-Sea points."),
    ("He-Sea (Uniting) Point", FIRE,
     "The point nearest the elbow or knee where a channel's Qi is said to converge/\"enter\" most fully, like "
     "a river reaching the sea. Classically used for disorders of the Six Fu (hollow) organs and for "
     "rebellious/reversed Qi (e.g., vomiting, diarrhea)."),
    ("Lower He-Sea Point", FIRE,
     "A special subset of He-Sea points specifically for the 6 Fu organs, located on the leg. Three Fu "
     "organs (ST, GB, BL) use their own He-Sea point; the other three (LI, SI, SJ) BORROW a point on a "
     "different Foot channel entirely -- a frequently-tested distinction."),
    ("Confluent (Opening) Point", TEAL,
     "One of 8 points on the 12 primary meridians that each \"open\" (activate) one of the 8 Extraordinary "
     "Vessels. Confluent points are the ONLY way to access an Extraordinary Vessel's function through "
     "needling, since the vessels themselves (except GV/CV) have no points of their own."),
    ("Command Point", GOLD,
     "One of a small classical set of points (the Four Command Points/Si Zong Xue) each said to \"command\" "
     "-- have outsized therapeutic reach over -- an entire body region (abdomen, back, face/mouth, head/nape), "
     "regardless of where the specific complaint is located within that region."),
    ("Hui-Meeting (Influential) Point", WOOD,
     "One of 8 points, each governing a broad tissue/substance category (Qi, Blood, Bone, Marrow, Sinew, "
     "Vessels, and the Zang or Fu organs as groups) rather than a single channel or organ -- used when a "
     "condition affects that category broadly, cutting across multiple channels."),
    ("Crossing (Meeting) Point", GRAY,
     "A point where two or more channels physically intersect or run together for a stretch. A crossing "
     "point can be needled to influence every channel that passes through it, not just the channel it's "
     "numbered under -- explaining why some points (e.g. GV14, SP6) show up in multiple channels' pathology."),
]

# ---------------------------------------------------------------------------
# FIVE SHU (TRANSPORT) POINTS -- full master table, 12 x 5 = 60 points.
# Verified in Week 9 Special Points Decoder / master table.
# ---------------------------------------------------------------------------
FIVE_SHU_DEFINITION = (
    "A specific group of 5 points on each of the 12 primary meridians, situated distal to the elbows/knees: "
    "Jing-Well (\u201cwhere it emerges\u201d, tips of fingers/toes, first aid/resuscitation), Ying-Spring "
    "(\u201cwhere it flows\u201d, before MCP/MTP, febrile disease), Shu-Stream (\u201cwhere it pours\u201d, "
    "after MCP/MTP, heaviness & joint pain), Jing-River (\u201cwhere it travels\u201d, forearm/lower leg, "
    "externally-contracted disease), He-Sea (\u201cwhere it enters\u201d, near elbow/knee, disorders of the six Fu)."
)
FIVE_SHU_MASTER = [
    dict(m="Lung (LU)", cycle="Outer", accent=METAL, pts=["LU11 Shaoshang", "LU10 Yuji", "LU9 Taiyuan", "LU8 Jingqu", "LU5 Chize"]),
    dict(m="Large Intestine (LI)", cycle="Outer", accent=METAL, pts=["LI1 Shangyang", "LI2 Erjian", "LI3 Sanjian", "LI5 Yangxi", "LI11 Quchi"]),
    dict(m="Stomach (ST)", cycle="Outer", accent=EARTH, pts=["ST45 Lidui", "ST44 Neiting", "ST43 Xiangu", "ST41 Jiexi", "ST36 Zusanli"]),
    dict(m="Spleen (SP)", cycle="Outer", accent=EARTH, pts=["SP1 Yinbai", "SP2 Dadu", "SP3 Taibai", "SP5 Shangqiu", "SP9 Yinlingquan"]),
    dict(m="Heart (HT)", cycle="Inner", accent=FIRE, pts=["HT9 Shaochong", "HT8 Shaofu", "HT7 Shenmen", "HT4 Lingdao", "HT3 Shaohai"]),
    dict(m="Small Intestine (SI)", cycle="Inner", accent=FIRE, pts=["SI1 Shaoze", "SI2 Qiangu", "SI3 Houxi", "SI5 Yanggu", "SI8 Xiaohai"]),
    dict(m="Bladder (BL)", cycle="Inner", accent=WATER, pts=["BL67 Zhiyin", "BL66 Zutonggu", "BL65 Shugu", "BL60 Kunlun", "BL40 Weizhong"]),
    dict(m="Kidney (KI)", cycle="Inner", accent=WATER, pts=["KI1 Yongquan", "KI2 Rangu", "KI3 Taixi", "KI7 Fuliu", "KI10 Yingu"]),
    dict(m="Pericardium (PC)", cycle="Middle", accent=FIREMIN, pts=["PC9 Zhongchong", "PC8 Laogong", "PC7 Daling", "PC5 Jianshi", "PC3 Quze"]),
    dict(m="San Jiao (SJ)", cycle="Middle", accent=FIREMIN, pts=["SJ1 Guanchong", "SJ2 Yemen", "SJ3 Zhongzhu", "SJ6 Zhigou", "SJ10 Tianjing"]),
    dict(m="Gallbladder (GB)", cycle="Middle", accent=WOOD, pts=["GB44 Zuqiaoyin", "GB43 Xiaxi", "GB41 Zulinqi", "GB38 Yangfu", "GB34 Yanglingquan"]),
    dict(m="Liver (LR)", cycle="Middle", accent=WOOD, pts=["LR1 Dadun", "LR2 Xingjian", "LR3 Taichong", "LR4 Zhongfeng", "LR8 Ququan"]),
]
FIVE_SHU_COLS = ["Jing-Well", "Ying-Spring", "Shu-Stream", "Jing-River", "He-Sea"]
FIVE_SHU_YUAN_NOTE = (
    "Yin meridians have NO separate Yuan-Source point -- the Shu-Stream point IS the Yuan point "
    "(e.g. Taiyuan LU9 is both Shu-Stream and Yuan for Lung; Taixi KI3 for Kidney). Yang meridians have a "
    "6th, separate Yuan-Source point beyond the 5 Shu points (e.g. Chongyang ST42, Hegu LI4)."
)

# ---------------------------------------------------------------------------
# EIGHT EXTRAORDINARY VESSELS -- Week 7, verified against 2026 lecture deck
# ---------------------------------------------------------------------------
EXTRAORDINARY_VESSELS = [
    dict(name="Governor Vessel (Du Mai)", abbr="GV", n_points=28, sea="Sea of the Yang Meridians",
         first_last="GV1 Changqiang / GV28 Yinjiao", confluent="SI3 Houxi", partner="BL62 Shenmai (Yang Qiao Mai)",
         course="Perineum -> posterior midline of spine -> nape -> vertex -> forehead -> nose -> upper gum",
         function="Governs Qi of all Yang meridians; keeps body warm; spine/brain disorders", accent=EXTRA),
    dict(name="Conception Vessel (Ren Mai)", abbr="CV", n_points=24, sea="Sea of the Yin Meridians",
         first_last="CV1 Huiyin / CV24 Chengjiang", confluent="LU7 Lieque", partner="KI6 Zhaohai (Yin Qiao Mai)",
         course="Perineum -> anterior midline of abdomen/chest -> throat -> chin",
         function="Receives/bears Qi of all Yin meridians; reproduction, urogenital, CV4/CV12 major tonics",
         accent=EXTRA),
    dict(name="Penetrating Vessel (Chong Mai)", abbr="Chong", n_points=None, sea="Sea of the 12 Meridians / Sea of Blood",
         first_last="One source, three branches (shares 11 KI-channel points as coalescent points)",
         confluent="SP4 Gongsun", partner="PC6 Neiguan (Yin Wei Mai)",
         course="Lower abdomen, runs parallel to Kidney meridian",
         function="Sea of Blood; regulates menstruation and the 12 meridians/zang-fu Qi-Blood", accent=EXTRA),
    dict(name="Girdle/Belt Vessel (Dai Mai)", abbr="Dai", n_points=None, sea="none (structurally unique)",
         first_last="Only vessel that runs HORIZONTALLY, around the waist",
         confluent="GB41 Zulinqi", partner="SJ5 Waiguan (Yang Wei Mai)",
         course="Encircles the waist like a belt", function="Binds/controls all longitudinally-running meridians",
         accent=EXTRA),
    dict(name="Yang Heel Vessel (Yang Qiao Mai)", abbr="Yang Qiao", n_points=None, sea="none",
         first_last="Starts at its confluent point BL62 Shenmai", confluent="BL62 Shenmai", partner="SI3 Houxi (Du Mai)",
         course="Lateral leg -> trunk -> meets Yin Qiao at inner canthus",
         function="Governs wakefulness/activity; balances limb movement with Yin Qiao", accent=EXTRA),
    dict(name="Yin Heel Vessel (Yin Qiao Mai)", abbr="Yin Qiao", n_points=None, sea="none",
         first_last="Starts at its confluent point KI6 Zhaohai", confluent="KI6 Zhaohai", partner="LU7 Lieque (Ren Mai)",
         course="Medial leg -> trunk -> meets Yang Qiao at inner canthus",
         function="Governs calm/rest, promotes sleep -- opposite of Yang Qiao", accent=EXTRA),
    dict(name="Yang Linking Vessel (Yang Wei Mai)", abbr="Yang Wei", n_points=None, sea="none",
         first_last="Connects to all Yang meridians, esp. GV", confluent="SJ5 Waiguan", partner="GB41 Zulinqi (Dai Mai)",
         course="Lateral leg/trunk -> head", function="Dominates exterior of the whole body", accent=EXTRA),
    dict(name="Yin Linking Vessel (Yin Wei Mai)", abbr="Yin Wei", n_points=None, sea="none",
         first_last="Connects to all Yin meridians, esp. CV", confluent="PC6 Neiguan", partner="SP4 Gongsun (Chong Mai)",
         course="Medial leg/trunk -> chest", function="Dominates interior of the whole body", accent=EXTRA),
]
CONFLUENT_PAIRS_QUICK = [
    ("SI3 Houxi", "BL62 Shenmai", "Du Mai + Yang Qiao Mai", "posterior body, spine, neck, febrile disease"),
    ("LU7 Lieque", "KI6 Zhaohai", "Ren Mai + Yin Qiao Mai", "throat, chest, lung, insomnia"),
    ("SP4 Gongsun", "PC6 Neiguan", "Chong Mai + Yin Wei Mai", "chest, heart, stomach -- MOST-used pairing in clinic"),
    ("GB41 Zulinqi", "SJ5 Waiguan", "Dai Mai + Yang Wei Mai", "lateral body, hypochondriac pain, exterior disorders"),
]

# ---------------------------------------------------------------------------
# 15 COLLATERALS (Luo-Connecting) -- Week 8/9
# ---------------------------------------------------------------------------
LUO_15 = [
    ("LU7 Lieque", "LU -> LI", "also opens Ren Mai (Week 7)"),
    ("LI6 Pianli", "LI -> LU", "closest pairing around the wrist to LU7"),
    ("ST40 Fenglong", "ST -> SP", "#1 phlegm point in TCM"),
    ("SP4 Gongsun", "SP -> ST", "also opens Chong Mai"),
    ("HT5 Tongli", "HT -> SI", "1 cun above wrist crease"),
    ("SI7 Zhizheng", "SI -> HT", "5 cun above wrist"),
    ("BL58 Feiyang", "BL -> KI", "7 cun above external malleolus"),
    ("KI4 Dazhong", "KI -> BL", "posterior to internal malleolus"),
    ("PC6 Neiguan", "PC -> SJ", "also opens Yin Wei Mai"),
    ("SJ5 Waiguan", "SJ -> PC", "also opens Yang Wei Mai"),
    ("GB37 Guangming", "GB -> LR", "5 cun above external malleolus"),
    ("LR5 Ligou", "LR -> GB", "5 cun above internal malleolus"),
    ("CV15 Jiuwei", "Ren Mai collateral", "spreads over the FRONT midline/abdomen"),
    ("GV1 Changqiang", "Du Mai collateral", "spreads over the BACK midline"),
    ("SP21 Dabao", "Great (Major) Collateral of Spleen", "covers the LATERAL chest -- why there are 15, not 12"),
]
LUO_RULE = ("Connecting (Luo) points of HAND meridians cluster around the WRIST. Connecting points of FOOT "
            "meridians cluster around the ANKLE/MALLEOLUS. CV/GV/SP-Great-Luo are the exceptions, covering "
            "front midline, back midline, and lateral chest respectively.")

# ---------------------------------------------------------------------------
# DIVERGENT / MUSCLE (SINEW) / CUTANEOUS -- LOW PRIORITY per Dr. Zhang, kept
# brief for completeness only.
# ---------------------------------------------------------------------------
LOW_PRIORITY_NOTE = (
    "Dr. Zhang confirmed live in the Week 9 final-exam review that Divergent Channels and Collaterals detail "
    "is NOT covered in the review portion for the final. Muscle (Sinew) Regions and the 12 Cutaneous Regions "
    "were likewise absent from her review slides. Know the definitions below at a conceptual level only -- do "
    "not spend final-prep time memorizing individual divergent-channel pathways."
)
DIVERGENT_SUMMARY = (
    "12 Divergent Channels branch from the 12 primary meridians and run DEEP into the body to strengthen the "
    "connection with the Zang-Fu organs (unlike the superficial Collaterals). Basic pattern: LI (\u96e2, "
    "\u2018separate/begin\u2019) -> travels through the trunk to the associated organ(s) -> emerges around the "
    "neck/face -> merges into its paired YANG meridian. All Yin divergent channels ultimately merge into a "
    "Yang meridian."
)
SINEW_SUMMARY = (
    "12 Muscle (Sinew) Regions follow the same surface course as their primary meridian but cover a WIDER band "
    "and connect specifically to muscles/tendons -- used clinically for motion dysfunction, muscle pain, and "
    "stiffness (e.g., gua sha, cupping, massage, motor-point needling)."
)
CUTANEOUS_SUMMARY = (
    "12 Cutaneous Regions are the most superficial layer -- the skin-surface reflection of each meridian's "
    "range, first line of defense against external pathogenic invasion. Exception: cutaneous regions connect "
    "BOTH the hand and foot channels of the same Yin/Yang category together (e.g., Hand + Foot Taiyang are "
    "one cutaneous region) -- this is why there are only 6 named cutaneous regions, not 12 separate ones."
)

# ---------------------------------------------------------------------------
# EXAM TRAPS -- consolidated "read these last" facts pulled from every week's
# verified Cram Sheet. This is deliberately the densest, highest-yield page.
# ---------------------------------------------------------------------------
EXAM_TRAPS = [
    ("Naming convention", "3 parts only: Hand/Foot + Yin/Yang + Zang/Fu (e.g. \"Hand Taiyin Lung\"). Element "
     "(Metal, Earth...) is a SEPARATE Five-Phase classification, not part of the formal channel name."),
    ("Point-count doesn't track Yin/Yang", "LI (20) > LU (11); SI (19) > HT (9) -- the Yang/Fu partner almost "
     "always has more points than its Yin/Zang pair, even though it's the \"lesser\" organ in Zang-Fu theory."),
    ("ST begins at LI20, not ST1", "ST1 (Chengqi) is only the first NUMBERED point on the channel -- the true "
     "pathway origin is LI20 Yingxiang on the face, a crossing point of the LI channel."),
    ("UPPER vs LOWER teeth/gums", "UPPER teeth/gums = ST channel. LOWER teeth/gums = LI channel. A classic "
     "Dr. Zhang exam distinction."),
    ("ST25 vs CV12 Front-Mu", "ST25 (Tianshu) = Front-Mu of LARGE INTESTINE. CV12 (Zhongwan) = Front-Mu of "
     "STOMACH. These sit on completely different channels."),
    ("Only ST passes through the nipple", "ST17 Ruzhong = center of nipple -- landmark ONLY, never needled."),
    ("SP is the ONLY channel on the LOWER surface of the tongue", "KI reaches the ROOT of the tongue; SP "
     "spreads over its lower surface -- do not conflate the two tongue relationships."),
    ("SP's 8-cun crossover", "The ONLY distribution exception among all 12 meridians: below 8 cun above the "
     "medial malleolus, SP runs POSTERIOR to LR; above 8 cun, SP moves ANTERIOR (crosses in front of LR)."),
    ("Forbidden-in-pregnancy points", "LI4 Hegu, SP6 Sanyinjiao, BL60 Kunlun (promotes labor), BL67 Zhiyin "
     "(malposition correction via MOXA only, needle contraindicated)."),
    ("Circuit hand-offs (Outer)", "LU->LI at LI1 (fingers). LI->ST at LI20 (face). ST->SP at SP1/ST42 (toe). "
     "SP->HT internally (chest) -- opens the Inner/Posterior Circuit."),
    ("BL does NOT connect to Lung", "BL's only internal connection is Kidney. Do not confuse with the Metal "
     "pathway."),
    ("BL's two back lines run simultaneously", "NOT a sequential up-down loop -- Dr. Zhang confirmed directly "
     "in Q&A: both the 1.5-cun and 3-cun parallel lines run \"at the same time.\""),
    ("BL7 vs GV20", "BL7 Tongtian is NOT the vertex-joining point -- that is GV20 Baihui, which BL merely "
     "joins at the vertex."),
    ("Heel pain -> think Kidney first", "Dr. Zhang's explicit clinical teaching point -- the KI pathway curves "
     "directly behind the medial malleolus and through the heel."),
    ("KI3 vs KI7", "KI3 Taixi = Shu-Stream AND Yuan-Source (dual role), in the malleolus/Achilles depression. "
     "KI7 Fuliu = Jing-River only, 2 cun proximal, anterior to the Achilles tendon."),
    ("PC and HT are the ONLY 2 primary channels with zero crossing points.", "An easy paired exam trap."),
    ("Confluent point pairings never mix elements", "SI3+BL62 (both Yang, posterior); LU7+KI6 (mixed but "
     "classic Yin pairing); SP4+PC6 (both Yin, most clinically used); GB41+SJ5 (both Yang, lateral body)."),
    ("Yuan-Source rule by polarity", "On YIN channels, Yuan-Source = the Shu-Stream point (same point, dual "
     "role). On YANG channels, Yuan-Source is a separate 6th point beyond the 5 Shu points."),
    ("ST36 is He-Sea + Command Abdomen, NOT Yuan-Source.", "ST's actual Yuan-Source is ST42 Chongyang -- don't "
     "let ST36's fame as \"#1 tonic point\" cause you to misassign it."),
    ("GB crossing points: 12 across 6 meridians", "SJ, LR, PC, SI, ST, GV -- includes Yifeng SJ17, Jiaosun "
     "SJ20, Erheliao SJ22, Dadun LR1, Zhangmen LR13, Tianchi PC1, Bingfeng SI12, Tianrong SI17, Tinggong SI19, "
     "Xiaguan ST7, Touwei ST8, Dazhui GV14."),
    ("Extraordinary Vessels have NO pertaining/connecting organs.", "Unlike the 12 primary meridians, the 8 "
     "EVs run superficially and do not pertain to or connect with internal Zang-Fu organs directly."),
    ("Yang Qiao / Yin Qiao \"start\" at their confluent points.", "BL62 (Yang Qiao) and KI6 (Yin Qiao) -- Dr. "
     "Zhang repeated this exact fact live in the Week 9 review as a quiz-recycled item."),
]

# ---------------------------------------------------------------------------
# MASTER DECODER -- category-pivoted special point data (built from
# CHANNEL_META plus classical reference categories not already captured
# per-channel). Tier A = Dr. Zhang's confirmed review emphasis; Tier B =
# quiz-tested / high clinical yield; Tier C = classical/reference, lower
# priority for the final per Dr. Zhang's explicit Week 9 statement.
# ---------------------------------------------------------------------------
DECODER_TIERS = [
    ("TIER A", RED, "Dr. Zhang's confirmed final-exam review emphasis -- know cold"),
    ("TIER B", GOLD, "Quiz-tested (Quiz 1-6) and/or high clinical yield -- know well"),
    ("TIER C", GRAY, "Classical/reference material -- lower priority per Dr. Zhang's Week 9 statement"),
]

LOWER_HE_SEA = [
    ("ST37 Shangjuxu", "Large Intestine", "LI bowel disorders (diarrhea, appendicitis-type pain)"),
    ("ST39 Xiajuxu", "Small Intestine", "SI bowel disorders, lower abdominal pain"),
    ("BL39 Weiyang", "San Jiao", "water metabolism, edema, lower back/leg pain"),
    ("ST36 Zusanli", "Stomach (own)", "master tonic, digestion, immunity"),
    ("GB34 Yanglingquan", "Gallbladder (own)", "also Hui-Meeting of Sinews -- tendons, hypochondriac pain"),
    ("BL40 Weizhong", "Bladder (own)", "also Command Point of the back"),
]
LOWER_HE_SEA_NOTE = (
    "The 6 Fu (hollow) organs each have a Lower He-Sea point on the leg. ST, GB, and BL simply use their "
    "own He-Sea point (already Fu channels). LI, SI, and SJ -- despite being Hand channels -- BORROW a "
    "Lower He-Sea point on a FOOT channel (ST or BL) instead of using a point on their own pathway. This is "
    "a classic exam trap: LI's and SI's Lower He-Sea points are NOT on the LI or SI channel at all."
)

HUI_MEETING_POINTS = [
    ("CV12 Zhongwan", "Fu (Hollow) Organs", "digestive disorders, all six Fu organs"),
    ("LR13 Zhangmen", "Zang (Solid) Organs", "organ-level disharmony, hypochondriac pain"),
    ("CV17 Danzhong", "Qi", "chest Qi stagnation, breathing, lactation"),
    ("BL17 Geshu", "Blood", "all blood disorders -- bleeding, stasis, deficiency"),
    ("BL11 Dazhu", "Bone", "bone disorders, also a classic exterior-releasing point"),
    ("GB39 Xuanzhong (Juegu)", "Marrow", "marrow, brain, spinal cord, also relates to bone marrow"),
    ("GB34 Yanglingquan", "Sinew (Tendon)", "tendons/ligaments, also He-Sea of GB and Lower He-Sea of GB"),
    ("LU9 Taiyuan", "Vessels (Pulse)", "all pulse/vessel disorders, also Yuan-Source of LU"),
]
HUI_MEETING_NOTE = (
    "The 8 Hui-Meeting (Influential) Points are classical CAM/MOA reference material -- each governs a "
    "tissue/substance category rather than a single channel. Not explicitly confirmed as part of Dr. Zhang's "
    "live review, but standard course-textbook material worth recognizing (Tier C)."
)

COMMAND_POINTS_CLASSICAL = [
    ("ST36 Zusanli", "Abdomen", "the #1 tonic point in TCM; He-Sea + Lower He-Sea of ST"),
    ("BL40 Weizhong", "Back", "He-Sea of BL; \"aspirin of acupuncture\""),
    ("LU7 Lieque", "Head / Nape", "Luo of LU; also Confluent point opening Ren Mai"),
    ("LI4 Hegu", "Face / Mouth", "Yuan-Source of LI; FORBIDDEN in pregnancy"),
]
COMMAND_POINTS_NOTE = (
    "The Four Command Points (Si Zong Xue) -- a classical mnemonic distinct from, but often confused with, "
    "the 8 Confluent Points. \"Command\" points treat a whole body REGION; Confluent points open an "
    "Extraordinary Vessel. Some points (LU7, LI4) do double duty as both a Command point AND part of another "
    "special category -- always check whether a question is asking about regional command or vessel confluence."
)

MEETING_CROSSING_SUMMARY = [
    ("ST", "11", "the MOST of any single primary channel -- LI20, BL1, GB3/4/6, SP1, GV24, GV26, CV12/13/24"),
    ("BL", "14", "shared specifically with GV and Gallbladder, concentrated around the head"),
    ("GB", "12", "across 6 meridians (SJ, LR, PC, SI, ST, GV) -- confirmed against the 2026 slide deck"),
    ("SJ", "10+", "shares crossing points with GB around head/ear/shoulder, plus GV14, SI12"),
    ("SP", "6", "abdomen/chest region -- CV3, CV4, CV10, GB24, LR14, LU1"),
    ("LR", "6", "shared with CV (2) and SP (1) around the genital/abdomen region"),
    ("SI / LI", "few", "crosses GV14 and the cheek/eye/shoulder region"),
    ("HT / PC", "0", "the ONLY 2 primary channels with ZERO named crossing points -- classic paired trap"),
]

# Auto-pivot CHANNEL_META into category tables so the Decoder never drifts
# out of sync with the Study Guide's per-channel data.
def _pivot(field):
    return [(abbr, CHANNEL_META[abbr][field]) for abbr in CHANNEL_ORDER]

YUAN_SOURCE_TABLE = _pivot("yuan")
LUO_CONNECTING_TABLE = _pivot("luo")
BACK_SHU_TABLE = _pivot("back_shu")
FRONT_MU_TABLE = _pivot("front_mu")
XI_CLEFT_TABLE = _pivot("xi_cleft")
HE_SEA_TABLE = _pivot("he_sea")

# Back-Shu series organized by point number (ascending along the back) --
# the more clinically useful ordering for a decoder vs. by-channel.
BACK_SHU_SERIES = [
    ("BL13 Feishu", "Lung"), ("BL14 Jueyinshu", "Pericardium"), ("BL15 Xinshu", "Heart"),
    ("BL18 Ganshu", "Liver"), ("BL19 Danshu", "Gallbladder"), ("BL20 Pishu", "Spleen"),
    ("BL21 Weishu", "Stomach"), ("BL22 Sanjiaoshu", "San Jiao"), ("BL23 Shenshu", "Kidney"),
    ("BL25 Dachangshu", "Large Intestine"), ("BL27 Xiaochangshu", "Small Intestine"),
    ("BL28 Pangguangshu", "Bladder"),
]
BACK_SHU_NOTE = (
    "All 12 Back-Shu points sit on the Bladder channel's inner line, 1.5 cun lateral to the spine -- roughly "
    "in organ order top-to-bottom. BL20 (Spleen) and BL21 (Stomach) sit directly adjacent and are a classic "
    "confusable pair."
)

# ---------------------------------------------------------------------------
# WEEKLY MAP -- syllabus reference
# ---------------------------------------------------------------------------
WEEKLY_MAP = [
    ("Week 1", "Channel Theory & Nomenclature", "Foundational rules, 12 meridians overview, 3 circuits, clock"),
    ("Week 2", "LU / LI", "Metal, Outer Circuit begins, Quiz 1-2 material"),
    ("Week 3", "ST / SP", "Earth, Outer Circuit completes, most crossing points (ST=11)"),
    ("Week 4", "HT / SI", "Fire, Inner/Posterior Circuit begins"),
    ("Week 5", "BL / KI", "Water, Inner/Posterior Circuit completes -- largest (BL=67) + Water pair"),
    ("Week 6", "PC / SJ / GB / LR", "Ministerial Fire + Wood, Middle Circuit complete"),
    ("Week 7", "Eight Extraordinary Vessels", "GV, CV, Chong, Dai, Yang/Yin Qiao, Yang/Yin Wei; 8 Confluent Points"),
    ("Week 8", "Collaterals, Divergent Channels, Sinew Channels", "15 Luo points, divergent theory, muscle regions"),
    ("Week 9", "Cutaneous Regions + Five Shu + Final Review", "12 cutaneous regions, 60-point Five Shu master table, "
     "live Final Exam Review, clinical evidence (not exam material)"),
    ("Week 10", "COMPREHENSIVE FINAL EXAM", "30 questions, cumulative, reuses quiz material"),
]
