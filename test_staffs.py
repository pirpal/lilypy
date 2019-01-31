#!usr/bin/env python3

from api import *

CHROMATIC_6_8_IT = Staff(
    num          = 1,
    time_sign    = TimeSignature(beats=6, base_duration=8),
    notes        = [
        Note("do",  16, None, None), # TOT_TIME
        Note("do",  16, "#",  None), # 1/8
        Note("re",  16, None, None),
        Note("mi",  16, "b",  None), # 2/8
        Note("mi",  16, None, None),
        Note("fa",  16, None, None), # 3/8
        Note("fa",  16, "#",  None),
        Note("sol", 16, None, None), # 4/8
        Note("la",  16, "b",  None),
        Note("la",  16, None, None), # 5/8
        Note("si",  16, "b",  None),
        Note("si",  8,  None, None), # 6/8
    ]
    
)

CHROMATIC_6_8_EN = Staff(
    num          = 1,
    time_sign    = TimeSignature(beats=6, base_duration=8),
    notes        = [
        Note("c", 16, None, False), # TOT_TIME
        Note("c", 16, "#",  False), # 1/8
        Note("d", 16, None, False),
        Note("e", 16, "b",  False), # 2/8
        Note("e", 16, None, False),
        Note("f", 16, None, False), # 3/8
        Note("f", 16, "#",  False),
        Note("g", 16, None, False), # 4/8
        Note("a", 16, "b",  False),
        Note("a", 16, None, False), # 5/8
        Note("b", 16, "b",  False),
        Note("b", 8,  None, False), # 6/8
    ]
    
)


TIME_TEST_4_4 = Staff(
    num          = 1,
    time_sign    = TimeSignature(beats=4, base_duration=4),
    notes        = [               # TOT_TIME
        Note("c", 4,  None, False), # 1/4
        Note("d", 4,  None, True),  # 1/4 + 1/8
        Note("e", 16, None, False),
        Note("f", 16, "b",  False), # 2/4
        Note("g", 4, None, False),  # 4/4
    ]
    
)
