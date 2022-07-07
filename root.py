
import math
import cmath

a=float(input("enter 1st coefficient number:"))
b=float(input("enter 2nd coefficient number:"))
c=float(input("enter 3rd coefficient number:"))
discriminant= (b**2) - (4*a*c)

if (discriminant > 0):
    print("real and different roots")
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("root1 = ", root1, " and root2 = ",root2)

elif(discriminant ==0):
    print("real and equal roots")
    root1 = root2 = -b / (2 * a)
    print("root1 = root2 = ", root1)

else:
    print("roots are not real")
    realPart = -b / (2 * a);
    imagPart = cmath.sqrt(discriminant) / (2 * a);
    print("root1 =",realPart,"+",imagPart,"and \nroot2 =",realPart,"-",imagPart);
    

    


