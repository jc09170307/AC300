"""Week 8 -- 15 Luo-Connecting Vessels, 12 Divergent Channels, 12 Muscle/Sinew
Regions, 12 Cutaneous Regions. Data sourced and verified against
Lecture8vivian1119.pdf (85 slides, Dr. Zhang, slides 1-61 delivered live;
slides 62-85 assigned as self-study / reference, confirmed against the
AC300_Week_8_Transcript.txt live-class transcript).

FLAGGED DISCREPANCIES (not silently resolved):
  - Slide 85 ("For Next Week") reads "Homework2 Due Week 8" / "Quiz 2" and a
    reading assignment referencing "intro to all 12 Primary Meridians" --
    this text does not match Week 8/9's actual position in the course and
    appears to be an un-updated template slide carried over from an earlier
    week. Dr. Zhang stated VERBALLY in lecture (transcript ~1:59:00) that
    "this week we do not have any homework" and "next week we also have not
    adding quiz, just review." Per content-integrity rule, the verbal
    statement is treated as authoritative for homework/quiz status this
    week, but the slide text is flagged rather than silently discarded.
  - No written-syllabus table entry for Week 8 was available in project
    files to cross-check topic placement; placement below is drawn from the
    live lecture + slide deck only and should be checked against the
    syllabus when available.
  - Middle Circuit (PC/SJ/GB/LR) collaterals + divergent channels were
    covered live only through PC and SJ (slides 58-62); GB/LR collateral
    and divergent-channel narration (slides 66-70) and ALL 12 Muscle
    Region / Cutaneous Region slides (63-72, 79-83) were NOT reached live
    -- Dr. Zhang said she would "study from the middle sacer[sic]" (Jueyin/
    Shaoyang circuit) "in the next week." Since next week is review-only
    (no new content, no quiz), this slide content is included here as
    verified slide-deck material (Dr. Zhang's own slides, not a third-party
    source) but flagged as NOT YET LIVE-LECTURED -- treat as read-ahead /
    self-study material, not confirmed-by-live-walkthrough content.
  - RESOLVED (2026-09-02): Slide 85's MOA citation "p.16-17, 26-28" was
    checked against physical CAM/MOA copies (photographed TOC pages) and is
    CORRECT -- MOA pg.16 = twelve divergent channels, pg.26 = Luo-connecting/
    sinew/minute collaterals, pg.27 = twelve cutaneous regions. This part of
    the flag is lifted. The CAM citation "p.88-114" was NOT correct -- real
    range is CAM p.93-118 (IV. Divergent Meridians + Fifteen Collaterals,
    starting p.93; V. Muscle Regions + Cutaneous Regions, ending p.118; p.88
    belongs to Week 7's Eight Extra Meridians theory section instead). The
    "intro to 12 Primary Meridians" phrasing and the Quiz2/Homework2 text
    remain flagged as stale template leftovers.
"""

NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.10, 0.10, 0.10)
GRAY = (0.40, 0.40, 0.40)

# Circuit accent colors (kept consistent with element colors used across the
# course for the organs anchoring each circuit -- never gray/purple fallback)
ACCENT_OUTER = (0.616, 0.478, 0.216)     # amber/ochre -- Earth-adjacent anterior circuit (LU/LI, ST/SP)
ACCENT_INNER = (0.75, 0.20, 0.16)        # deep red -- Fire circuit (HT/SI) blended toward Water (BL/KI)
ACCENT_INNER_WATER = (0.16, 0.32, 0.60)  # blue -- Water half of inner circuit (BL/KI)
ACCENT_MIDDLE = (0.85, 0.42, 0.38)       # coral/lighter red -- Ministerial Fire circuit (PC/SJ)
ACCENT_MIDDLE_WOOD = (0.20, 0.48, 0.27)  # green -- Wood half of middle circuit (GB/LR)
ACCENT_LUO = (0.55, 0.38, 0.16)          # amber-brown -- 15 Collaterals
ACCENT_DIVERGENT = (0.16, 0.44, 0.46)    # slate teal -- 12 Divergent Channels
ACCENT_SINEW = (0.45, 0.30, 0.55)        # muted purple -- 12 Muscle/Sinew Regions (structural, not organ-colored)
ACCENT_CUTANEOUS = (0.35, 0.35, 0.35)    # kept distinct via LBLUE tint boxes, not flat gray, in layout

READING_NOTE = (
    "Written-syllabus Week 8 reading entry not available in project files. "
    "Verified against physical CAM/MOA copies: MOA p.16-17 (twelve divergent "
    "channels) + p.26-28 (Luo-connecting/sinew/cutaneous regions) -- CONFIRMED "
    "correct. CAM p.93-118 (IV. Divergent Meridians + Fifteen Collaterals; "
    "V. Muscle Regions + Cutaneous Regions) -- CORRECTED from slide 85's "
    "\u201cp.88-114,\u201d which bled into Week 7's territory and cut off before the "
    "Cutaneous Regions section finished. Still no written-syllabus entry to "
    "cross-check against; confirm with Dr. Zhang before treating as final."
)

HOMEWORK_QUIZ_NOTE = (
    "Dr. Zhang stated verbally that Week 8 has NO new homework, and Week 9 "
    "(review week) has NO new quiz -- Week 9 is pure review before the final "
    "exam. Slide 85's \u201cHomework2 Due Week 8 / Quiz 2\u201d text conflicts with "
    "this and is flagged as likely stale template text, not silently "
    "corrected."
)

# ---------------------------------------------------------------------------
# THE THREE CIRCUITS -- Dr. Zhang's organizing structure for the whole
# lecture (slide 15). Used to group every topic below.
# ---------------------------------------------------------------------------
CIRCUITS = [
    dict(key="outer", name="Outer Circuit (Anterior)", pinyin="Yangming / Taiyin",
         pairs=["LU / LI", "ST / SP"], accent=ACCENT_OUTER,
         note="Chest->Hand->Head->Foot->Chest. Anterior aspect of the body."),
    dict(key="inner", name="Inner Circuit (Posterior)", pinyin="Taiyang / Shaoyin",
         pairs=["HT / SI", "BL / KI"], accent=ACCENT_INNER,
         note="Chest->Hand->Head->Foot->Chest, posterior aspect. BL is the largest meridian (67 pts, 6 branches)."),
    dict(key="middle", name="Middle Circuit (Lateral)", pinyin="Shaoyang / Jueyin",
         pairs=["PC / SJ", "GB / LR"], accent=ACCENT_MIDDLE,
         note="Lateral aspect. GB/LR muscle regions + cutaneous regions were slide-deck content not reached live (self-study)."),
]

