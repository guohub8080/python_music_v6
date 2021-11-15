#!/usr/bin/env python
# @Time    : 2021/11/9 11:13 下午
# @Author  : guo2018@88.com
from circle import CLOCK_META
from datetime import timedelta


def produce_clock_location_from_meta(meta_list: list):
    def produce_note_time(minute):
        FIXED_YEAR = 2021
        FIXED_MONTH = 11
        FIXED_DAY = 7
        FIXED_HOUR = 4
        FIXED_SECOND_AND_MICROSECOND = 0
        from datetime import datetime
        return datetime(FIXED_YEAR, FIXED_MONTH, FIXED_DAY, FIXED_HOUR,
                        minute, FIXED_SECOND_AND_MICROSECOND,
                        FIXED_SECOND_AND_MICROSECOND)

    # def time_delta_within_one_circle(origin_datetime: datetime, minutes_delta):
    #     new_datetime = origin_datetime + timedelta(minutes=minutes_delta)
    #     new_datetime = new_datetime.replace(hour=origin_datetime.hour)
    #     return new_datetime

    set_list = []
    for each_minute_mapping_note in range(0, 60, 5):
        each_turn_produce_set = []
        clock_note_time_start = produce_note_time(each_minute_mapping_note)
        each_turn_produce_set.append(clock_note_time_start)
        for each_add in meta_list:
            each_turn_produce_set.append(each_turn_produce_set[-1] + timedelta(minutes=each_add * 5))
        each_turn_produce_set = set([i.minute for i in each_turn_produce_set])
        flag = True
        for single_set in set_list:
            if single_set == each_turn_produce_set:
                flag = False
                break
        if flag:
            set_list.append(each_turn_produce_set)
    return set_list


def __print_clock_location_sets(sets_list: list[set]):
    for i in sets_list:
        i = sorted(list(i))
        print(i[0], "\t", i[1], "\t", i[2])


if __name__ == '__main__':
    a = produce_clock_location_from_meta(CLOCK_META.chord3_dim)
    __print_clock_location_sets(a)
