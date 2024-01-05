# def format_number(num):
#     if num % 1 == 0:
#         return int(num)
#     else:
#         return num

# def calculate(operand1, operand2, operator):
#     if operator == "+":
#         return format_number(operand1 + operand2)
#     elif operator == "-":
#         return format_number(operand1 - operand2)
#     elif operator == "*":
#         return format_number(operand1 * operand2)
#     elif operator == "/":
#         if operand2 == 0:
#             return "Error"
#         else:
#             return format_number(operand1 / operand2)


def calculate_decorator(func):
    def wrapper(a, b, operator):
        # print(f"Calculating {a} {operator} {b}")
        result = func(a, b, operator)
        # print(f"Result: {result}")
        return result
    return wrapper

@calculate_decorator
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"