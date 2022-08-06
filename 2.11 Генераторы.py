from random import random

def ranrator(quantity, minimum, maximum):
    while quantity > 0:
        yield random() * (maximum - minimum) + minimum
        quantity -= 1

a = ranrator(5, -2, 2)
for i in a:
    print(round(i, 2))