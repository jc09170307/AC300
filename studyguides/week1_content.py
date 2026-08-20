# Week 1 content - Channel Theory (Concept, History, Morphology, Nomenclature, Flow of Qi)
# All facts verified directly against the Week 1 lecture transcript (AC300Week1.txt).

TWELVE_MERIDIANS = [
    ("LU", "Lung", "Hand Taiyin", "Yin", "Chest -> Hand", "Outer (Anterior)"),
    ("LI", "Large Intestine", "Hand Yangming", "Yang", "Hand -> Head", "Outer (Anterior)"),
    ("ST", "Stomach", "Foot Yangming", "Yang", "Head -> Foot", "Outer (Anterior)"),
    ("SP", "Spleen", "Foot Taiyin", "Yin", "Foot -> Chest", "Outer (Anterior)"),
    ("HT", "Heart", "Hand Shaoyin", "Yin", "Chest -> Hand", "Inner (Posterior)"),
    ("SI", "Small Intestine", "Hand Taiyang", "Yang", "Hand -> Head", "Inner (Posterior)"),
    ("BL", "Bladder", "Foot Taiyang", "Yang", "Head -> Foot", "Inner (Posterior)"),
    ("KI", "Kidney", "Foot Shaoyin", "Yin", "Foot -> Chest", "Inner (Posterior)"),
    ("PC", "Pericardium", "Hand Jueyin", "Yin", "Chest -> Hand", "Middle"),
    ("SJ", "San Jiao (Triple Burner)", "Hand Shaoyang", "Yang", "Hand -> Head", "Middle"),
    ("GB", "Gallbladder", "Foot Shaoyang", "Yang", "Head -> Foot", "Middle"),
    ("LR", "Liver", "Foot Jueyin", "Yin", "Foot -> Chest", "Middle"),
]

ZANG_ORGANS = ["Lung (LU)", "Spleen (SP)", "Heart (HT)", "Liver (LR)", "Kidney (KI)", "Pericardium (PC)"]
FU_ORGANS = ["Large Intestine (LI)", "Stomach (ST)", "Small Intestine (SI)", "Bladder (BL)", "Gallbladder (GB)", "San Jiao (SJ)"]

CIRCUITS = [
    ("Outer Circuit", "Anterior", ["LU (chest->hand)", "LI (hand->head)", "ST (head->foot)", "SP (foot->chest)"],
     "Taiyin / Yangming"),
    ("Inner Circuit", "Posterior", ["HT (chest->hand)", "SI (hand->head)", "BL (head->foot)", "KI (foot->chest)"],
     "Shaoyin / Taiyang"),
    ("Middle Circuit", "Middle/Lateral", ["PC (chest->hand)", "SJ (hand->head)", "GB (head->foot)", "LR (foot->chest)"],
     "Jueyin / Shaoyang"),
]

DIRECTION_RULES = [
    ("Yin meridians of the HAND", "Chest -> Hand"),
    ("Yang meridians of the HAND", "Hand -> Head"),
    ("Yang meridians of the FOOT", "Head -> Foot"),
    ("Yin meridians of the FOOT", "Foot -> Chest/Abdomen"),
]

LIMB_POSITION_TABLE = [
    # (Position, Yin name, Yang name)
    ("Anterior", "Taiyin", "Yangming"),
    ("Middle / Lateral", "Jueyin", "Shaoyang"),
    ("Posterior", "Shaoyin", "Taiyang"),
]
TRUNK_POSITION_NOTE = (
    "On the HEAD and TRUNK, only the Yang channels get a 3-way anterior/posterior/lateral split "
    "(Yangming/Taiyang/Shaoyang) - Yin channels don't reach the head. On the trunk (chest/abdomen), "
    "all three Yin channels (Taiyin, Shaoyin, Jueyin) run together along the anterior aspect only - "
    "there's no separate Yin posterior or lateral position on the trunk the way there is on the limbs."
)
LIMB_POSITION_SOURCE = "Cross-verified against Dr. Zhang's Week 1 lecture (AC300Week1.txt) and Slide 27 of her lecture deck."

