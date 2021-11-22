#!/usr/bin/env python
# @Time    : 2021/11/22 8:23 下午
# @Author  : guo2018@88.com
from note import Note


def execute(score_term, chord_content: list[Note]):
    a = f"和弦{score_term}:"
    the_str = ""
    # print(self.chord_content)
    # asdasd = [i.math_name for i in self.chord_content]
    # print(asdasd)
    for i in range(len(chord_content)):
        the_str = the_str.__add__(f"{chord_content[i].art_name}_{chord_content[i].octave}")
        if i < len(chord_content) - 1:
            the_str = the_str.__add__("  ")
    # print(the_str)
    return a.__add__(the_str)
