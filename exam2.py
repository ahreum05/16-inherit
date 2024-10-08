class CalcParent1 :
    def __init__(self, a=0, b=0) :
        self.a = a
        self.b = b
        
    def plus(self, x, y) :
        print('CalcParent1')
        return x + y
    
    def minus(self, x, y) :
        return x - y
    
    def output1(self) :
        print('CalcParent1', self.a, self.b)

class CalcParent2 :
    def __init__(self, a=0, b=0) :
        self.a = a
        self.b = b
        
    def plus(self, x, y) :
        print('CalcParent2')
        return x + y
    
    def minus(self, x, y) :
        return x - y
    
    def multiply(self, x, y) :
        return x * y 
    
    def divide(self, x, y) :
        return x / y 
    
    def output2(self) :
        print('CalcParent2', self.a, self.b)
    
class CalcChild(CalcParent1, CalcParent2) :
    def __init__(self, a=7, b=8) :
        CalcParent1.__init__(self, 1, 2)
        CalcParent2.__init__(self, 3, 4)

calc = CalcChild()
print(calc.plus(10, 20))
print(calc.minus(10, 20))
print(calc.multiply(10, 20))
print(calc.divide(10, 20))

calc.output1()
calc.output2()

calc.a = 50
calc.b = 100
calc.output1()
calc.output2()