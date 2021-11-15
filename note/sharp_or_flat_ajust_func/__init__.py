#!/usr/bin/env python
# @Time    : 2021/8/21 11:48 下午
# @Author  : guo2018@88.com

from note import Note


def adjust_semitone(target_note_instace, sharp_or_flat_value=0):
    assert isinstance(target_note_instace, Note) and isinstance(sharp_or_flat_value, int)
    from sqlalchemy import create_engine
    from common.table_class.meta import Table_Meta
    from sqlalchemy.orm import sessionmaker
    from common.settings import DB_SQL_LOCATION
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    if not sharp_or_flat_value:
        return target_note_instace
    new_bias = target_note_instace.bias + sharp_or_flat_value
    new_note_info = session.query(Table_Meta).filter(Table_Meta.bias == new_bias).filter(
        Table_Meta.index == target_note_instace.index).one_or_none()
    if new_note_info:
        return Note(new_note_info.uid, target_note_instace.octave)
    return None


def adjust_semitone_to(target_note_instace, sharp_or_flat_value=0):
    assert isinstance(target_note_instace, Note) and isinstance(sharp_or_flat_value, int)
    from sqlalchemy import create_engine
    from common.table_class.meta import Table_Meta
    from sqlalchemy.orm import sessionmaker
    from common.settings import DB_SQL_LOCATION
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    new_note_info = session.query(Table_Meta).filter(Table_Meta.bias == sharp_or_flat_value).filter(
        Table_Meta.index == target_note_instace.index).one_or_none()
    if new_note_info:
        return Note(new_note_info.uid, target_note_instace.octave)
    return None
