class Snow:

    def __init__(self, amount):
        self.snow = int(amount)
    def __call__(self, amount):
        self.snow = int(amount)
    def __add__(self, n):
        self.snow += n # этот метод ничего не возвращает, он просто вносит изменения в уже существующую переменную (атрибут)
    def __sub__(self, n):
        self.snow -= n
    def __mul__(self, n):
        self.snow *= n
    def __truediv__(self, n):
        self.snow //= n
    def makeSnow(self, row_amount):
        amount_row = self.snow // row_amount
        s = ''
        for i in range(amount_row):
            s += '*' * row_amount + '\n'
        s += (self.snow - amount_row * row_amount) * '*' # self.snow = amount_row * row_amount + остаток => остаток = self.snow - amount_row * row_amount
        if s[-1] == '\n': # если количество снежинок кратно row_amount, т. е. это условие эквивалентно: self.snow // row_amount == self.snow / row_amount
            s = s[:-1] # удаляем последний, ненужный переход на новую строку
        return s

a = Snow(23)
a + 42
a / 2
print(a.makeSnow(15))


    
