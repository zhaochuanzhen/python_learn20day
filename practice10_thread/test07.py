import threading
import time


def loop():
    print('子线程启动 :', threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread ', threading.current_thread().name, ':', n)
        time.sleep(0.5)
    print('子线程结束 :', threading.current_thread().name)


if __name__ == '__main__':
    print(threading.current_thread().name, '开始')
    t = threading.Thread(target=loop, name='Loop')
    t.start()
    # t.join()
    print(threading.current_thread().name, '结束')
