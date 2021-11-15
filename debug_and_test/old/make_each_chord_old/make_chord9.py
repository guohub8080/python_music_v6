#!/usr/bin/env python
# @Time    : 2021/8/26 2:43 下午
# @Author  : guo2018@88.com

from note import Note
from common.settings import CENTER_C_LOCATION

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_old import Table_Chord9, Table_Chord7
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()
chord9_suffix = ["maj9", "min9", "aug9", "dim9"]
res = session.query(Table_Chord7).all()

for i in res:
    for chord9_suffix_item in chord9_suffix:
        new_n9_term = "{}_{}".format(getattr(i, "chord_term"), chord9_suffix_item)
        rn_uid = getattr(i, "rn_uid")
        rn_math_name = getattr(i, "rn_math_name")
        rn_art_name = getattr(i, "rn_art_name")
        n3_uid = getattr(i, "n3_uid")
        n3_octave = getattr(i, "n3_octave")
        n3_math_name = getattr(i, "n3_math_name")

        n5_uid = getattr(i, "n5_uid")
        n5_octave = getattr(i, "n5_octave")
        n5_math_name = getattr(i, "n5_math_name")

        n7_uid = getattr(i, "n7_uid")
        n7_octave = getattr(i, "n7_octave")
        n7_math_name = getattr(i, "n7_math_name")

        is_valid = False
        if getattr(i, "is_valid"):
            is_valid = True

        note_9 = None

        if chord9_suffix_item == "maj9":
            note_9 = Note(rn_math_name).interval.M9
        elif chord9_suffix_item == "min9":
            note_9 = Note(rn_math_name).interval.m9
        elif chord9_suffix_item == "aug9":
            note_9 = Note(rn_math_name).interval.AUG9
        elif chord9_suffix_item == "dim9":
            note_9 = Note(rn_math_name).interval.dim9
        new_add = None
        if (not note_9.is_valid) or (not is_valid):
            new_add = Table_Chord9(
                rn_uid=rn_uid,
                rn_math_name=rn_math_name,
                rn_art_name=rn_art_name,
                chord_term=new_n9_term,
                is_valid=False
            )
            session.add(new_add)
            continue
        new_add = Table_Chord9(
            rn_uid=rn_uid,
            rn_math_name=rn_math_name,
            rn_art_name=rn_art_name,
            n3_uid=n3_uid,
            n3_octave=n3_octave,
            n3_math_name=n3_math_name,
            n5_uid=n5_uid,
            n5_octave=n5_octave,
            n5_math_name=n5_math_name,
            n7_octave=n7_octave,
            n7_math_name=n7_math_name,
            n7_uid=n7_uid,
            is_valid=True,
            n9_uid=note_9.uid,
            chord_term=new_n9_term,
            n9_math_name=note_9.math_name,
            n9_octave=note_9.octave - CENTER_C_LOCATION
        )
        session.add(new_add)
        session.commit()
        # print(new_n9_term)
        # print(i.rn_uid)
