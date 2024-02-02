#Left angle triangle with stars
rows = 5
for i in range(1, rows + 1):
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()


#Left angle triangle with numbers
rows = 5
for i in range(1, rows + 1):
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(i, end=" ")
    print()


rows = 5
for i in range(1, rows + 1):
    for j in range(rows, i, -1):
        print(" ", end=" ")
    
    for k in range(i, 0, -1):
        print(k, end=" ")
    
    print()






