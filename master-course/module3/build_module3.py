import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common_module3 import (DocBuilder, module_cover, section_header, sub_header,
                             paragraph, bullet_list, numbered_list, table, table_start_height,
                             dance_sidebar, flag_box, embed_figure_pair, embed_figure_row,
                             figure_caption, NAVY, RED, GOLD_DARK, DARK)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
OUT = f"/home/claude/module3/out/AC300_Module3_ST_SP_{EDITION}.pdf"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
FIG = os.path.join(os.path.dirname(__file__), "figures")

db = DocBuilder(OUT, "Module 3: Stomach & Spleen", "Module 3 \u2014 Stomach & Spleen")

module_cover(
    db,
    title="Stomach & Spleen",
    subtitle="The Anterior Circuit Continues \u2014 Head to Foot, Foot to Chest",
    points_line="Second channel pair of the 12 Primary Meridians \u2014 the two largest yet",
    covers_bullets=[
        "The Stomach Meridian of Foot-Yangming (ST) \u2014 6 branches, 45 points",
        "The Spleen Meridian of Foot-Taiyin (SP) \u2014 3 branches, 21 points",
        "How ST and SP close out the Anterior Circuit and hand off to Heart (HT)",
        "Ballroom & DanceSport relevance",
    ],
    info_lines=[
        "Sourced from the Week 3 lecture deck (Dr. Zhang, 49 slides) and the Week 3 class transcript.",
        "Slides 1\u201313 of the deck are LU/LI review (already covered in Module 2) and are not repeated",
        "here except where the transcript adds something genuinely new.",
    ],
    module_num="3",
)

# ---------------------------------------------------------------------------
db.new_page()
section_header(db, "How to Use This Module")
paragraph(db, "ST and SP are the third and fourth of the 12 primary meridians, closing out the "
              "Anterior Circuit (LU to LI to ST to SP) before Qi hands off into the Posterior "
              "Circuit at the Heart Meridian. ST is by far the largest channel covered so far \u2014 45 "
              "points across 6 branches \u2014 so this module leans harder on the branch-by-branch "
              "structure than Module 2 did.")

section_header(db, "1. The Stomach Meridian of Foot-Yangming (ST)")
paragraph(db, "Meridian Clock: 7:00\u20139:00 a.m. Part of the Anterior Circuit, paired as Fu with the "
              "Spleen (Zang). Runs head to foot \u2014 the only Yang meridian of foot whose external "
              "course this module covers so far.")
sub_header(db, "Running Course \u2014 The Six Branches")
paragraph(db, "Dr. Zhang's own slides organize this channel as six named branches rather than one "
              "continuous line. Learning the branch boundaries first makes the point-by-point course "
              "far easier to hold onto.")
numbered_list(db, [
    "Facial branch (ascending): lateral side of the ala nasi to the forehead.",
    "Facial branch (internal): a separate facial branch that pertains to the stomach and connects "
    "with the spleen internally.",
    "The straight portion: supraclavicular fossa, through the nipple, down the abdomen to the groin.",
    "Branch from the lower orifice of the stomach: descends inside the abdomen, down the thigh, to "
    "the lateral side of the tip of the 2nd toe.",
    "The tibial branch: from 3 cun below the knee (ST36) to the lateral side of the middle toe.",
    "The foot branch: from the dorsum of the foot to the medial tip of the great toe, linking with "
    "the Spleen Meridian.",
])

# ---------------------------------------------------------------------------
sub_header(db, "Branch 1 \u2014 Facial, Ascending to the Forehead")
paragraph(db, "Starts at the lateral side of the ala nasi (Yingxiang, LI20 \u2014 a crossing point, not "
              "an ST point itself). Ascends to the bridge of the nose, meeting the Bladder Meridian "
              "(Jingming, BL1). Turns downward along the lateral side of the nose (Chengqi, ST1), "
              "enters the upper gum, re-emerges, curves around the lips, and descends to meet the "
              "Conception Vessel at the mentolabial groove (Chengjiang, CV24). Runs posterolaterally "
              "across the lower cheek (Daying, ST5), winds along the mandible angle (Jiache, ST6), "
              "ascends in front of the ear, crossing Shangguan (GB3), then reaches the anterior "
              "hairline (Touwei, ST8) \u2014 shown on the same step as two nearby crossing points, "
              "Xuanli (GB6) and Hanyan (GB4) \u2014 before ending this branch at the forehead.")
