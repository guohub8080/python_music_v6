#!/usr/bin/env python
# @Time    : 2021/8/22 2:34 下午
# @Author  : guo2018@88.com

import music21
from music21 import *

# f = note.Note()
# f.name="F"
# f.pitch.accidental=0
# # print(f)
# # #
# # print(f.name)
# # print(f.octave)
# f.octave=5
# print(f.pitch)
# print("//")
# print(f.pitch.accidental.alter)
# print(f.pitch.accidental.alter)
# print(f.pitch.accidental)
# # f.name = "g#"
# # print(f.name)
# # print(f)
# # print(f.pitch)
# # f.pitch.accidental = -2
# # print(f.pitch.accidental)
# # print(f.name)
# # print(f.pitch)
# # print(f.fullName)
# # print("-" * 50)
# print(f.pitch.accidental.alter)
# f.pitch.accidental.alter = 1
# print(f.pitch.accidental)
# f.show()
# # --------------------------------
# # the_note = note.Note()
# # the_note.name = "C"
# # the_note.pitch.accidental = 1
# # the_note.octave = 5
# # print(the_note.fullName)
# # the_note.show()
# # -------------------------
# # n1 = note.Note()
# # n1.name = "F"
# # n1.octave = 4
# # n1.pitch.accidental = -1
# # n1.quarterLength = 0.25
# #
# # n1.addLyric(n1.nameWithOctave)
# # n1.addLyric(n1.pitch.pitchClassString)
# # n1.addLyric(f'QL: {n1.quarterLength}')
# # n1.show()

m = music21.note.Note()
m.name = "B"
m.octave = 3
m.pitch.accidental = -2
print(m.fullName)
