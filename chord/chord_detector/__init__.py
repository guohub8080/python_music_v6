#!/usr/bin/env python
# @Time    : 2021/11/21 6:50 下午
# @Author  : guo2018@88.com
from copy import deepcopy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common import trans_str_to_list
from chord import Chord
from circle import Circle
from common.settings import DB_SQL_LOCATION
from common.table_class.chord import Table_Chord
from note import Note


# 严格模式，即有可能输出的是一个，还有可能是一个列表：
def strict_detector(chord_list: list[0, Note]):
    if not chord_list:
        return None
    chord_list: list[Note] = sorted([i for i in chord_list if i], key=lambda x: x.semitone)

    if not chord_list:
        return None

    uid_list = sorted(list(set([i.uid for i in chord_list])))

    def trans_to_str(the_input):
        return str(the_input).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")

    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    the_result = session.query(Table_Chord).filter(
        Table_Chord.notes_uid_list == trans_to_str(uid_list)).all()

    if len(the_result) == 1:
        # 没有转位的情况下：
        if chord_list[0].uid == getattr(the_result, "root_note_uid"):
            return Chord(getattr(the_result, "root_note_uid"), chord_list[0].octave,
                         getattr(the_result, "chord_full_term"))
        # 有转位的情况下：
        else:
            return Chord(getattr(the_result, "root_note_uid"), chord_list[0].octave,
                         [getattr(the_result, "chord_full_term"), f"uid/{chord_list[0].uid}"])
    elif len(the_result) > 0:
        chord_result_list = []
        for each_result in the_result:
            if chord_list[0].uid == getattr(each_result, "root_note_uid"):
                chord_result_list.append(Chord(
                    getattr(each_result, "root_note_uid"), chord_list[0].octave,
                    getattr(each_result, "chord_full_term"))
                )
            else:
                chord_result_list.append(Chord(
                    getattr(each_result, "root_note_uid"), chord_list[0].octave,
                    [getattr(each_result, "chord_full_term"), f"uid/{chord_list[0].uid}"])
                )
        return chord_result_list


# 优先输出基本的和弦，例如增减大小：
def base_prime_detector(chord_list: list[0, Note]):
    if not chord_list:
        return None
    chord_list: list[Note] = sorted([i for i in chord_list if i], key=lambda x: x.semitone)

    if not chord_list:
        return None

    uid_list = sorted(list(set([i.uid for i in chord_list])))

    def trans_to_str(the_input):
        return str(the_input).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")

    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    the_result = session.query(Table_Chord).filter(
        Table_Chord.notes_uid_list == trans_to_str(uid_list)).filter(
        Table_Chord.chord_base_term == Table_Chord.chord_full_term).one_or_none()

    if the_result:
        # 没有转位的情况下：
        if chord_list[0].uid == getattr(the_result, "root_note_uid"):
            return Chord(getattr(the_result, "root_note_uid"), chord_list[0].octave,
                         getattr(the_result, "chord_full_term"))
        else:
            return Chord(getattr(the_result, "root_note_uid"), chord_list[0].octave,
                         [getattr(the_result, "chord_full_term"), f"uid/{chord_list[0].uid}"])
    else:
        return strict_detector(chord_list)


# 只看位置不看音名：
def location_detector(chord_list: list[0, Note]):
    if not chord_list:
        return None
    chord_list: list[Note] = sorted([i for i in chord_list if i], key=lambda x: x.semitone)

    if not chord_list:
        return None

    loc_id_list = sorted(list(set([i.loc_id for i in chord_list])))

    def trans_to_str(the_input):
        return str(the_input).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")

    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    the_result = session.query(Table_Chord).filter(
        Table_Chord.notes_loc_id_list == trans_to_str(loc_id_list)).all()
    if not the_result:
        return None
    result_list = []
    for i in the_result:
        if chord_list[0].loc_id == getattr(i, "root_note_loc_id"):
            result_list.append(Chord(getattr(i, "root_note_uid"), chord_list[0].octave,
                                     getattr(i, "chord_full_term")))
        else:
            result_list.append(Chord(getattr(i, "root_note_uid"), chord_list[0].octave,
                                     [getattr(i, "chord_full_term"), f"uid/{chord_list[0].uid}"]))

    return result_list


if __name__ == '__main__':
    list1 = [Note("d", 6), Note("f", 5), Note("a", 6), Note("c")]
    a = location_detector(list1)
    for i in a:
        print(i)
