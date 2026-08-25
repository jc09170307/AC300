"""Week 7 Quiz Kit question bank -- standalone practice exam. Mirrors the
established Quiz Kit format (multiple choice + fill-in + matching + answer
key). Content verified against Lecture_7vivian11_12.pdf and the Week 7
transcript (Dr. Zhang's live Quiz 5 review is folded in as MAINT items)."""

# ---------------------------------------------------------------------------
# SECTION A -- Multiple Choice (vessel identity, sea titles, point counts)
# ---------------------------------------------------------------------------
MC_QUESTIONS = [
    dict(q="Which vessel is described as the \u201csea of the yang meridians\u201d?",
         choices=["Ren Mai (CV)", "Du Mai (GV)", "Chong Mai", "Dai Mai"], answer=1,
         explain="Du Mai (GV) governs the qi of all yang meridians and is the sea of the yang meridians."),
    dict(q="Which vessel is described as the \u201csea of the yin meridians\u201d?",
         choices=["Ren Mai (CV)", "Du Mai (GV)", "Yin Qiao Mai", "Yin Wei Mai"], answer=0,
         explain="Ren Mai (CV) receives and bears the qi of all yin meridians."),
    dict(q="Chong Mai carries three \u201csea of...\u201d titles. Which of the following is NOT one of them?",
         choices=["Sea of the 12 meridians", "Sea of blood", "Sea of the zang-fu organs", "Sea of the yang meridians"],
         answer=3, explain="Chong Mai's three titles are sea of the 12 meridians, sea of blood, and sea of the zang-fu organs -- \u201csea of the yang meridians\u201d belongs to GV."),
    dict(q="How many acupuncture points does the Governor Vessel have?",
         choices=["24", "28", "23", "44"], answer=1, explain="GV runs GV1 Changqiang to GV28 Yinjiao -- 28 points total."),
    dict(q="How many acupuncture points does the Conception Vessel have?",
         choices=["28", "22", "24", "20"], answer=2, explain="CV runs CV1 Huiyin to CV24 Chengjiang -- 24 points total."),
    dict(q="Which TWO vessels are the only ones with their own dedicated acupuncture points?",
         choices=["Chong Mai and Dai Mai", "GV and CV", "Yang Qiao and Yin Qiao", "Yang Wei and Yin Wei"],
         answer=1, explain="Only Du Mai (GV) and Ren Mai (CV) have their own points; the other six share points with primary meridians (coalescent points)."),
    dict(q="What is the ONE structural feature all 8 Extraordinary Vessels share, distinguishing them from the 12 primary meridians?",
         choices=["They all run vertically", "None pertains to a zang or fu organ", "They all have 12 points", "They all start at the fingertips"],
         answer=1, explain="None of the 8 Extraordinary Vessels pertains to a zang/fu organ, and none has an interior-exterior paired relationship."),
    dict(q="Which vessel is the ONLY one of the 8 that runs horizontally rather than vertically?",
         choices=["Chong Mai", "Dai Mai", "Yang Wei Mai", "Ren Mai"], answer=1,
         explain="Dai Mai (Belt Vessel) wraps horizontally around the waist -- structurally unique among the 8."),
    dict(q="\u201cOne source, three branches\u201d (Yi Yuan San Qi) refers to which three vessels?",
         choices=["GV, CV, Dai Mai", "GV, CV, Chong Mai", "Chong, Dai, Wei", "Qiao, Wei, Dai"], answer=1,
         explain="Du, Ren, and Chong Mai all arise from the lower abdomen and emerge together at the perineum before diverging."),
    dict(q="Which vessel governs sleep/wake balance by keeping the body alert and active (as opposed to promoting rest)?",
         choices=["Yin Qiao Mai", "Yang Qiao Mai", "Yin Wei Mai", "Dai Mai"], answer=1,
         explain="Yang Qiao Mai keeps the body awake/active; Yin Qiao Mai promotes calm and restful sleep."),
    dict(q="Which vessel dominates the EXTERIOR of the whole body and connects to all yang meridians?",
         choices=["Yang Wei Mai", "Yin Wei Mai", "Yang Qiao Mai", "Chong Mai"], answer=0,
         explain="Yang Wei Mai connects to all yang meridians (esp. Du) and dominates the exterior of the body."),
    dict(q="Which vessel dominates the INTERIOR of the whole body and connects to all yin meridians?",
         choices=["Yin Qiao Mai", "Yin Wei Mai", "Ren Mai", "Chong Mai"], answer=1,
         explain="Yin Wei Mai connects to all yin meridians (esp. Ren) and dominates the interior of the body."),
]

# ---------------------------------------------------------------------------
# SECTION B -- Confluent Point Matching (the highest-yield content)
# ---------------------------------------------------------------------------
CONFLUENT_MATCH_LEFT = ["1. Du Mai", "2. Ren Mai", "3. Chong Mai", "4. Dai Mai",
                         "5. Yang Qiao Mai", "6. Yin Qiao Mai", "7. Yang Wei Mai", "8. Yin Wei Mai"]
