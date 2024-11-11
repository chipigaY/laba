from random import *
s = input("Введите строку: ")
print("Введенная строка:", s)
count = len(s)
print("Количество символов в строке:", count) # Подсчет количества символов

# Подсчет количества символов
import random

# Генерация списка с рандомными элементами
random_list = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", random_list)

# Очистка списка
random_list.clear()
print("Список после удаления всех элементов:", random_list)
# Подсчет количества элементов списка равных 0
n = int(input("Введите кол-во элементов списка: "))
n0 = int(input("Введите начало рандома от 0: "))
n1 = int(input("Введите конец рандома: "))
l = list()
for i in range(n):
    l.append(randint(n0,n1))
print(l)
cnt = 0
for i in l:
    if i == 0:
         cnt+=1
print(cnt)