THREE_CIRCUITS_RULE = (
    "Every circuit follows the same four-leg rule: the Yin meridian of the Hand runs chest->hand; "
    "its paired Yang meridian of the Hand runs hand->head; the next Yang meridian, of the Foot, runs "
    "head->foot; and the paired Yin meridian of the Foot runs foot->abdomen/chest, closing the loop "
    "back to the next Yin-Hand meridian. Outer Circuit = LU->LI->ST->SP. Inner Circuit = "
    "HT->SI->BL->KI. Middle Circuit = PC->SJ->GB->LR."
)

# ---------------------------------------------------------------------------
# 15 COLLATERALS (Luo-Connecting Points) -- slide 76 table, verbatim
# structure, cross-checked against slides 19-20, 29-30, 39-40, 47-48,
# 58-59, 66-67, 74 narrative descriptions.
# ---------------------------------------------------------------------------
LUO_POINTS = [
    dict(circuit="outer", meridian="Lung Meridian, Hand-Taiyin", abbr="LU",
         point="LU 7  Lieque", partner="Large Intestine Meridian, Hand-Yangming",
         course="Arises from Lieque (LU 7); runs to the LI meridian. A second branch follows the "
                "LU meridian into the palm and spreads through the thenar eminence.",
         note="Lieque is ALSO the Confluent (opening) point of the Conception Vessel (Ren Mai) -- "
              "one point, two jobs, reviewed Week 7.",
         accent=ACCENT_OUTER),
    dict(circuit="outer", meridian="Large Intestine Meridian, Hand-Yangming", abbr="LI",
         point="LI 6  Pianli", partner="Lung Meridian, Hand-Taiyin",
         course="Starts from Pianli (LI 6), joins the LU meridian 3 cun above the wrist. A branch runs "
                "along the arm to Jianyu (LI 15), crosses the jaw, and extends to the teeth; another "
                "branch enters the ear to join the Thoroughfare of Hearing area.",
         note="LU7 + LI6 sit closest to each other around the wrist -- combine for throat/LI symptoms together.",
         accent=ACCENT_OUTER),
    dict(circuit="outer", meridian="Stomach Meridian, Foot-Yangming", abbr="ST",
         point="ST 40  Fenglong", partner="Spleen Meridian, Foot-Taiyin",
         course="Starts from Fenglong (ST 40), 8 cun above the external malleolus; connects with the "
                "SP meridian. A branch runs up the lateral tibia to the vertex, converging with the other "
                "Yang meridians on the head/neck, then runs back down to connect with the throat.",
         note="Rule reminder: connecting points of Foot meridians cluster around the ankle (malleolus).",
         accent=ACCENT_OUTER),
    dict(circuit="outer", meridian="Spleen Meridian, Foot-Taiyin", abbr="SP",
         point="SP 4  Gongsun", partner="Stomach Meridian, Foot-Yangming",
         course="Branches out at Gongsun (SP 4), 1 cun posterior to the base of the 1st metatarsal bone; "
                "joins the ST meridian. A branch runs upward to the abdomen and connects with the "
                "stomach and intestines.",
         note="Gongsun is ALSO the Confluent point of Chong Mai (paired with PC 6 Neiguan) -- reviewed Week 7.",
         accent=ACCENT_OUTER),
    dict(circuit="inner", meridian="Heart Meridian, Hand-Shaoyin", abbr="HT",
         point="HT 5  Tongli", partner="Small Intestine Meridian, Hand-Taiyang",
         course="Branches out at Tongli (HT 5), 1 cun above the transverse wrist crease; connects with "
                "the SI meridian. About 1.5 cun above the wrist it re-enters the meridian proper, enters "
                "the heart, then runs to the root of the tongue and connects with the eye system.",
         note="Rule reminder: connecting points of Hand meridians cluster around the wrist.",
         accent=ACCENT_INNER),
    dict(circuit="inner", meridian="Small Intestine Meridian, Hand-Taiyang", abbr="SI",
         point="SI 7  Zhizheng", partner="Heart Meridian, Hand-Shaoyin",
         course="Originates from Zhizheng (SI 7), 5 cun above the wrist; connects with the HT meridian. "
                "A branch runs upward, crosses the elbow, and connects with Jianyu (LI 15).",
         note="HT5 (1 cun above wrist) and SI7 (5 cun above wrist) are the paired connecting points for this circuit.",
         accent=ACCENT_INNER),
    dict(circuit="inner", meridian="Bladder Meridian, Foot-Taiyang", abbr="BL",
         point="BL 58  Feiyang", partner="Kidney Meridian, Foot-Shaoyin",
         course="Arises from Feiyang (BL 58), 7 cun above the external malleolus; connects with the KI "
                "meridian.",
         note="BL is the largest meridian in the body -- 67 points, 6 branches (per lecture).",
         accent=ACCENT_INNER_WATER),
    dict(circuit="inner", meridian="Kidney Meridian, Foot-Shaoyin", abbr="KI",
         point="KI 4  Dazhong", partner="Bladder Meridian, Foot-Taiyang",
         course="Originates from Dazhong (KI 4), posterior to the internal malleolus; crosses the heel "
                "and joins the BL meridian. A branch follows the KI meridian upward to below the "
                "pericardium, then pierces through the lumbar vertebrae.",
         note="Do not confuse with KI 6 Zhaohai (the Confluent point of Yin Qiao Mai, reviewed Week 7).",
         accent=ACCENT_INNER_WATER),
    dict(circuit="middle", meridian="Pericardium Meridian, Hand-Jueyin", abbr="PC",
         point="PC 6  Neiguan", partner="Sanjiao (Triple Energizer) Meridian, Hand-Shaoyang",
         course="Begins from Neiguan (PC 6), 2 cun above the wrist, disperses between the two tendons, "
                "runs along the PC meridian to the pericardium, and finally connects with the heart.",
         note="Neiguan is ALSO the Confluent point of Yin Wei Mai (paired with SP 4 Gongsun) -- the "
              "most-used confluent pairing in clinic (Week 7).",
         accent=ACCENT_MIDDLE),
    dict(circuit="middle", meridian="Sanjiao Meridian, Hand-Shaoyang", abbr="SJ",
         point="SJ 5  Waiguan", partner="Pericardium Meridian, Hand-Jueyin",
         course="Arises from Waiguan (SJ 5), 2 cun above the dorsum of the wrist; travels up the "
                "posterior arm and over the shoulder, disperses in the chest, converging with the PC "
                "meridian.",
         note="Waiguan is ALSO the Confluent point of Yang Wei Mai (paired with GB 41 Zulinqi) -- Week 7.",
         accent=ACCENT_MIDDLE),
    dict(circuit="middle", meridian="Gallbladder Meridian, Foot-Shaoyang", abbr="GB",
         point="GB 37  Guangming", partner="Liver Meridian, Foot-Jueyin",
         course="Begins from Guangming (GB 37), 5 cun above the external malleolus; joins the LR "
                "meridian, then runs downward and disperses over the dorsum of the foot.",
         note="Self-study slide content (not reached live) -- confirm against Dr. Zhang's review next week.",
         accent=ACCENT_MIDDLE_WOOD, self_study=True),
    dict(circuit="middle", meridian="Liver Meridian, Foot-Jueyin", abbr="LR",
         point="LR 5  Ligou", partner="Gallbladder Meridian, Foot-Shaoyang",
         course="Starts from Ligou (LR 5), 5 cun above the internal malleolus; connects with the GB "
                "meridian. A branch runs up the leg to the genitals.",
         note="Self-study slide content (not reached live) -- confirm against Dr. Zhang's review next week.",
         accent=ACCENT_MIDDLE_WOOD, self_study=True),
]

