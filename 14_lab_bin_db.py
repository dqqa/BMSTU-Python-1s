# Выполнил Жижин Никита. ИУ7-11Б.
# Лабораторная работа №14 “База данных в бинарном файле”
import struct
import utils
import os
from typing import Iterable

# Database architecture
# 1 field - int ID
# 2 field - string Name
# 3 field - unsigned short Age


def print_menu():
    menu = [
        "Вывести содержимое БД.",
        "Добавить запись в указанное место базы данных.",
        "Удалить запись по индексу.",
        "Поиск по одному полю.",
        "Поиск по двух полям.",
    ]

    for i, el in enumerate(menu):
        print(f"{i+1}. {el}")

    return utils.safe_menu_input(1, len(menu))


def find_databases():
    files = os.listdir()
    databases = []
    i = 0
    for file in files:
        if os.path.isfile(file) and file.endswith(".db"):
            i += 1
            databases.append(file)
            print(f"{i}. {file}")
    if databases:
        while not (
            1
            <= (
                selected_db := utils.safe_num_input(
                    ">>> Введите номер базы данных: ", int
                )
            )
            <= len(databases)
        ):
            print(f"Введите число в диапазоне [1-{len(databases)}]")
        return databases[selected_db - 1]
    else:
        print("В данной директории существующих баз данных не найдено.")
        name = input(">>> Введите название базы данных: ") + ".db"
        create_db(name)
        return name


def create_db(file: str):
    open(file, "wb").close()


def check_row(data: Iterable, types: Iterable):
    if len(data) != len(types):
        return False
    for col, _type in zip(data, types):
        if not isinstance(col, _type):
            return False
    return True


def read_rows_db(file):
    struct_fmt = "<I255sH"
    size = struct.calcsize(struct_fmt)
    with open(file, "rb") as fp:
        while True:
            data = fp.read(size)
            if not data:
                break
            (Id, Name, Age) = struct.unpack(struct_fmt, data)
            yield Id, Name.decode().split("\x00")[0], Age


def add_new_row(file, row: Iterable, index: int):
    struct_fmt = "<I255sH"
    size = struct.calcsize(struct_fmt)
    if not check_row(row, (int, bytes, int)):
        raise ValueError
    data = struct.pack(struct_fmt, *row)
    with open(file, "r+b") as fp:
        tmp_data = fp.read()
        fp.truncate(0)
        fp.seek(0)
        fp.write(tmp_data[: size * index] + data + tmp_data[size * (index) :])


def main():
    database = find_databases()
    while True:
        choice = print_menu()
        if choice == 1:
            for row in read_rows_db(database):
                print(row)
        elif choice == 2:
            while True:
                index = int(input(">>> Введите индекс, куда вставить строку: "))
                _id, name, age = input(
                    ">>> Введите ID, имя и возраст через пробел: "
                ).split()
                _id, age = int(_id), int(age)
                name = name.encode()
                try:
                    add_new_row(database, (_id, name, age), index)
                    break
                except ValueError:
                    print("Введено неверное значение! Попробуйте еще раз.")
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass


if __name__ == "__main__":
    main()
