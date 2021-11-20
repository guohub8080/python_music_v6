#!/usr/bin/env python
# @Time    : 2021/11/11 10:40 下午
# @Author  : guo2018@88.com
from note import Note
from common.settings import CENTER_C_LOCATION
from chord.when_init import find_1_chord
from chord.CHORD_META import Adjust_Chord

is_valid = False

chord_base_list = None
chord_base_term = None

adjust_info = Adjust_Chord()


def init_process(root_note_uid_or_math_name=1, root_note_octave=CENTER_C_LOCATION,
                 chord_term_list: [None, list, str] = "maj3"):
    if isinstance(chord_term_list, str):
        chord_term_list = [chord_term_list]
    assert isinstance(chord_term_list, list)
    # 第一个一定是基本和弦类型：
    base_chord_dict = find_1_chord.execute(root_note_uid_or_math_name, root_note_octave, chord_term_list[0])
    if base_chord_dict:
        global chord_base_list, chord_base_term, adjust_info, is_valid
        chord_base_list = base_chord_dict["chord_list"]
        chord_base_term = base_chord_dict["chord_base_term"]
        if base_chord_dict["move5"]:
            adjust_info.move(5, base_chord_dict["move5"])
        if base_chord_dict["move9"]:
            adjust_info.move(9, base_chord_dict["move9"])
        if base_chord_dict["move11"]:
            adjust_info.move(11, base_chord_dict["move11"])
        if base_chord_dict["move13"]:
            adjust_info.move(13, base_chord_dict["move13"])
        if base_chord_dict["is_add2"]:
            adjust_info.add(2)
        if base_chord_dict["is_add4"]:
            adjust_info.add(4)
        if base_chord_dict["is_add6"]:
            adjust_info.add(6)
        if base_chord_dict["is_add9"]:
            adjust_info.add(9)
        if base_chord_dict["is_add11"]:
            adjust_info.add(11)
        if base_chord_dict["is_add13"]:
            adjust_info.add(13)
        if base_chord_dict["sus"]:
            adjust_info.sus(base_chord_dict["sus"])

        from chord.when_init import decode_ajust
        adjust_info = decode_ajust.decode(chord_term_list[1:], adjust_info)
        is_valid = True
    else:
        pass


if __name__ == '__main__':
    init_process(1, 5, ["maj7", "+5", "add2", "sus", "/e", "omit3"])
    # print(chord_list)
    # print(chord_base_term)
    # a = Note()
    # print(a.sharp_or_flat_adjust(3))
    print(adjust_info)
    print(chord_base_term)
    [print(i.math_name, i.octave) for i in chord_base_list if i]
