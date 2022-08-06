class Rectangle:

    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)
    def __str__(self):
        rect = []
        for i in range(self.h):
            rect.append(self.s * self.w)
        rect = '\n'.join(rect)
        return rect
    def __add__(self, other):
        return Rectangle(self.w + other.w, self.h + other.h, self.s)

a = Rectangle(4, 2, 'w')
b = Rectangle(8, 3, 'z')
print(a) # функция print автоматически вызывает функцию str, в данном случае перегруженную в __str__
print(b)
print(a + b) # сложение подразумевает равенство чему-то, т. к. оператор слож. перегружен в данном случае тому что возвращает __add__, таким образом создается объект, который отправляется в функцию str, вызванную print автоматически
print(b + a)
