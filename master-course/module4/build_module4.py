import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common_module4 import (DocBuilder, module_cover, section_header, sub_header,
                             paragraph, bullet_list, numbered_list, table, table_start_height,
                             dance_sidebar, flag_box, embed_figure_pair, embed_figure_single,
                             figure_caption, NAVY, RED, GOLD_DARK, DARK)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
OUT = f"/home/claude/module4/out/AC300_Module4_HT_SI_{EDITION}.pdf"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
FIG = os.path.join(os.path.dirname(__file__), "figures")

db = DocBuilder(OUT, "Module 4: Heart & Small Intestine", "Module 4 \u2014 Heart & Small Intestine")

module_cover(
    db,
    title="Heart & Small Intestine",
    subtitle="The Posterior Circuit Opens \u2014 Plus: The Five Shu Points",
    points_line="Third channel pair of the 12 Primary Meridians \u2014 first pair of the Posterior Circuit",
    covers_bullets=[
        "The Five Shu Points \u2014 finally addressed, straight from Dr. Zhang's own slides",
        "A formal definition of \u201ccrossing point\u201d",
        "The Heart Meridian of Hand-Shaoyin (HT) \u2014 course, points, syndromes",
        "The Small Intestine Meridian of Hand-Taiyang (SI) \u2014 course, points, syndromes",
        "Ballroom & DanceSport relevance",
    ],
    info_lines=[
        "Sourced from the 2026 Lecture 4 deck (Dr. Zhang, 41 slides) and the Week 4 class transcript.",
        "This deck includes classical Chinese source text (Ling Shu citations) for each channel, not",
        "seen in Weeks 1\u20133 \u2014 noted where it adds something the English paraphrase doesn't.",
    ],
    module_num="4",
)

# ---------------------------------------------------------------------------
db.new_page()
section_header(db, "How to Use This Module")
paragraph(db, "HT and SI are the fifth and sixth of the 12 primary meridians \u2014 the first pair of "
              "the Posterior Circuit (Module 1, Section 6: HT to SI to BL to KI). This module also "
              "finally addresses the Five Shu Points, flagged as pending back in Module 1 \u2014 Dr. "
              "Zhang introduces them here, organically, as part of the Heart Meridian's running "
              "course, rather than in a separate special-points lecture.")

section_header(db, "1. The Five Shu Points")
paragraph(db, "Slide 19 of this lecture introduces these directly, described as new content students "
              "had not previously covered. Each of the 12 primary meridians has five specific points "
              "below the elbow or knee, named for how far along the channel's flow of Qi has "
              "progressed at that point \u2014 from where Qi 'emerges' at the fingertip/toenail to where "
              "it 'enters' near the elbow/knee.")
_shu_headers = ["Point", "Meaning", "Location", "Clinical Application"]
_shu_rows = [
    ["Jing-Well", "\u201cWhere it emerges\u201d", "Tips of fingers and toes", "First aid, clearing heat, relieving pain, reducing inflammation"],
    ["Ying-Spring", "\u201cWhere it flows\u201d", "Before the metacarpophalangeal/metatarsophalangeal joints", "Feverish diseases, heat-related disorders"],
    ["Shu-Stream", "\u201cWhere it pours\u201d", "After the metacarpophalangeal/metatarsophalangeal joints", "Heaviness in the body, joint pain, pain syndromes"],
    ["Jing-River", "\u201cWhere it travels\u201d", "Forearms or lower legs", "Externally contracted diseases (colds, flu), cough, asthma"],
    ["He-Sea", "\u201cWhere it enters\u201d", "Near the elbow or knee joints", "Disorders of the six Fu organs"],
]
table(db, _shu_headers, _shu_rows, col_widths=[70, 90, 175, 211], font_size=7.8, leading=10.2)
paragraph(db, "Module 1 flagged meeting-point logic (Yuan-Source, Luo-Connecting, Five Shu, etc.) as "
              "deferred to a future Special Points module. The Five Shu Points specifically are now "
              "covered \u2014 the rest (Yuan-Source, Luo-Connecting, Xi-Cleft, Eight Confluent) remain "
              "open, noted again in this module's Still Open section.")

