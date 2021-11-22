#!/usr/bin/env python
# @Time    : 2021/11/22 8:06 下午
# @Author  : guo2018@88.com
from note import Note
from scale import Scale


def execute(note_uid: int, scale_instance: Scale):
    uid_lsits = [i.uid for i in scale_instance.scale_list]
    flag = False
    for i in uid_lsits:
        if i == note_uid:
            flag = True
            break
    return flag
