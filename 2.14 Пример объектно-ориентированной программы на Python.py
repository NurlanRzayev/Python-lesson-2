class Data:

    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Teacher:

    def __init__(self):
        self.work = 0
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1

class Pupil:

    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
    def lose(self):
        from random import randrange
        if self.knowledge:
            i = randrange(len(self.knowledge)) # = randint(len(self.knowledge) - 1)
            del self.knowledge
    
lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
marIvanna.teach(lesson[0], pety)
vasy.take(lesson[0])
print(vasy.knowledge)
print(pety.knowledge)    