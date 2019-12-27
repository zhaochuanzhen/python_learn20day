"""
desc: 切片
author: 赵传真
date: 2019年12月27日14:50:16
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

person = ['陈独秀', '李时珍', 'Tom']
print(person)
print(person[0:2])
print(person[:2])
print(person[1:2])
print(person[-1:])

# =======灵活切分=========
print('=============灵活切分===============')
r = list(range(100))
print(r[:])
print(r[11:20])
print(r[0:10:2])
print(r[90:])
print(r[20::10])

# ========tuple========
print('=============tuple===============')

t = tuple(range(100))
print(t[:])
print(t[11:20])
print(t[0:10:2])
print(t[90:])
print(t[20::10])

# ========字符串切分========
print('=============字符串切分===============')

s = 'alakdsglkreoi'
print(s[0:5])
print(s[5:])

# ========练习题========
print('=============练习题===============')


def trim(s):
    return s.strip()


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
