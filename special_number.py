def facorial(n):
    f=1
    for i in range(1,(n+1)):
        f=f*i
    return f

def isSpecialNumber(n):
    org=n
    r=0
    f=0
    while(n!=0):
        r=n%10
        n=n//10
        f+=facorial(r)
    if(org==f):
        return True
    else:
        return False
    
a=1
b=500
for i in range(a,(b+1)):
    
    if(isSpecialNumber(i)):
        print(i,"Special Number")
