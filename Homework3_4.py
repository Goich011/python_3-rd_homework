# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import re

a = int(input('Введите число: '))
numbrs = []

while a:
    numbrs.append(a % 2)
    a //= 2

numbrs.reverse()
list = str(numbrs)
print(re.sub(', ','',list)) #не знаю как удалить [ и ]
