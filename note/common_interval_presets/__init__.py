#!/usr/bin/env python
# @Time    : 2021/8/22 11:12 上午
# @Author  : guo2018@88.com
from note import Note


# =============================    概   述    ============================= #
# 这是预置的音程类，实例化的时候需要接受一个Note类。
# inverse_query是指反向查询，例如C的上行纯五度就是G，这是正向查询。反向查询是指谁的上行纯五度是C，答案是F。
# 但是反向查询并不是使用传统的乐理转位方法来做到的，即「不是」使用5+4=9然后反向找C的上行纯四度来反推C的下行纯五度。
# 之所以这样做，是因为考虑到了上述乐理方法并没有把八度范围也考虑进去。
# 因为第5个八度的C的上行纯五度是第5个八度的G，而下行纯五度是「第4个八度」的F。
#
# =============================    术   语   ============================= #
# 以下为作者随心所欲的预设。
# P ：纯，例如P1表示纯1度，P5表示纯五度。
# M ：大，例如M2表示大二度，M3表示大三度。
# m ：小，例如m6表示小6度，m7表示小7度。
# AUG ：增，例如AUG4表示增四度，因为是增大的趋势，所以我使用了大写字母。同时因为增音程并非常用，所以增加字母长度以区分常用。
# dim ：减，同上。
# 倍增倍减不在预设范围内，想用就用自带的get_note_by_interval方法好了。
#
# =============================   方  法  论   ============================= #
# 1. Note实例通过@property属性把interval这个命名空间占用上；
# 2. interval实际上是import了一个Common_Interval类，并且将其实例化①，传入的参数为Note的实例②以及inverse_query③。
# 3. ①再用自己的@property实现了同一个命名空间下的多个结果，例如同样都是interval.P5，由于①的不同而实现了不同的效果。
# 3.1 解释：例如如果①在实例化的时候传入的②是C_5，那么Note("C").interval.P5是一个G_5，如果②是其他的音符，虽然都调用了interval.P5，但是结果不同。
# 4. ③为布尔值，如果是默认是TRUE，即上行查询，如果是FALSE，那么是下行查询。
# 5. 每个@property后面加了一句「 # type:()-> Note 」的目的纯属为了PyCharm可以提示，以实现连续调用。
# 5.1 连续调用的基础是因为return了一个新的Note的实例。
#
# =============================    一   览   ============================= #
# 根据「一四五八无大小，二三六七没有纯」的口诀，同样地，9、10度也没有纯，表格如下方便检查：
#     [ 1 ]       2      3      [ 4 ]     [ 5 ]      6      7
#     [ 8 ]       9      10    [ 11 ]    [ 12 ]     13      14
#    [ 15 ]      16      17    [ 18 ]    [ 19 ]     20      21