sub_header(db, "Crossing Point \u2014 A Formal Definition")
paragraph(db, "Also given directly in this lecture, worth having on record precisely: \u201cA crossing "
              "point is defined as a specific acupoint situated at the convergence or crossing of two "
              "or more meridians.\u201d Every crossing point named in Modules 1\u20133 fits this definition "
              "exactly \u2014 this is simply the first time the lecture states it as a formal rule.")

# ---------------------------------------------------------------------------
section_header(db, "2. The Heart Meridian of Hand-Shaoyin (HT)")
paragraph(db, "Meridian Clock: 11:00 a.m.\u20131:00 p.m. Part of the Posterior Circuit, paired as Zang "
              "with the Small Intestine (Fu). The Posterior Circuit's first channel, opening where "
              "Module 3's Spleen Meridian handed off.")
sub_header(db, "Running Course \u2014 Three Branches")
numbered_list(db, [
    "Internal descending portion: originates in the heart, emerges to spread over the \u201cheart "
    "system\u201d (the tissues connecting the heart to other Zang-Fu organs), passes through the "
    "diaphragm, and connects with the small intestine (its connecting organ).",
    "The branch (ascending portion): from the heart system, runs alongside the esophagus to connect "
    "with the \u201ceye system\u201d (the tissues connecting the eyes with the brain). The transcript "
    "notes a classical line worth keeping: \u201cthe eye is the window of the heart\u201d \u2014 both the "
    "Heart and Small Intestine Meridians connect with the eye.",
    "The branch (straight portion): from the heart system, goes upward to the lung, then turns "
    "downward and emerges from the axilla at Jiquan (HT1). Runs the posterior border of the medial "
    "upper arm \u2014 behind the Lung Meridian and the Pericardium Meridian \u2014 down to the cubital "
    "fossa (HT3), the medial-posterior forearm (HT4, HT5), the pisiform region (HT6, HT7), the palm "
    "(HT8), ending at the tip of the little finger, radial side (Shaochong, HT9).",
])
flag_box(db, "Clinical emphasis from the Week 4 transcript, not on the slides themselves: Jiquan "
             "(HT1) is specifically called out as important for treating stroke. Shaochong (HT9), the "
             "Jing-Well point, is emphasized for emergency presentations \u2014 severe chest pain, "
             "difficulty breathing, palpitations \u2014 consistent with the Jing-Well category's general "
             "first-aid function from Section 1 above.")

embed_figure_pair(db, f"{FIG}/moa_ht.jpg", "MOA \u2014 Internal Course",
                   f"{FIG}/cam_ht.jpg", "CAM \u2014 External Points",
                   "Left: internal course showing the Heart/Small Intestine/Lung/eye connections "
                   "(MOA). Right: the 9 external points, Jiquan (HT1) to Shaochong (HT9) (CAM).", max_h=250)

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Jiquan (HT1)", "\u2014"],
    ["Last point", "Shaochong (HT9)", "Jing-Well Point"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Summary of the Heart Meridian")
bullet_list(db, [
    "Pertaining organ: Heart. Connecting organ: Small Intestine.",
    "Running course: chest to hand, along the posterior-medial arm.",
    "Total points: 9 \u2014 the smallest channel covered so far.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "General feverishness, headache.",
    "Pain in the eyes, pain along the back of the upper arm.",
    "Dry throat, thirst.",
    "Hot or painful palms; coldness in the palms and soles of the feet.",
    "Pain along the scapula and/or medial aspect of the forearm.",
])
sub_header(db, "B. Internal organ (Heart) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Blood pressure changes, palpitation.",
    "Pain or fullness in the chest and ribs, or below the ribs.",
    "Mental disorders \u2014 anxiety, depression, poor memory.",
])
paragraph(db, "The transcript is explicit about why the internal symptom list spans both cardiovascular "
              "and mental/emotional territory: the Heart has two main functions in this framework \u2014 "
              "governing Blood and the blood vessels, and \u201chousing the mind\u201d (Shen). The second "
              "function is why Heart Meridian points, especially those near the wrist, are used "
              "clinically for insomnia, poor memory, depression, and anxiety, not only for "
              "cardiovascular symptoms.")
