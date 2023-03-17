from math import *
from turtle import *
#------FONCTION------
def aire(n,L):
    a = L/(2*tan(pi/n))
    p = n*L
    Aire = a*p/2
    return Aire
def PlusGrand(n1,L1,n2,L2):
    if aire(n1,L1)>=aire(n2,L2):
        polygone(n1,L1)
    else:
        polygone(n2,L2)

def polygone(n,L):
    for loop in range(n):
        forward(L)
        right(360 / n)
#----PROGRAMME PRINCIPAL----
PlusGrand(2,10,15,10)