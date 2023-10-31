# Выполнил Жижин Никита. ИУ7-11Б
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов
import math

# Блок ввода
y_size = int(input(">>> Введите количество строк в матрице: "))

matrix = []
for i in range(y_size):
    line = map(int, input(f">>> Введите строку {i+1}: ").split())
    matrix.append(list(line))

# Блок вычислений
max_count, min_count = 0, math.inf
max_l, min_l = 0, 0
for i, l in enumerate(matrix):
    cnt = 0
    for e in l:
        if e < 0:
            cnt += 1

    if cnt < min_count:
        min_count = cnt
        min_l = i
    if cnt > max_count:
        max_count = cnt
        max_l = i

for i in range(len(matrix[0])):
    matrix[max_l][i], matrix[min_l][i] = matrix[min_l][i], matrix[max_l][i]

# Блок вывода
for i, l in enumerate(matrix):
    fstr = "".join([f"{e:<10}" for e in l])
    print(f"matrix[{i}] = {fstr}")