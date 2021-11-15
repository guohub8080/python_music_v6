#!/usr/bin/env python
# @Time    : 2021/8/26 2:43 下午
# @Author  : guo2018@88.com

from note import Note
from sqlalchemy.orm import aliased

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_old import Table_Chord3
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()

res = session.query(Table_Chord3).all()
session.close()
# print(res)
for i in res:
    if i.chord_term == "maj3":
        try:
            root_note = Note(i.rn_uid)
            note_3 = root_note.interval.M3
            note_3_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_3.uid).one_or_none()
            note_3_math_name = note_3_pack.math_name
            note_3_uid = note_3_pack.uid
            note_3_octave = note_3.octave - root_note.octave

            note_5 = root_note.interval.P5
            note_5_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_5.uid).one_or_none()
            note_5_math_name = note_5_pack.math_name
            note_5_uid = note_5_pack.uid
            note_5_octave = note_5.octave - root_note.octave
            assert note_3.is_valid and note_5.is_valid

            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
            })
            session.commit()
        except:
            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "min3":
        try:
            root_note = Note(i.rn_uid)
            note_3 = root_note.interval.m3
            note_3_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_3.uid).one_or_none()
            note_3_math_name = note_3_pack.math_name
            note_3_uid = note_3_pack.uid
            note_3_octave = note_3.octave - root_note.octave

            note_5 = root_note.interval.P5
            note_5_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_5.uid).one_or_none()
            note_5_math_name = note_5_pack.math_name
            note_5_uid = note_5_pack.uid
            note_5_octave = note_5.octave - root_note.octave
            assert note_3.is_valid and note_5.is_valid

            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
            })
            session.commit()
        except:
            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "aug3":
        try:
            root_note = Note(i.rn_uid)
            note_3 = root_note.interval.M3
            note_3_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_3.uid).one_or_none()
            note_3_math_name = note_3_pack.math_name
            note_3_uid = note_3_pack.uid
            note_3_octave = note_3.octave - root_note.octave

            note_5 = root_note.interval.AUG5
            note_5_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_5.uid).one_or_none()
            note_5_math_name = note_5_pack.math_name
            note_5_uid = note_5_pack.uid
            note_5_octave = note_5.octave - root_note.octave
            assert note_3.is_valid and note_5.is_valid

            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
            })
            session.commit()
        except:
            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "dim3":
        try:
            root_note = Note(i.rn_uid)
            note_3 = root_note.interval.m3
            note_3_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_3.uid).one_or_none()
            note_3_math_name = note_3_pack.math_name
            note_3_uid = note_3_pack.uid
            note_3_octave = note_3.octave - root_note.octave

            note_5 = root_note.interval.dim5
            note_5_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_5.uid).one_or_none()
            note_5_math_name = note_5_pack.math_name
            note_5_uid = note_5_pack.uid
            note_5_octave = note_5.octave - root_note.octave
            assert note_3.is_valid and note_5.is_valid

            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
            })
            session.commit()
        except:
            session.query(Table_Chord3).filter(i.id == Table_Chord3.id).update({"is_valid": 0})
            session.commit()
            session.close()

# session.add(new_add)
# 提交：
# session.commit()
