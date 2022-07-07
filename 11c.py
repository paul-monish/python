'''11 c'''
fp=open('fibonacci.txt','w+')
n=int(input("Enter range:"))


fp.write("Fibonacci number in range 0 to"+str(n)+" : ")
a,b=0,1
fp.write(str(a)+" ")
fp.write(str(b)+" ")
for i in range(2,n+1):
    c=a+b
    fp.write(str(c)+" ")
    a=b
    b=c
fp.close()