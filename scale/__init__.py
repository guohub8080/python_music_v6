#!/usr/bin/env python
# @Time    : 2021/11/20 10:16 下午
# @Author  : guo2018@88.com

from common.settings import CENTER_C_LOCATION
from note import Note


class Scale(object):
    def __init__(self, tonic_uid=1, tonic_octave=CENTER_C_LOCATION, scale_term="ION"):
        # 输入的根音：
        self.input_tonic_instance = Note(tonic_uid, tonic_octave)
        self._scale_term = scale_term
        from scale import when_init
        when_init.get_info(tonic_uid, tonic_octave, scale_term)

        # 实际的根音：
        self.scale_name = when_init.scale_name
        self.scale_description = when_init.scale_description
        self.tonic_note = when_init.tonic_note

        self.is_trans = when_init.is_trans
        self.key_signature = when_init.key_signature
        self.scale_list = when_init.scale_list

    def octave_shift(self, shift_int=0):
        if shift_int:
            return Scale(self.tonic_note.uid, self.tonic_note.octave + shift_int, self._scale_term)
        return self

    def __str__(self):
        signature_words = "升"
        if self.key_signature < 0:
            signature_words = "降"
        from prettytable import PrettyTable
        print(f"{self.input_tonic_instance.art_name}_{self.input_tonic_instance.octave}"
              f"的{self.scale_name}音阶有[ {abs(self.key_signature)} ]个[ {signature_words} ]号，具体内容是：")
        if self.is_trans:
            print(f"主音已变更为{self.tonic_note.art_name}_{self.tonic_note.octave}：")
        table = PrettyTable(["index", "art_name", "octave"])
        for v, i in enumerate(self.scale_list, 1):
            table.add_row([
                v, i.art_name, i.octave
            ])
        print(table)
        return ""


if __name__ == '__main__':
    a = Scale(16, 5, "ION")
    print(a)
