import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common_module2 import (DocBuilder, module_cover, section_header, sub_header,
                             paragraph, bullet_list, numbered_list, table, table_start_height,
                             dance_sidebar, flag_box, embed_figure_pair, figure_caption,
                             NAVY, RED, GOLD_DARK, DARK)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
OUT = f"/home/claude/module2/out/AC300_Module2_LU_LI_{EDITION}.pdf"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
FIG = os.path.join(os.path.dirname(__file__), "figures")

db = DocBuilder(OUT, "Module 2: Lung & Large Intestine", "Module 2 \u2014 Lung & Large Intestine")

module_cover(
    db,
    title="Lung & Large Intestine",
    subtitle="The Anterior Circuit Begins \u2014 Plus: Cun Measurement",
    points_line="First channel pair of the 12 Primary Meridians, hand-to-hand",
    covers_bullets=[
        "Cun measurement \u2014 how points are actually located on the body",
        "The Lung Meridian of Hand-Taiyin (LU) \u2014 course, points, syndromes",
        "The Large Intestine Meridian of Hand-Yangming (LI) \u2014 course, points, syndromes",
        "The Zang-Fu (interior-exterior) relationship between LU and LI",
        "Ballroom & DanceSport relevance",
    ],
    info_lines=[
        "Sourced from the Week 2 lecture deck (Dr. Zhang, 33 slides) \u2014 no class transcript was",
        "available for Week 2, so this module relies on the slides alone.",
        "Cun measurement is sourced separately from the CAM reference text (cited below), since it",
        "does not appear in Dr. Zhang's slides.",
    ],
    module_num="2",
)

# ---------------------------------------------------------------------------
db.new_page()
section_header(db, "How to Use This Module")
paragraph(db, "This module assumes Module 1 (Foundations) is already familiar \u2014 the Anterior/"
              "Posterior/Middle Circuits, the Yin/Yang nomenclature, and the medial/lateral "
              "distribution rules are used here without re-explanation. This is the first of the 12 "
              "primary meridians covered channel-by-channel, and it also introduces cun measurement, "
              "flagged as pending back in Module 1.")

section_header(db, "New Terms This Module")
_new_terms = [
    ("Cun", "A proportional, not fixed, unit of measurement for locating acupuncture points \u2014 defined relative to the patient's own body landmarks, not a fixed inch or centimeter value."),
    ("Meridian Clock", "The traditional 24-hour cycle assigning each of the 12 primary meridians a 2-hour window of peak Qi flow. LU: 3\u20135 a.m. LI: 5\u20137 a.m."),
    ("Front-Mu Point", "A point on the torso where the Qi of a Zang or Fu organ is said to gather \u2014 used diagnostically and therapeutically for that organ. LU1 is the Lung's Front-Mu point."),
    ("Jing-Well Point", "The most distal of the Five Shu points on each channel, located at the fingertip or toenail corner \u2014 where channel Qi is said to 'bubble up.' Both LU and LI start/end runs at Jing-Well points (LU11, LI1)."),
    ("Crossing Point", "A point where two or more different channels physically intersect. The Large Intestine Meridian has 4 named crossing points with other channels (Du14, Du26, ST4, SI12)."),
]
table(db, ["Term", "Definition"], _new_terms, col_widths=[130, 416], font_size=8.2, leading=10.8)

# ---------------------------------------------------------------------------
section_header(db, "1. Cun Measurement \u2014 Locating Points on the Body")
paragraph(db, "This section is sourced from a CAM reference text (\u201cAn Introduction to Acupuncture "
              "Points,\u201d p.127\u2013129, and \u201cChinese Acupuncture and Moxibustion,\u201d Table 7) \u2014 "
              "not from Dr. Zhang's Week 2 slides, which move directly into the Lung Meridian without "
              "covering point-location methodology.")
paragraph(db, "The source text names four methods used in clinic today: proportional measurement, "
              "anatomical landmarks, finger measurement, and practical simple methods. Cun is the unit "
              "proportional measurement is built on \u2014 it scales to each patient's own body rather "
              "than a fixed length.")
