#!/usr/bin/env python
# @Time    : 2021/8/26 12:14 上午
# @Author  : guo2018@88.com
from note import Note
from sqlalchemy.orm import aliased

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_old import Table_Chord3
from sqlalchemy.orm import sessionmaker


def execute(root_note_instance, chord_term):
    # assert isinstance(root_note_instance, Note)
    chord_term = str(chord_term).lower()
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    note3_meta = aliased(Table_Meta)
    note5_meta = aliased(Table_Meta)
    data = session.query(Table_Chord3, note3_meta, note5_meta).outerjoin(
        note3_meta, note3_meta.uid == Table_Chord3.n3_uid).outerjoin(
        note5_meta, note5_meta.uid == Table_Chord3.n5_uid).filter(
        Table_Chord3.chord_term == chord_term).filter(
        Table_Chord3.rn_uid == root_note_instance.uid).filter(
        Table_Chord3.is_valid == 1).one_or_none()
    if data:
        note_3_uid = getattr(data[1], "uid")
        note_3_octave = getattr(data[0], "n3_octave")
        note_3_instance = Note(note_3_uid, root_note_instance.octave + note_3_octave)
        note_5_uid = getattr(data[2], "uid")
        note_5_octave = getattr(data[0], "n5_octave")
        note_5_instance = Note(note_5_uid, root_note_instance.octave + note_5_octave)
        return [root_note_instance, note_3_instance, note_5_instance]
    return None


if __name__ == '__main__':
    a = execute(Note(), "maj3")
    print(a)
    [print(i) for i in a]
    # print(a[0].rn_uid, a[0].rn_math_name, a[1].uid, a[1].math_name, a[2].uid, a[2].math_name)
