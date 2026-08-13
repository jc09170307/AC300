# Week 6 Study Materials content -- Pericardium (PC), San Jiao/Triple Energizer (SJ),
# Gallbladder (GB), Liver (LR)
# Pathway narrative verified against Week 6 class transcript (otter.ai, both the
# professor's live description AND the video voiceover read for each channel).
# Point locations/categories are standard Deadman MOA / CAM 4th Ed. values --
# flagged [STANDARD] where not independently re-verified against transcript,
# since the transcript covers pathway + high-yield points in detail but not
# every single point location.

# ---------------------------------------------------------------------------
# META
# ---------------------------------------------------------------------------
PC_META = [
    ("Pertaining", "Pericardium"),
    ("Connecting", "San Jiao"),
    ("Total points", "9 (PC1-PC9) -- fewest of any Yin channel except HT"),
    ("Direction", "Chest -> hand (Yin, hand)"),
    ("Position on arm", "Middle line of anterior/medial arm -- between LU (anterior) and HT (posterior)"),
    ("Circuit", "Middle Circuit (per transcript: 'totally middle circuit')"),
    ("Active hours", "7-9 PM (Xu)"),
    ("Back-Shu", "BL14"),
    ("Front-Mu", "CV17"),
    ("Yuan-Source", "PC7"),
    ("Luo-Connecting", "PC6"),
    ("He-Sea", "PC3"),
    ("Xi-Cleft", "PC4"),
    ("Crossing points", "NONE -- exam trap, matches HT pattern (only 2 primary channels with zero crossing points)"),
]

SJ_META = [
    ("Pertaining", "San Jiao"),
    ("Connecting", "Pericardium"),
    ("Total points", "23 (SJ1-SJ23)"),
    ("Direction", "Hand -> head (Yang, hand)"),
    ("Position on arm", "Middle line, posterior aspect of forearm/upper arm, between SI (posterior) and LI (anterior)"),
    ("Circuit", "Middle Circuit"),
    ("Active hours", "9-11 PM (Hai)"),
    ("Back-Shu", "BL22"),
    ("Front-Mu", "CV5"),
    ("Yuan-Source", "SJ4"),
    ("Luo-Connecting", "SJ5"),
    ("He-Sea", "SJ10"),
    ("Xi-Cleft", "SJ7"),
    ("Confluent (opens EV)", "SJ5 -- opens Yang Wei Mai, paired with GB41"),
    ("Crossing points", "10+ -- shares crossing points w/ GB around the head/ear/shoulder, plus GV14, SI12"),
]

GB_META = [
    ("Pertaining", "Gallbladder"),
    ("Connecting", "Liver"),
    ("Total points", "44 (GB1-GB44) -- 3rd largest channel after BL(67) and ST(45)"),
    ("Direction", "Head -> foot (Yang, foot)"),
    ("Position", "Lateral side of head, trunk, and leg -- zigzag/'Z-shape' course on the head, unique among channels"),
    ("Circuit", "Middle Circuit (per transcript: GB continues 'the totally middle circuit' alongside PC/SJ)"),
    ("Active hours", "11 PM-1 AM (Zi)"),
    ("Back-Shu", "BL19"),
    ("Front-Mu", "GB24"),
    ("Yuan-Source", "GB40"),
    ("Luo-Connecting", "GB37"),
    ("He-Sea", "GB34 (also Hui-Meeting Sinews)"),
    ("Xi-Cleft", "GB36"),
    ("Confluent (opens EV)", "GB41 -- opens Dai Mai (Girdle Vessel), paired with SJ5"),
    ("Crossing points", "12 on slide / only 9 named -- UNRESOLVED, flagged for Dr. Zhang"),
]

