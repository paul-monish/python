import numpy as np

p=np.empty(6,dtype=int)


print("enter element for p:")
for i in range(len(p)):
    p[i]=int(input())
 

q=np.empty(4,dtype=int)
print("enter element q:")
for i in range(len(q)):
    q[i]=int(input())
    
c=0

r=np.empty((len(p)+len(q)),dtype=int)
for i in range(len(p)):
    r[i]=p[i]
    c=c+1

for j in range(len(q)):
    r[c]=q[j]
    c=c+1
   
print("display resultant element of array p and q:")

for i in range((len(p)+len(q))):
    print(r[i]," ",end=" ")
