"""getitem"""
__author__ = '赵传真'


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if step is None:
                step = 1
            if start is None:
                start = 0
            a, b, c = 1, 1, 1
            L = []
            for x in range(stop):
                if x >= start and c % step == 0:
                    L.append(a)
                a, b, c = b, a + b, c + 1
            return L


f = Fib()
print(f[10])
print(f[1:10])
print(f[1:10:2])
