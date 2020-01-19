"""异常捕获"""
__author__ = '赵传真'

import logging

try:
    a = 10 / 0
    print(111)
except ZeroDivisionError as e:
    logging.exception(e)
finally:
    print("finish")
