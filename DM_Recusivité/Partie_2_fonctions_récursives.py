from turtle import *
from math import *
from numpy import *
def carre(l):
    for loop in range(4):
        forward(l)
        left(90)
def truc(k,a,n):
    if n%2 ==0:
        fillcolor('blue')
        begin_fill()
    else:
        fillcolor('yellow')
        begin_fill()
    carre(a)
    forward((1-k)*a)
    left(degrees(arctan((1-k)/k)))
    end_fill()
    if n > 0:
            truc(k,a*(sqrt(2*k**2-2*k+1)),n-1)
speed(0)
truc(0.15,400,30)