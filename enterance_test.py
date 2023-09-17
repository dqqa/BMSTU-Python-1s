# 04.09.2023
# Задача: поменять местами минимальный элемент в каждой строке квадратной матрицы с элементом, лежащим на главной диагонали
# Вывести матрицу, справа каждой строки количество нулей в строке

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for c, row in enumerate(matrix):
    _min = min(row)
    ind = row.index(_min)
    row[ind], matrix[n - ind - 1][n - c - 1] = matrix[n - ind - 1][n - c - 1], row[ind]

print()
print(*[" ".join(map(str, a + [a.count(0)])) for a in matrix], sep="\n")
