#!/usr/bin/env python
# @Time    : 2021/11/3 9:06 上午
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
    ["ION", "自然大调Ionian调式", "大", "大", "纯", "纯", "大", "大"],
    ["DOR", "Dorian调式（小调式）", "大", "小", "纯", "纯", "大", "小"],
    ["PHR", "Phrygian调式（小调式）", "小", "小", "纯", "纯", "小", "小"],
    ["LYD", "Lydian调式（大调式）", "大", "大", "增", "纯", "大", "大"],
    ["MLY", "Mixo-lydian调式（大调式）", "大", "大", "纯", "纯", "大", "小"],
    ["AEO", "自然小调Aeolian调式", "大", "小", "纯", "纯", "小", "小"],
    ["LOC", "Locrian调式（半减七调式）", "小", "小", "纯", "减", "小", "小"],
]


# 封装一个用来插入数据的函数：
def insert(db_path, new_add_class, is_echo=True):
    # 先创建连接的引擎
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///".__add__(db_path), echo=is_echo)

    # 再创建session
    from sqlalchemy.orm import sessionmaker
    DbSession = sessionmaker(bind=engine)  # 这里其实是一个类
    session = DbSession()  # 这里其实是类的实例化

    session.add(new_add_class)
    # 提交执行：
    session.commit()  # 提交
    session.close()  # 关闭会话


for single_scale in ready_list:
    root_note = Note("C")
    # print(root_note)
    note2 = root_note.get_note_by_interval(single_scale[2], 2)
    note3 = root_note.get_note_by_interval(single_scale[3], 3)
    note4 = root_note.get_note_by_interval(single_scale[4], 4)
    note5 = root_note.get_note_by_interval(single_scale[5], 5)
    note6 = root_note.get_note_by_interval(single_scale[6], 6)
    note7 = root_note.get_note_by_interval(single_scale[7], 7)
    whole_scale_list = [
        root_note, note2, note3, note4, note5, note6, note7
    ]

    print(single_scale[1])
    # print(note2)
    # print(note3)
    # print(note4)
    # print(note5)
    # print(note6)
    # print(note7)
    # input()
    # 三级的级数和弦的查询：
    def chord3_query(note_index_in_scale):
        temp_list = [
            None,
            [0, 2, 4],
            [1, 3, 5],
            [2, 4, 6],
            [3, 5, 0],
            [4, 6, 1],
            [5, 0, 2],
            [6, 1, 3]
        ]
        chord_result = session.query(Table_Chord3).filter(
            Table_Chord3.rn_uid == whole_scale_list[temp_list[note_index_in_scale][0]].uid).filter(
            Table_Chord3.n3_uid == whole_scale_list[temp_list[note_index_in_scale][1]].uid).filter(
            Table_Chord3.n5_uid == whole_scale_list[temp_list[note_index_in_scale][2]].uid).one_or_none()
        print(chord_result.chord_term)
        return chord_result.chord_term


    # 七级和弦技术的查询：
    def chord7_query(note_index_in_scale):
        temp_list = [
            None,
            [0, 2, 4, 6],
            [1, 3, 5, 0],
            [2, 4, 6, 1],
            [3, 5, 0, 2],
            [4, 6, 1, 3],
            [5, 0, 2, 4],
            [6, 1, 3, 5]
        ]
        chord_result = session.query(Table_Chord7).filter(
            Table_Chord7.rn_uid == whole_scale_list[temp_list[note_index_in_scale][0]].uid).filter(
            Table_Chord7.n3_uid == whole_scale_list[temp_list[note_index_in_scale][1]].uid).filter(
            Table_Chord7.n5_uid == whole_scale_list[temp_list[note_index_in_scale][2]].uid).filter(
            Table_Chord7.n7_uid == whole_scale_list[temp_list[note_index_in_scale][3]].uid).one_or_none()
        print(chord_result.chord_term)
        return chord_result.chord_term


    chord3_1 = chord3_query(1)
    chord3_2 = chord3_query(2)
    chord3_3 = chord3_query(3)
    chord3_4 = chord3_query(4)
    chord3_5 = chord3_query(5)
    chord3_6 = chord3_query(6)
    chord3_7 = chord3_query(7)
    chord7_1 = chord7_query(1)
    chord7_2 = chord7_query(2)
    chord7_3 = chord7_query(3)
    chord7_4 = chord7_query(4)
    chord7_5 = chord7_query(5)
    chord7_6 = chord7_query(6)
    chord7_7 = chord7_query(7)
    print("*" * 20)
    # input()
    new_add = Table_Scale_Meta(
        scale_term=single_scale[0],
        scale_name=single_scale[1],
        scale2_prefix=single_scale[2],
        scale3_prefix=single_scale[3],
        scale4_prefix=single_scale[4],
        scale5_prefix=single_scale[5],
        scale6_prefix=single_scale[6],
        scale7_prefix=single_scale[7],

        i3=chord3_1,
        ii3=chord3_2,
        iii3=chord3_3,
        iv3=chord3_4,
        v3=chord3_5,
        vi3=chord3_6,
        vii3=chord3_7,
        i7=chord7_1,
        ii7=chord7_2,
        iii7=chord7_3,
        iv7=chord7_4,
        v7=chord7_5,
        vi7=chord7_6,
        vii7=chord7_7
    )
    session.add(new_add)
    # 提交：
    session.commit()
