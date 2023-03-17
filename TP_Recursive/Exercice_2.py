def mystere1(n) :
    if n>=0 :
        print(n)
        mystere1(n-1)
def mystere2(n) :
    if n>=0 :
        mystere2(n-1)
        print(n)

mystere1(4)
mystere2(4)
