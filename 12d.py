import math
class Circle:
    def __init__(self,radius):
         self.radius=radius
    def get_radius(self):
        return self.radius
    def calc_area(self):
        return round(math.pi*math.pow(self.radius,2),3)
    
class Cylinder(Circle):
     def __init__(self,radius,height):
        super().__init__(radius)
        self.height=height
      
     def calc_area(self):
        self.area=2*math.pi*self.radius*self.height
        print("Area Of Cylinder:",round(self.area,3))
        
        
    
r=eval(input("Enter Radius of a Circle:"))
h=eval(input("Enter Height of a Cylender:"))
c=Cylinder(r,h)
print("Radius of the Circle= ",c.get_radius())
c.calc_area()