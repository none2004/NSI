#---classe---
class Pile:
    def __init__(self):
        self.taille=0
        self.contenu=[]

    def est_vide(self):
        '''Renvoie un boléen'''
        return self.contenu==[]

    def empiler(self,x):
        '''empile x dans la pile p'''
        self.taille=self.taille+1
        self.contenu.append(x)

    def depiler(self):
        '''si la pile est non vide, dépile la dernière valeur et la retourne'''
        if self.taille!=0:
            self.taille = self.taille-1
            return self.contenu.pop()

    def __str__(self):
        return "Pile : taille = %s et contenu = %s"%(self.taille,self.contenu)

#---programme principale---
P=Pile()
print(P)
print(P.est_vide())
P.empiler(5)
print(P)
print(P.depiler())