LR_META = [
    ("Pertaining", "Liver"),
    ("Connecting", "Gallbladder"),
    ("Total points", "14 (LR1-LR14) -- smallest Yin channel of the foot"),
    ("Direction", "Foot -> chest (Yin, foot)"),
    ("Position", "Medial leg -- crosses IN FRONT of SP from ~8 cun above the medial malleolus upward (exception to the usual order); ends highest of the 3 leg Yin channels, reaching the vertex via the vertex branch"),
    ("Circuit", "Middle Circuit -- LR completes it (per transcript, the four hand/foot channels PC/SJ/GB/LR together form 'a totally middle circuit')"),
    ("Active hours", "1-3 AM (Chou) -- 'liver time'; per transcript, waking 1-3AM = treat Liver, waking 3-5AM = treat Lung"),
    ("Back-Shu", "BL18"),
    ("Front-Mu", "LR14"),
    ("Yuan-Source", "LR3"),
    ("Luo-Connecting", "LR5"),
    ("He-Sea", "LR8"),
    ("Xi-Cleft", "LR6"),
    ("Crossing points", "6 crossing points, shared with CV (2) and SP (1) around the genital/abdomen region, per transcript"),
]

# ---------------------------------------------------------------------------
# PATHWAY -- internal running course (numbered "beats", verified from transcript)
# ---------------------------------------------------------------------------
PC_COURSE = [
    "Originates in the chest, emerges and enters its pertaining organ, the Pericardium",
    "Descends through the diaphragm to the abdomen, connecting successively with the Upper, Middle, and Lower Jiao (San Jiao)",
    "BRANCH: from inside the chest, emerges at the costal region 3 cun below the anterior axillary fold (PC1 Tianchi), ascends to the axilla",
    "Runs down the medial aspect of the upper arm, BETWEEN the Lung channel (anterior) and Heart channel (posterior)",
    "Crosses the cubital fossa (PC3 Quze), continues down the forearm between the tendons of palmaris longus and flexor carpi radialis",
    "Crosses the wrist (PC7 Daling), through the palm (PC8 Laogong), ending at the tip of the middle finger (PC9 Zhongchong)",
    "BRANCH: arises from the palm at PC8 Laogong, runs along the ring finger to its tip, links with the SAN JIAO channel",
]
SJ_COURSE = [
    "Originates at the tip of the ring finger (SJ1 Guanchong)",
    "Runs upward between the 4th and 5th metacarpal bones, along the dorsal wrist, to the lateral forearm between radius and ulna",
    "Passes the olecranon, ascends the lateral upper arm, reaches the shoulder -- crosses BEHIND the Gallbladder channel there",
    "Winds to the supraclavicular fossa, spreads in the chest to connect with the Pericardium",
    "Descends through the diaphragm to the abdomen, enters its pertaining organ: Upper, Middle, and Lower Jiao",
    "BRANCH: from the chest, ascends through the supraclavicular fossa, up the neck, along the posterior border of the ear, to the corner of the anterior hairline, then turns down to the cheek, terminates infraorbitally",
    "BRANCH (auricular): arises retroauricularly, enters the ear, exits in front of the ear, crosses the cheek branch, reaches SJ23 Sizhukong, links with the GALLBLADDER channel at the outer canthus",
]
GB_COURSE = [
    "Originates at the outer canthus (GB1 Tongziliao)",
    "Ascends to the corner of the forehead (GB4 Hanyan), then curves down to the retroauricular region (GB20 Fengchi)",
    "Runs along the side of the neck, in FRONT of San Jiao to the shoulder, then turns back and crosses BEHIND San Jiao, down to the supraclavicular fossa",
    "BRANCH (head): from behind the ear, enters the ear, exits in front, to the posterior aspect of the outer canthus",
    "BRANCH (canthus): from the outer canthus down to ST5/6 region, meets San Jiao infraorbitally, descends to the neck, rejoins the main channel at the supraclavicular fossa",
    "MAIN INTERNAL: from the supraclavicular fossa, descends through the diaphragm, connects with the Liver, enters its pertaining organ the Gallbladder; continues through the hypochondriac region, emerges at the inguinal region (ST30 area), circles the pubic hair margin, transverses to the hip (GB30 Huantiao)",
    "STRAIGHT/EXTERNAL PORTION: from the supraclavicular fossa, descends in front of the axilla, along the lateral chest and free ends of the floating ribs (GB24-GB25), to the hip where it joins the internal branch (GB30)",
    "Continues down the lateral thigh and knee, along the anterior fibula, to GB39 Xuanzhong, in front of the external malleolus, along the dorsum of the foot to the lateral tip of the 4th toe (GB44)",
    "BRANCH: from the dorsum of the foot, to the great toe, links with the LIVER channel",
]
LR_COURSE = [
    "Begins at the lateral side of the great toe (LR1 Dadun), runs along the dorsum of the foot",
    "At 8 cun above the medial malleolus, crosses IN FRONT of the Spleen channel (exception to the usual anterior/middle/posterior leg-Yin order)",
    "Ascends the medial knee and thigh to the pubic region, circles the genitals, enters the lower abdomen",
    "Curves around the Stomach, enters the Liver (its pertaining organ), connects with the Gallbladder",
    "Continues up through the diaphragm, spreads through the costal/hypochondriac region",
    "Ascends along the posterior trachea/throat, connects with the eye system, EMERGES AT THE FOREHEAD, meets the Governing Vessel AT THE VERTEX (GV20 Baihui) -- unique among primary channels for reaching the vertex",
    "BRANCH (cheek): from the eye system, descends to the cheek, circles the inner lips",
    "BRANCH (internal): from the Liver, through the diaphragm, into the Lung, connects with the LUNG channel (completes the 12-channel cycle back to LU)",
]

