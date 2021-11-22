#!/usr/bin/env python
# @Time    : 2021/11/5 4:04 下午
# @Author  : guo2018@88.com

scale_name = None
tonic_note = None

is_trans = False
key_signature = 0
scale_list = None

scale_description = None


def get_info(input_tonic_uid, input_tonic_octave, scale_term):
    # from common.scale_old.when_init import query_scale_from_db
    # content_result = query_scale_from_db.query_scale_content(input_tonic_uid, input_tonic_octave, scale_term)
    # if not content_result:
    #     return None
    global is_trans, scale_name, scale_list, key_signature
    global tonic_note, scale_description
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from common.table_class.scale import Table_Scale
    from common.table_class.scale_meta import Table_Scale_Meta
    from common import trans_str_to_list
    from common.settings import DB_SQL_LOCATION, CENTER_C_LOCATION

    from note import Note

    engine = create_engine(DB_SQL_LOCATION)
    session = sessionmaker(bind=engine)()
    the_result = session.query(Table_Scale).filter(
        Table_Scale.given_root_note_uid == input_tonic_uid).filter(Table_Scale.scale_term == scale_term).one_or_none()
    if the_result:
        the_scale_term = getattr(the_result, "scale_term")
        scale_meta = session.query(Table_Scale_Meta).filter(Table_Scale_Meta.scale_term == the_scale_term).one()
        scale_name = getattr(scale_meta, "scale_name")
        scale_description = getattr(scale_meta, "scale_description")
        # the_root_note_uid = getattr(the_result, "real_root_note_uid")
        is_trans = getattr(the_result, "is_trans")
        key_signature = getattr(the_result, "sharp_flat_num")
        the_uid_list: list[int] = trans_str_to_list(getattr(the_result, "uid_list"))
        the_octave_list: list[int] = trans_str_to_list(getattr(the_result, "octave_list"))
        # root_note_instance = Note(the_root_note_uid, input_tonic_octave)
        scale_list_result = []
        for i in range(len(the_uid_list)):
            scale_list_result.append(Note(the_uid_list[i], the_octave_list[i] + input_tonic_octave))
        scale_list = scale_list_result
        tonic_note = scale_list_result[0]
