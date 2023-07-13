class A:
    def __init__(self, a, b, c):
        self.__a = a  
        self._b = b 
        self.c = c  

    def display(self):
        print("class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def display(self):
        print("class B:")
        try:
            
            print("a:", self.__a)  
        except AttributeError:
            print("a cannot be accessed as it is a private member")
        print("b:", self._b)
        print("c:", self.c)
        super().display()



b = B(34, 54, 23)
b.display()

