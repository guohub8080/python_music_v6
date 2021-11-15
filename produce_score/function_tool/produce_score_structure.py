#!/usr/bin/env python
# @Time    : 2021/11/3 8:38 下午
# @Author  : guo2018@88.com

from produce_score import Score, Part


# 把东西装入另一个容器的函数，比较可以见名知意：
def put_one_or_many_A_into_B_return_B(a: [list, object], b):
    assert hasattr(b, "append")
    if isinstance(a, list):
        for i in a:
            b.append(i)
        return b
    b.append(a)
    return b


# 这是对已有的数据集进行添加渲染的函数。
# 如何生成，请去generator里面。
def produce_score(info_pack_instance):
    # 要把实例化的数据包（例如速度多少等等）一并填入进去。
    # assert isinstance(info_pack_instance, Score)
    # 一套标准的Python乐谱格式是这样的：
    # score_file = [ [ part1_content ] , [ part2_content ] ]
    # part_content = [ [ measure1_content ] , [ measure2_content ] ]
    # measure_content = [ note1 , note2 , note3 ... ]
    # 先加一层断言：整个score就是一个list，并且长度为1

    # ====================================================================================
    # 第一步：新建乐谱，并定义元数据。
    import music21
    final_score_instance = music21.stream.Score()
    score_meta = music21.metadata.Metadata()
    score_meta.title = info_pack_instance.title
    score_meta.composer = info_pack_instance.composer
    final_score_instance.metadata = score_meta

    # ====================================================================================
    # 第二步：新建Part部分，并定义和Part有关的元数据。
    # score文件下一层，是part层：
    assert isinstance(info_pack_instance.part_content, list)
    for each_part in info_pack_instance.part_content:
        # assert isinstance(each_part, Part)
        part_instance = music21.stream.Part()
        part_instance.partName = each_part.part_name
        if each_part.is_F_clef:
            part_instance.append(music21.clef.FClef())

        part_instance.insert(0, music21.tempo.MetronomeMark(number=info_pack_instance.bpm))
        # print(info_pack_instance.key_signature)
        part_instance.insert(0, music21.meter.TimeSignature(info_pack_instance.time_signature))
        part_instance.insert(0, music21.key.KeySignature(info_pack_instance.key_signature))
        # ==============================================================================
        # 第三步：新建小节Measure部分，并定义和小节有关的元数据。
        for i in each_part.notes_content:
            part_instance.append(i)
        # ------- 小节处理完毕，别忘了把这一part添加到Score里面 --------------
        part_instance = part_instance.makeMeasures()
        final_score_instance.append(part_instance)
    return final_score_instance


if __name__ == '__main__':
    a = put_one_or_many_A_into_B_return_B([0, 1, 2, 3], [0])
    print(a)
