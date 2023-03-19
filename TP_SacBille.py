from math import pi
#----class----
class Bille:
    def __init__(self,rayon):
        self.rayon = rayon

    def masse(self):
        return (4/3*pi*self.rayon**3)*8/1000
    def tamis(self,maille):
        return self.rayon*2<maille

    def __repr__(self):
        return "%s"%(self.rayon)

class Sac:
    def __init__(self):
        self.collection_billes = []

    def mettre(self,b):
        self.collection_billes.append(b)
    def enlever(self,b):
        self.collection_billes.remove(b)
    def masse(self):
        masse=0
        for loop in range(len(self.collection_billes)):
            masse = masse + self.collection_billes[loop].masse()
        return masse
    def tri(self,maille):
        Reste = []
        for loop in self.collection_billes:
            if loop.tamis(maille) == False:
                Reste.append(loop)
        self.collection_billes = Reste
                
        

    def __repr__(self):
        return "%s Billes: %s"%(len(self.collection_billes),self.collection_billes)
            
#----Programme principale----
r=[2.1,3.7,3.6,2.4,1.7,2.6,2.8,1.4,1.1,1.7]
S=Sac()
for rayon in r:
    S.mettre(Bille(rayon))
print(S)
print("Masse du sac en kg:",S.masse())
M=5
S.tri(M)
print(S)
print("Masse du sac en kg:",S.masse())
