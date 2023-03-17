#taille = 10 / hauteur = 5
#3,6,13,21,28
#8<x<13
#3,5,6,8,x,13,20,21,25,28 / que x est biene ntre 8 et 13
#parcours largeur

#partie 2


#---CLASSES---
class ABR:
    def __init__(self,data):
        self.V=data # valeur d'un noeud
        self.G=None # ABR gauche
        self.D=None # ABR droit
        
    def insert(self,val): # méthode récursive
        if val<=self.V:
            if self.G==None: # on est au bon endroit pour insérer val
                self.G=ABR(val)
            else:
                self.G.insert(val) # méthode récursive sur l'arbre gauche
                ''' si l'ABR gauche était vide alors self.G serait du type None,
                    or la méthode insert ne peut s'appliquer qu'à un objet de type ABR
                    self.G.insert(val) aurait déclencher une erreur de type
                    'NoneType' object has no attribute 'insert'
                '''
        else:
            if self.D==None: # on est au bon endroit pour insérer val 
                self.D=ABR(val)
            else:
                self.D.insert(val) # méthode récursive sur l'arbre droit



    def taille(self):
        if self.G != None and self.D != None:
            return 1 + self.G.taille() + self.D.taille()
        elif self.G != None and self.D == None:
            return 1 + self.G.taille()
        elif self.D != None and self.G == None:
            return 1 + self.D.taille()
        else:
            return 1

    def hauteur(self):
        if self.G != None:
            return 1 + self.G.hauteur()
        elif self.D != None:
            return 1 + self.D.hauteur()
        else:
            return 1


#=== FONCTION ===

#=== PROGRAMME PRINCIPAL ===
A=ABR(20)
LA=[5,25,3,12,21,28,8,13,6]
for valeur in LA:
    A.insert(valeur)

print(A.taille())
print(A.hauteur())