# The 3 "extra" collaterals that bring the total from 12 to 15 (slide 74, 75, 76)
LUO_EXTRA = [
    dict(name="Collateral of the Conception Vessel (Ren Mai)", point="CV 15  Jiuwei",
         course="Separates from the Governor Vessel at the lower end of the sternum; from Jiuwei "
                "(CV 15) it spreads over the abdomen.",
         why="Covers the FRONT midline -- balances the GV collateral on the back midline.",
         accent=ACCENT_LUO),
    dict(name="Collateral of the Governor Vessel (Du Mai)", point="GV 1  Changqiang",
         course="Arises from Changqiang (GV 1) in the perineum; runs upward along both sides of the "
                "spine to the nape and spreads over the top of the head. At the scapular region it "
                "connects with the Bladder meridian and pierces through the spine.",
         why="Covers the BACK midline -- balances the CV collateral on the front midline.",
         accent=ACCENT_LUO),
    dict(name="Great (Major) Collateral of the Spleen", point="SP 21  Dabao",
         course="Begins from Dabao (SP 21), emerges 3 cun below Yuanye (GB 22), and spreads through "
                "the chest and hypochondriac (lateral costal) region, gathering the blood all over the "
                "body.",
         why="Covers the LATERAL side of the chest -- the one area the 12 paired-meridian collaterals "
             "leave uncovered. This is WHY there are 15 collaterals, not 12: the body needs front "
             "(CV), back (GV), AND lateral (Spleen Great Luo) coverage to stay in harmony.",
         accent=ACCENT_LUO),
]

LUO_DEFINITION = (
    "The 12 Primary Meridians and the Conception and Governor Vessels each give off a collateral "
    "branch, totaling fifteen when combined with the Major (Great) Collateral of the Spleen -- "
    "collectively the \u201c15 Collaterals\u201d (Luo Mai). Each is named after the acupoint from which it "
    "originates -- its Luo-Connecting point."
)

LUO_WHY_15_LOGIC = (
    "Why 15, not 12? The 12 paired meridians (6 yin-yang pairs) each need a Luo-Connecting point to "
    "link them -- that's 12. But the 12 primary meridians don't have their own acupoints EVERYWHERE "
    "harmony is needed: two extra vessels (Du Mai/GV and Ren Mai/CV) have their own dedicated points, "
    "so they each need their own collateral too -- that's 14. And there is one region no collateral "
    "yet covers: the LATERAL side of the chest (CV covers front, GV covers back, but nothing covers "
    "the side). The Spleen's Great Collateral (Dabao, SP 21) fills that gap -- bringing the total to 15."
)

LUO_FUNCTION = (
    "Function: the Luo-Connecting point's job is to link (\u7edc, luo = \u201cnet/connect\u201d) each meridian to "
    "its interior-exteriorly paired partner, strengthening their shared function and treating disorders "
    "that involve both. Distinguish from a Yuan-Source point (treats disorders of its OWN meridian) and "
    "from a Confluent point (opens an Extraordinary Vessel). One acupoint can carry more than one of "
    "these special-point identities at once (e.g. LU 7 is both Luo point AND CV's Confluent point) -- "
    "when a point carries multiple special functions, its clinical reach is broader/stronger."
)

# ---------------------------------------------------------------------------
# 12 DIVERGENT CHANNELS -- slide 77 master table + narrative slides
# 22-25, 31-33, 41-43, 49-51, 60-62, 68-70. The "Li-He-Chu-merge" framework
# (Chinese: Li = beginning, He = organs/systems involved, Chu = exiting,
# then merges back to its Yang partner meridian).
# ---------------------------------------------------------------------------
DIVERGENT_DEFINITION = (
    "The 12 Divergent Meridians (Jing Bie) originate from the 12 Primary Meridians, distribute "
    "throughout the chest, abdomen, and head, connect the superficial (exterior) and interior "
    "meridians, and strengthen the relationship with the Zang-Fu organs. Unlike the primary "
    "meridians, they have NO acupuncture points of their own and do NOT pertain to an organ -- their "
    "job is purely to reinforce/enhance the existing interior-exterior meridian relationships by "
    "running a deeper course."
)

