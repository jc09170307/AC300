"""Shared channel-attribute data for AC300 Master Map + Comparison Matrix.
Core attributes (points, pertains/connects, Yuan/Luo/Xi/Front-Mu/Back-Shu/Confluent)
are pulled directly from the existing, already-pushed build_master_comparison.py
(itself verified against Workbook v28 + Wk2-6 transcripts/slides). Direction and
limb-position rows are standard CAM/Deadman channel topography (not lecture-specific
claims) and are labeled as such rather than "lecture-verified" per the content
integrity rule.
"""

CHANNELS = ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "SJ", "GB", "LR"]

COLORS = {
    "LU": (0.32, 0.42, 0.53), "LI": (0.40, 0.48, 0.58),            # Metal
    "ST": (0.706, 0.518, 0.204), "SP": (0.780, 0.612, 0.294),      # Earth
    "HT": (0.627, 0.220, 0.180), "SI": (0.784, 0.353, 0.294),      # Fire
    "BL": (0.118, 0.435, 0.400), "KI": (0.180, 0.494, 0.482),      # Water
    "PC": (0.80, 0.40, 0.36), "SJ": (0.85, 0.50, 0.46),            # Ministerial Fire
    "GB": (0.20, 0.48, 0.27), "LR": (0.30, 0.56, 0.36),            # Wood
}

ATTR = {
    "LU": dict(yinyang="Yin", hf="Hand", elem="Metal", points="11", pertains="Lung", connects="Lg Intestine",
               yuan="LU9", luo="LU7", xi="LU6", hesea="LU5", frontmu="LU1", backshu="BL13", confluent="LU7 (Ren Mai)", pair="LI"),
    "LI": dict(yinyang="Yang", hf="Hand", elem="Metal", points="20", pertains="Lg Intestine", connects="Lung",
               yuan="LI4", luo="LI6", xi="LI7", hesea="LI11", frontmu="ST25", backshu="BL25", confluent="--", pair="LU"),
    "ST": dict(yinyang="Yang", hf="Foot", elem="Earth", points="45", pertains="Stomach", connects="Spleen",
               yuan="ST42", luo="ST40", xi="ST34", hesea="ST36", frontmu="CV12", backshu="BL21", confluent="--", pair="SP"),
    "SP": dict(yinyang="Yin", hf="Foot", elem="Earth", points="21", pertains="Spleen", connects="Stomach",
               yuan="SP3", luo="SP4", xi="SP8", hesea="SP9", frontmu="LR13", backshu="BL20", confluent="SP4 (Chong Mai)", pair="ST"),
    "HT": dict(yinyang="Yin", hf="Hand", elem="Fire", points="9", pertains="Heart", connects="Sm Intestine",
               yuan="HT7", luo="HT5", xi="HT6", hesea="HT3", frontmu="CV14", backshu="BL15", confluent="--", pair="SI"),
    "SI": dict(yinyang="Yang", hf="Hand", elem="Fire", points="19", pertains="Sm Intestine", connects="Heart",
               yuan="SI4", luo="SI7", xi="SI6", hesea="SI8", frontmu="CV4", backshu="BL27", confluent="SI3 (Du Mai)", pair="HT"),
    "BL": dict(yinyang="Yang", hf="Foot", elem="Water", points="67", pertains="Bladder", connects="Kidney",
               yuan="BL64", luo="BL58", xi="BL63", hesea="BL40", frontmu="CV3", backshu="BL28", confluent="BL62 (Yang Qiao)", pair="KI"),
    "KI": dict(yinyang="Yin", hf="Foot", elem="Water", points="27", pertains="Kidney", connects="Bladder",
               yuan="KI3", luo="KI4", xi="KI5", hesea="KI10", frontmu="GB25", backshu="BL23", confluent="KI6 (Yin Qiao)", pair="BL"),
    "PC": dict(yinyang="Yin", hf="Hand", elem="Fire (Min.)", points="9", pertains="Pericardium", connects="San Jiao",
               yuan="PC7", luo="PC6", xi="PC4", hesea="PC3", frontmu="CV17", backshu="BL14", confluent="PC6 (Yin Wei)", pair="SJ"),
    "SJ": dict(yinyang="Yang", hf="Hand", elem="Fire (Min.)", points="23", pertains="San Jiao", connects="Pericardium",
               yuan="SJ4", luo="SJ5", xi="SJ7", hesea="SJ10", frontmu="CV5", backshu="BL22", confluent="SJ5 (Yang Wei)", pair="PC"),
    "GB": dict(yinyang="Yang", hf="Foot", elem="Wood", points="44", pertains="Gallbladder", connects="Liver",
               yuan="GB40", luo="GB37", xi="GB36", hesea="GB34", frontmu="GB24", backshu="BL19", confluent="GB41 (Dai Mai)", pair="LR"),
    "LR": dict(yinyang="Yin", hf="Foot", elem="Wood", points="14", pertains="Liver", connects="Gallbladder",
               yuan="LR3", luo="LR5", xi="LR6", hesea="LR8", frontmu="LR14", backshu="BL18", confluent="--", pair="GB"),
}

