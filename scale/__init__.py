#!/usr/bin/env python
# @Time    : 2021/11/20 10:16 下午
# @Author  : guo2018@88.com

from common.settings import CENTER_C_LOCATION
from note import Note


class Scale(object):
    def __init__(self, tonic_uid: [int, str, None] = None, tonic_octave=CENTER_C_LOCATION, scale_term="ION"):
        if not tonic_uid:
            tonic_uid = 1
        # 输入的根音：
        self.input_tonic_instance = Note(tonic_uid, tonic_octave)
        self._scale_term = scale_term
        from scale import when_init
        when_init.get_info(tonic_uid, tonic_octave, scale_term)

        # 实际的根音：
        self._scale_name = when_init.scale_name
        self._scale_description = when_init.scale_description
        self.tonic_note = when_init.tonic_note

        self.is_trans = when_init.is_trans
        self.key_signature = when_init.key_signature
        self._scale_list = when_init.scale_list

    @property
    def scale_description(self):
        return self._scale_description

    @property
    def scale_name(self):
        return self._scale_name

    @property
    def scale_list(self):
        return self._scale_list

    def octave_shift(self, shift_int=0):
        if shift_int:
            return Scale(self.tonic_note.uid, self.tonic_note.octave + shift_int, self._scale_term)
        return self

    # 直接找到调内三和弦：
    def degree_chord3(self, rank_int: int):
        from scale.find_degree_chord import find_degree3
        return find_degree3(self.scale_list, rank_int)

    # 直接找到调内七和弦：
    def degree_chord7(self, rank_int: int):
        from scale.find_degree_chord import find_degree7
        return find_degree7(self.scale_list, rank_int)

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


# 自定义音阶（待开发使用）：
# class Customize_Scale(Scale):
#     def __init__(self, tonic_uid: [int, str, None] = None, tonic_octave=CENTER_C_LOCATION, base_scale_term="ION"):
#         super(Customize_Scale, self).__init__(tonic_uid, tonic_octave, base_scale_term)
#
#     @property
#     def scale_list(self):
#         return ":"
#
#     def __str__(self):
#         return "hehe"


if __name__ == '__main__':
    a = Scale(1, 5, "ION")
    # print(a.scale_list)
    # print(a.degree_chord3(7))
    print(a.degree_chord7(3))
