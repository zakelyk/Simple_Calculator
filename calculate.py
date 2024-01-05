        
def format_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)) and result % 1 == 0:
            return int(result)
        else:
            return result
    return wrapper
    
@format_number
def calculate(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            return "Error"
        else:
            return operand1 / operand2