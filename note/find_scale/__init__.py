#!/usr/bin/env python
# @Time    : 2021/11/5 9:35 下午
# @Author  : guo2018@88.com


def execute(tonic_uid, tonic_octave, scale_term_or_id: [int, str]):
    from scale import Scale
    if isinstance(scale_term_or_id, str):
        return Scale(tonic_uid, tonic_octave, scale_term_or_id)

    from sqlalchemy import create_engine
    from common.table_class.scale_meta import Table_Scale_Meta
    from sqlalchemy.orm import sessionmaker

    from common.settings import DB_SQL_LOCATION
    scale_term = getattr(sessionmaker(bind=create_engine(DB_SQL_LOCATION))().query(Table_Scale_Meta).filter(
        Table_Scale_Meta.id == scale_term_or_id).one_or_none(), "scale_term")

    return Scale(tonic_uid, tonic_octave, scale_term)
