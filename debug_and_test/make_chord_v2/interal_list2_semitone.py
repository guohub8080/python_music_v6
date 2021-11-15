#!/usr/bin/env python
# @Time    : 2021/11/14 5:26 下午
# @Author  : guo2018@88.com
from datetime import timedelta, datetime
import datetime
from note import Note
from common.settings import CENTER_C_LOCATION

note_instance = Note("C")


def list_2_semitone(list_str):

    from common import trans_str_to_list
    the_list = trans_str_to_list(list_str)
    # print(the_list)
    # print(the_list)
    notes_list = []
    semitone_list = []

    for v, i in enumerate(the_list, 2):
        if i:
            notes_list.append(note_instance.get_note_by_interval(i, v))
    # [print(i.math_name, i.octave,end="  *  ") for i in notes_list]
    # print("---"*20)
    for i in notes_list:
        semitone_list.append(i.semitone - note_instance.semitone)

    # [print(i) for i in notes_list]

    def clock_minutes_step(origin_datetime: datetime, target_datetime: datetime):
        how_many_minutes = (target_datetime - origin_datetime).seconds / 60 / 5
        return int(how_many_minutes)

    # [print(i.math_name,i.octave) for i in notes_list]
    new_notes = [i.octave_shift_to(CENTER_C_LOCATION) for i in notes_list]
    new_notes.insert(0, note_instance)
    new_notes.append(Note("C",6))
    new_notes = sorted(new_notes, key=lambda x: x.clock_instance.mapping_time)
    # [print(i.clock_instance.mapping_time) for i in new_notes]
    # [print(i) for i in new_notes]
    # print("===")
    clock_gap_list = []
    for v, i in enumerate(new_notes):
        if v > 0:
            clock_gap_list.append(clock_minutes_step(new_notes[v - 1].clock_instance.mapping_time,
                                                     new_notes[v].clock_instance.mapping_time))

    clock_octave_list = []
    origin_clock_list = [i for i in notes_list]
    origin_clock_list.insert(0, note_instance)
    # origin_clock_list.append(note_instance.octave_shift(1))
    origin_clock_list = [i.clock_instance.mapping_time for i in origin_clock_list]
    # print("origin_clock_list:", origin_clock_list)
    # print("clock_gap_list:", clock_gap_list)

    temp_clock = None
    for v, i in enumerate(clock_gap_list[:-1]):
        if v == 0:
            temp_clock = origin_clock_list[0]
        # print(i)

        temp_clock = temp_clock + timedelta(minutes=i * 5)
        # print(temp_clock)
        if temp_clock in origin_clock_list:
            clock_octave_list.append(0)
        elif temp_clock.replace(hour=temp_clock.hour + 1) in origin_clock_list:

            clock_octave_list.append(1)
        elif temp_clock.replace(hour=temp_clock.hour + 2) in origin_clock_list:
            clock_octave_list.append(2)

    notes_list.insert(0, note_instance)
    result = [clock_gap_list, clock_octave_list, semitone_list, [i.art_name for i in notes_list],
              f"*{len(notes_list)}*"]
    for i in result:
        the_str = str(i)[1:][:-1].replace(" ", "").replace("'", "")
        print(the_str, end="\t")
    print("")

    return


