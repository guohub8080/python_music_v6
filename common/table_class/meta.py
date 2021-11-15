#!/usr/bin/env python
# @Time    : 2021/8/20 10:01 下午
# @Author  : guo2018@88.com


from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Meta(Base):  # 继承生成的orm基类
    __tablename__ = "meta"  # 表名
    uid = Column(INT, primary_key=True)  # 设置主键
    loc_id = Column(INT)
    math_name = Column(TEXT(3))
    art_name = Column(TEXT(3))
    semitone = Column(INT)
    bias = Column(INT)
    index = Column(INT)
    is_black = Column(BOOLEAN)
    is_normal = Column(BOOLEAN)
