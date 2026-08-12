"""Generates flashcard data (PointID, NameRecall, Special-Category) for
PC/SJ/GB/LR from wk6_content.py's point tables. Single source of truth for
both the Anki export and the print/reMarkable reference PDFs."""
import re, sys
sys.path.insert(0, "/home/claude/work")
from wk6_content import PC_POINTS, SJ_POINTS, GB_POINTS_GROUPED, LR_POINTS, PC_META, SJ_META, GB_META, LR_META

def clean_location(loc):
    loc = re.sub(r'^[A-Z\-\+\s]+\.\s*', '', loc)
    loc = re.sub(r'HIGH-YIELD:.*$', '', loc).strip()
    loc = re.sub(r'\.$', '', loc).strip()
    return loc

def flatten_gb():
    out = []
    for zone, pts in GB_POINTS_GROUPED:
        for code, pin, cat, loc in pts:
            if '-' in code and code[0].isalpha():  # skip ranged placeholder rows like "GB4-GB13"
                continue
            out.append((code, pin, cat, loc))
    return out

CHANNEL_POINTS = {
    "PC": PC_POINTS,
    "SJ": SJ_POINTS,
    "GB": flatten_gb(),
    "LR": LR_POINTS,
}

CHANNEL_META = {"PC": PC_META, "SJ": SJ_META, "GB": GB_META, "LR": LR_META}

CATEGORY_LABELS = [
    ("Jing-Well", "JING-WELL"), ("Ying-Spring", "YING-SPRING"),
    ("Shu-Stream", "SHU-STREAM"), ("Jing-River", "JING-RIVER"),
    ("He-Sea", "HE-SEA"), ("Yuan-Source", "YUAN-SOURCE"),
    ("Luo-Connecting", "LUO-CONNECTING"), ("Xi-Cleft", "XI-CLEFT"),
    ("Confluent", "CONFLUENT"), ("Hui-Meeting", "HUI-MEETING"),
]

def build_pointid_cards(channel):
    cards = []
    for code, pin, cat, loc in CHANNEL_POINTS[channel]:
        clue = clean_location(loc)
        cards.append((f"{channel} point: {clue}", f"{code} \u2014 {pin}"))
    return cards

def build_namerecall_cards(channel):
    return [(f"{code} = ?", pin) for code, pin, cat, loc in CHANNEL_POINTS[channel]]

def build_special_category_cards(channel):
    cards = []
    meta = dict(CHANNEL_META[channel])
    label_map = [
        ("Back-Shu", "Back-Shu (of {ch})"),
        ("Front-Mu", "Front-Mu (of {ch})"),
        ("Yuan-Source", "Yuan-Source"),
        ("Luo-Connecting", "Luo-Connecting"),
        ("He-Sea", "He-Sea"),
        ("Xi-Cleft", "Xi-Cleft"),
    ]
    organ = {"PC": "Pericardium", "SJ": "San Jiao", "GB": "Gallbladder", "LR": "Liver"}[channel]
    for key, label_tmpl in label_map:
        if key in meta:
            val = meta[key]
            label = label_tmpl.format(ch=organ)
            cards.append((f"{channel} \u2014 {label} point?", val.split(" (")[0].split(" --")[0].strip()))
    if "Confluent (opens EV)" in meta:
        val = meta["Confluent (opens EV)"]
        pt = val.split(" -- ")[0].strip()
        cards.append((f"{channel} \u2014 Confluent point (opens which EV)?", val))
    for code, pin, cat, loc in CHANNEL_POINTS[channel]:
        for label, keyword in CATEGORY_LABELS:
            if keyword in cat and keyword not in ("HE-SEA",):  # He-Sea handled via meta above; avoid dup except where per-point needed
                pass
    # per-point Jing-Well / Ying-Spring / Jing-River (not in meta) pulled directly from category field
    for code, pin, cat, loc in CHANNEL_POINTS[channel]:
        for label, keyword in [("Jing-Well", "JING-WELL"), ("Ying-Spring", "YING-SPRING"), ("Jing-River", "JING-RIVER")]:
            if keyword in cat:
                cards.append((f"{channel} \u2014 {label} point?", f"{code} {pin}"))
    return cards

ALL_CHANNELS = ["PC", "SJ", "GB", "LR"]

def all_cards():
    """Returns dict: channel -> {'pointid': [...], 'namerecall': [...], 'special': [...]}"""
    out = {}
    for ch in ALL_CHANNELS:
        out[ch] = {
            "pointid": build_pointid_cards(ch),
            "namerecall": build_namerecall_cards(ch),
            "special": build_special_category_cards(ch),
        }
    return out

if __name__ == "__main__":
    data = all_cards()
    total = 0
    for ch, d in data.items():
        n = len(d["pointid"]) + len(d["namerecall"]) + len(d["special"])
        total += n
        print(ch, {k: len(v) for k, v in d.items()}, "=", n)
    print("TOTAL:", total)
