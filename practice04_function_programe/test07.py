"""
desc: 装饰器
author: 赵传真
date: 2020年1月6日15:25:53
"""

# !/usr/bin/env python3
# -*- encoding: UTF-8 -*-

import time
import functools


def log(text):
    def f1(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('进入函数 %s(), 提示语：%s' % (func.__name__, text))
            return func(*args, **kw)

        return wrapper

    return f1


@log('你好世界')
def now():
    print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))


now()
print(now.__name__)
