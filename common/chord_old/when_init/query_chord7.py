#!/usr/bin/env python
# @Time    : 2021/8/26 12:14 上午
# @Author  : guo2018@88.com
from sqlalchemy.orm import aliased

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta
from common.table_class.chord_old import Table_Chord7
from sqlalchemy.orm import sessionmaker


def execute(root_note_instance, chord_term):
    from note import Note
    assert isinstance(root_note_instance, Note)
    chord_term = str(chord_term).lower()
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    note3_meta = aliased(Table_Meta)
    note5_meta = aliased(Table_Meta)
    note7_meta = aliased(Table_Meta)
    # aaa = aliased(Table_Meta)
    data = session.query(Table_Chord7, note3_meta, note5_meta, note7_meta).outerjoin(
        note3_meta, note3_meta.uid == Table_Chord7.n3_uid).outerjoin(
        note5_meta, note5_meta.uid == Table_Chord7.n5_uid).outerjoin(
        note7_meta, note7_meta.uid == Table_Chord7.n7_uid).filter(
        Table_Chord7.chord_term == chord_term).filter(
        Table_Chord7.rn_uid == root_note_instance.uid).filter(
        Table_Chord7.is_valid == 1).one_or_none()
    if data:
        note_3_uid = getattr(data[1], "uid")
        note_3_octave = getattr(data[0], "n3_octave")
        note_3_instance = Note(note_3_uid, root_note_instance.octave + note_3_octave)
        note_5_uid = getattr(data[2], "uid")
        note_5_octave = getattr(data[0], "n5_octave")
        note_5_instance = Note(note_5_uid, root_note_instance.octave + note_5_octave)
        note_7_uid = getattr(data[3], "uid")
        note_7_octave = getattr(data[0], "n7_octave")
        note_7_instance = Note(note_7_uid, root_note_instance.octave + note_7_octave)
        return [root_note_instance, note_3_instance, note_5_instance, note_7_instance]
    return None


if __name__ == '__main__':
    from note import Note

    print(Note("F").uid)
    a = execute(Note("F"), "maj7")
    print(a)
    [print(i) for i in a]
    # print(a[0].rn_uid, a[0].rn_math_name, a[1].uid, a[1].math_name, a[2].uid, a[2].math_name)
