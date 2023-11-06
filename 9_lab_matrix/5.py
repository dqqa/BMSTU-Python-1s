# Выполнил Жижин Никита. ИУ7-11Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

VOWELS = 'aouei'
def input_matrix(size):
    lst = []
    for i in range(size):
        line = input(f">>> Введите элемент {i+1}: ").split()
        lst.append(list(line))
    return lst

def pprint_mat(mat, name):
    for i, line in enumerate(mat):
        fmt = "".join([f"{s!r:<8}" for s in line])
        print(f"{name}[{i}] = {fmt}")
    print()

mat_size = int(input(">>> Введите размер матрицы: "))
matrix = input_matrix(mat_size)

pprint_mat(matrix, "mat")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j].lower() in VOWELS:
            matrix[i][j] = "."

pprint_mat(matrix, "mat")