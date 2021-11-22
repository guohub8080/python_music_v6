#!/usr/bin/env python
# @Time    : 2021/11/22 3:59 下午
# @Author  : guo2018@88.com
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.settings import CENTER_C_LOCATION
from chord import detect_base_chord
from common import trans_to_str, trans_str_to_list
from common.settings import DB_SQL_LOCATION
from common.table_class.scale import Table_Scale
from common.table_class.chord_meta import Table_Chord_Meta
from common.table_class.meta import Table_Meta
from common.table_class.scale_meta import Table_Scale_Meta
from note import Note

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()

full_normal_uids = [getattr(i, "uid") for i in session.query(Table_Meta).filter(Table_Meta.is_normal == True).all()]

full_scale_info = [i for i in session.query(Table_Scale_Meta).all()]

for each_uid in full_normal_uids:
    for each_chord_info in full_scale_info:
        base_note = Note(each_uid, CENTER_C_LOCATION)
        scale_list = [base_note]
        frexi = trans_str_to_list(getattr(each_chord_info, "prefix_list"))
        for v, i in enumerate(frexi, 2):
            scale_list.append(base_note.get_note_by_interval(i, v))
        # [print(i.math_name, end=" , ") for i in scale_list]
        # print("")
        djuge_list = [1 for i in scale_list if abs(i.bias) > 0]
        # print(djuge_list)
        scale_term = getattr(each_chord_info, "scale_term")
        note_num = 7
        uid_list = trans_to_str([i.uid for i in scale_list])
        math_name_list = trans_to_str([i.math_name for i in scale_list])
        octave_list = trans_to_str([i.octave - CENTER_C_LOCATION for i in scale_list])
        given_root_note_uid = each_uid
        given_root_note_math_name = base_note.math_name
        real_root_note_uid = given_root_note_uid
        real_root_note_math_name = given_root_note_math_name
        is_trans = False
        print(frexi)
        x = 0
        for i in scale_list:
            x += i.bias

        if len(djuge_list) == len(scale_list):
            new_base_note = [i for i in Note(each_uid).same_pitch_notes if abs(i.bias) < 2][0]
            new_scale_list = [new_base_note]
            for v, i in enumerate(frexi, 2):
                print(i, v)
                new_scale_list.append(new_base_note.get_note_by_interval(i, v))
            real_root_note_uid = new_base_note.uid
            real_root_note_math_name = new_base_note.math_name
            is_trans = True
            uid_list = trans_to_str([i.uid for i in new_scale_list])
            math_name_list = trans_to_str([i.math_name for i in new_scale_list])
            octave_list = trans_to_str([i.octave - CENTER_C_LOCATION for i in new_scale_list])
            y = 0
            for i in new_scale_list:
                y += i.bias
            x = y

        new_add = Table_Scale(
            given_root_note_uid=given_root_note_uid,
            given_root_note_math_name=given_root_note_math_name,
            real_root_note_uid=real_root_note_uid,
            real_root_note_math_name=real_root_note_math_name,
            is_trans=is_trans,
            scale_term=scale_term,
            note_num=note_num,
            uid_list=uid_list,
            octave_list=octave_list,
            math_name_list=math_name_list,
            sharp_flat_num=x
        )
        session.add(new_add)
        session.commit()
