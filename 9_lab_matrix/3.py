# Выполнил Жижин Никита. ИУ7-11Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.


def input_matrix(size):
    lst = []
    for i in range(size):
        line = map(int, input(f">>> Введите элемент {i+1}: ").split())
        lst.append(list(line))
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


size = int(input(">>> Введите размер матрицы: "))
D = input_matrix(size)
print()
Z = input_matrix(size)

print()
pprint_mat(D, "D")
pprint_mat(Z, "Z")

G = []

for i, line in enumerate(D):
    count = 0
    _sum = sum(Z[i])
    for el in line:
        if el > _sum:
            count += 1
    G.append(count)

multiply_matrix(D, max(G))

print("После преобразований: ")
pprint_mat(D, "D")
pprint_lst(G, "G")