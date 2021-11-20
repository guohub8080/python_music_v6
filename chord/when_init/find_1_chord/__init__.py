#!/usr/bin/env python
# @Time    : 2021/11/12 2:49 下午
# @Author  : guo2018@88.com
from note import Note

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine
from common.table_class.meta import Table_Meta
from common.table_class.chord_meta import Table_Chord_Meta
from sqlalchemy.orm import sessionmaker
from common import trans_str_to_list


def execute(base_note_uid: [int, str], base_note_octave, chord_term: str):
    engine = create_engine(DB_SQL_LOCATION)
    session = sessionmaker(bind=engine)()
    if isinstance(base_note_uid, str):
        base_note_uid = session.query(Table_Meta).filter(Table_Meta.math_name == base_note_uid).one_or_none()
        if not base_note_uid:
            return None
    the_return = {
        "chord_list": None,
        "chord_base_term": None
    }
    result = session.query(Table_Chord_Meta).filter(Table_Chord_Meta.chord_full_term == chord_term).one_or_none()
    if not result:
        return None

    the_return["chord_base_term"] = getattr(result, "chord_base_term")
    the_return["move5"] = getattr(result, "move5")
    the_return["move9"] = getattr(result, "move9")
    the_return["move11"] = getattr(result, "move11")
    the_return["move13"] = getattr(result, "move13")
    the_return["is_add2"] = getattr(result, "is_add2")
    the_return["is_add4"] = getattr(result, "is_add4")
    the_return["is_add6"] = getattr(result, "is_add6")
    the_return["is_add9"] = getattr(result, "is_add9")
    the_return["is_add11"] = getattr(result, "is_add11")
    the_return["is_add13"] = getattr(result, "is_add13")
    the_return["sus"] = getattr(result, "sus")
    the_interval_prefix_list = None
    if getattr(result, "chord_base_term") == getattr(result, "chord_full_term"):
        the_interval_prefix_list = trans_str_to_list(getattr(result, "interval_prefix_list"))
    else:
        the_interval_prefix_list = trans_str_to_list(getattr(session.query(Table_Chord_Meta).filter(
            Table_Chord_Meta.chord_full_term == the_return["chord_base_term"]).one_or_none(), "interval_prefix_list"))
    notes_list = [Note(base_note_uid, base_note_octave)]
    for v, i in enumerate(the_interval_prefix_list, 2):
        if i:
            temp_note_instance = notes_list[0].get_note_by_interval(i, v)
            if temp_note_instance.is_valid:
                notes_list.append(temp_note_instance)
            else:
                return None
        else:
            notes_list.append(0)
    the_return["chord_list"] = notes_list
    return the_return


if __name__ == '__main__':
    a = execute(1, 5, "sus2")
    print(a)
