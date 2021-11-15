#!/usr/bin/env python
# @Time    : 2021/11/2 11:22 下午
# @Author  : guo2018@88.com

import music21

the_chord = music21.chord.Chord()
note1 = music21.note.Note("C4")
note2 = music21.note.Note("E#4")
note3 = music21.note.Note("G#4")
the_chord.add(note1)
the_chord.add(note2)
the_chord.add(note3)
the_chord.quarterLength = 3

score1 = music21.stream.Score()
score1.append(the_chord)
score1.append(music21.note.Note("F"))
score1.append(music21.note.Note("A"))
score1.show()
