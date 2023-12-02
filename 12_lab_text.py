# Выполнил Жижин Никита. Группа ИУ7-11Б
# Лабораторная работа №12 “Текстовый процессор”
import utils
import re


TEXT = (
    "Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему. "
    "Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме гувернанткой, "
    "и объявила мужу, что не может жить с ним в одном доме. Положение это продолжалось уже третий день и му"
    "чительно чувствовалось и самими супругами, и всеми членами семьи, и домочадцами. Все члены семьи и"
    " домочадцы 1/2, что нет 81+9 смысла в их сожительстве и что на каждом постоялом дворе случай"
    "но сошедшиеся люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. Жена "
    "не выходила из своих комнат, мужа третий день не было дома. Дети бегали по всему дому, как потер"
    "янные; англичанка поссорилась с экономкой и написала записку приятельнице, прося приискать ей но"
    "вое место; повар ушел вчера со двора, 12/3 во время с5-1амого обеда; черная кухарка и кучер просили расчета."
)


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


def separate_by_lines(text: str) -> list[str]:
    lines = []
    splitted = text.split(" ")
    line_length = len(text) // 10
    current_line = ""
    for word in splitted:
        if len(current_line + word) > line_length:
            lines.append(current_line.strip())
            current_line = ""
        current_line += " " + word
    lines.append(current_line.strip())

    return lines


def left_align(text: list[str]):
    max_size = len(max(text, key=lambda x: len(x.strip())))
    for i in range(len(text)):
        text[i] = f"{text[i].strip():<{max_size}}"


def right_align(text: list[str]):
    max_size = len(max(text, key=lambda x: len(x.strip())))
    for i in range(len(text)):
        text[i] = f"{text[i].strip():>{max_size}}"


def width_align(text: list[str]):
    max_size = len(max(text, key=lambda x: len(x.strip())))
    for i in range(len(text)):
        text[i] = text[i].strip()
        gap_width, max_replace = divmod(
            max_size - len(text[i]) + text[i].count(" "), text[i].count(" ")
        )
        text[i] = (
            text[i]
            .replace(" ", " " * gap_width)
            .replace(" " * gap_width, " " * (gap_width + 1), max_replace)
        )


def replace_word(text: list[str], word: str, word_to_replace: str):
    for i in range(len(text)):
        if word_to_replace:
            text[i] = re.sub(f"{word}", word_to_replace, text[i])
        else:
            text[i] = re.sub(f"\\s*{word}\\s*", word_to_replace, text[i])


def solve_math(text: list[str]):
    regexp = r"(\d+)([\+\-\*\/])(\d+)"
    for i in range(len(text)):
        string = text[i]
        for obj in re.finditer(regexp, text[i]):
            a, op, b = obj.groups()
            a=int(a)
            b=int(b)
            result = 0
            match op:
                case "+":
                    result = a + b
                case "-":
                    result = a - b
                case "/":
                    result = a // b
                case "*":
                    result = a * b
            string = re.sub(f"{a}\{op}{b}", str(result), string)
        text[i] = string


def delete_shortest(text: list[str]):
    pass


def main():
    lines = separate_by_lines(TEXT)
    while True:
        usr_input = ask_menu()
        match usr_input:
            case 1:
                left_align(lines)
            case 2:
                right_align(lines)
            case 3:
                width_align(lines)
            case 4:
                word = input(">>> Введите слово, которое необходимо удалить: ")
                replace_word(lines, word, "")
            case 5:
                word = input(">>> Введите слово, которое необходимо удалить: ")
                new_word = input(f">>> Введите слово, на которое необходимо заменить {word}: ")
                replace_word(lines, word, new_word)
            case 6:
                solve_math(lines)
            case 7:
                delete_shortest(lines)
            case 8:
                exit(0)

        print(*lines, sep="\n")
        # utils.press_anykey()
        # utils.clear_terminal()


if __name__ == "__main__":
    main()
