"""json"""
__author__ = '赵传真'

import json

d = dict(name='Bob', age=28, score=98)

print(json.dumps(d))
str = '{"name": "Bob", "age": 28, "score": 98}'
print(json.loads(str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('陈独秀', 28, 99)
print(json.dumps(s, default=lambda obj: obj.__dict__))


def str2student(self):
    return Student(self['name'], self['age'], self['score'])


str2 = "{\"name\": \"\u9648\u72ec\u79c0\", \"age\": 28, \"score\": 99}"
print(json.loads(str, object_hook=str2student))

print(('==============练习题===================='))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
