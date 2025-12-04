def is_year_leap(year):
    return 'True' if (year % 4 == 0) else 'False'

y = int(input('Введите номер года: '))
result = is_year_leap(y)
print(f'год {y}: {result}')