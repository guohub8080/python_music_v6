#!/usr/bin/env python
# @Time    : 2021/11/7 7:11 下午
# @Author  : guo2018@88.com
from datetime import datetime

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


if __name__ == '__main__':
    # a = Circle([1, 2, 3, 4])
    # b = a.reverse_move(4)
    # print(b.whole_queue)
    # print(b.cursor_element)
    a = Note("C")
    print(a.clock_instance.mapping_time)
