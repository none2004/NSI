#Fonction
def nombre_de_bits_1(nD,nB=0):
    if nD//2 == 0:
        return nB
    else:
        return nombre_de_bits_1(nD//2,nB+1)
#Programme principale
print(nombre_de_bits_1(125))
