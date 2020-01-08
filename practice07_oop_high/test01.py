"""__slots__的使用"""
__author__ = '赵传真'


class Student(object):
    __slots__ = ('name', 'socre')


bob = Student()
bob.name = 'Bob'
print(bob.name)
