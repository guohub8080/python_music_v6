#!/usr/bin/env python
# @Time    : 2021/8/21 7:48 下午
# @Author  : guo2018@88.com

uid = None
math_name = None
art_name = None
index = None
bias = None
is_black = False
loc_id = None
semitone = None
is_valid = False
is_normal = False


def get_info(name):
    assert isinstance(name, str) or isinstance(name, int)
    info_pack = None

    # 如果是字母查询：
    if isinstance(name, str):
        from note.when_init.query_meta import get_by_math_name
        info_pack = get_by_math_name(name)
    # 如果使用uid查询：
    elif isinstance(name, int):
        from note.when_init.query_meta import get_by_uid
        info_pack = get_by_uid(name)

    if info_pack:
        # print(key_list)
        global uid, math_name, art_name, index, bias, is_black, loc_id, semitone, is_valid, is_normal
        uid = getattr(info_pack, "uid")
        art_name = getattr(info_pack, "art_name")
        math_name = getattr(info_pack, "math_name")
        index = getattr(info_pack, "index")
        bias = getattr(info_pack, "bias")
        is_black = getattr(info_pack, "is_black")
        loc_id = getattr(info_pack, "loc_id")
        semitone = getattr(info_pack, "semitone")
        is_normal = getattr(info_pack, "is_normal")
        is_valid = True
        return
    return None


def make_music21_instance(note_name, note_octave, note_bias):
    from note.when_init.create_by_music21 import execute
    return execute(note_name, note_octave, note_bias)


if __name__ == '__main__':
    get_info(1)
    print(is_valid)
    print(uid)
