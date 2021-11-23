#!/usr/bin/env python
# @Time    : 2021/11/23 11:10 上午
# @Author  : guo2018@88.com
from note import Note
from chord.chord_detector import base_prime_detector


def find_degree3(scale_list: list[Note], rank_int):
    ready_list = [None,
                  [0, 2, 4],
                  [1, 3, 5],
                  [2, 4, 6],
                  [3, 5, 0],
                  [4, 6, 1],
                  [5, 0, 2],
                  [6, 1, 3]]
    the_notes_content = [scale_list[i] for i in ready_list[rank_int]]
    # print(the_notes_content)
    return base_prime_detector(the_notes_content)


def find_degree7(scale_list: list[Note], rank_int):
    ready_list = [None,
                  [0, 2, 4, 6],
                  [1, 3, 5, 0],
                  [2, 4, 6, 1],
                  [3, 5, 0, 2],
                  [4, 6, 1, 3],
                  [5, 0, 2, 4],
                  [6, 1, 3, 5]
                  ]
    the_notes_content = [scale_list[i] for i in ready_list[rank_int]]
    # print(the_notes_content)
    return base_prime_detector(the_notes_content)
