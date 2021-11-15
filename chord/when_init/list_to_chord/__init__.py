#!/usr/bin/env python
# @Time    : 2021/11/12 3:00 下午
# @Author  : guo2018@88.com
from note import Note
from datetime import datetime
from collections import deque
from pandas import read_excel
from common.settings import BASE_DIR


def execute(chord_list: list[Note]):
    from note import Note
    # 1.首先要把全部的音符展平，然后放在同一个时钟圈内：
    clock_instances_within_1_circle: list[datetime] = [
        getattr(getattr(i, "clock_instance"), "mapping_time").replace(microsecond=0)
        for i in chord_list]
    # 现在得到的是类似[0, 20, 35]这样的列表：
    clock_minutes_set_list = deque(
        sorted(list(set([i.minute for i in clock_instances_within_1_circle])), reverse=False))
    # print(list(clock_minutes_set_list))
    from chord import CHORD_META
    # print(BASE_DIR.joinpath("chord"))
    # print()
    the_chord_meta = read_excel(BASE_DIR.joinpath("chord").joinpath("CHORD_META").joinpath("chord_meta.xlsx"))
    print(the_chord_meta.shape)
    # for i in the_chord_meta:
    #     print(i)
    # print(the_chord_meta["chord_term"])
    print(the_chord_meta.head())
    print(clock_minutes_set_list == [0, 20, 35])

    return


if __name__ == '__main__':
    execute([Note("C"), Note("E"), Note("G")])
