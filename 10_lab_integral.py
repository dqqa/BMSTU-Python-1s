# Выполнил Жижин Никита. ИУ7-11Б
# Требуется написать программу для вычисления приближённого значения интеграла
# известной, заданной в программе, функции двумя разными методами (по варианту).
# 1 метод - срединных прямоугольников
# 2 метод - парабол
import math

func = lambda x: math.sin(x)  # Интегрируемая функция
func_primitive = lambda x: -math.cos(x)  # Первообразная


def safe_multiple_input(msg: str, _type, count: int, sep: str = " ") -> list:
    while True:
        mapped = []
        usr_input = input(msg).split(sep)
        all_done = True
        if len(usr_input) != count:
            print(
                f"Необходимо ввести {count} элементов, но было введено {len(usr_input)}"
            )
            continue
        for item in usr_input:
            try:
                converted = _type(item)
                mapped.append(converted)
            except Exception as e:
                all_done = False
                print(f"Вызвано исключение {e}")
                print(f"Введено неверное значение ({item!r})")
                break
        if all_done:
            return mapped


def safe_num_input(msg: str, _type):
    while True:
        usr_input = input(msg)
        try:
            return _type(usr_input)
        except ValueError:
            print(f"Введено неверное значение ({usr_input!r})")


def integrate_middle(f, start, stop, N):
    result = 0
    step = (stop - start) / N
    for i in range(N):
        result += f((i * step + (i + 1) * step) / 2 + start) * step
    return result


def integrate_parabolas(f, start: float, stop: float, N: int):
    N = math.ceil(N / 2) * 2

    step = (stop - start) / N
    result = 0
    for i in range(0, N, 2):
        result += (step / 3) * (
                f(step * i + start)
                + 4 * f(step * (i + 1) + start)
                + f(step * (i + 2) + start)
        )
    return result


def calc_with_prec(f, prec: float, max_attempts: int = None) -> tuple[int, float]:
    N = 2
    integral = f(N)
    integral_2 = f(N * 2)
    N *= 2
    i = 0
    while abs(integral - integral_2) > prec or (max_attempts and i <= max_attempts):
        i += 1
        integral = integral_2
        integral_2 = f(N * 2)
        N *= 2
    return N, integral_2


def err_abs(res1: float, res2: float) -> float:
    return abs(res2 - res1)


def err_rel(res1: float, res2: float) -> float:
    return abs(err_abs(res1, res2) / res2)


def main() -> None:
    N1 = safe_num_input(">>> Введите количество участков разбиения N1: ", int)
    N2 = safe_num_input(">>> Введите количество участков разбиения N2: ", int)
    a, b = safe_multiple_input(
        ">>> Введите начало и конец отрезка интегрирования через пробел: ", float, 2
    )

    i1 = integrate_middle(func, a, b, N1)
    i2 = integrate_middle(func, a, b, N2)
    i3 = integrate_parabolas(func, a, b, N1)
    i4 = integrate_parabolas(func, a, b, N2)
    prim_diff = func_primitive(b) - func_primitive(a)

    print(" " + "_" * 47)
    print(f"|{'':^15}|{'N1':^15}|{'N2':^15}|")
    print(" " + "-" * 47)
    print(f"|{'Метод 1':<15}|{i1:^15.6g}|{i2:^15.6g}|")
    print(f"|{'Метод 2':<15}|{i3:^15.6g}|{i4:^15.6g}|")
    print(" " + "-" * 47)

    min_prec = safe_num_input(">>> Введите необходимую точность: ", float)

    if abs(prim_diff - i2) > abs(prim_diff - i4):
        less_accurate = lambda x: integrate_middle(func, a, b, x)
        print(
            "Метод срединных прямоугольников менее точен по сравнению с методом парабол"
        )
    else:
        less_accurate = lambda x: integrate_parabolas(func, a, b, x)
        print(
            "Метод парабол менее точен по сравнению с методом срединных прямоугольников"
        )

    print(" " + "_" * 47)
    print(f"|{'Метод':^15}|{'Сред. прямоуг.':^15}|{'Парабол':^15}|")
    print(" " + "-" * 47)
    print(f"|{'Абс. погр.':<15}|{err_abs(i1, i2):^15.6g}|{err_abs(i3, i4):^15.6g}|")
    print(f"|{'Отн. погр.':<15}|{err_rel(i1, i2):^15.6g}|{err_rel(i3, i4):^15.6g}|")
    print(" " + "-" * 47)

    min_n, int_with_prec = calc_with_prec(less_accurate, min_prec)
    print(f"Вычисленное значение интеграла с точностью {min_prec}: {int_with_prec:.6g}")
    print(
        f"Для вычисления интеграла с заданной точностью требуется {min_n} участков разбиения"
    )


if __name__ == "__main__":
    main()
