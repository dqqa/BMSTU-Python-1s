# Выполнил Жижин Никита. ИУ7-11Б.
# Лабораторная работа №15 “Бинарные файлы”
import struct
import os
import utils

gnome_sort = __import__("11_lab_sort").gnome_sort


def print_menu():
    menu = [
        "Удалить все отрицательные числа",
        "После каждого отрицательного элемента добавить его удвоенное значение",
        "Гномья сортировка",
    ]

    for i, el in enumerate(menu):
        print(f"{i+1}. {el}")

    return utils.safe_menu_input(1, len(menu))


def delete_elements(file):
    print("Удаление элементов, меньших нуля")
    with open(file, "rb") as fp, open("temp.bin", "wb") as tmpf:
        while True:
            data = fp.read(4)
            if not data:
                break
            dec_number = struct.unpack("<i", data)[0]
            if dec_number < 0:
                continue
            tmpf.write(data)
            print(f"{dec_number} = 0x{data.hex()}, ", end="")
        print()
    os.remove(file)
    os.rename("temp.bin", file)


def double_element(file):
    print("Добавление удвоенного значения после каждого отрицательного элемента")
    with open(file, "rb") as fp, open("temp.bin", "wb") as tmpf:
        while True:
            data = fp.read(4)
            if not data:
                break
            dec_number = struct.unpack("<i", data)[0]
            tmpf.write(data)
            if dec_number >= 0:
                print(f"{dec_number} = 0x{data.hex()}, ", end="")
            else:
                doubled = struct.pack("<i", dec_number * 2)
                tmpf.write(doubled)
                print(
                    f"{dec_number} = 0x{data.hex()}, {dec_number*2} = 0x{doubled.hex()}, ",
                    end="",
                )

        print()
    os.remove(file)
    os.rename("temp.bin", file)


def sort(file):
    print("Сортировка")
    with open(file, "rb") as fp, open("temp.bin", "wb") as tmpf:
        elements = []
        while True:
            data = fp.read(4)
            if not data:
                break
            dec_number = struct.unpack("<i", data)[0]
            elements.append(dec_number)

        _, _, sorted_lst = gnome_sort(elements)
        for el in sorted_lst:
            data = struct.pack("<i", el)
            tmpf.write(data)
            print(f"{el} = 0x{data.hex()}, ", end="")
    os.remove(file)
    os.rename("temp.bin", file)


def main():
    filename = input(">>> Введите имя файла: ")
    if not (os.path.exists(filename) and os.stat(filename).st_size > 0):
        print("Такого файла не существует или он пуст.")
        elements = list(
            map(
                int,
                input(
                    ">>> Введите элементы для сохранения в файл через пробел: "
                ).split(),
            )
        )
        with open(filename, "wb") as fp:
            fp.write(struct.pack(f"<{len(elements)}i", *elements))

    choice = print_menu()
    if choice == 1:
        delete_elements(filename)
    elif choice == 2:
        double_element(filename)
    elif choice == 3:
        sort(filename)


if __name__ == "__main__":
    main()
