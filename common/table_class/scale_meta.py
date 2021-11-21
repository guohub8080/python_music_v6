#!/usr/bin/env python
# @Time    : 2021/11/3 8:45 上午
# @Author  : guo2018@88.com

from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Scale_Meta(Base):  # 继承生成的orm基类
    __tablename__ = "scale_meta"  # 表名
    # id = Column(INT)  # 设置主键
    scale_term = Column(TEXT(10), primary_key=True)
    scale_name = Column(TEXT(50))
    scale_description = Column(TEXT(50))
    prefix_list = Column(TEXT)
    notes_num = Column(INT)
    chord3_list = Column(TEXT)
    chord7_list = Column(TEXT)


if __name__ == '__main__':
    input("请注意，即将创建表，不要轻易确定1。")
    input("请注意，即将创建表，不要轻易确定2。")
    input("请注意，即将创建表，不要轻易确定3。")
    from sqlalchemy import create_engine
    from common.settings import DB_SQL_LOCATION

    engine = create_engine(DB_SQL_LOCATION, echo=True)
    Base.metadata.create_all(engine)
