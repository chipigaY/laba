# import random
# M = int(input('Введите кол-во строк: '))
# N = int(input('Введите кол-во столбцов: '))
#
# # Генерируем случайную матрицу
# matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
#
# # Получаем строки с четными индексами и выводим их
# even_rows = matrix[::2]  # Срез для получения строк с четными индексами
#
# # Выводим элементы строк с четными индексами
# for row in even_rows:
#     print(*row)
import random
from collections import deque

# 1. Генерация списка размером M×N и вывод элементов из строк с четными номерами
def generate_and_display_matrix(m, n):
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    print("\nЭлементы из строк с четными номерами (2, 4, ...):")
    for i in range(1, m, 2):  # Четные номера строк: индексы 1, 3, ...
        print(f"Строка {i + 1}: {matrix[i]}")

# 2. Циклический сдвиг элементов списка на n элементов вправо или вниз
def cyclic_shift(lst, n, direction="right"):
    if direction == "right":
        shifted = deque(lst)
        shifted.rotate(n)
        return list(shifted)
    elif direction == "down":
        shifted = list(zip(*lst))  # Транспонирование
        shifted = [cyclic_shift(list(row), n) for row in shifted]
        return [list(row) for row in zip(*shifted)]  # Обратно транспонируем

# 3. Работа с множествами
def sets_operations():
    set1 = {1, 2, 3, 4, 5}
    frozen_set1 = frozenset({4, 5, 6, 7, 8})
    union_result = set1.union(frozen_set1)
    intersection_result = set1.intersection(frozen_set1)

    print("\nМножество set1:", set1)
    print("Неизменяемое множество frozen_set1:", frozen_set1)
    print("Объединение множеств:", union_result)
    print("Пересечение множеств:", intersection_result)

M, N = 5, 6  # Размер матрицы
generate_and_display_matrix(M, N)

matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
for row in matrix:
    print(row)
print("\nСдвиг вправо на 2 элемента:")
for row in matrix:
    print("Исходная строка:", row)
    print("Сдвинутая строка:", cyclic_shift(row, 2, direction="right"))

print("\nСдвиг вниз на 1 элемент:")
shifted_matrix = cyclic_shift(matrix, 1, direction="down")
for row in shifted_matrix:
    print(row)

sets_operations()