sub_header(db, "Anatomical Landmarks")
bullet_list(db, [
    "Fixed landmarks: don't change with body movement \u2014 the five sense organs, hair line, nails, nipples, umbilicus, and bone prominences/depressions. Points adjacent to or on these can be located directly (e.g., Yintang between the eyebrows, Shenque at the center of the umbilicus).",
    "Moving landmarks: only appear when a body part holds a specific position \u2014 e.g., Quchi (LI11) appears at the cubital crease only when the arm is flexed; Houxi (SI3) appears at the transverse palmar crease only when a fist is made.",
])
_cun_headers = ["Body Region", "Landmarks", "Cun", "Method"]
_cun_rows = [
    ["Upper Extremities", "Axillary fold to transverse cubital crease", "9 cun", "Longitudinal"],
    ["Upper Extremities", "Transverse cubital crease to transverse wrist crease", "12 cun", "Longitudinal"],
    ["Lower Extremities", "Upper border of pubic symphysis to medial epicondyle of femur", "18 cun", "Longitudinal"],
    ["Lower Extremities", "Medial condyle of tibia to tip of medial malleolus", "13 cun", "Longitudinal"],
    ["Lower Extremities", "Greater trochanter to popliteal crease (via lateral thigh)", "19 cun", "Longitudinal"],
    ["Lower Extremities", "Popliteal crease to tip of lateral malleolus", "16 cun", "Longitudinal"],
    ["Head/Face", "Anterior hairline to posterior hairline", "12 cun", "Longitudinal"],
    ["Head/Face", "Glabella to anterior hairline", "3 cun", "Longitudinal"],
    ["Head/Face", "Between the two mastoid processes", "9 cun", "Transverse"],
    ["Chest/Abdomen", "Suprasternal fossa to sternocostal angle", "9 cun", "Longitudinal"],
    ["Chest/Abdomen", "Sternocostal angle to center of umbilicus", "8 cun", "Longitudinal"],
    ["Chest/Abdomen", "Center of umbilicus to upper border of pubic symphysis", "5 cun", "Longitudinal"],
    ["Chest/Abdomen", "Between the two nipples", "8 cun", "Transverse"],
    ["Back", "Between medial border of scapula and posterior midline", "3 cun", "Transverse"],
]
sub_header(db, "Proportional (Bone) Measurement \u2014 the standard reference table",
           keep_with=table_start_height(_cun_headers, _cun_rows, [100, 280, 55, 111], font_size=7.8, leading=10) + 32)
paragraph(db, "The distance between two fixed bony landmarks is divided into a set number of equal "
              "cun, regardless of the patient's actual height \u2014 that division is what makes the "
              "unit proportional rather than fixed.")
table(db, _cun_headers, _cun_rows, col_widths=[100, 280, 55, 111], font_size=7.8, leading=10)
flag_box(db, "Finger measurement (the fourth named method \u2014 using the patient's own finger widths "
             "as a quick field estimate) is named in the source but its specific ratios are not shown "
             "on the pages available here. Flagged as pending rather than filled in from general "
             "knowledge \u2014 will confirm against source before stating specific finger-cun values.")

# ---------------------------------------------------------------------------
section_header(db, "2. The Lung Meridian of Hand-Taiyin (LU)")
paragraph(db, "Meridian Clock: 3:00\u20135:00 a.m. Part of the Anterior Circuit, paired as Zang with the "
              "Large Intestine (Fu). The first of the 12 primary meridians in the standard teaching "
              "order.")
sub_header(db, "Internal Running Course")
paragraph(db, "Originates in the Middle Jiao, descends to connect with the large intestine, turns back "
              "to pass through the upper orifice of the stomach, passes through the diaphragm, and "
              "enters its pertaining organ, the lung.")
sub_header(db, "External Running Course",
           keep_with=90)
numbered_list(db, [
    "Emerges from the lung system and surfaces at Zhongfu (LU1) and Yunmen (LU2).",
    "Descends the anterior-medial upper arm (LU3 Tianfu, LU4 Xiabai).",
    "Crosses the cubital fossa at Chize (LU5).",
    "Continues down the anterior-medial forearm (LU6 Kongzui).",
    "Reaches the wrist (cunkou) at Lieque (LU7), Jingqu (LU8), Taiyuan (LU9).",
    "Crosses the thenar eminence at Yuji (LU10).",
    "Ends at the radial side of the thumb, Shaoshang (LU11).",
])
sub_header(db, "The Branch")
paragraph(db, "From LU7 (Lieque), a branch separates and runs to the radial side of the tip of the "
              "index finger, Shangyang (LI1) \u2014 connecting to the Large Intestine Meridian of "
              "Hand-Yangming and handing off the circuit.")

