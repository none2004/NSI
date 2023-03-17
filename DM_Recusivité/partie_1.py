
#------FONCTION------
def moyenne(l):
    moyenne = 0
    for loop in range(len(l)):
        moyenne = l[loop-1] + moyenne
    moyenne = moyenne/len(l)
    return moyenne
def variance(l):
    variance = 0
    m = moyenne(l)
    for loop in range(len(l)):
        variance = variance + (l[loop-1]-m)**2
    return variance/len(l)
#----PROGRAMME PRINCIPAL----
liste = [5,8,9,11,14,17,19]
print(moyenne(liste))
print(variance(liste))