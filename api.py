#!usr/bin/env python3


class TimeSignature:
    def __init__(self, beats, base_dur):
        self.beats = beats
        self.base_dur = base_dur

    def totalDur(self):
        return self.beats * self.base_dur
    
    def __str__(self):
        return "{}/{}".format(self.beats, self.base_dur)


class Note:
    def __init__(self, name, dur, alteration=None, pointed=False):
        self.name         = name
        self.dur     = dur
        self.dec_dur = round(1 / self.dur, 2)
        self.alteration   = alteration
        self.pointed      = pointed

    def __str__(self):
        return "{}{}{}{}".format(
            self.name, self.dur, self.alteration, self.pointed
        )


class Staff:
    def __init__(self, num, time_sign, notes):
        self.num          = num
        self.time_sign    = time_sign
        self.notes        = notes
        self.correct_time = self.checkTime()

    def checkTime(self):
        return sum(n.dec_dur for n in self.notes) == 1

#-------------------------------------------------------------------------------
s = Staff(
    1,
    TimeSignature(3, 4),
    [
        Note("do", 4, None, False),
        Note("do", 4, None, False),
        Note("do", 8, None, False),
        Note("do", 8, None, False),
    ]
)

print(s.checkTime())
