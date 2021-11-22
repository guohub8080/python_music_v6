#!/usr/bin/env python
# @Time    : 2021/11/21 6:35 下午
# @Author  : guo2018@88.com

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chord import detect_base_chord
from common import trans_to_str
from common.settings import DB_SQL_LOCATION
from common.table_class.scale_meta import Table_Scale_Meta
from note import Note

ready_list = [
    ["ION", "自然大调Ionian调式", "也称为自然大调，自然大调的 I 级音阶，由 C 大调的 C 进行到高八度的 C，构成音分别为：1 2 3 4 5 6 7 1",
     "大", "大", "纯", "纯", "大", "大"],
    ["DOR", "Dorian调式（小调式）", "自然大调的 II 级音阶，由 C 大调的 D 进行到高八度的 D，构成音分别为：1 2 b3 4 5 6 b7 1",
     "大", "小", "纯", "纯", "大", "小"],
    ["PHR", "Phrygian调式（小调式）", "自然大调的 III 级音阶，由 C 大调的 E 进行到高八度的 E，构成音分别为：1 b2 b3 4 5 b6 b7 1",
     "小", "小", "纯", "纯", "小", "小"],
    ["LYD", "Lydian调式（大调式）", "自然大调的 IV 级音阶，由 C 大调的 F 进行到高八度的 F，构成音分别为：1 2 3 #4 5 6 7 1  ",
     "大", "大", "增", "纯", "大", "大"],
    ["MLY", "Mixo-lydian调式（大调式）", "自然大调的 V 级音阶，由 C 大调的 G 进行到高八度的 G，构成音分别为：1 2 3 4 5 6 b7 1",
     "大", "大", "纯", "纯", "大", "小"],
    ["AEO", "自然小调Aeolian调式", "自然小调，自然大调的 VI 级音阶，由 C 大调的 A 进行到高八度的 A，构成音分别为：1 2 b3 4 5 b6 b7 1",
     "大", "小", "纯", "纯", "小", "小"],
    ["LOC", "Locrian调式（半减七调式）", "自然大调的 VII 级音阶，由 C 大调的 B 进行到高八度的 B，构成音分别为：1 b2 b3 4 b5 b6 b7 1",
     "小", "小", "纯", "减", "小", "小"],
]

for each_scale in ready_list:
    interval_list = trans_to_str(each_scale[3:])
    engine = create_engine(DB_SQL_LOCATION)
    session = sessionmaker(bind=engine)()
    base_note = Note("C")
    scale_list = [base_note]
    for v, i in enumerate(each_scale[3:], 2):
        scale_list.append(base_note.get_note_by_interval(i, v))
    chord3_list = []
    [print(i.math_name) for i in scale_list]


    def get_rank3(input_list: list[Note]):
        temp_list = [[0, 2, 4],
                     [1, 3, 5],
                     [2, 4, 6],
                     [3, 5, 0],
                     [4, 6, 1],
                     [5, 0, 2],
                     [6, 1, 3]]
        rank_list = []
        for i in temp_list:
            the_chord = detect_base_chord([
                input_list[i[0]],
                input_list[i[1]],
                input_list[i[2]]
            ])
            print(the_chord)
            rank_list.append(the_chord.chord_base_term)
        return trans_to_str(rank_list)


    print(get_rank3(scale_list))


    def get_rank7(input_list: list[Note]):
        temp_list = [
            [0, 2, 4, 6],
            [1, 3, 5, 0],
            [2, 4, 6, 1],
            [3, 5, 0, 2],
            [4, 6, 1, 3],
            [5, 0, 2, 4],
            [6, 1, 3, 5]
        ]
        rank_list = []
        for i in temp_list:
            the_chord = detect_base_chord([
                input_list[i[0]],
                input_list[i[1]],
                input_list[i[2]],
                input_list[i[3]]
            ])
            print(the_chord)
            rank_list.append(the_chord.chord_base_term)
        return trans_to_str(rank_list)


    # print(get_rank3(scale_list))
    new_add = Table_Scale_Meta(
        scale_term=each_scale[0],
        scale_name=each_scale[1],
        scale_description=each_scale[2],
        prefix_list=interval_list,
        notes_num=7,
        chord3_list=get_rank3(scale_list),
        chord7_list=get_rank7(scale_list)
    )
    session.add(new_add)
    session.commit()
