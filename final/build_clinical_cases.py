#!/usr/bin/env python3
import sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Lora', '/home/claude/fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', '/home/claude/fonts/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', '/home/claude/fonts/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', '/home/claude/fonts/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.114, 0.227, 0.369)
GOLD = (0.616, 0.478, 0.216)
RED = (0.627, 0.220, 0.180)
TEAL = (0.106, 0.369, 0.353)
PURPLE = (0.380, 0.180, 0.522)
DARK = (0.15, 0.15, 0.15)
GRAY = (0.40, 0.40, 0.40)
HEADER_H = 44

OUT = "/mnt/user-data/outputs/AC300_Clinical_Reasoning_Cases.pdf"
c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


ML, MR = 36, 36
CW = W - ML - MR
page_num = [1]


def page_bg():
    setfill((1, 1, 1)); c.rect(0, 0, W, H, fill=1, stroke=0)


def header(subtitle=""):
    setfill(NAVY); c.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    setfill(GOLD); c.rect(0, H - HEADER_H, W, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12)
    c.drawString(ML, H - HEADER_H + 15, "AC300 CLINICAL REASONING CASES")
    if subtitle:
        c.setFont("Lora-Italic", 9.5)
        c.drawRightString(W - ML, H - HEADER_H + 15, subtitle[:70])


def footer():
    setstroke(GOLD); c.setLineWidth(0.5)
    c.line(ML, 30, W - ML, 30)
    setfill(GRAY); c.setFont("Lora-Italic", 7.5)
    c.drawCentredString(W / 2, 19, f"AC300/AC375 Clinical Reasoning Cases  \u00b7  VUIM Summer 2026  \u00b7  Page {page_num[0]}")


def new_page(subtitle=""):
    page_bg(); header(subtitle)


def end_page():
    footer(); c.showPage(); page_num[0] += 1


y = [H - HEADER_H - 20]


def ensure_space(needed, subtitle=""):
    if y[0] - needed < 46:
        end_page(); new_page(subtitle); y[0] = H - HEADER_H - 20


def section_bar(text, accent=NAVY, sub=""):
    lines = wrap_words(text, "Lora-Bold", 12.5, CW - (pdfmetrics.stringWidth(sub, "Lora-Italic", 8.5) + 20 if sub else 0))
    line_h = 14
    est_h = len(lines) * line_h + 10
    ensure_space(est_h + 10)
    setfill(accent); c.rect(ML, y[0] - est_h + 5, 3, est_h - 5, fill=1, stroke=0)
    yy = y[0]
    setfill(NAVY); c.setFont("Lora-Bold", 12.5)
    for ln in lines:
        c.drawString(ML + 9, yy - 10, ln); yy -= line_h
    if sub:
        setfill(GRAY); c.setFont("Lora-Italic", 8.5)
        c.drawRightString(ML + CW, y[0] - 10, sub)
    y[0] -= est_h
    setstroke(accent); c.setLineWidth(1.1)
    c.line(ML, y[0] + 2, ML + CW, y[0] + 2)
    y[0] -= 9


def para(text, size=9.2, color=DARK, font="Lora", gap=8):
    lines = wrap_words(text, font, size, CW)
    needed = len(lines) * (size * 1.4) + gap
    ensure_space(needed)
    setfill(color); c.setFont(font, size)
    for ln in lines:
        c.drawString(ML, y[0], ln); y[0] -= size * 1.4
    y[0] -= gap


