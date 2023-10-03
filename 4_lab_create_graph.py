# Написал Жижин Ниикта. ИУ7-11Б
import math

# Константы
size = 120  # Количество колонок, выделенное под график
# Функции
f1 = lambda x: (1+x**2)**0.5-x**3
f2 = lambda x: math.sin(x)

# Блок ввода
start_x, end_x, step = map(
    float, input(">>> Задайте область построения графика и шаг через пробел: ").split()
)
y_points = int(input(">>> Введите количество засечек на оси y: "))

# Отрисовка таблицы и подсчет значений
table = []
x = start_x
number = 0
draw_x_axis = False

print(f'\n{"Таблица значений для функций":^88}')
print(" " + "_" * 88)
print(f'|{"Номер":^10}|{"x":^25}|{"f1":^25}|{"f2":^25}|')
print(" " + "-" * 88)

while x <= end_x:
    number += 1
    cur_y1 = f1(x)
    cur_y2 = f2(x)
    print(f"|{number:^10}|{x:^25.6g}|{cur_y1:^25.6g}|{cur_y2:^25.6g}|")
    table.append((x, cur_y1))
    if cur_y1 <= 0:
        draw_x_axis = True
    x += step

print(" " + "-" * 88)

# Определение минимума и максимума функции
_max_digit_cnt = len(max([format(l[0], ".6g") for l in table], key=len))
_min = min(table, key=lambda x: x[1])[1]
_max = max(table, key=lambda x: x[1])[1]

print(f"Максимальное значение функции f1(x) на этом промежутке: {_max:.6g}")
print()

should_draw_graph = input(">>> Отрисовать график? (Д, н): ").lower()
if should_draw_graph in ("н", "n"):
    exit(0)
print()

# Отрисовка графика
# Засечки
point_step = (_max - _min) / (y_points - 1)
scale = size / (_max - _min)
last_y = 0
scale_ruler = " " * (_max_digit_cnt + 2)
for i in range(y_points):
    y_value = _min + point_step * i
    virt_y_pos = round((y_value - _min) * scale)
    f_y = format(y_value, ".6g")
    scale_ruler += " " * (virt_y_pos - last_y) + f"|{f_y}"
    last_y = virt_y_pos + len(f_y) + 1
print(scale_ruler)

# Вычисление позиции оси абсцисс
x_axis_pos = 0
if draw_x_axis:
    x_axis_pos = round(size * (1 - _max / (_max - _min)))

# Ось ординат
print("-" * (size + _max_digit_cnt + 4) + "> y")

# Ось абсцисс + сам график
for k, v in table:
    form_k = format(k, ".6g")
    print(f"{form_k:>{_max_digit_cnt}}| ", end="")
    if not draw_x_axis:
        virt_y_pos = round(size * ((v - _min) / (_max - _min)))
        assert virt_y_pos <= size  # debug
        print(" " * (virt_y_pos - 1) + "*")
    else:
        if v < 0:
            virt_y_pos = math.floor(x_axis_pos - x_axis_pos * (v / _min))
            print(" " * virt_y_pos + "*" + " " * (x_axis_pos - virt_y_pos - 1) + "|")
        elif v > 0:
            virt_y_pos = round((size - x_axis_pos) * (v / _max))
            print(" " * x_axis_pos + "|" + " " * virt_y_pos + "*")
        else:
            print(" " * x_axis_pos + "|")

print(" " * (_max_digit_cnt + x_axis_pos + 2) + "|")
print(" " * (_max_digit_cnt + x_axis_pos + 2) + "˅ x")
