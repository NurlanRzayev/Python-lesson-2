from random import randint

class Warrior:

    health = 100

    def set_name(self, name):
        self.name = name
    def make_strike(self, enemy):
        enemy.health -= 20
        print(self.name, 'strike', enemy.name)
        print('%s = %d' %(enemy.name, enemy.health))

u1 = Warrior()
u2 = Warrior()
u1.set_name('unit1')
u2.set_name('unit2')

while u1.health > 0 and u2.health > 0:
    strike = randint(1, 2)
    if strike == 1:
        u1.make_strike(u2)
    else:
        u2.make_strike(u1)

print('Win:', end='')
if u1.health > u2.health:
    print(u1.name)
else:
    print(u2.name)