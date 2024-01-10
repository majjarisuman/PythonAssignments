#tuple to list converting.

# t1 = list(11,22,33,55,76)     #TypeError: list expected at most 1 argument, got 5
# print((t1))      
# print(type(t1))

# t2 = (11,22,33,55,76)
# t3 = list(t2)
# print((t3))         #[11, 22, 33, 55, 76]
# print(type(t3))     #<class 'list'>
# t3.append(23)       #[11, 22, 33, 55, 76, 23]
# print(t3)
# t3.extend([45])    
# print(t3)           #[11, 22, 33, 55, 76, 23, 45]

# lst1 = [11, 22, 33, 55, 76, 23, 45]
# tuple1 = tuple(lst1)
# print(tuple1)         #(11, 22, 33, 55, 76, 23, 45)
# print(type(tuple1))   #<class 'tuple'> 