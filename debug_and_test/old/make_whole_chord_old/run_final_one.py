#!/usr/bin/env python
# @Time    : 2021/9/7 12:12 上午
# @Author  : guo2018@88.com

from debug_and_test.old.make_whole_chord_old import make_whole_chord7, make_whole_chord13, make_whole_chord11, \
    make_whole_chord3, make_whole_chord9
from multiprocessing import Process


# class MyProcess(Process):
    # def __init__(self, name):
    #     super().__init__()
    #     self.name = name
    #
    # def run(self):  # start会自动调用run
    #     print('{} is running'.format(self.name))


if __name__ == '__main__':
    p1 = Process(target=make_whole_chord3.make_whole_chord3)
    p2 = Process(target=make_whole_chord7.make_whole_chord7)
    p3 = Process(target=make_whole_chord9.make_whole_chord9)
    p4 = Process(target=make_whole_chord13.make_whole_chord13)
    p5 = Process(target=make_whole_chord11.make_whole_chord11)
    p1.start()
    print("P1 start...")

    p2.start()
    print("P2 start...")

    p3.start()
    print("P3 start...")
    p4.start()
    print("P4 start...")
    p5.start()
    print("P5 start...")

    #
    #
    # make_whole_chord3.make_whole_chord3()
    # make_whole_chord7.make_whole_chord7()
    # make_whole_chord9.make_whole_chord9()
    # make_whole_chord11.make_whole_chord11()
    # make_whole_chord13.make_whole_chord13()
