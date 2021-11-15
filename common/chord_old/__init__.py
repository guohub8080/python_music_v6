#!/usr/bin/env python
# @Time    : 2021/8/24 5:14 下午
# @Author  : guo2018@88.com

from note.PRESETS import D


class Chord(object):
    def __init__(self, root_note_instance):
        # print(isinstance(root_note_instance,Note))
        # print(dir(root_note_instance))
        # print(root_note_instance.__class__)
        # print(root_note_instance.__module__)
        # assert isinstance(root_note_instance, Note)
        self.root_note_instance = root_note_instance
        self.is_valid = False

    # ======================================================================== #
    # =============================    三和弦    ============================= #
    # ======================================================================== #
    # 大三和弦
    @property
    def major_3(self):
        from common.chord_old.when_init import Chord3
        return Chord3(self.root_note_instance, chord_type="MAJ3")

    # 小三和弦
    @property
    def minor_3(self):
        from common.chord_old.when_init import Chord3
        return Chord3(self.root_note_instance, chord_type="MIN3")

    # 增三和弦
    @property
    def aug_3(self):
        from common.chord_old.when_init import Chord3
        return Chord3(self.root_note_instance, chord_type="AUG3")

    # 减三和弦
    @property
    def dim_3(self):
        from common.chord_old.when_init import Chord3
        return Chord3(self.root_note_instance, chord_type="DIM3")

    # ======================================================================== #
    # =============================    七和弦    ============================= #
    # ======================================================================== #
    # 大七和弦
    @property
    def major_7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="MAJ7")

    # 属七和弦
    @property
    def dom_7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="DOM7")

    # 小七和弦
    @property
    def min_7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="MIN7")

    # 小大七和弦
    @property
    def min_maj_7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="MM7")

    # 减七和弦
    @property
    def dim_7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="DIM7")

    # 增大七和弦
    @property
    def aug_maj7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="AUG_MAJ7")

    # 增小七和弦
    @property
    def aug_min7(self):
        from common.chord_old.when_init import Chord7
        return Chord7(self.root_note_instance, chord_type="AUG_MIN7")

    def __str__(self):
        if self.is_valid:
            from common.chord_old.when_init.chord__str__func import show_chord_content
            return show_chord_content(self.content.chord_list)
        else:
            return "和弦组成尚未完成调用，请在后面继续加点调用..."


if __name__ == '__main__':
    print(Chord(D()))
    a = Chord(D(5)).major_3
    print(a)
    print(Chord(D(6)).aug_3)
