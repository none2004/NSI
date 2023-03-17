#---Fonctions---
def creer_pile():
    ''' créer une pile vide'''
    return []

def taille(p):
    ''' retourne la taille de la pile'''
    return len(p)

def sommet(p):
    '''retourne la dernière de la pile'''
    return p[len(p)-1]

def pile_vide(p):
    '''Renvoie un boléen'''
    return p==[]

def empiler(p,x):
    '''empile x dans la pile p'''
    p.append(x)

def depiler(p):
    '''si la pile est non vide, dépile la dernière valeur et la retourne'''
    if len(p)!=0:
        return p.pop()

#---PROGRAMME PRINCIPAL---
P=creer_pile()
print(P)
print(pile_vide(P))
for i in range(10):
    empiler(P,i)
print(P)
print(pile_vide(P))
depiler(P)
print(P)
print(taille(P))
print(sommet(P))
