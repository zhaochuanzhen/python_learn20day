"""
desc: 生成器
author: 赵传真
date: 2019年12月27日16:26:40
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

g1 = (x ** 2 for x in range(1, 11))
for n in g1:
    print(n)

print('=============斐波拉契数列=================')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for g in fib(7):
    print(g)
