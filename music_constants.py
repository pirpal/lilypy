#!usr/bin/env python3

"""
Durées:
1: Ronde
2: Blanche
4: Noire
8: Croche
16: Double-croche
32: Triple-croche
64: Quadruple-croche
128: Quintuple-croche
"""

DURATIONS = [1, 2, 4, 8, 16, 32, 64, 128]

FRAC_1   = 1 / 1
FRAC_2   = 1 / 2
FRAC_4   = 1 / 4
FRAC_8   = 1 / 8
FRAC_16  = 1 / 16
FRAC_32  = 1 / 32
FRAC_64  = 1 / 64
FRAC_128 = 1 / 128

DURATIONS_FRACTIONS = {
    1: FRAC_1, 2: FRAC_2, 4: FRAC_4, 8: FRAC_8,
    16: FRAC_16, 32: FRAC_32, 64: FRAC_64, 128: FRAC_128
}

ALTERATIONS = [None, "f", "s", "b", "#"] # flat sharp bemol diese

NOTES_NAMES = {
    "en": "c d e f g a b".split(" "),
    "it": "do re mi fa sol la si".split(" "),
}
