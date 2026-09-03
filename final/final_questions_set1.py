# AC300 Practice FINAL Exam -- SET 1 (Weeks 1-9, cumulative)
# 20 questions, mixed MC / True-False / EXCEPT format.
# Per Dr. Zhang: the real final draws heavily from quiz material -- these
# items are modeled on that same style and pulled from verified content
# across every week's Cram Sheet / Special Points Decoder.

SECTIONS = [
    ("FOUNDATIONS & THE THREE CIRCUITS", "Week 1", [
        dict(n=1, type="MC",
             q="How many primary (regular) meridians are there, and how many total acupoints across the Five Shu system?",
             opts=["12 meridians; 60 Five Shu points", "14 meridians; 60 Five Shu points",
                   "12 meridians; 72 Five Shu points", "10 meridians; 50 Five Shu points"],
             ans="A",
             exp="12 primary meridians x 5 Five Shu points each = 60 points total. GV and CV also have points, but "
                 "are not part of the 12 x 5 Five Shu system."),
        dict(n=2, type="EXCEPT",
             q="All of the following are true of the direction-of-flow rules EXCEPT:",
             opts=["Yin meridians of the hand run chest -> hand", "Yang meridians of the hand run hand -> head",
                   "Yang meridians of the foot run foot -> head", "Yin meridians of the foot run foot -> chest/abdomen"],
             ans="C",
             exp="Yang meridians of the FOOT run HEAD -> FOOT (descending), not foot -> head. This is the most "
                 "commonly reversed direction rule on exams."),
        dict(n=3, type="MC",
             q="Which circuit is completed first, chronologically, in the course sequence?",
             opts=["Outer/Anterior Circuit (LU-LI-ST-SP)", "Inner/Posterior Circuit (HT-SI-BL-KI)",
                   "Middle Circuit (PC-SJ-GB-LR)", "All three complete simultaneously"],
             ans="A",
             exp="Outer/Anterior (LU/LI/ST/SP, Weeks 2-3) completes first, then Inner/Posterior (HT/SI/BL/KI, "
                 "Weeks 4-5), then Middle (PC/SJ/GB/LR, Week 6)."),
    ]),
    ("LU / LI -- METAL", "Week 2", [
        dict(n=4, type="MC",
             q="LU7 (Lieque) is loaded with which combination of special categories?",
             opts=["He-Sea + Xi-Cleft", "Luo-Connecting + Confluent (opens Ren Mai) + Command (head/neck)",
                   "Jing-Well + Yuan-Source", "Shu-Stream + Back-Shu"],
             ans="B",
             exp="LU7 is Luo-Connecting of LU, the Confluent point opening the Ren Mai (paired with KI6), AND a "
                 "Command Point for the head/neck -- three jobs on one point."),
        dict(n=5, type="TF",
             q="True or False: LI4 (Hegu) and SP6 (Sanyinjiao) are both forbidden in pregnancy.",
             opts=["True", "False"], ans="A",
             exp="Both have strong, descending Qi/Blood-moving actions -- the two classic pregnancy-forbidden "
                 "points from the primary-meridian portion of the course."),
    ]),
    ("ST / SP -- EARTH", "Week 3", [
        dict(n=6, type="MC",
             q="Where does the Stomach channel's pathway TRULY begin, versus its first numbered point?",
             opts=["ST1 Chengqi is the true origin", "LI20 Yingxiang is the true origin; ST1 is just point #1",
                   "GV24 is the true origin", "BL1 is the true origin"],
             ans="B",
             exp="ST originates at LI20 (a crossing point of the LI channel) on the face -- ST1 Chengqi is simply "
                 "the first NUMBERED point along the pathway, a classic exam trap."),
        dict(n=7, type="EXCEPT",
             q="All of the following are true of the Spleen channel's 8-cun crossover with Liver EXCEPT:",
             opts=["It occurs 8 cun above the medial malleolus", "Below 8 cun, SP runs posterior to LR",
                   "Above 8 cun, SP crosses in front of (anterior to) LR",
                   "This same crossover pattern happens on 3 other primary channels"],
             ans="D",
             exp="This 8-cun SP/LR crossover is the ONLY distribution exception among ALL 12 primary meridians -- "
                 "it does not recur elsewhere."),
        dict(n=8, type="MC",
             q="Which channel has the most crossing points of any single primary meridian, and how many?",
             opts=["BL, 14", "GB, 12", "ST, 11", "SJ, 10"],
             ans="C",
             exp="ST has 11 crossing points -- the most of any single primary channel (BL's 14 are shared "
                 "specifically with GV and GB, a different framing)."),
    ]),
    ("HT / SI -- FIRE", "Week 4", [
        dict(n=9, type="MC",
             q="HT7 (Shenmen) holds which dual special-point role, and why is this role predictable?",
             opts=["He-Sea + Luo-Connecting; predictable because HT is Yang",
                   "Shu-Stream + Yuan-Source; predictable because on YIN channels the Shu-Stream point IS the Yuan point",
                   "Jing-Well + Xi-Cleft; predictable because HT is the smallest channel",
                   "Front-Mu + Back-Shu; predictable because HT has no crossing points"],
             ans="B",
             exp="On Yin channels, Shu-Stream and Yuan-Source always coincide at the same point (e.g. HT7, LU9, "
                 "SP3, KI3, PC7, LR3). On Yang channels, Yuan-Source is a separate 6th point."),
        dict(n=10, type="MC",
             q="SI3 (Houxi) is significant because it is:",
             opts=["The Yuan-Source point of SI, opening the Ren Mai",
                   "The Shu-Stream point of SI, also a Confluent point opening the Du Mai (paired with BL62)",
                   "The He-Sea point of SI, opening the Chong Mai",
                   "The Jing-Well point of SI, opening the Yin Wei Mai"],
             ans="B",
             exp="SI3 is SI's Shu-Stream point AND the Confluent point opening the Du Mai, paired with BL62 "
                 "Shenmai (Yang Qiao Mai) -- useful for spine, neck, and febrile conditions."),
    ]),
    ("BL / KI -- WATER", "Week 5", [
        dict(n=11, type="MC",
             q="Which organ does the Bladder channel internally connect with, and which is a common exam trap?",
             opts=["Kidney only; the trap is assuming BL connects to Lung", "Lung and Kidney; no trap exists",
                   "Liver only; the trap is assuming BL connects to Spleen", "Heart; the trap is assuming BL connects to Kidney"],
             ans="A",
             exp="BL's only internal connection is Kidney. Confusing BL with a Metal/Lung pathway is a classic "
                 "verified exam trap."),
        dict(n=12, type="TF",
             q="True or False: The two parallel lines of the Bladder channel on the back run sequentially, one after "
             "the other, rather than at the same time.",
             opts=["True", "False"], ans="B",
             exp="False -- Dr. Zhang confirmed directly in class Q&A that both back lines (1.5 cun and 3 cun "
                 "lateral to the spine) run SIMULTANEOUSLY, not as a sequential up-down loop."),
        dict(n=13, type="MC",
             q="A patient presents with heel pain. Which channel should you think of first, per Dr. Zhang's explicit "
             "clinical teaching point?",
             opts=["Liver", "Kidney", "Bladder", "Spleen"],
             ans="B",
             exp="Kidney -- its pathway curves directly behind the medial malleolus and through the heel; Dr. "
                 "Zhang called this out explicitly as a common clinical presentation."),
    ]),
    ("PC / SJ / GB / LR -- MIDDLE CIRCUIT", "Week 6", [
        dict(n=14, type="MC",
             q="Which TWO primary channels have zero named crossing points?",
             opts=["HT and PC", "LU and LR", "SP and KI", "GB and SJ"],
             ans="A",
             exp="Heart and Pericardium are the only two primary channels with no crossing points -- a classic "
                 "paired exam trap."),
        dict(n=15, type="MC",
             q="The Gallbladder channel's 12 crossing points span how many meridians, and which is the most-forgotten one?",
             opts=["6 meridians; GV14 Dazhui is the most commonly missed",
                   "4 meridians; ST7 is the most commonly missed",
                   "8 meridians; LR13 is the most commonly missed",
                   "6 meridians; SI19 is the most commonly missed"],
             ans="A",
             exp="GB crosses 12 points across 6 meridians (SJ, LR, PC, SI, ST, GV) -- GV14 Dazhui is easy to "
                 "forget since it sits on the posterior midline, away from GB's lateral course."),
    ]),
    ("EIGHT EXTRAORDINARY VESSELS", "Week 7", [
        dict(n=16, type="MC",
             q="Which pair of confluent points is described as the most-used pairing in clinical practice, per Dr. Zhang?",
             opts=["SI3 + BL62 (Du Mai + Yang Qiao)", "LU7 + KI6 (Ren Mai + Yin Qiao)",
                   "SP4 + PC6 (Chong Mai + Yin Wei)", "GB41 + SJ5 (Dai Mai + Yang Wei)"],
             ans="C",
             exp="SP4 Gongsun + PC6 Neiguan (Chong Mai + Yin Wei Mai) is repeatedly flagged as the most-used "
                 "confluent pairing in clinic, treating chest, heart, and stomach disorders together."),
        dict(n=17, type="TF",
             q="True or False: The Eight Extraordinary Vessels have their own pertaining and connecting Zang-Fu organs, "
             "just like the 12 primary meridians.",
             opts=["True", "False"], ans="B",
             exp="False -- the Extraordinary Vessels run superficially and do NOT pertain to or connect with "
                 "internal Zang-Fu organs the way the 12 primary meridians do."),
        dict(n=18, type="MC",
             q="Per Dr. Zhang's own words in the Week 9 review, the Yang Qiao and Yin Qiao vessels each \"start\" at:",
             opts=["Their first numbered coalescent point", "Their respective confluent points, BL62 and KI6",
                   "GV1 and CV1", "The inner canthus of the eye"],
             ans="B",
             exp="Direct quote from the Week 9 review: the Yin Qiao and Yang Qiao vessels' running courses start "
                 "from their confluent points -- BL62 Shenmai (Yang Qiao) and KI6 Zhaohai (Yin Qiao)."),
    ]),
    ("COLLATERALS, DIVERGENT, SINEW & CUTANEOUS", "Week 8-9", [
        dict(n=19, type="MC",
             q="Why are there 15 Luo-Connecting points instead of just 12 (one per primary meridian)?",
             opts=["Because GV, CV, and the Spleen Great Luo each add one more, covering back, front, and lateral chest",
                   "Because each Yin meridian has 2 Luo points",
                   "Because BL and GB each have 2 Luo points due to their size",
                   "There are only 12 -- this is a trick question"],
             ans="A",
             exp="12 paired-meridian Luo points + GV1 (back midline) + CV15 (front midline) + SP21 Dabao, the "
                 "Great/Major Luo of Spleen (lateral chest) = 15 total, giving full front/back/lateral coverage."),
        dict(n=20, type="TF",
             q="True or False: Per Dr. Zhang's explicit statement in the Week 9 final-exam review, Divergent Channels "
             "and Collaterals are heavily emphasized on the final exam.",
             opts=["True", "False"], ans="B",
             exp="False -- Dr. Zhang directly told the class that the review portion of the final does NOT cover "
                 "divergent channels and collaterals in detail. Know the concepts, but they are low-yield versus "
                 "the primary meridian pathways, Five Shu points, and Confluent points."),
    ]),
]

TOTAL_Q = sum(len(qs) for _, _, qs in SECTIONS)
