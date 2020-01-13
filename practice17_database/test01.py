"""数据库操作"""
__ahthor__ = '赵传真'

import MySQLdb

db = MySQLdb.connect("localhost", "root", ".", "sys", charset='utf8')
cursor = db.cursor()
cursor.execute("select * from user")
data = cursor.fetchall()
print(data)
db.close()