if __name__ == '__main__':
    the_list = [

        "0,大,0,纯",
        "0,小,0,纯",
        "0,小,0,减",
        "0,大,0,增",
        "0,大,0,减",
        "大,0,0,纯",
        "0,0,纯,纯",
        "大,大,0,纯",
        "大,小,0,纯",
        "0,大,纯,纯",
        "0,小,纯,纯",
        "0,大,0,纯,大",
        "0,小,0,纯,大",
        "0,大,0,纯,0,0,0,大",
        "0,小,0,纯,0,0,0,大",
        "0,大,0,纯,0,0,0,0,0,纯",
        "0,小,0,纯,0,0,0,0,0,纯",
        "0,大,0,纯,大,0,0,大",
        "0,小,0,纯,大,0,0,大",
        "0,大,0,纯,0,0,0,0,0,0,0,大",
        "0,小,0,纯,0,0,0,0,0,0,0,大",
        "0,大,0,纯,0,大",
        "0,大,0,纯,0,小",
        "0,小,0,纯,0,小",
        "0,小,0,减,0,小",
        "0,小,0,纯,0,大",
        "0,小,0,减,0,减",
        "0,大,0,增,0,小",
        "0,大,0,增,0,大",
        "0,大,0,减,0,大",
        "0,大,0,增,0,大",
        "0,大,0,纯,0,大,0,小",
        "0,大,0,纯,0,大,0,0,0,0,0,小",
        "0,大,0,纯,0,大,0,0,0,增",
        "0,大,纯,纯,0,大",
        "0,大,0,减,0,小",
        "0,大,0,增,0,小",
        "0,大,0,纯,大,小",
        "0,大,0,纯,0,小,0,增",
        "0,大,0,纯,0,小,0,小",
        "0,大,0,纯,0,小,0,0,0,增",
        "0,大,0,纯,0,小,0,0,0,减",
        "0,大,0,纯,0,小,0,0,0,0,0,小",
        "0,大,0,减,0,小,0,小",
        "0,大,0,减,0,小,0,增",
        "0,大,0,增,0,小,0,小",
        "0,大,0,增,0,小,0,增",
        "0,小,0,减,0,小",
        "0,小,0,增,0,小",
        "0,小,0,减,0,大",
        "0,小,0,增,0,大",
        "大,0,0,纯,0,大",
        "0,0,纯,纯,0,大",
        "大,0,0,纯,0,小",
        "0,0,纯,纯,0,小",
        "0,大,0,纯,0,大,0,大",
        "0,0,纯,纯,0,大,0,大",
        "0,大,0,减,0,大,0,大",
        "0,大,0,增,0,大,0,大",
        "0,大,0,纯,0,大,0,大,0,增",
        "0,大,0,纯,0,大,0,大,0,0,0,小",
        "0,大,0,纯,0,小,0,大",
        "0,0,纯,纯,0,小,0,大",
        "0,大,0,增,0,小,0,大",
        "0,大,0,纯,0,小,0,小",
        "0,大,0,纯,0,小,0,大,0,减",
        "0,大,0,纯,0,小,0,大,0,增",
        "0,大,0,纯,0,小,0,大,0,0,0,小",
        "0,小,0,纯,0,小,0,大",
        "0,小,0,减,0,小,0,大",
        "0,小,0,纯,0,小,0,小",
        "0,小,0,纯,0,大,0,大",
        "0,大,0,增,0,小,0,大",
        "0,大,0,纯,0,大,0,大,0,纯",
        "0,大,0,纯,0,小,0,大,0,纯",
        "0,大,0,纯,0,小,0,大,0,纯,0,小",
        "0,大,0,纯,0,小,0,小,0,纯",
        "0,大,0,纯,0,小,0,增,0,纯",
        "0,大,0,减,0,小,0,大,0,纯",
        "0,大,0,增,0,小,0,大,0,纯",
        "0,小,0,纯,0,小,0,大,0,纯",
        "0,小,0,减,0,小,0,大,0,纯",
        "0,小,0,纯,0,大,0,大,0,纯",
        "0,大,0,纯,0,大,0,大,0,纯,0,大",
        "大,0,0,纯,0,大,0,大,0,纯,0,大",
        "0,0,纯,纯,0,大,0,大,0,纯,0,大",
        "0,大,0,纯,0,大,0,小,0,纯,0,大",
        "0,大,0,纯,0,大,0,大,0,增,0,大",
        "0,大,0,减,0,大,0,大,0,纯,0,大",
        "0,大,0,增,0,大,0,大,0,纯,0,大",
        "0,0,纯,纯,0,小,0,大,0,纯,0,大",
        "0,大,0,纯,0,小,0,大,0,纯,0,大",
        "0,大,0,纯,0,小,0,大,0,增,0,大",
        "0,大,0,纯,0,小,0,增,0,纯,0,大",
        "0,大,0,纯,0,小,0,小,0,纯,0,大",
        "0,大,0,减,0,小,0,大,0,纯,0,大",
        "0,大,0,增,0,小,0,大,0,纯,0,大",
        "0,小,0,纯,0,小,0,大,0,纯,0,大",
        "0,小,0,纯,0,大,0,大,0,纯,0,大",]
    for i in the_list:
        the_Str = str(list_2_semitone(i))
