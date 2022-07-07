def append_middle(a,b):
    n=len(a)//2
    y=(a[0:n]+b)+a[n+1:len(a)]
    print(y)
    
a=input("enter 1st string:")
b=input("enter 2nd string:")
append_middle(a,b)