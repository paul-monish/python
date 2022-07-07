n=int(input("enter number:"))
org=n
rev=0
while(n!=0):
    a=n%10
    n=n//10
    rev=rev*10+a

if(org==rev):
    print(org,"palindrom")
else:
    print(org,"not palindrom")
    
