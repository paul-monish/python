n=int(input("enter range:"))
a,b=0,1
print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    print(c)
    a=b
    b=c
    
