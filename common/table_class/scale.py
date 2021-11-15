#!/usr/bin/env python
# @Time    : 2021/11/5 4:49 下午
# @Author  : guo2018@88.com

from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Scale(Base):  # 继承生成的orm基类
    __tablename__ = "scale"  # 表名
    id = Column(INT, primary_key=True)  # 设置主键
    rn_uid = Column(INT)
    rn_math_name = Column(TEXT)
    rn_art_name = Column(TEXT)
    scale_term = Column(TEXT(10))
    is_valid = Column(BOOLEAN)
    is_trans = Column(BOOLEAN)
    note_num = Column(INT)

    n1_uid = Column(INT)
    n1_math_name = Column(TEXT)

    n2_uid = Column(INT)
    n2_math_name = Column(TEXT)
    n2_octave = Column(INT)

    n3_uid = Column(INT)
    n3_math_name = Column(TEXT)
    n3_octave = Column(INT)

    n4_uid = Column(INT)
    n4_math_name = Column(TEXT)
    n4_octave = Column(INT)

    n5_uid = Column(INT)
    n5_math_name = Column(TEXT)
    n5_octave = Column(INT)

    n6_uid = Column(INT)
    n6_math_name = Column(TEXT)
    n6_octave = Column(INT)

    n7_uid = Column(INT)
    n7_math_name = Column(TEXT)
    n7_octave = Column(INT)

    next_rn_uid = Column(INT)
    next_rn_octave = Column(INT)
    next_rn_math_name = Column(TEXT)
