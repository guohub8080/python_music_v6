#!/usr/bin/env python
# @Time    : 2021/8/22 2:34 下午
# @Author  : guo2018@88.com

import music21
from music21 import *

cMinor = chord.Chord(["C4", "G4", "E-5"])
cMinor.quarterLength = 2
# cMinor.show()
# cClosed = cMinor.closedPosition()
# cClosed.show()

d = note.Note('D4')
fSharp = note.Note('F#4')
a = note.Note('A5')
dMajor = chord.Chord([d, fSharp, a])

# dMajor.show()
e7 = chord.Chord("E4 G#4 B4 D5")
# e7.show()

b = corpus.parse('bach/bwv66.6')
b.show() # I've altered this so it's much shorter than it should be...

bChords = b.chordify()
bChords.show()
