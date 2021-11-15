#!/usr/bin/env python
# @Time    : 2021/11/3 7:10 下午
# @Author  : guo2018@88.com

import music21

note1 = music21.note.Note("C4")
measure1 = music21.stream.Measure()
measure1.append(note1)
part1 = music21.stream.Part()
part1.append(measure1)
score1 = music21.stream.Score()
score1.append(music21.tempo.MetronomeMark(number=20))
score1.append(part1)
m1 = music21.metadata.Metadata()
m1.title = "score1..."
m1.composer = "hehe"
# score1.metadata = m1
# score1.show()
stream1 = music21.stream.Stream()
stream1.append(score1)
stream1.metadata = m1
print(dir(stream1.metadata))

print(dir(music21.metadata.Metadata()))

stream1.show()
