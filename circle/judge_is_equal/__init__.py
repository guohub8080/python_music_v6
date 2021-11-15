#!/usr/bin/env python
# @Time    : 2021/11/10 5:37 下午
# @Author  : guo2018@88.com
from circle import Circle


def execute(a_circle_instance: Circle, another_circle_instance: Circle):
    if len(a_circle_instance.whole_queue) != len(another_circle_instance.whole_queue):
        return [False, None, None]
    if a_circle_instance.whole_queue == another_circle_instance.whole_queue:
        return [True, 0, 0]
    for i in range(len(a_circle_instance.whole_queue)):
        if a_circle_instance.whole_queue == another_circle_instance.move(i).whole_queue:
            return [True, len(a_circle_instance.whole_queue) - i, i]
    return [False, None, None]


if __name__ == '__main__':
    a = Circle([1, 2, 3, 4, 5])
    b = Circle([5, 1, 2, 3, 4])
    print(a.is_equal_to(b))
