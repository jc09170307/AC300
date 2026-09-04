# THE REAL QUIZ 1-6 -- reconstructed from Dr. Zhang's actual live-class transcripts.
# Every quiz was confirmed at 6 questions (Weeks 4, 6, 7, 8 transcripts all state this
# directly: "just six questions" / "six questions" / "five questions and one more").
#
# VERBATIM = extracted directly from a transcript segment where Dr. Zhang read the
#   actual quiz question and answer back to the class during live review.
# RECONSTRUCTED = the real quiz's topic and count are confirmed, but no review
#   transcript was found -- these are representative questions on the confirmed
#   topics, NOT literal transcriptions of the real quiz text.

REAL_QUIZZES = [
    dict(quiz_n=1, week=1, topic="Channel Theory Foundations", source="RECONSTRUCTED", questions=[
        dict(n=1, q="How many primary (regular) meridians are there?", opts=["8", "12", "14", "15"], ans="B",
             exp="12 Primary Meridians (Jing) -- the main pathways of the channel system."),
        dict(n=2, q="How many Luo-Connecting points (Collaterals) are there in total?", opts=["8", "12", "15", "20"], ans="C",
             exp="15 total: 12 paired-meridian Luo points + GV1 + CV15 + SP21 (Spleen's Great Luo)."),
        dict(n=3, q="How many Zang (Yin) organs pair with primary meridians?", opts=["4", "5", "6", "8"], ans="C",
             exp="6 Zang organs: Lung, Spleen, Heart, Liver, Kidney, Pericardium."),
        dict(n=4, q="Yin meridians of the HAND flow in which direction?", opts=["Hand to chest", "Chest to hand", "Hand to head", "Head to hand"], ans="B",
             exp="Yin meridians of the hand flow chest -> hand."),
        dict(n=5, q="Yang meridians of the FOOT flow in which direction?", opts=["Foot to head", "Head to foot", "Foot to chest", "Chest to foot"], ans="B",
             exp="Yang meridians of the foot flow head -> foot (descending)."),
        dict(n=6, q="How many Eight Extraordinary Vessels are there?", opts=["6", "8", "10", "12"], ans="B",
             exp="8 Extraordinary Vessels, distinct from the 12 primary meridians."),
    ]),
    dict(quiz_n=2, week=2, topic="LU / LI -- Metal", source="RECONSTRUCTED", questions=[
        dict(n=1, q="How many points does the LU channel have?", opts=["9", "11", "14", "20"], ans="B",
             exp="LU has 11 points (LU1-LU11)."),
        dict(n=2, q="How many points does the LI channel have?", opts=["11", "14", "19", "20"], ans="D",
             exp="LI has 20 points (LI1-LI20) -- nearly double LU's count."),
        dict(n=3, q="What element do LU and LI both belong to?", opts=["Earth", "Fire", "Metal", "Water"], ans="C",
             exp="LU and LI are the Metal pair."),
        dict(n=4, q="Direction of Qi flow in the LU meridian?", opts=["Hand to chest", "Chest to hand", "Hand to head", "Head to hand"], ans="B",
             exp="LU is Hand-Yin: flows chest -> hand."),
        dict(n=5, q="Peak Qi activity of the Lung meridian is:", opts=["3-5 AM", "5-7 AM", "7-9 AM", "9-11 AM"], ans="A",
             exp="LU peaks 3-5 AM, the first channel in the 24-hour clock cycle."),
        dict(n=6, q="LU4 is loaded with which special category?", opts=["Xi-Cleft", "Luo-Connecting", "Yuan-Source", "He-Sea"], ans="A",
             exp="LU6 Kongzui is LU's Xi-Cleft point (used for acute Lung conditions)."),
    ]),
    dict(quiz_n=3, week=3, topic="ST / SP -- Earth", source="RECONSTRUCTED", questions=[
        dict(n=1, q="Direction of Qi in the 3 foot-YANG meridians?", opts=["Foot to chest", "Foot to head", "Head to foot", "Chest to foot"], ans="C",
             exp="Foot Yang meridians flow head -> foot (descending)."),
        dict(n=2, q="Which element do ST and SP both belong to?", opts=["Earth", "Fire", "Metal", "Wood"], ans="A",
             exp="ST and SP are the Earth pair -- interior-exterior partners of the Anterior Circuit."),
        dict(n=3, q="The CONNECTING organ of the Stomach meridian is:", opts=["Large Intestine", "Kidney", "Liver", "Spleen"], ans="D",
             exp="ST pertains to Stomach, connects with Spleen (Yin-Yang interior-exterior pair)."),
        dict(n=4, q="Where does the ST channel's pathway truly begin?", opts=["ST1 Chengqi", "LI20 Yingxiang", "GV24", "BL1"], ans="B",
             exp="ST originates at LI20 on the face -- ST1 is just the first NUMBERED point."),
        dict(n=5, q="How many points does the ST channel have?", opts=["21", "45", "20", "11"], ans="B",
             exp="ST has 45 points -- the most of any primary channel."),
        dict(n=6, q="SP is the only channel on which surface of the tongue?", opts=["Root", "Upper", "Lower", "Lateral edge"], ans="C",
             exp="SP spreads over the LOWER surface of the tongue; KI reaches the root."),
    ]),
    dict(quiz_n=4, week=5, topic="BL / KI -- Water", source="VERBATIM", questions=[
        dict(n=1, type="EXCEPT",
             q="The Kidney meridian internally connects with all of the following organs EXCEPT:",
             opts=["Kidney (itself)", "Bladder", "Liver", "Spleen"], ans="D",
             exp="Dr. Zhang, live review: KI connects internally with Kidney, Bladder, Liver, and Lung -- but NOT Spleen. "
                 "\u201cIt's special for kidney because it's a root of our source in the body... connecting not only the "
                 "kidney, the bladder, but also the liver, the lung, but not all organs, just kidney, bladder, liver, and lung.\u201d"),
        dict(n=2, q="What is the connecting (paired) organ of the Kidney meridian?",
             opts=["Stomach", "Bladder", "Liver", "Spleen"], ans="B",
             exp="Dr. Zhang, live review: \u201cWhich of the following option is the connecting organ of the kidney? "
                 "Its paired organ is bladder, and its pertaining organ is kidney.\u201d"),
        dict(n=3, q="Per its running course, the Bladder meridian of Foot-Taiyang begins at:",
             opts=["BL1, inner canthus of the eye", "BL67, little toe", "GV14", "BL13"], ans="A",
             exp="Dr. Zhang, live review: \u201cthe bladder meridian of foot Taiyang begins... at BL1, in the inner canthus.\u201d"),
        dict(n=4, type="EXCEPT",
             q="Which of the following statements about the Kidney meridian's internal connections is NOT correct?",
             opts=["It connects with Kidney", "It connects with Bladder, Liver, and Lung",
                   "It connects with all 12 Zang-Fu organs", "It does not connect with Spleen"], ans="C",
             exp="Dr. Zhang, live review: reinforces that KI connects with Kidney/Bladder/Liver/Lung specifically -- "
                 "not with all Zang-Fu organs."),
        dict(n=5, q="Per its running course, the Kidney meridian of Foot-Shaoyin begins at:",
             opts=["The inner canthus", "Below the little toe, on the sole of the foot", "GV20", "The nipple"], ans="B",
             exp="Dr. Zhang, live review: \u201cthe kidney meridian of foot Shaoyin begins at the inferior aspect of the "
                 "little toe\u201d -- i.e. KI1 Yongquan, below the little toe on the sole."),
        dict(n=6, q="(Supplementary) The Bladder meridian of Foot-Taiyang ENDS at:",
             opts=["BL1, inner canthus", "The lateral tip of the little toe", "GV14", "The nipple"], ans="B",
             exp="Dr. Zhang, live review, bonus question: \u201cthe bladder meridian... at the lateral side of the tip "
                 "of the little toe\u201d -- BL67 Zhiyin."),
    ]),
    dict(quiz_n=5, week=6, topic="PC / SJ / GB / LR -- Middle Circuit", source="VERBATIM", questions=[
        dict(n=1, q="Where does the Pericardium meridian of Hand-Jueyin start?",
             opts=["The chest", "The hand", "The head", "The foot"], ans="A",
             exp="Dr. Zhang, live review: \u201cOnly three Yin meridians start from the chest to the hand... the "
                 "Pericardium meridian of hand [Jueyin] started from the chest.\u201d"),
        dict(n=2, q="Which meridian is specifically associated with the external genitalia?",
             opts=["Gallbladder", "San Jiao", "Liver", "Pericardium"], ans="C",
             exp="Dr. Zhang, live review: the Liver meridian's specific points connect with the external genitalia -- "
                 "clinically used for genital pain."),
        dict(n=3, q="Where does the Gallbladder meridian of Foot-Shaoyang end?",
             opts=["The inner canthus", "The tip of the fourth toe", "The tip of the little toe", "The nipple"], ans="B",
             exp="Dr. Zhang, live review: GB \u201cis ending on the tip of the fourth toe, only fourth toe.\u201d"),
        dict(n=4, q="The Liver meridian connects with which meridian, completing the 12-channel cycle?",
             opts=["Lung", "Heart", "Kidney", "Stomach"], ans="A",
             exp="Dr. Zhang, live review: \u201cthe liver meridian connects with the [Lung] meridian of hand Taiyin\u201d -- "
                 "closing the loop back to the first channel."),
        dict(n=5, q="Which pair of meridians runs in front of the ear, at the lateral side of the head?",
             opts=["Taiyang (Hand + Foot)", "Yangming (Hand + Foot)", "Shaoyang (Hand + Foot)", "Jueyin (Hand + Foot)"], ans="C",
             exp="Dr. Zhang, live review: \u201cthe Shao Yang meridians, both hand and foot... runs across the ear.\u201d"),
        dict(n=6, q="(Supplementary) The Liver meridian does NOT connect with which organ?",
             opts=["Gallbladder", "Lung", "Heart", "Stomach (via its eye branch)"], ans="C",
             exp="Dr. Zhang, live review: LR connects with Gallbladder, Lung, and has an eye-system branch -- "
                 "\u201cit does not connect with the heart.\u201d"),
    ]),
    dict(quiz_n=6, week=7, topic="Eight Extraordinary Vessels", source="VERBATIM", questions=[
        dict(n=1, q="Which vessel is described as the belt that runs around the waist?",
             opts=["Chong Mai", "Ren Mai", "Dai Mai", "Du Mai"], ans="C",
             exp="Dr. Zhang, live review: \u201cwhich belt is called belt around the waist? The Dai meridian.\u201d"),
        dict(n=2, type="TF", q="True or False: The Dai Mai is the only Extraordinary Vessel that runs horizontally.",
             opts=["True", "False"], ans="A",
             exp="Dr. Zhang, live review: \u201cthe Dai meridian is the only one that runs horizontally... right.\u201d"),
        dict(n=3, q="Which two vessels have a confluent point that is also their starting point?",
             opts=["Ren Mai and Du Mai", "Chong Mai and Dai Mai", "Yang Qiao Mai and Yin Qiao Mai", "Yang Wei Mai and Yin Wei Mai"], ans="C",
             exp="Dr. Zhang, live review: \u201cwhich two meridians have a confluent point that's the same as a "
                 "starting point? [Yang] Qiao and Yin Qiao.\u201d"),
        dict(n=4, q="Which three vessels share the lower abdomen as their common point of origin?",
             opts=["Du Mai, Dai Mai, and the Bladder meridian", "Ren Mai, Chong Mai, and Du Mai",
                   "Yang Wei Mai, Yin Wei Mai, and Dai Mai", "Ren Mai, Dai Mai, and the Kidney meridian"], ans="B",
             exp="Dr. Zhang, live review: Ren Mai, Chong Mai, and Du Mai (\u201cone source, three branches\u201d) all "
                 "originate in the lower abdomen/uterus region."),
        dict(n=5, q="Which vessel is called the Sea of the Yang Meridians?",
             opts=["Ren Mai", "Chong Mai", "Dai Mai", "Du Mai"], ans="D",
             exp="Dr. Zhang, live review, closing question: Du Mai (Governor Vessel) is the Sea of the Yang Meridians."),
        dict(n=6, q="(Supplementary) Which vessel is called the Sea of the Yin Meridians?",
             opts=["Ren Mai", "Chong Mai", "Yin Qiao Mai", "Yin Wei Mai"], ans="A",
             exp="Ren Mai (Conception Vessel) is the paired counterpart -- Sea of the Yin Meridians."),
    ]),
]
