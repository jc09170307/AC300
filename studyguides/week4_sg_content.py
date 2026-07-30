# Week 4 Study Guide content - Heart & Small Intestine
# Point locations verified via OCR of AC300_CAM_HTSI.pdf against Deadman CAM
# text (cross-checked HE1, HE2, HE9, SI1, SI4, SI8, SI15, SI16 against raw
# OCR extraction - all matched standard locations exactly).

HT_POINTS = [
    ("HT1", "Jiquan", "In the depression at the centre of the axilla, medial to the axillary artery."),
    ("HT2", "Qingling", "3 cun above HT3, in the groove medial to biceps brachii, one handbreadth proximal to Shaohai HE-3."),
    ("HT3", "Shaohai", "At the medial end of the transverse cubital crease, midway between the medial epicondyle of the humerus and the crease, elbow flexed. HE-SEA."),
    ("HT4", "Lingdao", "1.5 cun proximal to HT7, on the radial side of the flexor carpi ulnaris tendon. JING-RIVER."),
    ("HT5", "Tongli", "1 cun proximal to HT7, radial side of flexor carpi ulnaris tendon. LUO-CONNECTING."),
    ("HT6", "Yinxi", "0.5 cun proximal to HT7, radial side of flexor carpi ulnaris tendon. XI-CLEFT."),
    ("HT7", "Shenmen", "At the ulnar end of the wrist crease, in the depression on the radial side of the flexor carpi ulnaris tendon, level with the pisiform bone. SHU-STREAM + YUAN-SOURCE."),
    ("HT8", "Shaofu", "Between the 4th and 5th metacarpal bones, where the tip of the little finger rests when a fist is made. YING-SPRING."),
    ("HT9", "Shaochong", "On the RADIAL side of the little finger, ~0.1 cun from the corner of the nail. JING-WELL \u2014 last point of HT."),
]

SI_POINTS = [
    ("SI1", "Shaoze", "On the ULNAR side of the little finger, ~0.1 cun from the corner of the nail. JING-WELL \u2014 first point of SI."),
    ("SI2", "Qiangu", "Ulnar side of the hand, distal to the 5th metacarpophalangeal joint, in the depression proximal to the margin of the web. YING-SPRING."),
    ("SI3", "Houxi", "Ulnar side of the hand, proximal to the 5th MCP joint, at the end of the transverse crease, at the junction of red/white skin. SHU-STREAM + CONFLUENT (opens Du Mai)."),
    ("SI4", "Wangu", "Ulnar border of the hand, in the depression between the base of the 5th metacarpal bone and the triquetral bone. YUAN-SOURCE."),
    ("SI5", "Yanggu", "Ulnar end of the wrist crease, in the depression between the styloid process of the ulna and the triquetral bone. JING-RIVER."),
    ("SI6", "Yanglao", "Dorsal to the head of the ulna; with palm facing the chest, in the bony cleft on the radial side of the ulnar styloid process. XI-CLEFT."),
    ("SI7", "Zhizheng", "On the line joining SI5 and SI8, 5 cun proximal to SI5. LUO-CONNECTING."),
    ("SI8", "Xiaohai", "Between the olecranon of the ulna and the medial epicondyle of the humerus, elbow flexed. HE-SEA."),
    ("SI9", "Jianzhen", "Postero-inferior to the shoulder joint, 1 cun above the posterior end of the axillary fold, arm adducted."),
    ("SI10", "Naoshu", "Directly above SI9, in the depression inferior to the scapular spine."),
    ("SI11", "Tianzong", "Center of the infrascapular fossa."),
    ("SI12", "Bingfeng", "Center of the suprascapular fossa, palpable when the arm is lifted."),
    ("SI13", "Quyuan", "Medial extremity of the suprascapular fossa, above the medial end of the scapular spine."),
    ("SI14", "Jianwaishu", "3 cun lateral to the lower border of the T1 spinous process, near the medial border of the scapula."),
    ("SI15", "Jianzhongshu", "2 cun lateral to the lower border of the C7 spinous process (Dazhui GV14)."),
    ("SI16", "Tianchuang", "Posterior border of sternocleidomastoid, level with the laryngeal prominence (Adam's apple) - WINDOW OF HEAVEN point."),
    ("SI17", "Tianrong", "Posterior to the angle of the mandible, anterior to sternocleidomastoid."),
    ("SI18", "Quanliao", "Directly below the outer canthus, in the depression on the lower border of the zygomatic bone."),
    ("SI19", "Tinggong", "Anterior to the tragus, posterior to the condyloid process of the mandible, in the depression formed when the mouth is open - LAST point of SI."),
]

