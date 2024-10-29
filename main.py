# def F(n):
#     sum1 = 0
#     for i in range(1, n + 1):
#         num = 2 * i - 1  # Формула
#         sum1 += num
#         print(f"Квадрат числа {i}: {sum1}")
#
# n = int(input("Введите целое число n: "))
# if n > 0:
#     F(n)
# else:
#     print("Число должно быть больше 0.")

def F(N):
    if N <= 0:
        return False

    while N % 3 == 0:
        N //= 3

    return N == 1


# Пример использования
N = int(input("Введите целое число N: "))
if N > 0:
    result = F(N)
    print(result)
else:
    print("Число должно быть больше 0.")





import math

#входные данные от пользователя

def F(x):
    if x > 0:
        return x ** 2
    elif 0 < x <= 1:
        return math.sin(x)
    else:
        return math.cos(x)
xo = float(input("Введите начальное значение x: "))
x1 = float(input("Введите конечное значение x: "))
dx = float(input("Шаг: "))
if x1 <= xo:
    print("Ошибка: Конечное значение x1 должно быть больше начального значения xo.")
else:
    x = xo
    while x >= x1:
        z = F(x)
        x += dx
        print(x**2)



