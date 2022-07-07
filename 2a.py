a=int(input("enter a= "))
b=int(input("enter b= "))

temp=0

temp=a
a=b
b=temp
print("After swaping using thired variable a=",a,"b=",b)

a=a+b
b=a-b
a=a-b

print("After swaping using without thired variable a=",a,"b=",b) 