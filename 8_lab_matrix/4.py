# Выполнил Жижин Никита. ИУ7-11Б
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов.
import math

# Блок ввода
y_size = int(input(">>> Введите количество строк в матрице: "))

matrix = []
for i in range(y_size):
    line = map(int, input(f">>> Введите строку {i+1}: ").split())
    matrix.append(list(line))

# Блок вычислений
max_sum, min_sum = 0, math.inf
max_l, min_l = 0, 0
for i, l in enumerate(matrix):
    s = sum(l)
    if s < min_sum:
        min_l = i
        min_sum = s
    if s > max_sum:
        max_l = i
        max_sum = s

for i in range(len(matrix[0])):
    matrix[max_l][i], matrix[min_l][i] = matrix[min_l][i], matrix[max_l][i]
    
# Блок вывода
for i, l in enumerate(matrix):
    fstr = "".join([f"{e:<10}" for e in l])
    print(f"matrix[{i}] = {fstr}")