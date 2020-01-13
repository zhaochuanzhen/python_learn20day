"""StringIO ByteIO"""
__author__ = '赵传真'

from io import StringIO, BytesIO

f1 = StringIO()
f1.write('hello')
f1.write(' ')
f1.write('world')

print(f1.getvalue())

f2 = StringIO("hello\nworld.")
print(f2.getvalue())

f3 = BytesIO("你好 世界".encode('utf-8'))
print(f3.getvalue())
