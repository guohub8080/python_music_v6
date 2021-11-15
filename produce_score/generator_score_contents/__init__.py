#!/usr/bin/env python
# @Time    : 2021/11/5 3:55 下午
# @Author  : guo2018@88.com

from produce_score import Score, Part, Measure
from note import Note, Rest_Note


# 需要说明的是，这个模块是创作模块，即根据乐理进行创作。
def final_generator():
    the_score = Score()
    the_score.bpm = 200

    # 每个小节的四分音符数：
    notes_num_in_measures = 5

    # 小节数：
    measure_num = 64
    for part_single in range(4):
        part_instance = Part()
        from produce_score.function_tool import deal_part_meta
        part_instance = deal_part_meta.execute(part_instance, )
        for measure_single in range(measure_num):
            measure_instance = Measure()
            for note_single in range(notes_num_in_measures):
                the_note_instance = make_q_notes()
                measure_instance.note_content.append(the_note_instance)
            part_instance.measure_content.append(measure_instance)
        the_score.part_content.append(part_instance)
    the_score.render(is_show=True)
