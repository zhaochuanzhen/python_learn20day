"""
desc: if elif else
version: 1.0
date: 2019年12月26日14:38:37
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
if age >= 18:
    print('your age is %d' % age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

if 2:
    print(0)
else:
    print(1)

# birth = input('birth: ')
# if int(birth) > 2000:
#     print('00后')
# else:
#     print('00前')

# =============练习题==============
height = 1.70
weight = 60
bmi = weight / (height ** 2)
print(bmi)
if bmi <= 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
