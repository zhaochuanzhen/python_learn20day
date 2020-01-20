import threading
import time


def loop():
    print('子线程', threading.current_thread().name, '开始执行')
    for i in range(5):
        print(threading.current_thread().name, i)
        time.sleep(0.5)
    print('子线程', threading.current_thread().name, '执行结束')


if __name__ == '__main__':
    print(threading.current_thread().name, '线程开始执行')
    t = threading.Thread(target=loop, name='loop')
    t.start()
    t.join()
    print(threading.current_thread().name, '线程执行结束')