flag_box(db, "Xiaguan (ST7) is not named anywhere in Dr. Zhang's numbered course for this branch "
             "(Slides 17\u201318 go straight from the mandible at ST6 to Shangguan GB3) \u2014 flagged "
             "here because an earlier draft of this module inserted it based on general anatomical "
             "assumption rather than the source. Corrected.")
sub_header(db, "Branch 2 \u2014 Facial, Internal (Pertaining/Connecting)")
paragraph(db, "From in front of Daying (ST5), descends past the anterior neck (Renying, ST9), the "
              "throat (ST10, ST11), enters the supraclavicular fossa (ST12), then internally pertains "
              "to the stomach, passes through the diaphragm, and connects with the spleen.")
sub_header(db, "Branch 3 \u2014 The Straight Portion")
paragraph(db, "From the supraclavicular fossa, descends through the nipple (Ruzhong, ST17) and by the "
              "umbilicus (ST19\u2013ST29), entering the lateral side of the lower abdomen at Qichong "
              "(ST30).")
flag_box(db, "The Week 3 transcript specifically calls out: \u201cOnly the stomach meridian passes "
             "through the nipple\u201d \u2014 stated as a distinguishing landmark for telling ST apart "
             "from the Kidney, Spleen, and CV lines running nearby on the chest/abdomen. The "
             "transcript also discusses the relative spacing of these lines out from the midline "
             "(Conception Vessel), roughly CV to KI to ST to SP moving laterally \u2014 but the "
             "specific cun values given verbally were garbled in an auto-transcription (numbers like "
             "\u201cfour,\u201d \u201csix,\u201d and \u201ctwo\u201d cun are audible but not clearly attributable to "
             "the correct lines). Flagged rather than stated as fact \u2014 will confirm exact spacing "
             "against a written source before using it for point-location purposes.")

# ---------------------------------------------------------------------------
sub_header(db, "Branch 4 \u2014 From the Lower Orifice of the Stomach")
paragraph(db, "Descends inside the abdomen from the lower orifice of the stomach, rejoining the "
              "straight portion near Qichong (ST30), traverses the anterior thigh (Biguan, ST31), the "
              "knee via Futu (ST32), continues down the anterior-lateral tibia, crosses the dorsum of "
              "the foot, and ends at the lateral side of the tip of the 2nd toe (Lidui, ST45).")
sub_header(db, "Branch 5 \u2014 The Tibial Branch")
paragraph(db, "Separates 3 cun below the knee (Zusanli, ST36) and descends to the lateral side of the "
              "middle toe.")
sub_header(db, "Branch 6 \u2014 The Foot Branch")
paragraph(db, "Separates from the dorsum of the foot (Chongyang, ST42) and ends at the medial side of "
              "the tip of the great toe (Yinbai, SP1) \u2014 linking with the Spleen Meridian of "
              "Foot-Taiyin and handing off the Anterior Circuit's third leg.")

embed_figure_row(db, [
    (f"{FIG}/moa_st.jpg", "MOA \u2014 Internal Course"),
    (f"{FIG}/cam_st1.jpg", "CAM \u2014 Face/Torso (I)"),
    (f"{FIG}/cam_st2.jpg", "CAM \u2014 Leg (II)"),
], "Left: internal course and crossing points (MOA). Center/Right: the 45 external points, Chengqi "
   "(ST1) to Lidui (ST45), split across the source's two figures (CAM).", max_h=250)

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Chengqi (ST1)", "\u2014"],
    ["Last point", "Lidui (ST45)", "Jing-Well Point"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Crossing Points (11 points)",
           keep_with=40)
paragraph(db, "Yingxiang (LI20), Jingming (BL1), Shangguan (GB3), Hanyan (GB4), Xuanli (GB6), Yinbai "
              "(SP1), Shenting (GV24), Shuigou (GV26), Zhongwan (CV12), Shangwan (CV13), Chengjiang "
              "(CV24). By far the most crossing points of any channel covered so far \u2014 consistent "
              "with ST being the largest and most widely-branching meridian.")

