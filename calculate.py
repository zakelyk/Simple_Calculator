def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

def calculate(operand1, operand2, operator):
    if operator == "+":
        return format_number(operand1 + operand2)
    elif operator == "-":
        return format_number(operand1 - operand2)
    elif operator == "*":
        return format_number(operand1 * operand2)
    elif operator == "/":
        if operand2 == 0:
            return "Error"
        else:
            return format_number(operand1 / operand2)