DIVERGENT_FEATURES = [
    "Govern the INSIDE of the body (vs. collaterals, which control the body surface).",
    "Branch out from the 12 primary meridians; distributed mainly on the chest, abdomen, and head.",
    "Have NO acupuncture points of their own (points live in the skin; divergent channels run deep).",
    "Have no pertaining zang-fu organ of their own -- they strengthen the primary meridian's existing organ relationship instead.",
    "Function: enhance/strengthen the relationship between meridian and zang-fu organs, and supplement pathway coverage the primary meridian doesn't reach.",
]

LI_HE_CHU_MERGE = (
    "Every Divergent Meridian follows the same 4-part running structure -- Chinese: Li \u2013 He \u2013 Chu \u2013 "
    "He (again). English glosses used in lecture: LI = beginning (where it branches off the primary "
    "meridian), HE = organs/systems the deep course involves, CHU = exiting (where it re-emerges to "
    "the surface), and finally it MERGES back into its paired YANG primary meridian. All 6 Yin "
    "divergent meridians merge into their paired Yang meridian at the head/face -- the Yin divergent "
    "channels never resurface as separate Yin channels."
)

DIVERGENT_CHANNELS = [
    dict(circuit="outer", meridian="Lung (LU)", abbr="LU", pair_label="LU + LI Confluence",
         beginning="The axilla (from the Lung meridian)",
         organs="Lung, Large Intestine, Throat",
         exiting="Supraclavicular fossa",
         merging="Hand-Yangming (Large Intestine)",
         narrative="Deriving from the Lung meridian in the axilla -> chest, anterior to the Pericardium "
                    "meridian -> the lung -> the large intestine. A branch: emerges at the clavicle, runs "
                    "upward from the lung -> the throat -> merges into the Large Intestine meridian.",
         accent=ACCENT_OUTER),
    dict(circuit="outer", meridian="Large Intestine (LI)", abbr="LI", pair_label="LU + LI Confluence",
         beginning="Hand / Spine",
         organs="Spine, Large Intestine, Lung, Throat",
         exiting="Supraclavicular fossa",
         merging="Hand-Yangming (itself -- LI is the Yang partner)",
         narrative="Deriving from the LI meridian on the hand -> shoulder -> arm -> breast. Branch: "
                    "shoulder -> top of the shoulder -> nape -> the spine, then downward to the large "
                    "intestine and the lung. Branch: shoulder -> emerging at the supraclavicular fossa -> "
                    "the throat -> the LI meridian.",
         accent=ACCENT_OUTER),
    dict(circuit="outer", meridian="Stomach (ST)", abbr="ST", pair_label="ST + SP Confluence",
         beginning="Thigh, abdomen (from the Stomach meridian)",
         organs="Abdomen, stomach, spleen, heart, esophagus, mouth, nose, eye",
         exiting="Mouth",
         merging="Foot-Yangming (itself -- ST is the Yang partner)",
         narrative="From the ST meridian (thigh) -> abdomen -> stomach -> spleen -> through the heart -> "
                    "alongside the esophagus -> the mouth -> upward beside the nose -> the eye -> merges "
                    "into the ST meridian.",
         accent=ACCENT_OUTER),
    dict(circuit="outer", meridian="Spleen (SP)", abbr="SP", pair_label="ST + SP Confluence",
         beginning="Thigh (from the Spleen meridian)",
         organs="Throat, tongue",
         exiting="Throat (converges upward with the ST divergent channel)",
         merging="Foot-Yangming (Stomach)",
         narrative="Deriving from the SP meridian on the thigh -> converges upward with the Divergent "
                    "Meridian of the Stomach -> the throat -> the tongue.",
         accent=ACCENT_OUTER),
    dict(circuit="inner", meridian="Heart (HT)", abbr="HT", pair_label="HT + SI Confluence",
         beginning="Axillary fossa (from the Heart meridian)",
         organs="Heart, chest, throat",
         exiting="Face",
         merging="Hand-Taiyang (Small Intestine)",
         narrative="From the HT meridian (axillary fossa) -> the chest -> the heart -> the throat -> "
                    "emerging on the face -> the SI meridian (inner canthus).",
         accent=ACCENT_INNER),
    dict(circuit="inner", meridian="Small Intestine (SI)", abbr="SI", pair_label="HT + SI Confluence",
         beginning="Shoulder joint (from the Small Intestine meridian)",
         organs="Heart, small intestine",
         exiting="Axilla / abdomen",
         merging="Hand-Taiyang (itself -- SI is the Yang partner)",
         narrative="From the SI meridian (shoulder joint) -> the axilla -> the heart -> the abdomen -> the "
                    "SI meridian. Specific feature: the SI divergent/primary meridian reaches BOTH the "
                    "inner and outer canthus of the eye -- unique among the meridians.",
         accent=ACCENT_INNER),
    dict(circuit="inner", meridian="Bladder (BL)", abbr="BL", pair_label="BL + KI Confluence",
         beginning="Popliteal fossa (from the Bladder meridian)",
         organs="Bladder, kidneys, spine, cardiac region",
         exiting="Neck",
         merging="Foot-Taiyang (itself -- BL is the Yang partner)",
         narrative="Deriving from the BL meridian in the popliteal fossa -> 5 cun below the sacrum -> the "
                    "anal region -> the bladder -> the kidneys -> the spine -> the cardiac region -> emerging "
                    "at the neck -> the BL meridian.",
         accent=ACCENT_INNER_WATER),
    dict(circuit="inner", meridian="Kidney (KI)", abbr="KI", pair_label="BL + KI Confluence",
         beginning="Popliteal fossa (from the Kidney meridian)",
         organs="Kidney, root of the tongue",
         exiting="Nape (merges upward with the BL divergent channel)",
         merging="Foot-Taiyang (Bladder)",
         narrative="From the KI meridian (popliteal fossa) -> upward, intersecting the Divergent "
                    "Meridian of the Bladder (thigh) -> the kidney -> crossing the Dai (Belt) Meridian "
                    "at the level of T7 -> the root of the tongue -> emerging at the nape -> the BL "
                    "meridian.",
         accent=ACCENT_INNER_WATER),
    dict(circuit="middle", meridian="Pericardium (PC)", abbr="PC", pair_label="PC + SJ Confluence",
         beginning="Chest, 3 cun below the axilla (from the Pericardium meridian)",
         organs="Sanjiao (Triple Energizer)",
         exiting="Behind the ear (via a branch)",
         merging="Hand-Shaoyang (Sanjiao)",
         narrative="From the PC meridian (3 cun below the axilla) -> the chest -> the Sanjiao. Branch: "
                    "ascending across the throat -> emerging behind the ear -> the Sanjiao meridian.",
         accent=ACCENT_MIDDLE),
    dict(circuit="middle", meridian="Sanjiao (SJ)", abbr="SJ", pair_label="PC + SJ Confluence",
         beginning="Vertex (from the Sanjiao meridian)",
         organs="Upper, middle, and lower Jiao; chest",
         exiting="Supraclavicular fossa",
         merging="Hand-Shaoyang (itself -- SJ is the Yang partner)",
         narrative="From the SJ meridian (vertex) -> the chest -> the upper, middle, and lower Jiao -> "
                    "emerging at the supraclavicular fossa -> the SJ meridian.",
         accent=ACCENT_MIDDLE),
    dict(circuit="middle", meridian="Gallbladder (GB)", abbr="GB", pair_label="GB + LR Confluence",
         beginning="Lateral thigh, hip joint, abdomen/pelvic region (from the Gallbladder meridian)",
         organs="Gallbladder, liver, heart, esophagus, eye",
         exiting="Face / outer canthus",
         merging="Foot-Shaoyang (itself -- GB is the Yang partner)",
         narrative="From the GB meridian (thigh) -> the hip joint -> the lower abdomen -> the pelvic "
                    "region -> converging with the Divergent Meridian of the Liver -> between the lower "
                    "ribs -> the gallbladder -> the liver -> upward through the heart -> esophagus -> the "
                    "face -> the eye -> the GB meridian (outer canthus).",
         accent=ACCENT_MIDDLE_WOOD, self_study=True),
    dict(circuit="middle", meridian="Liver (LR)", abbr="LR", pair_label="GB + LR Confluence",
         beginning="Instep of the foot (from the Liver meridian)",
         organs="Pubic region (converges with the GB divergent channel)",
         exiting="Pubic region",
         merging="Foot-Shaoyang (Gallbladder)",
         narrative="Deriving from the LR meridian on the instep -> the pubic region -> converging with "
                    "the Divergent Meridian of the Gallbladder.",
         accent=ACCENT_MIDDLE_WOOD, self_study=True),
]

