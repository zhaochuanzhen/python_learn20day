"""@property的使用"""
__author__ = '赵传真'


class Student(object):
    __slots__ = ('_name', '_age', '_score')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('成绩必须是int类型')
        elif score < 0 or score > 100:
            raise ValueError('成绩必须在0--100之间')
        self._score = score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def print_student(self):
        print('%s : %d' % (self._name, self._score))


bob = Student()
bob.name = 'Bob'
bob.score = 98
bob.print_student()

print('================练习题===================')


class Screen(object):
    __slots__ = ('_width', '_height', '_resolution')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._height * self._width


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
