# Выполнил Жижин Никита. ИУ7-11Б
# Изменение элемента в списке строк по варианту.
# 3. Замена всех заглавных согласных английских букв на строчные

# Блок ввода
el_cnt = int(input(">>> Введите количество элементов в списке: "))
lst = []
for i in range(el_cnt):
    el = input(f">>> Введите элемент {i+1}: ")
    lst.append(el)

# Блок вычислений
# A --> 65
# ..
# Z --> 90
# ..
# a --> 97
# offset A -- a = 32

for i in range(len(lst)):
    el = lst[i]
    should_change = False
    for j in range(len(el)):
        if 65 <= ord(el[j]) <= 90:
            should_change = True
            el = el[:j] + chr(ord(el[j]) + 32) + el[j+1:]
    if should_change:
        lst[i] = el


# Блок вывода
for i, el in enumerate(lst):
    print(f"lst[{i}]={el!r}")
