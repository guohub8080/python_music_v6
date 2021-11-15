#!/usr/bin/env python
# @Time    : 2021/11/3 7:09 下午
# @Author  : guo2018@88.com

from note import Note, Rest_Note


# 生成单个音符（包括休止符）：
def produce_note(note_instance: [Note, Rest_Note], quarter_length=1.0, add_rank=0, add_name=True):
    music21_instance = note_instance.music21_instance
    if add_name:
        if isinstance(note_instance, Note):
            music21_instance.addLyric(note_instance.art_name)
        elif isinstance(note_instance, Rest_Note):
            music21_instance.addLyric("0")
    if add_rank:
        music21_instance.addLyric(add_rank)
    music21_instance.quarterLength = quarter_length
    return music21_instance


# 生成柱式和弦：
def produce_column_chord(chord_list: list[Note, object], chord_term: [None, str, int], quarter_length=1.0,
                         chord_rank=0):
    from music21.chord import Chord

    the_chord = Chord()
    for single_note in chord_list:
        if isinstance(single_note, Note):
            m21_instance = produce_note(single_note, add_name=False)
            the_chord.add(m21_instance)
        else:
            the_chord.add(single_note)
    if chord_term:
        the_chord.addLyric(chord_term)
    if chord_rank:
        the_chord.addLyric(chord_rank)
    the_chord.quarterLength = quarter_length
    return the_chord


# 生成三连音（可包含休止符）：
def produce_triplet(notes_list: [list[Note, Rest_Note], Note],
                    quarter_length_list: [list[float, int], None] = None,
                    rank_list: [list[int], None] = None):
    if not quarter_length_list:
        quarter_length_list = [1 / 3, 1 / 3, 1 / 3]
    if not rank_list:
        rank_list = [0, 0, 0]
    if isinstance(notes_list, Note):
        from copy import deepcopy
        notes_list = [deepcopy(notes_list), deepcopy(notes_list), deepcopy(notes_list)]
    if isinstance(notes_list, list) and len(notes_list) == len(quarter_length_list) == len(rank_list) == 3:
        final_list = []
        for v, i in enumerate(notes_list):
            note_m21_instance = produce_note(i, quarter_length=quarter_length_list[v], add_rank=rank_list[v])
            final_list.append(note_m21_instance)
        return final_list
    raise AttributeError("三连音必须是三个！")


if __name__ == '__main__':
    a = Note("C+1", 4)
    # produce_note(a, 1.5, 4).show()
    # produce_note(Rest_Note(), 5).show()
    b = Note("E", 4)
    c = Note("G-1", 4)
    # the_li = [a, b, c]
    # produce_column_chord(the_li, "C", 2, 7).show()
    # print(type(1 / 3))
    d = Rest_Note()
    import music21

    meae1 = music21.stream.Measure()
    for i in produce_triplet(c, [2 / 3, 5 / 3, 2 / 3]):
        meae1.append(i)
    # meae1.show()
    meae1.write("musicxml", "1.mxl")
