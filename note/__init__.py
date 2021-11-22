#!/usr/bin/env python
# @Time    : 2021/8/21 5:08 下午
# @Author  : guo2018@88.com

from common.settings import CENTER_C_LOCATION, MIDI_RENDER_CALC_AJUST_SEMITONE, MIDI_RENDER_CALC_AJUST_OCTAVE


class Note(object):
    # 初始化音符，必须接收一个音符名称或者音符index（C为1，D为2，以此类推）。
    # 默认中央C是5，可以在settings里面更改。
    def __init__(self, name=None, octave=CENTER_C_LOCATION):
        # type:([str,int,None],int)->None
        if not name:
            name = "C"
        assert isinstance(name, str) or isinstance(name, int)
        from note import when_init
        when_init.get_info(name)
        self.is_valid = False
        self.math_name = None
        self.art_name = None
        self.index = None
        self.bias = None
        self.uid = None
        self.is_black = None
        self.loc_id = None
        self.octave = None
        self.semitone = None
        self.is_normal = None
        if when_init.is_valid:
            self.is_valid = True
            self.uid = when_init.uid
            self.math_name = when_init.math_name
            self.art_name = when_init.art_name
            self.index = when_init.index
            self.bias = when_init.bias
            self.is_black = when_init.is_black
            self.loc_id = when_init.loc_id
            self.is_normal = when_init.is_normal
            self.octave = octave + MIDI_RENDER_CALC_AJUST_OCTAVE
            self.semitone = when_init.semitone + self.octave * 12 + MIDI_RENDER_CALC_AJUST_SEMITONE
            from note.when_init import make_music21_instance
            self.music21_instance = make_music21_instance(self.math_name, self.octave, self.bias)

    @property
    def clock_instance(self):
        if self.is_valid:
            from circle import Clock
            return Clock(self.uid, self.octave, self.loc_id)
        return None

    # 音程查询1：
    # 使用普通的音程来查询，例如Note("D").get_note_by_interval("大",3)表示求D的上行大三度：
    def get_note_by_interval(self, prefix, interval, trend="上"):
        from note.interval_to_note import execute
        the_result = execute(origin_uid=self.uid, origin_octave=self.octave,
                             prefix=prefix, interval_type=interval,
                             trend=trend)
        if the_result:
            return the_result
        self.is_valid = False
        return self

        # 音程查询2：

    # 写于2021年08月22日11:00:02
    # 使用预置的、提前设定好的音程，例如Note("D").interval.P5表示求D的上行纯5度。
    # 提前设定好的音程是一个类，储存在common_interval_presets里面。前缀标识请移步该类的说明区。
    # 调用这个property的时候，就实例化一下这个类，以实现以一个「interval」为中心的连续加点的效果。
    # 这样写的目的纯粹是为了符合直觉，如果写成子类的话，就会差不多类似这样的效果：Note("D").interval(Note("D")).P5()。
    # 上述写法没问题，但是不太符合直觉。
    # 我在第一版的时候尝试使用setattr的方法来做到我的目标预期，但会导致在这里面写一大堆东西，显得杂乱且无法实现类本身就有的继承特性。
    @property
    def interval(self):
        from note.common_interval_presets import Common_Interval
        return Common_Interval(self)

    # 音程查询3：
    # 同音程查询2，唯一的不同是反向查询。
    @property
    def backward_interval(self):
        from note.common_interval_presets import Common_Interval
        return Common_Interval(self, inverse_query=True)

    def make_chord(self, chord_str_or_list):
        from chord import Chord
        return Chord(self.uid, self.octave, chord_str_or_list)
        # 八度调整的函数：

    def octave_shift(self, octave_shift_value=0):
        assert isinstance(octave_shift_value, int)
        if octave_shift_value:
            return Note(self.math_name, self.octave + octave_shift_value)
        return self

    def octave_shift_to(self, octave_shift_value=-1):
        if octave_shift_value < 0:
            return self
        return Note(self.uid, octave_shift_value)

    # 调整原地升降的函数：
    def sharp_or_flat_adjust(self, adjust_value):
        from note.sharp_or_flat_ajust_func import adjust_semitone
        return adjust_semitone(self, adjust_value)

    def sharp_or_flat_adjust_to(self, adjust_value):
        from note.sharp_or_flat_ajust_func import adjust_semitone_to
        return adjust_semitone_to(self, adjust_value)

    # 找到在keyboard同一位置的其他音名的函数，例如C#又是Db：
    @property
    def same_pitch_notes(self):
        from note.find_same_pitch_notes import execute
        return execute(uid=self.uid, loc_id=self.loc_id,
                       semitone=self.semitone - self.octave * 12, octave=self.octave)

    # 找到音阶：
    def scale(self, scale_id_or_term: [int, str] = 1):
        from note.find_scale import execute
        return execute(self.uid, self.octave, scale_id_or_term)

    # 判断一个音是否在一个音阶里：
    def is_in_scale(self, scale_instance):
        from note.judge_in_scale import execute
        return execute(self.uid, scale_instance)

        # 设置输出字符

    def __str__(self):
        the_sen = "The Note is not valid."
        if self.is_valid:
            from prettytable import PrettyTable
            table = PrettyTable(["math_name", "art_name", "octave", "midi_value", "is_black", "bias", "location"])
            table.header_style = "title"
            table.add_row(
                [self.math_name, self.art_name, self.octave, self.semitone, self.is_black, self.bias, self.loc_id])
            print(table)
            return ""
        return the_sen


class Rest_Note(object):
    def __init__(self):
        from music21.note import Rest
        self.music21_instance = Rest()


if __name__ == '__main__':
    a = Note("C")
    b = Note("d+1")
    c = b.scale(7)
    print(c)
    from scale import Scale

    d = Scale()
    print(a.is_in_scale(d))
    e = a.make_chord(["maj3", "+5"])
    # print(e)
    print(e)

    # print(a.interval.P5.interval.P5.interval.P5.interval.P5)
    # # from PRESETS import C_FLAT_5, D_6
    # #
    # # print(C_FLAT_5)
    # # print(D_6)
    # print("/" * 50)
    # from PRESETS import *
    #
    # c = C(5).interval.P5.interval.AUG5.interval.AUG5
    # print(c)
