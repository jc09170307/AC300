"""Shared content for the Week 7 PLA -- Divergent Channels, Sinew Channels &
Cutaneous Regions. Per Dr. Zhang's own Week 1 syllabus reading (AC300Week1.txt,
verified transcript): 'in week seven, we'll get some knowledge about the
additional channels and regions. And in week eight, we'll know about the
eight extraordinary meridians.' This corrects an earlier assumption that
Week 7 = Extraordinary Vessels -- that's Week 8.

Reading assignment for this week (verified, from Lecture_61102.pdf 'For Next
Week' slide, which follows the Week 6 GB lecture): MOA p.367-370, 387-390,
417-421, 469-472; CAM p.77-82. Channels Projects due Week 8 (same slide).
"""

ACCENT_DIVERGENT = (0.114, 0.227, 0.369)   # navy
ACCENT_SINEW = (0.55, 0.38, 0.16)          # brown/amber -- not an organ-element color
ACCENT_CUTANEOUS = (0.16, 0.44, 0.46)      # slate teal -- not an organ-element color
GRAY = (0.40, 0.40, 0.40)

READING_ASSIGNMENT = ("MOA p.367-370, 387-390, 417-421, 469-472; CAM p.77-82 "
                       "(per Lecture 6 'For Next Week' slide) \u00b7 Channels Projects due Week 8")

CONFLUENCES = [
    ("Foot Taiyang / Foot Shaoyin", "BL", "KI"),
    ("Foot Shaoyang / Foot Jueyin", "GB", "LR"),
    ("Foot Yangming / Foot Taiyin", "ST", "SP"),
    ("Hand Taiyang / Hand Shaoyin", "SI", "HT"),
    ("Hand Shaoyang / Hand Jueyin", "SJ", "PC"),
    ("Hand Yangming / Hand Taiyin", "LI", "LU"),
]

VOCAB = [
    ("Jing Bie", "Divergent Channel", ACCENT_DIVERGENT),
    ("Jing Jin", "Sinew Channel / Muscle Region", ACCENT_SINEW),
    ("Pi Bu", "Cutaneous Region", ACCENT_CUTANEOUS),
    ("Liu He", "Six Confluences / Six Unions", ACCENT_DIVERGENT),
    ("Biao-Li", "Exterior-Interior (paired-channel relationship)", ACCENT_DIVERGENT),
    ("Li", "\"Separate\" -- divergent channel leaves the primary pathway", ACCENT_DIVERGENT),
    ("Ru", "\"Enter\" -- divergent channel enters the body cavity/organs", ACCENT_DIVERGENT),
    ("Chu", "\"Emerge\" -- divergent channel re-emerges superficially", ACCENT_DIVERGENT),
    ("He", "\"Converge/Join\" -- divergent channel rejoins at the neck/head", ACCENT_DIVERGENT),
    ("Jing Luo", "General term: the whole channel system (jing = channels, luo = collaterals)", None),
]

LEARNING_TARGETS = [
    "Define a Divergent Channel (Jing Bie) and state how it differs functionally from a primary channel.",
    "State where divergent channels mainly distribute (chest, abdomen, head) and their core function -- deepening the interior-exterior (Biao-Li) relationship between paired channels.",
    "Name the pattern of a divergent channel's path using the 4 verbs: Li (separate) -> Ru (enter) -> Chu (emerge) -> He (converge).",
    "List all 6 Confluences (Liu He) by their paired primary channels.",
    "Define a Sinew Channel (Jing Jin) and state the one thing it does NOT have that a primary channel does (no pertaining Zang/Fu organ).",
    "Define a Cutaneous Region (Pi Bu) as the surface/skin reflection zone of a primary channel, and state its diagnostic use.",
    "Distinguish all 4 supplementary systems from each other in one line each: Collaterals (Luo), Divergent Channels (Jing Bie), Sinew Channels (Jing Jin), Cutaneous Regions (Pi Bu).",
    "TRAP: state clearly that this week is NOT the Eight Extraordinary Vessels -- that's Week 8. Don't let study time bleed into next week's material by mistake.",
]

CONNECT_BLANKS = [
    ("Divergent channels branch out from the primary meridians and are mainly distributed on chest, abdomen, and", 70, "."),
    ("Sinew channels reflect the relationship between channels and body", 90, "."),
    ("Cutaneous regions are the surface", 90, "reflection of the 12 meridians."),
    ("Divergent channels strengthen the interior-exterior (", 90, ") relationship between paired channels."),
    ("The 4-verb divergent-channel pattern is: Li, Ru, Chu,", 60, "."),
    ("The 12 divergent channels organize into", 40, "confluences (unions)."),
    ("Next week (Week 8) covers the Eight", 100, "."),
]

