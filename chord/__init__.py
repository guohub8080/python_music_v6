#!/usr/bin/env python
# @Time    : 2021/11/11 10:18 下午
# @Author  : guo2018@88.com

from note import Note
from common.settings import CENTER_C_LOCATION


# 我们期待如下的效果：
# Chord("C",5,"maj") -> C大三和弦
# Chord("C", 5, ["maj", "sus2", "add9"]) -> C挂二加九和弦（虽然这样是不存在的）


class Chord(object):
    def __init__(self, root_note_uid_or_math_name: [str, int] = 1, root_note_octave=CENTER_C_LOCATION,
                 chord_term_list: [str, list[str]] = "maj3"):
        from chord import when_init
        when_init.init_process(root_note_uid_or_math_name, root_note_octave, chord_term_list)
        self.is_valid = when_init.is_valid
        self.chord_base_list = when_init.chord_base_list
        self.chord_base_term = when_init.chord_base_term
        self.adjust_info = when_init.adjust_info

    def set_adjust(self, adjust_list: list):
        from chord.when_init.decode_ajust import decode
        self.adjust_info = decode(adjust_list, self.adjust_info)
        return self



    @property
    def score_term(self):
        return

    @property
    def show_chord(self):
        return

    def __str__(self):
        print("ok")
        return ""


def notes_list_to_chord(chord_list: list[Note]):
    return


if __name__ == '__main__':
    a = Chord(1, 5, "half_dim7")
    a.adjust_info.add(2).add(4)
    print(a.chord_base_list)
    print(a.adjust_info)
    print(a)