# Internal/external running course, numbered "beats" for the meta page
HT_COURSE = [
    "Originates in the Heart, emerges from the system of blood vessels surrounding the Heart",
    "Descends through the diaphragm to connect with the SMALL INTESTINE (interior-exterior pairing)",
    "A branch ascends alongside the oesophagus, crosses the face and cheek, connects with the tissues surrounding the eye (the 'eye system')",
    "The main external pathway emerges from the axilla at HT1 Jiquan",
    "Descends along the postero-medial aspect of the arm (posterior to LU and PC channels) to the elbow at HT3 Shaohai",
    "Continues along the medial/ulnar aspect of the forearm to the wrist at HT7 Shenmen (pisiform bone)",
    "Travels through the palm along the radial side of the little finger",
    "Ends at HT9 Shaochong, radial tip of the little finger nail - hands off to SMALL INTESTINE",
]
SI_COURSE = [
    "Begins at SI1 Shaoze, ulnar side of the little finger tip - where HT's branch terminates",
    "Runs along the ulnar/dorsal aspect of the hand and forearm, through SI3 Houxi and SI5 Yanggu",
    "Crosses the elbow at SI8 Xiaohai (He-Sea), ascends the posterior aspect of the upper arm",
    "Circles the shoulder joint (SI9-SI10), zigzags across the scapula (SI11-SI13)",
    "Crosses GV14 Dazhui at the top of the shoulder, enters the supraclavicular fossa",
    "Descends internally to the HEART, through the diaphragm, reaches the Stomach, PERTAINS Small Intestine",
    "BRANCH: from the neck, ascends the cheek to the outer canthus, enters the ear at SI19 Tinggong",
    "SECOND BRANCH: from the cheek, ascends to the inner canthus (crosses BL1 Jingming), then to the cheekbone (crosses GB14 Yangbai)",
]

HT_META = [
    ("Pertaining", "Heart"),
    ("Connecting", "Small Intestine"),
    ("Back-Shu", "BL15 Xinshu"),
    ("Front-Mu", "CV14 Juque"),
    ("Yuan-Source", "HT7 Shenmen"),
    ("Luo", "HT5 Tongli"),
    ("He-Sea", "HT3 Shaohai"),
    ("Xi-Cleft", "HT6 Yinxi"),
]
SI_META = [
    ("Pertaining", "Small Intestine"),
    ("Connecting", "Heart"),
    ("Back-Shu", "BL27 Xiaochangshu"),
    ("Front-Mu", "CV4 Guanyuan"),
    ("Yuan-Source", "SI4 Wangu"),
    ("Luo", "SI7 Zhizheng"),
    ("He-Sea", "SI8 Xiaohai"),
    ("Xi-Cleft", "SI6 Yanglao"),
    ("Shu-Stream/Confluent", "SI3 Houxi (opens Du Mai)"),
]

HT_FUNCTIONS = [
    "Governs Blood and the vessels (Heart controls the pulse)",
    "Houses the Shen (spirit/mind) - the Heart 'stores the Shen'",
    "Has ZERO crossing points - the only primary channel with none (exam-critical, unique feature)",
    "Fewest total points of any primary channel (9)",
    "Back-Shu: BL15 Xinshu | Front-Mu: CV14 Juque",
]
SI_FUNCTIONS = [
    "Governs 'separation of the pure from the impure' in digestion (receives food from Stomach, separates nutrients from waste)",
    "More than double HT's point count (19 vs. 9), same pattern as LU(11)/LI(20)",
    "Crosses BL1 and GB14 on its facial branches - unlike HT, which has none",
    "SI3 opens the Du Mai (paired with BL62) - the only confluent point in this week's pair",
    "Back-Shu: BL27 Xiaochangshu | Front-Mu: CV4 Guanyuan",
]

SYNDROMES_HT = dict(
    external=[
        "Pain along the channel: axilla, medial arm, elbow, forearm to little finger",
        "Heat in the palms (palms of hands feel hot)",
        "Dry throat, thirst",
    ],
    internal=[
        "Palpitations, chest pain (Heart itself)",
        "Insomnia, excessive dreaming, poor memory",
        "Mental-emotional disturbance: anxiety, mania, incoherent speech, loss of consciousness (Shen disturbance)",
        "Yellowing of the eyes (classical symptom)",
    ],
    note="Dr. Zhang: HT is the smallest channel but treats the most emotionally significant disorders - anxiety, insomnia, and Shen disturbance are the clinical center of gravity for this channel.",
)
SYNDROMES_SI = dict(
    external=[
        "Swelling of the cheek and neck, jaw pain, deafness, tinnitus",
        "Pain along the postero-lateral shoulder, arm, and elbow",
        "Stiff neck, sore throat",
    ],
    internal=[
        "Abdominal pain and distension, borborygmus",
        "Diarrhea or constipation depending on presentation",
        "Excess breast milk / lactation problems (Dr. Zhang specifically noted SI1 for this)",
        "Mental disorders - SI's internal course also links to Shen disturbance via the Heart",
    ],
    note="Dr. Zhang: SI treats disorders along its course (mouth, cheek, throat, neck, upper arm) as well as internal-organ digestive symptoms, since it is paired with the Heart internally.",
)

