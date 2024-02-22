# function without arguments
def greet():
    return "Hello, how are you today?"

message = greet()
print(message)     #Hello, how are you today?


#get input from user input
def get_user_input():
    user_input = input("Enter a Name: ")
    print("You entered:", user_input)

get_user_input()    #You entered: Rohit 45


#calculation
def calculate():
    a = 5
    b = 3
    return a + b

result = calculate()
print("Result:", result)     #8


