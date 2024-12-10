import random

def find_min_elements(array1, array2):
    a = min(array1)
    b = min(array2)
    return a, b

def calculate_z(a, b):
    z = (a + b) / (a * b)
    return z

#массивы X и Y с случайными целыми числами
X = [random.randint(1, 100) for _ in range(15)]
Y = [random.randint(1, 100) for _ in range(20)]

#наименьшие элементы
a, b = find_min_elements(X, Y)

z = calculate_z(a, b)
print("Массив X:", X)
print("Массив Y:", Y)
print("Наименьший элемент массива X (a):", a)
print("Наименьший элемент массива Y (b):", b)
print("Значение z:", z)

#2
def SortInc3(A, B, C):
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    return A, B, C

A1, B1, C1 = [random.randint(1, 100) for _ in range(3)]
A2, B2, C2 = [random.randint(1, 100) for _ in range(3)]

#первый набор
A1, B1, C1 = SortInc3(A1, B1, C1)
print("Упорядоченный набор (A1, B1, C1):", A1, B1, C1)

#второй набор
A2, B2, C2 = SortInc3(A2, B2, C2)
print("Упорядоченный набор (A2, B2, C2):", A2, B2, C2)

#3
def PowerN(X, N):
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

X = float(input("Введите вещественное число X: "))
N_values = [random.randint(1, 50) for _ in range(5)]
for N in N_values:
    result = PowerN(X, N)
    print(f"Значение {X}^{N} = {result}")


# import random
# #1
# def F(A):
#     K = 1
#     sum1 = 0
#     while sum1 <= A:
#         sum1 += 1 / K
#         K += 1
#     return K - 1, sum1
#
# A = int(input("Введите число A > 1: "))
# if A <= 1:
#         raise ValueError("Ошибка")
# K, sum1 = F(A)
# print(f"Минимальное K: {K}, Сумма: {sum1}")
#
# #2
# def s(N):
#     current_sum = 0
#     for i in range(1, N + 1):
#         current_sum += 2 * i - 1
#         print(f"Квадрат числа {i}: {current_sum}")
#
#
# N = int(input("Введите число N > 0: "))
# if N <= 0:
#         raise ValueError("Ошибка")
# s(N)
#
# #3
# import math
#
# def calculate_speed_table():
#     g = 9.81
#     l = 10
#     print("Угол (°)\tСкорость (м/с)")
#     for alpha in range(0, 61, 5):  #углы от 0 до 60 градусов включительно
#         alpha_rad = math.radians(alpha)  #радианы
#         v = math.sqrt((4 / 3) * g * l * math.sin(alpha_rad))
#         print(f"{alpha}°\t\t{v:.2f} м/с")
#
# calculate_speed_table()


