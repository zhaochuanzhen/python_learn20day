"""getattr"""
__author__ = '赵传真'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 99
        raise AttributeError('没有找到该属性 %s' % item)


bob = Student('Bob')
print(bob.name)
print(bob.score)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users.repos)
