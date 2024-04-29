class ABC:
    def __init__(self,var):
        self.var=var
    def add(self):
        self.var+=1
        print("After adding, ",end="")
        self.display()
    def display(self):
        print("Variable value - ",self.var)


obj=ABC(90)
obj.display()
obj.add()
obj.display()


#OUTPUT -
'''
Variable value -  90
After adding, Variable value -  91
Variable value -  91
'''