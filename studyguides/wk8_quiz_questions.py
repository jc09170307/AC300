"""Week 8 Quiz Kit question bank -- standalone practice exam covering the 15
Collaterals, 12 Divergent Channels, 12 Muscle Regions, and 12 Cutaneous
Regions. Content verified against Lecture8vivian1119.pdf and the Week 8
transcript. NOTE: Dr. Zhang stated there is no new quiz this week (see
HOMEWORK_QUIZ_NOTE in wk8_content.py) -- this kit is self-test material for
review, not a stand-in for a graded Quiz N."""

# ---------------------------------------------------------------------------
# SECTION A -- Multiple Choice
# ---------------------------------------------------------------------------
MC_QUESTIONS = [
    dict(q="How many Luo-Connecting points (\u201c15 Collaterals\u201d) are there in total?",
         choices=["12", "14", "15", "16"], answer=2,
         explain="12 paired-meridian Luo points + CV's + GV's + the Spleen's Great Collateral = 15."),
    dict(q="What acupoint gives rise to the Great (Major) Collateral of the Spleen?",
         choices=["SP 4 Gongsun", "SP 21 Dabao", "SP 6 Sanyinjiao", "SP 9 Yinlingquan"], answer=1,
         explain="The Great/Major Collateral of the Spleen begins at Dabao, SP 21."),
    dict(q="Why does the body need a 15th collateral beyond the 12 paired + CV + GV (14)?",
         choices=["To cover the top of the head", "To cover the lateral side of the chest",
                  "To cover the soles of the feet", "To cover the palms"], answer=1,
         explain="CV covers the front midline, GV covers the back midline, but neither covers the "
                 "LATERAL chest -- the Spleen's Great Collateral fills that gap."),
    dict(q="What is the Luo-Connecting point of the Lung meridian, and what Extraordinary Vessel "
           "confluent point does it double as?",
         choices=["LU 9 Taiyuan; Chong Mai", "LU 7 Lieque; Ren Mai (CV)",
                  "LU 5 Chize; Du Mai (GV)", "LU 11 Shaoshang; Dai Mai"], answer=1,
         explain="LU 7 Lieque is both the Lung's Luo point AND the confluent (opening) point of "
                 "Ren Mai -- reviewed from Week 7."),
    dict(q="Where do the Luo-Connecting points of the HAND meridians generally cluster?",
         choices=["Around the elbow", "Around the wrist", "Around the shoulder", "Around the fingertips"],
         answer=1, explain="Per Dr. Zhang's rule of thumb, Hand-meridian Luo points cluster around the wrist."),
    dict(q="Where do the Luo-Connecting points of the FOOT meridians generally cluster?",
         choices=["Around the knee", "Around the hip", "Around the ankle (malleolus)", "Around the toes"],
         answer=2, explain="Foot-meridian Luo points cluster around the malleolus (ankle)."),
    dict(q="What do the 12 Divergent Channels (Jing Bie) lack that the 12 primary meridians have?",
         choices=["A course through the chest", "Their own acupuncture points", "A relationship to Yin/Yang",
                  "A beginning point"], answer=1,
         explain="Divergent channels have NO acupuncture points of their own and no pertaining organ."),
    dict(q="In the Li-He-Chu-merge framework for Divergent Channels, what does \u201cHe\u201d refer to?",
           choices=["Where it begins", "The organs/systems it involves", "Where it exits to the surface",
                    "The meridian it merges into"], answer=1,
           explain="Li = beginning, He = organs/systems involved, Chu = exiting, then it merges into its Yang partner."),
    dict(q="All 6 Yin Divergent Channels eventually do what?",
         choices=["Develop their own acupoints", "Merge into their paired Yang primary meridian",
                  "Terminate at the umbilicus", "Connect directly to the brain"], answer=1,
         explain="Every Yin divergent channel merges into its paired Yang meridian -- none resurfaces as a separate Yin pathway."),
    dict(q="Which Divergent Channel is the only one that crosses the Dai (Belt) Meridian along its course?",
         choices=["Bladder", "Kidney", "Liver", "Gallbladder"], answer=1,
         explain="The Kidney divergent channel crosses the Dai Meridian at the level of T7."),
    dict(q="Which Divergent Channel runs THROUGH the heart on its way to the mouth and eye?",
         choices=["Stomach", "Spleen", "Small Intestine", "Large Intestine"], answer=0,
         explain="The Stomach divergent channel passes through the heart en route to the mouth, nose, and eye."),
    dict(q="What do the 12 Muscle (Sinew) Regions connect, that the primary meridians and divergent channels do not directly address?",
         choices=["Zang-fu organs", "Bones, joints, and muscles", "Blood vessels", "The brain"], answer=1,
         explain="Muscle Regions nourish muscles and connect bones/joints -- they do NOT go inside the body or touch organs."),
    dict(q="All 3 Yang Muscle Regions of the FOOT connect with which structure?",
         choices=["The genitals", "The eyes", "The thoracic cavity", "The forehead angle"], answer=1,
         explain="All 3 Yang Muscle Regions of the Foot (BL, GB, ST) connect with the eyes."),
    dict(q="All 3 Yin Muscle Regions of the HAND connect with which structure?",
         choices=["The eyes", "The genitals", "The thoracic cavity (chest)", "The forehead"], answer=2,
         explain="All 3 Yin Muscle Regions of the Hand (LU, HT, PC) connect with the thoracic cavity."),
    dict(q="What are the 12 Cutaneous Regions (Pi Bu)?",
         choices=["The deepest layer of the meridian system", "The parts of the 12 meridians reflected on the "
                  "body surface", "A synonym for the 15 Collaterals", "The points shared between two meridians"],
         answer=1, explain="Cutaneous Regions are the outermost layer -- where meridian qi is reflected on the skin."),
    dict(q="Per Su Wen Chapter 56, what is the order of disease transmission from the surface inward?",
         choices=["Meridians -> Skin -> Collaterals -> Organs", "Skin -> Collaterals -> Meridians -> Fu organs -> Zang organs",
                  "Collaterals -> Skin -> Zang organs -> Fu organs", "Skin -> Zang organs -> Fu organs -> Meridians"],
         answer=1, explain="Skin -> Collaterals -> Meridians -> Fu organs -> Zang organs, progressing deeper each step."),
]

