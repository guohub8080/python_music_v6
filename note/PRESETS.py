#!/usr/bin/env python
# @Time    : 2021/8/21 7:42 下午
# @Author  : guo2018@88.com

from note import Note
from common.settings import CENTER_C_LOCATION


class C(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("C", octave)


class D(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("D", octave)


class E(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("E", octave)


class F(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("F", octave)


class G(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("G", octave)


class A(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("A", octave)


class B(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("B", octave)


class C_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("C+1", octave)


class D_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("D+1", octave)


class E_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("E+1", octave)


class F_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("F+1", octave)


class G_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("G+1", octave)


class A_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("A+1", octave)


class B_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("B+1", octave)


class C_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("C-1", octave)


class D_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("D-1", octave)


class E_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("E-1", octave)


class F_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("F-1", octave)


class G_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("G-1", octave)


class A_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("A-1", octave)


class B_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("B-1", octave)


class C_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("C+2", octave)


class D_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("D+2", octave)


class E_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("E+2", octave)


class F_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("F+2", octave)


class G_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("G+2", octave)


class A_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("A+2", octave)


class B_DOUBLE_SHARP(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("B+2", octave)


class C_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("C-2", octave)


class D_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("D-2", octave)


class E_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("E-2", octave)


class F_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("F-2", octave)


class G_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("G-2", octave)


class A_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("A-2", octave)


class B_DOUBLE_FLAT(Note):
    def __init__(self, octave=CENTER_C_LOCATION):
        super().__init__("B-2", octave)

# C_0 = Note("C", 0)
# D_0 = Note("D", 0)
# E_0 = Note("E", 0)
# F_0 = Note("F", 0)
# G_0 = Note("G", 0)
# A_0 = Note("A", 0)
# B_0 = Note("B", 0)
# C_SHARP_0 = Note("C+1", 0)
# C_FLAT_0 = Note("C-1", 0)
# D_SHARP_0 = Note("D+1", 0)
# D_FLAT_0 = Note("D-1", 0)
# E_SHARP_0 = Note("E+1", 0)
# E_FLAT_0 = Note("E-1", 0)
# F_SHARP_0 = Note("F+1", 0)
# F_FLAT_0 = Note("F-1", 0)
# G_SHARP_0 = Note("G+1", 0)
# G_FLAT_0 = Note("G-1", 0)
# A_SHARP_0 = Note("A+1", 0)
# A_FLAT_0 = Note("A-1", 0)
# B_SHARP_0 = Note("B+1", 0)
# B_FLAT_0 = Note("B-1", 0)
# C_DOUBLE_SHARP_0 = Note("C+2", 0)
# C_DOUBLE_FLAT_0 = Note("C-2", 0)
# D_DOUBLE_SHARP_0 = Note("D+2", 0)
# D_DOUBLE_FLAT_0 = Note("D-2", 0)
# E_DOUBLE_SHARP_0 = Note("E+2", 0)
# E_DOUBLE_FLAT_0 = Note("E-2", 0)
# F_DOUBLE_SHARP_0 = Note("F+2", 0)
# F_DOUBLE_FLAT_0 = Note("F-2", 0)
# G_DOUBLE_SHARP_0 = Note("G+2", 0)
# G_DOUBLE_FLAT_0 = Note("G-2", 0)
# A_DOUBLE_SHARP_0 = Note("A+2", 0)
# A_DOUBLE_FLAT_0 = Note("A-2", 0)
# B_DOUBLE_SHARP_0 = Note("B+2", 0)
# C_1 = Note("C", 1)
# D_1 = Note("D", 1)
# E_1 = Note("E", 1)
# F_1 = Note("F", 1)
# G_1 = Note("G", 1)
# A_1 = Note("A", 1)
# B_1 = Note("B", 1)
# C_SHARP_1 = Note("C+1", 1)
# C_FLAT_1 = Note("C-1", 1)
# D_SHARP_1 = Note("D+1", 1)
# D_FLAT_1 = Note("D-1", 1)
# E_SHARP_1 = Note("E+1", 1)
# E_FLAT_1 = Note("E-1", 1)
# F_SHARP_1 = Note("F+1", 1)
# F_FLAT_1 = Note("F-1", 1)
# G_SHARP_1 = Note("G+1", 1)
# G_FLAT_1 = Note("G-1", 1)
# A_SHARP_1 = Note("A+1", 1)
# A_FLAT_1 = Note("A-1", 1)
# B_SHARP_1 = Note("B+1", 1)
# B_FLAT_1 = Note("B-1", 1)
# C_DOUBLE_SHARP_1 = Note("C+2", 1)
# C_DOUBLE_FLAT_1 = Note("C-2", 1)
# D_DOUBLE_SHARP_1 = Note("D+2", 1)
# D_DOUBLE_FLAT_1 = Note("D-2", 1)
# E_DOUBLE_SHARP_1 = Note("E+2", 1)
# E_DOUBLE_FLAT_1 = Note("E-2", 1)
# F_DOUBLE_SHARP_1 = Note("F+2", 1)
# F_DOUBLE_FLAT_1 = Note("F-2", 1)
# G_DOUBLE_SHARP_1 = Note("G+2", 1)
# G_DOUBLE_FLAT_1 = Note("G-2", 1)
# A_DOUBLE_SHARP_1 = Note("A+2", 1)
# A_DOUBLE_FLAT_1 = Note("A-2", 1)
# B_DOUBLE_SHARP_1 = Note("B+2", 1)
# C_2 = Note("C", 2)
# D_2 = Note("D", 2)
# E_2 = Note("E", 2)
# F_2 = Note("F", 2)
# G_2 = Note("G", 2)
# A_2 = Note("A", 2)
# B_2 = Note("B", 2)
# C_SHARP_2 = Note("C+1", 2)
# C_FLAT_2 = Note("C-1", 2)
# D_SHARP_2 = Note("D+1", 2)
# D_FLAT_2 = Note("D-1", 2)
# E_SHARP_2 = Note("E+1", 2)
# E_FLAT_2 = Note("E-1", 2)
# F_SHARP_2 = Note("F+1", 2)
# F_FLAT_2 = Note("F-1", 2)
# G_SHARP_2 = Note("G+1", 2)
# G_FLAT_2 = Note("G-1", 2)
# A_SHARP_2 = Note("A+1", 2)
# A_FLAT_2 = Note("A-1", 2)
# B_SHARP_2 = Note("B+1", 2)
# B_FLAT_2 = Note("B-1", 2)
# C_DOUBLE_SHARP_2 = Note("C+2", 2)
# C_DOUBLE_FLAT_2 = Note("C-2", 2)
# D_DOUBLE_SHARP_2 = Note("D+2", 2)
# D_DOUBLE_FLAT_2 = Note("D-2", 2)
# E_DOUBLE_SHARP_2 = Note("E+2", 2)
# E_DOUBLE_FLAT_2 = Note("E-2", 2)
# F_DOUBLE_SHARP_2 = Note("F+2", 2)
# F_DOUBLE_FLAT_2 = Note("F-2", 2)
# G_DOUBLE_SHARP_2 = Note("G+2", 2)
# G_DOUBLE_FLAT_2 = Note("G-2", 2)
# A_DOUBLE_SHARP_2 = Note("A+2", 2)
# A_DOUBLE_FLAT_2 = Note("A-2", 2)
# B_DOUBLE_SHARP_2 = Note("B+2", 2)
# C_3 = Note("C", 3)
# D_3 = Note("D", 3)
# E_3 = Note("E", 3)
# F_3 = Note("F", 3)
# G_3 = Note("G", 3)
# A_3 = Note("A", 3)
# B_3 = Note("B", 3)
# C_SHARP_3 = Note("C+1", 3)
# C_FLAT_3 = Note("C-1", 3)
# D_SHARP_3 = Note("D+1", 3)
# D_FLAT_3 = Note("D-1", 3)
# E_SHARP_3 = Note("E+1", 3)
# E_FLAT_3 = Note("E-1", 3)
# F_SHARP_3 = Note("F+1", 3)
# F_FLAT_3 = Note("F-1", 3)
# G_SHARP_3 = Note("G+1", 3)
# G_FLAT_3 = Note("G-1", 3)
# A_SHARP_3 = Note("A+1", 3)
# A_FLAT_3 = Note("A-1", 3)
# B_SHARP_3 = Note("B+1", 3)
# B_FLAT_3 = Note("B-1", 3)
# C_DOUBLE_SHARP_3 = Note("C+2", 3)
# C_DOUBLE_FLAT_3 = Note("C-2", 3)
# D_DOUBLE_SHARP_3 = Note("D+2", 3)
# D_DOUBLE_FLAT_3 = Note("D-2", 3)
# E_DOUBLE_SHARP_3 = Note("E+2", 3)
# E_DOUBLE_FLAT_3 = Note("E-2", 3)
# F_DOUBLE_SHARP_3 = Note("F+2", 3)
# F_DOUBLE_FLAT_3 = Note("F-2", 3)
# G_DOUBLE_SHARP_3 = Note("G+2", 3)
# G_DOUBLE_FLAT_3 = Note("G-2", 3)
# A_DOUBLE_SHARP_3 = Note("A+2", 3)
# A_DOUBLE_FLAT_3 = Note("A-2", 3)
# B_DOUBLE_SHARP_3 = Note("B+2", 3)
# C_4 = Note("C", 4)
# D_4 = Note("D", 4)
# E_4 = Note("E", 4)
# F_4 = Note("F", 4)
# G_4 = Note("G", 4)
# A_4 = Note("A", 4)
# B_4 = Note("B", 4)
# C_SHARP_4 = Note("C+1", 4)
# C_FLAT_4 = Note("C-1", 4)
# D_SHARP_4 = Note("D+1", 4)
# D_FLAT_4 = Note("D-1", 4)
# E_SHARP_4 = Note("E+1", 4)
# E_FLAT_4 = Note("E-1", 4)
# F_SHARP_4 = Note("F+1", 4)
# F_FLAT_4 = Note("F-1", 4)
# G_SHARP_4 = Note("G+1", 4)
# G_FLAT_4 = Note("G-1", 4)
# A_SHARP_4 = Note("A+1", 4)
# A_FLAT_4 = Note("A-1", 4)
# B_SHARP_4 = Note("B+1", 4)
# B_FLAT_4 = Note("B-1", 4)
# C_DOUBLE_SHARP_4 = Note("C+2", 4)
# C_DOUBLE_FLAT_4 = Note("C-2", 4)
# D_DOUBLE_SHARP_4 = Note("D+2", 4)
# D_DOUBLE_FLAT_4 = Note("D-2", 4)
# E_DOUBLE_SHARP_4 = Note("E+2", 4)
# E_DOUBLE_FLAT_4 = Note("E-2", 4)
# F_DOUBLE_SHARP_4 = Note("F+2", 4)
# F_DOUBLE_FLAT_4 = Note("F-2", 4)
# G_DOUBLE_SHARP_4 = Note("G+2", 4)
# G_DOUBLE_FLAT_4 = Note("G-2", 4)
# A_DOUBLE_SHARP_4 = Note("A+2", 4)
# A_DOUBLE_FLAT_4 = Note("A-2", 4)
# B_DOUBLE_SHARP_4 = Note("B+2", 4)
# C_5 = Note("C", 5)
# D_5 = Note("D", 5)
# E_5 = Note("E", 5)
# F_5 = Note("F", 5)
# G_5 = Note("G", 5)
# A_5 = Note("A", 5)
# B_5 = Note("B", 5)
# C_SHARP_5 = Note("C+1", 5)
# C_FLAT_5 = Note("C-1", 5)
# D_SHARP_5 = Note("D+1", 5)
# D_FLAT_5 = Note("D-1", 5)
# E_SHARP_5 = Note("E+1", 5)
# E_FLAT_5 = Note("E-1", 5)
# F_SHARP_5 = Note("F+1", 5)
# F_FLAT_5 = Note("F-1", 5)
# G_SHARP_5 = Note("G+1", 5)
# G_FLAT_5 = Note("G-1", 5)
# A_SHARP_5 = Note("A+1", 5)
# A_FLAT_5 = Note("A-1", 5)
# B_SHARP_5 = Note("B+1", 5)
# B_FLAT_5 = Note("B-1", 5)
# C_DOUBLE_SHARP_5 = Note("C+2", 5)
# C_DOUBLE_FLAT_5 = Note("C-2", 5)
# D_DOUBLE_SHARP_5 = Note("D+2", 5)
# D_DOUBLE_FLAT_5 = Note("D-2", 5)
# E_DOUBLE_SHARP_5 = Note("E+2", 5)
# E_DOUBLE_FLAT_5 = Note("E-2", 5)
# F_DOUBLE_SHARP_5 = Note("F+2", 5)
# F_DOUBLE_FLAT_5 = Note("F-2", 5)
# G_DOUBLE_SHARP_5 = Note("G+2", 5)
# G_DOUBLE_FLAT_5 = Note("G-2", 5)
# A_DOUBLE_SHARP_5 = Note("A+2", 5)
# A_DOUBLE_FLAT_5 = Note("A-2", 5)
# B_DOUBLE_SHARP_5 = Note("B+2", 5)
# C_6 = Note("C", 6)
# D_6 = Note("D", 6)
# E_6 = Note("E", 6)
# F_6 = Note("F", 6)
# G_6 = Note("G", 6)
# A_6 = Note("A", 6)
# B_6 = Note("B", 6)
# C_SHARP_6 = Note("C+1", 6)
# C_FLAT_6 = Note("C-1", 6)
# D_SHARP_6 = Note("D+1", 6)
# D_FLAT_6 = Note("D-1", 6)
# E_SHARP_6 = Note("E+1", 6)
# E_FLAT_6 = Note("E-1", 6)
# F_SHARP_6 = Note("F+1", 6)
# F_FLAT_6 = Note("F-1", 6)
# G_SHARP_6 = Note("G+1", 6)
# G_FLAT_6 = Note("G-1", 6)
# A_SHARP_6 = Note("A+1", 6)
# A_FLAT_6 = Note("A-1", 6)
# B_SHARP_6 = Note("B+1", 6)
# B_FLAT_6 = Note("B-1", 6)
# C_DOUBLE_SHARP_6 = Note("C+2", 6)
# C_DOUBLE_FLAT_6 = Note("C-2", 6)
# D_DOUBLE_SHARP_6 = Note("D+2", 6)
# D_DOUBLE_FLAT_6 = Note("D-2", 6)
# E_DOUBLE_SHARP_6 = Note("E+2", 6)
# E_DOUBLE_FLAT_6 = Note("E-2", 6)
# F_DOUBLE_SHARP_6 = Note("F+2", 6)
# F_DOUBLE_FLAT_6 = Note("F-2", 6)
# G_DOUBLE_SHARP_6 = Note("G+2", 6)
# G_DOUBLE_FLAT_6 = Note("G-2", 6)
# A_DOUBLE_SHARP_6 = Note("A+2", 6)
# A_DOUBLE_FLAT_6 = Note("A-2", 6)
# B_DOUBLE_SHARP_6 = Note("B+2", 6)
# C_7 = Note("C", 7)
# D_7 = Note("D", 7)
# E_7 = Note("E", 7)
# F_7 = Note("F", 7)
# G_7 = Note("G", 7)
# A_7 = Note("A", 7)
# B_7 = Note("B", 7)
# C_SHARP_7 = Note("C+1", 7)
# C_FLAT_7 = Note("C-1", 7)
# D_SHARP_7 = Note("D+1", 7)
# D_FLAT_7 = Note("D-1", 7)
# E_SHARP_7 = Note("E+1", 7)
# E_FLAT_7 = Note("E-1", 7)
# F_SHARP_7 = Note("F+1", 7)
# F_FLAT_7 = Note("F-1", 7)
# G_SHARP_7 = Note("G+1", 7)
# G_FLAT_7 = Note("G-1", 7)
# A_SHARP_7 = Note("A+1", 7)
# A_FLAT_7 = Note("A-1", 7)
# B_SHARP_7 = Note("B+1", 7)
# B_FLAT_7 = Note("B-1", 7)
# C_DOUBLE_SHARP_7 = Note("C+2", 7)
# C_DOUBLE_FLAT_7 = Note("C-2", 7)
# D_DOUBLE_SHARP_7 = Note("D+2", 7)
# D_DOUBLE_FLAT_7 = Note("D-2", 7)
# E_DOUBLE_SHARP_7 = Note("E+2", 7)
# E_DOUBLE_FLAT_7 = Note("E-2", 7)
# F_DOUBLE_SHARP_7 = Note("F+2", 7)
# F_DOUBLE_FLAT_7 = Note("F-2", 7)
# G_DOUBLE_SHARP_7 = Note("G+2", 7)
# G_DOUBLE_FLAT_7 = Note("G-2", 7)
# A_DOUBLE_SHARP_7 = Note("A+2", 7)
# A_DOUBLE_FLAT_7 = Note("A-2", 7)
# B_DOUBLE_SHARP_7 = Note("B+2", 7)
# C_8 = Note("C", 8)
# D_8 = Note("D", 8)
# E_8 = Note("E", 8)
# F_8 = Note("F", 8)
# G_8 = Note("G", 8)
# A_8 = Note("A", 8)
# B_8 = Note("B", 8)
# C_SHARP_8 = Note("C+1", 8)
# C_FLAT_8 = Note("C-1", 8)
# D_SHARP_8 = Note("D+1", 8)
# D_FLAT_8 = Note("D-1", 8)
# E_SHARP_8 = Note("E+1", 8)
# E_FLAT_8 = Note("E-1", 8)
# F_SHARP_8 = Note("F+1", 8)
# F_FLAT_8 = Note("F-1", 8)
# G_SHARP_8 = Note("G+1", 8)
# G_FLAT_8 = Note("G-1", 8)
# A_SHARP_8 = Note("A+1", 8)
# A_FLAT_8 = Note("A-1", 8)
# B_SHARP_8 = Note("B+1", 8)
# B_FLAT_8 = Note("B-1", 8)
# C_DOUBLE_SHARP_8 = Note("C+2", 8)
# C_DOUBLE_FLAT_8 = Note("C-2", 8)
# D_DOUBLE_SHARP_8 = Note("D+2", 8)
# D_DOUBLE_FLAT_8 = Note("D-2", 8)
# E_DOUBLE_SHARP_8 = Note("E+2", 8)
# E_DOUBLE_FLAT_8 = Note("E-2", 8)
# F_DOUBLE_SHARP_8 = Note("F+2", 8)
# F_DOUBLE_FLAT_8 = Note("F-2", 8)
# G_DOUBLE_SHARP_8 = Note("G+2", 8)
# G_DOUBLE_FLAT_8 = Note("G-2", 8)
# A_DOUBLE_SHARP_8 = Note("A+2", 8)
# A_DOUBLE_FLAT_8 = Note("A-2", 8)
# B_DOUBLE_SHARP_8 = Note("B+2", 8)
# C_9 = Note("C", 9)
# D_9 = Note("D", 9)
# E_9 = Note("E", 9)
# F_9 = Note("F", 9)
# G_9 = Note("G", 9)
# A_9 = Note("A", 9)
# B_9 = Note("B", 9)
# C_SHARP_9 = Note("C+1", 9)
# C_FLAT_9 = Note("C-1", 9)
# D_SHARP_9 = Note("D+1", 9)
# D_FLAT_9 = Note("D-1", 9)
# E_SHARP_9 = Note("E+1", 9)
# E_FLAT_9 = Note("E-1", 9)
# F_SHARP_9 = Note("F+1", 9)
# F_FLAT_9 = Note("F-1", 9)
# G_SHARP_9 = Note("G+1", 9)
# G_FLAT_9 = Note("G-1", 9)
# A_SHARP_9 = Note("A+1", 9)
# A_FLAT_9 = Note("A-1", 9)
# B_SHARP_9 = Note("B+1", 9)
# B_FLAT_9 = Note("B-1", 9)
# C_DOUBLE_SHARP_9 = Note("C+2", 9)
# C_DOUBLE_FLAT_9 = Note("C-2", 9)
# D_DOUBLE_SHARP_9 = Note("D+2", 9)
# D_DOUBLE_FLAT_9 = Note("D-2", 9)
# E_DOUBLE_SHARP_9 = Note("E+2", 9)
# E_DOUBLE_FLAT_9 = Note("E-2", 9)
# F_DOUBLE_SHARP_9 = Note("F+2", 9)
# F_DOUBLE_FLAT_9 = Note("F-2", 9)
# G_DOUBLE_SHARP_9 = Note("G+2", 9)
# G_DOUBLE_FLAT_9 = Note("G-2", 9)
# A_DOUBLE_SHARP_9 = Note("A+2", 9)
# A_DOUBLE_FLAT_9 = Note("A-2", 9)
# B_DOUBLE_SHARP_9 = Note("B+2", 9)
# C_10 = Note("C", 10)
# D_10 = Note("D", 10)
# E_10 = Note("E", 10)
# F_10 = Note("F", 10)
# G_10 = Note("G", 10)
# A_10 = Note("A", 10)
# B_10 = Note("B", 10)
# C_SHARP_10 = Note("C+1", 10)
# C_FLAT_10 = Note("C-1", 10)
# D_SHARP_10 = Note("D+1", 10)
# D_FLAT_10 = Note("D-1", 10)
# E_SHARP_10 = Note("E+1", 10)
# E_FLAT_10 = Note("E-1", 10)
# F_SHARP_10 = Note("F+1", 10)
# F_FLAT_10 = Note("F-1", 10)
# G_SHARP_10 = Note("G+1", 10)
# G_FLAT_10 = Note("G-1", 10)
# A_SHARP_10 = Note("A+1", 10)
# A_FLAT_10 = Note("A-1", 10)
# B_SHARP_10 = Note("B+1", 10)
# B_FLAT_10 = Note("B-1", 10)
# C_DOUBLE_SHARP_10 = Note("C+2", 10)
# C_DOUBLE_FLAT_10 = Note("C-2", 10)
# D_DOUBLE_SHARP_10 = Note("D+2", 10)
# D_DOUBLE_FLAT_10 = Note("D-2", 10)
# E_DOUBLE_SHARP_10 = Note("E+2", 10)
# E_DOUBLE_FLAT_10 = Note("E-2", 10)
# F_DOUBLE_SHARP_10 = Note("F+2", 10)
# F_DOUBLE_FLAT_10 = Note("F-2", 10)
# G_DOUBLE_SHARP_10 = Note("G+2", 10)
# G_DOUBLE_FLAT_10 = Note("G-2", 10)
# A_DOUBLE_SHARP_10 = Note("A+2", 10)
# A_DOUBLE_FLAT_10 = Note("A-2", 10)
# B_DOUBLE_SHARP_10 = Note("B+2", 10)
