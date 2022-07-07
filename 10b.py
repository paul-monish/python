import datetime
def validateDate(day,month,year):
    
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        print("no,  It is not a Valid date!!")
    else:
        print("yes, It is a valid date!!")

dt=input("Enter birth date like (dd.mm.yyyy) formate:")
date=dt.split('.')

dd=date[0]
mm=date[1]
yyyy=date[2]

validateDate(dd,mm,yyyy)