#!/usr/bin/env python
# @Time    : 2021/11/7 9:55 下午
# @Author  : guo2018@88.com
from datetime import date

a = date(2021, 12, 1)
b = date(2021, 2, 1)
c = a - b
print(c)

d = {1, 2}
d.add({1, 2})
d.add({2, 1})

print(d)
