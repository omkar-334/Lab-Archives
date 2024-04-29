class ABC:
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("Class Access private method - ",self.__var)

obj=ABC(20)
obj._ABC__display()


#OUTPUT -
'''
Class Access private method -  20
'''