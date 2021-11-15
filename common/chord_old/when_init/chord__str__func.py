#!/usr/bin/env python
# @Time    : 2021/8/26 11:04 上午
# @Author  : guo2018@88.com
from note import Note


def show_chord_content(the_list):
    # type:([Note])->None
    from prettytable import PrettyTable
    table = PrettyTable(["order", "math_name", "art_name", "octave", "MIDI_Value"])
    table.header_style = "title"
    for i in range(len(the_list)):
        list_index = len(the_list) - 1 - i
        table.add_row([
            list_index + 1,
            the_list[list_index].math_name,
            the_list[list_index].art_name,
            the_list[list_index].octave,
            the_list[list_index].semitone
        ])
    print(table)
    return ""
