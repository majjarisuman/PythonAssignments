# 1. Calculate the sum of all numbers from 1 to a given number.
sum = 0
number = int(input("Enter a number"))
for i in range(1,number+1):
    sum +=i
print(sum)   #given 5 output 15

# 2. Write a program to print multiplication table of a given number.
num = int(input("Enter a number :"))
for i in range(1,11):
    print(num,'*',i,'=',num*i)

# 3: Display numbers from a list using loop.
numbers = [11, 22, 33, 44, 55, 66]
for i in numbers:
    print(i)

# 4: Count the total number of digits in a number.
number = int(input("Enter a number: "))
num_digits = len(str(number))
print(f'Total number of digits in {number}: {num_digits}')

# 7: Print list in reverse order using a loop.
list1 = [11,22,33,44,55]
reversed_list=[]
for i in list1:
    reversed_list = [i]+reversed_list
print(reversed_list)

## another option
for i in list1[::-1]:
    print(i)

# 8: Display numbers from -10 to -1 using for loop.
for i in range(-10,0):
    print(i,end=' ')

# 9: Use else block to display a message “Done” after successful execution of for loop.
for i in range(5):
    print(i)
else:
    print("Done")

# 10: Write a program to display all prime numbers within a range.
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number) 

# 11 Reverse a given integer number.
number = int(input("Enter a numver"))
reversed_str = str(number)[::-1]
reversed_number = int(reversed_str)
print(reversed_number)

# 12: Use a loop to display elements from a given list present at odd index positions.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range(1, len(my_list), 2):
    print(my_list[index])

# 13: Calculate the cube of all numbers from 1 to a given number.
given_number = int(input("Enter a number:"))

for num in range(1, given_number + 1):
    cube = num ** 3
    print(f"The cube of {num} is: {cube}")

# 14: Find the sum of the series upto n terms.
n_terms = int(input('Enter a number'))

# Calculate the sum of the series
series_sum = n_terms * (n_terms + 1) // 2

print(f"The sum of the series up to {n_terms} terms is: {series_sum}")