# ---------------------------------------------------------------------------
# FULL POINT LISTS -- name, pinyin, category tag (categories per Deadman/CAM std.)
# ---------------------------------------------------------------------------
PC_POINTS = [
    ("PC1", "Tianchi", "--", "4th ICS, 1 cun lateral to the nipple."),
    ("PC2", "Tianquan", "--", "2 cun below the anterior axillary fold, between the two heads of biceps brachii."),
    ("PC3", "Quze", "HE-SEA", "Medial end of cubital crease, ulnar side of biceps tendon, elbow slightly flexed."),
    ("PC4", "Ximen", "XI-CLEFT", "5 cun proximal to the wrist crease, between the tendons of palmaris longus and flexor carpi radialis."),
    ("PC5", "Jianshi", "JING-RIVER", "3 cun proximal to the wrist crease, same tendon groove."),
    ("PC6", "Neiguan", "LUO-CONNECTING + CONFLUENT (opens Yin Wei Mai, pairs with SP4)", "2 cun proximal to the wrist crease, same tendon groove. HIGH-YIELD: nausea/vomiting, motion sickness, chest oppression, palpitations, calms the Shen."),
    ("PC7", "Daling", "SHU-STREAM + YUAN-SOURCE", "Midpoint of the wrist crease, between the tendons of palmaris longus and flexor carpi radialis. Ghost point (Ghost Cave)."),
    ("PC8", "Laogong", "YING-SPRING", "Center of the palm, where the tip of the middle finger touches when a fist is made. Emergency point -- mental disorders, palpitations, syncope."),
    ("PC9", "Zhongchong", "JING-WELL", "Center of the tip of the middle finger. Last point of PC; emergency/resuscitation point."),
]
SJ_POINTS = [
    ("SJ1", "Guanchong", "JING-WELL", "Ulnar side of the ring finger, ~0.1 cun from the corner of the nail. First point of SJ."),
    ("SJ2", "Yemen", "YING-SPRING", "Between the 4th and 5th fingers, proximal to the margin of the web."),
    ("SJ3", "Zhongzhu", "SHU-STREAM", "Dorsum of hand, between the 4th and 5th metacarpal bones, in the depression proximal to the MCP joints."),
    ("SJ4", "Yangchi", "YUAN-SOURCE", "Dorsal wrist crease, in the depression lateral to the tendon of extensor digitorum."),
    ("SJ5", "Waiguan", "LUO-CONNECTING + CONFLUENT (opens Yang Wei Mai, pairs with GB41)", "2 cun proximal to the dorsal wrist crease, between radius and ulna. HIGH-YIELD: exterior wind-heat/common cold, treats the exterior via the Yang Wei Mai link."),
    ("SJ6", "Zhigou", "JING-RIVER", "3 cun proximal to the dorsal wrist crease, between radius and ulna."),
    ("SJ7", "Huizong", "XI-CLEFT", "Same level as SJ6, one finger-breadth to the ulnar side."),
    ("SJ8", "Sanyangluo", "--", "4 cun proximal to the dorsal wrist crease."),
    ("SJ9", "Sidu", "--", "5 cun below the olecranon, between radius and ulna."),
    ("SJ10", "Tianjing", "HE-SEA", "1 cun proximal to the olecranon, in the depression above it, elbow flexed."),
    ("SJ11", "Qinglengyuan", "--", "1 cun above SJ10."),
    ("SJ12", "Xiaoluo", "--", "Midpoint between SJ10/olecranon and shoulder."),
    ("SJ13", "Naohui", "--", "Posterior border of deltoid muscle."),
    ("SJ14", "Jianliao", "--", "Posterior/inferior to the acromion."),
    ("SJ15", "Tianliao", "CROSSING (w/ GB21)", "Midpoint between GV14 and the acromion, superior scapular angle."),
    ("SJ16", "Tianyou", "WINDOW OF HEAVEN", "Posterior border of SCM, level with the mandible angle."),
    ("SJ17", "Yifeng", "CROSSING (w/ GB)", "Posterior to the earlobe, in the depression between the mastoid process and the mandible. HIGH-YIELD: tinnitus, deafness, facial paralysis, TMJ."),
    ("SJ18", "Chimai", "--", "Center of the mastoid process."),
    ("SJ19", "Luxi", "--", "Posterior to the ear, behind SJ18."),
    ("SJ20", "Jiaosun", "CROSSING (w/ GB, SI)", "Directly above the ear apex, within the hairline."),
    ("SJ21", "Ermen", "--", "Supratragic notch, anterior to the supratragic notch, mouth slightly open. HIGH-YIELD: tinnitus, deafness, ear pain."),
    ("SJ22", "Erheliao", "CROSSING (w/ GB, SI)", "Anterior/superior to SJ21, at the hairline of the temple, posterior to the superficial temporal artery."),
    ("SJ23", "Sizhukong", "--", "Lateral end of the eyebrow, in the depression. LAST point of SJ, links to GB channel."),
]
GB_POINTS_GROUPED = [
    ("Head/neck (GB1-GB20)", [
        ("GB1", "Tongziliao", "CROSSING (w/ SI, ST)", "0.5 cun lateral to the outer canthus. First point of GB."),
        ("GB2", "Tinghui", "--", "Anterior to the intertragic notch, posterior to the condyloid process of the mandible."),
        ("GB3", "Shangguan", "CROSSING", "Upper border of the zygomatic arch, anterior to the ear."),
        ("GB4-GB13", "(Hanyan...Benshen etc.)", "Several CROSSING", "Zigzag course across the temporal/forehead region -- the 'Z-shape' unique to GB on the head."),
        ("GB14", "Yangbai", "CROSSING", "1 cun above the midpoint of the eyebrow."),
        ("GB20", "Fengchi", "CROSSING (w/ SJ)", "Below the occiput, in the depression between sternocleidomastoid and trapezius. HIGH-YIELD (Wind Gate): headache, dizziness, common cold, hypertension, eye disorders."),
        ("GB21", "Jianjing", "CROSSING (w/ SJ, ST, ren-adjacent)", "Midpoint between GV14 and the acromion, at the highest point of the shoulder. FORBIDDEN IN PREGNANCY -- strong descending action, can induce labor."),
    ]),
    ("Trunk (GB22-GB27)", [
        ("GB24", "Riyue", "FRONT-MU (Gallbladder)", "6th ICS, on the mamillary line."),
        ("GB25", "Jingmen", "FRONT-MU (Kidney)", "Free end (anterior/inferior border) of the 12th rib."),
        ("GB26/27", "Daimai / Wushu", "CROSSING (w/ Dai Mai)", "Below the free end of the 11th rib / anterior superior iliac spine level -- where the Dai Mai (Girdle Vessel) actually wraps the body."),
    ]),
    ("Leg (GB30-GB44)", [
        ("GB30", "Huantiao", "CROSSING (w/ BL)", "Junction of lateral 1/3 and medial 2/3 of the line from the greater trochanter to the sacral hiatus."),
        ("GB34", "Yanglingquan", "HE-SEA + HUI-MEETING (Sinews/Tendons)", "Anterior/inferior to the head of the fibula. HIGH-YIELD: master point for tendons/sinews, hypochondriac pain, jaundice."),
        ("GB37", "Guangming", "LUO-CONNECTING", "5 cun above the tip of the external malleolus, anterior to the fibula."),
        ("GB39", "Xuanzhong", "HUI-MEETING (Marrow)", "3 cun above the tip of the external malleolus, between the fibula and the tendons of peroneus longus/brevis."),
        ("GB40", "Qiuxu", "YUAN-SOURCE", "Anteroinferior to the external malleolus, lateral to the tendon of extensor digitorum longus."),
        ("GB41", "Zulinqi", "SHU-STREAM + CONFLUENT (opens Dai Mai, pairs w/ SJ5)", "Between the 4th/5th metatarsal bones, lateral to the tendon of extensor digitorum longus."),
        ("GB44", "Zuqiaoyin", "JING-WELL", "Lateral side of the 4th toe, ~0.1 cun from the corner of the nail. LAST point of GB, links to LR channel."),
    ]),
]
LR_POINTS = [
    ("LR1", "Dadun", "JING-WELL", "Lateral side of the great toe, ~0.1 cun from the corner of the nail. First point of LR."),
    ("LR2", "Xingjian", "YING-SPRING", "Web margin between the 1st and 2nd toes."),
    ("LR3", "Taichong", "SHU-STREAM + YUAN-SOURCE", "Dorsum of foot, in the depression distal to the junction of the 1st/2nd metatarsal bones. HIGHEST-YIELD LR POINT: smooths Liver Qi, subdues Liver Yang/wind, pairs with LI4 (the 'Four Gates') -- classic combination for pain and to move Qi and Blood."),
    ("LR4", "Zhongfeng", "JING-RIVER", "Anterior to the medial malleolus, medial to tibialis anterior tendon."),
    ("LR5", "Ligou", "LUO-CONNECTING", "5 cun above the tip of the medial malleolus, on the medial tibial surface."),
    ("LR6", "Zhongdu", "XI-CLEFT", "7 cun above the tip of the medial malleolus, medial tibial surface."),
    ("LR8", "Ququan", "HE-SEA", "Medial end of the popliteal crease, posterior to the medial condyle, knee flexed. HIGH-YIELD: nourishes Liver Blood/Yin, genital/gynecological disorders."),
    ("LR13", "Zhangmen", "FRONT-MU (Spleen) + HUI-MEETING (Zang/solid organs)", "Free end of the 11th floating rib, level with LR14. HIGH-YIELD: dual special-point status -- Front-Mu for SP and Hui-Meeting for all 5 Zang."),
    ("LR14", "Qimen", "FRONT-MU (Liver)", "6th ICS, directly below the nipple, on the mamillary line."),
]

