#!/usr/bin/env python
# @Time    : 2021/11/5 6:18 下午
# @Author  : guo2018@88.com

def just_do_it():
    from note import Note
    from sqlalchemy import create_engine
    from note import Note
    from common.table_class.meta import Table_Meta
    from common.table_class.scale import Table_Scale
    from common.table_class.scale_meta import Table_Scale_Meta
    from sqlalchemy.orm import sessionmaker

    from common.settings import DB_SQL_LOCATION

    ready_list = [
        ["ION", "自然大调Ionian调式", "大", "大", "纯", "纯", "大", "大"],
        ["DOR", "Dorian调式（小调式）", "大", "小", "纯", "纯", "大", "小"],
        ["PHR", "Phrygian调式（小调式）", "小", "小", "纯", "纯", "小", "小"],
        ["LYD", "Lydian调式（大调式）", "大", "大", "增", "纯", "大", "大"],
        ["MLY", "Mixo-lydian调式（大调式）", "大", "大", "纯", "纯", "大", "小"],
        ["AEO", "自然小调Aeolian调式", "大", "小", "纯", "纯", "小", "小"],
        ["LOC", "Locrian调式（半减七调式）", "小", "小", "纯", "减", "小", "小"],
    ]

    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()

    the_uid_list = [getattr(i, "uid") for i in session.query(Table_Meta).filter(Table_Meta.is_normal == True).all()]
    # scale_lsit = [getattr(i, "scale_term") for i in session.query(Table_Scale_Meta).all()]
    for i in the_uid_list:
        for ii in ready_list:
            root_note_instance = Note(i)
            note2 = root_note_instance.get_note_by_interval(ii[2], 2)
            note3 = root_note_instance.get_note_by_interval(ii[3], 3)
            note4 = root_note_instance.get_note_by_interval(ii[4], 4)
            note5 = root_note_instance.get_note_by_interval(ii[5], 5)
            note6 = root_note_instance.get_note_by_interval(ii[6], 6)
            note7 = root_note_instance.get_note_by_interval(ii[7], 7)
            note_list = [root_note_instance, note2, note3, note4, note5, note6, note7]
            bias_judge = 0
            is_trans = False
            for x in note_list:
                if abs(x.bias) >= 1:
                    bias_judge += 1
            if abs(bias_judge) >= 7:
                is_trans = True
                new_root_note = [i for i in root_note_instance.same_pitch_notes if abs(i.bias) <= 1][0]
                note2 = new_root_note.get_note_by_interval(ii[2], 2)
                note3 = new_root_note.get_note_by_interval(ii[3], 3)
                note4 = new_root_note.get_note_by_interval(ii[4], 4)
                note5 = new_root_note.get_note_by_interval(ii[5], 5)
                note6 = new_root_note.get_note_by_interval(ii[6], 6)
                note7 = new_root_note.get_note_by_interval(ii[7], 7)
                note_list = [new_root_note, note2, note3, note4, note5, note6, note7]
            next_rn_octave = note_list[6].octave - note_list[0].octave
            next_rn_instance = Note(note_list[0].uid, note_list[0].octave + next_rn_octave)
            if next_rn_instance.semitone < note_list[-1].semitone:
                next_rn_octave += 1
            new_add = Table_Scale(
                rn_uid=i, rn_math_name=root_note_instance.math_name, rn_art_name=root_note_instance.art_name,

                scale_term=ii[0], is_valid=True, is_trans=is_trans, note_num=7,
                n1_uid=note_list[0].uid, n1_math_name=note_list[0].math_name,
                n2_uid=note_list[1].uid, n2_math_name=note_list[1].math_name,
                n2_octave=note_list[1].octave - note_list[0].octave,
                n3_uid=note_list[2].uid, n3_math_name=note_list[2].math_name,
                n3_octave=note_list[2].octave - note_list[0].octave,
                n4_uid=note_list[3].uid, n4_math_name=note_list[3].math_name,
                n4_octave=note_list[3].octave - note_list[0].octave,
                n5_uid=note_list[4].uid, n5_math_name=note_list[4].math_name,
                n5_octave=note_list[4].octave - note_list[0].octave,
                n6_uid=note_list[5].uid, n6_math_name=note_list[5].math_name,
                n6_octave=note_list[5].octave - note_list[0].octave,
                n7_uid=note_list[6].uid, n7_math_name=note_list[6].math_name,
                n7_octave=note_list[6].octave - note_list[0].octave,
                next_rn_uid=note_list[0].uid,
                next_rn_math_name=note_list[0].math_name,
                next_rn_octave=next_rn_octave
            )
            session.add(new_add)
            session.commit()
        print(i)


if __name__ == '__main__':
    input("不要轻易开启这个动作！")
    input("不要轻易开启这个动作！")
    input("不要轻易开启这个动作！")
    input("不要轻易开启这个动作！")
    just_do_it()
