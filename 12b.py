
import math
class Circle:
    radius=0
    def __init__(self,radius):
        self.radius=radius
        
    def get_radius(self):
        return self.radius
    
    def calc_area(self):
        return round(math.pi*math.pow(self.radius,2),3)

c=eval(input("Enter Radius of a Circle:"))
c=Circle(c)
print("Radius of the Circle= ",c.get_radius())
print("Area of the Circle= ",c.calc_area())