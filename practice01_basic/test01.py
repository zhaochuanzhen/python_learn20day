"""
desc: 我的第一个程序
version: 1.0
date: 2019年12月24日17:47:46
"""
import turtle

turtle.pensize(2)
turtle.pencolor('blue')
for item in range(5):
    turtle.forward(200)
    turtle.right(144)

turtle.penup()
turtle.goto(-100, 0)
turtle.mainloop()
