x=int(input("enter number of class held:"))
y=int(input("enter number of class attend:"))
per=(y/x)*100
if(per>=75):
    print("student allowed to sit in exam")
else:
    str=input("has student any medical cause?")
    if(str=="yes" or str=="YES"):
        print("student allowed to sit in exam")
    elif(str=="no" or str=="NO"):
        print("student not allowed to sit in exam")
        
    

