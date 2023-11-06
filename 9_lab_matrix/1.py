# Выполнил Жижин Никита. ИУ7-11Б
# Даны массивы D и F. Сформировать матрицу A по формуле
# a[j,k] = sin(d[j]+f[k]).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.
import math


def get_avg_pos(lst):
    positive_only = [el for el in lst if el > 0]
    if positive_only:
        return sum(positive_only) / len(positive_only)
    else:
        return None


def input_lst(n):
    lst = []
    for i in range(n):
        el = int(input(f">>> Введите элемент {i+1}: "))
        lst.append(el)
    return lst


# Блок ввода
size = int(input(">>> Введите количество элементов в списках: "))
d, f = input_lst(size), input_lst(size)

# Блок вычислений
a = [[0] * size for _ in range(size)]
for j in range(size):
    for k in range(size):
        a[j][k] = math.sin(d[j] + f[k])
av = []
l = []

for line in a:
    avg = get_avg_pos(line)
    if avg is not None:
        cnt = sum(1 for i in line if i < avg)

        av.append(format(avg, ".5g"))
        l.append(cnt)
    else:
        av.append(None)
        l.append(None)

# Блок вывода
for i, line in enumerate(a):
    fmt = "".join([f"{i:>8.5g}" for i in line])
    print(f"a[{i}] = {fmt}; {av[i]=}; {l[i]=}")
