"""Week 9 Quiz Kit question bank -- Five Shu Points, Confluent Points, 15
Collaterals, Cutaneous Regions, Final Exam Master Table."""

MC_QUESTIONS = [
    dict(q="Which Five Shu point category is located at the tips of the fingers and toes?",
         choices=["Jing-Well", "Ying-Spring", "Shu-Stream", "He-Sea"], answer=0,
         explain="Jing-Well points sit at the fingertips/toe-tips -- \u201cwhere it emerges.\u201d"),
    dict(q="Which Five Shu point category treats disorders of the six Fu (hollow) organs?",
         choices=["Jing-Well", "Ying-Spring", "Jing-River", "He-Sea"], answer=3,
         explain="He-Sea points, near the elbow/knee, treat Fu-organ disorders and rebellious Qi."),
    dict(q="What is the Shu-Stream point of the Lung meridian, and what special role does it also hold?",
         choices=["Taiyuan LU9 -- also the Yuan-Source point", "Chize LU5 -- also the He-Sea point",
                   "Shaoshang LU11 -- also the Jing-Well point", "Lieque LU7 -- also the Luo point"], answer=0,
         explain="For Yin meridians, the Shu-Stream point doubles as the Yuan-Source point (Taiyuan LU9 for Lung)."),
    dict(q="Which point is the Confluent (opening) point of the Chong Vessel?",
         choices=["Houxi SI3", "Gongsun SP4", "Zulinqi GB41", "Waiguan SJ5"], answer=1,
         explain="Gongsun SP4 opens the Chong Vessel; its master-couple partner is Neiguan PC6 (Yin Wei Vessel)."),
    dict(q="Houxi (SI3) and Shenmai (BL62) form a master couple that treats which shared body region?",
         choices=["Chest and stomach", "Inner canthus, ear, shoulder, neck", "Lower abdomen", "Outer canthus and cheek"],
         answer=1, explain="Houxi (Du Vessel) + Shenmai (Yang Qiao Vessel) share the inner canthus/ear/shoulder/neck region."),
    dict(q="Which meridian's Luo-Connecting point is Guangming GB37?",
         choices=["Liver", "Gallbladder", "Bladder", "Sanjiao"], answer=1,
         explain="Guangming GB37 is the Gallbladder's Luo point, connecting to the Liver meridian."),
    dict(q="Which of the 15 Collaterals is NOT tied to a paired organ meridian?",
         choices=["Lieque LU7", "Tongli HT5", "The Major Collateral of the Spleen (Dabao SP21)", "Waiguan SJ5"],
         answer=2, explain="The Major Collateral of the Spleen, plus the CV and GV collaterals, are the 3 'extra' collaterals -- not paired-organ Luo points."),
    dict(q="What is the originating point of the Governor Vessel's collateral?",
         choices=["Jiuwei CV15", "Changqiang GV1", "Dabao SP21", "Guanyuan CV4"], answer=1,
         explain="The GV collateral arises from Changqiang GV1 in the perineum."),
    dict(q="Why do Cutaneous Regions form only 6 groups instead of 12?",
         choices=["They only cover the Yang meridians", "The Hand and Foot meridian of the same name (e.g. both Taiyang) merge into one region",
                   "They only cover the trunk, not the limbs", "Extraordinary Vessels replace half of them"], answer=1,
         explain="Cutaneous Regions are the exception that connects Hand+Foot meridians of the same name into one continuous region."),
    dict(q="Per the diagnostic color rule from Su Wen Ch. 56, what does blue-colored skin signify?",
         choices=["Heat syndrome", "Cold syndrome", "Local pain", "Blockage of qi and blood"], answer=2,
         explain="Blue skin = local pain; dark = qi/blood blockage; yellow-red = heat; white = cold."),
    dict(q="What is the pertaining organ and first point of the Kidney meridian?",
         choices=["Kidney; Yongquan KI1 (sole)", "Bladder; Jingming BL1", "Kidney; Taixi KI3", "Liver; Dadun LR1"], answer=0,
         explain="Kidney meridian pertains to the Kidney and begins at Yongquan KI1 on the sole of the foot."),
    dict(q="Which meridian is the ONLY one that connects to both the inner AND outer canthus of the eye?",
         choices=["Bladder", "Gallbladder", "Small Intestine", "Stomach"], answer=2,
         explain="Small Intestine sends a branch to the outer canthus and another below the eye to the inner canthus."),
    dict(q="What is the direction of Qi flow for the Yang meridians of the foot?",
         choices=["Chest to hand", "Hand to head", "Head to foot", "Foot to abdomen"], answer=2,
         explain="Yang meridians of the foot descend head -> foot, closing with the Yin meridians of the foot."),
    dict(q="Which meridian has the highest total point count, and why?",
         choices=["Gallbladder (44 pts) -- zig-zag head pathway", "Bladder (67 pts) -- 4 branches, largest meridian",
                   "Stomach (45 pts) -- longest running course", "Large Intestine (20 pts) -- most branches"], answer=1,
         explain="Bladder has 67 points across 4 branches -- the largest meridian in the body."),
    dict(q="Per Dr. Zhang's PCOS/PMOS protocol, what was the reported change in HOMA-IR (insulin resistance)?",
         choices=["No significant change", "5.26 to 2.89 (p<0.05)", "2.89 to 5.26 (worsened)", "Not measured in this study"],
         answer=1, explain="HOMA-IR improved from 5.26 to 2.89 (p<0.05) after the acupuncture protocol."),
    dict(q="In the JAMA 2017 urinary incontinence RCT, which points were used for electroacupuncture?",
         choices=["CV4 and CV6", "BL33 and BL35 (bilateral)", "SP6 and ST36", "GV20 and CV4"], answer=1,
         explain="Bilateral Zhongliao (BL33) and Huiyang (BL35), lumbosacral electroacupuncture, per Liu Z et al., JAMA 2017."),
]

