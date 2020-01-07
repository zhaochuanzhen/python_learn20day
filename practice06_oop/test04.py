"""继承和多态"""
__author__ = '赵传真'


class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    def run(self):
        print('dog is running')


class Cat(Animal):
    def run(self):
        print('cat is running')


dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run(a):
    a.run()


run(Dog())

print(dir(Dog()))
print('===============类属性和实例属性===============')


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
