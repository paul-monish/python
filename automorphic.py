a=11
b=100
sqr=0
def isAutomorphic(i):
    sqr=i**2
    while(i!=0):
        if(i%10 != sqr%10):
            return False
        i//=10
        sqr//=10
    return True
for i in range(a,(b+1)):
    if(isAutomorphic(i)):
        print(i,"is automorphic")
        
        

        
