# Выполнил Жижин Никита. ИУ7-11Б
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы.

def input_matrix(n):
    lst = []
    for i in range(n):
        line = map(int, input(f">>> Введите элемент {i+1}: ").split())
        lst.append(list(line))
    return lst

def pprint_mat(mat):
    for i, l in enumerate(mat):
        fmt = "".join([f"{s:<8}" for s in l])
        print(f"mat[{i}] = {fmt}")

def rotate_right(mat: list):
    return tuple(zip(*mat[::-1]))


def rotate_left(mat):
    return tuple(zip(*mat))[::-1]


size = int(input(">>> Введите размер матрицы: "))

matrix = input_matrix(size)
print("Исходная матрица: ")
pprint_mat(matrix)

print()
print("Повернутая по часовой стрелке матрица: ")
rot_right = rotate_right(matrix)
pprint_mat(rot_right)

print()
print("Повернутая против часовой стрелки матрица: ")
rot_left = rotate_left(rot_right)
pprint_mat(rot_left)
