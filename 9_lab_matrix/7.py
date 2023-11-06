# Выполнил Жижин Никита. ИУ7-11Б
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1).


def input_3d_arr(lst, x, y, z):
    for i in range(x):
        for j in range(y):
            for k in range(z):
                el = int(input(f">>> Введите {(i,j,k)} элемент: "))
                lst[i][j][k] = el


def pprint_mat(mat, name):
    for i, line in enumerate(mat):
        fmt = "".join([f"{s:<8}" for s in line])
        print(f"{name}[{i}] = {fmt}")
    print()


X, Y, Z = map(
    int, input(">>> Введите размерность трехмерного списка через пробел: ").split()
)

lst = [[[0 for k in range(Z)] for j in range(Y)] for i in range(X)]
input_3d_arr(lst, X, Y, Z)

i = int(input(">>> Введите i: ")) - 1
pprint_mat(lst[i], f"lst[{i}]")
