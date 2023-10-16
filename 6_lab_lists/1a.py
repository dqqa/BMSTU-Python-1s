# Выполнил Жижин Никита. ИУ7-11Б
# Добавить элемент в заданное место списка (по индексу) с использованием
# любых средств Python.

count = int(input(">>> Введите количество элементов в списке: "))

lst = []
for i in range(count):
    n = int(input(f"Введите {i + 1} элемент списка: "))
    lst.append(n)

ind = int(input(">>> Введите индекс, куда вставить элемент начиная с 0: "))
value = int(input(f">>> Введите число для вставки по индексу {ind}: "))
lst.insert(ind, value)

for i, val in enumerate(lst):
    print(f"lst[{i}] = {val}")