# ---------------------------------------------------------------------------
# SECTION B -- Luo Point Matching
# ---------------------------------------------------------------------------
LUO_MATCH_LEFT = ["1. Lung (LU)", "2. Large Intestine (LI)", "3. Stomach (ST)", "4. Spleen (SP)",
                   "5. Heart (HT)", "6. Small Intestine (SI)", "7. Bladder (BL)", "8. Kidney (KI)",
                   "9. Pericardium (PC)", "10. Sanjiao (SJ)"]
LUO_MATCH_RIGHT = ["A. HT5 Tongli", "B. LU7 Lieque", "C. KI4 Dazhong", "D. SP4 Gongsun",
                    "E. BL58 Feiyang", "F. SI7 Zhizheng", "G. ST40 Fenglong", "H. LI6 Pianli",
                    "I. SJ5 Waiguan", "J. PC6 Neiguan"]
LUO_MATCH_ANSWER = {"1": "B", "2": "H", "3": "G", "4": "D", "5": "A", "6": "F", "7": "E", "8": "C",
                     "9": "J", "10": "I"}

# ---------------------------------------------------------------------------
# SECTION C -- Fill in the Blank
# ---------------------------------------------------------------------------
FILL_BLANK = [
    ("The Luo-Connecting point of the Gallbladder meridian is ______, 5 cun above the external malleolus.", "GB 37 Guangming"),
    ("The Luo-Connecting point of the Liver meridian is ______, 5 cun above the internal malleolus.", "LR 5 Ligou"),
    ("The Governor Vessel's collateral arises from ______, in the perineum.", "GV 1 Changqiang"),
    ("The Conception Vessel's collateral separates from the Governor Vessel at ______, the lower end of the sternum.", "CV 15 Jiuwei"),
    ("The Great Collateral of the Spleen begins from ______ and spreads through the chest and hypochondriac region.", "SP 21 Dabao"),
    ("Divergent Channels are characterized by the four-part relationship of Li (beginning), He (organs/systems), Chu (exiting), and then ______ into the Yang meridian.", "merging"),
    ("All 3 Yin Muscle Regions of the FOOT connect with the ______ region.", "genital"),
    ("The 12 Cutaneous Regions are the ______ layer of the human body, where meridian qi is distributed.", "outermost"),
]

