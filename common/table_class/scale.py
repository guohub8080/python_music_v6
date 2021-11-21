#!/usr/bin/env python
# @Time    : 2021/11/5 4:49 下午
# @Author  : guo2018@88.com

from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Scale(Base):  # 继承生成的orm基类
    __tablename__ = "scale"  # 表名
    id = Column(INT, primary_key=True)  # 设置主键
    given_root_note_uid = Column(INT)
    given_root_note_math_name = Column(TEXT)
    real_root_note_uid = Column(INT)
    real_root_note_math_name = Column(TEXT)
    is_trans = Column(BOOLEAN)

    scale_term = Column(TEXT(10))
    is_valid = Column(BOOLEAN)
    note_num = Column(INT)

    uid_list = Column(TEXT)
    octave_list = Column(TEXT)
    math_name_list = Column(TEXT)
if __name__ == '__main__':
    input("请注意，即将创建表，不要轻易确定1。")
    input("请注意，即将创建表，不要轻易确定2。")
    input("请注意，即将创建表，不要轻易确定3。")
    from sqlalchemy import create_engine
    from common.settings import DB_SQL_LOCATION

    engine = create_engine(DB_SQL_LOCATION, echo=True)
    Base.metadata.create_all(engine)
