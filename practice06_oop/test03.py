"""访问限制"""
__author__ = '赵传真'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name


bob = Student('Bob', 98)
print(bob.get_name())
bob.__name = 'Tom'
print(bob.__name)
print(bob.get_name())
