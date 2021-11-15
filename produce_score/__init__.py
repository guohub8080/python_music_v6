#!/usr/bin/env python
# @Time    : 2021/11/3 3:59 下午
# @Author  : guo2018@88.com
import random

from note import Note, Rest_Note
from produce_score import SCORE_META


class Score(object):
    def __init__(self,
                 time_signature: [None, str] = None,
                 bpm: [int, float, None] = None,
                 tonic_name: [None, str] = None,
                 scale_name: [None, str] = None, key_signature=0,
                 measure_quarter_length=0,
                 measures_num_per_part=0):
        # 拍号：
        self.time_signature = time_signature
        if not time_signature:
            self.time_signature = SCORE_META.TIME_SIGNATURE
        # 速度：
        self.bpm = bpm
        if not bpm:
            self.bpm = SCORE_META.BPM

        # 主音音名：
        self.tonic_name = tonic_name
        # 音阶（例如是C大调还是A小调）：
        self.scale_name = scale_name
        # 升降号有几个：
        self.key_signature = key_signature

        # Part包：（后续会有命令告诉如何添加）
        self.part_content = []

        self.score_instance = None

        # 每小节的四分音符长度：
        self.measure_quarter_length = measure_quarter_length
        if not measure_quarter_length:
            self.measure_quarter_length = SCORE_META.MEASURE_QUARTER_LENGTH
        # 每部分都有多少小节：
        self.measures_num_per_part = measures_num_per_part
        if not measures_num_per_part:
            self.measures_num_per_part = SCORE_META.MEASURES_NUM_PER_PART

    @property
    def title(self):
        return f"{SCORE_META.TITLE}\n{self.tonic_name}{self.scale_name}"

    @property
    def composer(self):
        return SCORE_META.COMPOSER

    def render(self, is_show=False):
        if not self.score_instance:
            from produce_score.function_tool.produce_score_structure import produce_score
            self.score_instance = produce_score(self)
            self.render(is_show=is_show)
        elif hasattr(self.score_instance, "write") and hasattr(self.score_instance, "show"):
            if not SCORE_META.RENDER_LOCATION.exists():
                SCORE_META.RENDER_LOCATION.mkdir(parents=True)
            self.score_instance.write("musicxml", SCORE_META.RENDER_LOCATION.joinpath(f"{SCORE_META.TITLE}.xml"))
            print("生成文件成功。")
            if is_show:
                self.score_instance.show()
            return self
        else:
            print("乐谱对象生成有误，请检查错误！")
        return None


class Part(object):
    def __init__(self, is_F_clef: bool = False, part_name: [None, str] = None
                 ):
        self.is_F_clef = is_F_clef
        self.part_name = part_name
        self.notes_content = []


if __name__ == '__main__':
    the_score = Score()
    the_score.bpm = 200


    # 随机生成四个四分音符：
    def make_q_notes(rest_prob):
        from produce_score.function_tool.produce_score_elements import produce_note
        from random import randint
        from produce_score.function_tool.random_tool import random_probability
        rest_pro = random_probability(rest_prob)
        if rest_pro:
            return produce_note(Rest_Note())
        return produce_note(Note(randint(1, 7), randint(3, 5)))


    # 随机生成和弦：
    def make_q_chords():
        from random import random, randint
        chord_lsit = []
        for i in range(randint(3, 5)):
            chord_lsit.append(make_q_notes(0))
        from produce_score.function_tool.produce_score_elements import produce_column_chord
        return produce_column_chord(chord_lsit, "")


    # 每个小节的四分音符数：
    notes_num_in_measures = 5

    # 小节数：
    measure_num = 64
    for part_single in range(4):
        part_instance = Part()
        for notes in range(notes_num_in_measures * measure_num):
            next_level = random.choice([make_q_chords(), make_q_notes(random.random())])
            part_instance.notes_content.append(next_level)
        the_score.part_content.append(part_instance)
    the_score.render(is_show=True)
