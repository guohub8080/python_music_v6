#!/usr/bin/env python
# @Time    : 2021/11/11 10:40 下午
# @Author  : guo2018@88.com
from note import Note
from common.settings import CENTER_C_LOCATION
from chord.when_init import find_1_chord

is_valid = False
chord_list = None
chord_base_list = None
chord_base_term = None
move2 = None
move4 = None
move5 = None
move6 = None
move7 = None
move9 = None
move11 = None
move13 = None
is_sus2 = None
is_sus4 = None
is_add2 = None
is_add4 = None
is_add6 = None
is_add9 = None
is_add11 = None
is_add13 = None
is_omit3 = None
is_omit5 = None
is_omit7 = None
is_omit9 = None
is_omit11 = None

inversion_uid = None
inversion_type = 0


def init_process(root_note_uid_or_math_name=1, root_note_octave=CENTER_C_LOCATION,
                 chord_term_list: [None, list, str] = "maj3"):
    if isinstance(chord_term_list, str):
        chord_term_list = [chord_term_list]
    assert isinstance(chord_term_list, list)
    # 第一个一定是基本和弦类型：
    base_chord_dict = find_1_chord.execute(root_note_uid_or_math_name, root_note_octave, chord_term_list[0])
    if base_chord_dict:
        global chord_list, chord_base_term, move5, move9, move11, move13, is_sus2, is_sus4, is_add2, is_add4, is_add6
        global is_add9, is_add11, is_add13, is_omit3, is_omit5, is_omit7, is_omit9, is_omit11
        chord_list = base_chord_dict["chord_list"]
        chord_base_term = base_chord_dict["chord_base_term"]
        adjust_list = []
        if base_chord_dict["move5"]:
            adjust_list.append({"move5": base_chord_dict["move5"]})
        if base_chord_dict["move9"]:
            adjust_list.append({"move9": base_chord_dict["move9"]})
        if base_chord_dict["move11"]:
            adjust_list.append({"move11": base_chord_dict["move11"]})
        if base_chord_dict["move13"]:
            adjust_list.append({"move13": base_chord_dict["move13"]})

        # 解析变化：
        from chord.when_init import decode_ajust
        if adjust_list:
            chord_term_list.extend(adjust_list)
        decode_results = decode_ajust.decode(chord_term_list[1:])
        print(decode_results)
        # 应用变化：
        from chord.when_init import apply_adjust
        if decode_results:
            final_dict = apply_adjust.apply(chord_list, decode_results)
            if final_dict["is_valid"]:
                ...


if __name__ == '__main__':
    print(init_process(1, 5, "dom9-13"))
    # print(chord_list)
    # print(chord_base_term)
    # a = Note()
    # print(a.sharp_or_flat_adjust(3))