HT_HIGHEST_YIELD = [
    ("HT7", "Shu-Stream + Yuan-Source", "Calms Shen; #1 point for anxiety, insomnia, palpitations"),
    ("HT3", "He-Sea", "Clears heart fire; fear, arm pain along the channel"),
    ("HT6", "Xi-Cleft", "Night sweats, acute heart pain"),
    ("HT9", "Jing-Well", "Emergency point: severe heart pain, palpitations, revives consciousness"),
    ("HT5", "Luo-Connecting", "Links to SI; treats disorders of both channels"),
    ("HT1", "First point", "Landmark for axilla; rarely needled directly in modern practice"),
]
SI_HIGHEST_YIELD = [
    ("SI3", "Shu-Stream + Confluent", "Opens Du Mai (pairs with BL62); spine, neck, febrile disease"),
    ("SI4", "Yuan-Source", "Wrist/finger pain, febrile disease"),
    ("SI8", "He-Sea", "Elbow/arm disorders, mental-emotional Fire patterns"),
    ("SI19", "Last point", "Tinnitus, deafness, ear disorders"),
    ("SI1", "Jing-Well", "Excess breast milk / lactation problems - specifically noted by Dr. Zhang"),
    ("SI16", "Window of Heaven", "Throat/voice disorders; needle with care (carotid region)"),
]

HT_FIVE_SHU = [("Jing-Well", "Wood", "HT9 Shaochong", "revives consciousness, mental-emotional Fire"),
               ("Ying-Spring", "Fire", "HT8 Shaofu", "clears heart fire"),
               ("Shu-Stream", "Earth", "HT7 Shenmen (=Yuan-Source)", "calms Shen, anxiety/insomnia"),
               ("Jing-River", "Metal", "HT4 Lingdao", "voice disorders, arm pain"),
               ("He-Sea", "Water", "HT3 Shaohai", "clears heart fire, fear/arm pain")]
SI_FIVE_SHU = [("Jing-Well", "Metal", "SI1 Shaoze", "breast/lactation, breast abscess"),
               ("Ying-Spring", "Water", "SI2 Qiangu", "clears heat, ear/eye disorders"),
               ("Shu-Stream", "Wood", "SI3 Houxi (also Confluent)", "opens Du Mai, spine/neck, febrile disease"),
               ("Jing-River", "Fire", "SI5 Yanggu", "wrist pain, febrile disease, malaria"),
               ("He-Sea", "Earth", "SI8 Xiaohai", "elbow/arm, mental-emotional Fire")]

CLINICAL_PEARLS_WK4 = [
    ("HT is the Smallest Channel, Not the Least Important",
     "HT has only 9 points - the fewest of any primary channel - but governs the Shen (mind/spirit), making it clinically central for anxiety, insomnia, and emotional disorders despite its small point count."),
    ("HT has ZERO Crossing Points - Genuinely Unique",
     "Confirmed from lecture: HT is the only one of the 12 primary channels with no crossing (jiaohui) points on its external pathway. This is one of the highest-yield 'unique feature' facts in the Weeks 1-4 scope."),
    ("HT7 Shenmen - The Spirit Gate",
     "HT7's name literally means 'Spirit Gate'. As both Shu-Stream and Yuan-Source, it is the single most important point on the Heart channel for calming an agitated Shen - anxiety, insomnia, palpitations, and excessive dreaming."),
    ("SI Point Count Mirrors the LU/LI Pattern",
     "SI (19 pts) has more than double HT's points (9 pts) - just as LI (20) has nearly double LU (11). In both pairs, the Yang/Fu channel carries far more points than its Yin/Zang partner."),
    ("SI's Lower He-Sea Sits on a Different Channel",
     "SI's Lower He-Sea is ST39 Xiajuxu, located on the STOMACH channel - not on SI itself. This is true for all six Fu organs: their Lower He-Sea points sit on the leg-Yang channels (ST, BL, GB), regardless of where the organ's own channel runs."),
    ("SI3 Houxi - Opens the Du Mai",
     "SI3 is SI's Shu-Stream point and also a Confluent point, opening the Du Mai (paired with BL62 Shenmai). This makes it a key point for spinal and neck disorders, and for febrile disease."),
    ("Primary Fire vs. Ministerial Fire - Don't Conflate",
     "HT and SI are the PRIMARY Fire pair, opening the Posterior Circuit (also called Inner Circuit). PC and SJ are a separate MINISTERIAL Fire pair with their own circuit, taught in Week 6. Do not lump all four channels together as one 'Fire' group."),
    ("SI1 and Lactation - A Specific Clinical Note from Lecture",
     "Dr. Zhang highlighted SI1 (Shaoze) specifically for breast milk / lactation problems, noting it as a distinctive clinical use worth remembering for practice."),
    ("The Posterior Circuit Begins This Week",
     "HT (chest to hand) -> SI (hand to head) completes this week's hand-off and opens the Posterior Circuit (also called Inner Circuit on the revised Lecture 4 slide), which continues next week with BL and KI."),
]

