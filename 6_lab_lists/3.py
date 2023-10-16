# Выполнил Жижин Никита. ИУ7-11Б
# Найти значение K-го экстремума в списке.

count = int(input(">>> Введите количество элементов в списке: "))

lst = []
for i in range(count):
    n = int(input(f"Введите {i + 1} элемент списка: "))
    lst.append(n)

ind = int(input(">>> Введите номер экстремума, начиная с 1: "))

ext = lst[0]
count = 0
for i in range(1, len(lst)-1):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
        count += 1
        ext = lst[i]
    if count == ind:
        break

print(f"{ind}-ый экстремум списка равен: {ext}")
