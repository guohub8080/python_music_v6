#!/usr/bin/env python
# @Time    : 2021/11/3 7:04 下午
# @Author  : guo2018@88.com
from common.settings import CENTER_C_LOCATION
from note import Note


class Scale(object):
    def __init__(self, tonic_uid=1, tonic_octave=CENTER_C_LOCATION, scale_term="ION"):
        self.input_tonic_instance = Note(tonic_uid, tonic_octave)
        self.scale_name = None
        self.tonic_note = None
        self.tonic_uid = tonic_uid
        self.tonic_octave = tonic_octave
        self.is_trans = False
        self.is_valid = False
        self.key_signature = 0
        self.scale_list = None
        self.tonic_instance = None
        self.scale_description = None
        from common.scale_old import when_init
        when_init.get_info(tonic_uid, tonic_octave, scale_term)
        if when_init.is_valid:
            self.scale_name = when_init.scale_name
            self.is_valid = True
            self.tonic_uid = when_init.tonic_uid
            self.is_trans = when_init.is_trans
            self.key_signature = when_init.key_signature
            self.scale_list = when_init.scale_list
            self.tonic_instance = when_init.tonic_instance
            self.scale_description = when_init.scale_description
            self.tonic_note = when_init.tonic_note

    # 三级和弦级数：
    def scale_degree_chord3(self, degree_int):
        from common.scale_old.find_scale_degree import find_degree3
        return find_degree3(degree_int, self.scale_list)

    # 七级和弦级数：
    def scale_degree_chord7(self, degree_int):
        from common.scale_old.find_scale_degree import find_degree7
        return find_degree7(degree_int, self.scale_list)

    def __str__(self):
        if self.is_valid:
            signature_words = "升"
            if self.key_signature < 0:
                signature_words = "降"
            from prettytable import PrettyTable
            print(f"{self.input_tonic_instance.art_name}_{self.input_tonic_instance.octave}"
                  f"的{self.scale_name}音阶有[ {abs(self.key_signature)} ]个[ {signature_words} ]号，具体内容是：")
            if self.is_trans:
                print(f"主音已变更为{self.tonic_instance.art_name}_{self.tonic_instance.octave}：")
            table = PrettyTable(["index", "art_name", "octave"])
            for v, i in enumerate(self.scale_list, 1):
                table.add_row([
                    v, i.art_name, i.octave
                ])
            print(table)
            return ""
        return ""


if __name__ == '__main__':
    a = Scale(6, 5, "ION")
    print(a)
    b = a.scale_degree_chord7(4)
    for i in b:
        print(i)