MEETING_POINTS = [
    ("Hand Yin meets Hand Yang", "at the FINGERS", "e.g. LU7's branch meets LI1 at the index finger"),
    ("Hand Yang meets Foot Yang", "at the FACE", "e.g. LI ends at LI20, ST begins there"),
    ("Foot Yang meets Foot Yin", "at the TOES", "e.g. ST ends at ST45, SP begins at SP1"),
    ("Foot Yin meets Hand Yin", "at the CHEST", "completes the full 12-channel loop back to the next circuit"),
]

MERIDIAN_CLOCK = [
    ("LU", "3-5 AM"), ("LI", "5-7 AM"), ("ST", "7-9 AM"), ("SP", "9-11 AM"),
    ("HT", "11 AM-1 PM"), ("SI", "1-3 PM"), ("BL", "3-5 PM"), ("KI", "5-7 PM"),
    ("PC", "7-9 PM"), ("SJ", "9-11 PM"), ("GB", "11 PM-1 AM"), ("LR", "1-3 AM"),
]

# Five-Element color mapping for each channel, matching the established project palette
CLOCK_ELEMENT = {
    "LU": "Metal", "LI": "Metal",
    "ST": "Earth", "SP": "Earth",
    "HT": "Fire", "SI": "Fire",
    "BL": "Water", "KI": "Water",
    "PC": "Ministerial Fire", "SJ": "Ministerial Fire",
    "GB": "Wood", "LR": "Wood",
}

FUNCTIONS_OF_MERIDIANS = [
    ("Transporting", "Transport Qi and Blood to nourish the organs, skin, muscles, tendons, and bones; keep Yin-Yang in harmony throughout the body."),
    ("Resisting (Defending)", "Defend the body against disease - meridians help resist pathogens and reflect symptoms/signs when something is wrong."),
    ("Treatment", "Transmit needling sensation and regulate deficiency and excess conditions - the basis for using meridians and points clinically."),
]

NOMENCLATURE = dict(
    parts=["Hand or Foot (location of the pathway)", "Yin or Yang (nature / medial-lateral surface)", "Zang or Fu (pertaining organ)"],
    example="e.g. \u2018Lung Meridian of Hand-Taiyin\u2019, \u2018Stomach Meridian of Foot-Yangming\u2019",
    location_note="Anterior = Taiyin(yin)/Yangming(yang); Posterior = Shaoyin(yin)/Taiyang(yang); Middle = Jueyin(yin)/Shaoyang(yang) - "
                   "this naming is based on LOCATION (medial/lateral position on the limb), not organ function.",
)

CHANNELS_VS_MERIDIANS = dict(
    definition="\u2018Channels\u2019 (Jing-Luo) is the umbrella term covering BOTH Meridians (Jing, the primary pathways - like a river) "
                "AND Collaterals (Luo, the branches - smaller networks connecting meridians to tissues and organs).",
    counts=[
        "12 Primary Meridians (Jing) - the main rivers",
        "15 Collaterals (Luo) - 12 from each primary meridian's own Luo-connecting point, plus the Luo of Du Mai, "
        "Ren Mai, and the Spleen's Great Luo (Dabao)",
        "12 Divergent Meridians - branch from the primary meridians, distribute on chest/abdomen/head, deepen "
        "the Zang-Fu relationship (detail taught later in the course)",
        "12 Muscle (Sinew) Regions - distribution of the primary meridians into the muscular system",
        "12 Cutaneous Regions - the most superficial layer, where channel Qi reflects on the skin",
        "8 Extraordinary Vessels - Du, Ren, Chong, Dai, Yinwei, Yangwei, Yinqiao, Yangqiao; act as reservoirs of "
        "Qi and Blood, closely connected to the Kidney, regulating the primary meridians as needed (detail taught later)",
    ],
)

CLINICAL_PEARLS_WK1 = [
    ("The Meridian Clock Has Real Clinical Use",
     "Dr. Zhang's own example: if you want to treat a Large Intestine dysfunction, consider timing treatment "
     "around 5-7 AM, LI's active period. Symptoms that flare at a specific time of day can point directly to "
     "which channel is involved."),
    ("Channels Is a Bigger Category Than Meridians",
     "A student asked this directly in lecture: 'meridians' specifically means the 12 Primary Meridians, while "
     "'channels' is the whole system - meridians AND collaterals together. When a question says 'channels,' "
     "don't assume it only means the 12 primary pathways."),
    ("Draw It, Don't Just Read It",
     "Dr. Zhang's own studying advice, repeated multiple times in lecture: draw each circuit's four meridians "
     "by hand, more than once, rather than only reading the sequence. This is also the format of the homework "
     "assignments for this course."),
    ("Same-Named Channels on Opposite Limbs Communicate",
     "Per lecture: arm and leg channels of the same name (e.g., Hand Taiyin LU and Foot Taiyin SP) communicate "
     "with one another. A problem in one can sometimes be addressed by treating points on its same-name partner."),
    ("The Extraordinary Vessels Are Reservoirs, Not Organs",
     "The 8 Extraordinary Vessels aren't directly linked to a specific Zang-Fu organ the way the 12 Primary "
     "Meridians are. They act as reservoirs of Qi and Blood, closely tied to the Kidney, releasing or absorbing "
     "as the primary meridians need."),
]

