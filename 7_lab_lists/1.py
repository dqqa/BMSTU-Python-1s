# Выполнил Жижин Никита. ИУ7-11Б
# Удалить все элементы целочисленного списка, имеющие свойство по варианту,
# за один цикл. Без del pop remove срезов
# 5. Отрицательные элементы

# Блок ввода
el_cnt = int(input(">>> Введите количество элементов в списке: "))
lst = []
for i in range(el_cnt):
    el = int(input(f">>> Введите элемент {i+1}: "))
    lst.append(el)

# Блок вычислений
cur = 0
for i in range(len(lst)):
    if lst[i] < 0:
        for j in range(i-1, cur-1, -1):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        cur += 1
lst = lst[cur:]

# Блок вывода
for i, el in enumerate(lst):
    print(f"lst[{i}]={el}")
