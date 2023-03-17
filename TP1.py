from File import *
from random import randint
#---class---
class Noeud:
    def __init__(self,v,g=None,d=None):
        self.valeur=v
        self.filsGauche=g #de type Noeud
        self.filsDroit=d #de type Noeud

    def Taille(self,racine):
        
        if racine == None:
            return 0
        return 1 + self.Taille(racine.filsGauche) + self.Taille(racine.filsDroit)

    def Hauteur(self,racine):
        if racine == None:
            return 0
        return 1 + max(self.Hauteur(racine.filsGauche),self.Hauteur(racine.filsDroit))

    def prefixe(self,racine):
        if racine != None:
            print(racine.valeur,end=' ') 
            self.prefixe(racine.filsGauche)
            self.prefixe(racine.filsDroit)

    def infixe(self,racine,L):
        if racine != None:
            self.infixe(racine.filsGauche,L)
            L.append(racine.valeur)
            self.infixe(racine.filsDroit,L)
        return L

    def postfixe(self,racine):
        if racine != None:
            self.postfixe(racine.filsGauche) 
            self.postfixe(racine.filsDroit)
            print(racine.valeur,end=' ')

    def Parcours_en_largeur(self,racine,taille): #revoir file
        F = File()
        if racine != None:
            F.enfiler(racine)
        while False == F.est_vide():#for loop in range(taille):#mettre une vérification de si F est vide et non la taille de F...... ;-;
            racine = F.defiler()
            print(racine.valeur, end=' ')
            if racine.filsGauche != None:
                F.enfiler(racine.filsGauche)
            if racine.filsDroit != None:
                F.enfiler(racine.filsDroit)

    def Recherche(self,racine,val):
        if racine == None:
            return False
        if val < racine.valeur:
            return self.Recherche(racine.filsGauche,val)
        elif val > racine.valeur:
            return self.Recherche(racine.filsDroit,val)
        else:
            return True

    def recherche(self,racine,val):
        while racine != None and val != racine.valeur:
            if val < racine.valeur:
                racine = racine.filsGauche
            else:
                racine = racine.filsDroit
        return racine !=None

    def Insertion(self,racine,val):
        if racine == None:
            return Noeud(val)
        if val <= racine.valeur:
            return Noeud(racine.valeur,self.Insertion(racine.filsGauche,val),racine.filsDroit)
        else:
            return Noeud(racine.valeur,racine.filsGauche,self.Insertion(racine.filsDroit,val))

    def insertion(self,racine,val):
        if racine == None:
            racine = Noeud(val)
        else:
            while racine != None:
                pere = racine
                if val <= racine.valeur:
                    racine = racine.filsGauche
                else:
                    racine = racine.filsDroit
            if val <= pere.valeur:
                pere.filsGauche = Noeud(val)
            else:
                pere.filsDroit = Noeud(val)
                

class Arbre:
    def __init__(self,racine=None):
        self.racine=racine #de type Noeud

    def taille(self):
        '''renvoie le nombre de Noeud a partir de la racine'''
        return self.racine.Taille(self.racine)

    def hauteur(self):
        '''renvoie la hauteur de la racine jusqu'au feuille'''
        return self.racine.Hauteur(self.racine)

    def prefixe(self):
        '''determine le parcour prefixe d'un arbre'''
        return self.racine.prefixe(self.racine)

    def infixe(self):
        '''determine le parcour infixe d'un arbre'''
        return self.racine.infixe(self.racine)

    def postfixe(self):
        '''determine le parcour postfixe d'un arbre'''
        return self.racine.postfixe(self.racine)

    def Parcours_en_largeur(self,arbre):
        t = arbre.taille()
        return self.racine.Parcours_en_largeur(self.racine,t)

class ABR:
    def __init__(self,racine=None):
        self.racine = racine

    def Recherche(self,val):
        return self.racine.Recherche(self.racine,val)

    def recherche(self,val):
        return self.racine.recherche(self.racine,val)

    def Insertion(self,val):
        return ABR(self.racine.Insertion(self.racine,val))

    def insertion(self,val):
        return self.racine.insertion(self.racine,val)

    def infixe(self):
        '''determine le parcour infixe d'un arbre'''
        return self.racine.infixe(self.racine,[])
    def est_ABR(self):
        print(self.infixe())
        if self.racine != None:
            if self.infixe() == sorted(self.infixe()):
                return True


