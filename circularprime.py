def isPrime(n):
    f=0
    for i in range(1,(n+1)//2):
        if(n%i==0):
            f=f+1
            #print(f)
    if(f<=2):
        return True
    else:
        return False
 
def countDigit(n):
    count=0
    while(n!=0):
        n=n//10
        count=count+1
    return count

def isCircularPrime(n):
    c=countDigit(x)
    p=1
    i=1
    f=1
    while(c!=0):
        n=x
        c=c-1
        p1=pow(10,c)
        p2=pow(10,p)
        rem=n%p2
        n=n//p2
        p=p+1
        cd=rem*p1+n
        print("after shifting",i,":",cd)
        i=i+1
        if(isPrime(cd)==False):
            f=0
            break
        
    if(f==1):
        return True
    else:
        return False
    
x=int(input("enter number:"))     
#print(countDigit(n))
if(isPrime(x)==False):
    print(x,"is not a circular prime!!")
else:
    if(isCircularPrime(x)==True):
        print(x,"is a circular prime!!")
    else:
        print(x,"is prime but not a circular prime!!")
        
    

