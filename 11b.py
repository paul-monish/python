fp=open('Prime.txt','w+')
numr=int(input("Enter range:"))


fp.write("Prime numbers in range"+str(numr)+" : ")
for n in range(1,(numr)):

    for i in range(2,(n//2)):

        if(n%i==0):

            break

    else:
        
        fp.write(str(n)+" ")

fp.close()