# =========================================================================
# HISTORY OF CHANNELS & POINTS (Slides 12-18; verified against transcript
# lines ~347-359). New section added per Jon's request to make Week 1
# genuinely comprehensive - this content was in the lecture and on the
# slides but had not yet been built into any document.
# =========================================================================
HISTORY_KEY_QUESTION = dict(
    question="Which were discovered first: the channels, or the points?",
    answer="The CHANNELS were discovered first, then the points. This is confirmed by the Mawangdui "
           "Silk Manuscripts (excavated from a Western Han Dynasty tomb): the silk texts describe channel "
           "pathways but do not yet reference specific points - meaning the pathway concept predates the "
           "point concept in the historical record.",
    source="Dr. Zhang, Week 1 lecture (verbatim transcript) + Slide 13",
)

HISTORY_TIMELINE = [
    ("Origins", "c. 2000+ years ago", "Theoretical foundation laid in China; earliest surviving textual "
     "evidence is the Mawangdui Silk Manuscripts (Western Han Dynasty tomb), which describe the Yin and "
     "Yang meridians but predate point-specific texts."),
    ("Formalization", "Zhou & Han Dynasties", "The Huangdi Neijing (Yellow Emperor's Inner Canon) - "
     "read as two volumes, Su Wen (Basic Questions) and Ling Shu (Miraculous Pivot) - details the "
     "location, properties, and uses of acupuncture points, laying the foundation of modern practice. "
     "This text marks the formal establishment of the Meridian System as composed of the 12 Primary "
     "Meridians."),
    ("Spread to East Asia", "6th century CE", "Channel theory and acupuncture practice spread to East "
     "Asian countries neighboring China."),
    ("Spread to the West", "17th century onward", "Acupuncture reached Europe and, later, North America."),
    ("Modern Recognition", "Present day", "Recognized by the WHO as an evidence-based complementary "
     "therapy and integrated into healthcare systems worldwide; modern research reinterprets meridians "
     "as networks integrating neural, circulatory, connective-tissue, and bioelectrical processes rather "
     "than fixed anatomical structures like nerves or blood vessels."),
]

HISTORY_FORMATION_THEORY = [
    ("\u58f9  Observation", "Observation of stimulation induction and conduction (needle sensation, Qi)."),
    ("\u8d30  Documentation", "Summary of acupoint effects (Points -> The Line)."),
    ("\u53c1  Classical text support", "Ling Shu: \u201cAs for a man eight feet tall, his skin and flesh are "
     "right here: outwardly they can be measured, palpated, and examined; after death, they can be "
     "dissected and observed.\u201d"),
    ("\u8086  Internal Qi flow", "The phenomenon of internal Qi flow (the small cycle) discovered by "
     "ancient people in qigong and guided breathing practice."),
]

HISTORY_MODERN_REINTERPRETATION = (
    "A key point from lecture: acupuncture's mechanism is increasingly understood through neuroscience, "
    "not superseded by it. The reason acupuncture works isn't because of the ancient explanations "
    "themselves, but because the loci ancient clinicians selected are direct access points to the "
    "nervous system. In this framing, meridians can be understood as a combination of peripheral nerve "
    "pathways, arterial pathways, and myofascial referred-pain patterns - a map of favorable access "
    "points to the nervous system discovered empirically, centuries before that neuroscience existed to "
    "explain why they worked."
)

