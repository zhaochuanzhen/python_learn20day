"""
desc: map/reduce
author: 赵传真
date: 2020/01/04
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from functools import reduce

print('==================map===============')
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f1(num):
    return num ** 2


m1 = map(f1, l1)
print(tuple(m1))


def f2(num):
    return str(num)


m2 = map(f2, l1)
print(tuple(m2))

print('================reduce=================')


def f3(x, y):
    return x + y


r1 = reduce(f3, l1)
print(r1)
print(sum(l1))


def f4(x, y):
    return x * 10 + y


r2 = reduce(f4, l1)
print(r2)


def f5(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


s1 = '123456758'
r3 = reduce(f4, map(f5, s1))
print(r3)


def str2int(s):
    def f6(x, y):
        return x * 10 + y

    def f7(k):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[k]

    return reduce(f6, map(f7, s))


print(str2int('89485984589'))


def f8(s):
    def f9(k):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[k]

    return reduce(lambda x, y: x * 10 + y, map(f9, s))


print(f8('99484883'))

print('=================练习题===================')

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
l2 = ['adam', 'LISA', 'barT']


def f10(s):
    return s.capitalize()


print(list(map(f10, l2)))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l):
    return reduce(lambda x, y: x * y, l)


l3 = [1, 3, 5, 7, 9]

print(prod(l3))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def f11(s):
    def f12(k):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[k]

    index = s.index('.')
    s = s.replace('.', '')
    n = reduce(lambda x, y: x * 10 + y, map(f12, s))
    return n / (10 ** index)


s1 = '123.456'
print(f11(s1))
