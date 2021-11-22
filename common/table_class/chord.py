#!/usr/bin/env python
# @Time    : 2021/11/14 3:27 下午
# @Author  : guo2018@88.com


from sqlalchemy import Column, TEXT, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Chord(Base):  # 继承生成的orm基类
    __tablename__ = "chord"  # 表名
    id = Column(INT, primary_key=True)  # 设置主键
    root_note_uid = Column(INT)
    root_note_loc_id = Column(INT)
    root_note_math_name = Column(TEXT)
    # is_valid = Column(BOOLEAN)

    chord_base_id = Column(INT)
    chord_base_term = Column(TEXT)
    chord_full_term = Column(TEXT)

    notes_uid_list = Column(TEXT)
    notes_loc_id_list = Column(TEXT)
    notes_clock_list = Column(TEXT)
    # notes_octave_list = Column(TEXT)
    notes_math_name_list = Column(TEXT)

    note_num = Column(INT)


if __name__ == '__main__':
    input("请注意，即将创建表，不要轻易确定1。")
    input("请注意，即将创建表，不要轻易确定2。")
    input("请注意，即将创建表，不要轻易确定3。")
    from sqlalchemy import create_engine
    from common.settings import DB_SQL_LOCATION

    engine = create_engine(DB_SQL_LOCATION, echo=True)
    Base.metadata.create_all(engine)
