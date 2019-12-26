"""
desc: for while
version: 1.0
date: 2019年12月26日14:38:37
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 0
for item in range(101):
    a += item
print(a)

b = ('Bob', 'Tom', 3.14, True)
for item in b:
    print(item)

c = 0
d = 100
while d > 0:
    c += d
    d = d - 1
print(c)

L = ['Bart', 'Lisa', 'Adam']
for item in L:
    print('Hello, %s' % item)

e = 0
while e <= 10:
    e += 1
    if e == 5:
        continue
    if e > 8:
        break
    print(e)

print('hi')
