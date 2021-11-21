#!/usr/bin/env python
# @Time    : 2021/11/21 6:50 下午
# @Author  : guo2018@88.com

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chord import Chord
from common.settings import DB_SQL_LOCATION
from common.table_class.chord import Table_Chord
from note import Note


def detector(chord_list: list[0, Note], is_may_inversion=True):
    if not chord_list:
        return None
    chord_list: list[Note] = sorted([i for i in chord_list if i], key=lambda x: x.semitone)
    if not chord_list:
        return None
    minutes_list = sorted(list(set([i.clock_instance.mapping_time.minute for i in chord_list])))

    def trans_to_str(the_input):
        return str(the_input).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")

    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    the_result = session.query(Table_Chord).filter(Table_Chord.notes_clock_list == trans_to_str(minutes_list)).all()
    if len(the_result) == 1:
        if getattr(the_result[0], "root_note_loc_id") == chord_list[0].loc_id:
            return Chord(chord_list[0].uid, chord_list[0].octave, getattr(the_result[0], "chord_full_term"))
        else:
            return Chord(getattr(the_result[0], "root_note_uid"), chord_list[0].octave,
                         [getattr(the_result[0], "chord_full_term"), f"uid/{chord_list[0].uid}"])
    elif len(the_result) == 0:
        return None


if __name__ == '__main__':
    list1 = [Note("c", 6), Note("e", 5), Note("g", 6)]
    print(detector(list1))