ANTICIPATORY_DIVERGENT = [
    (1, True, "The 4-Verb Pattern", "Walk through Li -> Ru -> Chu -> He for a Yang-channel divergent branch. Where does it typically emerge from (hint: a joint)?"),
    (2, True, "Yin vs Yang Rejoining", "Where does a YIN channel's divergent branch rejoin -- back to its own primary channel, or somewhere else? What's different about the Yang pattern?"),
    (3, False, "The 6 Confluences", "List all 6 Confluences (Liu He) pairs by primary channel abbreviation."),
    (4, False, "Clinical Value", "What can divergent channels treat that primary-channel points alone might miss?"),
]
ANTICIPATORY_SINEW = [
    (5, True, "Structural Difference", "What is the single biggest structural difference between a Sinew Channel and a primary Channel?"),
    (6, False, "Where They Concentrate", "Sinew channels tend to gather/knot at which kind of body landmarks?"),
    (7, False, "Clinical Association", "What category of clinical conditions are Sinew Channels most associated with treating?"),
]
ANTICIPATORY_CUTANEOUS = [
    (8, True, "Diagnostic Use", "How can changes in a Cutaneous Region (color, texture, temperature) be used diagnostically?"),
    (9, False, "Trap: Count", "How many Cutaneous Regions are there, and do they map 1:1 onto the 12 primary channels?"),
]
ANTICIPATORY_COMPARE = [
    (10, True, "Luo vs Jing Bie", "Collaterals (Luo) and Divergent Channels (Jing Bie) both 'branch off' a primary channel. What's the key functional difference between them?"),
    (11, False, "Why This Order", "Why might Dr. Zhang's syllabus place Divergent/Sinew/Cutaneous (Week 7) BEFORE the Eight Extraordinary Vessels (Week 8), rather than after?"),
]

IQ_CHECKPOINTS = [
    ("1-4", [
        (1, "ACQ", "What does 'Jing Bie' mean, literally and functionally?"),
        (2, "ACQ", "Name the 4 verbs describing a divergent channel's path, in order."),
        (3, "ACQ", "How many Confluences (Liu He) do the 12 divergent channels form?"),
        (4, "MAINT", "What are the 3 circuits from the Master Map, and which weeks completed each? (Wks 1-6 review)"),
    ]),
    ("5-8", [
        (5, "ACQ", "Name the BL/KI confluence pairing by Yin/Yang stage name (e.g. Foot Taiyang/Foot Shaoyin)."),
        (6, "ACQ", "What does a Sinew Channel lack that a primary channel has?"),
        (7, "ACQ", "What is a Cutaneous Region, in one sentence?"),
        (8, "MAINT", "Name all 8 confluent (opening) points you already know, with their vessel. (Wks 2-6 review)"),
    ]),
    ("9-12", [
        (9, "ACQ", "TRAP: Which week covers the Eight Extraordinary Vessels -- 7 or 8?"),
        (10, "ACQ", "What's the key functional difference between Luo (Collaterals) and Jing Bie (Divergent Channels)?"),
        (11, "MAINT", "State the Yin/Yang direction rule for Hand-Yang channels. (Wk1 Master Map review)"),
        (12, "MAINT", "GB's slide claims 12 points/6 meridians for crossing points, but only how many are actually named? (Wk6 flag)"),
    ]),
]

IQ_ANSWERS = [
    "Jing Bie = 'channel divergence/separation' -- a deep branch that leaves the primary channel to strengthen ties between paired channels and the organs.",
    "Li (separate) -> Ru (enter) -> Chu (emerge) -> He (converge).",
    "6 Confluences (Liu He) -- one per Yin/Yang paired-channel relationship.",
    "Anterior Circuit (LU-LI-ST-SP, Wks 2-3), Posterior/Inner Circuit (HT-SI-BL-KI, Wks 4-5), Middle Circuit (PC-SJ-GB-LR, Wk 6).",
    "Foot Taiyang / Foot Shaoyin (BL-KI).",
    "A pertaining Zang/Fu organ -- Sinew Channels have no internal organ connection, only muscle/joint distribution.",
    "The surface/skin zone where a primary channel's Qi and Blood reflect onto the body -- used for observation-based diagnosis.",
    "LU7 (Ren Mai), KI6 (Yin Qiao), SI3 (Du Mai), BL62 (Yang Qiao), SP4 (Chong Mai), PC6 (Yin Wei), SJ5 (Yang Wei), GB41 (Dai Mai) -- all 8 confluent points, already complete as of Week 6.",
    "Week 8 -- NOT Week 7. Week 7 is Divergent/Sinew/Cutaneous systems.",
    "Divergent Channels reach deep into the torso/organs and reinforce interior-exterior pairing; Collaterals are more superficial, branching from Luo points to link paired channels directly without the same deep organ-level detour.",
    "Hand -> Head.",
    "9 are actually named, though the slide states 12 points / 6 meridians -- flagged, unresolved pending Dr. Zhang confirmation.",
]

FLINNER_NOTE = (
    "No Flinner transcript exists yet for this week's topic -- his parallel-section transcripts on file cover "
    "only Weeks 1-4. Nothing below is presented as verified Flinner-lecture content; it reuses corrections "
    "already verified from his Weeks 1-4 material, applied where directly relevant, and flags his general "
    "teaching emphasis as a study-approach suggestion, not a content claim."
)
FLINNER_CROSSFIRE = [
    "Don't confuse this week's NEW connections (Divergent-Channel Li/Ru/Chu/He links) with primary-channel "
    "Crossing/Meeting Points from earlier weeks -- different systems. Per Flinner's verified corrections: LU has "
    "only 1 true meeting point (shared with SP); LI has zero incoming meeting points; PC and HT both have zero "
    "crossing points. Keep these separate from this week's divergent-channel confluences.",
    "Per Flinner's general emphasis across Weeks 1-4: prioritize the ROUTE pattern (the 4-verb Li/Ru/Chu/He "
    "logic and the 6 Confluences) over memorizing every point along each divergent branch -- most divergent "
    "channels reuse points you already know from the primary channels, so the new information this week is "
    "almost entirely structural, not point-level.",
]
