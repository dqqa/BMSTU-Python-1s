# Выполнил Жижин Никита. ИУ7-11Б
# Рекурсивно вычислить определитель матрицы

def sub_matrix(mat: list[list], x: int, y: int) -> list[list]:
    mat = mat.copy()
    sub_mat = [[0] * (len(mat) - 1) for _ in range(len(mat)-1)]
    a, b = 0, 0

    for i in range(len(mat)):
        if i != x:
            for j in range(len(mat[0])):
                if j != y:
                    sub_mat[a][b] = mat[i][j]
                    b += 1
            a += 1
            b = 0

    return sub_mat


def determinant(mat: list[list], n: int) -> int:
    ans = 0
    if n == 1:
        return mat[0][0]
    elif n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        for i in range(n):
            sub_mat = sub_matrix(mat, 0, i)
            ans += ((-1) ** i) * mat[0][i] * determinant(sub_mat, n-1)
    return ans


def main():
    y_size = int(input(">>> Введите количество строк в матрице: "))

    matrix = []
    for i in range(y_size):
        line = map(int, input(f">>> Введите строку {i+1}: ").split())
        matrix.append(list(line))

    # print(sub_matrix(matrix, 0, 0))
    det = determinant(matrix, y_size)
    print(f"Вычисленный определитель матрицы: {det}")


if __name__ == "__main__":
    main()
