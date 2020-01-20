"""线程"""
__author__ = '赵传真'

from multiprocessing import Process
import os


def foo(s):
    print(s, " :", os.getpid())


if __name__ == '__main__':
    print('进入main线程 :', os.getpid())
    t = Process(target=foo, args=('test',))
    t.start()
    t.join()
    print('子线程开始')