dance_sidebar(db, "the axilla line and performance-anxiety physiology",
    "HT's straight portion runs the posterior-medial arm from the axilla \u2014 directly under sustained "
    "load in any extended-arm frame position, and the exact territory that tightens under prolonged "
    "overhead or extended-arm holds. The dual Heart function the transcript describes \u2014 blood "
    "vessels and Shen/mind together \u2014 also maps onto something dancers know from experience even "
    "without the TCM framing: physical cardiovascular strain and performance anxiety show up through "
    "the same channel, not as two separate problems.")

# ---------------------------------------------------------------------------
section_header(db, "3. The Small Intestine Meridian of Hand-Taiyang (SI)")
paragraph(db, "Meridian Clock: 1:00\u20133:00 p.m. Part of the Posterior Circuit, paired as Fu with the "
              "Heart (Zang).")
sub_header(db, "Running Course \u2014 Three Branches")
numbered_list(db, [
    "The main course: starts at the ulnar side of the tip of the little finger (Shaoze, SI1). "
    "Follows the ulnar side of the dorsum of the hand to the wrist, emerging at the styloid process "
    "of the ulna (SI4, SI5). Ascends the posterior forearm (SI6, SI7), passes between the olecranon "
    "of the ulna and the medial epicondyle of the humerus (SI8), runs the posterior-lateral upper arm "
    "to the shoulder joint (SI9, SI10), circles the scapular region (SI11\u2013SI13), meets Dazhui "
    "(GV14) at the top of the shoulder, turns down to the supraclavicular fossa, connects with the "
    "heart, descends alongside the esophagus, passes the diaphragm, reaches the stomach, and finally "
    "enters the small intestine, its pertaining organ.",
    "The branch (from the supraclavicular fossa): ascends the neck to the cheek, to the outer canthus "
    "(Tongziliao, GB1), entering the ear at Tinggong (SI19).",
    "The branch (from the neck): rises to the infraorbital region (Quanliao, SI18), continues to the "
    "lateral side of the nose, and reaches the inner canthus (Jingming, BL1), linking with the "
    "Bladder Meridian of Foot-Taiyang \u2014 the next channel in the Posterior Circuit.",
])

sub_header(db, "Crossing Points",
           keep_with=90)
paragraph(db, "This channel has an unusually well-documented crossing-point list \u2014 the source gives "
              "precise locations, not just names, for each:")
table(db, ["Point", "Location"], [
    ["Zhongwan (CV12)", "Anterior midline, 4 cun above the umbilicus"],
    ["Shangwan (CV13)", "Anterior midline, 5 cun above the umbilicus"],
    ["Jingming (BL1)", "Slightly above the inner canthus"],
    ["Dazhu (BL11)", "1.5 cun lateral to Taodao (GV13), at the lower border of the T1 spinous process"],
    ["Fufen (BL41)", "3 cun lateral to the Governor Vessel, at the lower border of the T2 spinous process"],
    ["Dazhui (GV14)", "Below the C7 spinous process, roughly level with the shoulders"],
    ["Tongziliao (GB1)", "0.5 cun lateral to the outer canthus"],
    ["Erheliao (SJ22)", "Anterior/superior to Ermen (SJ21), level with the root of the auricle"],
], col_widths=[130, 416], font_size=8.0)

