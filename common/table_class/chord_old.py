#!/usr/bin/env python
# @Time    : 2021/8/25 11:52 下午
# @Author  : guo2018@88.com

from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Chord3(Base):  # 继承生成的orm基类
    __tablename__ = "chord3"  # 表名
    id = Column(INT, primary_key=True)
    rn_uid = Column(INT)
    # n1_math_name = Column(TEXT(3))

    # n2_math_name = Column(TEXT(3))
    rn_math_name = Column(TEXT(3))
    rn_art_name = Column(TEXT(3))

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT(3))
    n3_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT(3))
    n5_octave = Column(INT)

    is_valid = Column(BOOLEAN)

    chord_term = Column(TEXT)


class Table_Chord7(Base):  # 继承生成的orm基类
    __tablename__ = "chord7"  # 表名
    id = Column(INT, primary_key=True)
    rn_uid = Column(INT)

    rn_math_name = Column(TEXT(3))
    rn_art_name = Column(TEXT(3))

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT(3))
    n3_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT(3))
    n5_octave = Column(INT)

    n7_uid = Column(INT)
    n7_math_name = Column(TEXT(3))
    n7_octave = Column(INT)

    is_valid = Column(BOOLEAN)
    chord_term = Column(TEXT)


class Table_Chord9(Base):  # 继承生成的orm基类
    __tablename__ = "chord9"  # 表名
    id = Column(INT, primary_key=True)
    rn_uid = Column(INT)

    rn_math_name = Column(TEXT(3))
    rn_art_name = Column(TEXT(3))

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT(3))
    n3_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT(3))
    n5_octave = Column(INT)

    n7_uid = Column(INT)
    n7_math_name = Column(TEXT(3))
    n7_octave = Column(INT)

    n9_uid = Column(INT)
    n9_math_name = Column(TEXT(3))
    n9_octave = Column(INT)

    is_valid = Column(BOOLEAN)
    chord_term = Column(TEXT)


class Table_Chord11(Base):  # 继承生成的orm基类
    __tablename__ = "chord11"  # 表名
    id = Column(INT, primary_key=True)
    rn_uid = Column(INT)

    rn_math_name = Column(TEXT(3))
    rn_art_name = Column(TEXT(3))

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT(3))
    n3_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT(3))
    n5_octave = Column(INT)

    n7_uid = Column(INT)
    n7_math_name = Column(TEXT(3))
    n7_octave = Column(INT)

    n9_uid = Column(INT)
    n9_math_name = Column(TEXT(3))
    n9_octave = Column(INT)

    n11_uid = Column(INT)
    n11_math_name = Column(TEXT(3))
    n11_octave = Column(INT)

    is_valid = Column(BOOLEAN)
    chord_term = Column(TEXT)


class Table_Chord13(Base):  # 继承生成的orm基类
    __tablename__ = "chord13"  # 表名
    id = Column(INT, primary_key=True)
    rn_uid = Column(INT)

    rn_math_name = Column(TEXT(3))
    rn_art_name = Column(TEXT(3))

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT(3))
    n3_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT(3))
    n5_octave = Column(INT)

    n7_uid = Column(INT)
    n7_math_name = Column(TEXT(3))
    n7_octave = Column(INT)

    n9_uid = Column(INT)
    n9_math_name = Column(TEXT(3))
    n9_octave = Column(INT)

    n11_uid = Column(INT)
    n11_math_name = Column(TEXT(3))
    n11_octave = Column(INT)

    n13_uid = Column(INT)
    n13_math_name = Column(TEXT(3))
    n13_octave = Column(INT)

    is_valid = Column(BOOLEAN)
    chord_term = Column(TEXT)


class Table_Whole_Chord(Base):  # 继承生成的orm基类
    __tablename__ = "whole_chord"  # 表名
    id = Column(INT, primary_key=True)
    rn_uid = Column(INT)

    rn_math_name = Column(TEXT(3))
    is_valid = Column(BOOLEAN)
    base_chord_term = Column(TEXT)
    note_count = Column(INT)

    is_add2 = Column(BOOLEAN)
    is_add4 = Column(BOOLEAN)
    is_add6 = Column(BOOLEAN)
    is_add9 = Column(BOOLEAN)
    is_add11 = Column(BOOLEAN)
    is_add13 = Column(BOOLEAN)
    is_sharp5 = Column(BOOLEAN)
    is_flat5 = Column(BOOLEAN)
    is_omit3 = Column(BOOLEAN)
    is_omit5 = Column(BOOLEAN)
    is_omit7 = Column(BOOLEAN)
    is_omit9 = Column(BOOLEAN)
    is_omit11 = Column(BOOLEAN)
    is_sus2 = Column(BOOLEAN)
    is_sus4 = Column(BOOLEAN)

    inversion_uid = Column(INT)
    inversion_math_name = Column(TEXT)

    n1_uid = Column(INT)
    n1_math_name = Column(TEXT(3))

    n2_uid = Column(INT)
    n2_math_name = Column(TEXT(3))
    n2_octave = Column(INT)

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT(3))
    n3_octave = Column(INT)

    n4_uid = Column(INT)
    n4_math_name = Column(TEXT(3))
    n4_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT(3))
    n5_octave = Column(INT)

    n6_uid = Column(INT)
    n6_math_name = Column(TEXT(3))
    n6_octave = Column(INT)

    n7_uid = Column(INT)
    n7_math_name = Column(TEXT(3))
    n7_octave = Column(INT)
