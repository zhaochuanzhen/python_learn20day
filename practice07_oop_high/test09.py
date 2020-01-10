"""测试元类"""
__author__ = '赵传真'


def fn(self, name='world'):
    print('hello %s.' % name)


Hello = type("Hello", (object,), dict(hello=fn))

h = Hello()
h.hello('陈独秀')
