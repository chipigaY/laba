
n = int(input("Введите целое число n больше 0: "))

sum = 0

# Вычисляем квадрат числа n с помощью формулы
for i in range(1, 2*n, 2):
    sum += i
    print(sum)

print(f"Квадрат числа {n} равен {sum}")
