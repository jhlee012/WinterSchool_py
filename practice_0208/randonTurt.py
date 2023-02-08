import turtle
import random

t= turtle.Turtle()
t.shape('turtle')

while True:
    length= random.randint(100,300)
    t.forward(length)
    angle = random.randint(-90, 90)
    t.right(angle)
    t.write('어쩌라고씨발련아')

turtle.mainloop()


endcode = input('Endcode [q]')
if endcode == 'q':
    exit()
