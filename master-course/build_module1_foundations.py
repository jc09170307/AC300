import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common_foundations import (DocBuilder, module_cover, section_header, sub_header,
                                 paragraph, bullet_list, numbered_list, table, table_start_height,
                                 dance_sidebar, flag_box, circulation_diagram, circuits_diagram,
                                 circuit_photo_figures, distribution_figure, NAVY, RED, GOLD_DARK, DARK)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
OUT = f"/home/claude/foundations/out/AC300_Module1_Foundations_{EDITION}.pdf"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

db = DocBuilder(OUT, "Module 1: Foundations", "Module 1 \u2014 Foundations")

module_cover(
    db,
    title="Foundations",
    subtitle="Channel Theory: History, Terminology & System Architecture",
    points_line="The conceptual scaffolding for the entire AC300 course",
    covers_bullets=[
        "History and origins of channel theory (Yellow Emperor's Inner Canon)",
        "Meridians vs. Collaterals \u2014 the core distinction",
        "Nomenclature: how every meridian gets its name",
        "Distribution rules on limbs, head, and trunk",
        "Circulation direction and the closed 12-meridian loop",
        "The Three Main Circuits (Anterior / Posterior / Middle)",
        "The three functions of the meridian system",
        "Ballroom & DanceSport relevance",
    ],
    info_lines=[
        "Sourced from Lecture 1 (Dr. Zhang, 41 slides) and the Week 1 class transcript.",
        "Two topics \u2014 cun measurement and meeting-point logic \u2014 are not in Lecture 1 and are",
        "flagged as pending in later modules rather than invented here.",
    ],
    module_num="1",
)

# ---------------------------------------------------------------------------
db.new_page()
section_header(db, "How to Use This Module")
paragraph(db, "This is the conceptual scaffolding for the entire course. Everything from the "
              "individual channels, points, and special-point categories built in Weeks 2 through 9 "
              "hangs on the handful of ideas in this module. If only one document gets re-read before "
              "boards in 2030, it should probably be this one \u2014 the channel-specific material is "
              "easier to relearn than the underlying logic that organizes it.")
flag_box(db, "Scope note: cun measurement (the proportional point-location system) and meeting-point "
             "logic (Yuan-Source, Luo-Connecting, Five Shu, etc.) are NOT covered in Lecture 1. Rather "
             "than invent placeholder content, cun measurement is deferred to Module 2 (Lung/Large "
             "Intestine, where point-location language first appears) and meeting-point logic to the "
             "future Extraordinary Vessels / Special Points module.")

section_header(db, "Glossary")
paragraph(db, "Read this before anything else \u2014 every term below is used without redefinition "
              "throughout the rest of this module.")
glossary = [
    ("Qi", "The animating functional activity/energy TCM holds moves through and sustains the body. One of the two substances the meridians transport, along with Blood."),
    ("Blood (Xue)", "In TCM, a substance broader than the Western hematologic sense \u2014 it nourishes tissue and is co-transported with Qi through the channels."),
    ("Meridian (Jingmai)", "Literally 'pathway.' One of the main trunk-line channels through which Qi and Blood circulate. Deep, few in number, vertical in orientation."),
    ("Collateral (Luomai)", "Literally 'network.' A smaller branch off a meridian \u2014 shallow, numerous, running crosswise rather than in a straight vertical line. Meridians and collaterals together make up the channel system."),
    ("Channel", "The umbrella term for the whole system \u2014 meridians and collaterals together. 'Meridian' means specifically the 12 primary trunk lines."),
    ("Zang", "A Yin, solid organ in TCM organ theory (Lung, Heart, Spleen, Liver, Kidney, Pericardium). Each of the 12 primary meridians pairs with one Zang or Fu organ."),
    ("Fu", "A Yang, hollow organ (Large Intestine, Stomach, Small Intestine, Bladder, Gallbladder, San Jiao)."),
    ("San Jiao (SJ)", "Also called Triple Burner/Triple Energizer \u2014 the Fu organ paired with the Pericardium channel. Standardized as 'SJ' throughout this course's weekly materials; used here for consistency even though Lecture 1's own slides mix 'SJ' and 'TE.'"),
    ("Taiyin / Yangming / Shaoyin / Taiyang / Jueyin / Shaoyang", "The six-part Yin/Yang naming system applied to each limb pair of meridians (three Yin, three Yang) \u2014 explained in full in Section 3."),
    ("The 12 Primary Meridians", "The main trunk channels, one per Zang or Fu organ, forming six hand/foot pairs."),
    ("The 8 Extraordinary Meridians", "A separate set of eight channels (Conception, Governing, and six others) that don't pair with organs the way the 12 primary meridians do \u2014 own module."),
    ("The 15 Collaterals", "The named connecting branches off the primary meridians \u2014 covered in the Connective Tissue Systems module."),
    ("The 12 Sinew Meridians & 12 Cutaneous Regions", "The muscular/myofascial and superficial-skin distributions paralleling the 12 primary meridians \u2014 the two categories most directly relevant to dance biomechanics."),
]
table(db, ["Term", "Definition"], glossary, col_widths=[135, 411], font_size=8.2, leading=10.8)

