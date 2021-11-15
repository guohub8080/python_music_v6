#!/usr/bin/env python
# @Time    : 2021/8/26 2:43 下午
# @Author  : guo2018@88.com

from note import Note
from sqlalchemy.orm import aliased

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_old import Table_Chord7
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()

res = session.query(Table_Chord7).all()
session.close()
# print(res)
for i in res:
    if i.chord_term == "maj7":
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

            note_7 = root_note.interval.M7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "min7":
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

            note_7 = root_note.interval.m7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "dom7":
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

            note_7 = root_note.interval.m7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "dim7":
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

            note_7 = root_note.get_note_by_interval("减", 7)
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "mm7":
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

            note_7 = root_note.interval.M7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "aug_maj7":
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

            note_7 = root_note.interval.M7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "aug_min7":
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

            note_7 = root_note.interval.m7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "aug_maj7":
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

            note_7 = root_note.interval.M7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
    elif i.chord_term == "half_dim7":
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

            note_7 = root_note.interval.m7
            note_7_pack = session.query(Table_Meta).filter(Table_Meta.uid == note_7.uid).one_or_none()
            note_7_math_name = note_7_pack.math_name
            note_7_uid = note_7_pack.uid
            note_7_octave = note_7.octave - root_note.octave

            assert note_3.is_valid and note_5.is_valid and note_7.is_valid

            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({
                "is_valid": 1,
                "n3_uid": note_3_uid,
                "n3_math_name": note_3_math_name,
                "n3_octave": note_3_octave,
                "n5_uid": note_5_uid,
                "n5_math_name": note_5_math_name,
                "n5_octave": note_5_octave,
                "n7_uid": note_7_uid,
                "n7_math_name": note_7_math_name,
                "n7_octave": note_7_octave
            })
            session.commit()
        except:
            session.query(Table_Chord7).filter(i.id == Table_Chord7.id).update({"is_valid": 0})
            session.commit()
            session.close()
