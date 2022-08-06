from random import randint
import itertools

class Person:

    count = itertools.count()

    def __init__(self, c):
        self.id = next(Person.count)
        self.command = c

class Hero(Person):

    level = 1

    def upLevel(self):
        self.level += 1

class Soldier(Person):

    my_hero = None

    def follow(self, hero):
        self.my_hero = hero.id

h1 = Hero(1)
h2 = Hero(2)

army1 = []
army2 = []

for i in range(20):
    n = randint(1, 2)
    if n == 1:
        army1.append(Soldier(n))
    else:
        army2.append(Soldier(n))

print(len(army1), len(army2))

if len(army1) > len(army2):
    h1.upLevel()
else:
    h2.upLevel()

army1[0].follow(h1)
print(army1[0].id, h1.id)        