sub_header(db, "Summary of the Stomach Meridian")
bullet_list(db, [
    "Pertaining organ: Stomach. Connecting organ: Spleen.",
    "Running course: head to foot. Starts lateral to the nose, terminates at the medial tip of the "
    "great toe (Yinbai, SP1), linking with the Spleen Meridian.",
    "Total points: 45 \u2014 the largest channel covered so far.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "High fever, tidal fevers, flushed face.",
    "Sweating, sometimes chills, or pain in the eyes.",
    "Fever blisters (mouth and lips), sore throat.",
    "Swelling on the neck, facial paralysis, chest pain.",
    "Pain or distension along the channel in the leg and foot; coldness in the lower limb.",
])
sub_header(db, "B. Internal organ (Stomach) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Abdominal distension, fullness, edema.",
    "Persistent hunger.",
])
dance_sidebar(db, "the longest line on the body, and the one most loaded by extension",
    "ST runs the entire front of the body, head to toe \u2014 the single longest continuous line covered "
    "so far, and it's almost exactly the line placed under stretch in any deep backbend or extended "
    "contra-body line (American Smooth again, but also Rumba's hip-forward walk). \u2018Coldness in the "
    "lower limb\u2019 and leg/foot pain along the channel are worth knowing as a distinct pattern from "
    "the Posterior Circuit's own leg symptoms (Module 1) \u2014 anterior-leg complaints point here, "
    "posterior-leg complaints point to BL/KI instead.")

# ---------------------------------------------------------------------------
section_header(db, "2. The Spleen Meridian of Foot-Taiyin (SP)")
paragraph(db, "Meridian Clock: 9:00\u201311:00 a.m. Part of the Anterior Circuit, paired as Zang with "
              "the Stomach (Fu). Closes out the Anterior Circuit before Qi flows into the Heart "
              "Meridian, opening the Posterior Circuit.")
sub_header(db, "Running Course")
numbered_list(db, [
    "Starts at the tip of the big toe (Yinbai, SP1).",
    "Runs the medial aspect of the foot at the junction of red and white skin, ascends in front of "
    "the medial malleolus (SP5).",
    "Follows the medial aspect of the leg and the posterior aspect of the tibia.",
    "Crosses in front of the Liver Meridian of Foot-Jueyin, 8 cun above the medial malleolus (SP9) "
    "\u2014 the same crossing named as the Liver Meridian's exception back in Module 1, Section 4.",
    "Passes the anterior-medial knee and thigh, enters the abdomen, and pertains to the spleen, "
    "connecting with the stomach.",
])
sub_header(db, "Branch 2 \u2014 Ascending from the Stomach")
paragraph(db, "Passes through the diaphragm, runs alongside the esophagus, and spreads over the lower "
              "surface of the tongue, reaching the root of the tongue.")
sub_header(db, "Branch 3 \u2014 Internal Connection")
paragraph(db, "From the stomach, a separate branch goes through the diaphragm to the heart, linking "
              "with the Heart Meridian of Hand-Shaoyin \u2014 the first channel of the Posterior Circuit.")

embed_figure_pair(db, f"{FIG}/moa_sp.jpg", "MOA \u2014 Internal Course",
                   f"{FIG}/cam_sp.jpg", "CAM \u2014 External Points",
                   "Left: internal course showing the Spleen/Stomach/Heart connections (MOA). Right: "
                   "the 21 external points, Yinbai (SP1) to Dabao (SP21) (CAM).", max_h=250)

# ---------------------------------------------------------------------------
sub_header(db, "First and Last Points")
table(db, ["", "Point", "Category"], [
    ["First point", "Yinbai (SP1)", "Jing-Well Point"],
    ["Last point", "Dabao (SP21)", "Major Luo-Connecting Point of the Spleen"],
], col_widths=[90, 180, 276], font_size=8.5)

sub_header(db, "Crossing Points (6 points)",
           keep_with=30)
paragraph(db, "Zhongji (CV3), Guanyuan (CV4), Xiawan (CV10), Riyue (GB24), Qimen (LR14), Zhongfu "
              "(LU1) \u2014 the last of these, Zhongfu, is the same point that opened the Lung Meridian "
              "in Module 2, now revisited as a crossing point rather than a starting point.")

sub_header(db, "Summary of the Spleen Meridian")
bullet_list(db, [
    "Pertaining organ: Spleen. Connecting organ: Stomach.",
    "Running course: starts at the tip of the big toe, enters the abdomen, ascends through the "
    "diaphragm alongside the esophagus, reaches the tongue.",
    "The branch: stomach to diaphragm to heart, linking with the Heart Meridian of Hand-Shaoyin.",
    "Total points: 21.",
])

