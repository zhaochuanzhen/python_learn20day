"""文件读写"""
__author__ = '赵传真'

print('==============读取全部==================')
with open('./shuihu.txt', 'r') as f1:
    print(f1.read())

print('=================分行读取=====================')
with open('./shuihu.txt', 'r') as f2:
    for item in f2.readlines():
        print(item.strip())

print('===================按照size读取========================')
with open('./shuihu.txt', 'r') as f3:
    print(f3.read(30))

print('===============读取二进制文件===================')
with open('./shuihu.txt', 'rb') as f4:
    print(f4.read())

print('===================按照字符编码读取=======================')
with open('./shuihu.txt', 'r', encoding='utf-8', errors='ignore') as f5:
    print(f5.read())

print('==============写文件================')
with open('./shuihu.txt', 'a') as f6:
    f6.write('hello world.')
