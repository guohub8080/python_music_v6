#!/usr/bin/env python
# @Time    : 2021/8/21 5:05 下午
# @Author  : guo2018@88.com
from pathlib import Path

# 根目录，即settings所在的文件夹
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# print(BASE_DIR)

# 数据库位置
DB = BASE_DIR.joinpath("common").joinpath("gzt_v6.sqlite3")

# SQLite位置
DB_SQL_LOCATION = "sqlite:///".__add__(str(DB))

# 中央C的位置
CENTER_C_LOCATION = 5

# midi输出时候的临时调整值
MIDI_RENDER_CALC_AJUST_OCTAVE = 0
MIDI_RENDER_CALC_AJUST_SEMITONE = 0


if __name__ == '__main__':
    print(BASE_DIR)
