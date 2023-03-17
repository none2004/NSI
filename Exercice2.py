##taille = 7
##hauteur = 3
## racine = kamel / feuille = joris, kamel, carine, abdou

#=========Methode======== (Partie 1)
def est_vide(L):
    return len(L)==0

def racine(L):
    return L[0]

def gauche(L):
    return L[1]

def droit(L):
    return L[2]

def vainqueur(L):
    return "Le vainqueur est " + racine(L)

def finaliste(L):
    return "Les finalistes sont " + racine(gauche(L)) + " et " + racine(droit(L))

#========= programme principale ========= (Partie 1)
A=[]
A.append("Kamel")
A.append(["Kamel",["Joris",[],[]],["Kamel",[],[]]])
A.append(["Carine",["Carine",[],[]],["Abdou",[],[]]])

##print(est_vide(A))
##print(vainqueur(A))
##print(finaliste(A))


#=========Methode======== (Partie 2)
def occurrences(arbre,nom):
    if racine(arbre) == nom and not est_vide(gauche(arbre))and not est_vide(droit(arbre)):
        return 1 + occurrences(gauche(arbre),nom) + occurrences(droit(arbre),nom)
    elif not est_vide(gauche(arbre))and not est_vide(droit(arbre)):
        return occurrences(gauche(arbre),nom) + occurrences(droit(arbre),nom)
    elif racine(arbre)==nom:
        return 1
    else:
        return 0

def a_gagner(arbre,nom):
    return occurrences(arbre,nom)>1

def nombre_matchs(arbre,nom):
    return occurrences(arbre,nom)-1


def liste_joueurs(arbre):
    if est_vide(arbre):
        return None
    elif est_vide(gauche(arbre)) and est_vide(droit(arbre)):
        return [racine(arbre)]
    else:
        return liste_joueurs(gauche(arbre)) +liste_joueurs(droit(arbre))
        
    
#========= programme principale ========= (Partie 2)
B=[]
B.append("Lea")
B.append(["Lea",\
          ["Lea",["Marc",[],[]],["Lea",[],[]]],\
          ["Theo",["Claire",[],[]],["Theo",[],[]]]])
B.append(["Louis",\
          ["Louis",["Marie",[],[]],["Louis",[],[]]],\
          ["Anne",["Anne",[],[]],["Kevin",[],[]]]])

print(occurrences(A,"Kamel"))
print(a_gagner(A,"Kamel"))
print(nombre_matchs(A,"Kamel"))
print(liste_joueurs(B))
