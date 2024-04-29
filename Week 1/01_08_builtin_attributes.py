class ABC:
    def __init__(self,var,str):
        self.var=var
        self.str=str
    def display(self):
        print(self.var)
        print(self.str)

obj=ABC(90,"omkar")
obj.display()
print(obj.__dict__)
print(obj.__doc__)
print(ABC.__name__)
print(obj.__module__)
print(ABC.__bases__)


#OUTPUT -
'''
90
omkar
{'var': 90, 'str': 'omkar'}
None
ABC
__main__
(<class 'object'>,)
'''