# Выполнил Жижин Никита. ИУ7-11Б
# Найти столбец, имеющий определённое свойство по варианту
# 5. Наибольшее количество чисел, являющихся степенями 2
import math

# Блок ввода
y_size = int(input(">>> Введите количество строк в матрице: "))

matrix = []
for i in range(y_size):
    line = map(int, input(f">>> Введите строку {i+1}: ").split())
    matrix.append(list(line))

# Блок вычислений
max_count, ans_col = 0, None

for i in range(len(matrix[0])):
    cur_cnt = 0
    for j in range(y_size):
        if math.log2(matrix[j][i]) % 1 == 0:
            cur_cnt += 1

    if cur_cnt > max_count:
        max_count = cur_cnt
        ans_col = i

# Блок вывода
print(f"Найденный столбец под номером {ans_col}:")
for i in range(y_size):
    print(matrix[i][ans_col], end=" ")