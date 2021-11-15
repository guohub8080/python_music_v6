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
        self.is_valid = False
        from chord.when_init import init_process
        init_process(root_note_uid_or_math_name, root_note_octave, chord_term_list)
        self.non = None

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
    a = Chord()
    print(a)
