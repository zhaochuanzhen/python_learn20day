"""创建表"""
__author__ = '赵传真'

import MySQLdb
db = MySQLdb.connect("localhost", "root", ".", "sys", charset='utf8')
cursor = db.cursor()

cursor.execute('DROP table if exists EMPLOYEE')
cursor.execute("""
CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )
""")

cursor.close()
db.close()