# ---------------------------------------------------------------------------
section_header(db, "1. A Quick History")
bullet_list(db, [
    "Acupuncture's core theory was first systematically recorded in The Yellow Emperor's Inner Canon (Huangdi Neijing), over 2,000 years ago.",
    "The Inner Canon marks the formal establishment of the Meridian System, built primarily around the 12 primary meridians, framed inside Yin-Yang cosmology \u2014 health as harmony between body and natural principles.",
    "The theory spread to East Asia by roughly the 6th century CE, and to Europe/North America from the 17th century onward.",
    "Today the WHO recognizes acupuncture as an evidence-based complementary therapy, integrated into healthcare systems worldwide.",
])
paragraph(db, "Lecture 1 poses a genuine open question, worth sitting with rather than answering too "
              "quickly: which came first, the channels or the points? The lecture does not resolve it "
              "\u2014 it is presented as a live question in the field's own history, not a settled fact.")
sub_header(db, "Where the theory came from \u2014 three converging strands")
numbered_list(db, [
    "Observation of needling sensation \u2014 ancient practitioners noticing and tracking the sensation and conduction of stimulation (deqi/needle sensation).",
    "Summary of acupoint effects, extended into lines \u2014 points were mapped for their effects first, and the lines connecting related points (channels) were inferred afterward.",
    "Internal Qi flow observed through Qigong and guided-breathing practice ('small cycle' circulation) \u2014 a separate, meditative line of observation feeding the same theoretical structure.",
])
paragraph(db, "The lecture quotes the Ling Shu directly on the physicality of the claim being made: "
              "ancient physicians held that a person's structure could be measured, palpated, and "
              "examined while alive, and dissected and observed after death \u2014 the channel system "
              "was proposed as something with a real anatomical correlate, even though (as the lecture "
              "notes) modern researchers still don't treat channels as fixed anatomical structures like "
              "nerves or vessels \u2014 more as functional networks integrating neural, circulatory, "
              "connective-tissue, and bioelectrical processes.")

# ---------------------------------------------------------------------------
_merid_v_coll_headers = ["", "Meridians (Jingmai)", "Collaterals (Luomai)"]
_merid_v_coll_rows = [
    ["Meaning", "Pathway", "Network"],
    ["Standing", "Trunk", "Branch"],
    ["Distribution", "Vertical line", "Running crosswise"],
    ["Depth", "Deep", "Shallow"],
    ["Number", "Few", "Many"],
    ["Function", "Leading \u2014 the pathways through which Qi and Blood circulate", "Supplement and bond \u2014 promotes Qi/Blood circulation"],
]
section_header(db, "2. Meridians vs. Collaterals \u2014 The Core Distinction",
               keep_with=table_start_height(_merid_v_coll_headers, _merid_v_coll_rows, [80, 233, 233]))
