"""
desc: 位置参数、默认参数、可变参数、关键字参数、参数组合
author: 赵传真
date: 2019年12月27日10:16:44
"""


# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

def power(x, n=2):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误')
    while n > 1:
        x *= x
        n -= 1
    return x


print(power(5, 5))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


a = (1, 2)
print(calc(*a))


def person(name, **person):
    print("name : ", name, " other : ", person)


p = {"age": 22, "gender": "Man"}
person('陈独秀', **p)


def product(*x):
    sum = 1
    for n in x:
        sum *= n
    return sum


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
