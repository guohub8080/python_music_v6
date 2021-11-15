#!/usr/bin/env python
# @Time    : 2021/11/5 11:07 下午
# @Author  : guo2018@88.com
from scale import Scale
from produce_score import Score, Part
from note import Note, Rest_Note
import random
from produce_score.function_tool.random_tool import random_list_with_weight
from produce_score.function_tool.produce_score_elements import produce_note

a_scale = Scale(8,4,"AEO")
print(a_scale)
print(a_scale.scale_list)

the_score = Score()
the_score.bpm = 120
the_score.key_signature = a_scale.key_signature
the_score.tonic_name = a_scale.tonic_note
print(a_scale.tonic_note)
the_score.scale_name = a_scale.scale_name
the_score.measures_num_per_part = 64
the_score.measure_quarter_length = 4
the_score.time_signature = "4/4"

# 随机生成四个四分音符：
from produce_score.function_tool.random_tool import random_list_with_weight


def make_random_notes(rest_prob, notes_list, quarter_length, octave):
    from produce_score.function_tool.produce_score_elements import produce_note
    from produce_score.function_tool.random_tool import random_probability
    rest_pro = random_probability(rest_prob)
    if rest_pro:
        return produce_note(Rest_Note(), quarter_length=quarter_length)
    return produce_note(random.choice(notes_list).octave_shift_to(octave), quarter_length=random_list_with_weight())


# 随机生成和弦：
def make_random_chords(quarter_length):
    from random import random, randint
    from produce_score.function_tool.produce_score_elements import produce_column_chord
    the = produce_column_chord([x.octave_shift(0) for x in a_scale.scale_degree_chord7(randint(1, 6))], i)
    the.quarterLength = quarter_length
    return the


whole_quarter_length = the_score.measures_num_per_part * the_score.measure_quarter_length


def slice_quarter_length(whole_quarter_length):
    quarter_length_list = []
    while whole_quarter_length >= 0.5:
        the_length = random_list_with_weight()
        quarter_length_list.append(the_length)
        whole_quarter_length -= the_length
    quarter_length_list.append(whole_quarter_length)
    return quarter_length_list


part1 = Part()
part1_length = slice_quarter_length(whole_quarter_length)

for i in part1_length:
    part1.notes_content.append(make_random_notes(0.2, a_scale.scale_list, i, random.randint(4, 5)))

part2 = Part()
part2_length = slice_quarter_length(whole_quarter_length)
for i in part2_length:
    part2.notes_content.append(make_random_notes(0.15, a_scale.scale_list, i, random.randint(4, 5)))

part3 = Part()
part3_length = slice_quarter_length(whole_quarter_length)
for i in part3_length:
    part3.notes_content.append(make_random_notes(0.1, a_scale.scale_list, i, random.randint(4, 5)))

part4 = Part()
part4_length = slice_quarter_length(whole_quarter_length)
for i in part4_length:
    part4.notes_content.append(make_random_notes(0.1, a_scale.scale_list, i, random.randint(4, 5)))

# part2 = Part()
# part2_length = slice_quarter_length(whole_quarter_length)
# for i in part2_length:
#     part2.notes_content.append(make_random_chords(random.randint(2, 4)))

the_score.part_content.append(part1)
the_score.part_content.append(part2)
the_score.part_content.append(part3)
the_score.part_content.append(part4)
the_score.render(is_show=True)
