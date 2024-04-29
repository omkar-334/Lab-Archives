class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
    @classmethod
    def square(cls,side):
        return cls(side,side)
S=Rectangle.square(10)
S.area()


#OUTPUT -
'''
100
'''