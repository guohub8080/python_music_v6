#!/usr/bin/env python
# @Time    : 2021/11/3 10:36 上午
# @Author  : guo2018@88.com
import music21

from common.settings import DB_SQL_LOCATION
from sqlalchemy import create_engine

from common.table_class.meta import Table_Meta

from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_SQL_LOCATION)
session = sessionmaker(bind=engine)()
all_notes = [i.math_name for i in session.query(Table_Meta).filter(Table_Meta.uid < 8).all()]


# print(all_notes)
def insert_note(note_name, octave):
    from note import Note
    note_instance = Note(note_name, octave)
    m21_instance = note_instance.music21_instance
    m21_instance.addLyric(f"{note_instance.art_name}{octave}")
    return m21_instance


score = music21.stream.Score()
part1 = music21.stream.Part()
part2 = music21.stream.Part()
part2.clef = music21.clef.FClef()
for i in all_notes:
    part1.append(insert_note(i, 4))
for i in all_notes:
    part1.append(insert_note(i, 5))

for i in all_notes:
    part2.append(insert_note(i, 2))
for i in all_notes:
    part2.append(insert_note(i, 3))
score.append(part1)
score.append(part2)
score.show()
