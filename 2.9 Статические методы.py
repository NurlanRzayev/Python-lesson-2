# -*- coding: utf-8 -*- # строка нужна, чтобы не было ошибки Non-UTF-8 ..., без нее из-за латинской буквы h в комментарии ниже, с какого-то хуя выдается ошибка

from math import pi

class Cylinder:

    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)
    def __init__(self, diametr, high):
        self.__dict__['dia'] = diametr # в данном случае в __init__() мы не можем присваивать стандартным способом, так как уже присвоение первому свойству вызовет __setattr__(), но поскольку объект еще не обзовелся свойством h, которое нужно для передачи в make_area(), будет генерироваться исключение. Через словарь __dict__ мы можем менять значения свойств объекта, избегая вызов __setattr__()  
        self.__dict__['h'] = high
        self.__dict__['area'] = self.make_area(diametr, high)
    def __setattr__(self, attr, value):
        if attr == 'dia' or attr == 'h':
            self.__dict__[attr] = value
            self.__dict__['area'] = self.make_area(self.dia, self.h)
        elif attr == 'area':
            print('Нельзя изменять площадь на прямую!')

a = Cylinder(1, 2)
print(a.dia, a.h, a.area)
a.dia = 4.5
a.h = 3.3
print(a.dia, a.h, a.area)
a.area = 100
print(a.area)

        
