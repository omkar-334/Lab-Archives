class ABC:
    def __init__(self,pubvar,privar):
        self.pubvar=pubvar
        self.__privar=privar
    def display(self):
        print("Class Access public variable - ",self.pubvar)
        print("Class Access private variable (without operator) - ",end=" ")
        try:
            print(self.privar)
        except:
            print("NA")
        print("Class Acess private variable (with operator) - ",self.__privar)

obj=ABC(20,90)
obj.display()

print("-----x-----")
print("Main Access public variable - ",obj.pubvar)
try:
    print("Main Access private variable - ",obj.privar)
except:
    print("Attribute not found")


#OUTPUT -
'''
Class Access public variable -  20
Class Access private variable (without operator) -  NA
Class Acess private variable (with operator) -  90
-----x-----
Main Access public variable -  20
Attribute not found
'''