# Standard CAM/Deadman topography -- NOT a lecture-specific claim, labeled as
# general reference throughout the built documents.
DIRECTION = {
    "Hand-Yin": "Chest -> Hand", "Hand-Yang": "Hand -> Head",
    "Foot-Yang": "Head -> Foot", "Foot-Yin": "Foot -> Chest/Abdomen",
}

def direction_key(ch):
    a = ATTR[ch]
    return f"{a['hf']}-{a['yinyang']}"

CIRCUITS = [
    ("Anterior Circuit", ["LU", "LI", "ST", "SP"], (0.35, 0.45, 0.55)),
    ("Posterior (Inner) Circuit", ["HT", "SI", "BL", "KI"], (0.55, 0.30, 0.30)),
    ("Middle Circuit", ["PC", "SJ", "GB", "LR"], (0.45, 0.40, 0.30)),
]

# The 4 same-category triads -- one channel from each circuit, matched by
# hand/foot + yin/yang. This is the comparison structure ChatGPT's Phase 4
# recommends and is not already built as its own artifact.
TRIADS = [
    ("Hand-Yin Triad", ["LU", "PC", "HT"], "All three: chest -> hand, arm midline positions"),
    ("Hand-Yang Triad", ["LI", "SJ", "SI"], "All three: hand -> head, arm midline positions"),
    ("Foot-Yang Triad", ["ST", "GB", "BL"], "All three: head -> foot, leg midline positions"),
    ("Foot-Yin Triad", ["SP", "LR", "KI"], "All three: foot -> chest/abdomen, medial leg"),
]

LIMB_POSITION = {
    "LU": "Anterior/radial line, arm", "PC": "Middle line, arm", "HT": "Posterior/ulnar line, arm",
    "LI": "Anterior/radial line, arm", "SJ": "Middle line, arm", "SI": "Posterior/ulnar line, arm",
    "ST": "Anterior line, leg", "GB": "Lateral/middle line, leg", "BL": "Posterior line, leg",
    "SP": "Medial leg -- ANTERIOR above 8 cun/medial malleolus, MIDDLE below (crosses LR)",
    "LR": "Medial leg -- MIDDLE above 8 cun/medial malleolus, ANTERIOR below (crosses SP)",
    "KI": "Medial leg -- POSTERIOR line throughout",
}

# The 5-element color system (locked palette). Ministerial Fire (PC/SJ) is a
# lighter/coral tint of the same Fire hue -- still one of the 5 elements, not
# a 6th separate color -- per the enforced element color-coding rule.
ELEMENT_COLOR = {
    "Metal": (0.32, 0.42, 0.53),
    "Earth": (0.706, 0.518, 0.204),
    "Fire": (0.627, 0.220, 0.180),
    "Water": (0.153, 0.341, 0.514),
    "Wood": (0.20, 0.48, 0.27),
}
MINISTERIAL = {"PC", "SJ"}

def _tint(rgb, amt):
    r, g, b = rgb
    return (r + (1 - r) * amt, g + (1 - g) * amt, b + (1 - b) * amt)

def element_color(ch):
    base_elem = "Fire" if ATTR[ch]["elem"].startswith("Fire") else ATTR[ch]["elem"]
    base = ELEMENT_COLOR[base_elem]
    return _tint(base, 0.32) if ch in MINISTERIAL else base
