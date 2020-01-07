"""类和实例"""
__author__ = '赵传真'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %d' % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return 'A'
        if self.score > 80:
            return 'B'
        if self.score > 70:
            return 'C'
        else:
            return 'D'


bart = Student('Welims Bart', 98)
bart.print_score()
print(bart.get_grade())
