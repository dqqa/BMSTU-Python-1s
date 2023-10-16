# Выполнил Жижин Никита. ИУ7-11Б
# 5. Поменять местами элементы с характеристиками по варианту.
# Минимальный чётный и максимальный нечётный.

count = int(input(">>> Введите количество элементов в списке: "))

lst = []
for i in range(count):
    n = int(input(f"Введите {i + 1} элемент списка: "))
    lst.append(n)

min_even, max_odd = lst[0], lst[0]
for i in lst:
    if i % 2 == 0 and i < min_even:
        min_even = i
    elif i % 2 != 0 and i > max_odd:
        max_odd = i

min_even_ind, max_odd_ind = lst.index(min_even), lst.index(max_odd)
lst[min_even_ind], lst[max_odd_ind] = lst[max_odd_ind], lst[min_even_ind]

for i, val in enumerate(lst):
    print(f"lst[{i}] = {val}")
