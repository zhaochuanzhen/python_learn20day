"""插入数据"""
__author__ = '赵传真'

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='.',
    database='sys',
    charset='utf8'
)

cursor = db.cursor()
cursor.execute('insert into user (name, age) values (%s, %s)', ('陈独秀', 28))
db.commit()
cursor.close()
db.close()
