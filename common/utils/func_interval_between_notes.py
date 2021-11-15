#!/usr/bin/env python
# @Time    : 2021/8/30 8:59 下午
# @Author  : guo2018@88.com

from note import Note


def execute(note1, note2):
    assert isinstance(note1, Note) and isinstance(note2, Note)
    from common.settings import DB_SQL_LOCATION
    from sqlalchemy import create_engine

    from common.table_class.interval import Table_Interval
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(DB_SQL_LOCATION)
    session = sessionmaker(bind=engine)()

    res = session.query(Table_Interval).filter(Table_Interval.n1_uid == note1.uid).filter(
        Table_Interval.n2_uid == note2.uid).filter(
        Table_Interval.octave_gap == note2.octave - note1.octave).filter(
        Table_Interval.is_valid == 1).one_or_none()

    if res:
        the_dict = {
            "trend": getattr(res, "trend"),
            "prefix": getattr(res, "prefix"),
            "interval_type": getattr(res, "interval_type"),
        }
        return the_dict
    return None
