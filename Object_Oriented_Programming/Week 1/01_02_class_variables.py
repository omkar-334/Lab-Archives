class ABC:
    class_var=0 #class variable
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var #object variable
        print('Object variable - ',var)
        print('Class variable - ',ABC.class_var)
    def hi(self):
        print("hi")
obj1=ABC(100)
obj2=ABC(200)
obj3=ABC(300)

#del method
del obj3
obj3.hi()


#OUTPUT -
'''
Object variable -  100
Class variable -  1
Object variable -  200
Class variable -  2
Object variable -  300
Class variable -  3

Traceback (most recent call last):
  File "c:\Users\omkar\Desktop\OOP\Unit 1\01_02_class_variables.py", line 16, in <module>
    obj3.hi()
NameError: name 'obj3' is not defined
'''