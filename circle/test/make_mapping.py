#!/usr/bin/env python
# @Time    : 2021/11/7 9:05 下午
# @Author  : guo2018@88.com
import random
from datetime import time, timedelta
import datetime
from interval import Interval


def produce_note_time(octave, minute):
    FIXED_YEAR = 2021
    FIXED_MONTH = 11
    FIXED_DAY = 7
    FIXED_SECOND_AND_MICROSECOND = 0
    from datetime import datetime
    return datetime(FIXED_YEAR, FIXED_MONTH, FIXED_DAY, octave, minute, FIXED_SECOND_AND_MICROSECOND,
                    FIXED_SECOND_AND_MICROSECOND)


the_note_name_list = [
    "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"
]


def minute_to_note(octave, minute):
    FIXED_MINUTE = 4
    mapping_list = []
    a = produce_note_time(FIXED_MINUTE, 0)
    for i in range(12):
        b = a
        a = a + timedelta(minutes=5)
        mapping_list.append(Interval(a, b, lower_closed=False))
    judge_note = produce_note_time(4, minute)
    loc_id = None
    for v, i in enumerate(mapping_list):
        if judge_note in i:
            # print(v)
            loc_id = v
    return the_note_name_list[loc_id]
    # return 0


note1 = produce_note_time(4, 0)
note2 = produce_note_time(5, 0)
c = (note2 - note1).seconds / 60 / 5
print(c)


def make_triad(note1: datetime):
    note2 = note1 + timedelta(minutes=20)
    note3 = note1 + timedelta(minutes=35)
    return [note1, note2, note3]


# for i in range(20):
#     the_minute = random.randint(0, 59)
#     print(the_note_name_list[minute_to_note(0, the_minute)])
a = produce_note_time(4, 16)
b = make_triad(a)
for i in b:
    print(minute_to_note(4, i.minute))
