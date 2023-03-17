#function
def C(n,p):
    if n==p or p==0:
        return 1
    else:
        return C(n-1,p-1) + C(n-1,p)

def Triangle_pascal(n,p):
    for i in range(n):
        for p in range(i+1):
            print(C(i,p),end=" ")
        print("")

#programme_principale
print(C(8,3))

Triangle_pascal(8,3)

