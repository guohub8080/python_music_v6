#!/usr/bin/env python
# @Time    : 2021/11/11 10:40 下午
# @Author  : guo2018@88.com
from note import Note

is_valid = False
chord_content = None
chord_interval_list = None


def init_process(chord_term_or_list: [str, list[Note]]):
    if isinstance(chord_term_or_list, str):
        from chord.when_init.term_to_chord import execute
        the_chord = execute(chord_term_or_list)
        return
    if isinstance(chord_term_or_list, list):
        from chord.when_init.list_to_chord import execute
        return execute(chord_term_or_list)
