"""
desc: filter
author: 赵传真
date: 2020/1/5
"""


# !/usr/bin/env python3
# -*-encoding: UTF-8 -*-

def f1(x):
    return x % 2 == 1


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(f1, l1)))


def f2(s):
    return s and s.strip()


l2 = ['1', '2', "", " ", 'a', 'ss', None]
print(list(filter(f2, l2)))


def f3(n):
    return lambda x: x % n > 0


print(list(filter(f3(3), [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print('====================生成素数=====================')


# 生成序列.生成器
def f4():
    n = 3
    while True:
        yield n
        n += 2


def f5():
    yield 2
    it = f4()
    while True:
        n = next(it)
        yield n
        it = filter(f3(n), it)


g1 = f5()
n = 0
while n < 30:
    n += 1
    print(next(g1))

print('==================练习题====================')


def f6(x):
    return str(x) == str(x)[::-1]


print(list(filter(f6, range(1, 1000))))
