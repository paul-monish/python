import numpy as np

r=int(input("enter row:"))
c=int(input("enter col:"))
b=np.empty((r,c),dtype=int)
print("enter element for 2-D array:")
for i in range(r):
    for j in range(c):
        b[i,j]=int(input())

print("display 2-D array:")
for i in range(r):
    for j in range(c):
        print(b[i,j],"  ",end="")
    print()
    

print("display Non Boundary Element in 2-D array:")
count=0
for i in range(r):
    
    for j in range(c):
        
        if(i!=0 and j!=0 and i!=r-1 and j!=c-1 ):
            
            print(b[i,j],"  ",end="")
    print()
    
   
print(count)