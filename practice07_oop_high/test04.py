"""定制类"""
__author__ = '赵传真'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return 'Student(name:%s, score:%d)' % (self.name, self.score)

    __repr__ = __str__


bob = Student('Bob', 98)
print(bob)

print('====================iter=======================')


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a


for n in Fib():
    print(n)
