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


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


f = fib(10)
for i in f:
    print(i)

print('=============杨辉三角=================')


def yanghui():
    a = [1]
    while True:
        yield a
        a = [1] + [a[i] + a[i + 1] for i in range(len(a) - 1)] + [1]


y = yanghui()
n = 0
for i in y:
    print(i)
    n += 1
    if n > 10:
        break
