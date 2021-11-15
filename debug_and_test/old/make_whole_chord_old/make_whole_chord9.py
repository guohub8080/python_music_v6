#!/usr/bin/env python
# @Time    : 2021/9/1 9:33 下午
# @Author  : guo2018@88.com


from common.settings import DB_SQL_LOCATION, CENTER_C_LOCATION
from sqlalchemy import create_engine

from common.table_class.chord_old import Table_Chord9, Table_Whole_Chord
from sqlalchemy.orm import sessionmaker
from debug_and_test.old.make_whole_chord_old import the_function


def make_whole_chord9():
    print("开始处理 「 九和弦 」 ... ")
    from note import Note
    engine = create_engine(DB_SQL_LOCATION)
    session = sessionmaker(bind=engine)()

    res = session.query(Table_Chord9).all()
    adjust_list = [None, "sus2", "sus4", "add4", "add6", "sharp5", "flat5", "omit3", "omit5", "omit7", "sus2_omit5",
                   "sus2_omit7", "sus4_omit5", "sus4_omit7", "sus2_add4", "sus2_add6", "sus4_add6", "sus2_add4_omit5",
                   "sus2_add4_omit7"]
    for i in res:
        rn_uid = getattr(i, "rn_uid")
        chord_term = getattr(i, "chord_term")
        rn_math_name = getattr(i, "rn_math_name")
        is_valid = bool(getattr(i, "is_valid"))
        # 如果一开始就是不合法的，那么直接就创建一个不合格的字段，直接走人。
        if not is_valid:
            new_add = Table_Whole_Chord(
                is_valid=False,
                rn_uid=rn_uid,
                base_chord_term=chord_term,
                rn_math_name=rn_math_name,
            )
            session.add(new_add)
            continue
        # 如果可以的话，那么就继续
        origin_list = [
            Note(rn_uid, CENTER_C_LOCATION),
            Note(getattr(i, "n3_uid"), CENTER_C_LOCATION + int(getattr(i, "n3_octave"))),
            Note(getattr(i, "n5_uid"), CENTER_C_LOCATION + int(getattr(i, "n5_octave"))),
            Note(getattr(i, "n7_uid"), CENTER_C_LOCATION + int(getattr(i, "n7_octave"))),
            Note(getattr(i, "n9_uid"), CENTER_C_LOCATION + int(getattr(i, "n9_octave"))),
        ]
        for adjust in adjust_list:
            # 如果没有adjust：
            if not adjust:
                # 没有转位也没有其他的改变：
                the_function.insert_to_whole_chord(root_note_uid=rn_uid,
                                                   rn_math_name=rn_math_name,
                                                   base_chord=chord_term,
                                                   inset_list=origin_list)

                continue

            # 如果有adjust:
            if adjust == "add4":
                adjusted_list = the_function.add(origin_list, 4)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_add4=True)

            elif adjust == "add6":
                adjusted_list = the_function.add(origin_list, 6)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_add6=True)

            elif adjust == "sus2":
                adjusted_list = the_function.sus(origin_list, 2)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True)

            elif adjust == "sus4":
                adjusted_list = the_function.sus(origin_list, 4)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus4=True)

            elif adjust == "sharp5":
                adjusted_list = the_function.sharp5(origin_list)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sharp5=True)

            elif adjust == "flat5":
                adjusted_list = the_function.flat5(origin_list)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_flat5=True)

            elif adjust == "omit3":
                adjusted_list = the_function.omit(origin_list, 3)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_omit3=True)

            elif adjust == "omit5":
                adjusted_list = the_function.omit(origin_list, 5)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_omit5=True)
            elif adjust == "omit7":
                adjusted_list = the_function.omit(origin_list, 7)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_omit7=True)

            elif adjust == "sus2_omit5":
                adjusted_list = the_function.omit(origin_list, 5)
                adjusted_list = the_function.sus(adjusted_list, 2)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True,
                                                   is_omit5=True)
            elif adjust == "sus2_omit7":
                adjusted_list = the_function.omit(origin_list, 7)
                adjusted_list = the_function.sus(adjusted_list, 2)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True,
                                                   is_omit7=True)
            elif adjust == "sus4_omit7":
                adjusted_list = the_function.omit(origin_list, 7)
                adjusted_list = the_function.sus(adjusted_list, 4)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus4=True,
                                                   is_omit7=True)
            elif adjust == "sus4_omit5":
                adjusted_list = the_function.omit(origin_list, 5)
                adjusted_list = the_function.sus(adjusted_list, 4)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus4=True,
                                                   is_omit5=True)
            elif adjust == "sus2_add4":
                adjusted_list = the_function.add(origin_list, 4)
                adjusted_list = the_function.sus(adjusted_list, 2)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True,
                                                   is_add2=True)
            elif adjust == "sus2_add6":
                adjusted_list = the_function.add(origin_list, 6)
                adjusted_list = the_function.sus(adjusted_list, 2)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True,
                                                   is_add6=True)
            elif adjust == "sus4_add6":
                adjusted_list = the_function.add(origin_list, 6)
                adjusted_list = the_function.sus(adjusted_list, 4)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus4=True,
                                                   is_add6=True)
            elif adjust == "sus2_add4_omit5":
                adjusted_list = the_function.add(origin_list, 4)
                adjusted_list = the_function.sus(adjusted_list, 2)
                adjusted_list = the_function.omit(adjusted_list, 5)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True,
                                                   is_add4=True, is_omit5=True)
            elif adjust == "sus2_add4_omit7":
                adjusted_list = the_function.add(origin_list, 4)
                adjusted_list = the_function.sus(adjusted_list, 2)
                adjusted_list = the_function.omit(adjusted_list, 7)
                the_function.insert_to_whole_chord(root_note_uid=rn_uid, rn_math_name=rn_math_name,
                                                   base_chord=chord_term, inset_list=adjusted_list, is_sus2=True,
                                                   is_add4=True, is_omit7=True)

    print("「九和弦」处理完毕...")


if __name__ == '__main__':
    make_whole_chord9()
