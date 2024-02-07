L = [10,20,30,40]

L.append(50)
print(L)        #[10, 20, 30, 40, 50]

L.append(60)
print(L) #[10, 20, 30, 40, 50,60]

L.append([70,80])
print(L)   #[10, 20, 30, 40, 50, 60, [70, 80]]

L.append("Rohit45")
print(L)        #[10, 20, 30, 40, 50, 60, [70, 80], 'Rohit45']

# print(L[6[1]])   #TypeError: 'int' object is not subscriptable

# L.append(70,80)    #TypeError: list.append() takes exactly one argument (2 given)