sub_header(db, "Main Syndromes & Indications")
sub_header(db, "A. External course symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Heaviness in the body or head.",
    "Fatigued limbs and emaciated muscles.",
    "Stiffness of the tongue, coldness along the medial side of the leg and knee.",
    "Edema in the foot or leg.",
])
sub_header(db, "B. Internal organ (Spleen) symptoms", color=GOLD_DARK, size=10)
bullet_list(db, [
    "Abdominal pain.",
    "Fullness or distension, diarrhea, poor digestion.",
    "Vomiting, hard lumps in the abdomen.",
    "Reduced appetite, constipation.",
])
dance_sidebar(db, "fatigue, heaviness, and the medial leg line",
    "SP's external symptom list \u2014 heaviness in the body, fatigued limbs, edema in the foot or leg "
    "\u2014 reads almost like a checklist for late-competition-day fatigue, especially in styles with "
    "sustained turnout (SP runs the medial leg, directly loaded by turned-out standing and deep plies "
    "in Latin/Rhythm). Tongue stiffness as a symptom is also a genuinely distinctive marker worth "
    "knowing \u2014 nothing else covered so far lists it.")

# ---------------------------------------------------------------------------
section_header(db, "3. Closing the Anterior Circuit")
paragraph(db, "LU to LI to ST to SP is now complete \u2014 the full Anterior Circuit from Module "
              "1, Section 6. SP's third branch (stomach to diaphragm to heart) is the actual handoff "
              "point into the Posterior Circuit: the next channel is the Heart Meridian of "
              "Hand-Shaoyin, Module 1's Section 6 table already names this sequence, and Module 4 will "
              "cover it directly.")
paragraph(db, "Slide 48 of this week's deck states the underlying logic plainly: \u201cThe 12 main "
              "meridians are like the energy highways of the body, with each meridian having a "
              "specific active period and closely connected to its corresponding organ... mastering "
              "this pattern not only helps us understand the onset time of diseases but also provides "
              "important basis for precise treatment.\u201d Four meridians and their clock windows are "
              "now covered: LU (3\u20135 a.m.), LI (5\u20137 a.m.), ST (7\u20139 a.m.), SP (9\u201311 a.m.) \u2014 "
              "exactly the first third of the 24-hour cycle.")

section_header(db, "4. Ballroom & DanceSport Relevance \u2014 Summary")
paragraph(db, "Original synthesis, not lecture content \u2014 flagged as such throughout, consistent "
              "with Modules 1 and 2.")
bullet_list(db, [
    "ST and SP together cover the entire front-of-body and medial-leg lines \u2014 completing the "
    "Anterior Circuit's dance-relevant territory alongside LU/LI's arm and breath coverage from "
    "Module 2.",
    "Between the four Anterior Circuit channels, nearly every symptom list so far names fatigue, "
    "heaviness, or pain patterns that map onto real, specific training complaints rather than vague "
    "TCM abstraction \u2014 this is accumulating into real substance for the capstone's "
    "injury-pattern-to-channel framework.",
])

section_header(db, "5. Still Open / Not Yet Sourced")
bullet_list(db, [
    "The exact cun spacing of the abdominal/chest channels relative to the midline (CV, KI, ST, SP) "
    "\u2014 discussed verbally in the Week 3 transcript but the specific numbers were garbled in "
    "transcription. Will confirm against a written source before stating specific values.",
    "Meeting-point logic (Yuan-Source, Luo-Connecting, Five Shu, etc.) for ST and SP specifically "
    "\u2014 still deferred to the future Extraordinary Vessels / Special Points module, per Modules "
    "1 and 2.",
])

section_header(db, "Source Notes")
paragraph(db, "Primary source: Week_3.pdf (49 slides, Dr. Zhang, Week 3) and AC300Week3Transcription."
              "txt (class transcript). Slides 1\u201313 and 38\u201347 of the deck are review of prior "
              "material (LU, LI) and quiz preparation; not repeated here. MOA and CAM figures are the "
              "same reference figures used across the weekly study kits. Section 4 is flagged "
              "separately as original synthesis.")

db.end_page()
db.save()
