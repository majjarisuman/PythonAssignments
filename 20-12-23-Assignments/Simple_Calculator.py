def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Calculator function
def calculator(operation, num1, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        return "Invalid operation"

# Change this to perform different operations: '+', '-', '*', '/'
operation = '-'  
number1 = 10
number2 = 5

result = calculator(operation, number1, number2)
print(f"{number1} {operation} {number2} =", result)
