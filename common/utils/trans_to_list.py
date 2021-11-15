#!/usr/bin/env python
# @Time    : 2021/11/14 3:37 下午
# @Author  : guo2018@88.com

def execute(the_input_str: str):
    prime_list = the_input_str.split(",")

    def float_or_int(input_value: str):
        try:
            if len(input_value) == 0:
                return None
            if input_value.find(".") != -1:
                return float(input_value)
            if input_value.isdigit():
                return int(input_value)
            return input_value
        except:
            return input_value

    ready_list = []
    for i in prime_list:
        ready_list.append(float_or_int(i))
    return ready_list


if __name__ == '__main__':
    a = "1.2,2,3,4,1.%,0,"
    b = execute(a)
    print(b)
