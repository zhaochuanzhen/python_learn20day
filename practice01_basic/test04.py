"""
desc: list and tuple
version: 1.0
date: 2019年12月26日14:38:37
"""


# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
def foreach(array):
    for item in array:
        print(item)


classmates = ['Bob', 'Tom', '李时珍', "陈独秀"]
print(classmates)
print(len(classmates))
foreach(classmates)
print(classmates[-4])
print('==================================')
classmates.append('李大钊')
foreach(classmates)
print('==================================')

s = ['python', True, ['asp', 'php'], 22.22]
foreach(s)

# tuple
print('=================tuple=================')
tuple_classmates = ('Bob', 'Tom', '李时珍', "陈独秀")
print(tuple_classmates)
print((1,))
