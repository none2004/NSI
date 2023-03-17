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
        '''
        si les deux sous-arbres existent, retourne 1+self.G.taille()+self.D.taille()
        sinon si seul l'arbre gauche existe, retourne 1+ taille du sous-arbre gauche
        sinon si seul l'arbre droite existe, retourne 1+ taille du sous-arbre droit
        sinon retourne 1 (on est arrivé à une feuille)
        '''

    def hauteur(self):
        '''
        s'inspirer de la méthode taille
        '''

    def recherche(self,data):
        '''
        si data=la valeur du noeud, retourne True
        sinon si data<la valeur du noeud et que sous-arbre gauche existe, retourne self.G.recherche(data)
        sinon si data>la valeur du noeud et que sous-arbre droit existe, retourne la recherche de data dans sous-arbre droit
        sinon retourne ...
        '''
        
    def decroissant(self,L=[]):
        '''
        il suffit de faire un parcours infixe dans l'autre sens : de la droite vers la gauche
        '''

    def minimum(self):
        '''
        si l'arbre gauche n'existe pas, retourne la valeur du noeud
        sinon retourne le minimum de l'arbre gauche
        '''

    def maximum(self):
        '''
        s'inspirer de la méthode minimum
        '''
