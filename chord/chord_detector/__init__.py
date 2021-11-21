#!/usr/bin/env python
# @Time    : 2021/11/21 6:50 下午
# @Author  : guo2018@88.com
from note import Note
from chord import Chord
from datetime import timedelta, datetime
from note import Note
from common.settings import CENTER_C_LOCATION
from common import trans_str_to_list
from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine
from common.table_class.meta import Table_Meta
from common.table_class.chord_meta import Table_Chord_Meta
from sqlalchemy.orm import sessionmaker
from collections import deque
from circle import Circle


def detector(chord_list: list[0, Note]):
    if not chord_list:
        return None
    chord_list: list[Note] = sorted([i for i in chord_list if i], key=lambda x: x.semitone)
    if not chord_list:
        return None
    minutes_list = [i.clock_instance.mapping_time.minute for i in chord_list]
    mapping_time_list = sorted(list(set(minutes_list)))
    if mapping_time_list[0] != 0:
        mapping_time_list = [i - mapping_time_list for i in mapping_time_list]

    # print(mapping_time_list)

    def fixed_location_to_segments(the_list: list[int]):
        def gap_5_minutes(origin, target):
            from circle import CLOCK_META
            origin = datetime(CLOCK_META.FIXED_YEAR, CLOCK_META.FIXED_MONTH, CLOCK_META.FIXED_DAY,
                              CLOCK_META.FIXED_HOUR, origin, 0, 0)
            target = datetime(CLOCK_META.FIXED_YEAR, CLOCK_META.FIXED_MONTH, CLOCK_META.FIXED_DAY,
                              CLOCK_META.FIXED_HOUR, target, 0, 0)
            i = 0
            while origin.minute != target.minute:
                i += 1
                origin = origin + timedelta(minutes=5)
            return i

        result = []
        for temp_gap in range(len(the_list)):
            if temp_gap > 0:
                result.append(gap_5_minutes(the_list[temp_gap - 1], the_list[temp_gap]))
        result.append(gap_5_minutes(the_list[-1], the_list[0]))
        return result

    clock_segments = fixed_location_to_segments(mapping_time_list)
    judge_list = []
    for i in minutes_list:
        if not (i in judge_list):
            judge_list.append(i)
    origin_clock_segments = fixed_location_to_segments(judge_list)
    print(clock_segments)
    print(origin_clock_segments)
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    query_result = session.query(Table_Chord_Meta).filter(Table_Chord_Meta.note_num == len(clock_segments)).all()
    full_chord_term = ""
    if query_result:
        flag = True
        for each_query in query_result:
            if clock_segments == trans_str_to_list(getattr(each_query, "clock_list")):
                full_chord_term = getattr(each_query, "chord_full_term")
                flag = False
                break
        if flag:
            return None
    else:
        return None
    # print(full_chord_term)
    # 因为转位的存在，所以我们来判断哪个是和弦里面的低音：
    if clock_segments == origin_clock_segments:
        return Chord(chord_list[0].uid, chord_list[0].octave, full_chord_term)

    temp_circle = Circle(origin_clock_segments)
    real_root_note = None
    for i in range(1, len(clock_segments)):
        if temp_circle.move(i).whole_queue == clock_segments:
            real_root_note = chord_list[i]
            break
    print(real_root_note)
    print(chord_list[0])
    return Chord(real_root_note.uid, chord_list[0].octave, [full_chord_term, f"uid/{chord_list[0].uid}"])


if __name__ == '__main__':
    list1 = [Note("c", 6), Note("e", 5), Note("g", 5)]
    print(detector(list1))
