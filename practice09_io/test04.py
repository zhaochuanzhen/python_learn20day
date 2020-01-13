"""序列化"""
__author__ = '赵传真'
import pickle

# d = dict(name='Bob', age=20, score=80)
# print(d)
# print(pickle.dumps(d))
# f1 = open('dump.txt', 'wb')
# pickle.dump(d, f1)
# f1.close()

f2 = open('dump.txt', 'rb')
d = pickle.load(f2)
f2.close()
print(d)
