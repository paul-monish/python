import numpy as np

n=int(input("enter length of 1-D array:"))
a=np.empty(n,dtype=int)
max=a[0]
min=a[0]
print("enter element for 1-D array:")
for m in range(len(a)):
    a[m]=int(input())

for n in range(len(a)):
    if(a[n]>max):
        max=a[n]
    if(a[n]<min):
        min=a[n]
        
print("maximum in 1-D array=",max)
print("minimum in 1-D array=",min)


r=int(input("enter row:"))
c=int(input("enter col:"))
b=np.empty((r,c),dtype=int)
max=b[0,0]
min=b[0,0]
print("enter element for 2-D array:")
for i in range(r):
    for j in range(c):
        b[i,j]=int(input())


for i in range(r):
    for j in range(c):
        if(b[i,j]>max):
            max=b[i,j]
        if(b[i,j]<min):
            min=b[i,j]
        
print("maximum in 2-D array=",max)
print("minimum in 2-D array=",min)
