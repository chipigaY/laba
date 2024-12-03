import random

def find_min_elements(array1, array2):
    """Функция для нахождения наименьших элементов в двух массивах."""
    a = min(array1)  # Найти наименьший элемент в первом массиве
    b = min(array2)  # Найти наименьший элемент во втором массиве
    return a, b

def calculate_z(a, b):
    """Функция для вычисления значения z по формуле z = a + b / (a * b)."""
    z = (a + b) / (a * b)
    return z

# Генерируем массивы X и Y с случайными целыми числами
X = [random.randint(1, 100) for _ in range(15)]  # Массив X из 15 элементов
Y = [random.randint(1, 100) for _ in range(20)]  # Массив Y из 20 элементов

# Находим наименьшие элементы
a, b = find_min_elements(X, Y)

# Вычисляем z
z = calculate_z(a, b)

# Печатаем результаты
print("Массив X:", X)
print("Массив Y:", Y)
print("Наименьший элемент массива X (a):", a)
print("Наименьший элемент массива Y (b):", b)
print("Значение z:", z)

#2
def SortInc3(A, B, C):
    """Функция, упорядочивающая три значения A, B, C по возрастанию."""
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    return A, B, C

A1, B1, C1 = [random.randint(1, 100) for _ in range(3)]
A2, B2, C2 = [random.randint(1, 100) for _ in range(3)]

# Упорядочиваем первый набор (A1, B1, C1)
A1, B1, C1 = SortInc3(A1, B1, C1)
print("Упорядоченный набор (A1, B1, C1):", A1, B1, C1)

# Упорядочиваем второй набор (A2, B2, C2)
A2, B2, C2 = SortInc3(A2, B2, C2)
print("Упорядоченный набор (A2, B2, C2):", A2, B2, C2)

#3
def PowerN(X, N):
    """Рекурсивная функция для вычисления X^N."""
    if N == 0:
        return 1  # X^0 = 1
    elif N > 0:
        if N % 2 == 0:
            half_power = PowerN(X, N // 2)
            return half_power * half_power  # X^N = (X^(N/2))^2
        else:
            return X * PowerN(X, N - 1)  # X^N = X * X^(N-1)
    else:
        return 1 / PowerN(X, -N)  # X^N = 1 / X^(-N)

# Пример данных
X = float(input("Введите вещественное число X: "))

# Пять значений N
N_values = [random.randint(1, 100) for _ in range(5)]

# Вычисляем X^N для каждого значения N
for N in N_values:
    result = PowerN(X, N)
    print(f"Значение {X}^{N} = {result}")