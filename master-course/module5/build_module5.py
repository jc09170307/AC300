import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common_module5 import (DocBuilder, module_cover, section_header, sub_header,
                             paragraph, bullet_list, numbered_list, table, table_start_height,
                             dance_sidebar, flag_box, embed_figure_pair, figure_caption,
                             NAVY, RED, GOLD_DARK, DARK)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
OUT = f"/home/claude/module5/out/AC300_Module5_BL_KI_{EDITION}.pdf"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
FIG = os.path.join(os.path.dirname(__file__), "figures")

db = DocBuilder(OUT, "Module 5: Bladder & Kidney", "Module 5 \u2014 Bladder & Kidney")

module_cover(
    db,
    title="Bladder & Kidney",
    subtitle="The Posterior Circuit Closes \u2014 The Largest Channel of the Body",
    points_line="Fourth channel pair of the 12 Primary Meridians \u2014 67 and 27 points",
    covers_bullets=[
        "The Bladder Meridian of Foot-Taiyang (BL) \u2014 5 branches, 67 points, the largest so far",
        "The Kidney Meridian of Foot-Shaoyin (KI) \u2014 3 branches, 27 points",
        "How BL and KI close the Posterior Circuit and hand off to Pericardium (PC)",
        "Clinical context from the transcript: Back-Shu points, heel pain, SP6",
        "Ballroom & DanceSport relevance",
    ],
    info_lines=[
        "Sourced from the 2026 Lecture 5 deck (Dr. Zhang, 44 slides) and the Week 5 class transcript.",
        "Like Module 4, this draws on the newer 2026-series deck rather than an older Week_N deck,",
        "per the project's established source hierarchy.",
    ],
    module_num="5",
)

# ---------------------------------------------------------------------------
db.new_page()
section_header(db, "How to Use This Module")
paragraph(db, "BL and KI are the seventh and eighth of the 12 primary meridians, closing the Posterior "
              "Circuit (Module 1, Section 6: HT to SI to BL to KI) before Qi hands off into the Middle "
              "Circuit at the Pericardium Meridian. BL is the largest channel in the entire course \u2014 "
              "67 points across 5 branches \u2014 so this module leans on the branch structure even "
              "harder than Module 3 did for the Stomach Meridian.")

section_header(db, "1. The Bladder Meridian of Foot-Taiyang (BL)")
paragraph(db, "Meridian Clock: 3:00\u20135:00 p.m. Part of the Posterior Circuit, paired as Fu with the "
              "Kidney (Zang). The transcript is direct about why this channel is so large: it connects "
              "internally with more organs than any other \u2014 lung, liver, heart, and the kidney "
              "itself \u2014 via the Back-Shu points that run down its third branch, one point per organ. "
              "Back-Shu points themselves are deferred to the future Special Points module, but the "
              "concept \u2014 that this channel's back-line points are organ-specific access points "
              "\u2014 is worth knowing now.")
sub_header(db, "Running Course \u2014 Five Branches")
numbered_list(db, [
    "Facial/vertex branch: from the inner canthus (Jingming, BL1), ascends the forehead, joins the "
    "Governor Vessel at the vertex (Baihui, GV20).",
    "The temple branch: from the vertex, runs around the temple through 6 named crossing points "
    "(GB7\u2013GB12).",
    "The straight portion: from the vertex, enters and bifurcates around the brain, descends the "
    "posterior neck, runs parallel to the spine down the medial scapular region (1.5 cun lateral to "
    "the spine) through the lumbar region, then goes internally to connect with the kidney and pertain "
    "to the bladder.",
    "The first back branch: from the lumbar region, descends through the gluteal region to the "
    "popliteal fossa.",
    "The second (largest) back branch: from the posterior neck, runs the lateral pathway (3 cun from "
    "the spine, through the medial border of the scapula), down through the gluteal region, thigh, and "
    "into the popliteal fossa \u2014 meeting the first back branch there \u2014 then continues down the "
    "calf, behind the external malleolus, along the 5th metatarsal, ending at the lateral tip of the "
    "little toe (Zhiyin, BL67), linking with the Kidney Meridian.",
])
flag_box(db, "The two back branches run parallel to the spine at two fixed distances, both given "
             "directly in the lecture: the medial pathway is 1.5 cun from the spine (Back-Shu points, "
             "BL11\u2013BL30), and the lateral pathway is 3 cun from the spine (BL41\u2013BL54). The "
             "transcript adds a hand-measurement trick for the 1.5 cun distance: held together, the "
             "four fingers span roughly 3 cun, so half that width \u2014 two fingers \u2014 approximates "
             "1.5 cun.")

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Jingming (BL1)", "\u2014"],
    ["Last point", "Zhiyin (BL67)", "Jing-Well Point"],
], col_widths=[90, 180, 276], font_size=8.5)

