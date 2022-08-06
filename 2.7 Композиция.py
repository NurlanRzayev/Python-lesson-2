import math

class WinDoor:

    def __init__(self, x, y):
        self.square = x * y

class Room:

    def __init__(self, x, y, z):
        self.lenght = x
        self.width = y
        self.height = z
        self.wd = []
    def full_surface(self):
        return 2 * self.height * (self.lenght + self.width)
    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h)) # объект класса WinDoor создается и добавляется в self.wd
    def work_surface(self):
        new_square = self.full_surface()
        for i in self.wd:
            new_square -= i.square # это атрибут объекта класса WinDoor, а не класса Room
        return new_square
    def wallpapers(self, x, y):
        return math.ceil(self.work_surface() / x / y)

print('Размеры помещения:')
x = float(input('Длинна - '))
y = float(input('Ширина - '))
z = float(input('Высота - '))
r1 = Room(x, y, z)

flag = input('Есть неоклеиваемая поверхность? (1 - да, 2 - нет) ')
while flag == '1':
    w = float(input('Ширина - '))
    h = float(input('Высота - '))
    r1.add_wd(w, h)
    flag = input('Добавить еще? (1 - да, 2 - нет) ')

print('Размеры рулона:')
x = float(input('Длинна - '))
y = float(input('Ширина - '))

print('Площадь оклейки', r1.work_surface())
print('Количество рулонов', r1.wallpapers(x, y))
    