def case_block(num, level, vignette, prompt, model_answer, accent=NAVY):
    # Reserve room for the whole "setup" (badge + vignette + prompt + the
    # model-answer header) upfront, so a case never starts if there's only
    # enough room for one or two of its pieces -- the answer body can still
    # flow across a page break, but the setup must stay together.
    box_h = 18
    vlines_probe = wrap_words(vignette, "Lora-Italic", 9.3, CW - 14)
    vneeded = len(vlines_probe) * 12.6 + 14
    plines_probe = wrap_words(prompt, "Lora-Bold", 9.6, CW)
    pneeded = len(plines_probe) * 13 + 10
    setup_needed = (box_h + 8) + (vneeded + 8) + (pneeded + 6) + 20 + 24  # +24 safety margin
    ensure_space(setup_needed)

    setfill(accent); c.roundRect(ML, y[0] - box_h + 4, 56, box_h, 3, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 9.5)
    c.drawCentredString(ML + 28, y[0] - 10, f"CASE {num}")
    setfill(GRAY); c.setFont("Lora-Italic", 8.5)
    c.drawString(ML + 66, y[0] - 10, f"SOLO level: {level}")
    y[0] -= box_h + 8

    vlines = wrap_words(vignette, "Lora-Italic", 9.3, CW - 14)
    needed = len(vlines) * 12.6 + 14
    setfill((0.965, 0.967, 0.972)); c.rect(ML, y[0] - needed + 6, CW, needed - 6, fill=1, stroke=0)
    setfill(accent); c.rect(ML, y[0] - needed + 6, 3, needed - 6, fill=1, stroke=0)
    yy = y[0] - 10
    setfill(DARK); c.setFont("Lora-Italic", 9.3)
    for ln in vlines:
        c.drawString(ML + 12, yy, ln); yy -= 12.6
    y[0] -= needed + 8

    plines = wrap_words(prompt, "Lora-Bold", 9.6, CW)
    setfill(NAVY); c.setFont("Lora-Bold", 9.6)
    for ln in plines:
        c.drawString(ML, y[0], ln); y[0] -= 13
    y[0] -= 6

    setfill(TEAL); c.setFont("Lora-Bold", 8.8)
    c.drawString(ML, y[0], "MODEL ANSWER (check your reasoning against this after you've tried it yourself)")
    y[0] -= 14
    alines = wrap_words(model_answer, "Lora", 8.8, CW - 8)
    for ln in alines:
        ensure_space(12.4)
        setfill(DARK); c.setFont("Lora", 8.8)
        c.drawString(ML + 8, y[0], ln); y[0] -= 12.4
    y[0] -= 16
    ensure_space(2)
    setstroke((0.85, 0.85, 0.85)); c.setLineWidth(0.6)
    c.line(ML, y[0] + 8, ML + CW, y[0] + 8)
    y[0] -= 6


# =====================================================================
# INTRO
# =====================================================================
new_page("Why these are different")
y[0] = H - HEADER_H - 20
section_bar("CLINICAL REASONING CASES", accent=PURPLE, sub="Relational & extended-abstract prompts")
para("Every other document in this system is unistructural or multistructural, in SOLO-taxonomy terms -- "
     "recall a fact, identify a point, match a pathway. That's necessary but not sufficient: real clinical "
     "reasoning is RELATIONAL (connecting multiple facts into one coherent picture) and EXTENDED ABSTRACT "
     "(generalizing the pattern to a case you haven't seen before). These five cases are built for that. "
     "There's no multiple choice here -- write or think through your own answer FIRST, then compare it to "
     "the model answer. The gap between your reasoning and the model's is more informative than whether you "
     "got the \u201cright\u201d point.", size=9.2, gap=16)

case_block(
    1, "Relational",
    "A patient presents with low back pain radiating down the posterior leg, worse with cold exposure, "
    "and reports frequent urination with a weak stream.",
    "Walk through your full clinical reasoning: which channel(s) are implicated and why, and which points "
    "would you prioritize -- your answer must reference at least one Five Shu point AND the Back-Shu "
    "concept, not just name a channel.",
    "Posterior leg pain places this on the Bladder (Foot-Taiyang) pathway. Cold-worsened pain plus weak "
    "urination is a Kidney Yang deficiency pattern -- and BL/KI are the paired Water-element channels, so "
    "both are implicated even though only one shows up in the chief complaint. Point selection: BL40 "
    "Weizhong (He-Sea point AND a Command Point for the back -- \u201cback points, look to Weizhong\u201d) "
    "for the local/pathway pain; BL23 Shenshu, the Back-Shu point of the Kidney, to address the underlying "
    "Yang deficiency driving the urinary symptom and cold sensitivity. This is the Back-Shu logic in action: "
    "you're not just needling where it hurts, you're using BL's Back-Shu series to reach Kidney systemically "
    "through a different channel's points.", accent=NAVY)

