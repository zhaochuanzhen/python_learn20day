"""@property的使用"""
__author__ = '赵传真'


class Student(object):
    __slots__ = ('name', 'score')

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('成绩必须是int类型')
        elif score < 0 or score > 100:
            raise ValueError('成绩必须在0--100之间')
        self.score = score

    def get_score(self):
        return self.score

    def print_student(self):
        print('%s : %d' % (self.name, self.score))


bob = Student()
bob.name = 'Bob'
bob.set_score(98)
bob.print_student()


