#!/usr/bin/env python
# @Time    : 2021/11/3 8:45 上午
# @Author  : guo2018@88.com

from sqlalchemy import Column, TEXT, BOOLEAN, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 生成orm基类


class Table_Scale_Meta(Base):  # 继承生成的orm基类
    __tablename__ = "scale_meta"  # 表名
    id = Column(INT)  # 设置主键
    scale_term = Column(TEXT(10), primary_key=True)
    scale_name = Column(TEXT(50))
    scale_description = Column(TEXT(50))
    scale2_prefix = Column(TEXT(3))
    scale3_prefix = Column(TEXT(3))
    scale4_prefix = Column(TEXT(3))
    scale5_prefix = Column(TEXT(3))
    scale6_prefix = Column(TEXT(3))
    scale7_prefix = Column(TEXT(3))
    i3 = Column(TEXT)
    ii3 = Column(TEXT)
    iii3 = Column(TEXT)
    iv3 = Column(TEXT)
    v3 = Column(TEXT)
    vi3 = Column(TEXT)
    vii3 = Column(TEXT)
    i7 = Column(TEXT)
    ii7 = Column(TEXT)
    iii7 = Column(TEXT)
    iv7 = Column(TEXT)
    v7 = Column(TEXT)
    vi7 = Column(TEXT)
    vii7 = Column(TEXT)


if __name__ == '__main__':
    input("请注意，即将创建表，不要轻易确定1。")
    input("请注意，即将创建表，不要轻易确定2。")
    input("请注意，即将创建表，不要轻易确定3。")
    from sqlalchemy import create_engine
    from common.settings import DB_SQL_LOCATION

    engine = create_engine(DB_SQL_LOCATION, echo=True)
    Base.metadata.create_all(engine)
