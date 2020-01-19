import logging

logging.basicConfig(level=logging.DEBUG)


def foo(s):
    try:
        n = int(s)
        return 10 / n
    except ValueError as e:
        logging.debug('s不能为0')


print(foo('0'))
