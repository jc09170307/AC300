"""Week 7 -- The Eight Extraordinary Vessels (Qi Jing Ba Mai). Data sourced and
verified against Lecture_7vivian11_12.pdf (76 slides, Dr. Zhang, primary source)
and cross-checked against AC300_WEEK_7.txt transcript. CAM p.82-89, MOA p.17-25,
495-497, 529-533 per written syllabus.

FLAGGED DISCREPANCIES (not silently resolved -- see decoder/cram notes):
  - Yang Qiao Mai: slide header says "(12)" coalescent points but only 10 are
    named (BL1, BL59, BL61, BL62, GB20, GB29, SI10, ST1, ST3, ST4).
  - Yang Wei Mai: slide header says "(15)" coalescent points but only 14 are
    named (BL63, SI10, GV15, GV16, GB21, GB35, GB13-20).
  Both flagged for Dr. Zhang confirmation, same pattern as the Week 6 GB
  crossing-point discrepancy.
"""

NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.10, 0.10, 0.10)
GRAY = (0.40, 0.40, 0.40)

ACCENT_GV = (0.114, 0.227, 0.369)      # navy -- sea of yang meridians
ACCENT_CV = (0.753, 0.224, 0.169)      # red -- sea of yin meridians
ACCENT_CHONG = (0.55, 0.38, 0.16)      # amber/brown -- sea of 12 meridians/blood
ACCENT_DAI = (0.16, 0.44, 0.46)        # slate teal -- the horizontal vessel
ACCENT_QIAO = (0.20, 0.48, 0.27)       # green -- Heel vessels
ACCENT_WEI = (0.45, 0.30, 0.55)        # muted purple -- Link vessels

READING_ASSIGNMENT = "CAM p.82-89  |  MOA p.17-25, 495-497, 529-533 (per written syllabus, Week 7)"

# One-source-three-branches vessels (Du, Ren, Chong) all arise in the lower
# abdomen and share the perineum (Huiyin) as a common meeting area.
ONE_SOURCE_THREE_BRANCHES = (
    "Du Mai, Ren Mai, and Chong Mai all arise from inside the lower abdomen and "
    "emerge together at the perineum before diverging into three separate "
    "pathways -- Du posteriorly along the spine, Ren anteriorly along the "
    "abdomen/chest, Chong internally along the spine with a superficial branch "
    "beside the Kidney meridian. Chinese: Yi Yuan San Qi -- "
    "\u201cone source, three branches.\u201d"
)

# The 4 Confluent (Ba Mai Jiao Hui Xue / "master-couple") pairs -- the
# clinically central content of this week. Format: (vessel pair, master pt,
# couple pt, shared indication note)
CONFLUENT_PAIRS = [
    ("Chong Mai + Yin Wei Mai", "SP 4  Gongsun", "PC 6  Neiguan",
     "Stomach, heart, chest -- Gongsun opens Chong, Neiguan opens Yin Wei; combine to treat chest/epigastric/cardiac patterns."),
    ("Du Mai + Yang Qiao Mai", "SI 3  Houxi", "BL 62  Shenmai",
     "Inner canthus, neck, ear, shoulder -- spinal stiffness/pain, febrile disease, mental disorders."),
    ("Ren Mai + Yin Qiao Mai", "LU 7  Lieque", "KI 6  Zhaohai",
     "Lung, throat, chest, diaphragm -- cough, sore throat, chest tightness."),
    ("Dai Mai + Yang Wei Mai", "GB 41  Zulinqi", "SJ 5  Waiguan",
     "Outer canthus, ear, cheek, neck, shoulder -- lateral-body pain, febrile disease, exterior patterns."),
]

# ---------------------------------------------------------------------------
# Per-vessel structured data
# ---------------------------------------------------------------------------

