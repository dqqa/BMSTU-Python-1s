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
max_c, min_c = 0, 0

for c in range(y_size):
    s = 0
    for i in range(y_size):
        s += matrix[i][c]
    if s < min_sum:
        min_c = c
        min_sum = s
    if s > max_sum:
        max_c = c
        max_sum = s

for i in range(len(matrix[0])):
    matrix[i][max_c], matrix[i][min_c] = matrix[i][min_c], matrix[i][max_c]
    
# Блок вывода
for i, l in enumerate(matrix):
    fstr = "".join([f"{e:<8}" for e in l])
    print(f"matrix[{i}] = {fstr}")