flag_box(db, "Safety note from the transcript, not the slides: Dr. Zhang explicitly advises against "
             "needling the points immediately around the eye (BL1 and neighbors) early in training, "
             "given how close they sit to the orbit \u2014 stated directly as a caution, not a general "
             "point property.")

sub_header(db, "Crossing Points (14 points)",
           keep_with=140)
paragraph(db, "The transcript confirms this directly: \u201cit has 14 crossing points, belonging to two "
              "meridians \u2014 one is the Governor meridian, the other is the Gallbladder meridian.\u201d "
              "The full list, with locations where the source gives them:")
_bl_headers = ["Point", "Location"]
_bl_rows = [
    ["Taodao (GV13)", "Below the T1 spinous process"],
    ["Dazhui (GV14)", "Below the C7 spinous process, roughly level with the shoulders"],
    ["Fengfu (GV16)", "1 cun above the midpoint of the posterior hairline"],
    ["Naohu (GV17)", "2.5 cun above the midpoint of the posterior hairline"],
    ["Baihui (GV20)", "Midline of the head, 5 cun above the anterior hairline"],
    ["Shenting (GV24)", "0.5 cun above the midpoint of the anterior hairline"],
    ["Qubin (GB7)", "On the head, where the temple's posterior border crosses the ear-apex line"],
    ["Shuaigu (GB8)", "Above the ear apex, 1.5 cun within the hairline"],
    ["Tianchong (GB9)", "Above the posterior ear border, 2 cun within the hairline"],
    ["Fubai (GB10)", "Posterior/superior to the mastoid process"],
    ["Touqiaoyin (GB11)", "Posterior/superior to the mastoid process, below Fubai"],
    ["Wangu (GB12)", "Posterior/inferior to the mastoid process"],
    ["Toulinqi (GB15)", "Above the pupil, 0.5 cun above the anterior hairline"],
    ["Huantiao (GB30)", "Between the greater trochanter and the sacral hiatus"],
]
table(db, _bl_headers, _bl_rows, col_widths=[135, 411], font_size=8.0)

# ---------------------------------------------------------------------------
embed_figure_pair(db, f"{FIG}/moa_bl.jpg", "MOA \u2014 Internal Course",
                   f"{FIG}/cam_bl.jpg", "CAM \u2014 External Points",
                   "Left: internal course and crossing points (MOA). Right: all 67 external points, "
                   "Jingming (BL1) to Zhiyin (BL67) (CAM).", max_h=290)

sub_header(db, "Summary of the Bladder Meridian")
bullet_list(db, [
    "Pertaining organ: Bladder. Connecting organ: Kidney.",
    "Running course: head to foot. The largest channel in the course \u2014 67 points across 5 "
    "branches.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Alternating chills and fever, headache, stiff neck.",
    "Pain in the lumbar region, nasal congestion, diseases of the eye.",
    "Pain along the back of the leg and foot.",
])
sub_header(db, "B. Internal organ (Bladder) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Pain in the lower abdomen.",
    "Retention of urine; painful urination.",
])

