import os
import time
from multiprocessing import Pool


def foo(s):
    print(s, ' :', os.getpid())
    time.sleep(0.5)


if __name__ == '__main__':
    print('main进程 :', os.getpid())
    p = Pool(5)
    for i in range(6):
        p.apply_async(foo, args=(i,))
    p.close()
    print('等待子进程结束')
    p.join()
    print('子进程执行完毕')
