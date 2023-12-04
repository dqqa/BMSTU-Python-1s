# Защита 11 лабораторной работы. Выполнил Жижин Никита. ИУ7-11Б
# Примечание: пока что можно вводить все операнды и операторы только разделенными через пробел
import re


def convert_to_polish(exp: str) -> str:
    exp = exp.split()
    result = ""

    op_stack = ["#"] # Необходимо, чтобы избежать проверок на пустоту
    stack = []

    for el in exp:
        if re.fullmatch(r"^[+-]?[0-9]+$", el): # Если число
            stack.append(int(el))
        else: # Если оператор
            if el == "(":
                op_stack.append(el)
            elif el == ")":
                while op_stack[-1] != "(":
                    stack.append(op_stack.pop())
                op_stack.pop()
            elif el in ("+", "-"):
                if op_stack[-1] == "(":
                    op_stack.append(el)
                else:
                    while op_stack[-1] not in ("#", "("):
                        stack.append(op_stack.pop())
                    op_stack.append(el)
            elif el in ("*", "/"):
                if op_stack[-1] == "(":
                    op_stack.append(el)
                else:
                    while op_stack[-1] not in ("#", "(", "+", "-"):
                        stack.append(op_stack.pop())
                    op_stack.append(el)

    while op_stack[-1] != "#":
        stack.append(op_stack.pop())
    
    result = " ".join(map(str, stack))

    return result


def operation(op: str, nums: list) -> list:
    if op == "*":
        nums[-2] *= nums[-1]
    elif op == "+":
        nums[-2] += nums[-1]
    elif op == "-":
        nums[-2] -= nums[-1]
    elif op == "/":
        nums[-2] //= nums[-1]

    del nums[-1]


def calc_polish(exp: str) -> int:
    nums = []
    elems = exp.split()

    for el in elems:
        if re.fullmatch(r"^[+-]?[0-9]+$", el):
            nums.append(int(el))
        else:
            operation(el, nums)

    return nums[0]


def main():
    expression = input(">>> Enter expression: ")
    print(f"Source: {expression}")

    converted = convert_to_polish(expression)
    print(f"Polish: {converted}")

    result = calc_polish(converted)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()

# Source: 1 + 3 * 2 + 4 / 2 * ( 3 - 4 )
# Polish: 1 3 2 * + 4 2 / 3 4 - * +
# Result: 5

# Source: 2 * ( 4 + 3 * 5 )
# Polish: 2 4 3 5 * + *
# Result: 38

# Source: 2 * 2 + 3 * 3
# Polish: 2 2 * 3 3 * +
# Result: 13