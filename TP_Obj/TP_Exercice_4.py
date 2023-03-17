from math import *
from turtle import *
class Point:
    def __init__(self,abscisse,ordonnee):
        self.coord=[abscisse,ordonnee] # un point est défini par ses coordonnées mises dans une liste
    def trace(self,couleur):
        dot(15,couleur) # permet de représenter avec Turtle le point avec une couleur donnée
class Segment:
    def __init__(self,ptA,ptB): # ptA et ptB sont des objets définis par la classe Point
        self.ptA=ptA
        self.ptB=ptB

    def distance(self):
        return sqrt((self.ptB.coord[0]-self.ptA.coord[0])**2 + (self.ptB.coord[1]-self.ptA.coord[1])**2)
    def trace(self,couleur): # couleur est une variable de type chaîne de caractère
        up()
        goto(self.ptA.coord[0],self.ptA.coord[1]) # on se positionne à ptA(xA,yA)
        down()
        self.ptA.trace(couleur) # on représente le point ptA
        pencolor(couleur) # stylo en couleur
        pensize(5) # largeur du trait du stylo
        goto(self.ptB.coord[0],self.ptB.coord[1]) # on se positionne à ptB(xB,yB)
        self.ptB.trace(couleur) # on représente le point ptB

class Triangle:
    def __init__(self,ptA,ptB,ptC):
        self.sommets=[ptA,ptB,ptC] # collection d'objets Point
        self.Seg_AB=Segment(self.sommets[0],self.sommets[1]) #Segment AB
        self.Seg_BC=Segment(self.sommets[1],self.sommets[2]) # Segment BC
        self.Seg_CA=Segment(self.sommets[2],self.sommets[0]) # Segment CA
        self.AB=self.Seg_AB.distance() # Longueur AB
        self.BC=self.Seg_BC.distance() # Longueur BC
        self.CA=self.Seg_CA.distance() # Longueur CA
    def trace(self,couleur):
        up()
        goto(self.sommets[0].coord[0],self.sommets[0].coord[1]) # on se positionne au point ptA
        down()
        fillcolor(couleur)
        Segment(self.sommets[0],self.sommets[1]).trace(couleur) # on trace en couleur le segment ptAptB
        Segment(self.sommets[1],self.sommets[2]).trace(couleur) # on trace en couleur le segment ptBptC
        Segment(self.sommets[2],self.sommets[0]).trace(couleur) # on trace en couleur le segment ptCptA
        end_fill()
    def périmètre(self):
        return self.AB + self.BC + self.CA
    def aire(self):
        P=self.périmètre()/2
        return sqrt(P*(P-self.AB)*(P-self.BC)*(P-self.CA))
    def rectangle(self):
        return self.AB**2 == self.BC**2 + self.CA**2 or self.BC**2 == self.AB**2 + self.CA**2 or self.CA**2 == self.AB**2 + self.BC**2
    def isocele(self):
        return self.AB == self.BC or self.BC == self.CA or self.CA == self.AB
    def equilateral(self):
        return self.AB == self.BC == self.CA
#----PROGRAMME PRINCIPAL---- 2)
##A=Point(0,-60)
##B=Point(100,90)
##Seg_AB=Segment(A,B)
##Seg_AB.trace("green")
##print(Seg_AB.distance())

#----PROGRAMME PRINCIPAL---- 3) 
A=Point(0,-60)
B=Point(100,90)
C=Point(-180,60)
T=Triangle(A,B,C)
T.trace("blue")
print(T.périmètre())
print(T.aire())
print(T.rectangle())
print(T.isocele())
print(T.equilateral())
