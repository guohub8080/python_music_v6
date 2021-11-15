#!/usr/bin/env python
# @Time    : 2021/8/30 12:26 上午
# @Author  : guo2018@88.com

# 和弦内容需要单独弄一个类。

from pprint import pprint

from note import Note


class Chord_Content(object):
    def __init__(self, root_note_instance, chord_list):
        from note import Note
        # type:(Note,list[Note])
        self.root_note_instance: Note = root_note_instance
        self.chord_list: list[Note] = chord_list

    # 方法：转位，这次不分第几转位了，直接就写最低音是什么。
    def inversion_on(self, inversion_note_uid):
        if inversion_note_uid == 0:
            return self
        target_list = self.arrange_list_by_semitone.chord_list
        target_index = -1
        for i in target_list:
            if inversion_note_uid == i.uid:
                target_index = target_list.index(i)
        if target_index == 0:
            return Chord_Content(target_list[0], target_list)
        if target_index > 0:
            for i in range(target_index):
                if i < target_index:
                    target_list[i] = target_list[i].octave_shift(1)
            return Chord_Content(target_list[target_index], target_list).arrange_list_by_semitone
        if target_index < 0:
            new_note = Note(inversion_note_uid, target_list[0].octave)
            if new_note.semitone > target_list[0].semitone:
                new_note = new_note.octave_shift(-1)
            target_list.append(new_note)
            return Chord_Content(new_note, target_list).arrange_list_by_semitone

    # 和弦的方法
    # 方法：sus2
    @property
    def sus2(self):
        assert isinstance(self.root_note_instance, Note)
        note2 = self.root_note_instance.interval.M2
        note3 = self.note3
        new_list = [i for i in self.chord_list if i != note3]
        new_list.append(note2)
        return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone

    # 方法：sus4
    @property
    def sus4(self):
        assert isinstance(self.root_note_instance, Note)
        note2 = self.root_note_instance.interval.P4
        note3 = self.note3
        new_list = [i for i in self.chord_list if i != note3]
        new_list.append(note2)
        return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone

    # 方法：add2
    @property
    def add2(self):
        assert isinstance(self.root_note_instance, Note)
        new_note2 = self.root_note_instance.interval.M2
        if new_note2.is_valid:
            self.chord_list.append(new_note2)
            return self.arrange_list_by_semitone
        return None

    # 方法：add4
    @property
    def add4(self):
        assert isinstance(self.root_note_instance, Note)
        new_note4 = self.root_note_instance.interval.P4
        if new_note4.is_valid:
            self.chord_list.append(new_note4)
            return self.arrange_list_by_semitone
        return None

    # 方法：add6
    @property
    def add6(self):
        assert isinstance(self.root_note_instance, Note)
        new_note6 = self.root_note_instance.interval.M6
        new_list = self.chord_list.append(new_note6)
        return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone

    # 方法：和弦升5音
    @property
    def sharp5(self):
        note5 = self.note5
        note5_adjusted = note5.sharp_or_flat_adjust(1)
        if note5_adjusted:
            new_list = [i for i in self.chord_list if i != note5]
            new_list.append(note5_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦降5音
    @property
    def flat5(self):
        note5 = self.note5
        note5_adjusted = note5.sharp_or_flat_adjust(-1)
        if note5_adjusted:
            new_list = [i for i in self.chord_list if i != note5]
            new_list.append(note5_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦升9音
    @property
    def sharp9(self):
        note9 = self.note9
        note9_adjusted = note9.sharp_or_flat_adjust(1)
        if note9_adjusted:
            new_list = [i for i in self.chord_list if i != note9]
            new_list.append(note9_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦降9音
    @property
    def flat9(self):
        note9 = self.note9
        note9_adjusted = note9.sharp_or_flat_adjust(-1)
        if note9_adjusted:
            new_list = [i for i in self.chord_list if i != note9]
            new_list.append(note9_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦升11音
    @property
    def sharp11(self):
        note11 = self.note11
        note11_adjusted = note11.sharp_or_flat_adjust(1)
        if note11_adjusted:
            new_list = [i for i in self.chord_list if i != note11]
            new_list.append(note11_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦降11音
    @property
    def flat11(self):
        note11 = self.note11
        note11_adjusted = note11.sharp_or_flat_adjust(-1)
        if note11_adjusted:
            new_list = [i for i in self.chord_list if i != note11]
            new_list.append(note11_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦升13音
    @property
    def sharp13(self):
        note13 = self.note13
        note13_adjusted = note13.sharp_or_flat_adjust(1)
        if note13_adjusted:
            new_list = [i for i in self.chord_list if i != note13]
            new_list.append(note13_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 方法：和弦降13音
    @property
    def flat13(self):
        note13 = self.note13
        note13_adjusted = note13.sharp_or_flat_adjust(-1)
        if note13_adjusted:
            new_list = [i for i in self.chord_list if i != note13]
            new_list.append(note13_adjusted)
            return Chord_Content(self.root_note_instance, new_list).arrange_list_by_semitone
        return None

    # 和弦的三音：
    @property
    def note3(self):
        from common import interval_between_notes
        for i in self.chord_list:
            index_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if index_gap == 3:
                return i
        return None

    # 和弦的五音：
    @property
    def note5(self):
        from common import interval_between_notes
        for i in self.chord_list:
            index_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if index_gap == 5:
                return i
        return None

    # 和弦的七音：
    @property
    def note7(self):
        from common import interval_between_notes
        for i in self.chord_list:
            index_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if index_gap == 7:
                return i
        return None

    # 和弦的九音：
    @property
    def note9(self):
        from common import interval_between_notes
        for i in self.chord_list:
            index_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if index_gap == 9:
                return i
        return None

    # 和弦的十一音：
    @property
    def note11(self):
        from common import interval_between_notes
        for i in self.chord_list:
            index_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if index_gap == 11:
                return i
        return None

    # 和弦的十三音：
    @property
    def note13(self):
        from common import interval_between_notes
        for i in self.chord_list:
            index_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if index_gap == 13:
                return i
        return None

    # 距离根音的某度音：
    def note_far_from_root(self, interval_description):
        assert isinstance(interval_description, int)
        from common import interval_between_notes
        for i in self.chord_list:
            the_gap = interval_between_notes(self.root_note_instance, i)["interval_type"]
            if the_gap == interval_description:
                return i
        return None

    # 字符显示
    def __str__(self):
        from prettytable import PrettyTable
        the_table_title = ["Math_name", "art_name", "midi_value"]
        table = PrettyTable(the_table_title)
        table.padding_width = 2
        list_lenth = len(self.chord_list) - 1
        for i in range(list_lenth, -1, -1):
            the_item = self.chord_list[i]
            table.add_row([f"{the_item.math_name}_{the_item.octave}", f"{the_item.art_name}_{the_item.octave}",
                           the_item.semitone])
        table.header_style = "title"
        print(table)
        return ""

    # 输出按音高pitch（或者是半音数semitone）排列的列表
    @property
    def arrange_list_by_semitone(self):
        the_list = sorted(self.chord_list, key=lambda x: x.semitone)
        return Chord_Content(self.root_note_instance, the_list)

    # 输出按音名排列的列表
    @property
    def arrange_list_by_note_index(self):
        the_list = sorted(self.chord_list, key=lambda x: [x.index, x.uid])
        return Chord_Content(self.root_note_instance, the_list)

    # 输出整个和弦内容的最大跨度是多少
    @property
    def max_interval(self):
        new_list = self.arrange_list_by_semitone.chord_list
        min_note = new_list[0]
        max_note = new_list[-1]
        from common import interval_between_notes
        the_gap = interval_between_notes(min_note, max_note)["interval_type"]
        return the_gap

    # 这个函数会输出一个音程的列表，返回值是空的。
    @property
    def interval_list(self):
        from common import interval_between_notes
        from prettytable import PrettyTable
        the_table_title = ["▼起 止▶"]
        arranged_list = sorted(self.chord_list, key=lambda x: x.semitone)
        for i in arranged_list:
            the_table_title.append("{}_{}".format(i.art_name, i.octave))
        table = PrettyTable(the_table_title)
        table.padding_width = 2
        table.header_style = "title"
        for i in arranged_list:
            the_row = ["{}_{}".format(i.art_name, i.octave)]
            for ii in arranged_list:
                interval_info = interval_between_notes(i, ii)
                the_row.append(
                    "{} {}{}".format(interval_info["trend"], interval_info["prefix"], interval_info["interval_type"]))
            table.add_row(the_row)
        # print(table)
        return table


if __name__ == '__main__':
    from note.PRESETS import C, E, G, D, F, A, B

    c = C(5)
    d = D(5)
    e = E(5)
    f = F(5)
    g = G(5)
    a = A(5)
    b = B(5)
    alist = [c, e, g, b]
    z = Chord_Content(c, alist)
    # print(z.note3)
    # print(z.note5)
    # print(z.note7)
    print(z)
    # print(z.sus4.flat5)
    # print(z.max_interval)
    print("*" * 20)
    print(z.inversion_on(1))
