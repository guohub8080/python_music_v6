#!/usr/bin/env python
# @Time    : 2021/11/15 8:35 下午
# @Author  : guo2018@88.com
from chord.CHORD_META import Adjust_Chord
from note import Note


def show(root_note_art_name: str, chord_base_term: str, adjust_info: Adjust_Chord, additional_notes: list[Note],
         most_low_note_name: str):
    chord_term = ""
    if chord_base_term == "maj3":
        pass
    elif chord_base_term == "min3":
        chord_term = "m"
        if adjust_info.adjust_sus == 2:
            chord_term = ""
        elif adjust_info.adjust_sus == 4:
            chord_term = ""
    elif chord_base_term == "aug3":
        chord_term = "+"
    elif chord_base_term == "dim3":
        chord_term = "°"
    elif chord_base_term == "maj7":
        chord_term = "M7"
    elif chord_base_term == "min7":
        chord_term = "m7"
    elif chord_base_term == "dom7":
        chord_term = "7"
    elif chord_base_term == "dim7":
        chord_term = "°7"
    elif chord_base_term == "half_dim7":
        chord_term = "ø"
    elif chord_base_term == "mm7":
        chord_term = "mM7"
    elif chord_base_term == "maj9":
        chord_term = "M9"
    elif chord_base_term == "min9":
        chord_term = "m9"
    elif chord_base_term == "dom9":
        chord_term = "9"
    elif chord_base_term == "aug9":
        chord_term = "+9"
    elif chord_base_term == "mm9":
        chord_term = "mM9"
    elif chord_base_term == "maj11":
        chord_term = "M11"
    elif chord_base_term == "min11":
        chord_term = "m11"
    elif chord_base_term == "dom11":
        chord_term = "11"
    elif chord_base_term == "aug11":
        chord_term = "+11"
    elif chord_base_term == "mm11":
        chord_term = "mM11"
    elif chord_base_term == "maj13":
        chord_term = "M13"
    elif chord_base_term == "min13":
        chord_term = "m13"
    elif chord_base_term == "dom13":
        chord_term = "13"
    elif chord_base_term == "aug13":
        chord_term = "+13"
    elif chord_base_term == "mm13":
        chord_term = "mM13"

    if adjust_info.adjust_sus == 2:
        chord_term = chord_term.__add__("sus2")
        adjust_info.adjust_omit[2] = False
        adjust_info.adjust_add[1] = False
    if adjust_info.adjust_sus == 4:
        adjust_info.adjust_omit[2] = False
        adjust_info.adjust_add[3] = False
        chord_term = chord_term.__add__("sus4")

    add_list = []
    omit_list = []
    move_list = []
    for i in range(13):
        if adjust_info.adjust_add[i]:
            add_list.append(f"add{i + 1}")
        if adjust_info.adjust_omit[i]:
            omit_list.append(f"omit{i + 1}")
        if adjust_info.adjust_move[i]:
            if adjust_info.adjust_move[i] > 0:
                move_list.append(f"♯{i + 1}")
            elif adjust_info.adjust_move[i] < 0:
                move_list.append(f"♭{i + 1}")
    all_vary_list = add_list + omit_list + move_list
    vary_term = ",".join(all_vary_list)
    if vary_term:
        vary_term = f"({vary_term})"
    else:
        vary_term = ""
    final_term = root_note_art_name.__add__(chord_term).__add__(vary_term)
    if adjust_info.inversion_uid:
        final_term = final_term.__add__("/").__add__(Note(adjust_info.inversion_uid).art_name)
    elif adjust_info.inversion_type:
        final_term = final_term.__add__("/").__add__(most_low_note_name)

    if additional_notes:
        final_term.__add__(f"(add {','.join([i.art_name for i in additional_notes])})")

    return final_term
