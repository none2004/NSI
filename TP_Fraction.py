#----class----
class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    
    def pgcd(self,a,b):
        a,b=abs(a),abs(b) # on travaille avec des entiers naturels
        if a<b: # on doit intervertir a et b si a<b
            a,b=b,a
        if b==0: #Algorithme récursif d'Euclide
            return a
        else:
            r=a%b
            a=b
            b=r
            return self.pgcd(a,b) #self indispensable car pgcd() est interne à Fraction

    def plus(self,F):
        self.num = self.num*F.den+self.den*F.num
        self.den = (self.den*F.den)
        self.simplify()
        return Fraction(self.num,self.den)
    
    def moins(self,F):
        self.num = self.num*F.den-self.den*F.num
        self.den = (self.den*F.den)
        self.simplify()
        return Fraction(self.num,self.den)

    def fois(self,F):
        self.num = self.num*F.num
        self.den = self.den*F.den
        self.simplify()
        return Fraction(self.num,self.den)

    def div(self,F):
        self.num = self.num*F.den
        self.den = self.den*F.num
        self.simplify()
        return Fraction(self.num,self.den)
    
    def simplify(self):
        # on divise le num et le den par le pgcd(num,den)
        d=self.pgcd(self.num,self.den)
        self.num=self.num//d
        self.den=self.den//d
        if self.num*self.den<0: # on met sous la forme -a/b (a et b positifs)
            self.num=-abs(self.num)
            self.den=abs(self.den)
        else: # on met sous la forme a/b (a et b positifs)
            self.num=abs(self.num)
            self.den=abs(self.den)
    
    def __repr__(self):
        if self.den!=1:
            return "%s/%s"%(self.num,self.den)
        else:
            return str(self.num)


#----programme principale----
F1 = Fraction(8,9)
F2 = Fraction(-25,4)
F3 = Fraction(1,3)
F4 = Fraction(7,-5)
F5 = Fraction(-4,-9)
print(F1.moins(F2.fois(F3).div(F4.plus(F5))))
