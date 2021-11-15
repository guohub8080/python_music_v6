#!/usr/bin/env python
# @Time    : 2021/11/12 2:27 下午
# @Author  : guo2018@88.com

# 三和弦：
import pandas

maj3 = "maj3"
min3 = "min3"
aug3 = "aug3"
dim3 = "dim3"

# 七和弦：
maj7 = "maj7"
min7 = "min7"
dom7 = "dom7"
mm7 = "mm7"
aug_maj7 = "aug_maj7"
aug_min7 = "aug_min7"
half_dim7 = "half_dim7"
#
from pandas import read_excel
the_excel=pandas.array(read_excel("chord_meta.xlsx"))
# print(a)
print(the_excel)
# print(the_excel.columns)
# print(a.columns)
# for i in range(the_excel.shape[0]):
#     print(the_excel.index(i))

# print(dir(the_excel))
c="1,2,3"
print(c.split(","))
