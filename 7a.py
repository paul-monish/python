a=input("Enter String:")
count=0
b=a.replace(' ','')
print(a)
for i in b:
    if(i.isupper()==True):
        count=count+1
print(count," ",(len(b)-count))