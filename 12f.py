class A:
    c=5
    def __init__(self):
        self.c=6
        print("A")

class B(A):
    def __init__(self):
        print("B")
        
class C(B):
    def __init__(self):
        A.__init__(self)
        super().__init__()
        print("C")
        print(self.c)

C()