table(db, _merid_v_coll_headers, _merid_v_coll_rows, col_widths=[80, 233, 233])
paragraph(db, "The lecture cites the Ling Shu directly here too: meridians run through the interior as "
              "the main trunk; the crosswise branches are collaterals; and branches off the collaterals "
              "are the finest sub-branches ('grandchild' vessels).")
paragraph(db, "The river analogy, used explicitly in the Week 1 class discussion: meridians are the "
              "river itself; collaterals (Luo) are its tributary branches.")

# ---------------------------------------------------------------------------
section_header(db, "3. Naming the Meridians (Nomenclature)")
paragraph(db, "Every one of the 12 primary meridians is named using three characteristics: (1) Hand or "
              "Foot \u2014 which limb it runs through; (2) Yin or Yang \u2014 and specifically which of the "
              "six Yin/Yang subdivisions; (3) A Zang or Fu organ \u2014 which internal organ it's paired "
              "with. Example given directly in the lecture: 'the Lung Meridian of Hand-Taiyin', 'the "
              "Stomach Meridian of Foot-Yangming.'")
sub_header(db, "The Six Yin/Yang Subdivisions")
bullet_list(db, [
    "Three Yin: Taiyin, Shaoyin, Jueyin",
    "Three Yang: Yangming, Taiyang, Shaoyang",
])
_meridians_12_headers = ["", "Yin Meridian (Zang)", "Yang Meridian (Fu)"]
_meridians_12_rows = [
    ["Six Meridians of Hand", "Lung Meridian of Hand-Taiyin (LU)", "Large Intestine Meridian of Hand-Yangming (LI)"],
    ["", "Heart Meridian of Hand-Shaoyin (HT)", "Small Intestine Meridian of Hand-Taiyang (SI)"],
    ["", "Pericardium Meridian of Hand-Jueyin (PC)", "San Jiao Meridian of Hand-Shaoyang (SJ)"],
    ["Six Meridians of Foot", "Spleen Meridian of Foot-Taiyin (SP)", "Stomach Meridian of Foot-Yangming (ST)"],
    ["", "Kidney Meridian of Foot-Shaoyin (KI)", "Bladder Meridian of Foot-Taiyang (BL)"],
    ["", "Liver Meridian of Foot-Jueyin (LR)", "Gallbladder Meridian of Foot-Shaoyang (GB)"],
]
sub_header(db, "The Full Set of 12 Primary Meridians",
           keep_with=table_start_height(_meridians_12_headers, _meridians_12_rows, [110, 218, 218], font_size=8.0))
table(db, _meridians_12_headers, _meridians_12_rows, col_widths=[110, 218, 218], font_size=8.0)

# ---------------------------------------------------------------------------
section_header(db, "4. Distribution on the Body")
sub_header(db, "On the limbs")
bullet_list(db, [
    "Medial (inner) aspect leads to Yin meridians.",
    "Lateral (outer) aspect leads to Yang meridians.",
    "Within each, front-to-back ordering: Anterior = Taiyin/Yangming; Posterior = Shaoyin/Taiyang; Middle = Jueyin/Shaoyang.",
])
distribution_figure(db, os.path.join(os.path.dirname(__file__), "distribution_forearms.jpg"))
flag_box(db, "Named exception (called out directly in the lecture): the Liver Meridian of Foot-Jueyin "
             "ascends to a point 8 cun above the medial malleolus, where it crosses and runs behind the "
             "Spleen Meridian of Foot-Taiyin \u2014 a specific, testable irregularity in an otherwise "
             "clean pattern.")
sub_header(db, "On the head and trunk")
bullet_list(db, [
    "Anterior leads to Yangming.",
    "Posterior leads to Taiyang.",
    "Lateral leads to Shaoyang.",
    "Trunk (chest/abdomen) anterior specifically also carries Shaoyin, Taiyin, Jueyin.",
])
dance_sidebar(db, "medial/lateral injury pattern-matching",
    "The medial/lateral Yin/Yang split is worth knowing cold for injury pattern-matching. "
    "Medial-side overuse (adductor strain, medial knee pain common in turned-out Latin technique) sits "
    "on Yin-meridian territory; lateral-side overuse (IT band, lateral ankle sprains from a checked "
    "action) sits on Yang-meridian territory. Becomes directly useful once point selection for injury "
    "protocols comes up in the clinical module.")