GV = dict(
    name="Governor Vessel", pinyin="Du Mai", abbr="GV", accent=ACCENT_GV,
    sea="Sea of the Yang Meridians", own_points=True, n_points=28,
    first_point="GV 1  Changqiang -- midway between the tip of the coccyx and the anus (prone position)",
    last_point="GV 28  Yinjiao -- at the junction of the frenulum under the top lip and the gum",
    course=[
        "Arises from the lower abdomen, emerges at the perineum (near CV 1 Huiyin)",
        "Runs posteriorly along the interior of the spinal column (GV 1 Changqiang -> BL 12 Fengmen)",
        "Reaches the nape (GV 16 Fengfu), enters the brain",
        "Ascends to the vertex (GV 20 Baihui)",
        "Winds along the forehead to the columnella of the nose, ends at GV 28 Yinjiao",
    ],
    coalescent_points=["BL 12  Fengmen", "CV 1  Huiyin"],
    confluent_point="SI 3  Houxi",
    confluent_partner="BL 62  Shenmai (Yang Qiao Mai)",
    functions=[
        "Sea of the yang meridians -- governs the qi of all yang meridians",
        "Guides and stimulates the body's yang qi; keeps the body warm",
        "Confluent point Houxi (SI 3) treats spinal pain/heaviness and relieves fever",
    ],
    pathology=["Stiffness and pain along the spinal column", "Heavy sensation in the head",
               "Vertigo and shaking", "Mental disorders", "Fever"],
    figure="CAM_GV",
    confluent_location="Ulnar side of the hand, just behind the head of the 5th metacarpal bone, at the junction of the palm and dorsal skin.",
    mnemonic="GV runs the length of the spine and ends at the nose -- think \u201cspine to face, yang runs the race.\u201d Its confluent point Houxi (SI 3) sits on the SAME side of the hand as the vessel's posterior course, which is why it treats spinal stiffness so directly.",
)

CV = dict(
    name="Conception Vessel", pinyin="Ren Mai", abbr="CV", accent=ACCENT_CV,
    sea="Sea of the Yin Meridians", own_points=True, n_points=24,
    first_point="CV 1  Huiyin -- between the anus and root of scrotum (M) / posterior labial commissure (F)",
    last_point="CV 24  Chengjiang -- in the depression at the center of the chin",
    course=[
        "Arises from inside the lower abdomen, emerges at the perineum (CV 1 Huiyin)",
        "Runs anteriorly to the pubic region, ascends along the interior of the abdomen (through CV 4 Guanyuan)",
        "Continues along the front midline of abdomen and chest, reaches the throat",
        "Curves around the lips (meets GV 28 Yinjiao)",
        "Passes through the cheek, enters the infraorbital region, ends at ST 1 Chengqi",
    ],
    coalescent_points=["ST 1  Chengqi", "GV 28  Yinjiao"],
    confluent_point="LU 7  Lieque",
    confluent_partner="KI 6  Zhaohai (Yin Qiao Mai)",
    functions=[
        "Sea of the yin meridians -- receives and bears the qi of all yin meridians",
        "CV 4 Guanyuan is a major Xi/tonification point (\"the source point in the lower abdomen\")",
        "Confluent point Lieque (LU 7) is also the Luo-Connecting point of the Lung meridian",
    ],
    pathology=["Pathology of the yin channels (esp. Liver + Kidney)", "Infertility",
               "Disorders of the urogenital system", "Irregular menstruation", "Abdominal pain"],
    figure=None,
    confluent_location="Radial (thumb) side of the forearm, about 1.5 cun above the transverse wrist crease.",
    mnemonic="CV is GV's mirror image: anterior midline instead of posterior, sea of YIN instead of yang. Its confluent point Lieque (LU 7) doubles as the Lung Luo-Connecting point -- one point, two jobs, which is why it's so often chosen for throat/chest complaints tied to yin-channel patterns.",
)

