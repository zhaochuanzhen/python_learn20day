"""复杂查询"""
__author__ = '赵传真'
import mysql.connector

db = mysql.connector.connect(host='192.168.120.143', user='root', passwd='123456', database='think_admin_newtv')
cursor = db.cursor()
cursor.execute('select * from s_layout limit 0, 10')
print(cursor.fetchall())
