# Выполнил Жижин Никита. ИУ7-11Б
# Найти строку, имеющую определённое свойство по варианту
# 5. Наибольшее количество нулевых элементов.

# Блок ввода
# x_size = int(input(">>> Введите количество столбцов в матрице: "))
y_size = int(input(">>> Введите количество строк в матрице: "))

matrix = []
for i in range(y_size):
    line = map(int, input(f">>> Введите строку {i+1}: ").split())
    matrix.append(list(line))

# Блок вычислений
ans_line = None
max_count = 0
for i, l in enumerate(matrix):
    if l.count(0) > max_count:
        ans_line = i
        max_count = l.count(0)

# Блок вывода
print(f"Найденная строка под номером {ans_line}:")
print(*matrix[ans_line], sep=" ")