#!/usr/bin/env python
# @Time    : 2021/11/15 8:59 下午
# @Author  : guo2018@88.com
from note import Note
from chord.CHORD_META import Adjust_Chord


def decode(adjust_list: list, adjust_info: Adjust_Chord):
    if not adjust_list:
        return adjust_info
    # print(adjust_list)

    for each_adjust in adjust_list:
        if not each_adjust:
            continue
        if isinstance(each_adjust, str):
            if each_adjust[0] == "+" or each_adjust[0] == "#":
                if each_adjust[1:].isdigit():
                    move_int = int(each_adjust)
                    if move_int == 5:
                        adjust_info.move(5, 1)
                    elif move_int == 2:
                        adjust_info.move(2, 1)
                    elif move_int == 4:
                        adjust_info.move(4, 1)
                    elif move_int == 6:
                        adjust_info.move(6, 1)
                    elif move_int == 7:
                        adjust_info.move(7, 1)
                    elif move_int == 9:
                        adjust_info.move(9, 1)
                    elif move_int == 11:
                        adjust_info.move(11, 1)
                else:
                    raise TypeError("+ chord wrong!")
            elif each_adjust[0] == "-" or each_adjust[0].lower() == "b":
                if each_adjust[1:].isdigit():
                    move_int = int(each_adjust)
                    if move_int == 5:
                        adjust_info.move(5, -1)
                    elif move_int == 2:
                        adjust_info.move(2, -1)
                    elif move_int == 4:
                        adjust_info.move(4, -1)
                    elif move_int == 6:
                        adjust_info.move(6, -1)
                    elif move_int == 7:
                        adjust_info.move(7, -1)
                    elif move_int == 9:
                        adjust_info.move(9, -1)
                    elif move_int == 11:
                        adjust_info.move(11, -1)
                else:
                    raise TypeError("- chord wrong!")
            elif each_adjust[:3].lower() == "sus":
                if len(each_adjust) == 3 or each_adjust.lower() == "sus2":
                    adjust_info.sus(2)
                elif each_adjust.lower() == "sus4":
                    adjust_info.sus(4)
                elif each_adjust.lower() == "sus4":
                    adjust_info.sus(0)
                else:
                    raise TypeError("sus chord wrong!")
            elif each_adjust[:3].lower() == "add":
                if each_adjust[3:].isdigit():
                    add_int = int(each_adjust[3:])
                    if add_int == 2:
                        adjust_info.add(2)
                    elif add_int == 4:
                        adjust_info.add(4)
                    elif add_int == 6:
                        adjust_info.add(6)
                    elif add_int == 9:
                        adjust_info.add(9)
                    elif add_int == 11:
                        adjust_info.add(11)
                    elif add_int == 13:
                        adjust_info.add(13)
                else:
                    raise
            elif each_adjust[:4].lower() == "omit":
                if each_adjust[4:].isdigit():
                    omit_int = int(each_adjust[4:])
                    if omit_int == 3:
                        adjust_info.omit(3)
                    elif omit_int == 5:
                        adjust_info.omit(5)
                    elif omit_int == 7:
                        adjust_info.omit(7)
                    elif omit_int == 9:
                        adjust_info.omit(9)
                    elif omit_int == 11:
                        adjust_info.omit(11)
                else:
                    raise
            elif each_adjust[0] == "/":
                the_note_instance = Note(each_adjust[1:])
                if the_note_instance:
                    if the_note_instance.is_valid:
                        adjust_info.inversion_on_uid(the_note_instance.uid)
                    else:
                        raise TypeError("please check the note name.")
                else:
                    raise TypeError("please check the note name.")

            elif each_adjust[:4].lower() == "num/":
                if each_adjust[4:].isdigit():
                    adjust_info.inversion_on_index(int(each_adjust[4:]))
            elif each_adjust[:4].lower() == "uid/":
                if each_adjust[4:].isdigit():
                    adjust_info.inversion_on_uid(int(each_adjust[4:]))
        elif isinstance(each_adjust, int) or (isinstance(each_adjust, str) and each_adjust.isdigit()):
            each_adjust = int(each_adjust)
            if each_adjust == 5:
                adjust_info.move(5, 1)
            elif each_adjust == 2:
                adjust_info.add(2)
            elif each_adjust == 4:
                adjust_info.add(4)
            elif each_adjust == 6:
                adjust_info.add(6)
            elif each_adjust == 7:
                adjust_info.move(7, 1)
            elif each_adjust == 9:
                adjust_info.move(9, 1)
            elif each_adjust == 11:
                adjust_info.move(11, 1)
            elif each_adjust == 13:
                adjust_info.move(13, 1)
            elif each_adjust == -5:
                adjust_info.move(5, -1)
            elif each_adjust == -7:
                adjust_info.move(7, -1)
            elif each_adjust == -9:
                adjust_info.move(9, -1)
            elif each_adjust == -11:
                adjust_info.move(11, -1)
            elif each_adjust == -13:
                adjust_info.move(13, -1)

    return adjust_info


if __name__ == '__main__':
    print(decode(
        [""]))
