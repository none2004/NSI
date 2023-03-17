#---classe---
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

#---programme principal---
P=Pile()
for i in range(10):
    P.empiler(i)
print(P)
print("valeur dépiler :",P.depiler())
print(P)
