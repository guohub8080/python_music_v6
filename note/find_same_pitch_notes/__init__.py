#!/usr/bin/env python
# @Time    : 2021/11/5 7:59 下午
# @Author  : guo2018@88.com


# 找到同音的函数，例如升C其实又是降D，还是重升B：
def execute(uid, loc_id, semitone, octave):
    from sqlalchemy import create_engine
    from note import Note
    from common.table_class.meta import Table_Meta
    from sqlalchemy.orm import sessionmaker

    from common.settings import DB_SQL_LOCATION
    session = sessionmaker(bind=create_engine(DB_SQL_LOCATION))()
    the_result = session.query(Table_Meta).filter(Table_Meta.uid != uid).filter(Table_Meta.loc_id == loc_id).all()
    notes_list = []

    for i in the_result:
        if getattr(i, "semitone") == semitone:
            new_note = Note(getattr(i, "uid"), octave)
            notes_list.append(new_note)
        elif getattr(i, "semitone") > semitone:
            new_note = Note(getattr(i, "uid"), octave - 1)
            notes_list.append(new_note)
        else:
            new_note = Note(getattr(i, "uid"), octave + 1)
            notes_list.append(new_note)
    return notes_list


if __name__ == '__main__':
    a = execute(19, 9, 8, 4)
    print(a)
    for i in a:
        print(i)
