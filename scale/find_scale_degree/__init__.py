#!/usr/bin/env python
# @Time    : 2021/11/5 9:56 下午
# @Author  : guo2018@88.com
from note import Note


def find_degree3(degree_int: int, scale_list: list[Note]):
    note1_index = degree_int - 1

    def index_check(index_int):
        if index_int > 6:
            return index_int - 7
        if index_int < 0:
            return index_int + 7
        return index_int

    note2_index = index_check(note1_index + 2)
    note3_index = index_check(note2_index + 2)
    return [scale_list[note1_index], scale_list[note2_index], scale_list[note3_index]]


def find_degree7(degree_int: int, scale_list: list[Note]):
    note1_index = degree_int - 1

    def index_check(index_int):
        if index_int > 6:
            return index_int - 7
        if index_int < 0:
            return index_int + 7
        return index_int

    note2_index = index_check(note1_index + 2)
    note3_index = index_check(note2_index + 2)
    note4_index = index_check(note3_index + 2)
    return [scale_list[note1_index], scale_list[note2_index], scale_list[note3_index], scale_list[note4_index]]
