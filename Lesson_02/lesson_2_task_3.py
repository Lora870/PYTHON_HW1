import math

def square(side):
    return math.ceil(side * side)

number = float(input('Введите длину стороны квадрата: '))
print(f'Площадь квадрата равна: {square(number)}')