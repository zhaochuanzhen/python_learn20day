"""
desc: 装饰器
author: 赵传真
date: 2020年1月6日15:25:53
"""


# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2019-12-12')


f = now

print(now.__name__)
print(f.__name__)
f()

print('=====================================')
