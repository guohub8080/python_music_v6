#!/usr/bin/env python
# @Time    : 2021/11/14 3:27 下午
# @Author  : guo2018@88.com


from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Chord(Base):  # 继承生成的orm基类
    __tablename__ = "chord"  # 表名
    id = Column(INT, primary_key=True)  # 设置主键
    rn_uid = Column(INT)
    is_valid = Column(BOOLEAN)
    rn_math_name = Column(TEXT)
    chord_base_id = Column(INT)
    chord_base_term = Column(TEXT)
    chord_full_term = Column(TEXT)
    chord_uid_list = Column(TEXT)
    chord_octave_list = Column(TEXT)
    chord_math_name_list = Column(TEXT)
    base_chord_type = Column(INT)
    description = Column(TEXT)
    note_num = Column(INT)
    inversion_uid = Column(INT)
    inversion_math_name = Column(TEXT)
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
