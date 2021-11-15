#!/usr/bin/env python
# @Time    : 2021/11/5 4:39 下午
# @Author  : guo2018@88.com
from sqlalchemy import create_engine
from note import Note
from common.table_class.scale import Table_Scale
from common.table_class.scale_meta import Table_Scale_Meta
from sqlalchemy.orm import sessionmaker

from common.settings import DB_SQL_LOCATION


def query_scale_content(input_tonic_uid, input_tonic_octave, scale_term):
    scale_term = str(scale_term).upper()
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    result = session.query(Table_Scale).filter(Table_Scale.is_valid == True).filter(
        Table_Scale.rn_uid == input_tonic_uid).filter(Table_Scale.scale_term == scale_term).one_or_none()
    if not result:
        return None
    is_trans = getattr(result, "is_trans")
    note1 = Note(getattr(result, "n1_uid"), input_tonic_octave)
    note2 = Note(getattr(result, "n2_uid"), getattr(result, "n2_octave") + input_tonic_octave)
    note3 = Note(getattr(result, "n3_uid"), getattr(result, "n3_octave") + input_tonic_octave)
    note4 = Note(getattr(result, "n4_uid"), getattr(result, "n4_octave") + input_tonic_octave)
    note5 = Note(getattr(result, "n5_uid"), getattr(result, "n5_octave") + input_tonic_octave)
    note6 = Note(getattr(result, "n6_uid"), getattr(result, "n6_octave") + input_tonic_octave)
    note7 = Note(getattr(result, "n7_uid"), getattr(result, "n7_octave") + input_tonic_octave)
    next_rn = Note(getattr(result, "next_rn_uid"), getattr(result, "next_rn_octave") + input_tonic_octave)

    notes_list = [note1, note2, note3, note4, note5, note6, note7]
    # for i in notes_list:
    #     print(i)
    return [is_trans, notes_list, next_rn]


def query_scale_meta(scale_term):
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    result = session.query(Table_Scale_Meta).filter(Table_Scale_Meta.scale_term == scale_term).one_or_none()
    if result:
        return result
    return None


if __name__ == '__main__':
    a = query_scale_content(8, 1, "ION")
    for i in a[1]:
        print(i)
