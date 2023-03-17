import pygame
from pygame.locals import *
 
pygame.init()
 
black    = (0, 0, 0)
white   = (255, 255, 255)
blue     = (0, 0, 255)
green   = (0, 255, 0)
red       = (255, 0, 0)
 
size = [640,640]
fenetre = pygame.display.set_mode(size)
fenetre.fill(white)
 
def Milieu(Pt1,Pt2):
# Pt1 est une liste de deux réels représentant les coordonnées du point 1
# Pt2 est une liste de deux réels représentant les coordonnées du point 2    
    return [3********** , ***********]
 
def triangle(A,B,C,n):
    if(n>1):
        pygame.draw.polygon(fenetre,black,[Milieu(A,B),Milieu(B,C),Milieu(A,C)])
        triangle(***********,***********,***********,***********)
        triangle(***********,***********,***********,***********)
        triangle(***********,***********,***********,***********)
            
Pt1=[10,630]
Pt2=[630,630]
Pt3=[320,93]
pygame.draw.polygon(fenetre,black,[Pt1,Pt2,Pt3],5) 
triangle(Pt1,Pt2,Pt3,7)
pygame.display.flip()
 
continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type==QUIT or event.type==MOUSEBUTTONDOWN:
            pygame.quit()
            continuer=False
