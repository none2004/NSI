def annee_bissextile(annee):
    return (annee%4==0 and annee%100!=0 or annee%400==0)
def annee_seconde(annee):
    if annee_bissextile(annee):
        return 366*24*60*60
    else:
        return 365*24*60*60
def annee_temps(annee):
    return (2021-annee)*annee_seconde(annee)


print(annee_bissextile(2021))
print(annee_seconde(2021))
print(annee_temps(2020))