# Выполнил Жижин Никита. ИУ7-11Б
# Лабораторная работа №11 “Исследование методов сортировки”
# Алгоритм: "гномья" сортировка
import utils
import random
import time


def gnome_sort(lst: list):
    lst = lst.copy()
    start_time = time.time()

    i, j = 1, 2
    permutations = 0

    while i < len(lst):
        if lst[i - 1] < lst[i]:
            i, j = j, j + 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            permutations += 1
            i -= 1
            if i == 0:
                i, j = j, j + 1

    return time.time() - start_time, permutations, lst


def main():
    count = utils.safe_num_input(">>> Введите количество элементов в списке: ", int)
    input_lst = utils.safe_input_list(count, int)

    _, _, sorted_lst = gnome_sort(input_lst)
    utils.pprint_lst(sorted_lst)

    N1 = utils.safe_num_input(">>> Введите размерность N1: ", int)
    N2 = utils.safe_num_input(">>> Введите размерность N2: ", int)
    N3 = utils.safe_num_input(">>> Введите размерность N3: ", int)

    sorted_lst1 = list(range(N1))
    sorted_lst2 = list(range(N2))
    sorted_lst3 = list(range(N3))

    random_lst1 = [random.randint(-100, 100) for _ in range(N1)]
    random_lst2 = [random.randint(-100, 100) for _ in range(N2)]
    random_lst3 = [random.randint(-100, 100) for _ in range(N3)]

    reverse_sorted_lst1 = list(range(N1, -1, -1))
    reverse_sorted_lst2 = list(range(N2, -1, -1))
    reverse_sorted_lst3 = list(range(N3, -1, -1))

    t1, k1, _ = gnome_sort(sorted_lst1)
    t2, k2, _ = gnome_sort(sorted_lst2)
    t3, k3, _ = gnome_sort(sorted_lst3)

    t4, k4, _ = gnome_sort(random_lst1)
    t5, k5, _ = gnome_sort(random_lst2)
    t6, k6, _ = gnome_sort(random_lst3)

    t7, k7, _ = gnome_sort(reverse_sorted_lst1)
    t8, k8, _ = gnome_sort(reverse_sorted_lst2)
    t9, k9, _ = gnome_sort(reverse_sorted_lst3)

    utils.pprint_table(
        [
            "",
            "Время N1",
            "Перестановки N1",
            "Время N2",
            "Перестановки N2",
            "Время N3",
            "Перестановки N3",
        ],
        [
            ["Упорядоч.", t1, k1, t2, k2, t3, k3],
            ["Случайный", t4, k4, t5, k5, t6, k6],
            ["Обр. упоряд.", t7, k7, t8, k8, t9, k9],
        ],
    )


if __name__ == "__main__":
    main()
