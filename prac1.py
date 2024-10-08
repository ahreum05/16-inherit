class Area:
    def __init__(self, b=0, h=0):
        self.base = b
        self.height = h
        
    def setArea(self, b, h):
        self.base = b
        self.height = h

    def setBase(self, b):
        self.base = b
        
    def setHeight(self, h):
        self.height = h
    
    def getBase(self):
        return self.base

    def getHeight(self):
        return self.height

class Rectangle(Area):
    def getArea(self):
        return self.base * self.height

class Triangle(Area):
    def getArea(self):
        return self.base * self.height / 2
    
r = Rectangle()
t = Triangle()
r.setArea(10.5, 20.5)
t.setArea(5.0, 9.0)
print("사각형의 넓이 :", r.getArea())
print("삼각형의 넓이 :", t.getArea())



