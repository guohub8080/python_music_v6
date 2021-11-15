#!/usr/bin/env python
# @Time    : 2021/11/5 4:04 下午
# @Author  : guo2018@88.com
from note import Note

is_valid = False
scale_name = None
tonic_note = None
tonic_uid = 0
tonic_octave = 0
is_trans = False
key_signature = 0
scale_list = None
tonic_instance = None

scale_description = None


def get_info(input_tonic_uid, input_tonic_octave, scale_term):
    from scale.when_init import query_scale_from_db
    content_result = query_scale_from_db.query_scale_content(input_tonic_uid, input_tonic_octave, scale_term)
    if not content_result:
        return None
    global is_valid, is_trans, scale_name, scale_list, key_signature, tonic_uid, tonic_octave
    global tonic_instance, tonic_note, scale_description

    is_trans = content_result[0]
    tonic_instance = content_result[1][0]
    tonic_note = getattr(tonic_instance, "art_name")
    tonic_octave = getattr(tonic_instance, "octave")
    scale_list = content_result[1]
    meta_result = query_scale_from_db.query_scale_meta(scale_term)
    scale_name = getattr(meta_result, "scale_name")
    scale_description = getattr(meta_result, "scale_description")
    for i in scale_list:
        key_signature += i.bias

    is_valid = True