# ---------------------------------------------------------------------------
# FUNCTIONS / KEY EXAM FACTS
# ---------------------------------------------------------------------------
PC_FUNCTIONS = [
    "Protects the Heart -- 'Pericardium is an organ that protects the Heart' (transcript); shares many indications with HT (palpitations, chest/mental disorders)",
    "Governs Blood circulation and the vessels alongside HT; regulates the sexual/reproductive function (San Jiao lower jiao connection)",
    "ZERO crossing points -- exam trap identical to HT (both are the two channels with no crossing points)",
    "Runs on the MIDDLE line of the arm, between LU (anterior) and HT (posterior) -- 'in-between' position is exam-testable",
    "PC6 + PC8 are the most clinically-used points per the professor (safe, effective, on the hand/forearm) -- points ON THE CHEST (PC1) are used cautiously due to pneumothorax risk",
]
SJ_FUNCTIONS = [
    "No physical organ -- a 'function organ' governing the Upper/Middle/Lower Jiao (fluid pathways and overall qi transformation)",
    "Governs water passage/metabolism -- transcript: 'it can control the movement of water'",
    "Shares extensive crossing points with GB around the head, ear, and shoulder (both are Shaoyang channels -- 'same finger of Doctor Bobo' / same-name channel rule)",
    "SJ5 opens the Yang Wei Mai (paired with GB41) -- treats exterior wind-heat / alternating chills and fever",
    "Active 9-11 PM -- transcript: this is why we should sleep during this window, as San Jiao 'connects all organs' and needs rest",
]
GB_FUNCTIONS = [
    "3rd largest channel (44 points) after BL (67) and ST (45)",
    "Unique zigzag ('Z-shape') course on the head -- exam-testable visual signature",
    "GB34 is the Hui-Meeting Point for sinews/tendons -- master point for tendon/ligament disorders",
    "GB41 opens the Dai Mai (paired with SJ5) -- the only channel whose confluent point connects to an EV that encircles the waist",
    "Alternating fever and chills + bitter taste in the mouth = classic Shaoyang syndrome, specific to GB (transcript emphasized this repeatedly)",
    "GB21 is FORBIDDEN in pregnancy -- strong descending/labor-inducing action (matches GB's overall 'descending' channel character)",
    "CONTENT FLAG: crossing points slide lists '12 points / 6 meridians' but only 9 points are actually named -- confirm with Dr. Zhang before quiz",
]
LR_FUNCTIONS = [
    "Governs the smooth flow of Qi throughout the body (Liver Qi stagnation is the most common TCM pattern taught from this channel)",
    "Stores Blood; opens into the eyes (Liver Blood nourishes the eyes -- explains why LR reaches the eye system and the vertex)",
    "ONLY primary channel to reach the VERTEX (GV20) -- vertex headache = think Liver, per transcript's clinical Q&A",
    "Crosses IN FRONT of SP at 8 cun above the medial malleolus -- the single exception to the standard leg-Yin ordering rule",
    "LR3 + LI4 = the 'Four Gates' -- classic combination taught this week, smooths Qi and moves Blood, used for pain of many origins",
    "LR13 carries a DOUBLE special-point designation (Front-Mu of SP + Hui-Meeting of all Zang) -- easy to mix up on an exam",
    "Completes the 12-channel Qi cycle by connecting back to LU inside the body -- 'the total basic circulation of the 12 primary meridians'",
]

