# Выполнил Жижин Никита. ИУ7-11Б
# Удалить элемент с заданным индексом алгоритмически.

count = int(input(">>> Введите количество элементов в списке: "))

lst = []
for i in range(count):
    n = int(input(f"Введите {i + 1} элемент списка: "))
    lst.append(n)

ind = int(input(">>> Введите индекс элемента, который необходимо удалить начиная с 0: "))
lst = lst[:ind] + lst[ind+1:]

for i, val in enumerate(lst):
    print(f"lst[{i}] = {val}")
