# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
print("=============斐波拉契数列=============")


def fo():
    n, a, b = 0, 0, 1
    while True:
        yield b
        a, b = b, a + b
        n += 1


g1 = fo()
for i in g1:
    if i > 100:
        break
    print(i)

print("===============杨辉三角================")


def yanghui():
    n = 0
    a = [1]
    while True:
        yield a
        n = n + 1
        b = [0] + a
        c = a + [0]
        a = [b[i] + c[i] for i in range(n + 1)]


g2 = yanghui()
n = 0
for i in g2:
    if n > 10:
        break
    n += 1
    print(i)