embed_figure_pair(db, f"{FIG}/moa_lu.jpg", "MOA \u2014 Internal Course",
                   f"{FIG}/cam_lu.jpg", "CAM \u2014 External Points",
                   "Left: internal course showing the Lung/Large Intestine visceral connection (MOA). "
                   "Right: the 11 external points, Zhongfu (LU1) to Shaoshang (LU11) (CAM).", max_h=260)

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Zhongfu (LU1)", "Front-Mu Point of the Lung"],
    ["Last point", "Shaoshang (LU11)", "Jing-Well Point"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Summary of the Lung Meridian",
           keep_with=90)
bullet_list(db, [
    "Pertaining organ: Lung. Connecting organ: Large Intestine.",
    "Running course: chest to hand, along the anterior-medial arm.",
    "Total points: 11.",
    "The branch: LU7 to the radial side of the index finger, connecting to the Large Intestine Meridian.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Fever and sensitivity to cold.",
    "Nasal congestion, headache.",
    "Pain in the chest, clavicle, shoulder, and back.",
    "Chills and pain along the channel on the arm.",
])
sub_header(db, "B. Internal organ (Lung) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Coughing, asthma.",
    "Shortness of breath.",
    "Fullness in the chest.",
    "Dry throat.",
])
dance_sidebar(db, "breath capacity and posture",
    "The Lung Meridian's internal syndromes (shortness of breath, chest fullness) sit directly on top "
    "of the two things a dancer's endurance and frame both depend on: breath capacity and thoracic "
    "posture. American Smooth's extended frame and sustained core engagement both compress and expand "
    "the same chest/rib-cage territory this channel's internal branch runs through. Its external "
    "course down the anterior-medial arm also means shoulder/bicep tension patterns common from "
    "sustained frame-holding sit on LU territory, not just muscular fatigue.")

# ---------------------------------------------------------------------------
section_header(db, "3. The Large Intestine Meridian of Hand-Yangming (LI)")
paragraph(db, "Meridian Clock: 5:00\u20137:00 a.m. Part of the Anterior Circuit, paired as Fu with the "
              "Lung (Zang). Continues immediately where the Lung Meridian's branch leaves off.")
sub_header(db, "Running Course")
numbered_list(db, [
    "Begins at the tip of the index finger, Shangyang (LI1).",
    "Runs the radial side of the index finger through LI2 and LI3.",
    "Passes between the 1st and 2nd metacarpal bones at Hegu (LI4) and the anatomical snuffbox at LI5.",
    "Ascends the lateral-anterior forearm (LI6\u2013LI10).",
    "Crosses the elbow at LI11 and LI12.",
    "Ascends the lateral-anterior upper arm to the shoulder joint at Jianyu (LI15).",
    "Continues under/behind the shoulder to LI16, meeting Bingfeng (SI12).",
    "Passes to the 7th cervical vertebra, meeting Dazhui (Du14).",
    "Travels along the neck to the supraclavicular fossa, then internally connects with the lung, "
    "passes through the diaphragm, and pertains to the large intestine.",
])
sub_header(db, "The Branch",
           keep_with=110)
paragraph(db, "From the supraclavicular fossa, a separate branch rises through the neck (LI17, LI18), "
              "passes through the cheek and enters the lower gums, curves around the upper lip (meeting "
              "ST4) and passes the philtrum (meeting Du26), crosses to the opposite side of the nose, "
              "and ends at Yingxiang (LI20), meeting the Stomach Meridian of Foot-Yangming.")
flag_box(db, "The Ling Shu (Miraculous Pivot, Ch. 4) additionally describes a branch running to the "
             "leg, ending at Shangjuxu (ST37), the Lower He-Sea Point of the Large Intestine.")

embed_figure_pair(db, f"{FIG}/moa_li.jpg", "MOA \u2014 Internal Course",
                   f"{FIG}/cam_li.jpg", "CAM \u2014 External Points",
                   "Left: internal course showing the Large Intestine/Lung visceral connection (MOA). "
                   "Right: the 20 external points, Shangyang (LI1) to Yingxiang (LI20) (CAM).", max_h=260)

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Shangyang (LI1)", "Jing-Well Point"],
    ["Last point", "Yingxiang (LI20)", "\u2014"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Crossing Points (4 points)",
           keep_with=40)
