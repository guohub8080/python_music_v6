#!/usr/bin/env python
# @Time    : 2021/11/3 4:03 下午
# @Author  : guo2018@88.com
from common.settings import BASE_DIR
from datetime import datetime

__now = datetime.now()
# 题目：
TITLE = f"GZT_{__now.strftime('%Y_%m_%d_%H%M%S')}"
# 作者：
COMPOSER = f"by GZT {__now.strftime('%Y年%m月%d日 - %I:%M %p')}"

# 输出位置：
RENDER_LOCATION = BASE_DIR.joinpath("produce_score").joinpath("render").joinpath(f"{__now.strftime('%Y')}").joinpath(
    f"{__now.strftime('%Y_%m')}").joinpath(f"{__now.strftime('%Y_%m_%d')}")

# 节拍：
TIME_SIGNATURE = "4/4"

# 速度：
BPM = 120
# 每个小节是几拍：
MEASURE_QUARTER_LENGTH = 4
# 一个作品是几小节：
MEASURES_NUM_PER_PART = 8

# 这个作品含有的所有节拍数和其概率：
POSSIBLE_BEATS_AND_WIGHT = [
    [0.25, 2],
    [0.5, 6],
    [1, 10],
    [2, 3],
    [1.5, 3],
    [4, 0.5]
]

if __name__ == '__main__':
    print(TITLE)
    print(COMPOSER)
