# Выполнил Жижин Никита. ИУ7-11Б
# Изменение элемента в списке строк по варианту.
# 3. Замена всех заглавных согласных английских букв на строчные
import string

# Блок ввода
el_cnt = int(input(">>> Введите количество элементов в списке: "))
lst = []
for i in range(el_cnt):
    el = input(f">>> Введите элемент {i+1}: ")
    lst.append(el)

# Блок вычислений
for i in range(len(lst)):
    el = lst[i]
    should_change = False
    for j in range(len(el)):
        if el[j] in string.ascii_uppercase:
            should_change = True
            el = el[:j] + el[j].lower() + el[j+1:]
    if should_change:
        lst[i] = el


# Блок вывода
for i, el in enumerate(lst):
    print(f"lst[{i}]={el!r}")