# ---------------------------------------------------------------------------
section_header(db, "5. Circulation \u2014 Direction and Rules")
sub_header(db, "The four directional rules (stated as absolute rules, not tendencies)")
numbered_list(db, [
    "Yin meridians of the hand: chest to hand.",
    "Yang meridians of the hand: hand to head.",
    "Yang meridians of the foot: head to foot.",
    "Yin meridians of the foot: foot to abdomen.",
])
sub_header(db, "The connection logic between them \u2014 worth actually drawing")
numbered_list(db, [
    "The three Yin meridians of hand run chest to hand, converging at the fingertips with the three Yang meridians of hand (interior/exterior paired relationship).",
    "The three Yang meridians of hand ascend fingertips to head, connecting there with the three Yang meridians of foot.",
    "The three Yang meridians of foot descend head to toes, joining the three Yin meridians of foot.",
    "The three Yin meridians of foot ascend toes to abdomen/chest, meeting the three Yin meridians of hand \u2014 closing the loop.",
])
paragraph(db, "This closed loop is the entire logic of the meridian clock (Qi flowing through all 12 "
              "meridians across a 24-hour cycle) \u2014 not covered in depth in Lecture 1 beyond the "
              "instruction to notice, at any point in the day, which meridian's 'time' it currently is, "
              "as a memorization device.")
circulation_diagram(db)

# ---------------------------------------------------------------------------
section_header(db, "6. The Three Main Circuits")
paragraph(db, "This is the single most load-bearing organizational concept in the entire course \u2014 "
              "everything in Weeks 2 through 9 was taught circuit-by-circuit.")
flag_box(db, "Terminology note (locked, per standing correction): Lecture 1 calls these the Anterior, "
             "Posterior, and Middle Circuits. A later lecture drops those labels in speech, so working "
             "materials should use 'Posterior Circuit (also called Inner Circuit)' to stay consistent "
             "with both namings, since Dr. Zhang is verbally inconsistent between them and exams may "
             "use either term. Anterior and Middle didn't pick up an alternate naming \u2014 only "
             "Posterior/Inner.")
table(db, ["Circuit", "Meridians", "Yin/Yang labels"], [
    ["Anterior Circuit", "Lung (LU) to Large Intestine (LI) to Stomach (ST) to Spleen (SP)", "Taiyin / Yangming"],
    ["Posterior Circuit (also called Inner Circuit)", "Heart (HT) to Small Intestine (SI) to Bladder (BL) to Kidney (KI)", "Shaoyin / Taiyang"],
    ["Middle Circuit", "Pericardium (PC) to San Jiao (SJ) to Gallbladder (GB) to Liver (LR)", "Jueyin / Shaoyang"],
], col_widths=[140, 296, 110], font_size=8.0)
circuits_diagram(db)
circuit_photo_figures(db, os.path.dirname(__file__))
paragraph(db, "Each circuit traces the same four-stage loop described in Section 5 (chest to hand to "
              "head to foot to chest), just through its own four organs. Lecture 1's own diagram draws "
              "this as a single unified figure \u2014 chest, hand/fingers, face/head, foot/toes, back to "
              "chest \u2014 with all three circuits running in parallel through those same four "
              "anatomical waypoints.")
sub_header(db, "Study method suggested directly by Dr. Zhang, worth taking literally")
paragraph(db, "Draw all 12 meridians and their three circulations by hand, repeatedly, until the "
              "pattern is automatic. This isn't a throwaway suggestion \u2014 it's presented as the "
              "actual mechanism by which the material becomes memorable.")
