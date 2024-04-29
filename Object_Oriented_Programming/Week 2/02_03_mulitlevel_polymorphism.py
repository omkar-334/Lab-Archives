class person:
    def name(self):
        print("Name")

class teacher(person):
    def qual(self):
        print("Qualification")

class HOD(teacher):
    def exp(self):
        print("Experience")

hod=HOD()
hod.name()
hod.qual()
hod.exp()

#OUTPUT -
'''
Name
Qualification
Experience
'''