CHONG = dict(
    name="Thoroughfare Vessel", pinyin="Chong Mai", abbr="Chong", accent=ACCENT_CHONG,
    sea="Sea of the 12 Meridians \u00b7 Sea of Blood \u00b7 Sea of the Zang-Fu Organs",
    own_points=False, n_points=None,
    first_point=None, last_point=None,
    course=[
        "Arises from inside the lower abdomen, emerges at the perineum (CV 1 Huiyin)",
        "Ascends inside the spinal column",
        "Superficial branch passes through ST 30 Qichong, communicates with the Kidney meridian",
        "Runs along both sides of the abdomen (beside KI 11-KI 21) up to the throat",
        "Curves around the lips",
    ],
    coalescent_points=["CV 1", "CV 7", "ST 30", "KI 11", "KI 12", "KI 13", "KI 14", "KI 15",
                        "KI 16", "KI 17", "KI 18", "KI 19", "KI 20", "KI 21"],
    confluent_point="SP 4  Gongsun",
    confluent_partner="PC 6  Neiguan (Yin Wei Mai)",
    functions=[
        "Sea of the 12 meridians; sea of the zang-fu organs; sea of blood",
        "Runs parallel to the Kidney meridian -- shares 11 Kidney-meridian points as coalescent points",
        "Confluent point Gongsun (SP 4) is also the Luo-Connecting point of the Spleen meridian",
    ],
    pathology=["Gynecological disorders", "Male urological disease / male infertility", "Abdominal pain"],
    figure=None,
    confluent_location="Medial side of the foot, in front of and below the base of the 1st metatarsal bone.",
    mnemonic="Chong shares its very first station (CV1 Huiyin) with GV and CV -- \u201cone source, three branches\u201d -- then runs the length of the trunk right beside the Kidney meridian. Three \u201csea\u201d titles (12 meridians / blood / zang-fu organs) makes it the single most powerful of the 8 vessels for constitutional/gynecological work.",
)

DAI = dict(
    name="Belt Vessel", pinyin="Dai Mai", abbr="Dai", accent=ACCENT_DAI,
    sea="The Binding/Girdling Vessel (not a \u201csea\u201d)", own_points=False, n_points=None,
    first_point=None, last_point=None,
    course=[
        "Originates below the hypochondriac region (GB 26 Daimai)",
        "Wraps horizontally around the waist (GB 27 Wushu, GB 28 Weidao)",
        "The ONLY one of the 8 vessels that runs horizontally rather than vertically",
    ],
    coalescent_points=["GB 26  Daimai", "GB 27  Wushu", "GB 28  Weidao"],
    confluent_point="GB 41  Zulinqi",
    confluent_partner="SJ 5  Waiguan (Yang Wei Mai)",
    functions=[
        "Controls/binds all the longitudinally-running meridians -- \u201cthe belt that holds them together\u201d",
        "Closely related to Du, Ren, and Chong Meridians",
        "Structurally unique: horizontal, not vertical -- no true \u201csea\u201d title in the lecture",
    ],
    pathology=["Fullness in the abdomen", "Irregular menstruation", "Pain in the lumbar region"],
    figure=None,
    confluent_location="Dorsum of the foot, near the proximal end of the 4th toe.",
    mnemonic="Dai is the odd one out geometrically -- picture a literal belt cinched around the waist at GB 26/27/28, binding every vertical vessel and meridian that passes through it. No course to trace top-to-bottom, just a horizontal loop -- which is exactly why \u201cwaist pain with no clear up/down direction\u201d points here.",
)

YANG_QIAO = dict(
    name="Yang Heel Vessel", pinyin="Yang Qiao Mai", abbr="Yang Qiao", accent=ACCENT_QIAO,
    sea=None, own_points=False, n_points=None, first_point=None, last_point=None,
    course=[
        "Starts on the lateral aspect of the heel (BL 62 Shenmai, BL 61)",
        "Ascends along the posterior border of the fibula (BL 59), external malleolus",
        "Lateral thigh (GB 29), posterior hypochondrium, posterior axillary fold",
        "Shoulder (SI 10, LI 15, LI 16), neck, corner of the mouth (ST 4), inner canthus (SI 1, BL 1)",
        "Forehead, ends by merging into the Gallbladder meridian (GB 20 Fengchi)",
    ],
    coalescent_points=["BL 1", "BL 59", "BL 61", "BL 62", "GB 20", "GB 29", "SI 10", "ST 1", "ST 3", "ST 4"],
    coalescent_flag="Slide header states \u201c(12)\u201d coalescent points but only 10 are named -- flagged for Dr. Zhang.",
    confluent_point="BL 62  Shenmai",
    confluent_partner="SI 3  Houxi (Du Mai)",
    functions=[
        "Balances movement of the extremities together with Yin Qiao (they meet at the inner canthus)",
        "Governs wakefulness / activity -- keeps the body alert and active",
    ],
    pathology=["Diseases of the eyes", "Tightness/spasm of lateral lower-leg muscles (seizures, paralysis)",
               "Pain and stiffness in the lumbar region"],
    figure=None,
    confluent_location="Directly below the external malleolus, in a depression between BL 60 and BL 62's landmark bony structures.",
    mnemonic="Yang Qiao = LATERAL heel to LATERAL/posterior head, ending by merging into GB. Pairs with Du Mai (both \u201cyang\u201d) via Houxi + Shenmai. Remember the function split with its Yin partner: Yang Qiao keeps you UP and moving; Yin Qiao brings you DOWN to rest.",
)

