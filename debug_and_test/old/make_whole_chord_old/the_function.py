#!/usr/bin/env python
# @Time    : 2021/9/2 12:22 下午
# @Author  : guo2018@88.com
from note import Note


def add(need_add_list: list[Note], add_interval):
    assert add_interval in (2, 4, 6)
    if not need_add_list:
        return None
    need_add_list = sorted(need_add_list, key=lambda x: x.semitone)
    new_note = Note()
    new_note.is_valid = False
    if add_interval == 2:
        new_note = need_add_list[0].interval.M2
    elif add_interval == 4:
        new_note = need_add_list[0].interval.P4
    elif add_interval == 6:
        new_note = need_add_list[0].interval.M6
    if new_note.is_valid:
        need_add_list.append(new_note)
        return sorted(need_add_list, key=lambda x: x.semitone)
    return None


def sus(need_sus_list: list[Note], sus_type: int):
    assert sus_type in (2, 4)
    if not need_sus_list:
        return None
    need_sus_list = sorted(need_sus_list, key=lambda x: x.semitone)
    the_index = 0
    for i in range(1, len(need_sus_list)):
        if need_sus_list[i].index - need_sus_list[0].index == 2:
            the_index = i
            break
    new_list = [i for i in need_sus_list if need_sus_list.index(i) != the_index]
    if sus_type == 2:
        note2 = need_sus_list[0].interval.M2
        if note2.is_valid:
            new_list.append(note2)
            return sorted(new_list, key=lambda x: x.semitone)
    if sus_type == 4:
        note4 = need_sus_list[0].interval.P4
        if note4.is_valid:
            new_list.append(note4)
            return sorted(new_list, key=lambda x: x.semitone)
    return None


def omit(need_omit_list: list[Note], omit_type: int):
    if not need_omit_list:
        return None
    need_omit_list = sorted(need_omit_list, key=lambda x: x.semitone)
    root_note = need_omit_list[0]
    temp_index = 0
    if omit_type == 3:
        for i in range(1, len(need_omit_list)):
            if need_omit_list[i].index - root_note.index == 2:
                temp_index = i
                break
    if omit_type == 5:
        for i in range(1, len(need_omit_list)):
            if need_omit_list[i].index - root_note.index == 4:
                temp_index = i
                break
    if omit_type == 7:
        for i in range(1, len(need_omit_list)):
            if need_omit_list[i].index - root_note.index == 6:
                temp_index = i
                break
    if omit_type == 9:
        for i in range(1, len(need_omit_list)):
            if need_omit_list[i].index - root_note.index == 8:
                temp_index = i
                break
    if omit_type == 11:
        for i in range(1, len(need_omit_list)):
            if need_omit_list[i].index - root_note.index == 10:
                temp_index = i
                break
    if temp_index:
        new_list = [i for i in need_omit_list if need_omit_list.index(i) != temp_index]
        return new_list
    return None


def sharp5(need_sharp_list: list[Note]):
    if not need_sharp_list:
        return None
    need_sharp_list = sorted(need_sharp_list, key=lambda x: x.semitone)
    temp_index = 0
    for i in range(1, len(need_sharp_list)):
        if need_sharp_list[i].index - need_sharp_list[0].index == 4:
            temp_index = i
            break
    if temp_index:
        need_sharp_list[temp_index] = need_sharp_list[temp_index].sharp_or_flat_adjust(1)
        if not need_sharp_list[temp_index]:
            return None
        if need_sharp_list[temp_index].is_valid:
            return need_sharp_list
    return None


def flat5(need_sharp_list: list[Note]):
    if not need_sharp_list:
        return None
    need_sharp_list = sorted(need_sharp_list, key=lambda x: x.semitone)
    temp_index = 0
    for i in range(1, len(need_sharp_list)):
        if need_sharp_list[i].index - need_sharp_list[0].index == 4:
            temp_index = i
            break
    if temp_index:
        need_sharp_list[temp_index] = need_sharp_list[temp_index].sharp_or_flat_adjust(-1)
        if not need_sharp_list[temp_index]:
            return None
        if need_sharp_list[temp_index].is_valid:
            return need_sharp_list
    return None


