#!/usr/bin/env python
# @Time    : 2021/11/14 3:29 下午
# @Author  : guo2018@88.com


from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Chord_Meta(Base):  # 继承生成的orm基类
    __tablename__ = "chord_meta"  # 表名
    id = Column(INT, primary_key=True)  # 设置主键
    chord_base_term = Column(TEXT)
    chord_full_term = Column(TEXT)
    base_chord_type = Column(INT)
    description = Column(TEXT)
    clock_list = Column(TEXT)
    octave_gap = Column(TEXT)
    semitone_gap_list = Column(TEXT)
    example = Column(TEXT)
    note_num = Column(INT)
    interval_prefix_list = Column(TEXT)

    move5 = Column(INT)
    move9 = Column(INT)
    move11 = Column(INT)
    move13 = Column(INT)

    is_add2 = Column(BOOLEAN)
    is_add4 = Column(BOOLEAN)
    is_add6 = Column(BOOLEAN)
    is_add9 = Column(BOOLEAN)
    is_add11 = Column(BOOLEAN)
    is_add13 = Column(BOOLEAN)


if __name__ == '__main__':
    input("请注意，即将创建表，不要轻易确定1。")
    input("请注意，即将创建表，不要轻易确定2。")
    input("请注意，即将创建表，不要轻易确定3。")
    from sqlalchemy import create_engine
    from common.settings import DB_SQL_LOCATION

    engine = create_engine(DB_SQL_LOCATION, echo=True)
    Base.metadata.create_all(engine)
