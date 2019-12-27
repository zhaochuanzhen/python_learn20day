"""
desc: 递归函数
author: 赵传真
date: 2019年12月27日11:25:35
"""


# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

# 尾递归方式
def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, num * product)


def fact(n):
    return fact_iter(n, 1)


print(fact(10))

# 汉诺塔
print('=================汉诺塔====================')


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
