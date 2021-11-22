#!/usr/bin/env python
# @Time    : 2021/8/21 10:52 下午
# @Author  : guo2018@88.com
# from note import Note


# 根据SQLAlchemy结果输出的键列表：
# 要求：输入的data必须是单个的table的数据，例如，session.query(XXX).all()[0]
def get_sql_attr_list(data):
    return [i for i in dir(data) if (not i.startswith("_")) and (not i in ["metadata", "registry"])]


# 输入两个音符对象，输出他们的音程：
def interval_between_notes(note1, note2):
    from common.utils.func_interval_between_notes import execute
    return execute(note1, note2)


# 把全部列表转成无空格的字符串：
def trans_to_str(input_value):
    return str(input_value).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")


# 将数据库里面的列表类型的字符串转成列表：
def trans_str_to_list(input_str):
    from common.utils.trans_to_list import execute
    return execute(input_str)


if __name__ == '__main__':
    from note import Note

    n1 = Note("C+2", 6)
    n2 = Note("G")
    a = interval_between_notes(n1, n2)
    print(a)
    # chord_query((1, 2, 3))
