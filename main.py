def F(n):
    count = 0
    for x in n:
        if x.isnumeric():
            count += 1
    return count

n = input("Введите строку: ")
count = F(n)
print(f"Количество чисел в строке: {count}")