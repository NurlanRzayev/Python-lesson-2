from random import randint

class Warrior:

    health = 100

    def set_name(self, name):
        self.name = name
    def make_strike(self, enemy):
        enemy.health -= 20
        print(self.name, 'strike', enemy.name)
        print('%s = %d' %(enemy.name, enemy.health))

class Battle:

    result = 'No battle'

    def battle(self, u1, u2):

        while u1.health > 0 and u2.health > 0:
            strike = randint(1, 2)
            if strike == 1:
                u1.make_strike(u2)
            else:
                u2.make_strike(u1)
        if u1.health > u2.health:
            self.result = u1.name + ' win'
        else:
            self.result = u2.name + ' win'

    def who_win(self):
        print(self.result)

w1 = Warrior()
w2 = Warrior()
w1.set_name('unit1')
w2.set_name('unit2')

b = Battle()
b.battle(w1, w2)
b.who_win()

