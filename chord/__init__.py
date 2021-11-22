#!/usr/bin/env python
# @Time    : 2021/11/11 10:18 下午
# @Author  : guo2018@88.com

from common.settings import CENTER_C_LOCATION
from note import Note
from copy import deepcopy


# 我们期待如下的效果：
# Chord("C",5,"maj") -> C大三和弦
# Chord("C", 5, ["maj", "sus2", "add9"]) -> C挂二加九和弦（虽然这样是不存在的）


class Chord(object):
    def __init__(self, root_note_uid_or_math_name: [str, int] = 1, root_note_octave=CENTER_C_LOCATION,
                 chord_term_list: [str, list[str], None] = None):
        if not chord_term_list:
            chord_term_list = "maj3"
        self._input_root_note_uid_or_math_name = root_note_uid_or_math_name
        self._input_root_note_octave = root_note_octave
        self._input_chord_term_list = chord_term_list
        from chord import when_init
        when_init.init_process(root_note_uid_or_math_name, root_note_octave, chord_term_list)
        self.is_valid = when_init.is_valid
        self._chord_base_list = when_init.chord_base_list
        self.chord_base_term = when_init.chord_base_term
        self.adjust_info = when_init.adjust_info
        # 这个是在和弦范围以外随便添加音符(因为和弦只支持13度，超出范围的只能通过这种方式来添加)：
        self.additional_notes = []
        # 和弦级数（一般是在和音阶合并使用过程中产生）
        self.rank_in_scale = 0

    # 已经生成好的一个和弦后，再次可以使用列表来改变和弦：
    def set_adjust(self, adjust_list: list):
        from chord.when_init.decode_ajust import decode
        self.adjust_info = decode(adjust_list, deepcopy(self.adjust_info))
        return self

    # 根音：
    @property
    def root_note(self):
        return self._chord_base_list[0]

    # 这是应用了变化的列表，还是没有转位：
    @property
    def _chord_complete_list_without_inversion(self):
        from chord.apply_adjust_without_inversion import apply
        return apply(deepcopy(self._chord_base_list), deepcopy(self.adjust_info))

    # 这是最终的、去除了所有的空格的、按照顺序排列的和弦列表：
    @property
    def chord_content(self):
        from chord.final_complete_chord import show_final
        return show_final(self._chord_complete_list_without_inversion, self.adjust_info.inversion_uid,
                          self.adjust_info.inversion_type, deepcopy(self.additional_notes))

    @property
    def score_term(self):
        from chord.show_chord_score_style import show
        return show(root_note_art_name=self.root_note.art_name,
                    adjust_info=deepcopy(self.adjust_info),
                    chord_base_term=self.chord_base_term,
                    additional_notes=deepcopy(self.additional_notes),
                    most_low_note_name=self.chord_min_pitch_note.art_name)

    @property
    def chord_semitone_range(self):
        semitone_list = [i.semitone for i in self.chord_content]
        return max(semitone_list) - min(semitone_list)

    @property
    def chord_max_pitch_note(self):
        return self.chord_content[-1]

    @property
    def chord_min_pitch_note(self):
        return self.chord_content[0]

    def octave_shift(self, shift_int=0):
        if shift_int:
            return Chord(self._input_root_note_uid_or_math_name, self._input_root_note_octave + shift_int,
                         self._input_chord_term_list)
        return self

    def __str__(self):
        if self.is_valid:
            # new_ins = deepcopy(self)
            from chord.screen_show import execute
            return execute(self.score_term, self.chord_content)
        return f"和弦{self.score_term}不存在。"


# 严格模式（必须按照音名关系，1对1，例如，C♭不等于B，虽然他们的响度是一致的）而且只看几个基本类型，例如大小增减和弦：
def detect_base_chord(chord_list: list[0, Note]):
    from chord.chord_detector import base_detector
    return base_detector(chord_list)


# 位置模式：只看位置，不看音符
def detect_location_chord(chord_list: list[0, Note]):
    from chord.chord_detector import location_detector
    return location_detector(chord_list)


if __name__ == '__main__':
    a = Chord(1, 5, ["maj3", "+5"])
    # for i in a.chord_content:
    #     print(i)
    # print(a)
    # for i in a._chord_base_list:
    #     print(i)
    # for i in a._chord_complete_list_without_inversion:
    #     print(i)
    # print(a._chord_complete_list_without_inversion)
    print(a)
    for i in a.chord_content:
        print(i)
