#!/usr/bin/env python
# @Time    : 2021/11/22 9:48 下午
# @Author  : guo2018@88.com
from note import Note


def execute(one_list: list[Note], another_list: list[Note]):
    origin_loc_id_set = set([i.loc_id for i in one_list])
    target_loc_id_set = set([i.loc_id for i in another_list])
    if origin_loc_id_set == target_loc_id_set:
        return True
    return False
