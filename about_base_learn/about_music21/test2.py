#!/usr/bin/env python
# @Time    : 2021/11/2 10:30 下午
# @Author  : guo2018@88.com
from copy import deepcopy

import music21

h1_score = music21.stream.Score()

h2_part_1 = music21.stream.Part()
h2_part_2 = music21.stream.Part()

h3_stream_1 = music21.stream.Stream()
h3_stream_2 = music21.stream.Stream()

h4_measure_1 = music21.stream.Measure()
h4_measure_2 = music21.stream.Measure()

note1 = music21.note.Note("C5")
note1.addLyric("C5")
note2 = music21.note.Note("D5")
note2.addLyric("D5")
note3 = music21.note.Note("E5")
note3.addLyric("E5")
note4 = music21.note.Note("G5")
note4.addLyric("G5")

h4_measure_1.append(deepcopy(note3))
h4_measure_1.append(deepcopy(note2))
h4_measure_1.append(deepcopy(note4))
h4_measure_1.append(deepcopy(note1))

h4_measure_2.append(deepcopy(note1))
h4_measure_2.append(deepcopy(note4))
h4_measure_2.append(deepcopy(note3))
h4_measure_2.append(deepcopy(note2))

h3_stream_1.append(deepcopy(h4_measure_2))
h3_stream_1.append(deepcopy(h4_measure_2))
h3_stream_2.append(deepcopy(h4_measure_1))
h3_stream_2.append(deepcopy(h4_measure_1))

h2_part_1.append(deepcopy(h3_stream_1))
h2_part_1.append(deepcopy(h3_stream_1))
h2_part_2.append(deepcopy(h3_stream_2))
h2_part_2.append(deepcopy(h3_stream_2))
h2_part_2.clef=music21.clef.FClef()
h1_score.append(h2_part_1)
h1_score.append(h2_part_2)
h1_score.show()
