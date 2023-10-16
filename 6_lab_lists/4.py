# Выполнил Жижин Никита. ИУ7-11Б
# Найти наиболее длинную непрерывную последовательность по варианту.
# 10. Возрастающая последовательность отрицательных чисел, модуль которых
# является простым числом.
import math

count = int(input(">>> Введите количество элементов в списке: "))

lst = []
for i in range(count):
    n = int(input(f"Введите {i + 1} элемент списка: "))
    lst.append(n)

max_len = 0
cur_len = 0
last_i = -math.inf
for i in lst:
    is_prime = True
    for j in range(2, abs(i) // 2 + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        if i > last_i:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 0

        last_i = i
max_len = max(max_len, cur_len)

print(f"Максимальная длина такой возрастающей последовательности равна: {max_len}")
