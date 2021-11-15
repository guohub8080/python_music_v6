#!/usr/bin/env python
# @Time    : 2021/8/25 12:26 上午
# @Author  : guo2018@88.com
from common.chord_old import Chord
from common.chord_old.when_init.chord_content_class import Chord_Content


class Chord3(Chord):
    def __init__(self, root_note_instance, chord_type):
        assert str(chord_type).upper() in ["MAJ3", "MIN3", "AUG3", "DIM3"]
        super().__init__(root_note_instance)
        self.chord_type = chord_type
        self.chord_family = "三和弦"
        self.content = None
        from common.chord_old.when_init.query_chord3 import execute
        the_content = execute(root_note_instance=self.root_note_instance, chord_term=self.chord_type)
        if the_content:
            self.is_valid = True
            self.content = Chord_Content(root_note_instance=root_note_instance, chord_list=the_content)

    # 第一转位
    @property
    def inversion1(self):
        if self.is_valid:
            new_root_note = self.content.root_note_instance.octave_shift(1)
            new_lsit = [i for i in self.content.chord_list if i != self.root_note_instance]
            new_lsit.append(new_root_note)
            self.content = Chord_Content(root_note_instance=self.root_note_instance,
                                         chord_list=new_lsit).arrange_list_by_semitone
            return self
        self.is_valid = False
        return self

    # 第二转位
    @property
    def inversion2(self):
        if self.is_valid:
            new_root_note = self.content.root_note_instance.octave_shift(1)
            new_note_3 = self.content.note3.octave_shift(1)
            new_lsit = [i for i in self.content.chord_list if i != self.root_note_instance and i != self.content.note3]
            new_lsit.append(new_root_note)
            new_lsit.append(new_note_3)
            self.content = Chord_Content(root_note_instance=self.root_note_instance,
                                         chord_list=new_lsit).arrange_list_by_semitone
            return self
        self.is_valid = False
        return self


class Chord7(Chord):
    def __init__(self, root_note_instance, chord_type):
        assert str(chord_type).upper() in ["MAJ7", "MIN7", "AUG_MAJ7", "AUG_MIN7", "DIM7", "DOM7", "MM7"]
        super().__init__(root_note_instance)
        self.chord_type = chord_type
        self.chord_family = "七和弦"
        self.content = None
        from common.chord_old.when_init.query_chord7 import execute
        the_content = execute(root_note_instance=self.root_note_instance, chord_term=self.chord_type)
        if the_content:
            self.is_valid = True
            self.content = Chord_Content(root_note_instance=root_note_instance, chord_list=the_content)

    # 第一转位
    @property
    def inversion1(self):
        if self.is_valid:
            new_root_note = self.content.root_note_instance.octave_shift(1)
            new_lsit = [i for i in self.content.chord_list if i != self.root_note_instance]
            new_lsit.append(new_root_note)
            self.content = Chord_Content(root_note_instance=self.root_note_instance,
                                         chord_list=new_lsit).arrange_list_by_semitone
            return self
        self.is_valid = False
        return self

    # 第二转位
    @property
    def inversion2(self):
        if self.is_valid:
            new_root_note = self.content.root_note_instance.octave_shift(1)
            new_note_3 = self.content.note3.octave_shift(1)
            new_lsit = [i for i in self.content.chord_list if i != self.root_note_instance and i != self.content.note3]
            new_lsit.append(new_root_note)
            new_lsit.append(new_note_3)
            self.content = Chord_Content(root_note_instance=self.root_note_instance,
                                         chord_list=new_lsit).arrange_list_by_semitone
            return self
        self.is_valid = False
        return self

    # 第三转位
    @property
    def inversion3(self):
        if self.is_valid:
            new_root_note = self.content.root_note_instance.octave_shift(1)
            new_note_3 = self.content.note3.octave_shift(1)
            new_note_5 = self.content.note5.octave_shift(1)
            new_lsit = [i for i in self.content.chord_list if
                        i != self.root_note_instance and i != self.content.note3 and i != self.content.note5]
            new_lsit.append(new_root_note)
            new_lsit.append(new_note_3)
            new_lsit.append(new_note_5)
            self.content = Chord_Content(root_note_instance=self.root_note_instance,
                                         chord_list=new_lsit).arrange_list_by_semitone
            return self
        self.is_valid = False
        return self


class Chord9(Chord):
    def __init__(self, root_note_instance, chord_type):
        assert str(chord_type).upper() in ["MAJ9", "MIN9", "AUG9", "DOM9", "MM9"]
        super().__init__(root_note_instance)
        self.chord_type = chord_type
        self.chord_family = "九和弦"
        self.content = None
        from common.chord_old.when_init.query_chord9 import execute
        the_content = execute(root_note_instance=self.root_note_instance, chord_term=self.chord_type)
        if the_content:
            self.is_valid = True
            self.content = Chord_Content(root_note_instance=root_note_instance, chord_list=the_content)


if __name__ == '__main__':
    from note import Note

    # e = Chord9(Note("C"), "aug9")
    f = Chord7(Note("C"), "aug_maj7")
    # print(e)
    print(f)