def inversion_on(the_list: list[Note], inversion_uid):
    if not the_list:
        return None
    the_list = sorted(the_list, key=lambda x: x.semitone)
    if inversion_uid == the_list[0].uid or inversion_uid == 0:
        return the_list
    flag = False
    for v, i in enumerate(the_list):
        if i.uid == inversion_uid:
            flag = v
            break
    # print(flag)
    if flag:
        for i in range(flag):
            if i < flag:
                the_list[i] = the_list[i].octave_shift(1)
        return the_list
    new_note = Note(inversion_uid, the_list[0].octave)
    if new_note.semitone > the_list[0].semitone:
        new_note = new_note.octave_shift(-1)
        if new_note.semitone == the_list[0].semitone:
            return None
    the_list.append(new_note)
    return the_list


def insert_to_whole_chord(root_note_uid: int, rn_math_name: str, base_chord: str, inset_list: list[Note],
                          is_add2=False, is_add4=False, is_add6=False, is_add9=False, is_add11=False,
                          is_add13=False, is_sharp5=False, is_omit5=False, is_flat5=False,
                          is_omit3=False, is_omit7=False, is_omit9=False, is_omit11=False,
                          is_sus2=False, is_sus4=False, inversion_uid=0, inversion_math_name=None):
    from common.settings import DB_SQL_LOCATION
    from sqlalchemy import create_engine
    from common.table_class.chord_old import Table_Whole_Chord
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(DB_SQL_LOCATION)
    session = sessionmaker(bind=engine)()
    new_add = Table_Whole_Chord(is_valid=True)
    new_add.is_add2 = is_add2
    new_add.is_add4 = is_add4
    new_add.is_add6 = is_add6
    new_add.is_add9 = is_add9
    new_add.is_add11 = is_add11
    new_add.is_add13 = is_add13
    new_add.is_sharp5 = is_sharp5
    new_add.is_omit5 = is_omit5
    new_add.is_flat5 = is_flat5
    new_add.is_omit3 = is_omit3
    new_add.is_omit7 = is_omit7
    new_add.is_omit9 = is_omit9
    new_add.is_omit11 = is_omit11
    new_add.is_sus2 = is_sus2
    new_add.is_sus4 = is_sus4
    new_add.inversion_uid = inversion_uid
    new_add.inversion_math_name = inversion_math_name
    new_add.rn_uid = root_note_uid
    new_add.base_chord_term = base_chord
    new_add.rn_math_name = rn_math_name
    if not inset_list:
        new_add.is_valid = False
        session.add(new_add)
        session.commit()
        return
    inset_list = sorted(inset_list, key=lambda x: (x.semitone, -x.index))
    # 最基本的和弦也都有三个音符：
    new_add.n1_uid = inset_list[0].uid
    new_add.n1_math_name = inset_list[0].math_name
    new_add.n2_uid = inset_list[1].uid
    new_add.n2_math_name = inset_list[1].math_name
    new_add.n2_octave = inset_list[1].octave - inset_list[0].octave
    new_add.n3_uid = inset_list[2].uid
    new_add.n3_math_name = inset_list[2].math_name
    new_add.n3_octave = inset_list[2].octave - inset_list[0].octave
    if len(inset_list) >= 4:
        new_add.n4_uid = inset_list[3].uid
        new_add.n4_math_name = inset_list[3].math_name
        new_add.n4_octave = inset_list[3].octave - inset_list[0].octave
    if len(inset_list) >= 5:
        new_add.n5_uid = inset_list[4].uid
        new_add.n5_math_name = inset_list[4].math_name
        new_add.n5_octave = inset_list[4].octave - inset_list[0].octave
    if len(inset_list) >= 6:
        new_add.n6_uid = inset_list[5].uid
        new_add.n6_math_name = inset_list[5].math_name
        new_add.n6_octave = inset_list[5].octave - inset_list[0].octave
    if len(inset_list) >= 7:
        new_add.n7_uid = inset_list[6].uid
        new_add.n7_math_name = inset_list[6].math_name
        new_add.n7_octave = inset_list[6].octave - inset_list[0].octave
    new_add.note_count = len(inset_list)
    session.add(new_add)
    session.commit()


if __name__ == '__main__':
    origin_list = [Note("C"), Note("E"), Note("G")]
    # new_lsit = inversion_on(origin_list, 9)
    # for i in new_lsit:
    #     print(i)
    # the_note = Note("C+2")
    # print(the_note.interval.AUG5.is_valid)
    [print(i) for i in sus(origin_list, 4)]
    [print(i) for i in omit(origin_list, 5)]
    # print(sus2(origin_list))
