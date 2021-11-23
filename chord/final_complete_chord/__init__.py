#!/usr/bin/env python
# @Time    : 2021/11/19 11:27 下午
# @Author  : guo2018@88.com
from copy import deepcopy

from note import Note


def show_final(chord_complete_list_without_inversion, inversion_uid, inversion_type, additional_notes):
    chord_list = deepcopy(sorted([i for i in chord_complete_list_without_inversion if i], key=lambda x: x.semitone))
    if inversion_uid and not inversion_type:
        flag = -1
        for v, i in enumerate(chord_list):
            if v > 0:
                if i.uid == inversion_uid:
                    flag = chord_list.index(i)
                    break
        if flag > -1:
            for i in range(len(chord_list)):
                if i < flag:
                    chord_list[i] = chord_list[i].octave_shift(1)
        else:
            the_most_low_note = Note(inversion_uid, chord_list[0].octave)
            while the_most_low_note.semitone > chord_list[0].semitone:
                the_most_low_note = the_most_low_note.octave_shift(-1)
            chord_list.append(the_most_low_note)
    elif inversion_type and not inversion_uid:
        # inversion_times = inversion_type % len(chord_list)
        # # print(inversion_times)
        # if inversion_times != 0:
        for i in range(inversion_type):
            chord_list[i] = chord_list[i].octave_shift(1)
        # elif inversion_times == 0:
        #     pass
    elif inversion_type and inversion_uid:
        raise TypeError("转位和弦名称和第几转位不能共存！")
    chord_list.extend(additional_notes)
    chord_list = sorted(chord_list, key=lambda x: x.semitone)
    return chord_list


if __name__ == '__main__':
    list1 = [Note("C"), 0, Note("E"), 0, Note("G")]
    print()
    [print(i.math_name, i.octave) for i in show_final(list1, 3, 0, [])]
