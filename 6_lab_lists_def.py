# Выполнил Жижин Никита. ИУ7-11Б
# Защита 6 лабораторной работы

cur = 0
lst = []
count = int(input("Введите количество чисел в списке: "))
for i in range(count):
    num = int(input(f"Введите число {i + 1}: "))
    lst.append(num)

for i in range(len(lst)):
    n = lst[i]
    is_prime = True
    for j in range(2, n // 2 + 1):
        if n % j == 0:
            is_prime = False
            break

    if not is_prime:
        for j in range(i - 1, cur - 1, -1):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        cur += 1
lst = lst[cur:]

for i in range(len(lst)):
    print(f"lst[{i}] = {lst[i]}")
