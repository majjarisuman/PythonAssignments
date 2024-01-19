#pro to find biggest of 3 given numbers , user input 

number = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))

if number > number2 and number > number3 :
    print(number,"Is Biggest Number")
elif number2 > number and number2 > number3:
    print(number2,"Is Biggest Number")
else :
    print(number3,"Is Biggest Number")
    
#--------------------------------------------------------
number = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))

if number > number2 and number > number3 :
    Largest = number
elif number2 > number and number2 > number3:
    Largest = number2
else :
    print(number3,"Is Biggest Number")
print("Largest number in given numbers is : ",Largest)