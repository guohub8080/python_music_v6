#!/usr/bin/env python
# @Time    : 2021/11/14 10:48 下午
# @Author  : guo2018@88.com

from note import Note

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_meta import Table_Chord_Meta
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()

full_normal_uids = [getattr(i, "uid") for i in session.query(Table_Meta).filter(Table_Meta.is_normal == True).all()]

full_chord_term = [i for i in session.query(Table_Chord_Meta).all()]

for each_note_uid in full_chord_term:
    for each_chord_info in full_chord_term:
        session.query(Table_Chord_Meta).filter().all()
print(full_normal_uids)
print(full_chord_term)
