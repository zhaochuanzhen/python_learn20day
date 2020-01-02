"""
desc: 高阶函数
author: 赵传真
date: 2020年1月2日11:30:30
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-
from functools import reduce


def test(a, b, f):
    return f(a) + f(b)


print(test(-4, 5, abs))

print("==================map/reduce=====================")


def f1(a):
    return a ** 2


m1 = map(f1, [1, 2, 3, 4, 5])
print(list(m1))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


def f1(x, y):
    return x * 10 + y


print(reduce(f1, [1, 2, 3, 4, 5, 6]))


def f2(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(f1, map(f2, '123456')))


def f3(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}

    def f31(x, y):
        return x * 10 + y

    def f32(s):
        return digits[s]

    return reduce(f31, map(f32, s))


print(f3('123456'))


def f4(s):
    return reduce(lambda x, y: x * 10 + y, map(f2, s))


print(f4('123456'))

print('=============练习题==============')


def f6(name):
    n = 0
    str = ''
    for i in name:
        if n == 0:
            str += i.upper()
        else:
            str += i
        n += 1
    return str


def f5(name):
    return f6(name.lower())


l1 = ['adam', 'LISA', 'barT']
print(list(map(f5, l1)))


def f7(l):
    def f6(x, y):
        return x * y

    return reduce(f6, l)


print('3 * 5 * 7 * 9 =', f7([3, 5, 7, 9]))


def str2float(s):
    return 1


print('str2float(\'123.456\') =', str2float('123.456'))
