# Выполнил Жижин Никита. ИУ7-11Б
# Выполнить транспонирование квадратной матрицы.

# Блок ввода
y_size = int(input(">>> Введите количество строк в матрице: "))

matrix = []
for i in range(y_size):
    line = map(int, input(f">>> Введите строку {i+1}: ").split())
    matrix.append(list(line))

# Блок вычислений
for i in range(y_size):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Блок вывода
for i, l in enumerate(matrix):
    fstr = "".join([f"{e:<10}" for e in l])
    print(f"matrix[{i}] = {fstr}")