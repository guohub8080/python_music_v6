#!/usr/bin/env python
# @Time    : 2021/9/13 3:10 下午
# @Author  : guo2018@88.com

def execute(note_name, note_octave, note_bias):
    from music21 import note
    the_note = note.Note()
    the_note.name = note_name[0]
    if not note_bias:
        the_note.pitch.accidental = None
    else:
        the_note.pitch.accidental = note_bias
    the_note.octave = note_octave
    return the_note
