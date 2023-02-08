import turtle as t
import time

def tree_l(length):
    if length > 15:
        t.forward(length)
        t.right(40)
        tree(length-30)
        t.left(80)
        tree(length-30)
        t.right(40)
        tree(length-15)
        t.backward(length)
def tree(length):
    if length > 5:
        t.forward(length)
        t.right(40)
        tree(length-30)
        t.left(80)
        tree(length-30)
        t.right(40)
        tree_l(length-15)
        t.backward(length)




t.left(90)
t.color("green")
t.speed(1000)
tree(150)

time.sleep(20000)