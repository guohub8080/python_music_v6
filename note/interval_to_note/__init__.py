#!/usr/bin/env python
# @Time    : 2021/8/22 10:51 上午
# @Author  : guo2018@88.com
from common.settings import DB_SQL_LOCATION
from common import get_sql_attr_list


def execute(origin_octave, origin_uid, prefix, interval_type, trend):
    from sqlalchemy import create_engine

    from common.table_class.meta import Table_Meta
    from common.table_class.interval import Table_Interval
    from sqlalchemy.orm import sessionmaker
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    data = session.query(Table_Interval, Table_Meta).outerjoin(Table_Meta, Table_Meta.uid == Table_Interval.n2_uid).filter(
        Table_Interval.n1_uid == origin_uid).filter(
        Table_Interval.interval_type == interval_type).filter(
        Table_Interval.prefix == prefix).filter(
        Table_Interval.is_valid == 1).filter(
        Table_Interval.trend == trend).one_or_none()
    if data:
        from note import Note
        return Note(data[1].math_name, origin_octave + data[0].octave_gap)

    return None


if __name__ == '__main__':
    from note import Note

    origin_note = Note("C", 5)
    print(origin_note)
    b = origin_note.get_note_by_interval("纯", 5,"下")
    # a = execute(5,1, "大", 2)
    # print(a)
    print(b)
