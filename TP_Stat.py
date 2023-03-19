from math import sqrt
#----class----
class SerieStat:
    def __init__(self,l,L):
        self.Valeurs = l
        self.Effectifs = L

    def moyenne(self):
        Moyenne = 0
        for loop in range(len(self.Effectifs)):
            Moyenne = Moyenne + self.Valeurs[loop-1]*self.Effectifs[loop-1]
        Moyenne = Moyenne/sum(self.Effectifs)
        return Moyenne

    def variance(self):
        Variance = 0
        for loop in range(len(self.Effectifs)):
            Variance = Variance +self.Effectifs[loop-1]*(self.Valeurs[loop-1]-self.moyenne())**2
        Variance = Variance/sum(self.Effectifs)
        return Variance

    def ecart_type(self):
        return sqrt(self.variance())
    
    def __str__(self):
        return "Valeurs:      %s \nEffectifs:    %s"%(self.Valeurs,self.Effectifs)



#----Programme principale----
a = SerieStat([1,2,3,4,5],[10,12,5,12,20])
print(a)
M = a.moyenne()
print("Moyenne :",M)
V = a.variance()
print("Variance :",V)
E = a.ecart_type()
print("Ecart-type :",E)