# ---------------------------------------------------------------------------
# 12 MUSCLE / SINEW REGIONS (Jing Jin) -- slides 13, 14, 26-27, 34-35,
# 44-45, 52-53, 63-64, 71-72. Function: connect bones/joints, maintain
# normal range of motion; pathway = "same as primary meridian, but bigger."
# GB/LR were self-study slides.
# ---------------------------------------------------------------------------
SINEW_DEFINITION = (
    "The 12 Muscle (Sinew) Regions, Jing Jin, are a newer nomenclature layered on top of the primary "
    "meridians -- their pathways mainly follow the course of the corresponding primary meridian, just "
    "over a WIDER area (a region, not a line). They originate at the extremities of the limbs and "
    "ascend to the head and trunk. They do NOT go inside the body and do NOT connect with the zang-fu "
    "organs -- they connect only with muscles, tendons, and bones/joints."
)

SINEW_FUNCTIONS = [
    "Nourish the muscles; clinical significance is mainly muscular -- Bi (painful obstruction) "
    "syndrome, contracture, stiffness, spasm, and muscular atrophy.",
    "Connect all the bones and joints of the body.",
    "Maintain the normal range of motion.",
    "Run from the extremities of the limbs toward the head and trunk (never the reverse).",
]

SINEW_PATTERN_RULES = [
    "All 3 Yang Muscle Regions of the FOOT (anterior/lateral/posterior aspects of the trunk) connect with the EYES.",
    "All 3 Yin Muscle Regions of the FOOT connect with the GENITAL region.",
    "All 3 Yang Muscle Regions of the HAND connect with the ANGLE OF THE FOREHEAD.",
    "All 3 Yin Muscle Regions of the HAND connect with the THORACIC CAVITY (chest).",
]

SINEW_CLINICAL_NOTE = (
    "Clinical use (from Q&A in lecture): because a single acupoint is small, but a Muscle Region "
    "covers a whole area along the channel's course, practitioners can treat local muscle/joint pain "
    "and motor dysfunction (including conditions like osteoarthritis-related pain, per the "
    "massage-therapist student's question) by stimulating anywhere along the Muscle Region, not just "
    "the exact acupoint -- this is part of the theoretical basis for techniques like dry needling."
)

