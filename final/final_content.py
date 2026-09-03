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