class Common_Interval(object):

    def __init__(self, origin_note_instance, inverse_query=False):
        self.origin_note_instance = origin_note_instance
        self.inverse_query = inverse_query

    def __str__(self):
        return "[ WARNING ] 调用不全，请补充语句以继续调用，如「.P5」，当前返回None..."

    # ======================================================================== #
    # =============================    1   度    ============================= #
    # ======================================================================== #
    # 纯1度
    @property
    def P1(self):
        # type:()-> Note
        return self.origin_note_instance

    # 增1度
    @property
    def AUG1(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 1, "下")
        return self.origin_note_instance.get_note_by_interval("增", 1)

    # ======================================================================== #
    # =============================    2   度    ============================= #
    # ======================================================================== #
    # 大2度
    @property
    def M2(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 2, "下")
        return self.origin_note_instance.get_note_by_interval("大", 2)

    # 小2度
    @property
    def m2(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 2, "下")
        return self.origin_note_instance.get_note_by_interval("小", 2)

    # 增2度
    @property
    def AUG2(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 2, "下")
        return self.origin_note_instance.get_note_by_interval("增", 2)

    # 减2度
    @property
    def dim2(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 2, "下")
        return self.origin_note_instance.get_note_by_interval("减", 2)

    # ======================================================================== #
    # =============================    3   度    ============================= #
    # ======================================================================== #
    # 大3度
    @property
    def M3(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 3, "下")
        return self.origin_note_instance.get_note_by_interval("大", 3)

    # 小3度
    @property
    def m3(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 3, "下")
        return self.origin_note_instance.get_note_by_interval("小", 3)

    # 增3度
    @property
    def AUG3(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 3, "下")
        return self.origin_note_instance.get_note_by_interval("增", 3)

    # 减3度
    @property
    def dim3(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 3, "下")
        return self.origin_note_instance.get_note_by_interval("减", 3)

    # ======================================================================== #
    # =============================    4   度    ============================= #
    # ======================================================================== #
    # 纯4度
    @property
    def P4(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 4, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 4)

    # 增4度
    @property
    def AUG4(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 4, "下")
        return self.origin_note_instance.get_note_by_interval("增", 4)

    # 减4度
    @property
    def dim4(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 4, "下")
        return self.origin_note_instance.get_note_by_interval("减", 4)

    # ======================================================================== #
    # =============================    5   度    ============================= #
    # ======================================================================== #
    # 纯5度
    @property
    def P5(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 5, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 5)

    # 增5度
    @property
    def AUG5(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 5, "下")
        return self.origin_note_instance.get_note_by_interval("增", 5)

    # 减5度
    @property
    def dim5(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 5, "下")
        return self.origin_note_instance.get_note_by_interval("减", 5)

    # ======================================================================== #
    # =============================    6   度    ============================= #
    # ======================================================================== #
    # 大6度
    @property
    def M6(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 6, "下")
        return self.origin_note_instance.get_note_by_interval("大", 6)

    # 小6度
    @property
    def m6(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 6, "下")
        return self.origin_note_instance.get_note_by_interval("小", 6)

    # 增6度
    @property
    def AUG6(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 6, "下")
        return self.origin_note_instance.get_note_by_interval("增", 6)

    # 减6度
    @property
    def dim6(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 6, "下")
        return self.origin_note_instance.get_note_by_interval("减", 6)

    # ======================================================================== #
    # =============================    7   度    ============================= #
    # ======================================================================== #
    # 大7度
    @property
    def M7(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 7, "下")
        return self.origin_note_instance.get_note_by_interval("大", 7)

    # 小7度
    @property
    def m7(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 7, "下")
        return self.origin_note_instance.get_note_by_interval("小", 7)

    # 增7度
    @property
    def AUG7(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 7, "下")
        return self.origin_note_instance.get_note_by_interval("增", 7)

    # 减7度
    @property
    def dim7(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 7, "下")
        return self.origin_note_instance.get_note_by_interval("减", 7)

    # ======================================================================== #
    # =============================    8   度    ============================= #
    # ======================================================================== #
    # 纯8度
    @property
    def P8(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 8, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 8)

    # 增8度
    @property
    def AUG8(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 8, "下")
        return self.origin_note_instance.get_note_by_interval("增", 8)

    # 减8度
    @property
    def dim8(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 8, "下")
        return self.origin_note_instance.get_note_by_interval("减", 8)

    # ======================================================================== #
    # =============================    9   度    ============================= #
    # ======================================================================== #
    # 大9度
    @property
    def M9(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 9, "下")
        return self.origin_note_instance.get_note_by_interval("大", 9)

    # 小9度
    @property
    def m9(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 9, "下")
        return self.origin_note_instance.get_note_by_interval("小", 9)

    # 增9度
    @property
    def AUG9(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 9, "下")
        return self.origin_note_instance.get_note_by_interval("增", 9)

    # 减9度
    @property
    def dim9(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 9, "下")
        return self.origin_note_instance.get_note_by_interval("减", 9)

    # ======================================================================== #
    # =============================    10   度    ============================= #
    # ======================================================================== #

    # 大10度
    @property
    def M10(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 10, "下")
        return self.origin_note_instance.get_note_by_interval("大", 10)

    # 小10度
    @property
    def m10(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 10, "下")
        return self.origin_note_instance.get_note_by_interval("小", 10)

    # 增10度
    @property
    def AUG10(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 10, "下")
        return self.origin_note_instance.get_note_by_interval("增", 10)

    # 减10度
    @property
    def dim10(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 10, "下")
        return self.origin_note_instance.get_note_by_interval("减", 10)

    # ======================================================================== #
    # =============================    11   度    ============================= #
    # ======================================================================== #
    # 纯11度
    @property
    def P11(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 11, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 11)

    # 增11度
    @property
    def AUG11(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 11, "下")
        return self.origin_note_instance.get_note_by_interval("增", 11)

    # 减11度
    @property
    def dim11(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 11, "下")
        return self.origin_note_instance.get_note_by_interval("减", 11)

    # ======================================================================== #
    # =============================    12   度    ============================= #
    # ======================================================================== #
    # 纯12度
    @property
    def P12(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 12, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 12)

    # 增12度
    @property
    def AUG12(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 12, "下")
        return self.origin_note_instance.get_note_by_interval("增", 12)

    # 减12度
    @property
    def dim12(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 12, "下")
        return self.origin_note_instance.get_note_by_interval("减", 12)

    # ======================================================================== #
    # =============================    13   度    ============================= #
    # ======================================================================== #
    # 大13度
    @property
    def M13(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 13, "下")
        return self.origin_note_instance.get_note_by_interval("大", 13)

    # 小13度
    @property
    def m13(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 13, "下")
        return self.origin_note_instance.get_note_by_interval("小", 13)

    # 增13度
    @property
    def AUG13(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 13, "下")
        return self.origin_note_instance.get_note_by_interval("增", 13)

    # 减13度
    @property
    def dim13(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 13, "下")
        return self.origin_note_instance.get_note_by_interval("减", 13)

    # ======================================================================== #
    # =============================    14   度    ============================= #
    # ======================================================================== #
    # 大14度
    @property
    def M14(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 14, "下")
        return self.origin_note_instance.get_note_by_interval("大", 14)

    # 小14度
    @property
    def m14(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 14, "下")
        return self.origin_note_instance.get_note_by_interval("小", 14)

    # 增14度
    @property
    def AUG14(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 14, "下")
        return self.origin_note_instance.get_note_by_interval("增", 14)

    # 减14度
    @property
    def dim14(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 14, "下")
        return self.origin_note_instance.get_note_by_interval("减", 14)

    # ======================================================================== #
    # =============================    15   度    ============================= #
    # ======================================================================== #
    # 纯15度
    @property
    def P15(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 15, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 15)

    # 增15度
    @property
    def AUG15(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 15, "下")
        return self.origin_note_instance.get_note_by_interval("增", 15)

    # 减15度
    @property
    def dim15(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 15, "下")
        return self.origin_note_instance.get_note_by_interval("减", 15)

    # ======================================================================== #
    # =============================    18   度    ============================= #
    # ======================================================================== #
    # 纯18度
    @property
    def P18(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 18, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 18)

    # 增18度
    @property
    def AUG18(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 18, "下")
        return self.origin_note_instance.get_note_by_interval("增", 18)

    # 减18度
    @property
    def dim18(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 18, "下")
        return self.origin_note_instance.get_note_by_interval("减", 18)

    # ======================================================================== #
    # =============================    19   度    ============================= #
    # ======================================================================== #
    # 纯19度
    @property
    def P19(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("纯", 19, "下")
        return self.origin_note_instance.get_note_by_interval("纯", 19)

    # 增19度
    @property
    def AUG19(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 19, "下")
        return self.origin_note_instance.get_note_by_interval("增", 19)

    # 减19度
    @property
    def dim19(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 19, "下")
        return self.origin_note_instance.get_note_by_interval("减", 19)

    # ======================================================================== #
    # =============================    16   度    ============================= #
    # ======================================================================== #
    # 大16度
    @property
    def M16(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 16, "下")
        return self.origin_note_instance.get_note_by_interval("大", 16)

    # 小16度
    @property
    def m16(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 16, "下")
        return self.origin_note_instance.get_note_by_interval("小", 16)

    # 增16度
    @property
    def AUG16(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 16, "下")
        return self.origin_note_instance.get_note_by_interval("增", 16)

    # 减16度
    @property
    def dim16(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 16, "下")
        return self.origin_note_instance.get_note_by_interval("减", 16)

    # ======================================================================== #
    # =============================    17   度    ============================= #
    # ======================================================================== #
    # 大17度
    @property
    def M17(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 17, "下")
        return self.origin_note_instance.get_note_by_interval("大", 17)

    # 小17度
    @property
    def m17(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 17, "下")
        return self.origin_note_instance.get_note_by_interval("小", 17)

    # 增17度
    @property
    def AUG17(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 17, "下")
        return self.origin_note_instance.get_note_by_interval("增", 17)

    # 减17度
    @property
    def dim17(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 17, "下")
        return self.origin_note_instance.get_note_by_interval("减", 17)

    # ======================================================================== #
    # =============================    20   度    ============================= #
    # ======================================================================== #
    # 大20度
    @property
    def M20(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 20, "下")
        return self.origin_note_instance.get_note_by_interval("大", 20)

    # 小20度
    @property
    def m20(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 20, "下")
        return self.origin_note_instance.get_note_by_interval("小", 20)

    # 增20度
    @property
    def AUG20(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 20, "下")
        return self.origin_note_instance.get_note_by_interval("增", 20)

    # 减20度
    @property
    def dim20(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 20, "下")
        return self.origin_note_instance.get_note_by_interval("减", 20)

    # ======================================================================== #
    # =============================    21   度    ============================= #
    # ======================================================================== #
    # 大21度
    @property
    def M21(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("大", 21, "下")
        return self.origin_note_instance.get_note_by_interval("大", 21)

    # 小21度
    @property
    def m21(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("小", 21, "下")
        return self.origin_note_instance.get_note_by_interval("小", 21)

    # 增21度
    @property
    def AUG21(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("增", 21, "下")
        return self.origin_note_instance.get_note_by_interval("增", 21)

    # 减21度
    @property
    def dim21(self):
        # type:()-> Note
        if self.inverse_query:
            return self.origin_note_instance.get_note_by_interval("减", 21, "下")
        return self.origin_note_instance.get_note_by_interval("减", 21)
