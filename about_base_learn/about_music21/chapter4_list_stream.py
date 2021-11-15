#!/usr/bin/env python
# @Time    : 2021/8/22 2:34 下午
# @Author  : guo2018@88.com
from copy import copy, deepcopy

import music21
from music21 import *

# note1 = note.Note("C4")
# note2 = note.Note("F#4")
# note1.quarterLength = 2
# note2.quarterLength = 1
#
# noteList = [note1, note2]
# note3 = note.Note("B-2")
# noteList.append(note3)
#
# stream1 = stream.Stream()
#
# stream1.append(note1)
# stream1.append(note2)
# stream1.append(note3)
# stream1.show()
#
# stream2 = stream.Stream()
# n3 = note.Note('D#5')  # octave values can be included in creation arguments
# stream2.repeatAppend(n3, 4)
# # stream2.show()
# # stream1.show()
# print(stream1.analyze('ambitus'))

# 添加第一个小节：
measure1 = music21.stream.Measure()

measure1.append(music21.meter.TimeSignature("6/8"))
measure1.append(music21.note.Note("C#5"))
measure1.append(music21.note.Note("D5"))
measure1.append(music21.note.Note("D5"))
measure1.append(music21.note.Note("D5"))
measure1.append(music21.note.Note("D5"))
measure1.append(music21.note.Note("D5"))

# 添加第二个小节：
measure2 = music21.stream.Measure()
measure2.append(music21.meter.TimeSignature("3/4"))  # 注意这里
measure2.append(music21.note.Note("C#5"))
measure2.append(music21.note.Note("D4"))
measure2.append(music21.note.Note("E4"))
measure2.append(music21.note.Rest())  # 这里是休止符
measure2.append(music21.note.Note("G5"))
measure2.append(music21.note.Note("D4"))

total_whole_score = music21.stream.Score()
total_whole_score.append(music21.tempo.MetronomeMark(number=20))
score_meta = music21.metadata.Metadata()  # 先生成一个元对象数据，再更改
score_meta.title = "方块郭的Python乐谱"
score_meta.composer = "我是方块郭"


# print(dir(score_meta))
total_whole_score.metadata = score_meta
part1 = music21.stream.Part()

part1.keySignature = music21.key.KeySignature(5)


part1.append(music21.clef.TenorClef())
part1.append(measure1)
part1.append(measure2)
part1.append(deepcopy(measure2))
part1.append(deepcopy(measure2))
part1.append(deepcopy(measure2))
part1.partName = "Part1"
# print(dir(part1))


part2 = music21.stream.Part()
part2.keySignature = music21.key.KeySignature(-3)
part2.append(music21.clef.CClef())
part2.append(measure2)
part2.append(measure1)
part2.append(deepcopy(measure1))
part2.append(deepcopy(measure1))
part2.append(deepcopy(measure1))

total_whole_score.append(part1)
total_whole_score.append(part2)
total_whole_score.append(music21.tempo.MetronomeMark(number=20))
# total_whole_score.show()
total_whole_score.write("midi","11.midi")