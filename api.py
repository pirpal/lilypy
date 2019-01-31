#!usr/bin/env python3

import re
from music_constants import *


def validNoteStr(note_str, lng_option):
    m = re.search()

class TimeSignature:
    def __init__(self, beats, base_duration):
        self.beats = beats
        self.base_duration = base_duration

    def totalDuration(self):
        """
        A duration is expressed as a fraction of 1 / duration:
        
        """
        return self.beats * (1 / self.base_duration)
    
    def __str__(self):
        return "{}/{}".format(self.beats, self.base_duration)


class Note:
    """

    Note(string):
    string is validated before initializing a Note
    """
    def __init__(self, name, duration, alteration=None, point=False):
        self.name         = name
        self.duration     = duration
        self.dec_duration = DURATIONS_FRACTIONS[duration]
        self.alteration   = alteration
        self.point        = point

    def __str__(self):
        str_alteration = "" if not self.alteration else self.alteration
        str_point      = "" if not self.point else self.point
        return "{}{}{}{}".format(
            self.name, str_alteration, self.duration, str_point
        )

    # TODO: replace all of this by a regex
    def validName(self):
        return (self.name in NOTES_NAMES["en"] or self.name in NOTES_NAMES["it"])

    

    def validNote(str_note):
        """
        """
        rgx_en = r"([a,b, c, d, e, f, g])([#, b, f, s]?)(\d+|\d{1})(\.?)"
        reg_it = r"([do, re, mi, fa, sol, la, si]{2,3})([#, b, f, s]?)(\d+|\d{1})(\.?)"
        m = re.search(rgx_en, str_note)
        
    def validDuration(self):
        return self.duration in DURATIONS

    def validAlteration(self):
        return self.alteration in ALTERATIONS

    def validPoint(self):
        return self.point in [".", None]
    
    def isValid(self):
        return self.validName("en") and self.validDuration() and self.validAlteration() and self.validPoint()


class Staff:
    """
    Staff(int, TimeSignature(beats, duration), [Note])
    """
    
    def __init__(self, num, time_sign, notes):
        self.num          = num
        self.time_sign    = time_sign
        self.notes        = notes
        self.correct_time = self.checkTime()

    def checkTime(self):
        total_duration = 0
        for note in self.notes:
            total_duration += (1 / note.duration)
            time_sign_total = (1 / self.time_sign.base_duration) * self.time_sign.beats
        print("notes tot dur: {}\ntime_sign tot dur; {}".format(
            total_duration, time_sign_total
        ))

        return total_duration == time_sign_total    

