#!/usr/bin/env python
# @Time    : 2021/11/15 8:59 下午
# @Author  : guo2018@88.com
from note import Note


def decode(adjust_list: list):
    if not adjust_list:
        return None
    # print("haha",adjust_list)
    final_dict = {
        "move2": 0,
        "move4": 0,
        "move5": 0,
        "move6": 0,
        "move7": 0,
        "move9": 0,
        "move11": 0,
        "move13": 0,
        "is_sus2": False,
        "is_sus4": False,
        "is_add2": False,
        "is_add4": False,
        "is_add6": False,
        "is_add9": False,
        "is_add11": False,
        "is_add13": False,
        "is_omit3": False,
        "is_omit5": False,
        "is_omit7": False,
        "is_omit9": False,
        "is_omit11": False,
        "inversion_uid": None,
        "inversion_type": 0}
    for each_adjust in adjust_list:
        if not each_adjust:
            continue
        if isinstance(each_adjust, dict):
            for i in each_adjust.keys():
                if i[:4] == "move":
                    final_dict[i] += each_adjust[i]
                else:
                    final_dict[i] = each_adjust[i]
        elif isinstance(each_adjust, str):
            if each_adjust[0] == "+" or each_adjust[0] == "#":
                if each_adjust[1:].isdigit():
                    move_int = int(each_adjust)
                    if move_int == 5:
                        final_dict["move5"] += 1
                    elif move_int == 2:
                        final_dict["move2"] += 1
                    elif move_int == 4:
                        final_dict["move4"] += 1
                    elif move_int == 6:
                        final_dict["move6"] += 1
                    elif move_int == 7:
                        final_dict["move7"] += 1
                    elif move_int == 9:
                        final_dict["move9"] += 1
                    elif move_int == 11:
                        final_dict["move11"] += 1
                else:
                    raise TypeError("+ chord wrong!")
            elif each_adjust[0] == "-" or each_adjust[0].lower() == "b":
                if each_adjust[1:].isdigit():
                    move_int = int(each_adjust)
                    if move_int == 5:
                        final_dict["move5"] -= 1
                    elif move_int == 2:
                        final_dict["move2"] -= 1
                    elif move_int == 4:
                        final_dict["move4"] -= 1
                    elif move_int == 6:
                        final_dict["move6"] -= 1
                    elif move_int == 7:
                        final_dict["move7"] -= 1
                    elif move_int == 9:
                        final_dict["move9"] -= 1
                    elif move_int == 11:
                        final_dict["move11"] -= 1
                else:
                    raise TypeError("- chord wrong!")
            elif each_adjust[:3].lower() == "sus":
                if len(each_adjust) == 3:
                    final_dict["is_sus2"] = True
                elif each_adjust.lower() == "sus2":
                    final_dict["is_sus2"] = True
                elif each_adjust.lower() == "sus4":
                    final_dict["is_sus4"] = True
                else:
                    raise TypeError("sus chord wrong!")
            elif each_adjust[:3].lower() == "add":
                if each_adjust[3:].isdigit():
                    add_int = int(each_adjust[3:])
                    if add_int == 2:
                        final_dict["is_add2"] = True
                    elif add_int == 4:
                        final_dict["is_add4"] = True
                    elif add_int == 6:
                        final_dict["is_add6"] = True
                    elif add_int == 9:
                        final_dict["is_add9"] = True
                    elif add_int == 11:
                        final_dict["is_add11"] = True
                    elif add_int == 13:
                        final_dict["is_add13"] = True
                else:
                    raise
            elif each_adjust[:4].lower() == "omit":
                if each_adjust[4:].isdigit():
                    omit_int = int(each_adjust[4:])
                    if omit_int == 3:
                        final_dict["is_omit3"] = True
                    elif omit_int == 5:
                        final_dict["is_omit5"] = True
                    elif omit_int == 7:
                        final_dict["is_omit7"] = True
                    elif omit_int == 9:
                        final_dict["is_omit9"] = True
                    elif omit_int == 11:
                        final_dict["is_omit11"] = True
                else:
                    raise
            elif each_adjust[0] == "/":
                the_note_instance = Note(each_adjust[1:])
                if the_note_instance:
                    if the_note_instance.is_valid:
                        final_dict["inversion_uid"] = the_note_instance.uid
                    else:
                        raise
                else:
                    raise

            elif each_adjust[:4].lower() == "num/":
                if each_adjust[4:].isdigit():
                    final_dict["inversion_type"] = int(each_adjust[2:])
            elif each_adjust[:4].lower() == "uid/":
                if each_adjust[4:].isdigit():
                    final_dict["inversion_type"] = int(each_adjust[2:])
        elif isinstance(each_adjust, int) or (isinstance(each_adjust, str) and each_adjust.isdigit()):
            if each_adjust == 5:
                final_dict["move5"] += 1
            elif each_adjust == 2:
                final_dict["is_add2"] = True
            elif each_adjust == 4:
                final_dict["is_add4"] = True
            elif each_adjust == 6:
                final_dict["is_add6"] = True
            elif each_adjust == 7:
                final_dict["move7"] += 1
            elif each_adjust == 9:
                final_dict["move9"] += 1
            elif each_adjust == 11:
                final_dict["move11"] += 1
            elif each_adjust == 13:
                final_dict["move13"] += 1
            elif each_adjust == -5:
                final_dict["move5"] -= 1
            elif each_adjust == -7:
                final_dict["move7"] -= 1
            elif each_adjust == -9:
                final_dict["move9"] -= 1
            elif each_adjust == -11:
                final_dict["move11"] -= 1
            elif each_adjust == -13:
                final_dict["move13"] -= 1

    return final_dict


if __name__ == '__main__':
    print(decode(
        []))
