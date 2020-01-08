"""枚举类"""
__author__ = '赵传真'

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Feb)
for name, member in Month.__members__.items():
    print(name, "==>", member, "==>", member.value)


@unique
class Weekday(Enum):
    Sub = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)
print(Weekday.Mon.value)
for name, member in Weekday.__members__.items():
    print(name, "=>", member, "==>", member.value)

print('======================练习题=========================')


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
print(bart.gender)
print(bart.gender.value)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
