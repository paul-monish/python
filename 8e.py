
orgstr=input("Enter string:")
if(len(orgstr)<7):
    print("Please give string has greater 7 charecter...")
else:
    n=(len(orgstr)-3)//2
    newstr=orgstr[n:(n+3)]
    print(newstr);
    
