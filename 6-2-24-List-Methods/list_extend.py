L = [10,20,30,40]

L.extend("MSR")
print(L)      #[10, 20, 30, 40, 'M', 'S', 'R']

L.extend(["MSR"])
print(L)          #[10, 20, 30, 40, 'M', 'S', 'R', 'MSR']

# L.extend(50,60,70)
# print(L)           #TypeError: list.extend() takes exactly one argument (3 given)

L.extend([50,60,70])
print(L)             #[10, 20, 30, 40, 'M', 'S', 'R', 'MSR', 50, 60, 70]

L.extend(["Rohit45","Kohli18"])
print(L)             #[10, 20, 30, 40, 'M', 'S', 'R', 'MSR', 50, 60, 70, 'Rohit45', 'Kohli18']