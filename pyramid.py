import turtle
from turtle import *
t = Turtle()



length = 50
iterations = 25

t.speed(0)
def square():
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
def row(x):
    for what in range(x):
        square()
        t.forward(length)




def pyramid(x):
    iterations = x
    pixellength = iterations*length    
    for i in range(iterations):
        row(iterations)
        t.right(90)
        t.forward(length)
        t.left(90)
        t.back(pixellength - length)
        t.left(90)
        t.forward(length*2)
        t.right(90)
        iterations -= 1
        pixellength -= length
pyramid(iterations)





turtle.done()