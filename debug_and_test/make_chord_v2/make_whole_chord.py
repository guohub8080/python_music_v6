#!/usr/bin/env python
# @Time    : 2021/11/14 10:48 下午
# @Author  : guo2018@88.com

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from common import trans_str_to_list
from common.settings import DB_SQL_LOCATION, CENTER_C_LOCATION
from common.table_class.chord import Table_Chord
from common.table_class.chord_meta import Table_Chord_Meta
from common.table_class.meta import Table_Meta
from note import Note

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()

full_normal_uids = [getattr(i, "uid") for i in session.query(Table_Meta).filter(Table_Meta.is_normal == True).all()]

full_chord_term = [i for i in session.query(Table_Chord_Meta).all()]

for each_note_uid in full_normal_uids:
    for each_chord_info in full_chord_term:
        base_note = Note(each_note_uid)
        prefix_list = trans_str_to_list(getattr(each_chord_info, "interval_prefix_list"))
        chord_render = []
        for v, i in enumerate(prefix_list, 2):
            if i:
                chord_render.append(base_note.get_note_by_interval(i, v))

        chord_render.insert(0, base_note)


        def trans_to_str(lsit):
            return str(lsit).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")


        uid_list = trans_to_str(sorted([i.uid for i in chord_render]))
        loc_id_list = trans_to_str(sorted([i.loc_id for i in chord_render]))
        clock_list = trans_to_str(sorted([i.clock_instance.mapping_time.minute for i in chord_render]))
        math_name_list = trans_to_str([i.math_name for i in chord_render])
        new_add = Table_Chord(
            root_note_uid=base_note.uid,
            root_note_loc_id=base_note.loc_id,
            root_note_math_name=base_note.math_name,
            chord_base_id=getattr(each_chord_info, "id"),
            chord_base_term=getattr(each_chord_info, "chord_base_term"),
            chord_full_term=getattr(each_chord_info, "chord_full_term"),
            note_num=len(chord_render),
            notes_uid_list=uid_list,
            notes_loc_id_list=loc_id_list,
            notes_clock_list=clock_list,
            # notes_octave_list=octave_list,
            notes_math_name_list=math_name_list
        )
        session.add(new_add)
        session.commit()
        print(f"完成{each_note_uid}的{getattr(each_chord_info, 'chord_full_term')}...")
