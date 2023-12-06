# Выполнил Жижин Никита. ИУ7-11Б
# Лабораторная работа №13 “База данных в текстовом файле”
import utils
import os


SPLITTER = ";;"


def print_menu():
    menu = [
        "Вывести содержимое БД.",
        "Добавить запись в конец базы данных.",
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
    open(file, "w").close()


def get_database(file: str):
    with open(file, encoding="utf-8") as db:
        while True:
            row = db.readline()
            if not row:
                break
            print(*[f"{c:12}" for c in row.split(SPLITTER)], sep="")


def append_db(file: str, data: list):
    with open(file, encoding="utf-8", mode="a") as db:
        db.write(f"{SPLITTER}".join([str(a) for a in data]) + "\n")


def search_db(file: str, item) -> list:
    with open(file, encoding="utf-8") as db:
        while True:
            row = db.readline()
            if not row:
                break
            row = row.split(SPLITTER)
            if item in row:
                return row


def search_db_multiple(file: str, items: list) -> list:
    if not isinstance(items, (list, tuple)):
        raise TypeError

    with open(file, encoding="utf-8") as db:
        while True:
            row = db.readline()
            if not row:
                break
            row = row.split(SPLITTER)
            if all(el in row for el in items):
                return row


def main():
    db_file = find_databases()
    while True:
        choice = print_menu()
        if choice == 1:
            get_database(db_file)
        elif choice == 2:
            data = input(
                ">>> Введите новую строку, разделяя каждый элемент через пробел: "
            ).split()
            append_db(db_file, data)
            print("Измененная БД:")
            get_database(db_file)
        elif choice == 3:
            data = input(">>> Введите элемент: ")
            row = search_db(db_file, data)
            if not row:
                print("Такой строки не существует!")
            else:
                print("Найденная строка:")
                print(*[f"{a:12}" for a in row], sep="")
        elif choice == 4:
            data = input(">>> Введите элементы, разделенные через пробел: ").split()
            row = search_db_multiple(db_file, data)
            if not row:
                print("Такой строки не существует!")
            else:
                print("Найденная строка:")
                print(*[f"{a:12}" for a in row], sep="")

        utils.press_anykey()
        utils.clear_terminal()


if __name__ == "__main__":
    main()
