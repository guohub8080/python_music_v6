#!/usr/bin/env python
# @Time    : 2021/11/12 2:27 下午
# @Author  : guo2018@88.com

# 三和弦：
import pandas

maj3 = "maj3"
min3 = "min3"
aug3 = "aug3"
dim3 = "dim3"

# 七和弦：
maj7 = "maj7"
min7 = "min7"
dom7 = "dom7"
mm7 = "mm7"
aug_maj7 = "aug_maj7"
aug_min7 = "aug_min7"
half_dim7 = "half_dim7"
#
adjust_dict = {
    "move2": 0,
    "move4": 0,
    "move5": 0,
    "move6": 0,
    "move7": 0,
    "move9": 0,
    "move11": 0,
    "move13": 0,
    "is_sus2": False,
    "is_sus4": False,
    "is_add2": False,
    "is_add4": False,
    "is_add6": False,
    "is_add9": False,
    "is_add11": False,
    "is_add13": False,
    "is_omit3": False,
    "is_omit5": False,
    "is_omit7": False,
    "is_omit9": False,
    "is_omit11": False,
    "inversion_uid": 0,
    "inversion_type": 0}


class Adjust_Chord(object):
    def __init__(self):
        self.move2 = 0
        self.move4 = 0
        self.move5 = 0
        self.move6 = 0
        self.move7 = 0
        self.move9 = 0
        self.move11 = 0
        self.move13 = 0,
        self.is_sus2 = False
        self.is_sus4 = False
        self.is_add2 = False
        self.is_add4 = False
        self.is_add6 = False
        self.is_add9 = False
        self.is_add11 = False
        self.is_add13 = False
        self.is_omit3 = False
        self.is_omit5 = False
        self.is_omit7 = False
        self.is_omit9 = False
        self.is_omit11 = False
        self.inversion_uid = 0
        self.inversion_type = 0
