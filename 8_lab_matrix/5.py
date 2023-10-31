# Выполнил Жижин Никита. ИУ7-11Б
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю.
import math

# Блок ввода
y_size = int(input(">>> Введите количество строк в матрице: "))

matrix = []
for i in range(y_size):
    line = map(int, input(f">>> Введите строку {i+1}: ").split())
    matrix.append(list(line))

# Блок вычислений
max_val, min_val = 0, math.inf

for x in range(len(matrix[0])):
    for y in range(x):
        max_val = max(max_val, matrix[y][x])

for x in range(len(matrix[0])):
    for y in range(y_size-x, y_size):
        min_val = min(min_val, matrix[y][x])

# Блок вывода
print(f"Максиамльное значение над главной диагональю: {max_val}")
print(f"Минимальное значение под побочной диагональю: {min_val}")