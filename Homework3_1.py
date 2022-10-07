# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

a = int(input('Укажите количество чисел в списке: '))
numbrs = []
count = 0

for i in range(a):
    numbrs.append(randint(1,100))
    if i % 2:
        count = count + numbrs[i]

print(numbrs)
print(count)