paragraph(db, "Dazhui (Du14), Shuigou (Du26), Dicang (ST4), Bingfeng (SI12) \u2014 points where the "
              "Large Intestine Meridian physically intersects with another channel's pathway.")

sub_header(db, "Summary of the Large Intestine Meridian")
bullet_list(db, [
    "Pertaining organ: Large Intestine. Connecting organ: Lung.",
    "Running course: hand to head, along the lateral-anterior arm, up to the lower gums.",
    "Total points: 20.",
    "The branch: supraclavicular fossa to neck to cheek to lower gums to around the lip to across the "
    "philtrum to the opposite side of the nose, connecting to the Stomach Meridian of Foot-Yangming.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Fever.",
    "Parched mouth and thirst.",
    "Sore throat, nosebleed, toothache, red and painful eyes.",
    "Swelling of the neck; pain along the channel on the upper arm, shoulder, and shoulder blade.",
    "Motor impairment of the fingers.",
])
sub_header(db, "B. Internal organ (Large Intestine) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Abdominal pain.",
    "Intestinal noises.",
    "Loose stool.",
    "Sometimes accompanied by shortness of breath and belching.",
])
dance_sidebar(db, "the arm line and partnering mechanics",
    "LI's external course runs the entire lateral-anterior arm line, hand to shoulder to neck to face "
    "\u2014 essentially the whole visible \"arm styling\" line judges watch in Latin and the frame-arm in "
    "Smooth. 'Motor impairment of the fingers' and pain along the shoulder/shoulder-blade sit exactly "
    "where partnering-related overuse shows up: leading-hand grip fatigue, shoulder impingement from "
    "sustained frame extension, and the lateral elbow strain common from repeated turns and lifts.")

# ---------------------------------------------------------------------------
section_header(db, "4. The Zang-Fu Relationship \u2014 Lung and Large Intestine")
paragraph(db, "The Lung and Large Intestine are externally-internally related via their meridians: the "
              "Lung Meridian belongs to Zang, the Large Intestine Meridian belongs to Fu. This is the "
              "same interior-exterior pairing logic introduced in Module 1 (each of the 12 primary "
              "meridians pairs a Zang with a Fu organ) \u2014 LU/LI is the first such pair encountered "
              "channel-by-channel, and it is also the pair that opens the Anterior Circuit.")

section_header(db, "5. Ballroom & DanceSport Relevance \u2014 Summary")
paragraph(db, "Original synthesis, not lecture content \u2014 flagged as such throughout, consistent "
              "with Module 1.")
bullet_list(db, [
    "LU and LI together cover the entire functional arm line plus breath mechanics \u2014 the two "
    "systems most directly loaded by ballroom frame work, arm styling, and partnering.",
    "Both channels' symptom lists (shoulder/arm pain, finger motor impairment, chest fullness/"
    "shortness of breath) map onto genuinely common dancer complaints, not abstract theory \u2014 this "
    "is likely early, concrete material for the capstone's injury-pattern-to-channel framework.",
])

section_header(db, "6. Still Open / Not Yet Sourced")
bullet_list(db, [
    "Finger measurement's specific cun ratios \u2014 named as a method in the cun-measurement source "
    "but not detailed on the pages reviewed. Will confirm before stating specific values.",
    "Meeting-point logic (Yuan-Source, Luo-Connecting, Five Shu, etc.) for LU and LI specifically \u2014 "
    "still deferred to the future Extraordinary Vessels / Special Points module, per Module 1.",
])

section_header(db, "Source Notes")
paragraph(db, "Primary source: Week_2.pdf (33 slides, Dr. Zhang, Week 2). No class transcript was "
              "available for Week 2. Cun measurement (Section 1) is sourced separately from CAM "
              "reference material \u2014 \u201cAn Introduction to Acupuncture Points\u201d (p.127\u2013129) "
              "and \u201cChinese Acupuncture and Moxibustion\u201d (Table 7) \u2014 not from Dr. Zhang's "
              "slides. MOA and CAM figures are the same reference figures used across the weekly study "
              "kits. Section 5 is flagged separately as original synthesis.")

db.end_page()
db.save()
