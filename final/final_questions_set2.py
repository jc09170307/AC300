# AC300 Practice FINAL Exam -- SET 2 (Weeks 1-9, cumulative)
# 20 DIFFERENT questions from Set 1, same cumulative scope and style.

SECTIONS = [
    ("FOUNDATIONS & THE THREE CIRCUITS", "Week 1", [
        dict(n=1, type="MC",
             q="Hand Yin and Hand Yang channels hand off Qi to each other at the:",
             opts=["Face", "Fingers", "Toes", "Chest"], ans="B",
             exp="Hand Yin ends and Hand Yang begins at the fingers (e.g. LU7's branch meets LI1 at the index "
                 "finger). Hand Yang meets Foot Yang at the face; Foot Yang meets Foot Yin at the toes; Foot Yin "
                 "meets Hand Yin internally at the chest."),
        dict(n=2, type="MC",
             q="Which meridian receives Qi directly after the Spleen (9-11 AM) in the 24-hour clock, and what does "
             "this hand-off complete?",
             opts=["Heart (11 AM-1 PM); completes the Outer Circuit and opens the Inner Circuit",
                   "Small Intestine (1-3 PM); completes the Middle Circuit",
                   "Stomach (7-9 AM); reopens the Outer Circuit",
                   "Bladder (3-5 PM); completes the Inner Circuit"],
             ans="A",
             exp="SP's internal branch passes through the diaphragm into the Heart at 11 AM, ending the Outer/"
                 "Anterior Circuit (LU-LI-ST-SP) and beginning the Inner/Posterior Circuit (HT-SI-BL-KI)."),
    ]),
    ("LU / LI -- METAL", "Week 2", [
        dict(n=3, type="MC",
             q="How many acupoints does the Lung channel have, compared to its paired Large Intestine channel?",
             opts=["LU 11 vs. LI 20", "LU 9 vs. LI 20", "LU 11 vs. LI 14", "LU 20 vs. LI 11"],
             ans="A",
             exp="LU has 11 points (LU1-LU11), LI has 20 (LI1-LI20) -- nearly double, consistent with the "
                 "pattern that Yang/Fu partners usually have more points than their Yin/Zang pair."),
        dict(n=4, type="EXCEPT",
             q="All of the following statements about LU and LI are true EXCEPT:",
             opts=["Both belong to the Metal element", "LU flows from chest to hand",
                   "LI flows from hand to head", "LI has fewer total acupoints than LU"],
             ans="D",
             exp="Reversed -- LI actually has MORE points than LU (20 vs. 11)."),
    ]),
    ("ST / SP -- EARTH", "Week 3", [
        dict(n=5, type="MC",
             q="Which is the Front-Mu point of Stomach, and which is the Front-Mu point of Large Intestine -- a "
             "commonly confused pair?",
             opts=["CV12 = Stomach; ST25 = Large Intestine", "ST25 = Stomach; CV12 = Large Intestine",
                   "CV12 = Stomach; CV4 = Large Intestine", "ST36 = Stomach; ST25 = Large Intestine"],
             ans="A",
             exp="CV12 Zhongwan is the Front-Mu of STOMACH. ST25 Tianshu is the Front-Mu of LARGE INTESTINE, "
                 "even though ST25 sits on the Stomach channel -- classic exam trap."),
        dict(n=6, type="TF",
             q="True or False: SP4 (Gongsun) is SP's Luo-Connecting point and also the Confluent point opening the "
             "Chong Mai, classically paired with PC6.",
             opts=["True", "False"], ans="A",
             exp="Correct -- SP4 carries both roles, pairing with PC6 (Neiguan) to treat chest, heart, and "
                 "stomach disorders together."),
        dict(n=7, type="MC",
             q="What is the ONLY channel that spreads over the LOWER surface of the tongue?",
             opts=["Kidney", "Spleen", "Heart", "Liver"],
             ans="B",
             exp="Spleen. (Kidney terminates at the ROOT of the tongue -- a related but distinct fact often "
                 "confused with this one.)"),
    ]),
    ("HT / SI -- FIRE", "Week 4", [
        dict(n=8, type="MC",
             q="How many acupoints does the Heart channel have -- and what is notable about this number?",
             opts=["9 -- the fewest of any primary channel", "19 -- tied with Small Intestine",
                   "11 -- same as Lung", "20 -- the most of any Yin channel"],
             ans="A",
             exp="HT has only 9 points (HT1-HT9), the fewest of any primary channel. Its paired SI channel has "
                 "19, more than double."),
        dict(n=9, type="EXCEPT",
             q="All of the following are true of the Posterior/Inner Circuit EXCEPT:",
             opts=["It includes HT, SI, BL, and KI", "HT and SI belong to the Fire element within this circuit",
                   "Peak Qi times for HT/SI/BL/KI run consecutively from 11 AM through 7 PM",
                   "PC and SJ are also part of this circuit"],
             ans="D",
             exp="PC and SJ form their own Ministerial Fire pairing within the MIDDLE Circuit, distinct from the "
                 "Posterior/Inner Circuit of HT-SI-BL-KI."),
    ]),
    ("BL / KI -- WATER", "Week 5", [
        dict(n=10, type="MC",
             q="The Bladder channel's Back-Shu series (BL13-BL28) serves what overall function?",
             opts=["Treats only bladder and kidney disorders", "Provides organ transport points for ALL 12 "
                   "zang-fu organs, reached from the back", "Only treats spinal pain", "Opens the Du Mai"],
             ans="B",
             exp="BL13-BL28 are the Back-Shu (transport) points for every zang-fu organ (e.g. BL13 Lung, BL15 "
                 "Heart, BL18 Liver, BL20 Spleen, BL21 Stomach, BL23 Kidney, BL25 LI, BL27 SI, BL28 itself)."),
        dict(n=11, type="MC",
             q="KI3 (Taixi) and KI7 (Fuliu) sit close together near the medial malleolus/Achilles tendon. What "
             "distinguishes them?",
             opts=["KI3 is Jing-River; KI7 is Shu-Stream + Yuan-Source",
                   "KI3 is Shu-Stream + Yuan-Source (dual role); KI7 is Jing-River only, 2 cun proximal",
                   "They are functionally identical", "KI3 is the Confluent point; KI7 is the Xi-Cleft"],
             ans="B",
             exp="KI3 Taixi sits in the depression between the malleolus tip and Achilles tendon and carries "
                 "the dual Shu-Stream/Yuan-Source role. KI7 Fuliu is 2 cun proximal, Jing-River only."),
        dict(n=12, type="TF",
             q="True or False: The Bladder channel is the largest meridian in the body, with 67 points across 5 "
             "branches.",
             opts=["True", "False"], ans="A",
             exp="Correct -- BL is the largest primary channel: 67 points, 5 branches, more than any other "
                 "meridian."),
    ]),
    ("PC / SJ / GB / LR -- MIDDLE CIRCUIT", "Week 6", [
        dict(n=13, type="MC",
             q="Which point pairing opens the Yang Wei Mai, and to which channels do the two points belong?",
             opts=["SJ5 Waiguan (SJ) + GB41 Zulinqi (GB)", "PC6 Neiguan (PC) + SP4 Gongsun (SP)",
                   "LU7 Lieque (LU) + KI6 Zhaohai (KI)", "SI3 Houxi (SI) + BL62 Shenmai (BL)"],
             ans="A",
             exp="SJ5 Waiguan is the confluent point opening the Yang Wei Mai, paired with GB41 Zulinqi (which "
                 "opens the Dai Mai) -- both channels belong to the Middle Circuit."),
        dict(n=14, type="MC",
             q="What is unique about the Liver channel's crossing points, compared to most other primary channels?",
             opts=["It has none", "Its 6 crossing points are shared with CV (2) and SP (1) around the genital/"
                   "abdomen region", "It has the most of any channel, 12 total", "They are all located on the head"],
             ans="B",
             exp="LR has 6 crossing points, concentrated with CV and SP around the genital/abdominal region -- "
                 "consistent with LR's role in reproductive and lower-abdomen pathology."),
    ]),
    ("EIGHT EXTRAORDINARY VESSELS", "Week 7", [
        dict(n=15, type="MC",
             q="Which vessel is structurally unique for running HORIZONTALLY rather than along the body's long axis?",
             opts=["Chong Mai", "Dai Mai (Girdle/Belt Vessel)", "Yang Wei Mai", "Du Mai"],
             ans="B",
             exp="The Dai Mai is the only Extraordinary Vessel that encircles the waist horizontally, like a "
                 "belt -- binding/controlling all the longitudinally-running meridians."),
        dict(n=16, type="MC",
             q="The Chong Mai is classically described as the \"Sea of\" what?",
             opts=["The Yang Meridians", "The Yin Meridians", "The 12 Meridians / Sea of Blood",
                   "The Zang Organs only"],
             ans="C",
             exp="Chong Mai = Sea of the 12 Meridians and Sea of Blood -- it runs parallel to the Kidney "
                 "meridian and regulates menstruation and Qi-Blood distribution to all 12 primary channels."),
        dict(n=17, type="TF",
             q="True or False: GV (Governor Vessel) is the Sea of the Yin Meridians, and CV (Conception Vessel) is "
             "the Sea of the Yang Meridians.",
             opts=["True", "False"], ans="B",
             exp="Reversed -- GV is the Sea of the YANG Meridians; CV is the Sea of the YIN Meridians."),
    ]),
    ("FIVE SHU POINTS & CONFLUENT POINTS", "Week 9", [
        dict(n=18, type="MC",
             q="Per the Five Shu (Transport) Point system, where are Jing-Well points located and what is their "
             "primary clinical application?",
             opts=["Near the elbow/knee; disorders of the six Fu organs",
                   "Tips of fingers and toes; first aid, clearing heat, resuscitation",
                   "Forearms/lower legs; externally-contracted disease",
                   "Before the MCP/MTP joints; feverish disease"],
             ans="B",
             exp="Jing-Well points sit at the very tips of the fingers/toes -- classically used for first aid, "
                 "resuscitation, and clearing heat/consciousness disorders."),
        dict(n=19, type="MC",
             q="On a YIN meridian, which Five Shu point doubles as the Yuan-Source point?",
             opts=["Jing-Well", "Ying-Spring", "Shu-Stream", "He-Sea"],
             ans="C",
             exp="On Yin channels, the Shu-Stream point IS the Yuan-Source point (e.g. LU9 Taiyuan, HT7 Shenmen, "
                 "SP3 Taibai, KI3 Taixi, PC7 Daling, LR3 Taichong)."),
    ]),
    ("CUMULATIVE / CROSS-WEEK", "Weeks 1-9", [
        dict(n=20, type="MC",
             q="Per Dr. Zhang's own statement, how many questions are on the comprehensive final exam, and what is "
             "their source?",
             opts=["30 questions; entirely new material not covered before",
                   "30 questions; drawn from material \"concerns from each quiz, not new question\"",
                   "50 questions; new plus quiz material mixed evenly",
                   "20 questions; only from the Week 9 review slides"],
             ans="B",
             exp="Dr. Zhang confirmed 30 questions verbally, and separately stated the final \"mentions all the "
                 "questions, including in the final examination, concerns from each quiz, not new question\" -- "
                 "review every quiz you've taken, not just lecture notes."),
    ]),
]

TOTAL_Q = sum(len(qs) for _, _, qs in SECTIONS)