# ---------------------------------------------------------------------------
# CROSSING POINT DETAIL -- explicit "channel X crosses channel Y at point Z"
# facts, matching the quiz's own question format (e.g. "which crosses in
# front of LR at SP9"). Verified against transcript where noted.
# ---------------------------------------------------------------------------
PC_CROSSING_DETAIL = [
    "PC has NO crossing points -- no other channel crosses PC's pathway, and PC crosses no other channel's points. (Only PC and HT share this trait.)",
]
SJ_CROSSING_DETAIL = [
    "SJ crosses BEHIND the Gallbladder channel at the shoulder (per transcript: SJ 'goes across and passes behind the Gallbladder meridian of Foot-Shaoyang' at the shoulder region)",
    "SJ15 Tianliao is a crossing point shared with GB21 Jianjing (both at the shoulder/scapular region)",
    "SJ meets GB infraorbitally near ST/GB5-6 region on the facial branch",
    "SJ crosses GV14 Dazhui at the top of the shoulder before entering the supraclavicular fossa",
]
GB_CROSSING_DETAIL = [
    "GB runs IN FRONT of San Jiao along the side of the neck to the shoulder, THEN turns back and crosses BEHIND San Jiao down to the supraclavicular fossa -- GB and SJ cross each other TWICE in this region (verified, transcript)",
    "GB1 Tongziliao (first point) is a crossing point shared with SI and ST",
    "GB21 Jianjing is a crossing point shared with SJ, ST, and is near GV14",
    "GB's zigzag head course crosses/shares territory with SJ around the ear repeatedly -- both are Shaoyang channels ('same finger of Doctor Bobo' rule from transcript)",
    "GB30 Huantiao is a crossing point shared with BL",
]
LR_CROSSING_DETAIL = [
    "The SPLEEN channel crosses IN FRONT of LIVER at a point 8 cun above the medial malleolus (this is the exact quiz-style fact: 'which meridian crosses in front of LR at SP9' -> answer: Spleen) -- this is the ONE exception to the normal medial-leg Yin channel order (normally SP is anterior-most)",
    "LR shares crossing points with CV (2 points) and SP (1 point) around the genital/lower abdomen region",
    "LR reaches the VERTEX and meets the Governing Vessel at GV20 Baihui -- a crossing point on top of the head",
]