# ---------------------------------------------------------------------------
dance_sidebar(db, "the entire posterior chain, named as a single channel",
    "BL is the clearest single-channel argument for why 'posterior chain' matters as a trained concept "
    "in dance, not just a gym phrase: one continuous meridian runs the full erector/hamstring/calf line "
    "from the eye to the little toe. The two fixed back-branch distances (1.5 and 3 cun from the spine) "
    "roughly bracket the paraspinal and erector muscle groups that fail first when frame collapses "
    "under fatigue \u2014 already flagged in Module 1's Posterior Circuit sidebar, now with the specific "
    "channel and its actual point-line behind that claim.")

section_header(db, "2. The Kidney Meridian of Foot-Shaoyin (KI)")
paragraph(db, "Meridian Clock: 5:00\u20137:00 p.m. Part of the Posterior Circuit, paired as Zang with "
              "the Bladder (Fu). Closes the Posterior Circuit, handing off to the Pericardium Meridian "
              "\u2014 the first channel of the Middle Circuit.")
sub_header(db, "Running Course \u2014 Main Course Plus Two Branches")
numbered_list(db, [
    "Main course: starts beneath the small toe, crosses the sole (Yongquan, KI1), emerges below the "
    "navicular tuberosity (KI2), runs behind the medial malleolus (KI3), the heel (KI4\u2013KI6), the "
    "medial leg (KI7\u2013KI9, crossing Sanyinjiao SP6), the popliteal fossa (KI10), the thigh, and the "
    "vertebral column (meeting Changqiang, GV1) \u2014 then internally pertains to the kidney and "
    "connects with the bladder.",
    "The straight portion: re-emerges from the kidney, ascends through the liver and diaphragm, enters "
    "the lung, runs the throat, and ends at the root of the tongue. The transcript notes the Spleen "
    "Meridian also connects to the tongue root (Module 3) \u2014 tongue diagnosis distinguishes Spleen "
    "function at the lower/front surface from Kidney function at the root specifically.",
    "The branch: from the lung, connects with the heart and flows into the chest, linking with the "
    "Pericardium Meridian of Hand-Jueyin \u2014 the Middle Circuit's first channel.",
])
flag_box(db, "Clinical pearl from the transcript, not the slides: heel pain is specifically named as a "
             "first-line indicator to consider Kidney function, since the main course runs directly "
             "behind the heel. Also noted: KI1 (Yongquan) is described as commonly pressed/massaged "
             "rather than needled, given how painful direct needle stimulation is at that location.")

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Yongquan (KI1)", "Jing-Well Point"],
    ["Last point", "Shufu (KI27)", "\u2014"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Crossing Points",
           keep_with=70)
table(db, ["Point", "Location"], [
    ["Zhongji (CV3)", "Anterior midline, 4 cun below the umbilicus"],
    ["Guanyuan (CV4)", "Anterior midline, 3 cun below the umbilicus"],
    ["Changqiang (GV1)", "Midway between the coccyx tip and the anus"],
    ["Sanyinjiao (SP6)", "3 cun above the tip of the medial malleolus"],
], col_widths=[135, 411], font_size=8.2)
flag_box(db, "Sanyinjiao (SP6) gets specific clinical emphasis in the transcript beyond its role as a "
             "crossing point: described as a primary point for reproductive/gynecological complaints "
             "and menstrual pain, matching its name (\u201cthree Yin meridians meeting\u201d \u2014 Spleen, "
             "Liver, and Kidney all cross here). Worth remembering for the capstone, given the female "
             "athlete population in DanceSport.")

embed_figure_pair(db, f"{FIG}/moa_ki.jpg", "MOA \u2014 Internal Course",
                   f"{FIG}/cam_ki.jpg", "CAM \u2014 External Points",
                   "Left: internal course showing the Kidney/Liver/Lung/Heart/Pericardium connections "
                   "(MOA). Right: the 27 external points, Yongquan (KI1) to Shufu (KI27) (CAM).", max_h=250)

