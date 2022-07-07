ch = input("Please Enter a Character : ")

#if(ch.isupper()):
    #print( ch, "is an Uppercase Alphabet")
#elif(ch.islower()):
    #print( ch, "is a Lowercase Alphabet")
#else:
    #print( ch, "is Not a Alphabet")
    
if(65<=ord(ch)<=90):
     print( ch, "is an Uppercase Alphabet")
elif(97<=ord(ch)<=122):
     print( ch, "is an Lowercase Alphabet")
else:
    print( ch, "is Not a Alphabet")
