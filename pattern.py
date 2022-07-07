5
def pattern1(r,c):
    for i in range(0,r):
        
        for j in range(0,c):
            if((i+j)>=(r-1)):
                print(i+j-r+2,end="")
                
            else:
                print(" ",end="")
        print()
    
def pattern2(r,c):
    for i in range(r,0,-1):
        for j in range(i,0,-1):
            print(chr(i-j+65),end="")
        for k in range(i,r):
            print(" ",end="")
        #for k in range(i,r):
            #print(" ",end="")
        for m in range(i-1,0,-1):
            print(chr(m+64),end="")
        print()
        
def pattern3(r,c):
    for i in range(0,r):
        for j in range(0,c):
            if((i==0 or j==0 or i==4 or j==4) or (i==j) or (i+j)==(r-1) ):
                if((i==j) or (i+j)==4):
                    print(" $ ",end="")
                else:
                    print(" * ",end="")
            else:
                print("   ",end="")
        print()
        
        
row=int(input("enter row number:"))
col=int(input("enter column number:"))
print("press 1 for patter1.")
print("press 2 for patter2.")
print("press 3 for patter3.")
choice=int(input("enter your choice:"))
if(choice==1):
    pattern1(row,col)
elif(choice==2):
    pattern2(row,col)
elif(choice==3):
    pattern3(row,col)
else:
    print("Wrong choice!!")

    



        