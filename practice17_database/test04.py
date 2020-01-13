"""批量插入数据"""
__author__ = '赵传真'

import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='.', database='sys')

cursor = db.cursor()
cursor.executemany('insert into user (name, age) values (%s, %s)',
                   [
                       ('李时珍', 30),
                       ('Bob', 22)
                   ]
                   )
db.commit()
cursor.close()
db.close()
