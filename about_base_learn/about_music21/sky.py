#!/usr/bin/env python
# @Time    : 2021/9/20 7:54 下午
# @Author  : guo2018@88.com

from music21 import corpus, converter, stream

b = converter.parse('Dream_of_Sky.mxl')
# b.show() # I've altered this so it's much shorter than it should be...
# b.measures(1, 5).show()


# print(b)

# for i in b:
#     if isinstance(i, stream.Stream):
#         print(i)
#         for ii in i:
#             if isinstance(ii,stream.Measure):
#                 print(ii)
#                 for iii in ii:
#                     print(iii)

print(b.analyze("key"))