CONFLUENT_MATCH_RIGHT = ["A. SP 4 Gongsun", "B. SI 3 Houxi", "C. LU 7 Lieque", "D. GB 41 Zulinqi",
                          "E. BL 62 Shenmai", "F. KI 6 Zhaohai", "G. SJ 5 Waiguan", "H. PC 6 Neiguan"]
CONFLUENT_MATCH_ANSWER = {"1": "B", "2": "C", "3": "A", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H"}

# ---------------------------------------------------------------------------
# SECTION C -- Fill in the Blank
# ---------------------------------------------------------------------------
FILL_BLANK = [
    ("The Belt Vessel's confluent point is ______, on the Gallbladder meridian.", "GB 41 Zulinqi"),
    ("The confluent point pairing for Du Mai + Yang Qiao Mai is Houxi (SI 3) with ______.", "Shenmai (BL 62)"),
    ("Ren Mai's confluent point Lieque (LU 7) is also the ______ point of the Lung meridian.", "Luo-Connecting"),
    ("Chong Mai's confluent point Gongsun (SP 4) is also the ______ point of the Spleen meridian.", "Luo-Connecting"),
    ("The coalescent points of the Governor Vessel are Fengmen (BL 12) and ______.", "Huiyin (CV 1)"),
    ("The coalescent points of the Conception Vessel are Chengqi (ST 1) and ______.", "Yinjiao (GV 28)"),
    ("Yin Wei Mai's confluent point is Neiguan, ______.", "PC 6"),
    ("The first point of the Governor Vessel is ______, midway between the coccyx tip and the anus.", "GV 1 Changqiang"),
]

# ---------------------------------------------------------------------------
# SECTION D -- Short Answer / Pathology Recognition
# ---------------------------------------------------------------------------
SHORT_ANSWER = [
    dict(q="A patient presents with spinal stiffness, a heavy sensation in the head, and low-grade fever. Which vessel's pathology pattern does this most resemble, and what is its confluent point?",
         answer="Governor Vessel (GV/Du Mai) pathology. Confluent point: SI 3 Houxi."),
    dict(q="A patient presents with irregular menstruation, fullness in the abdomen, and lumbar pain, with no clear up/down directionality to the pain. Which vessel should you consider, and why is the \u201cno clear direction\u201d detail significant?",
         answer="Dai Mai (Belt Vessel) -- it is the only vessel that runs horizontally, so its pathology characteristically lacks the vertical/longitudinal directionality typical of the 12 primary meridians."),
    dict(q="A patient reports chest pain, waist pain, and hard lumps in the upper abdomen. Which vessel's pathology best fits, and what is its confluent point?",
         answer="Yin Wei Mai pathology. Confluent point: PC 6 Neiguan."),
    dict(q="Explain why GV and CV are the only two Extraordinary Vessels that can be point-prescribed independently of a primary meridian.",
         answer="GV and CV are the only two vessels with their own dedicated acupuncture points (28 and 24 respectively); the other six vessels have no points of their own and must be accessed via coalescent points they share with primary meridians, or via their confluent (opening) point."),
]

# ---------------------------------------------------------------------------
# SECTION E -- MAINT (cumulative review, pulled from Dr. Zhang's live Quiz 5
# review in the Week 7 transcript)
# ---------------------------------------------------------------------------
MAINT_QUESTIONS = [
    dict(q="What is the pertaining organ of the Pericardium meridian, and what is its connecting organ?",
         answer="Pertaining organ: Pericardium. Connecting organ: San Jiao (Triple Energizer) -- an interior-exterior (yin-yang) paired relationship."),
    dict(q="The Pericardium meridian has three branches. Name them.",
         answer="Internal branch, superficial branch, and an upper (arm/hand) branch; the meridian starts at the chest and runs to the hand."),
    dict(q="Which primary meridian is the only one that runs across/connects with the external genitalia?",
         answer="The Liver meridian (LR)."),
    dict(q="In the 12-meridian circulation sequence, which meridian does the Liver meridian connect to, closing the cycle?",
         answer="The Lung meridian (LU) -- closing the full 12-meridian circulation sequence."),
    dict(q="Both Hand-Shaoyang and Foot-Shaoyang meridians share a common anatomical pathway. What is it, and why is this clinically useful?",
         answer="Both SJ (Hand-Shaoyang) and GB (Foot-Shaoyang) run across the ear and the lateral side of the head -- combine points from both meridians to treat lateral (Shaoyang-type) headache."),
    dict(q="Where does the Gallbladder meridian of Foot-Shaoyang start and end?",
         answer="Starts at the outer canthus (GB 1 Tongziliao); ends at the tip of the 4th toe (GB 44 Zuqiaoyin)."),
]
