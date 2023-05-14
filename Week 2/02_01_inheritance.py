class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name - ",self.name)
        print("Age - ",self.age)

class teacher(person):
    def __init__(self,name,age,exp,area):
        person.__init__(self,name,age)
        self.exp=exp
        self.area=area
    def display(self):
        person.display(self)
        print("Experience - ",self.exp)
        print("Research Area - ",self.area)

class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def display(self):
        person.display(self)
        print("Course - ",self.course)
        print("Marks - ",self.marks)

T=teacher("padma",37,13,"English")
T.display()
print("")
S=student("omkar",19,"OOP",98)
S.display()


#OUTPUT -
'''
Name -  padma
Age -  37
Experience -  13
Research Area -  English

Name -  omkar
Age -  19
Course -  OOP
Marks -  98
'''