# ---------------------------------------------------------------------------
sub_header(db, "Summary of the Kidney Meridian")
bullet_list(db, [
    "Pertaining organ: Kidney. Connecting organ: Bladder.",
    "Running course: foot to chest, linking with the Pericardium Meridian of Hand-Jueyin.",
    "Total points: 27.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Pain along the lower vertebrae; coldness in the feet.",
    "Motor impairment or muscular atrophy of the foot.",
    "Dryness in the mouth, sore throat.",
    "Pain in the sole of the foot or along the posterior lower leg/thigh.",
])
sub_header(db, "B. Internal organ (Kidney) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Ashen complexion, blurred vision, shortness of breath.",
    "Frequent urination, incomplete voiding.",
    "Chronic diarrhea or constipation, abdominal distention, insomnia.",
])
dance_sidebar(db, "endurance reserve and the fatigue that isn't muscular",
    "KI's internal symptom list \u2014 shortness of breath, insomnia, an ashen look \u2014 reads as "
    "genuine overtraining/under-recovery territory, distinct from BL's more mechanical "
    "posterior-chain-under-load picture. Worth holding the two channels as separate diagnostic "
    "directions for the same complaint (\u2018I'm exhausted\u2019): BL points toward mechanical/postural "
    "fatigue, KI toward deeper reserve depletion. SP6 (Section 2) is also worth flagging here for "
    "female competitive dancers specifically, given the transcript's emphasis on its reproductive/"
    "menstrual applications.")

# ---------------------------------------------------------------------------
section_header(db, "3. Closing the Posterior Circuit")
paragraph(db, "HT to SI to BL to KI is now complete \u2014 the full Posterior Circuit from Module 1, "
              "Section 6. KI's third branch (lung to heart to Pericardium) is the actual handoff into "
              "the Middle Circuit, the next channel being the Pericardium Meridian of Hand-Jueyin, "
              "covered in Module 6.")

section_header(db, "4. Ballroom & DanceSport Relevance \u2014 Summary")
paragraph(db, "Original synthesis, not lecture content \u2014 flagged as such throughout, consistent "
              "with Modules 1\u20134.")
bullet_list(db, [
    "BL and KI complete the Posterior Circuit's dance-relevant territory: BL as the mechanical "
    "posterior-chain line, KI as the deeper endurance/recovery signal.",
    "Between the eight channels covered so far (the full Anterior and Posterior Circuits), a genuine "
    "pattern is forming: each channel pair distinguishes a mechanical/structural complaint from a "
    "systemic/organ-level one along the same body line. This structure itself may be worth proposing "
    "directly for the capstone's injury-framework organization once the Middle Circuit is complete.",
])

section_header(db, "5. Still Open / Not Yet Sourced")
bullet_list(db, [
    "Back-Shu points \u2014 named and located conceptually (Section 1) but not detailed point-by-point; "
    "still deferred to the future Special Points module alongside Yuan-Source, Luo-Connecting, "
    "Xi-Cleft, and Eight Confluent Points.",
    "Finger measurement's specific cun ratios \u2014 still unconfirmed, carried over from Module 2.",
    "The exact abdominal/chest channel spacing relative to the midline \u2014 still unconfirmed, "
    "carried over from Module 3.",
])

section_header(db, "Source Notes")
paragraph(db, "Primary source: 2026Lecture_5Vivian.pdf (44 slides, Dr. Zhang, Lecture 5) and "
              "AC300Week5BLKD.txt (class transcript). MOA and CAM figures are the same reference "
              "figures used across the weekly study kits. Section 4 is flagged separately as original "
              "synthesis. The transcript also includes clinical/research color from Dr. Zhang's own "
              "practice specialty (reproductive acupuncture) \u2014 omitted here as outside this "
              "module's channel-theory scope, except where it bears directly on a point's clinical "
              "application (SP6).")

db.end_page()
db.save()
