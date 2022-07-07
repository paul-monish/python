unit=int(input("enter number of unit of consumer:"))
if(0<=unit<=200):
    print("amount to be paid:",unit*0.50)
elif(201<=unit<=400):
    print("amount to be paid:",(unit*0.65)+100)
elif(401<=unit<=600):
    print("amount to be paid:",(unit*0.80)+200)
else:
    print("amount to be paid:",(unit*0.1)+300)
