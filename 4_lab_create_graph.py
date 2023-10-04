# Написал Жижин Ниикта. ИУ7-11Б
import math

# Константы
size = 120  # Количество колонок, выделенное под график

# Функции
f1 = lambda x: x**3 + 6.1 * x**2 - 35.4 * x - 25.7
f2 = lambda x: x**2 - math.cos(math.pi * x)
f3 = lambda x: (f1(x) ** 2 + f2(x) ** 2) ** 0.5

# Блок ввода
start_x, end_x, step = map(
    float, input(">>> Задайте область построения графика и шаг через пробел: ").split()
)
error = False
if end_x < start_x:
    print("Конечное значение должно быть больше начального!")
    error = True
if step < 0:
    print("Шаг не может быть отрицательным!")
    error = True

y_points = int(
    input(">>> Введите количество засечек на оси y (по умолчанию: 4): ") or 4
)

if not (4 <= y_points <= 8):
    print("Введите число от 4 до 8")
    error = True

if error:
    exit(1)

# Отрисовка таблицы и подсчет значений
table = []
num_iters = math.floor((end_x - start_x) / step)
draw_x_axis = True
positive_a2_vals = 0

print(f'\n{"Таблица значений для функций":^86}')
print(" " + "_" * 86)
print(f'|{"Номер":^10}|{"x":^18}|{"a1":^18}|{"a2":^18}|{"a3":^18}|')
print(" " + "-" * 86)

for i in range(num_iters+1):
    x = start_x + i * step
    cur_y1 = f1(x)
    cur_y2 = f2(x)
    cur_y3 = f3(x)
    table.append((x, cur_y1))

    print(f"|{i+1:^10}|{x:^18.6g}|{cur_y1:^18.6g}|{cur_y2:^18.6g}|{cur_y3:^18.6g}|")

    if cur_y2 > 0:
        positive_a2_vals += 1

    i += 1
    x += step

print(" " + "-" * 86)

if all(y < 0 for _, y in table) or all(y > 0 for _, y in table):
    draw_x_axis = False

# Определение минимума и максимума функции
_max_digit_cnt = len(max([format(l[0], ".6g") for l in table], key=len))
_min = min(table, key=lambda x: x[1])[1]
_max = max(table, key=lambda x: x[1])[1]

print(f"Количество положительных значений a2(x) на этом промежутке: {positive_a2_vals}")
print()

should_draw_graph = input(">>> Отрисовать график функции a1(x)? (Д, н): ").lower()
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
x_axis_pos = -2
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
