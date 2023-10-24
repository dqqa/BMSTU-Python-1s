# Выполнил Жижин Никита. ИУ7-11Б
# Поиск элемента в списке строк по варианту.
# 4. Поиск элемента с наибольшим числом подряд идущих пробелов

# Блок ввода
el_cnt = int(input(">>> Введите количество элементов в списке: "))
lst = []
for i in range(el_cnt):
    el = input(f">>> Введите элемент {i+1}: ")
    lst.append(el)

# Блок вычислений
ans = None
max_count = 0
for i, el in enumerate(lst):
    cur_count = 0
    for s in el:
        if s == " ":
            cur_count += 1
        else:
            if max_count < cur_count:
                max_count = cur_count
                ans = i
    if max_count < cur_count:
        max_count = cur_count
        ans = i

# Блок вывода
print(f"Строка, содержащая наибольшее количество пробелов ({max_count}) под индексом {ans}: {lst[ans]!r}")