SINEW_REGIONS = [
    dict(circuit="outer", meridian="Hand-Taiyin (Lung)", abbr="LU", accent=ACCENT_OUTER,
         path="Tip of thumb -> thenar eminence -> forearm -> elbow -> arm -> chest -> Quepen (ST 12) -> "
              "Jianyu (LI 15) -> clavicle -> chest diaphragm -> lowest rib.",
         binds="Thenar eminence, elbow"),
    dict(circuit="outer", meridian="Hand-Yangming (Large Intestine)", abbr="LI", accent=ACCENT_OUTER,
         path="Index finger -> wrist -> forearm -> elbow -> arm -> Jianyu (LI 15) -> neck -> side of nose "
              "-> crosses over the head -> mandible (other side). Branch: Jianyu -> scapula -> spine.",
         binds="Dorsum of wrist, lateral elbow, shoulder, side of nose"),
    dict(circuit="outer", meridian="Foot-Yangming (Stomach)", abbr="ST", accent=ACCENT_OUTER,
         path="2nd/middle/4th toes -> leg -> knee -> hip -> lower ribs -> spine. Straight branch: tibia -> "
              "knee -> thigh -> pelvic region -> abdomen -> Quepen (ST 12) -> neck -> mouth -> nose -> eyes "
              "(joins Foot-Taiyang/BL) -> jaw -> front of ear. Fibula branch -> joins the lateral system.",
         binds="Knee, hip, Quepen ST12, eyes"),
    dict(circuit="outer", meridian="Foot-Taiyin (Spleen)", abbr="SP", accent=ACCENT_OUTER,
         path="Medial side of big toe -> medial malleolus -> knee -> thigh -> hip -> external genitalia -> "
              "abdomen -> umbilicus -> abdominal cavity -> ribs -> chest -> spine.",
         binds="Medial malleolus (SP 5), medial knee (SP 9), groin, umbilicus, ribs"),
    dict(circuit="inner", meridian="Hand-Shaoyin (Heart)", abbr="HT", accent=ACCENT_INNER,
         path="Small finger -> pisiform bone -> elbow -> chest -> breast region -> chest -> thoracic "
              "diaphragm -> umbilicus.",
         binds="Pisiform bone, medial elbow, axilla"),
    dict(circuit="inner", meridian="Hand-Taiyang (Small Intestine)", abbr="SI", accent=ACCENT_INNER,
         path="Tip of small finger -> wrist -> forearm -> medial condyle of humerus -> arm -> axilla -> "
              "scapula -> neck -> behind the ear -> enters the ear -> emerges above the auricle -> the "
              "face -> mandible/outer canthus (ST 8 area).",
         binds="Wrist, medial epicondyle, axilla, mastoid process, mandible, outer canthus/ST8 area"),
    dict(circuit="inner", meridian="Foot-Taiyang (Bladder)", abbr="BL", accent=ACCENT_INNER_WATER,
         path="Little toe -> external malleolus -> knee -> heel -> popliteal fossa -> gluteal region -> "
              "side of spine -> the nape -> root of the tongue -> occipital bone -> top of head -> nose "
              "bridge -> around the eyes. Branch: posterior axillary fold -> Jianyu (LI 15). Branch: "
              "enters the chest.",
         binds="Popliteal fossa, nape, occiput, eyes"),
    dict(circuit="inner", meridian="Foot-Shaoyin (Kidney)", abbr="KI", accent=ACCENT_INNER_WATER,
         path="Beneath the little toe -> (together with Foot-Taiyin) below the medial malleolus -> "
              "heel -> (with Foot-Taiyang) knee -> (with Foot-Taiyin) genital region -> spine -> nape -> "
              "occipital bone -> (with Foot-Taiyang).",
         binds="Below medial malleolus, knee, genital region, occiput"),
    dict(circuit="middle", meridian="Hand-Jueyin (Pericardium)", abbr="PC", accent=ACCENT_MIDDLE,
         path="Middle finger -> elbow -> axilla -> ribs -> chest -> axilla -> spreads over the chest -> "
              "thoracic diaphragm.",
         binds="Medial elbow, axilla, diaphragm"),
    dict(circuit="middle", meridian="Hand-Shaoyang (Sanjiao)", abbr="SJ", accent=ACCENT_MIDDLE,
         path="4th finger -> wrist -> forearm -> olecranon -> upper arm -> shoulder -> neck -> (joins "
              "Hand-Taiyang) -> angle of mandible -> root of the tongue -> in front of the ear -> outer "
              "canthus -> temple -> corner of the forehead.",
         binds="Dorsum of wrist, posterior elbow, corner of forehead"),
    dict(circuit="middle", meridian="Foot-Shaoyang (Gallbladder)", abbr="GB", accent=ACCENT_MIDDLE_WOOD,
         self_study=True,
         path="4th toe -> external malleolus -> tibia -> knee. Fibula -> thigh (Futu, ST 32) -> sacrum. "
              "Straight branch -> ribs -> axilla -> breast region -> Quepen (ST 12) -> behind the ear -> "
              "temple -> vertex. Branch: temple -> cheek -> outer canthus.",
         binds="Outer canthus/side of nose, SC fossa (ST12 region), sacrum, above ST32, lateral "
               "malleolus/lateral knee"),
    dict(circuit="middle", meridian="Foot-Jueyin (Liver)", abbr="LR", accent=ACCENT_MIDDLE_WOOD,
         self_study=True,
         path="Dorsum of big toe -> medial malleolus -> tibia -> knee -> thigh -> genital region -> joins "
              "other muscle regions.",
         binds="Anterior medial malleolus, medial condyle of tibia, genitals"),
]

# ---------------------------------------------------------------------------
# 12 CUTANEOUS REGIONS -- slides 80, 81. Self-study slide content (not
# reached live) -- figures are Dr. Zhang's own lecture-deck diagrams
# (slides 82/83 of the deck).
# ---------------------------------------------------------------------------
CUTANEOUS_DEFINITION = (
    "The 12 Cutaneous Regions (Pi Bu) are the parts of the 12 meridians reflected on the body surface, "
    "where the qi of the meridians is distributed -- the outermost layer of the human body. Su Wen "
    "(Chapter 56): \u201cThe Cutaneous Regions are the part of the meridian system located in the "
    "superficial layers of the body, marked by the regular meridians.\u201d"
)

CUTANEOUS_FUNCTIONS = [
    ("Protects against exogenous pathogen invasion",
     "Su Wen Ch.56: \u201cSkin is the place where the meridians are distributed. When the pathogen "
     "attacks the skin, the sweat pores open, and the pathogen may advance toward the collaterals, "
     "meridians, and zang-fu organs through the sweat pore.\u201d Transmission order: Skin -> Collaterals "
     "-> Meridians -> Fu organs -> Zang organs."),
    ("Projects symptoms/signs of internal disease onto the surface",
     "Su Wen Ch.56: blue-colored skin signals local pain; dark-colored skin indicates blocked qi and "
     "blood; yellow-to-red skin signals heat syndromes; white skin signals cold syndromes."),
    ("Diagnostically and therapeutically interactive",
     "Because the cutaneous region is the most superficial layer, it is both the first line read for "
     "diagnosis (skin color/texture change) and the first line treated (very superficial needling, "
     "e.g. intradermal/press needles, work through this layer)."),
]

CUTANEOUS_DIVISIONS = [
    dict(group="3 Yang (posterior/lateral view)", figure="CUTANEOUS_YANG",
         members=["Taiyang (BL/SI territory)", "Shaoyang (GB/SJ territory)", "Yangming (ST/LI territory)"]),
    dict(group="3 Yin (anterior view)", figure="CUTANEOUS_YIN",
         members=["Taiyin (LU/SP territory)", "Shaoyin (HT/KI territory)", "Jueyin (PC/LR territory)"]),
]

