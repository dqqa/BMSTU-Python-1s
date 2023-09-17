import math

size = 120 # columns
func = lambda x: math.cos(x)**-1
precision = 3

start_x, end_x, step = map(
    float, input("Задайте область построения графика и шаг через пробел: ").split()
)
table = {}

x = start_x
while x <= end_x:
    table[round(x, precision)] = round(func(x), precision)
    x += step

_max_digit_cnt = len(max(map(str, table.keys()), key=len))
_min, _max = min(table.items(), key=lambda x: x[1]), max(
    table.items(), key=lambda x: x[1]
)

print("-" * size + "> y")

for k, v in table.items():
    print(" " * (_max_digit_cnt - len(str(k))) + f"{k}| ", end='')
    if v > 0:
        pos = round(v / (_max[1] / (size / 2)))
        print(" " * (size // 2)
            + "|"
            + " " * (pos - 1)
            + "*"
        )
    elif v < 0:
        pos = round(v / (_min[1] / (size / 2 - 1)))
        print(" " * (size // 2 - pos - 1)
            + "*"
            + " " * (pos)
            + "|"
        )
    else:
        print(" " * (size // 2)+ "*")

print(" " * (_max_digit_cnt) + "|")
print(" " * (_max_digit_cnt) + "˅ x")
