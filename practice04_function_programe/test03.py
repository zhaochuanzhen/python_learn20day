# 练习题
# 素数
print('==============素数==============')


def f1():
    n = 3
    while True:
        yield n
        n += 2


def f2(n):
    return lambda x: x % n > 0


def f3():
    yield 2
    it = f1()
    while True:
        n = next(it)
        yield n
        it = filter(f2(n), it)


g1 = f3()
for i in range(10):
    print(next(g1))

# 回数
print('=================回数================')


def f4(n):
    s = str(n)
    return s == s[::-1]


print(list(filter(f4, range(100))))
