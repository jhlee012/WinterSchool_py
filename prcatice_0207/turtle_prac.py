import turtle


t = turtle.Turtle()
t.shape('turtle')
n = int(input("Start Command? (n각형?): "))

for i in range(n):
    t.forward(30)
    t.left(360//n)