embed_figure_single(db, f"{FIG}/moa_si.jpg", "MOA \u2014 Full Course (Internal + External)",
                     "From MOA \u2014 back and front views with every crossing point labeled directly on "
                     "the figure. No CAM figure is used here: the CAM reference PDF's channel sequence "
                     "skips from Fig. 6 (Heart) to Fig. 8 (Bladder), and Fig. 7 (Small Intestine) is "
                     "genuinely absent from the source \u2014 not a page this module failed to find.",
                     max_h=300)

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Shaoze (SI1)", "Jing-Well Point"],
    ["Last point", "Tinggong (SI19)", "\u2014"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Summary of the Small Intestine Meridian")
bullet_list(db, [
    "Pertaining organ: Small Intestine. Connecting organ: Heart.",
    "Running course: hand to head, along the posterior-lateral arm, up through the neck and cheek.",
    "Total points: 19.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Numbness of the mouth and tongue.",
    "Pain in the neck or cheek; sore throat; stiff neck.",
    "Pain around the lateral aspect of the shoulder and upper arm.",
])
sub_header(db, "B. Internal organ (Small Intestine) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Pain and distention in the lower abdomen, sometimes extending to the waist.",
    "Diarrhea, or abdominal pain with dry stool or constipation.",
])
dance_sidebar(db, "the shoulder-circling course and neck tension",
    "SI's main course literally circles the scapular region before crossing the top of the shoulder "
    "\u2014 almost exactly the pattern of tension that builds from sustained frame work and repeated "
    "overhead arm positions. 'Stiff neck' and shoulder/upper-arm pain along the channel are worth "
    "knowing as SI territory specifically, distinct from LI's shoulder symptoms back in Module 2: LI "
    "runs the front/lateral line into the face, SI runs the back of the shoulder into the ear \u2014 "
    "different complaint, different channel.")

# ---------------------------------------------------------------------------
section_header(db, "4. Ballroom & DanceSport Relevance \u2014 Summary")
paragraph(db, "Original synthesis, not lecture content \u2014 flagged as such throughout, consistent "
              "with Modules 1\u20133.")
bullet_list(db, [
    "HT and SI open the Posterior Circuit's dance-relevant territory: HT covers the inner-arm/axilla "
    "line and the blood-vessel/Shen dual function; SI covers the shoulder-circling line into the neck "
    "and ear.",
    "Between LI (Module 2) and SI (this module), the shoulder is now covered from two distinct "
    "channel angles \u2014 front/lateral (LI) and back/circling (SI) \u2014 which is likely to matter for "
    "the capstone's injury-pattern framework when shoulder complaints don't cleanly separate by front "
    "vs. back.",
])

section_header(db, "5. Still Open / Not Yet Sourced")
bullet_list(db, [
    "Yuan-Source, Luo-Connecting, Xi-Cleft, and Eight Confluent Points \u2014 the Five Shu Points are "
    "now covered (Section 1), but these other meeting-point categories remain deferred to a future "
    "Special Points module.",
    "Finger measurement's specific cun ratios \u2014 still unconfirmed, carried over from Module 2.",
    "The exact abdominal/chest channel spacing relative to the midline \u2014 still unconfirmed, "
    "carried over from Module 3.",
])

section_header(db, "Source Notes")
paragraph(db, "Primary source: 2026AC300Lecture_4vivian_1.pdf (41 slides, Dr. Zhang, Lecture 4) and "
              "AC300_Week_4_Transcript.txt (class transcript). This is the first module to draw on a "
              "\u20182026\u2019-series deck rather than an older \u2018Week_N\u2019 deck \u2014 per the project's "
              "established source hierarchy, the 2026 decks are authoritative where both exist. MOA "
              "figures are the same reference figures used across the weekly study kits; the CAM "
              "reference PDF is missing its Small Intestine figure (Section 3 explains this directly "
              "rather than substituting silently).")

db.end_page()
db.save()
