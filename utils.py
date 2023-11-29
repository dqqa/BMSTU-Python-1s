from typing import List
import os


def press_anykey():
    input("\nНажмите любую кнопку для продолжения...")


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def safe_menu_input(start, end):
    while True:
        usr_input = input(f">>> Выберите пункт ({start}-{end}): ")
        try:
            if not (start <= int(usr_input) <= end):
                print("Пожалуйста, введите число из заданного диапазона!")
            else:
                return int(usr_input)
        except ValueError:
            print("Введено неверное значение!")


def safe_input_list(n: int, _type):
    res = []
    for i in range(n):
        while True:
            try:
                el = _type(input(f">>> Введите {i+1} элемент: "))
                res.append(el)
                break
            except Exception as e:
                print("Ошибка при добавлении элемента в список!")
                print(e)
    return res


def pprint_lst(lst):
    for i, el in enumerate(lst):
        print(f"lst[{i}]={el}")


def pprint_table(col_names: List, rows: List[List], padding: int = 2) -> None:
    cols = len(col_names)
    max_length = 0
    for row in [col_names] + rows:
        for item in row:
            if isinstance(item, float):
                item = format(item, ".6g")
            else:
                item = str(item)

            max_length = max(max_length, len(item))

    max_length += padding

    print(" " + "-" * (max_length * cols + cols - 1))
    for col in col_names:
        print(f"|{col:^{max_length}}", end="")
    print("|")
    print(" " + "-" * (max_length * cols + cols - 1))

    for row in rows:
        for item in row:
            if isinstance(item, float):
                item = format(item, ".6g")
            print(f"|{item:^{max_length}}", end="")
        print("|")
    print(" " + "-" * (max_length * cols + cols - 1))


def safe_multiple_input(msg, _type, count, sep=" "):
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


def safe_num_input(msg, _type):
    while True:
        usr_input = input(msg)
        try:
            return _type(usr_input)
        except ValueError:
            print(f"Введено неверное значение ({usr_input!r})")
