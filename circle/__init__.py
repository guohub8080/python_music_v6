#!/usr/bin/env python
# @Time    : 2021/11/7 7:11 下午
# @Author  : guo2018@88.com
from datetime import datetime, timedelta

from note import Note


class Circle(object):
    def __init__(self, circle_list: list):
        self.whole_queue = circle_list
        self.cursor_element = circle_list[0]

    def move(self, move_step: int = 0):
        new_index = move_step % len(self.whole_queue)
        if new_index == 0 or move_step == 0:
            return self
        new_part_start = self.whole_queue[new_index:]
        new_part_end = self.whole_queue[0:new_index]
        new_part_start.extend(new_part_end)
        return Circle(new_part_start)

    # 两个圆圈数据类型是否相同：
    # 返回的是一个三个元素的列表。list[0]是一个布尔，表示是或否。
    # list[1]只有是TRUE的时候才有意义，表示顺序移动多少，list[2]是逆向移动多少。
    # 当list[0]是False的时候，其余数据都是None，即无意义。
    def is_equal_to(self, another_circle):
        from circle.judge_is_equal import execute
        return execute(self, another_circle)

    def reverse_move(self, move_step: int = 0):
        new_index = move_step % len(self.whole_queue)
        if new_index == 0 or move_step == 0:
            return self
        new_index = len(self.whole_queue) - new_index
        new_part_start = self.whole_queue[new_index:]
        new_part_end = self.whole_queue[0:new_index]
        new_part_start.extend(new_part_end)
        return Circle(new_part_start)

    def reverse(self):
        cursor_element = self.whole_queue[0]
        new_queue = self.whole_queue[1:]
        new_queue.reverse()
        new_queue.insert(0, cursor_element)
        return Circle(new_queue)


class Clock(object):
    def __init__(self, uid, octave, note_loc_id):
        self.uid = uid
        self.octave = octave
        self.minute_location = (note_loc_id - 1) * 5

    @property
    def mapping_time(self):
        from circle import CLOCK_META
        return datetime(CLOCK_META.FIXED_YEAR, CLOCK_META.FIXED_MONTH, CLOCK_META.FIXED_DAY,
                        self.octave, self.minute_location,
                        CLOCK_META.FIXED_SECOND_AND_MICROSECOND,
                        CLOCK_META.FIXED_SECOND_AND_MICROSECOND)

    @property
    def mapping_note(self):
        return Note(self.uid, self.octave)


# 五度圈：
class Fifth_Circle(object):
    def __init__(self, cursor_location=0):
        self._inner_circle = [10, 5, 12, 7, 2, 9, 4, 11, 6, 1, 8, 3]
        self._outer_circle = [1, 8, 3, 10, 5, 12, 7, 2, 9, 4, 11, 6]
        self.cursor_location = cursor_location

    def move(self, input_int=0):
        self.cursor_location += input_int
        return self

    @staticmethod
    def _get_new_index(cursor_location):
        from circle import CLOCK_META
        prime_clock = datetime(CLOCK_META.FIXED_YEAR, CLOCK_META.FIXED_MONTH, CLOCK_META.FIXED_DAY,
                               CLOCK_META.FIXED_HOUR, 0, 0, 0)
        new_clock = prime_clock + timedelta(minutes=5 * cursor_location)
        return int(new_clock.minute / 5)

    @staticmethod
    def _get_note_instances_by_loc_id(loc_id):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from common.settings import DB_SQL_LOCATION
        from common.table_class.meta import Table_Meta
        from note import Note
        engine = create_engine(DB_SQL_LOCATION)
        session = sessionmaker(bind=engine)()
        note_uids = [getattr(i, "uid") for i in
                     session.query(Table_Meta).filter(Table_Meta.loc_id == loc_id).filter(
                         Table_Meta.is_normal == True).filter(Table_Meta.bias < 2).filter(
                         Table_Meta.bias > -2).all()]
        result = []
        for i in note_uids:
            result.append(Note(i))
        return result

    @property
    def inner_note(self):
        new_index = self._get_new_index(self.cursor_location)
        loc_id = self._inner_circle[new_index]
        return self._get_note_instances_by_loc_id(loc_id)

    @property
    def outer_note(self):
        new_index = self._get_new_index(self.cursor_location)
        loc_id = self._outer_circle[new_index]
        return self._get_note_instances_by_loc_id(loc_id)

    def __str__(self):
        print("外圈(大和弦根音)内容为：", end="")
        outer_list = " 或 ".join([i.art_name for i in self.outer_note])
        print(outer_list)

        print("内圈(小和弦根音)内容为：", end="")
        inner_list = " 或 ".join([i.art_name for i in self.inner_note])
        print(inner_list, end="")
        return ""


if __name__ == '__main__':
    # a = Circle([1, 2, 3, 4])
    # b = a.reverse_move(4)
    # print(b.whole_queue)
    # print(b.cursor_element)
    # a = Note("C")
    # print(a.clock_instance.mapping_time)
    # from note.PRESETS import *
    #
    # t = []
    # t.append(C().loc_id)
    # t.append(G().loc_id)
    # t.append(D().loc_id)
    # t.append(A().loc_id)
    # t.append(E().loc_id)
    # t.append(B().loc_id)
    # t.append(G_FLAT().loc_id)
    # t.append(D_FLAT().loc_id)
    # t.append(A_FLAT().loc_id)
    # t.append(E_FLAT().loc_id)
    # t.append(B_FLAT().loc_id)
    # t.append(F().loc_id)
    #
    # t.append(A().loc_id)
    # t.append(E().loc_id)
    # t.append(B().loc_id)
    # t.append(F_SHARP().loc_id)
    # t.append(C_SHARP().loc_id)
    # t.append(G_SHARP().loc_id)
    # t.append(E_FLAT().loc_id)
    # t.append(B_FLAT().loc_id)
    # t.append(F().loc_id)
    # t.append(C().loc_id)
    # t.append(G().loc_id)
    # t.append(D().loc_id)
    # print(t)
    a = Fifth_Circle(-1)
    for i in range(12):
        print(a.move(1))
        print("-----------")
