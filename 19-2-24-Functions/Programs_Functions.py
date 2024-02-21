# write a functions which contains some number as argument and print square of that numbers in python
def print_square(number):
    square = number ** 2
    print(f"The square of {number} is: {square}")

print_square(3)      #9
print_square(5)      #25
print_square(7)      #49


# write a function given number is even or odd  in python ?
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

check_even_odd(6)    #even
check_even_odd(10)   #even
check_even_odd(11)   #odd


#write a function to find factorial of given numbers
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(-3))  #Factorial is not defined for negative numbers.
print(factorial(3))   #6


#2nd way program 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a number for factorial :"))
print(f"The factorial of {number} is: {factorial(number)}")    #The factorial of 6 is: 720


#writa a profram using function for addtion ,sub,mul,division
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

num1 = int(input("Enter a int value1 :"))
num2 = int(input("Enter a int value2 :"))

print(f"Addition: {num1} + {num2} = {add(num1, num2)}")     #Addition: 10 + 5 = 15
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")     #Subtraction: 10 - 5 = 5
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")   #Multiplication: 10 * 5 = 50
print(f"Division: {num1} / {num2} = {divide(num1, num2)}")       #Division: 10 / 5 = 2.0


print(f"Addition: {num1} + {num2} = {add(num1, num2)}")     #Addition: 23 + 11 = 34
print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")     #Subtraction:  23 - 11 = 12
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")   #Multiplication: 23 * 11 = 253
print(f"Division: {num1} / {num2} = {divide(num1, num2)}")       #Division: 23 / 11 = 2.090909090909091