DIRECTION_POSITION = {
    "PC": ("Chest -> Hand (Yin, Hand)", "Middle line of the anterior/medial arm -- between LU (anterior) and HT (posterior)"),
    "SJ": ("Hand -> Head (Yang, Hand)", "Middle line, posterior forearm/upper arm -- between SI (posterior) and LI (anterior)"),
    "GB": ("Head -> Foot (Yang, Foot)", "Lateral side of head, trunk, and leg -- unique zigzag/'Z-shape' course on the head"),
    "LR": ("Foot -> Chest (Yin, Foot)", "Medial leg -- crosses IN FRONT of SP at 8 cun above the medial malleolus (exception to normal order); reaches highest of any channel via the vertex branch"),
}

# ---------------------------------------------------------------------------
# CROSSING/MEETING POINT DEFINITION -- this term was used throughout the
# guide (PC/SJ/GB/LR crossing-point trivia) without ever being defined.
# Added per Jon's request. "Crossing Point" and "Meeting Point" are the same
# concept (Jiaohui Xue) in these materials -- terminology drifted across
# weeks (earlier weeks used "meeting point," this week uses "crossing
# point"); both names are noted so nothing reads as a new/different concept.
# ---------------------------------------------------------------------------
CROSSING_DEF_FULL = (
    "A Crossing Point (also called a Meeting Point -- same concept, both terms appear across these "
    "materials) is a point where one channel's pathway physically crosses, touches, or runs directly "
    "alongside another channel's pathway. At that shared location, a single point can be understood as "
    "belonging to more than one channel. This is a TOPOGRAPHICAL fact about where pathways cross in "
    "space -- it is NOT one of the 14 special-point categories (Yuan-Source, Luo-Connecting, etc. -- see "
    "the Special Points Decoder for those). A channel can have ZERO crossing points if its entire "
    "pathway never touches another channel's points along the way -- PC and HT are the only two."
)
CROSSING_DEF_SHORT = (
    "Reminder: a Crossing/Meeting Point is a point where two channels' pathways physically cross or "
    "touch -- a topographical fact, not one of the 14 special-point categories. Full definition on the PC page."
)

