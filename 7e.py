def wellbracketed(s):
    d=0
    if(s[0]==')'):
        return False
    else:
        
        for i in s:
            if(i=='('):
                d+=1
            elif(i==')'):
                d-=1
            if(d<0):
                return False
        return(d==0)

s=input()
x=wellbracketed(s)
print(x)