"""
desc: 函数定义
author: 赵传真
date: 2019年12月27日09:39:15
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误，必须是int或float类型')
    if x >= 0:
        return x
    else:
        return -x


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("参数类型错误，必须是int或float类型")
    elif not isinstance(b, (int, float)):
        raise TypeError("参数类型错误，必须是int或float类型")
    elif not isinstance(c, (int, float)):
        raise TypeError("参数类型错误，必须是int或float类型")
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2
