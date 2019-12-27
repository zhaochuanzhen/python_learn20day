"""
desc: 迭代
author: 赵传真
date: 2019年12月27日15:07:16
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}
for item in d:
    print(item, d[item])

for k, v in d.items():
    print(k, v)

for v in d.values():
    print(v)

for k in d.keys():
    print(k)

for i, k in enumerate(d):
    print(i, k)

# ===========练习题==============
print('============练习题==============')


def findMinAndMax(l):
    # if not isinstance(l, Iterator):
    #     raise TypeError('类型错误')
    min_value = l[0]
    max_value = l[0]
    for key in l:
        if min_value > key:
            min_value = key
        if max_value < key:
            max_value = key
    return min_value, max_value


print(findMinAndMax([7, 1, 3, 9, 5]))
