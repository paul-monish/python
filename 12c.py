class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def Display(self):
        print("x and y co-ordinates are:",'(',self.x,',',self.y,')')
        
    def Translate(self,x,y):
        self.x+=y
        self.y+=x

x=eval(input("Enter X coordinate:"))
y=eval(input("Enter Y coordinate:"))
p=Point(x,y)
p.Display()
print("After Translate X and Y:")
p.Translate(x, y)
p.Display()