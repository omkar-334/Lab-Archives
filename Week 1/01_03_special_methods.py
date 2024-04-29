class ABC:
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj1=ABC("abc",100)
obj2=ABC("xyz",45)

print(obj1.__repr__())
print(obj1.__len__())
print(obj1.__cmp__(obj2))


#OUTPUT -
'''
100
3
55
'''