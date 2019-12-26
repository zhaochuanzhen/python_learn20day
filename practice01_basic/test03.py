"""
desc: 字符编码
version: 1.0
date: 2019年12月26日14:38:37
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
print(ord('赵'))
print(chr(25991))
print('\u4e2d\u6587')
print('中文')
print(b'ABD')
print('赵传真'.encode('utf-8'))
print(len('赵传真'.encode('utf-8')))
print(len(b'\xe8\xb5\xb5\xe4\xbc\xa0\xe7\x9c\x9f'))

# =============占位符格式化==============
print("Hello, %s, your score is %.2f" % ("赵传真", 98.99))
print('%2d-%03d' % (3, 1102))
print('%.2f' % 3.1415926)
# =============练习题==============
s1 = 72
s2 = 85
r = ((s2 - s1) / s1) * 100
print('小明的成绩提升了%.1f%%' % r)