case_block(
    2, "Relational",
    "A patient's symptoms don't fit one channel: shoulder pain radiating to the thumb, plus intermittent "
    "lower abdominal discomfort with bloating.",
    "Using the circuit hand-off logic (not just \u201cwhich channel runs there\u201d), explain how LU, LI, ST, "
    "and SP could all be relevant to this ONE patient, and name the hand-off points connecting them.",
    "This is the full Anterior/Outer Circuit. Shoulder-to-thumb pain sits on LU (Hand-Taiyin, chest->hand) "
    "-- LU11 is at the thumb. LU hands off to LI at the fingers (LU7 branch meets LI1), and LI runs hand-> "
    "head, ending near the face (LI20). LI20 is also a crossing point where ST begins (ST's pathway truly "
    "starts at LI20, not ST1) -- ST then runs head->foot directly through the abdomen, which is exactly "
    "where the bloating shows up. ST hands off to SP at the toes (ST42/SP1), and SP runs foot->chest, "
    "completing the circuit back near where it started. So a single patient's shoulder pain AND abdominal "
    "bloating aren't necessarily two unrelated complaints -- they can be two points on the same continuous "
    "circuit.", accent=RED)

case_block(
    3, "Extended Abstract",
    "A patient reports irregular menstruation, chronic low back pain, and describes a sensation of \u201cQi "
    "rushing upward\u201d into the chest, worse with stress.",
    "Which Extraordinary Vessel is most implicated, which confluent point pairing would you select, and "
    "explain WHY that pairing works mechanistically -- not just that it's the textbook combination.",
    "\u201cQi rushing upward\u201d plus menstrual irregularity points to Chong Mai -- classically the Sea of "
    "Blood and Sea of the 12 Meridians, and specifically associated with rebellious Qi counterflow. Chong "
    "Mai's confluent point is SP4 Gongsun, paired with PC6 Neiguan (Yin Wei Mai). The pairing isn't "
    "arbitrary: SP4 is ALSO SP's own Luo-Connecting point, and PC6 is ALSO PC's own Luo-Connecting point -- "
    "so this combination doubles up on two mechanisms at once (Luo + Confluent) rather than working through "
    "just one. That's also why Dr. Zhang flags SP4+PC6 as the single most clinically-used confluent pairing: "
    "it treats chest, heart, AND stomach complaints together, which maps directly onto \u201crushing upward "
    "into the chest\u201d as a presenting complaint.", accent=PURPLE)

case_block(
    4, "Extended Abstract",
    "No patient case this time -- a synthesis question instead.",
    "Without looking anything up: name every point that is BOTH a Luo-Connecting point AND a confluent "
    "point opening an Extraordinary Vessel. Then explain why \u201cdouble-duty\u201d points like these are "
    "disproportionately high-yield for exam purposes.",
    "Four points do double duty: LU7 Lieque (Luo of LU, opens Ren Mai), SP4 Gongsun (Luo of SP, opens Chong "
    "Mai), PC6 Neiguan (Luo of PC, opens Yin Wei Mai), and SJ5 Waiguan (Luo of SJ, opens Yang Wei Mai). The "
    "other 4 confluent points -- SI3, BL62, KI6, GB41 -- are NOT simultaneously Luo points of their own "
    "channel. Why these matter disproportionately: a question about any ONE of these 4 points can be asked "
    "from at least two different angles (\u201cwhat's LU's Luo point\u201d vs \u201cwhat opens Ren Mai\u201d) "
    "and both have the same correct answer -- which means they're statistically more likely to appear on any "
    "given exam, in some form, than a point that only belongs to one category.", accent=TEAL)

case_block(
    5, "Relational",
    "A patient has both heel pain and low back pain, and separately mentions feeling anxious and having "
    "trouble sleeping.",
    "Is there a single-channel explanation that accounts for all three complaints, or does this genuinely "
    "require two different channels? Justify your answer using pathway logic, not just symptom-matching.",
    "Heel pain and low back pain alone could both be explained by Kidney (KI's pathway curves directly "
    "behind the medial malleolus and through the heel, and KI/BL are the paired Water channels covering low "
    "back). But anxiety and sleep disruption are not primarily a Kidney presentation in this system -- "
    "that's a Heart pattern (Shen disturbance). The honest answer is that this DOES require two channels: "
    "Kidney for the heel/low-back pathway complaints, and Heart for the sleep/anxiety complaint, "
    "with the Kidney-Heart (Water-Fire) relationship being the physiological reason both can appear "
    "together in the same patient rather than a coincidence. The exam trap this case is built to catch: "
    "forcing every symptom in a vignette into one channel just because two of the three complaints matched "
    "it.", accent=GOLD)

end_page()

c.save()
print("SAVED:", OUT)
