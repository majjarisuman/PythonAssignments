rows = 5
for i in range(0, rows):
    for j in range(0, i):
        print(" ", end=" ")

    for k in range(0, rows - i):
        print("*", end=" ")
    print()


rows = 5

for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print("  ", end="")
    
    for k in range(i, 0, -1):
        print(f"{k} ", end="")  
    print()




#Example3
rows = 5
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ") 
    print()
