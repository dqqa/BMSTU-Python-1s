# Выполнил Жижин Никита. Группа ИУ7-11Б
# Лабораторная работа №12 “Текстовый процессор”
import utils


def ask_menu() -> int:
    print("Выберите желаемое действие.")

    print("1. Выровнять текст по левому краю.")
    print("2. Выровнять текст по правому краю.")
    print("3. Выровнять текст по ширине.")
    print("4. Удаление всех вхождений заданного слова.")
    print("5. Замена одного слова другим во всём тексте.")
    print(
        "6. Вычисление арифметических выражений над целыми числами внутри текста (умножение и деление)."
    )
    print("7. Найти и затем удалить cамое короткое по количеству слов предложение.")
    print("8. Выход из программы.")
    return utils.safe_menu_input(1, 8)


def separate_by_lines(text) -> list[str]:
    pass


def left_align(text):
    pass


def right_align(text):
    pass


def width_align(text):
    pass


def delete_word(text):
    pass


def replace_word(text):
    pass


def solve_math(text):
    pass


def delete_shortest(text):
    pass


def main():
    text = input(">>> Введите текст: ")
    lines = separate_by_lines(text)
    while True:
        usr_input = ask_menu()
        match usr_input:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                exit(0)

        utils.press_anykey()
        utils.clear_terminal()


if __name__ == "__main__":
    main()