YIN_QIAO = dict(
    name="Yin Heel Vessel", pinyin="Yin Qiao Mai", abbr="Yin Qiao", accent=ACCENT_QIAO,
    sea=None, own_points=False, n_points=None, first_point=None, last_point=None,
    course=[
        "Starts at the posterior aspect of the navicular bone (KI 6 Zhaohai)",
        "Ascends via the upper medial malleolus, posterior medial leg/thigh (KI 8)",
        "External genitalia, abdomen and chest, supraclavicular fossa",
        "Adam's apple (in front of ST 9 Renying), zygoma",
        "Ends at the inner canthus (BL 1), meeting the Bladder meridian and Yang Qiao Mai",
    ],
    coalescent_points=["KI 6", "KI 8", "BL 1"],
    confluent_point="KI 6  Zhaohai",
    confluent_partner="LU 7  Lieque (Ren Mai)",
    functions=[
        "Balances movement of the extremities together with Yang Qiao (meet at inner canthus)",
        "Governs calm / rest -- promotes relaxation and restful sleep (opposite of Yang Qiao)",
    ],
    pathology=["Diseases of the eyes", "Tightness/spasm of medial lower-leg muscles (seizures, paralysis)",
               "Lower abdominal pain"],
    figure=None,
    confluent_location="Directly below the medial malleolus, in the depression at the posterior aspect of the navicular bone (this IS the confluent point -- KI 6 is also the vessel's starting point).",
    mnemonic="Yin Qiao = MEDIAL heel to the inner canthus, merging into Bladder/Yang Qiao at the eye. The two Heel vessels literally meet at the inner canthus -- that shared meeting point is why both show up on \u201ceye disease\u201d pathology lists. Yin Qiao's job: calm, rest, sleep.",
)

YANG_WEI = dict(
    name="Yang Link Vessel", pinyin="Yang Wei Mai", abbr="Yang Wei", accent=ACCENT_WEI,
    sea=None, own_points=False, n_points=None, first_point=None, last_point=None,
    course=[
        "Originates at the lateral side of the heel (BL 63 Jinmen)",
        "Ascends via the external malleolus, lateral leg (GB 35), hip region",
        "Posterior hypochondriac/costal region, posterior axilla, shoulder (SI 10, SJ 15, GB 21)",
        "Retroauricular region, forehead (GB 13, GB 14), back of neck (GB 15-20)",
        "Ends by meeting the Du Meridian (GV 15, GV 16)",
    ],
    coalescent_points=["BL 63", "SI 10", "GV 15", "GV 16", "GB 21", "GB 35", "GB 13", "GB 14",
                        "GB 15", "GB 16", "GB 17", "GB 18", "GB 19", "GB 20"],
    coalescent_flag="Slide header states \u201c(15)\u201d coalescent points but only 14 are named -- flagged for Dr. Zhang.",
    confluent_point="SJ 5  Waiguan",
    confluent_partner="GB 41  Zulinqi (Dai Mai)",
    functions=[
        "Connects to all yang meridians, especially the Du Meridian",
        "Dominates the exterior of the whole body",
        "Joint function with Yin Wei: regulates qi flow between the yin and yang meridians",
    ],
    pathology=["Chills and fever, vertigo", "Muscular fatigue, stiffness, and pain",
               "Pain and distension in the waist"],
    figure=None,
    confluent_location="Back of the forearm, two finger-widths above the wrist crease, between the radius and ulna.",
    mnemonic="Yang Wei runs UP the lateral body from the heel, gathers nearly the whole GB channel along the head (GB13-20) before merging into Du Mai -- \u201cdominates the exterior.\u201d Waiguan (SJ 5) pairs with Zulinqi (GB 41, Dai Mai) -- both vessels patrol the lateral/exterior body, which is why the pairing treats lateral-body and febrile-exterior patterns.",
)

