#!/usr/bin/env python
# @Time    : 2021/11/21 6:35 下午
# @Author  : guo2018@88.com
from note import Note
from sqlalchemy.orm import aliased

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.scale_meta_old import Table_Scale_Meta
from common.table_class.chord_old import Table_Chord3, Table_Chord7
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()

ready_list = [
    ["ION", "自然大调Ionian调式", "也称为自然大调，自然大调的 I 级音阶，由 C 大调的 C 进行到高八度的 C，构成音分别为：1 2 3 4 5 6 7 1",
     "大", "大", "纯", "纯", "大", "大"],
    ["DOR", "Dorian调式（小调式）", "自然大调的 II 级音阶，由 C 大调的 D 进行到高八度的 D，构成音分别为：1 2 b3 4 5 6 b7 1",
     "大", "小", "纯", "纯", "大", "小"],
    ["PHR", "Phrygian调式（小调式）", "自然大调的 III 级音阶，由 C 大调的 E 进行到高八度的 E，构成音分别为：1 b2 b3 4 5 b6 b7 1",
     "小", "小", "纯", "纯", "小", "小"],
    ["LYD", "Lydian调式（大调式）", "自然大调的 IV 级音阶，由 C 大调的 F 进行到高八度的 F，构成音分别为：1 2 3 #4 5 6 7 1  ",
     "大", "大", "增", "纯", "大", "大"],
    ["MLY", "Mixo-lydian调式（大调式）", "自然大调的 V 级音阶，由 C 大调的 G 进行到高八度的 G，构成音分别为：1 2 3 4 5 6 b7 1",
     "大", "大", "纯", "纯", "大", "小"],
    ["AEO", "自然小调Aeolian调式", "自然小调，自然大调的 VI 级音阶，由 C 大调的 A 进行到高八度的 A，构成音分别为：1 2 b3 4 5 b6 b7 1",
     "大", "小", "纯", "纯", "小", "小"],
    ["LOC", "Locrian调式（半减七调式）", "自然大调的 VII 级音阶，由 C 大调的 B 进行到高八度的 B，构成音分别为：1 b2 b3 4 b5 b6 b7 1",
     "小", "小", "纯", "减", "小", "小"],
]

for each_scale in ready_list:
    interval_list = str(each_scale[3:]).replace(" ", "").replace("'", "").replace("[","").replace("]","")
    print(interval_list)
