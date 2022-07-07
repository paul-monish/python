
def sumofsquare(n):
    if(n<0):
        return False
    i=1
    while(i*i)<=n:
        j=1
        while (j*j)<=n:
            if((i*i)+(j*j)==n):
                return True
            j+=1
        i+=1
    return False

        
n=int(input("Enter number which you want to check?"))
print(sumofsquare(n))