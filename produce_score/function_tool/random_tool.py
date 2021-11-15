#!/usr/bin/env python
# @Time    : 2021/11/3 4:55 下午
# @Author  : guo2018@88.com
from produce_score.SCORE_META import POSSIBLE_BEATS_AND_WIGHT


# 这个函数的作用是，输入一个概率，然后输出True的概率就是给定的概率值。如果不输入，那么就真的随机输出True，不区分概率。
# 例如，给定0.6，就是60%的可能性输出True。
# 该函数已经经过测试，100%可信。
def random_probability(probability=-1.0):
    if probability < 0:
        from random import choice
        return choice([True, False])
    from random import random
    temp_value = random()
    if probability > temp_value:
        return True
    return False


# list的加权算法：给定一个list，给出最终选择的一个下标。list的模板如下：
# the_list = [ [ a, weight_a ], [ b, weight_b ], ...]
def random_list_with_weight(weight_list: list[list] = POSSIBLE_BEATS_AND_WIGHT):
    weight_list = sorted(weight_list, key=lambda x: x[-1], reverse=True)
    whole_wights_list = [i[-1] for i in weight_list]
    # print(whole_wights_list)
    total_wights = sum(whole_wights_list)
    from random import uniform
    judge_value = uniform(0, total_wights)
    # print(judge_value)
    correct_selected_index = -1
    while total_wights > judge_value:
        correct_selected_index += 1
        total_wights -= whole_wights_list[correct_selected_index]
    return weight_list[correct_selected_index][0]


def random_weight():
    pass


if __name__ == '__main__':
    from produce_score.SCORE_META import POSSIBLE_BEATS_AND_WIGHT

    print(random_list_with_weight(POSSIBLE_BEATS_AND_WIGHT))
