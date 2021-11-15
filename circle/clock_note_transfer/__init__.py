#!/usr/bin/env python
# @Time    : 2021/11/10 5:13 下午
# @Author  : guo2018@88.com
from note import Note
from datetime import datetime


def note_to_clock(note_instance: Note):
    note_octave = note_instance.octave
    note_clock_minute_location = note_instance.loc_id - 1 * 5
    return