QUIZ4_FUNDAMENTALS = dict(
    distribution=[
        "ON THE LIMBS: Medial = YIN, Lateral = YANG",
        "Anterior: Taiyin (yin) / Yangming (yang)",
        "Middle: Jueyin (yin) / Shaoyang (yang)",
        "Posterior: Shaoyin (yin) / Taiyang (yang)  <- HT and SI live here",
        "HT = Hand Shaoyin (posterior medial). SI = Hand Taiyang (posterior lateral).",
    ],
    circulation=[
        "a) Yin meridians of HAND: chest -> hand",
        "b) Yang meridians of HAND: hand -> head",
        "c) Yang meridians of FOOT: head -> foot",
        "d) Yin meridians of FOOT: foot -> chest",
        "This week completes the POSTERIOR pairing: HT -> SI (continues to BL -> KI next week)",
    ],
    circuit_connections=[
        "SP (Spleen) -> connects to HT at the internal branch -> HEART",
        "HT (Heart) -> connects to SI at HT9/SI1 -> little finger tip",
        "SI (Small Intestine) -> connects to BL (Bladder), NOT to any Fire-pair channel -> via facial branch to BL1",
        "Dr. Zhang stressed: SI connects to BLADDER next (not PC/SJ) - a classic circuit-continuity trap.",
    ],
    nomenclature=[
        "Meridian name = 3 parts: Hand/Foot + Yin/Yang + Zang/Fu",
        "e.g. 'Heart Meridian of Hand-Shaoyin'",
    ],
    clock=[
        "HT (Heart): 11 AM-1 PM",
        "SI (Small Intestine): 1-3 PM",
        "Preceded by: SP 9-11 AM | Followed by: BL 3-5 PM",
        "Full order: LU LI ST SP HT SI BL KI PC SJ GB LR",
    ],
    homework_rule="Dr. Zhang's homework rule: DRAW BOTH internal AND external pathways for every meridian.",
)

COMPARISON_HT_SI = [
    ("Yin / Yang", "Yin (posteromedial)", "Yang (posterolateral)"),
    ("Element", "Fire", "Fire"),
    ("Circuit", "Posterior - Chest to Hand", "Posterior - Hand to Head"),
    ("Clock", "11 AM-1 PM", "1-3 PM"),
    ("Points", "9 (HT1-HT9)", "19 (SI1-SI19)"),
    ("Start", "HT1 Jiquan (axilla)", "SI1 Shaoze (little finger)"),
    ("End", "HT9 Shaochong (little finger)", "SI19 Tinggong (in front of ear)"),
    ("Pertaining", "Heart", "Small Intestine"),
    ("Connecting", "Small Intestine", "Heart"),
    ("Back-Shu", "BL15", "BL27"),
    ("Front-Mu", "CV14", "CV4"),
    ("Yuan-Source", "HT7 Shenmen", "SI4 Wangu"),
    ("Luo", "HT5 Tongli", "SI7 Zhizheng"),
    ("Xi-Cleft", "HT6 Yinxi", "SI6 Yanglao"),
    ("He-Sea", "HT3 Shaohai", "SI8 Xiaohai"),
    ("Confluent Pt", "-", "SI3 (opens Du Mai)"),
    ("Lower He-Sea", "-", "ST39 (on the ST channel)"),
    ("Crossing Pts", "0 (unique - none)", "2 (BL1, GB14)"),
    ("Unique Feature", "ONLY channel w/ ZERO crossings", "Lower He-Sea sits on a different channel"),
    ("Ext Symptoms", "Palpitations, chest pain, arm pain", "Cheek/neck swelling, shoulder pain"),
    ("Int Symptoms", "Insomnia, anxiety, Shen disturbance", "Digestive pain, lactation issues"),
    ("Organ Function", "Governs Blood/vessels, houses Shen", "Separates pure from impure"),
]