# ---------------------------------------------------------------------------
# POINT COMBINATIONS -- clinically-paired points, to fill reference space
# and give the point tables clinical context beyond isolated locations.
# ---------------------------------------------------------------------------
PC_COMBINATIONS = [
    ("PC6 + SP4", "The linked-vessel pair -- both are Luo + Confluent points opening related Extraordinary Vessels (Yin Wei Mai + Chong Mai). Classic combination for chest, heart, stomach, and epigastric disorders."),
    ("PC7 + HT7", "Shu-Stream/Yuan-Source points of the two Fire-family Yin hand channels -- combined to calm the Shen; anxiety, insomnia, palpitations."),
    ("PC3 + LU5", "He-Sea points of neighboring Yin hand channels at the elbow -- combined to clear heat and descend rebellious Qi from the chest."),
    ("PC8 Laogong", "One of the classical 13 Ghost Points (Sun Simiao) -- used alone or with other Ghost Points for severe mental-emotional disturbance."),
]
GB_COMBINATIONS = [
    ("GB34 + LR3", "He-Sea/Hui-Meeting of Sinews + Yuan-Source of the paired Liver channel -- combined for tendon/sinew disorders with a Liver-Qi component, e.g. tight/spasming muscles."),
    ("GB20 + GB21", "Two of the most-used GB points together -- head/neck tension and headache with shoulder involvement."),
    ("GB41 + SJ5", "The confluent-point pair that opens the Dai Mai + Yang Wei Mai -- treats conditions along the flank/waist and alternating chills and fever together."),
    ("GB34 + BL18", "Hui-Meeting of Sinews + Liver's Back-Shu -- classic combination for hypochondriac pain and jaundice-type presentations."),
]
LR_COMBINATIONS = [
    ("LR3 + LI4", "The 'Four Gates' (Si Guan) -- pairs the Yuan-Source points of LR and LI. Smooths Liver Qi, moves Qi and Blood broadly; used for pain of many origins."),
    ("LR3 + SP6", "Both regulate Liver Blood and the lower jiao -- common combination for menstrual and gynecological disorders."),
    ("LR14 + LR13", "LR's own Front-Mu plus SP's Front-Mu (which LR13 also serves, as Hui-Meeting of Zang) -- used together for Liver-Spleen disharmony."),
    ("LR8 + KI10", "He-Sea points of neighboring Yin foot channels at the knee -- nourish Liver and Kidney Yin/Blood together ('Liver and Kidney share the same source')."),
]

