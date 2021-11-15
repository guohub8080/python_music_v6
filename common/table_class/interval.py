#!/usr/bin/env python
# @Time    : 2021/8/20 10:01 下午
# @Author  : guo2018@88.com

from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Interval(Base):  # 继承生成的orm基类
    __tablename__ = "interval"  # 表名
    id = Column(INT, primary_key=True)
    n1_uid = Column(INT)
    # n1_math_name = Column(TEXT(3))
    n2_uid = Column(INT)
    # n2_math_name = Column(TEXT(3))

    octave_gap = Column(INT)
    index_gap = Column(INT)
    semi_gap = Column(INT)
    interval_type = Column(INT)

    trend = Column(TEXT(3))
    prefix = Column(TEXT(3))

    is_valid = Column(BOOLEAN)