# ---------------------------------------------------------------------------
# WEEK 7 REVIEW RECAP -- used as PLA "Activate/Connect" bridge material.
# Confluent points table from slide 78 (image CONFLUENT_REVIEW), plus the
# 5 review Q&A pairs Dr. Zhang ran live at the start of Lecture 8.
# ---------------------------------------------------------------------------
WEEK7_REVIEW_QA = [
    ("Which vessel is called the \u201cBelt\u201d because it runs around the waist?", "Dai Mai (Belt Vessel)"),
    ("True or false: Dai Mai is the only vessel that runs horizontally.", "True"),
    ("Which two vessels have a confluent point that is the SAME as their starting point?",
     "Yin Qiao Mai (KI 6 Zhaohai) and Yang Qiao Mai / \u2014 Dr. Zhang: \u201cYin Qiao and Yang Qiao,\u201d "
     "both begin AND open at their confluent point."),
    ("Which three vessels share the lower abdomen as a common origin (\u201cyi yuan san qi\u201d)?",
     "Du Mai (GV), Ren Mai (CV), and Chong Mai"),
    ("True or false: the Du Meridian connects with the Bladder (zang-fu connection).",
     "False -- NONE of the 8 Extraordinary Vessels connect to a zang or fu organ; the vessels have no "
     "interior-exterior organ pairing the way primary meridians do."),
    ("Which channel is called the \u201cSea of All Yin Meridians\u201d?", "Ren Mai (Conception Vessel)"),
    ("Which channel is called the \u201cSea of All Yang Meridians\u201d?", "Du Mai (Governor Vessel)"),
]

WEEK7_REVIEW_DISCUSSION = [
    ("Do all four Foot-Yang meridians intersect with GV 14 (Dazhui)?",
     "No -- ALL Yang meridians intersect GV14 EXCEPT the Stomach meridian. ST runs head->foot "
     "along the FRONT of the body and has no branch that reaches back to the spine; the other Yang "
     "meridians either run the lateral/network side or the inner/deep side and so have a branch that "
     "reaches GV14."),
    ("Which meridians pass through the supraclavicular fossa?",
     "All meridians EXCEPT the Foot-Taiyang (Bladder) meridian, since BL runs along the back of the "
     "body and never comes to the front to reach the fossa. The fossa is a major convergence point "
     "for stimulating Yang qi -- useful for tension, depression, and emotional-regulation work."),
    ("Which meridians pass through/near the eyes?",
     "All 3 Foot-Yang meridians (ST, GB, BL -- because Foot-Yang runs head->foot and starts near the "
     "eye) and 2 Hand-Yang meridians (SI reaches BOTH inner and outer canthus because it is the "
     "Zhao-Yang \u2018network-side\u2019 meridian; SJ reaches only the outer canthus because it runs the "
     "lateral head). LI does NOT connect to the eye (its job is digestion, ending at the nose). Two "
     "Yin meridians ALSO reach the eye by special branch: HT (\u201cthe eye is the window of the heart\u201d) "
     "and LR (\u201cthe liver governs blood, and blood nourishes the eye\u201d)."),
]

DIVERGENT_PAIR_NOTES = {
    "LU + LI": "Clinical relevance: because the LU divergent channel passes anterior to the Pericardium "
               "meridian on its way to the lung, and the LI divergent channel reaches all the way back "
               "to the spine, this pair explains why LU/LI points can reach both chest (PC-adjacent) and "
               "upper-back complaints, not just their own organ's territory.",
    "ST + SP": "Clinical relevance: the ST divergent channel is the only one of the 12 that runs THROUGH "
               "the heart on its way to the mouth/eye -- this is the anatomical basis for using ST points "
               "in some heart-adjacent chest patterns, in addition to their expected digestive use.",
    "HT + SI": "Clinical relevance: both divergent channels begin at the SAME landmark (axillary fossa / "
               "shoulder joint area) and both pass through the heart -- reinforcing why HT and SI points "
               "are so often combined for chest/cardiac-adjacent and mouth-area symptom patterns.",
    "BL + KI": "Clinical relevance: the KI divergent channel is the only one that crosses the Dai (Belt) "
               "Meridian along its course (at the level of T7) -- a rare direct link between a primary "
               "meridian's divergent channel and an Extraordinary Vessel.",
    "PC + SJ": "Clinical relevance: both divergent channels are unusually short (chest-to-Sanjiao and "
               "vertex-to-chest) compared to the limb-spanning divergent channels of most other pairs -- "
               "consistent with PC/SJ's role as the Ministerial Fire pair governing the Triple Jiao itself.",
    "GB + LR": "Clinical relevance: the GB divergent channel is the only one that explicitly passes "
               "through BOTH paired organs (gallbladder AND liver) on a single course -- self-study "
               "content; confirm this reading with Dr. Zhang's review before treating as final.",
}

VOCAB = [
    ("Luo Mai", "Collateral / connecting vessel", "The 15 Luo-Connecting points as a system"),
    ("Jing Bie", "Divergent Meridian", "Runs deep, no points, no organ"),
    ("Jing Jin", "Muscle / Sinew Region", "Wide band, muscles/joints only"),
    ("Pi Bu", "Cutaneous Region", "Outermost layer, skin surface"),
    ("Li", "Beginning (of a divergent channel)", "First of the 4-part framework"),
    ("He", "Organs/systems involved", "2nd of the 4-part framework"),
    ("Chu", "Exiting (to the surface)", "3rd of the 4-part framework"),
    ("Dabao", "SP 21, the Great Luo of the Spleen", "Covers the lateral chest"),
    ("Bi Syndrome", "Painful obstruction syndrome", "Key Muscle Region pathology"),
    ("Yi Yuan San Qi", "\u201cOne source, three branches\u201d", "Du/Ren/Chong (Week 7 recap term)"),
]