# ---------------------------------------------------------------------------
# QUICK COMPARE -- condensed cross-reference against the channel's same-
# category neighbors (full version lives in the standalone Comparison Matrix).
# ---------------------------------------------------------------------------
PC_COMPARE = ("Quick compare vs. neighbors: LU (anterior line, Metal, 11 pts) -- PC (middle line, "
              "Ministerial Fire, 9 pts) -- HT (posterior line, Fire, 9 pts). All three run Chest -> Hand. "
              "PC and HT are the only 2 channels with zero crossing points.")
LR_COMPARE = ("Quick compare vs. neighbors: SP (Earth, 21 pts) -- LR (Wood, 14 pts) -- KI (Water, 27 pts). "
              "All three run Foot -> Chest/Abdomen on the medial leg. LR is the only one of the three "
              "that reaches the vertex (GV20).")


CIRCUITS_NOTE = (
    "This week completes the THIRD and final circuit: the Middle Circuit = "
    "PC + SJ + GB + LR, all four of this week's channels (transcript, describing "
    "GB/LR: 'it's a totally middle circuit'). This matches the pattern from "
    "earlier weeks: Anterior Circuit = LU+LI+ST+SP (Weeks 2-3); Posterior Circuit "
    "(also called Inner Circuit on earlier slide versions) = HT+SI+BL+KI (Weeks "
    "4-5, already complete). Exam safety: GB/LR belong to the MIDDLE circuit, "
    "not the Posterior one -- do not confuse with BL/KI's circuit."
)

QUIZ4_RECAP = [
    ("Q1", "Kidney channel connects with all EXCEPT Spleen.", "Kidney connects Kidney, Bladder, Liver, Lung -- NOT Spleen."),
    ("Q2", "Connecting organ of Kidney = Bladder.", "Paired Yin-Yang organ relationship."),
    ("Q3", "BL channel begins at BL1 Jingming (inner canthus).", "First point of the running course."),
    ("Q4", "Kidney channel does NOT connect to all Zang organs.", "Only KI, BL, LR, LU -- not all five."),
    ("Q5", "KI channel begins at the inferior aspect of the little toe.", "Origin point of the internal/oblique course."),
    ("Q6 (bonus)", "BL channel ends at the lateral tip of the little toe (BL67).", "Final point of the running course."),
]

# Element / crossing-point tally for master comparison
WEEK6_TALLY = {
    "PC": dict(points=9, element="Ministerial Fire", crossing=0),
    "SJ": dict(points=23, element="Ministerial Fire", crossing=10),
    "GB": dict(points=44, element="Wood", crossing=12),  # per slide, though only 9 named -- flagged
    "LR": dict(points=14, element="Wood", crossing=6),
}