YIN_WEI = dict(
    name="Yin Link Vessel", pinyin="Yin Wei Mai", abbr="Yin Wei", accent=ACCENT_WEI,
    sea=None, own_points=False, n_points=None, first_point=None, last_point=None,
    course=[
        "Starts at the medial aspect of the leg (KI 9 Zhubin)",
        "Ascends via the medial leg and thigh, abdomen",
        "Spleen meridian (SP 13, SP 15, SP 16), chest (LR 14)",
        "Neck, meets the CV Meridian (CV 22, CV 23)",
    ],
    coalescent_points=["KI 9", "SP 13", "SP 15", "SP 16", "LR 14", "CV 22", "CV 23"],
    confluent_point="PC 6  Neiguan",
    confluent_partner="SP 4  Gongsun (Chong Mai)",
    functions=[
        "Connects to all yin meridians, especially the Ren Meridian",
        "Dominates the interior of the whole body",
        "Joint function with Yang Wei: regulates qi flow and maintains yin-yang equilibrium",
    ],
    pathology=["Chest pain", "Waist pain", "Hard lumps in the upper abdomen"],
    figure=None,
    confluent_location="Two finger-widths above the wrist crease, on the inner (palmar) forearm, between the two tendons.",
    mnemonic="Yin Wei runs UP the medial body from KI 9, crosses SP and LR points on its way to the chest, then merges into Ren Mai at the neck -- \u201cdominates the interior.\u201d Neiguan (PC 6) pairs with Gongsun (SP 4, Chong Mai) -- the single most-used confluent pairing in clinic for chest, stomach, and heart complaints (deep-breathing + bilateral pressure, per Dr. Zhang's demonstration).",
)

ALL_VESSELS = [GV, CV, CHONG, DAI, YANG_QIAO, YIN_QIAO, YANG_WEI, YIN_WEI]

# Structural facts that don't pertain to any organ -- the defining trait of
# all 8 Extraordinary Vessels, used repeatedly across all Week 7 documents.
NO_ORGAN_NOTE = (
    "None of the Eight Extraordinary Vessels pertains to a zang or fu organ, "
    "and none has an interior-exterior paired relationship the way the 12 "
    "primary meridians do. Only Du Mai (GV) and Ren Mai (CV) have their own "
    "dedicated acupuncture points -- the other six vessels borrow points from "
    "the primary meridians they cross (their \u201ccoalescent points,\u201d Jiao Hui Xue)."
)

# MAINT review items pulled directly from Dr. Zhang's Quiz 5 verbal review in
# the Week 7 transcript, used in the Quiz Kit and Cram Sheet.
QUIZ5_REVIEW_TRANSCRIPT_ITEMS = [
    "PC's pertaining organ is the Pericardium; connecting organ is San Jiao (Triple Energizer) -- an interior-exterior (yin-yang) pair.",
    "PC has three branches: internal, superficial, and an upper branch; it starts at the chest and runs to the hand.",
    "The Liver meridian is the only primary meridian that runs across/connects with the external genitalia.",
    "The Liver meridian connects to the Lung meridian (closing the 12-meridian circulation sequence).",
    "Both Hand-Shaoyang (SJ) and Foot-Shaoyang (GB) meridians run across the ear and the lateral side of the head -- combine both for lateral headache.",
    "GB starts at the outer canthus and ends at the tip of the 4th toe.",
]
