class Shape:
    def __init__(self,color):
        self.color=color
    
class Rectangle(Shape):
    def __init__(self,color,height,width):
        self.height=height
        self.width=width
        super().__init__(color)
       
    def calc_area(self):
        return self.height*self.width
    
    def Rect_Details(self):
        print("height: ",self.height)
        print("width: ",self.width)
        print("color: ",self.color)
        
    
class Triangle(Shape):
    def __init__(self,color,base,height):
        self.height=height
        self.base=base
        super().__init__(color)
        
    def calc_area(self):
        return (0.5)*self.height*self.base
    
    def Tring_Details(self):
        print("height: ",self.height)
        print("base: ",self.base)
        print("color: ",self.color)
        
h=eval(input("Enter Height of a Rectangle:"))
w=eval(input("Enter Weight of a Rectangle:"))
c=input("Enter color of Rectangle:")
r=Rectangle(c,h,w)
r.Rect_Details()
print("Area of Rectangle:",r.calc_area())
hi=eval(input("Enter Height of a Triangle:"))
b=eval(input("Enter Weight of a Triangle:"))
c=input("Enter color of Triangle:")
t=Triangle(c,hi,b)
t.Tring_Details()
print("Area of Triangle:",r.calc_area())