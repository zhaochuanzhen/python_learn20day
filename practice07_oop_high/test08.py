"""元类学习"""
__author__ = '赵传真'

from myHello import Hello

h = Hello()
h.hello('赵传真')
print(type(h))
print(type(Hello))


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


l = MyList()
l.add(1)
print(l)
