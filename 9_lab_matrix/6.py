# Выполнил Жижин Никита. ИУ7-11Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.


def input_matrix(size):
    lst = []
    for i in range(size):
        line = map(int, input(f">>> Введите элемент {i+1}: ").split())
        lst.append(list(line))
    return lst


def input_lst(size):
    lst = []
    for i in range(size):
        el = int(input(f">>> Введите {i+1} элемент списка: "))
        lst.append(el)
    return lst


def pprint_mat(mat, name):
    for i, line in enumerate(mat):
        fmt = "".join([f"{s:<8}" for s in line])
        print(f"{name}[{i}] = {fmt}")
    print()


def pprint_lst(lst, name):
    for i, el in enumerate(lst):
        print(f"{name}[{i}] = {el}")
    print()


size = int(input(">>> Введите размер матриц: "))
A = input_matrix(size)
B = input_matrix(size)
C = []

for i in range(size):
    line = []
    for j in range(size):
        line.append(A[i][j] * B[i][j])
    C.append(line)
    
V = []
for i in range(size):
    _sum = 0
    for j in range(size):
        _sum += C[j][i]
    V.append(_sum)

pprint_mat(A, "A")
pprint_mat(B, "B")
pprint_mat(C, "B")
pprint_lst(V, "V")
