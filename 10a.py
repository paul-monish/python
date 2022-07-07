try:
    x=input("enter 1st number:")
    y=input("enther 2nd number:")
    if(x.isdigit() and y.isdigit()):
        print("sum= ",int(x)+int(y))
    else:
        raise Exception
except:
    print("These are not a number!!")
