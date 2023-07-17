import math as m

class math_operation :
    def __init__(self,a = 20,b = 30) :
        self.a = a
        self.b = b
    
    def power(self):
        print(f"Square root of {self.a}: ",m.sqrt(self.a))
        print(f"Square root of {self.b}: ",m.sqrt(self.b))
        print(f"{self.a} power off {self.b}:",m.pow(self.a,self.b))

    def trigno(self):
        print(f"Sine of {self.a} :",m.sin(self.a))
        print(f"Sine of {self.b} :",m.sin(self.b))
        print(f"Cosine of {self.a} :",m.cos(self.a))
        print(f"Cosine of {self.b} :",m.cos(self.b))
        print(f"Tan of {self.a} :",m.tan(self.a))
        print(f"Tan of {self.b} :",m.tan(self.b))
    
    def basic(self):
        print(f"Additon of {self.a} and {self.b} is:",self.a + self.b)
        print(f"Subtraction of {self.a} and {self.b} is:",self.a - self.b)
        print(f"Multiplication of {self.a} and {self.b} is:",self.a * self.b)
        print(f"Division of {self.a} and {self.b} is:",self.a / self.b)

    def rest(self):
        print(f"Factorial of {self.a} is:",m.factorial(self.a))
        print(f"Factorial of {self.b} is:",m.factorial(self.b))
        print("Floor of 8.4 :",m.floor(8.4))
        print("Ceil of 21.8 :",m.ceil(21.8))
        print("Sum of list [4,5,6,7] is :",m.fsum([4,5,6,7]))