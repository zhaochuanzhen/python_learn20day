"""
desc: 列表生成器
author: 赵传真
date: 2019年12月27日16:03:40
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-
import os

print(list(range(1, 11)))

l1 = [x + 2 for x in range(1, 11)]
print(l1)

print([d for d in range(1, 11) if d % 2 == 0])

print([m + n for m in 'ABC' for n in 'DEF'])

print([d for d in os.listdir('/')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

print([s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']])

# ===========练习题==============
print('============练习题==============')

l3 = ['Hello', 'World', 18, 'Apple', None]
l4 = [s.lower() for s in l3 if isinstance(s, str)]
print(l4)
