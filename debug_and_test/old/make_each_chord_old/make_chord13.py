#!/usr/bin/env python
# @Time    : 2021/8/26 2:43 下午
# @Author  : guo2018@88.com

from note import Note
from common.settings import CENTER_C_LOCATION

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_old import Table_Chord9, Table_Chord7, Table_Chord11, Table_Chord13
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()
chord13_suffix = ["maj13", "min13", "aug13", "dim13"]
res = session.query(Table_Chord11).all()

for i in res:
    for chord13_suffix_item in chord13_suffix:
        new_n13_term = "{}_{}".format(getattr(i, "chord_term"), chord13_suffix_item)
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

        n9_uid = getattr(i, "n9_uid")
        n9_octave = getattr(i, "n9_octave")
        n9_math_name = getattr(i, "n9_math_name")

        n11_uid = getattr(i, "n11_uid")
        n11_octave = getattr(i, "n11_octave")
        n11_math_name = getattr(i, "n11_math_name")

        is_valid = False
        if getattr(i, "is_valid"):
            is_valid = True

        note_13 = None
        if chord13_suffix_item == "maj13":
            note_13 = Note(rn_math_name).interval.M13
        elif chord13_suffix_item == "min13":
            note_13 = Note(rn_math_name).interval.m13
        elif chord13_suffix_item == "aug13":
            note_13 = Note(rn_math_name).interval.AUG13
        elif chord13_suffix_item == "dim13":
            note_13 = Note(rn_math_name).interval.dim13
        new_add = None
        if (not note_13.is_valid) or (not is_valid):
            new_add = Table_Chord13(
                rn_uid=rn_uid,
                rn_math_name=rn_math_name,
                rn_art_name=rn_art_name,
                chord_term=new_n13_term,
                is_valid=False
            )
            session.add(new_add)
            continue

        new_add = Table_Chord13(
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
            n9_uid=n9_uid,
            chord_term=new_n13_term,
            n9_math_name=n9_math_name,
            n9_octave=n9_octave,
            n11_uid=n11_uid,
            n11_math_name=n11_math_name,
            n11_octave=n11_octave,
            n13_uid=note_13.uid,
            n13_math_name=note_13.math_name,
            n13_octave=note_13.octave - CENTER_C_LOCATION
        )
        session.add(new_add)
        session.commit()
        # print(new_n9_term)
        # print(i.rn_uid)
