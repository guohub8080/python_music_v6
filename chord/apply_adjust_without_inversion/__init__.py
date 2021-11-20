#!/usr/bin/env python
# @Time    : 2021/11/15 10:19 下午
# @Author  : guo2018@88.com
from note import Note
from chord.CHORD_META import Adjust_Chord


def apply(origin_list: list[0, Note], adjust_info: Adjust_Chord):
    root_note_instance: Note = origin_list[0]
    # 先来处理sus：
    if adjust_info.adjust_sus == 2:
        adjust_info.adjust_omit[2] = True
        adjust_info.adjust_add[1] = True
    elif adjust_info.adjust_sus == 4:
        adjust_info.adjust_omit[2] = True
        adjust_info.adjust_add[3] = True
    final_list = origin_list
    final_list.extend([0 for i in range(13 - len(origin_list))])
    # print(final_list)
    # print(adjust_info.adjust_add)
    # print(adjust_info.adjust_move)
    # print(adjust_info.adjust_omit)
    # 开始循环：
    for v in range(len(adjust_info.adjust_add)):
        # 1. 如果add、move和omit三项都是空的，那么就直接跳过，什么都不做：
        if not (adjust_info.adjust_add[v] or adjust_info.adjust_omit[v] or adjust_info.adjust_move[v]):
            continue
        # 2. omit优先，如果omit存在就不管move和add了：
        if adjust_info.adjust_omit[v]:
            final_list[v] = 0
            continue

        # 3. move和add的话，其实是move优先。如果对一个不存在的音符进行move，那么意思是先add再move。否则就要先判断move的音符存不存在。
        # def execute_add(v):
        #     prefix = "大" if (v + 1) in (1, 4, 5, 8, 11, 12) else "纯"
        #     final_list[v] = root_note_instance.get_note_by_interval("大" if (v + 1) in (1, 4, 5, 8, 11, 12) else "纯", v + 1)

        if adjust_info.adjust_move[v]:
            # 3.1 如果原来的list里面没有，那么就先添加一个音符：
            if not final_list[v]:
                final_list[v] = root_note_instance.get_note_by_interval("纯" if (v + 1) in (1, 4, 5, 8, 11, 12) else "大",
                                                                        v + 1)
            # 3.2如果原来的list里面存在，那么就变换：
            final_list[v] = final_list[v].sharp_or_flat_adjust(adjust_info.adjust_move[v])
            continue
        # 4. add是最后来处理的：
        if adjust_info.adjust_add[v]:
            final_list[v] = root_note_instance.get_note_by_interval("纯" if (v + 1) in (1, 4, 5, 8, 11, 12) else "大",
                                                                    v + 1)

    while not final_list[-1]:
        final_list = final_list[0:len(final_list) - 1]
    return final_list


if __name__ == '__main__':
    oritin = [Note("C"), 0, Note("e"), 0, Note("g")]
    ad = Adjust_Chord()
    # ad.move(2, 1).move(4, -1)
    ad.sus(2)
    ad.move(9, 1)
    print(ad.adjust_move)
    b = apply(oritin, ad)
    print(b)
    [print(i.math_name, i.octave) for i in b if i]
