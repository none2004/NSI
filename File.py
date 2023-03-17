class Cellule:
    def __init__(self,v,s):
        self.valeur=v
        self.suivant=s

class Pile:
    def __init__(self):
        self.contenu=None

    def est_vide(self):
        '''Renvoie un boléen'''
        return self.contenu==None

    def empiler(self,v):
        '''empile v dans la cellule p'''
        self.contenu=Cellule(v,self.contenu)

    def depiler(self):
        '''depile le sommet et le renvoie'''
        d = self.contenu.valeur
        self.contenu=self.contenu.suivant
        return d

    def __str__(self):
        affichage=""
        c=self.contenu
        while c!=None:
            affichage=affichage+str(c.valeur)+"\n"
            c=c.suivant
        return affichage

class File:
    def __init__(self):
        self.entre=Pile()#pile d'entrée
        self.sortie=Pile()#pile de sortie

    def est_vide(self):
        return self.entre.est_vide() and self.sortie.est_vide()

    def enfiler(self,i):
        self.entre.empiler(i)

    def defiler(self):
        if self.sortie.est_vide(): #si sortie est vide on depile tout entre
            while not self.entre.est_vide():
                self.sortie.empiler(self.entre.depiler())
        return self.sortie.depiler() 
        
    def __str__(self):
        L1="---------\nPile d'entrée :\n"
        L2="Pile de sortie:\n"
        L3="---------"
        if self.entre.est_vide():
            L1=L1+"\n"
        else:
            L1=L1+str(self.entre)
        if self.sortie.est_vide():
            L2=L2+"\n"
        else:
            L2=L2+str(self.sortie)
        return L1+L2+L3