CLASSIFICATION_TREE_NOTE = (
    "Slide 21's classification table organizes the full channel system as one tree: the 12 Primary "
    "Meridians (Hand: 3 Yin + 3 Yang; Foot: 3 Yin + 3 Yang) sit at the center, branching into the 15 "
    "Collaterals (12 primary Luo-points + Du/Ren/Spleen's Great Luo), the 12 Divergent Meridians, and "
    "outward into the 12 Muscle (Sinew) Regions and 12 Cutaneous Regions - with the 8 Extraordinary "
    "Vessels running alongside as a separate reservoir system, sharing 2 members (Du Mai, Ren Mai) with "
    "the 14-meridian count some texts use."
)

MERIDIAN_VS_COLLATERAL_TABLE = [
    # (Aspect, Meridians/Jingmai, Collaterals/Luomai)
    ("Meaning", "Pathway", "Network"),
    ("Standing", "Trunk", "Branch"),
    ("Distribution", "Vertical line", "Running amok (irregular, web-like)"),
    ("Depth", "Deep", "Shallow"),
    ("Number", "Few (12 Primary)", "Many (15 named + further branching)"),
    ("Function", "Leading - the pathways through which Qi and Blood circulate",
     "Supplement and bond - promotes Qi and Blood circulation between meridians"),
]
MERIDIAN_VS_COLLATERAL_SOURCE_QUOTE = (
    "Classical source cited on Slide 22: \u300a\u96f5\u62ec\u300b - \u7ecf\u8109\u4e3a\u91cc\uff0c\u652f\u800c"
    "\u6a2a\u8005\u4e3a\u7edc\u4e5f\uff0c\u7edc\u4e4b\u522b\u8005\u4e3a\u5b59\u3002 "
    "(\u201cThe meridians run through the interior; the branches running crosswise from them are the "
    "collaterals; and the branches of the collaterals are the grandchild-vessels.\u201d)"
)

FUNCTIONS_LING_SHU_CITATIONS = [
    ("A. Transporting Qi and blood and regulating Yin and Yang.",
     "Ling Shu, Ch. 47", "\u201cThe meridians and collaterals transport blood and Qi to adjust Yin and "
     "Yang, nourish tendons and bones, and improve joint function.\u201d"),
    ("B. Resisting pathogens and reflecting symptoms and signs.",
     "Ling Shu, Ch. 71", "\u201cWhen the lung and heart are involved in a pathogenic invasion, the "
     "pathogenic Qi lingers in both elbows; when the liver is involved, it lingers in both axillae; when "
     "the spleen is involved, it stays in both groins; when the kidney is involved, it stays in both "
     "popliteal fossae.\u201d"),
    ("C. Transmitting needling sensation and regulating deficiency and excess conditions.",
     "Ling Shu, Ch. 5 / Ch. 9", "\u201cThe key point in acupuncture treatment is to know how to regulate "
     "Yin and Yang.\u201d (Ch. 5)  /  \u201cAcupuncture treatment must aim at regulating the flow of "
     "Qi.\u201d (Ch. 9)"),
]

# =========================================================================
# WRITTEN SYLLABUS TABLE (Slide 8) - authoritative per project rules, and
# overrides any verbal walkthrough. Captured in full for reference.
# =========================================================================
SYLLABUS_TABLE = [
    # (Week, Lecture Contents, Quiz/Exam, Assignments)
    ("1", "Introduction to Channels: History, Nomenclature, Distribution, Circulation & Function",
     "-", "CAM p.1-68 \u00b7 MOA p.11-16"),
    ("2", "Primary Meridians: LU & LI channels", "QUIZ 1 + Homework 1 (material from wk 1-2)",
     "CAM p.66-68 \u00b7 MOA p.73-75, 95-99"),
    ("3", "Primary Meridians: ST & SP channels", "QUIZ 2 + Homework 2 (material from wk 2-3)",
     "CAM p.68-71 \u00b7 MOA p.125-129, 177-181"),
    ("4", "Primary Meridians: HT & SI channels", "QUIZ 3 + Homework 3 (material from wk 3-4)",
     "CAM p.69-74 \u00b7 MOA p.209-212, 227-230"),
    ("5", "MIDTERM EXAM \u00b7 BL & KI channels", "MID TERM (material from wk 1-4)",
     "CAM p.73-77 \u00b7 MOA p.251-256, 331-335"),
    ("6", "PC, SJ (TE), GB, & LR channels", "QUIZ 4 + Homework 4",
     "CAM p.77-82 \u00b7 MOA p.367-370, 387-390, 417-421, 469-472"),
    ("7", "Eight Extraordinary Meridians", "QUIZ 5 + Homework 5 (material from wk 6-7)",
     "CAM p.82-89 \u00b7 MOA p.17-25, 495-497, 529-533"),
    ("8", "Additional Channels/Regions: 12 Muscle/Sinew channels, 15 collaterals, 12 cutaneous "
     "regions, 12 Divergent Channels", "QUIZ 6 (material from wk 7)",
     "CAM p.88-114 \u00b7 MOA p.16-17, 26-28 + intro to all 12 Primary Meridians"),
    ("9", "Acupuncture Points: General Functions and Categories", "-", "CAM p.115-134 \u00b7 MOA p.29-55"),
    ("10", "COMPREHENSIVE FINAL EXAMINATION", "Final Exam (material from wk 1-9)", "Prepare for Final Exam"),
]

