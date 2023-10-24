# Выполнил Жижин Никита. ИУ7-11Б
# После каждого элемента целочисленного списка, имеющего свойство по
# варианту, добавить его удвоенное значение, без использования вложенных
# циклов. Без insert append срезов
# 5. Отрицательные элементы

# Блок ввода
el_cnt = int(input(">>> Введите количество элементов в списке: "))
lst = []
for i in range(el_cnt):
    el = int(input(f">>> Введите элемент {i+1}: "))
    lst.append(el)

# Блок вычислений
to_multiply = []
k = 0
for i in range(len(lst)):
    if lst[i] < 0:
        to_multiply.append(i + k)
        k += 1

i = 0
while i < len(lst):
    if i in to_multiply:
        lst.append(0)
        for j in range(len(lst) - 1, i, -1):
            lst[j] = lst[j - 1]
        lst[i + 1] = 2 * lst[i]
        i += 2
    else:
        i += 1

# Блок вывода
for i, el in enumerate(lst):
    print(f"lst[{i}]={el}")
