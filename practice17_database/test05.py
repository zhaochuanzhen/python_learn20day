"""查询全部"""
__author__ = '赵传真'
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='.', database='sys')
cursor = db.cursor()
