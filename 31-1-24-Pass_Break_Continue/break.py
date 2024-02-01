#break in a while loop
num = 0
while True:
    print(num)
    num += 1

    if num > 6:
        break

#break in a for loop
for i in range(10):
    print(i)

    if i ==7:
        print("Breaking out of the loop.")
        break

#Finding the first even number in a loop
for number in range(1, 10):
    if number % 2 == 0:
        print(f"The first even number is: {number}")
        break

#Exiting from nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

        if j == 1:
            print("Breaking out of the nested loop.")
            break


#Terminating a while loop based on a condition
number = 0

while number < 10:
    print(number)

    if number == 5:
        print("Breaking out of the while loop.")
        break

    number += 1

#Using break in a list comprehension.
numbers = [1, 2, 3, 4, 5, 6]
result = []

for num in numbers:
    if num == 4:
        break
    result.append(num)

print(result)

