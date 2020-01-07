"""面向对象编程"""
__author__ = '赵传真'
std1 = {'name': 'Bob', 'score': 98}
std2 = {'name': 'Tom', 'score': 81}


def print_score(std):
    print('%s : %d' % (std['name'], std['score']))


print_score(std1)
print_score(std2)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %d' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
bart.print_score()
