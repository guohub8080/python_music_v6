#!/usr/bin/env python
# @Time    : 2021/8/30 8:52 下午
# @Author  : guo2018@88.com

from note import Note


def interval_between_notes(note1, note2):
    from common.utils.func_interval_between_notes import execute
    return execute(note1, note2)


if __name__ == '__main__':
    n1 = Note("C+2", 6)
    n2 = Note("G")
    a = interval_between_notes(n1, n2)
    print(a)
