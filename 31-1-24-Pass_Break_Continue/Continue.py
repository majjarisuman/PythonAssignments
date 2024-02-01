for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(f"Processing odd number: {number}")

# Using continue to skip specific values in a loop
for i in range(1, 6):
    if i == 3 or i == 5:
        continue
    print(f"Processing value: {i}")

numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        print(f"Skipping processing for negative number: {num}")
        continue
    print(f"Processing number: {num}")

# Using continue to skip strings in a list
mixed_list = [1, 'apple', 3, 'banana', 5]
for item in mixed_list:
    if isinstance(item, str):
        print(f"Skipping string: {item}")
        continue
    print(f"Processing item: {item}")


#Example1
for number in range(10):
    if number % 2 == 0:
        continue
    print(f"Odd number: {number}")

#Example2
for i in range(10):
    if i==5:
        continue
    print(f"Numbers :{i}")

#Example3
for i in range(5):
    if i == 2:
        print("Skipping iteration for i =", i)
        continue
    print("Processing iteration for i =", i)

#Example4
for i in range(3):
    for j in range(3):
        if j == 1:
            print("Skipping inner loop for j =", j)
            continue
        print(f"Processing inner loop for i = {i}, j = {j}")

#Example5
for i in range(10):
    if 3 <= i <= 6:
        print(f"Skipping iteration for i =", i)
        continue
    print(f"Processing iteration for i =", i)
