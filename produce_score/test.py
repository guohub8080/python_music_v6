#!/usr/bin/env python
# @Time    : 2021/11/6 1:32 下午
# @Author  : guo2018@88.com
import music21
from music21 import stream,note
# score = music21.stream.Score()
#
# a=score.m
# part = music21.stream.Part()

# measure1 = music21.stream.Measure()
# measure2 = music21.stream.Measure()
# note1 = music21.note.Note("C4")
# note1.tie = music21.tie.Tie("start")
# note2 = music21.note.Note("G4")
# note2.tie = music21.tie.Tie("stop")
#
# measure1.append(note1)
# measure2.append(note2)
#
# part.measure(1).notes[0].tie = music21.tie.Tie("start")
# part.measure(2).notes[0].tie = music21.tie.Tie("stop")
#
# part.append(measure1)
# part.append(measure2)
# print()
#
# score.append(part)
# score.show()
#
sSrc = stream.Score()
sPart=music21.stream.Part()
sPart.insert(0, music21.meter.TimeSignature('3/4'))
sPart.append(note.Note('C3', type='quarter'))
sPart.append(note.Note('D3', type='quarter'))
sPart.append(note.Note('E3', type='quarter'))
sPart.append(note.Note('f3', type='half'))
sPart.append(music21.bar.Barline())
sPart.append(note.Note('E3', type='quarter'))
sPart.append(note.Note('E3', type='quarter'))
sPart.append(note.Note('E3', type='quarter'))
sPart.append(note.Note('E3', type='quarter'))
sSrc.makeMeasures()


sPart2=music21.stream.Part()
sPart2.insert(0, music21.meter.TimeSignature('3/4'))
sPart2.append(note.Note('C5', type='eighth'))
sPart2.append(note.Note('C5', type='eighth'))
sPart2.append(note.Note('C5', type='eighth'))
sPart2.append(note.Note('C5', type='eighth'))
sPart2.append(note.Note('C5', type='quarter'))
sPart2.append(note.Note('D5', type='quarter'))
sPart2.append(note.Note('E5', type='quarter'))
sPart2.append(note.Note('f5', type='half'))
sPart2.append(note.Note('E5', type='quarter'))
sPart2.append(note.Note('E5', type='quarter'))
sPart2.append(note.Note('E5', type='quarter'))
sPart2.append(note.Note('E5', type='quarter'))
sSrc.append(sPart2)
sSrc.append(sPart)
sSrc.show()

# sScr = stream.Score()
# sPart = stream.Part()
# sPart.insert(0, music21.clef.TrebleClef())
# sPart.insert(0, music21.meter.TimeSignature('3/4'))
# sPart.append(note.Note('C4', quarterLength = 3.0))
# sPart.append(note.Note('D4', quarterLength = 3.0))
# sScr.insert(0, sPart)
# sScr.makeMeasures()
# # sScr.makeTies()
# sScr.makeChords()
# sScr.show()