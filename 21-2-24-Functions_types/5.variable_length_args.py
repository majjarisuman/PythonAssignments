#----------- exp1 ----------------
def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print("Sum:", result)   #Sum: 15

#------------ exp2 --------------
def my_function(*args):
    return " ".join(args)

result = my_function("Hello", "World", "Python", "Programming")
print("String:", result)   #String: Hello World Python Programming

#--------------- exp3 -----------------
def product_of_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

result = product_of_numbers(2, 3, 4, 5)
print("Product:", result)               #Product: 120

#------------- exp4 --------------
def average_num(*args):
    return sum(args) / len(args)

result = average_num(10, 15, 20, 25, 30)
print("Average:", result)           #Average: 20.0


#--------- exp5 ---------------
def My_func(*args):
    for element in args:
        print(element)

My_func("Apple", "Banana", "Orange", "Grapes", "Mango")
