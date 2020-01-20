import os
import time
from multiprocessing import Pool


def foo(s):
    print('Run task %s (%s)...' % (s, os.getpid()))
    time.sleep(0.5)


if __name__ == '__main__':
    print('main进程开始 :', os.getpid())
    t = Pool(4)
    for i in range(5):
        t.apply_async(foo, args=(i,))
    print('等待所有进程结束')
    t.close()
    t.join()
    print('所有进程已结束')
