"""
desc: sorted
author: 赵传真
date: 2020/01/05
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-
l1 = [36, 5, -12, 9, -21]
print(sorted(l1))
print(sorted(l1, key=abs))

l2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(l2))
print(sorted(l2, key=str.lower))

print(sorted(l2, key=str.lower, reverse=True))

print('==============练习题==============')

l3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def f1(t):
    return t[0].lower()


print(sorted(l3, key=f1))


def f2(t):
    return t[1]


print(sorted(l3, key=f2))
