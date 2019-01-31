#!usr/bin/env python3

import unittest
from api import *
from music_constants import *
from test_staffs import *


class TestDurations(unittest.TestCase):

    def testDurationsConstants(self):
        for d in DURATIONS:
            self.assertEqual(
                1 / d, DURATIONS_FRACTIONS[d]
            )

    def testDurationsEquivalences(self):
        time_sign_4_4 = TimeSignature(4, 4)
        self.assertEqual(
            1/4 + 1/4 + 1/4 + 1/4,
            time_sign_4_4.totalDuration()
        )
        time_sign_3_4 = TimeSignature(3, 4)
        self.assertEqual(
            1/4 + 1/4 + 1/4,
            time_sign_3_4.totalDuration()
        )
        time_sign_6_8 = TimeSignature(6, 8)
        self.assertEqual(
            1 / 8 * 6,
            time_sign_6_8.totalDuration()
        )



class TestNoteConstructor(unittest.TestCase):

    def testNoteName(self):
        for n in "do re mi fa sol la si c d e f g a b".split(" "):
            note = Note(name=n, duration=4)
            self.assertEqual(note.validName(), True)

    def testNoteDuration(self):
        for d in [1, 2, 4, 8, 16, 32, 64, 128]:
            note = Note(name="c", duration=d)
            self.assertEqual(note.validDuration(), True)

    def testNoteAlteration(self):
        for a in ["f", "s", "b", "#", None]:
            note = Note(name="c", duration=4, alteration=a)
            self.assertEqual(note.validAlteration(), True)

    def testNotePoint(self):
        for p in [".", None]:
            note = Note(name="c", duration=4, alteration=None, point=p)
            self.assertEqual(note.validPoint(), True)

    def testPrintNote(self):
        o_it = ""
        o_en = ""
        for note in CHROMATIC_6_8_IT.notes:
            o_it += note.__str__()
            o_it += " "
        self.assertEqual(
            o_it,
            "do16 do#16 re16 mib16 mi16 fa16 " \
            "fa#16 sol16 lab16 la16 sib16 si8 "
        )
        for note in CHROMATIC_6_8_EN.notes:
            o_en += note.__str__()
            o_en += " "
        self.assertEqual(
            o_en,
            "c16 c#16 d16 eb16 e16 f16 " \
            "f#16 g16 ab16 a16 bb16 b8 "
        )


class TestStaffConstructor(unittest.TestCase):

    def testStaffTime(self):
        self.assertEqual(CHROMATIC_6_8_IT.checkTime(), True)

    def testPrintStaff(self):
        pass

            
#-------------------------
if __name__ == "__main__":
    unittest.main()
