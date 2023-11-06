# Выполнил Жижин Никита. ИУ7-11Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.


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


def multiply_matrix(matrix, k):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= k

mat_size = int(input(">>> Введите размер матрицы G: "))
D = input_matrix(mat_size)

lst_size = int(input(">>> Введите размер списка L: "))
L = input_lst(lst_size)

R = []
for i in L:
    try:
        R.append(max(D[i-1]))
    except IndexError:
        pass

average = sum(R) / len(R)

pprint_mat(D, "D")
pprint_lst(L, "L")
pprint_lst(R, "R")
print(f"Среднее: {average:.6g}")