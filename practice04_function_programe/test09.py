"""
desc: 偏函数
author: 赵传真
date: 2020年1月6日15:25:53
"""
import functools

print(int('123456'))
print(int('123456', base=8))
print(int('11001010101', 2))

int2 = functools.partial(int, base=2)

print(int2('1111'))
