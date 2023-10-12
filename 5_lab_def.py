eps = float(input(">>> Введите точность вычислений eps: "))
y = 0
i = 0
while True:
    cur = ((-1) ** i) * 1 / (2 * i + 1)
    # print(cur)
    y += cur * 4
    if abs(cur) <= eps:
        break

    i += 1

print(f"Вычисленное значение Y равно: {y:.6g}")
