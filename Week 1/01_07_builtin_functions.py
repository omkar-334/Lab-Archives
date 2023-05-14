class ABC:
    def __init__(self,var,str):
        self.var=var
        self.str=str
    def display(self):
        print(self.var)
        print(self.str)

obj=ABC(90,"omkar")
obj.display()
print("")

print(hasattr(obj,'var'))
print(hasattr(obj,'str'))
print("")

print(getattr(obj,'var'))
print(getattr(obj,'str'))
print("")

setattr(obj,'var',50)
setattr(obj,'str',"natasha")
obj.display()
print("")

delattr(obj,'var')
obj.display()


#OUTPUT -
'''
90
omkar

True
True

90
omkar

50
natasha

Traceback (most recent call last):
  File "c:\Users\omkar\Desktop\OOP\Unit 1\01_07_builtin_functions.py", line 27, in <module>
    obj.display()
  File "c:\Users\omkar\Desktop\OOP\Unit 1\01_07_builtin_functions.py", line 6, in display
    print(self.var)
AttributeError: 'ABC' object has no attribute 'var'
'''