dance_sidebar(db, "three functional lines",
    "The Three Circuits map loosely onto three functional lines already trained on the floor. The "
    "Anterior Circuit (LU-LI-ST-SP) runs the front body line \u2014 the anterior chain load in an "
    "American Smooth contra-body extension, or the front-of-hip/quad demand in a Rumba forward walk. "
    "The Posterior Circuit (HT-SI-BL-KI) tracks the posterior chain that holds frame and postural "
    "extension \u2014 erectors, glutes, hamstrings \u2014 the chain that fails first when frame collapses "
    "under fatigue in a long Standard round. The Middle Circuit (PC-SJ-GB-LR) runs the lateral/"
    "rotational line \u2014 hip rotation in Cha Cha, lateral stability in a Foxtrot sway. This is a "
    "mnemonic bridge, not a claim that the channels are these muscle chains.")

# ---------------------------------------------------------------------------
section_header(db, "7. What the Meridians Actually Do (Three Functions)")
sub_header(db, "A. Transporting Qi and Blood, regulating Yin and Yang")
paragraph(db, "Ling Shu, Ch. 47: the meridians and collaterals transport Blood and Qi to adjust Yin and "
              "Yang, nourish tendons and bones, and support joint function.")
sub_header(db, "B. Resisting pathogens and reflecting symptoms/signs")
paragraph(db, "Ling Shu, Ch. 71: when a pathogen involves the Lung or Heart, it lingers at both elbows; "
              "when it involves the Liver, both axillae; when it involves the Spleen, both groins; when "
              "it involves the Kidney, both popliteal fossae. A direct, specific clinical-pattern claim "
              "\u2014 worth citing precisely rather than paraphrasing loosely.")
sub_header(db, "C. Transmitting needling sensation, regulating deficiency/excess")
paragraph(db, "Ling Shu, Ch. 5 and Ch. 9: acupuncture's key task is regulating Yin and Yang, and "
              "treatment must aim at regulating the flow of Qi.")

# ---------------------------------------------------------------------------
section_header(db, "8. Ballroom & DanceSport Relevance \u2014 Summary")
paragraph(db, "This section consolidates the sidebars above and adds context that spans the whole "
              "module. Everything here is original synthesis connecting channel theory to things "
              "already known from the floor and from teaching \u2014 not sourced from Dr. Zhang's "
              "lecture, and flagged as such throughout.")
bullet_list(db, [
    "The meridian clock, reframed practically: rather than 24-hour Qi-flow doctrine, it's a useful frame for when in a training day or competition schedule certain systems are more or less resilient \u2014 worth revisiting once TCM material on Qi/Blood depletion and fatigue comes up, directly relevant to back-to-back competitive rounds.",
    "This is exactly the terrain the capstone lit review lives in \u2014 the literature review on acupuncture for DanceSport injuries will eventually want a clean statement of channel distribution logic (Section 4) since injury-pattern-to-channel mapping is likely to be one of its organizing structures.",
])

section_header(db, "9. Still Open / Not Yet Sourced")
bullet_list(db, [
    "Cun measurement system \u2014 not addressed in Lecture 1. Will surface from Module 2 (Lung/Large Intestine) source material, where point locations are first given.",
    "Meeting-point logic (Yuan-Source, Luo-Connecting, Xi-Cleft, Five Shu, Eight Confluent, etc.) \u2014 not addressed in Lecture 1; built out as its own section in the future Extraordinary Vessels / Special Points module, using the existing Special Points Decoders as raw source material.",
    "SJ vs. TE labeling \u2014 Lecture 1 itself uses 'TE' on some slides and the paired-organ table elsewhere; later weekly materials standardized on 'SJ,' used throughout this module for consistency.",
])

section_header(db, "Source Notes")
paragraph(db, "Primary source: 2026AC300Lec1Vivian.pdf (41 slides, Dr. Zhang, Week 1). Secondary "
              "source: AC300Week1.txt (class transcript) \u2014 used for the meridian/collateral river "
              "analogy, the direct student Q&A on 'channel vs. meridian' terminology (meridians = the "
              "12 primary meridians specifically; channels = meridians plus collaterals, the whole "
              "system), and the 'draw it repeatedly' study instruction. Sections 1 through 7 are drawn "
              "directly from those two sources; Section 8 is flagged separately as original synthesis.")

db.end_page()
db.save()