FIVESHU_MATCH_LEFT = ["Lung (LU)", "Heart (HT)", "Pericardium (PC)", "Stomach (ST)", "Gallbladder (GB)",
                        "Kidney (KI)", "Liver (LR)", "Bladder (BL)", "Spleen (SP)", "Sanjiao (SJ)"]
FIVESHU_MATCH_RIGHT = ["Taiyuan LU9", "Shenmen HT7", "Daling PC7", "Chongyang ST42 (Yuan, 6th pt)", "Qiuxu GB40 (Yuan, 6th pt)",
                         "Taixi KI3", "Taichong LR3", "Jinggu BL64 (Yuan, 6th pt)", "Taibai SP3", "Yangchi SJ4 (Yuan, 6th pt)"]
FIVESHU_MATCH_ANSWER = {
    "Lung (LU)": "Taiyuan LU9", "Heart (HT)": "Shenmen HT7", "Pericardium (PC)": "Daling PC7",
    "Stomach (ST)": "Chongyang ST42 (Yuan, 6th pt)", "Gallbladder (GB)": "Qiuxu GB40 (Yuan, 6th pt)",
    "Kidney (KI)": "Taixi KI3", "Liver (LR)": "Taichong LR3", "Bladder (BL)": "Jinggu BL64 (Yuan, 6th pt)",
    "Spleen (SP)": "Taibai SP3", "Sanjiao (SJ)": "Yangchi SJ4 (Yuan, 6th pt)",
}

FILL_BLANK = [
    ("The Five Shu Points, in order from fingertip/toe-tip toward the elbow/knee, are: Jing-Well, ______, Shu-Stream, Jing-River, and He-Sea.", "Ying-Spring"),
    ("The Confluent point that opens the Yin Wei Vessel is ______.", "Neiguan (PC 6)"),
    ("The Major Collateral of the Spleen originates at ______ and is named ______.", "Dabao (SP 21)"),
    ("Yin meridians have no separate Yuan-Source point because the ______ point doubles as the Yuan point.", "Shu-Stream"),
    ("The Belt (Dai) Vessel is unique among the 8 Extraordinary Vessels because it runs ______ rather than up/down the body.", "horizontally around the waist"),
    ("Du, Ren, and Chong vessels are called \u201cone source, ______ branches\u201d because all three begin in the lower abdomen.", "three"),
    ("The Gallbladder meridian's first point is Tongziliao GB1, located at the ______.", "outer canthus"),
    ("PCOS was renamed ______ in 2026 to highlight the central role of metabolic dysfunction.", "PMOS (Polyendocrine Metabolic Ovarian Syndrome)"),
]

SHORT_ANSWER = [
    dict(q="Explain the \u201cLi / He / Chu / Ru\u201d framework used to describe a Divergent Channel's pathway.",
         answer="Li = where it begins; He = which organs/systems it connects with internally; Chu = where it exits back to the surface; Ru = where it merges back into a primary meridian (always a Yang meridian)."),
    dict(q="Why does Dr. Zhang alternate two acupuncture protocols across the PCOS/PMOS treatment course rather than using one fixed point set?",
         answer="The 'Phlegm-Dampness Obesity' framework addresses two different mechanisms in sequence -- one protocol emphasizes tonifying Kidney/regulating the Belt Vessel and activating blood, the other strengthens Spleen and drains dampness -- alternating gives broader multisystem coverage than either alone."),
    dict(q="State the eye-relationship rule for the Bladder and Gallbladder meridians and explain why it is a common exam trap.",
         answer="Bladder starts at the INNER canthus (BL1); Gallbladder starts at the OUTER canthus (GB1) -- students commonly swap these because both are Foot-Yang meridians beginning near the eye."),
    dict(q="Why are Extraordinary Vessels said to have 'no pertaining or connecting organ'?",
         answer="Unlike the 12 Primary Meridians, the 8 Extraordinary Vessels have no direct internal Zang-Fu branch -- their pathway stays superficial (nape, vertex, hip, etc.), so they cannot 'pertain to' or 'connect with' an organ the way a primary meridian does."),
]

MAINT_QUESTIONS = [
    dict(q="(Week 6/7 review) Name the Front-Mu point of the Liver.", answer="Qimen (LR 14)."),
    dict(q="(Week 6 review) Name the He-Sea point of the Gallbladder meridian.", answer="Yanglingquan (GB 34)."),
    dict(q="(Week 7 review) Which Confluent point opens the Chong Vessel, and what is its master-couple partner?", answer="Gongsun (SP 4); partner is Neiguan (PC 6)."),
    dict(q="(Week 8 review) What are the 3 extra Collaterals not tied to a paired-organ meridian?", answer="Conception Vessel (CV15), Governor Vessel (GV1), Major Collateral of the Spleen (SP21)."),
]
