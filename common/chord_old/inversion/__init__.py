#!/usr/bin/env python
# @Time    : 2021/8/30 12:26 上午
# @Author  : guo2018@88.com

# 和弦转位
from note import Note


def inversion(self, inversion_type):
    assert inversion_type in (1, 2, 3) and self.is_valid
    new_list: list[Note] = self.content
    if inversion_type >= 1:
        new_list[0] = new_list[0].octave_shift(1)
    if inversion_type >= 2:
        new_list[1] = new_list[1].octave_shift(1)
    if inversion_type == 3:
        new_list[2] = new_list[2].octave_shift(1)
    self.content = new_list
    return self
