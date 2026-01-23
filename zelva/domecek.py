from turtle import forward, left, exitonclick, right
from random import randint
from math import sqrt

def domecek(a):
    c = sqrt(2*a**2)
    forward(a)
    left(90)
    forward(a)
    left(45)
    forward(c/2)
    left(90)
    forward(c/2)
    left(135)
    forward(a)
    left(180)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
for i in range(10):
    domecek(randint(10,50))
    right(36)
exitonclick()