GRADING_CRITERIA = [
    ("Homework (5 total)", "4% each", "20%", "CLO 2-5"),
    ("Quizzes (6 total)", "5% each", "30%", "CLO 1-5"),
    ("Midterm", "-", "20%", "CLO 1-5"),
    ("Final Exam", "-", "30%", "CLO 1-5"),
]
GRADING_SOURCE_NOTE = (
    "Verified directly from the written syllabus table (Slide 8), which is the authoritative source "
    "and overrides Dr. Zhang's verbal walkthrough of grading during Week 1 lecture. Attendance is a "
    "separate pass/fail-style requirement (per the syllabus text portion): a minimum attendance rate is "
    "required or a grade of F is assigned; each unexcused absence beyond the allowed count requires a "
    "500-word written explanation to avoid losing attendance credit."
)
QUIZ1_SCOPE_NOTE = (
    "IMPORTANT: per the syllabus table, Quiz 1 (Week 2) covers material from BOTH Week 1 (Channel "
    "Theory) AND Week 2 (LU & LI channels) - not Week 1 content alone. Per Slide 41, Quiz 1 itself is "
    "5 questions worth 100 points total, plus 1 bonus question worth 20 points (6 questions, 120 points "
    "possible). This Week 1 material is necessary but not sufficient prep for Quiz 1 - pair it with the "
    "Week 2 LU/LI materials before that quiz."
)

QUIZ1_FUNDAMENTALS = dict(
    key_terms=[
        "Channel (Jing-Luo) = Meridians + Collaterals (the whole system)",
        "Meridian (Jing) = one of the 12 Primary pathways - 'like a river'",
        "Collateral (Luo) = a branch off a meridian's Luo-connecting point - 'like a branch'",
        "12 Meridians + 15 Collaterals + 12 Divergent + 12 Sinew + 12 Cutaneous + 8 Extraordinary Vessels = the full channel system",
    ],
    nomenclature=[
        "3-part name: Hand/Foot + Yin/Yang + Zang/Fu",
        "6 Zang (Yin) organs: Lung, Spleen, Heart, Liver, Kidney, Pericardium",
        "6 Fu (Yang) organs: Large Intestine, Stomach, Small Intestine, Bladder, Gallbladder, San Jiao",
    ],
    circulation=[
        "Yin meridians of the hand: chest -> hand",
        "Yang meridians of the hand: hand -> head",
        "Yang meridians of the foot: head -> foot",
        "Yin meridians of the foot: foot -> chest/abdomen",
        "Repeat this sequence until automatic - it's the single most tested fact in the course",
    ],
    circuits=[
        "Outer/Anterior: LU -> LI -> ST -> SP (Taiyin/Yangming)",
        "Inner/Posterior: HT -> SI -> BL -> KI (Shaoyin/Taiyang)",
        "Middle: PC -> SJ -> GB -> LR (Jueyin/Shaoyang)",
    ],
    functions=[
        "Transporting: nourish organs, skin, muscles, tendons, bones; keep Yin-Yang harmony",
        "Resisting: defend against disease, reflect symptoms when pathogens invade",
        "Treatment: transmit needling sensation, regulate deficiency/excess",
    ],
    homework_note="Dr. Zhang's Week 1 homework: draw the circulation, direction, and distribution of the Lung "
                   "Meridian of Hand-Taiyin specifically - the same drawing standard applies to every meridian "
                   "going forward.",
)