# ---------------------------------------------------------------------------
# SECTION D -- Short Answer
# ---------------------------------------------------------------------------
SHORT_ANSWER = [
    dict(q="Explain why there are 15 Collaterals rather than exactly 12, using the front/back/side logic from lecture.",
         answer="The 12 paired primary meridians each need one Luo point to link them (12). The Governor "
                "Vessel (back midline) and Conception Vessel (front midline) also have their own points and "
                "so need their own collaterals too (14). The lateral side of the chest is left uncovered by "
                "all of these, so the Spleen's Great Collateral (Dabao, SP21) covers that gap, bringing the "
                "total to 15."),
    dict(q="A patient has a point prescribed that is both a Luo-Connecting point AND a Confluent (opening) "
           "point of an Extraordinary Vessel. Name one such point and explain why carrying two special-point "
           "identities matters clinically.",
         answer="Example: LU7 Lieque (Luo point of Lung + Confluent point of Ren Mai), or SP4 Gongsun (Luo "
                "point of Spleen + Confluent point of Chong Mai), or PC6 Neiguan (Luo point of Pericardium + "
                "Confluent point of Yin Wei Mai), or SJ5 Waiguan (Luo point of Sanjiao + Confluent point of "
                "Yang Wei Mai). A point that carries multiple special-point identities has a broader/stronger "
                "clinical reach, since it can access both functions at once."),
    dict(q="Explain the difference between a Collateral (Luo Mai) and a Divergent Channel (Jing Bie) in terms of depth and points.",
         answer="Collaterals run on the body SURFACE and each have one dedicated Luo-Connecting acupoint. "
                "Divergent Channels run DEEP inside the body, have NO acupuncture points of their own, and "
                "have no pertaining zang-fu organ -- their job is purely to reinforce the existing "
                "interior-exterior relationship between paired meridians."),
    dict(q="A patient has chronic lateral knee/ankle pain with reduced range of motion, but no clear organ-level complaint. Which of this week's 4 systems is most directly relevant to treatment, and why?",
         answer="The Muscle (Sinew) Regions -- they connect bones, joints, and muscles and are specifically "
                "indicated for Bi (painful obstruction) syndrome, contracture, stiffness, spasm, and muscular "
                "atrophy. Because a Muscle Region covers a WIDE band rather than a single point, treatment can "
                "target anywhere along the region's course, not just one exact acupoint."),
]

# ---------------------------------------------------------------------------
# SECTION E -- MAINT Review (Week 7 confluent points, live Q&A from Lecture 8)
# ---------------------------------------------------------------------------
MAINT_QUESTIONS = [
    dict(q="Which vessel is called the \u201cBelt\u201d because it runs around the waist, and is it the only "
           "vessel that runs horizontally?",
         answer="Dai Mai (Belt Vessel) -- yes, it is the only one of the 8 Extraordinary Vessels that runs "
                "horizontally rather than vertically."),
    dict(q="Which two vessels have a confluent point that is the SAME as their starting point?",
         answer="Yin Qiao Mai (KI 6 Zhaohai) and Yang Qiao Mai (BL 62 Shenmai) -- both begin AND open at "
                "their confluent point."),
    dict(q="Which three vessels share the lower abdomen as a common origin (\u201cyi yuan san qi\u201d)?",
         answer="Du Mai (GV), Ren Mai (CV), and Chong Mai."),
    dict(q="True or false: the Du Meridian connects with the Bladder as a zang-fu pairing. Explain.",
         answer="False -- none of the 8 Extraordinary Vessels connect to a zang or fu organ; they have no "
                "interior-exterior organ pairing the way the 12 primary meridians do."),
    dict(q="Which channel is the \u201cSea of All Yin Meridians,\u201d and which is the \u201cSea of All Yang "
           "Meridians\u201d?",
         answer="Ren Mai (Conception Vessel) is the Sea of All Yin Meridians; Du Mai (Governor Vessel) is "
                "the Sea of All Yang Meridians."),
]
