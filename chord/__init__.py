#!/usr/bin/env python
# @Time    : 2021/11/11 10:18 下午
# @Author  : guo2018@88.com

from note import Note


class Chord(object):
    def __init__(self, chord_term_or_list: [None, str, list[Note]] = None):
        if chord_term_or_list is None:
            chord_term_or_list = "maj3"
        self.non = None

        from chord.when_init import init_process
        init_process(chord_term_or_list)
