import turtle
from turtle import *
t = Turtle()



length = 100



def square():
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
def modsquare():
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)    
def row(x):
    for what in range(x):
        square()
        t.forward(length)




def tower():    
    row(5)
    t.back()
tower()






turtle.done()