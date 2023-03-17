from random import random
#------OBJETS------
class Personnage:
    def __init__(self,nom,nbPieces,ptsVie):
        self.nom=nom
        self.nbPieces=nbPieces
        self.ptsVie=ptsVie
        self.main=None
        self.sac=[]

    def donnerPieces(self,p,N):
        if N<p.nbPieces:
            p.nbPieces=p.nbPieces+N
            self.nbPieces=self.nbPieces-N
        else: #pas assez de pièces : il donne tout ce qu'il a
            p.nbPieces=p.nbPieces+self.nbPieces
            self.nbPieces=0

    def volerPieces(self,p,N):
        if N<p.nbPieces:
            self.nbPieces=self.nbPieces+N
            p.nbPieces=p.nbPieces-N
        else: #pas assez de pièces : il donne tout ce qu'il a
            self.nbPieces=self.nbPieces+p.nbPieces
            p.nbPieces=0
            
    def acheter(self,obj):
        if obj.prix<self.nbPieces:
            self.rangerArme(obj)
            self.nbPieces=self.nbPieces-obj.prix
            self.main=obj
        else:
            print("Vous n'avez pas assez d'argent")

    def attaque(self,p):
        if self.main==None:
            print("vous n'avez pas d'arme")
        else:
            p.ptsVie=p.ptsVie-self.main.utilisation()

    def rangerArme(self,a):
        if a == self.main:
            self.sac.append(self.main)
            self.main = None
            

    def __repr__(self):
        return "nom: %s, nombre de piece: %s, nombre de point de vie: %s, Elle a comme arme: %s, elle a dans son sac: %s"%(self.nom,self.nbPieces,self.ptsVie,self.main,self.sac)

class Arme:
    def __init__(self,nom,degat,solidite,prix):
        self.nom=nom
        self.degat=degat
        self.solidite=solidite
        self.prix=prix
        self.appartien=None

    def __repr__(self):
        return "%s"%(self.nom)

    def utilisation(self):
        if random()<=80:
            return self.degat
        else:
            print("coup raté")
            return 0
    
            
#------PROGRAMME PRINCIPAL------
Lara=Personnage("Lara Croft",400,1000)
Kassandra=Personnage("Kassandra Adiades",500,800)
Epee_Bois=Arme("Épée en bois",4,10,20)
Lara.acheter(Epee_Bois)
Lara.acheter(Epee_Bois)
Lara.attaque(Kassandra)
print(Kassandra)
print(Lara)
