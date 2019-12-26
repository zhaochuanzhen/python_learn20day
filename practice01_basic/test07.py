"""
desc: dict set
version: 1.0
date: 2019年12月26日14:38:37
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

print('=======dict========')


def foreach(dic):
    for (k, v) in dic.items():
        print(k + "=" + str(v))


a = {'Bob': 95, 'Tom': 88, "李大钊": 96, "陈独秀": 99}
print(a)
foreach(a)

print('===============')

a['李时珍'] = 99
foreach(a)

print('李大钊' in a)
print(a.get('李大钊s', -1))

print('=======set========')

s = {1, 2, 3, 6, 4}
print(s)
s.add(4)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 | s2)

t1 = (1, 2, 3)
s.add(t1)
print(s)