LEARNING_TARGETS = [
    "I can state why there are 15 Collaterals rather than 12, using the front/back/side logic.",
    "I can name all 12 paired-meridian Luo-Connecting points and their locations (wrist vs. ankle rule).",
    "I can name the 3 \u201cextra\u201d collaterals (CV, GV, Spleen Great Luo) and explain what each covers.",
    "I can describe the Li-He-Chu-merge framework and apply it to any of the 12 Divergent Channels.",
    "I can explain why Divergent Channels have no points and no pertaining organ, unlike primary meridians.",
    "I can state the 4 structural pattern rules for the 12 Muscle Regions (Yang/Yin, Hand/Foot).",
    "I can describe the function of the Cutaneous Regions and the Su Wen disease-transmission order.",
    "I can identify at least 2 acupoints that carry both a Luo-Connecting AND a Confluent-point identity.",
]

ANTICIPATORY_QUESTIONS = [
    ("Structural", True, "Why does the Spleen (not another organ) get the Great/Major Collateral that covers the lateral chest?"),
    ("Structural", False, "How many total collaterals are there, and how is that number built from 12 + 2 + 1?"),
    ("Structural", True, "What is the ONE thing all 12 Divergent Channels lack that every primary meridian has?"),
    ("Structural", False, "What does the \u201cChu\u201d step of the Li-He-Chu-merge framework refer to?"),
    ("Clinical", True, "Why can Stomach-channel points sometimes address heart-adjacent chest symptoms?"),
    ("Clinical", False, "What clinical pattern do Muscle Regions treat that neither the primary meridian nor its Luo point directly addresses?"),
    ("Clinical", True, "Why might LU7 (Lieque) be chosen over another Lung-meridian point for a combined cough + irregular-menstruation presentation?"),
    ("Comparison", False, "How do Collaterals and Divergent Channels differ in depth, points, and function?"),
    ("Comparison", True, "How do the 4 Yang Muscle Region pattern-rule groups differ from the Yin groups (what do they each connect to)?"),
    ("Comparison", False, "Where do the 3 Yin Cutaneous Regions sit relative to the 3 Yang Cutaneous Regions (anterior vs. posterior)?"),
]

IQ_CHECKPOINTS = [
    ("Items 1-4: 15 Collaterals", [
        (1, "ACQ", "Name the Luo point of the Stomach meridian and what it connects to."),
        (2, "ACQ", "Name the Luo point of the Kidney meridian and what it connects to."),
        (3, "MAINT", "What is the confluent point of Chong Mai, and is it also a Luo point?"),
        (4, "ACQ", "Which collateral covers the lateral side of the chest, and from what point?"),
    ]),
    ("Items 5-8: Divergent Channels", [
        (5, "ACQ", "What does the Kidney Divergent Channel cross that no other divergent channel does?"),
        (6, "ACQ", "Which Divergent Channel passes through the heart on its way to the mouth and eye?"),
        (7, "MAINT", "What is the pertaining organ of the Pericardium, and its connecting organ?"),
        (8, "ACQ", "What do all 6 Yin Divergent Channels eventually do?"),
    ]),
    ("Items 9-12: Muscle & Cutaneous Regions", [
        (9, "ACQ", "What do all 3 Yang Muscle Regions of the Foot connect with?"),
        (10, "ACQ", "What do all 3 Yin Muscle Regions of the Hand connect with?"),
        (11, "ACQ", "State the Su Wen disease-transmission order from skin to organ."),
        (12, "MAINT", "Which vessel is the Sea of All Yang Meridians (Week 7 recap)?"),
    ]),
]

IQ_ANSWERS = [
    "ST 40 Fenglong -- connects to the Spleen meridian.",
    "KI 4 Dazhong -- connects to the Bladder meridian.",
    "SP 4 Gongsun is the confluent point of Chong Mai, and yes -- it is also the Luo-Connecting point of the Spleen meridian.",
    "The Great (Major) Collateral of the Spleen, from Dabao (SP 21).",
    "It crosses the Dai (Belt) Meridian, at the level of T7.",
    "The Stomach Divergent Channel.",
    "Pertaining organ: Pericardium. Connecting organ: Sanjiao (Triple Energizer) -- an interior-exterior pair.",
    "They merge into their paired Yang primary meridian -- none resurfaces as a separate Yin pathway.",
    "The eyes.",
    "The thoracic cavity (chest).",
    "Skin -> Collaterals -> Meridians -> Fu organs -> Zang organs.",
    "Du Mai (Governor Vessel).",
]

CLINICAL_CASE = (
    "Ms. Alvarez, 38, presents with several weeks of intermittent right-sided lateral hip and outer-knee "
    "pain that worsens with prolonged standing, plus mild stiffness first thing in the morning. She "
    "denies any digestive, urinary, or gynecological complaints, and her only other note is that she "
    "\u201cnever really feels it in one exact spot\u201d -- the discomfort seems to move along a band down the "
    "side of her leg rather than sitting at a single point."
)

CLINICAL_CASE_PRE_Q = (
    "Given that her pain follows a BAND rather than a single point, and there's no organ-level "
    "complaint, which of this week's 4 systems (Collaterals, Divergent Channels, Muscle Regions, "
    "Cutaneous Regions) best fits this presentation, and why?"
)

CLINICAL_CASE_POST_Q = (
    "Now that you've studied the Muscle Regions in depth: which specific Muscle Region (by meridian) "
    "best matches a lateral hip-to-knee band, and what binding points would you expect to be tender?"
)

FINAL_EXAM_SUMMARY = (
    "Dr. Zhang's own \u201cNext Quiz\u201d summary slide (verbatim, slide 84): \u201cThe exam focuses on the "
    "pathways, connections, and special features of the meridians. You should know which organs each "
    "meridian is associated with, their starting and ending points, and key landmarks they pass -- "
    "such as the ear, external genitalia, pubic region, and waist. Pay attention to the unique traits "
    "of certain meridians like the Dai Vessel encircling the waist, the Governor Vessel starting from "
    "the perineum, and the Gallbladder Meridian's zig-zag path along the head. Also review paired "
    "relationships between meridians, the composition of the fifteen collaterals, and how channels "
    "connect with each other.\u201d Keyword list from the same slide: KI, Pericardium, LR, GB, TE (SJ), "
    "Belt Vessel, GV, 15 Collaterals, GB."
)
