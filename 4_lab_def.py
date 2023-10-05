import math

f = lambda x: x ** 2 - 25

size = 120
start_x, end_x, step = map(float, input("Введите начальное, конечное значения аргумента и шаг через пробел: ").split())
table = []
iter_cnt = math.floor((end_x - start_x) / step)
draw_x = True
_max_digit_cnt = 0

for i in range(iter_cnt + 1):
    x = start_x + step * i
    y = f(x)
    table.append((x, y))
    _max_digit_cnt = max(_max_digit_cnt, len(format(x, '.6g')))

if all(y > 0 for _, y in table) or all(y < 0 for _, y in table):
    draw_x = False
_max = max(table, key=lambda x: x[1])[1]
_min = min(table, key=lambda x: x[1])[1]

x_axis_pos = -2
if draw_x:
    x_axis_pos = round(size * (1 - _max / (_max - _min)))

print('-' * (_max_digit_cnt + size + 3) + '> y')
for x, y in table:
    print(f"{x:>{_max_digit_cnt}.6g}| ", end="")
    if not draw_x:
        y_pos = round(size * ((y - _min) / (_max - _min)))
        print(" " * (y_pos - 1) + "*")
    else:
        if y < 0:
            virt_y_pos = math.floor(x_axis_pos - x_axis_pos * (y / _min))
            print(" " * virt_y_pos + "*" + " " * (x_axis_pos - virt_y_pos - 1) + "|")
        elif y > 0:
            virt_y_pos = round((size - x_axis_pos) * (y / _max))
            print(" " * x_axis_pos + "|" + " " * virt_y_pos + "*")
        else:
            print(" " * x_axis_pos + "*")

print(" " * (_max_digit_cnt + x_axis_pos + 2) + "|")
print(" " * (_max_digit_cnt + x_axis_pos + 2) + "˅ x")
