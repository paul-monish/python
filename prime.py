
x = int(input("Enter the lower range:"))
y = int(input("Enter the upper range:"))
for i in range(x,y+1):
    if(i>1):
        for j in range(2,((i+1)//2)):
            #print(i%j)
            if (i%j)==0:
                break
        else:
            print(i)
    