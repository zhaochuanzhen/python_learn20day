"""
desc: 匿名函数
author: 赵传真
date: 2020年1月6日15:00:18
"""
# !/usr/bin/env python
# -*- encoding: UTF-8 -*-
f1 = lambda x: x ** 2
print(f1(5))
# 匿名函数就是lambda表达式
print('====================练习题=======================')


def is_odd(n):
    return n % 2 == 1


l1 = list(filter(is_odd, range(1, 20)))
print(l1)

l2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(l2)
