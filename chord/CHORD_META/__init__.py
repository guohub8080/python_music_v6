#!/usr/bin/env python
# @Time    : 2021/11/12 2:27 下午
# @Author  : guo2018@88.com

# 三和弦：
import pandas

maj3 = ""
min3 = "m"
aug3 = "aug"
dim3 = "dim"

# 七和弦：
maj7 = "maj7"
min7 = "m7"
dom7 = "7"
mm7 = "mM7"

aug_maj7 = "aug_maj7"
aug_min7 = "aug_min7"
half_dim7 = "ø"

# 九和弦
min9 = "m9"


class Adjust_Chord(object):
    def __init__(self):
        self._adjust_add = [False for i in range(13)]
        self._adjust_move = [0 for i in range(13)]
        self._adjust_omit = [False for i in range(13)]
        self._adjust_sus = 0
        self._inversion_uid = 0
        self._inversion_type = 0

    def add(self, add_note_interval: int):
        self._adjust_add[add_note_interval - 1] = True
        return self

    def move(self, move_note_interval: int, move_semitone: int):
        self._adjust_move[move_note_interval - 1] += move_semitone
        return self

    def move_to(self, move_note_interval: int, move_target: int):
        self._adjust_move[move_note_interval - 1] = move_target
        return self

    def omit(self, omit_note_interval: int):
        self._adjust_omit[omit_note_interval - 1] = True
        return self

    def sus(self, sus_num=2):
        self._adjust_sus = sus_num
        return self

    def inversion_on_uid(self, inversion_uid: int):
        self._inversion_uid = inversion_uid
        return self

    def inversion_on_math_name(self, math_name: str):
        from note import Note
        self._inversion_uid = Note(math_name).uid
        return self

    def inversion_on_index(self, inversion_index: int):
        self._inversion_type = inversion_index
        return self

    def __str__(self):
        print([u for u in self._adjust_move])
        print([u for u in self._adjust_add])
        print([u for u in self._adjust_omit])
        print("sus:", self._adjust_sus)
        print(self._inversion_uid)
        print(self._inversion_type)
        return ""


if __name__ == '__main__':
    a = Adjust_Chord()
    print(a)
    print("---")
    a.add(2)
    print(a)
