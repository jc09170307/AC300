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
