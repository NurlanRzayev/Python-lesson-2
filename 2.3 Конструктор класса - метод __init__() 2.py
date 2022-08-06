class Person:

    def __init__(self,n,s,q=1):
        self.name=n
        self.surname=s
        self.skill=q
    def person_information(self):
        self.information='name:',self.name,'surname:',self.surname,'qualification:',self.skill
        return self.information
    def __del__(self):
        print('Good bye mr.',self.name,self.surname)

staff=[Person('Peter','Parker',3),Person('Steve','Jobs',1),Person('Bruce','Wayne',2)]

for person in staff:
    print(person.person_information())

staff.sort(key=lambda p:p.skill)
del staff[0]

input()