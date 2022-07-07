def findFactors(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    return count;

def isComposite(n):
    if(findFactors(n)>2):
        return True
    return False

def sumOfDigit(n):
    a=0
    sum=0
    while(n!=0):
        a=n%10
        n=n//10
        sum+=a
    return sum

def countDigit(n):
    count=0
    while(n!=0):
        n=n//10
        count=count+1
    return count

def isMagicNumber(n):
    s=0
    while(countDigit(n)>1):
        s=sumOfDigit(n)
        n=s
    return checkMagicNumber(s)
       
def checkMagicNumber(n):
    if(n==1):
        return True
    return False
    
    
    
m=int(input("enter lower range:"))
n=int(input("enter higher range:"))
#print(isMagicNumber(28))
count=0
for i in range(m,n+1):
    if(isComposite(i) and isMagicNumber(i)):
        print(i)
        count=count+1
print("frequency= ",count)


