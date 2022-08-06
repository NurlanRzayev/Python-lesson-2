from random import randint

class Warrior:
    
    health = 100

unit1 = Warrior()
unit2 = Warrior()

while unit1.health > 0 and unit2.health > 0:
    strike = randint(1, 2)
    if strike == 1:
        unit2.health = unit2.health - 20
        print('unit1 strike unit2:', unit2.health)
    else:
        unit1.health = unit1.health - 20
        print('unit2 strike unit1:', unit1.health)

if unit1.health > 0:
    print('unit1 win')
else:
    print('unit2 win')            



