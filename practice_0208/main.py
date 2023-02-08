# import time
# import turtle as t
# import time
#
# def squreUp(length):
#     for i in range(3):
#         t.forward(length)
#         t.left(90)
#
#
# def squareDown(length):
#     for i in range(3):
#         t.forward(length)
#         t.right(90)
#
#
# def drawSqX(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     t.color("green")
#     squareDown(50)
#     t.end_fill()
#
#
#
# screenCtrl = t.Screen()
# screenCtrl.setup(800, 700)
# screenCtrl.onscreenclick(drawSqX)  # Add some FUNCTION gets x, y (two params)
import turtle
import turtle


t = turtle.Turtle()
t.shape('turtle')
t.pensize(10)

def draw(x, y):
    t.goto(x,y)

s = turtle.Screen()
s.onscreenclick(draw)

# a = input('프로그램을 종료하려면 [q]입력..')
# if a == 'q' or a == 'Q':
#     exit()
turtle.mainloop()