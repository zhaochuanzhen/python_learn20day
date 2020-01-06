"""
desc: 返回函数
author: 赵传真
date: 2020年1月6日14:59:01
"""


# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-


def f1(*args):
    def sum():
        num = 0
        for n in args:
            num += n
        return num

    return sum()


f = f1(1, 3, 5, 7, 9)
print(f)


def f2():
    fs = []

    def f4(j):
        def f5():
            return j ** 2

        return f5

    for i in range(1, 4):
        fs.append(f4(i))
    return fs


fp1, fp2, fp3 = f2()
print(fp1())
print(fp2())
print(fp3())
