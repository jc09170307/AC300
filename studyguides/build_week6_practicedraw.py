#!/usr/bin/env python3
"""AC300 Week 6 Practice Draw -- PC, SJ, GB, LR. Production-recall pages:
faint MOA+CAM tracing guides with a checklist, then a blank dot-grid page
for drawing from memory. Matches Week 5's exact layout. Print + reMarkable."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

sys.path.insert(0, "/home/claude/work")
from wk6_content import PC_META, SJ_META, GB_META, LR_META

FIGS_DIR = "/home/claude/work/figs_faint"
FONT_DIR = "/home/claude/work/fonts"
pdfmetrics.registerFont(TTFont('Lora', f'{FONT_DIR}/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Bold', f'{FONT_DIR}/Lora-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora-Italic', f'{FONT_DIR}/Lora-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lora-BoldItalic', f'{FONT_DIR}/Lora-BoldItalic.ttf'))

W, H = letter
NAVY = (0.176, 0.271, 0.412)
GOLD = (0.616, 0.478, 0.216)
DARK = (0.12, 0.12, 0.12)
GRAY = (0.40, 0.40, 0.40)
CREAM = (0.970, 0.940, 0.860)
TEAL = (0.118, 0.435, 0.400)

EDITION = sys.argv[1] if len(sys.argv) > 1 else "print"
IS_RM = EDITION == "remarkable"
LW_MULT = 1.35 if IS_RM else 1.0

if IS_RM:
    PAGE_BG = (0.98, 0.965, 0.93)
    OUT = "/mnt/user-data/outputs/AC300_Week6_PracticeDraw_reMarkable.pdf"
    EDLABEL = "reMarkable Edition"
else:
    PAGE_BG = (1, 1, 1)
    OUT = "/mnt/user-data/outputs/AC300_Week6_PracticeDraw_Print.pdf"
    EDLABEL = "Print Edition"

c = canvas.Canvas(OUT, pagesize=letter)


def setfill(rgb): c.setFillColorRGB(*rgb)
def setstroke(rgb): c.setStrokeColorRGB(*rgb)


def wrap_words(text, font, size, max_width):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = wd
    if cur: lines.append(cur)
    return lines


ML, MR = 42, 42
RX = W - MR
CW = RX - ML
page_num = [1]


def page_bg():
    setfill(PAGE_BG); c.rect(0, 0, W, H, fill=1, stroke=0)


def top_bar():
    setfill(DARK); c.setFont("Lora", 8.5)
    c.drawString(ML, H - 30.3, "AC300/AC375  |  Acupuncture Channels & Points I  |  VUIM Summer 2026")
    setfill(GOLD); c.setFont("Lora-Italic", 8.5)
    c.drawRightString(RX, H - 30.3, EDLABEL)
    setstroke(GOLD); c.setLineWidth(0.6 * LW_MULT)
    c.line(ML, H - 38, RX, H - 38)


def bottom_bar(label):
    setfill(NAVY); c.rect(0, 0, W, 26, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora", 8)
    c.drawString(ML, 10, label)
    c.drawRightString(RX, 10, f"p.{page_num[0]}")


def new_page():
    page_bg(); top_bar()


def end_page(label):
    bottom_bar(label); c.showPage(); page_num[0] += 1


WEEK_LABEL = "AC300/AC375 | Week 6 | PC, SJ, GB, LR Channels | VUIM Summer 2026"


def title_bar(title, subtitle_right, color=TEAL):
    bar_top = H - 46
    bar_bot = H - 74
    setfill(color); c.rect(ML, bar_bot, CW, bar_top - bar_bot, fill=1, stroke=0)
    setfill((1, 1, 1)); c.setFont("Lora-Bold", 12.5)
    c.drawString(ML + 14, bar_bot + 9, title)
    if subtitle_right:
        c.setFont("Lora-Italic", 9)
        c.drawRightString(RX - 6, bar_bot + 10, subtitle_right)
    return bar_bot


def instruction_box(y, lines):
    box_h = 14 + len(lines) * 13
    setfill(CREAM); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
    setfill(DARK); c.setFont("Lora-Italic", 8.6)
    yy = y - 15
    for l in lines:
        c.drawString(ML + 8, yy, l); yy -= 13
    return y - box_h - 12


_img_size_cache = {}


def get_img_size(fig_key):
    if fig_key not in _img_size_cache:
        with Image.open(f"{FIGS_DIR}/{fig_key}.jpeg") as im:
            _img_size_cache[fig_key] = im.size
    return _img_size_cache[fig_key]


def draw_image_contain(fig_key, x, y_top, box_w, box_h):
    iw, ih = get_img_size(fig_key)
    scale = min(box_w / iw, box_h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (box_w - dw) / 2
    dy = y_top - dh
    c.drawImage(ImageReader(f"{FIGS_DIR}/{fig_key}.jpeg"), dx, dy, width=dw, height=dh)
    return dy


def practice_draw_page(name, subtitle_right, color, checklist, fig_moa, fig_cam):
    new_page()
    y = title_bar(f"Practice Draw \u2014 {name}", subtitle_right, color)
    y = instruction_box(y - 10, [
        "Dr. Zhang's rule: draw BOTH internal AND external pathways from memory.",
        "The faint figure is a guide only \u2014 trace, then check against the Study Guide overview pages.",
    ])
    checklist_w = 190
    setfill((0.945, 0.966, 0.964)); c.rect(ML, 40, checklist_w, y - 40, fill=1, stroke=0)
    setfill(TEAL); c.setFont("Lora-Bold", 9)
    c.drawString(ML + 8, y - 14, "CHECKLIST")
    cy = y - 30
    setfill(DARK); c.setFont("Lora", 8.4)
    for i, item in enumerate(checklist, 1):
        lines = wrap_words(f"{i}. {item}", "Lora", 8.4, checklist_w - 16)
        for l in lines:
            c.drawString(ML + 8, cy, l); cy -= 10.4
        cy -= 3

    img_x = ML + checklist_w + 16
    img_w = RX - img_x
    half_h = (y - 40 - 20) / 2
    top_bottom = draw_image_contain(fig_moa, img_x, y, img_w, half_h)
    draw_image_contain(fig_cam, img_x, top_bottom - 14, img_w, half_h)
    setfill(GRAY); c.setFont("Lora-Italic", 7.6)
    c.drawCentredString(img_x + img_w / 2, 44, "TOP: MOA (internal)  |  BOTTOM: CAM (external) \u2014 trace, label, check")
    end_page(WEEK_LABEL)


def draw_dot_grid(x, y_top, w, h):
    setstroke((0.70, 0.70, 0.70)); c.setLineWidth(0.7 * LW_MULT)
    c.rect(x, y_top - h, w, h, fill=0, stroke=1)
    setfill((0.91, 0.91, 0.91))
    spacing = 24
    yy = y_top - 24.6
    while yy > y_top - h:
        xx = x + 23.4
        while xx < x + w:
            c.circle(xx, yy, 0.6, fill=1, stroke=0)
            xx += spacing
        yy -= spacing


def blank_recall_page(name, color):
    new_page()
    y = title_bar(f"Blank Recall \u2014 {name}", "Pass 2 \u2014 from memory", color)
    y = instruction_box(y - 10, [
        "PASS 2: no guide figure. Draw the full pathway from memory, then check yourself against the",
        "Study Guide overview pages. Label at least the special points (Yuan-Source, Luo, He-Sea, etc.).",
    ])
    draw_dot_grid(ML, y, CW, y - 40)
    end_page(WEEK_LABEL)


# ============================================================
# COVER
# ============================================================
new_page()
y = H - 60
setfill(NAVY); c.setFont("Lora-Bold", 28)
c.drawCentredString(W / 2, y, "Practice Draw")
y -= 26
setfill((0.753, 0.224, 0.161)); c.setFont("Lora-BoldItalic", 15)
c.drawCentredString(W / 2, y, "Pericardium, San Jiao, Gallbladder & Liver Channels \u2014 Week 6")
y -= 20
setfill(GOLD); c.setFont("Lora-BoldItalic", 11)
c.drawCentredString(W / 2, y, "Production recall \u2014 draw it cold, then check")
y -= 18
setstroke(GOLD); c.setLineWidth(1.2)
c.line(ML + 40, y, RX - 40, y)
y -= 26

setfill(DARK); c.setFont("Lora", 10.5)
for l in wrap_words("Recognizing the right MCQ answer and producing a pathway from memory are different skills. Dr. Zhang's homework rule: draw BOTH the internal AND external pathways for every meridian -- most students only draw the external. Use the faint figure as a guide only: trace it once to build muscle memory, then try the blank version from memory and check yourself against the Study Guide.", "Lora", 10.5, CW):
    c.drawString(ML, y, l); y -= 13.5
y -= 12

box_h = 40
setfill(CREAM); c.rect(ML, y - box_h, CW, box_h, fill=1, stroke=0)
setfill(DARK); c.setFont("Lora-Italic", 9)
c.drawString(ML + 14, y - 16, "\"PC/SJ/GB/LR each get a full practice pass this week.\"")
c.drawString(ML + 14, y - 30, "Two passes per channel: (1) trace the faint figure, (2) redraw from memory on blank paper.")
y -= box_h + 30

setfill(GRAY); c.setFont("Lora-Italic", 8.5)
c.drawCentredString(W / 2, 40, "AC300 Practice Draw \u00b7 Week 6 \u00b7 pairs with the Study Guide")
end_page(WEEK_LABEL)


# ============================================================
# CHANNEL PAGES
# ============================================================
MINISTER = (0.80, 0.40, 0.36)
WOOD = (0.20, 0.48, 0.27)

practice_draw_page("The Pericardium Meridian of Hand-Jueyin", "9 points | 2 branches | chest to hand", MINISTER,
    ["Draw the INTERNAL pathway (dotted): chest -> Pericardium -> San Jiao (upper/middle/lower)",
     "Draw the EXTERNAL pathway (solid): PC1 (chest) -> axilla -> PC3 (elbow) -> PC7 (wrist) -> PC8 (palm) -> PC9 (fingertip)",
     "Mark the branch: PC8 -> ring finger tip -> links with SJ",
     "Label special points: PC7 (Yuan+Shu), PC6 (Luo+Confluent), PC3 (He-Sea), PC4 (Xi-Cleft)",
     "Note: ZERO crossing points -- nothing else to mark on this channel"],
    "MOA_PC", "CAM_PC")
blank_recall_page("The Pericardium Meridian of Hand-Jueyin", MINISTER)

practice_draw_page("The San Jiao Meridian of Hand-Shaoyang", "23 points | 2 branches | hand to head", MINISTER,
    ["Draw the INTERNAL pathway: chest -> San Jiao (upper/middle/lower) -> connects with Pericardium",
     "Draw the EXTERNAL pathway: SJ1 (ring finger) -> wrist -> elbow -> shoulder (crosses behind GB) -> SJ17/21 (ear) -> SJ23 (eyebrow)",
     "Mark where SJ crosses GB TWICE at the shoulder region",
     "Label special points: SJ4 (Yuan), SJ5 (Luo+Confluent, opens Yang Wei Mai), SJ10 (He-Sea)",
     "Mark the branch to the outer canthus, linking with GB"],
    "MOA_SJ", "CAM_SJ")
blank_recall_page("The San Jiao Meridian of Hand-Shaoyang", MINISTER)

practice_draw_page("The Gallbladder Meridian of Foot-Shaoyang", "44 points | 5 branches | head to foot", WOOD,
    ["Draw the zigzag HEAD course first (GB1 -> GB4 -> GB20) -- this is GB's signature feature",
     "Draw the INTERNAL pathway: supraclavicular fossa -> diaphragm -> Liver -> Gallbladder -> hip (GB30)",
     "Draw the EXTERNAL/straight pathway: shoulder -> axilla -> floating ribs (GB24-25) -> hip -> knee -> GB34 -> GB40 -> GB44",
     "Mark GB21 with a warning symbol (FORBIDDEN in pregnancy)",
     "Label special points: GB34 (He-Sea + Hui-Meeting Sinews), GB40 (Yuan), GB41 (Confluent, opens Dai Mai)",
     "Mark the branch: dorsum of foot -> great toe -> links with LR"],
    "MOA_GB", "CAM_GB")
blank_recall_page("The Gallbladder Meridian of Foot-Shaoyang", WOOD)

practice_draw_page("The Liver Meridian of Foot-Jueyin", "14 points | 3 branches | foot to chest", WOOD,
    ["Draw the INTERNAL pathway: foot -> 8 cun above medial malleolus (crosses IN FRONT of SP here) -> genitals -> Liver -> Gallbladder",
     "Draw the EXTERNAL pathway: LR1 (great toe) -> ankle -> knee (LR8) -> genital region -> LR13/LR14 (ribs)",
     "Draw the VERTEX branch: eye system -> forehead -> GV20 (vertex) -- the only channel that reaches here",
     "Label special points: LR3 (Yuan+Shu), LR8 (He-Sea), LR13 (Front-Mu SP + Hui-Meeting Zang), LR14 (Front-Mu LR)",
     "Mark the final internal branch: Liver -> diaphragm -> Lung, completing the 12-channel cycle"],
    "MOA_LR", "CAM_LR")
blank_recall_page("The Liver Meridian of Foot-Jueyin", WOOD)

c.save()
print(f"Saved {OUT}")
print(f"Pages: {page_num[0]-1}")
