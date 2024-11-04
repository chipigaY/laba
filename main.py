def F(n):
    count = 0
    for x in n:
        if x.isnumeric():
            count += 1
    return count

n = input("Введите строку: ")
count = F(n)
print(f"Количество чисел в строке: {count}")

new_n = ""
flag = True
for x in n:
    if x == '(':
        flag = False
    elif x == ')':
        flag = True
    elif flag:
        new_n += x
        print("Исходная строка без символов между скобками:",'(',new_n,')')
n = len(new_n)
lst = [int(new_n) for _ in range(n)]
count_zero = lst.count(0)
print("Количество элементов списка равных 0:", count_zero)
min_elem = min(lst)
sum_after_min = sum(lst[lst.index(min_elem) + 1:])
print("Сумма элементов списка после минимального элемента:", sum_after_min)
