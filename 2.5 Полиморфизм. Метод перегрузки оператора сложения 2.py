from random import randint

class Animal:

    def __init__(self, a, b):
        self.prop1 = a
        self.prop2 = b
    def __add__(self, other):
        n = randint(1, 2)
        if n == 1:
            return Animal(self.prop1, other.prop2)
        else:
            return Animal(other.prop1, self.prop2)
    def __str__(self):
        return f'{self.prop2} {self.prop1}' # функция str должна возвращать строку

unit1 = Animal('dog', 'black')
unit2 = Animal('cat', 'white')
unit3 = unit1 + unit2
print(unit3)