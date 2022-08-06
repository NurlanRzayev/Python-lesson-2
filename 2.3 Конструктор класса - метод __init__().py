class Person:

    def __init__(self,n,s,q=1):
        self.name=n
        self.surname=s
        self.skill=q
    def person_information(self):
        self.information='name:',self.name,'surname:',self.surname,'qualification:',self.skill#self.information='name :{} surname :{} qualification :{}'
        return self.information#return self.information.format(self.name,self.surname)
    def __del__(self):
        print('Good bye mr.',self.name,self.surname)

a=Person('Peter','Parker')
b=Person('Stive','Jobs')
c=Person('Bruce','Wayne')

print(a.person_information(),b.person_information(),c.person_information())
b.__del__()

input()
#В конце программы добавлена функция input() , чтобы программа не завершалась сама , пока не будет нажат enter , после или без ввода , потому что после
#завершения программы все переменные получают значение None и метод __del__ срабатывает автоматически для всех переменных
