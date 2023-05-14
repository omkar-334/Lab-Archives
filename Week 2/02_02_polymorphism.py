class person:
    def __init__(self):
        pass

class person1:
    def __init__(self):
        print("omkar")

class person2:
    def __init__(self):
        print("natasha")

class derived1(person,person1,person2):
    o=person1()
    n=person2()
D=derived1()
print("")
class derived2(person1,person2):
    o=person1()
    n=person2()
E=derived2()

#OUTPUT -
'''
omkar
natasha

omkar
natasha
omkar
'''