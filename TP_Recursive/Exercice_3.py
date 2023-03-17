#Fonction
def nombre_de_chiffres(n,d=0):
    if n >= 1:
        d = d+1
        return nombre_de_chiffres(n//10,d)
    else:
        return int(d)





#Programme principale
print(nombre_de_chiffres(105101))
