"""
desc: 函数
author: 赵传真
date: 2019年12月26日17:03:16
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from my_func import my_abs, quadratic

print(abs(-12.34))

print(max(1, 2, 44, 5))

print(int('123'))
print(float('123.12'))
print(int(float('123.12')))
print(bool(55))

a = abs
print(a(-22))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

# ===================自定义函数======================
print("=====================自定义函数=======================")

print(my_abs(-32.66))

print(isinstance(11, str))

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
