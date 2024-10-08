class CalcParent :
    def plus(self, x, y) :
        print("CalcParent")
        return x + y
    
    def minus(self, x, y) :
        return x - y
    
class CalcChild(CalcParent) :
    def plus(self, x, y) :
        super().plus(x, y)  # 부모클래스 함수 호출
        print("CalcChild")
        return x + y
    
    def multiply(self, x, y) :
        return x * y 
    
    def divide(self, x, y) :
        return x / y 

calc = CalcChild()
print(calc.plus(10, 20))
print(calc.minus(10, 20))
print(calc.multiply(10, 20))
print(calc.divide(10, 20))