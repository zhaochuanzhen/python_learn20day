"""操作目录"""
import os

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('HOME'))
print(os.path.abspath("."))
# os.mkdir(os.path.join(os.path.abspath("."), 'testdir'))
# os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))
print(os.path.split(os.path.abspath('.')))
