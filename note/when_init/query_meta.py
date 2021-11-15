#!/usr/bin/env python
# @Time    : 2021/8/21 7:38 下午
# @Author  : guo2018@88.com

from sqlalchemy import create_engine, func

from common.table_class.meta import Table_Meta
from sqlalchemy.orm import sessionmaker

from common.settings import DB_SQL_LOCATION


# 通过音符名称来查询，例如通过输入字符串“C”以确定音符。
def get_by_math_name(input_math_name):
    input_math_name = str(input_math_name).lower()
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    return session.query(Table_Meta).filter(func.lower(Table_Meta.math_name) == input_math_name).one_or_none()


# 通过uid来查找音符，通过直接查找1来找到C。
def get_by_uid(input_uid):
    assert isinstance(input_uid, int)
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    return session.query(Table_Meta).filter(Table_Meta.uid == input_uid).one_or_none()


# 测试：
if __name__ == '__main__':
    a = get_by_math_name("C-1")
    print(a)
    print(dir(a))
    c = [i for i in dir(a) if (not i.startswith("_")) and (not i in ["metadata", "registry"])]
    print(c)
    for i in c:
        print(i, ":", getattr(a, i))

    print("*" * 50)
    e = get_by_uid(1)
    print(e)
    for i in c:
        print(i, ":", getattr(e, i))
