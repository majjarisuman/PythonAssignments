#pop()  function removes the last element or item in a list.
#       element based on the index given.

L = [10,20,30,40,"MSR","A","B"]
a=L.pop()
print(a)   #B
print(L)   #[10, 20, 30, 40, 'MSR', 'A']

b=L.pop(4)
print(b)   #MSR
print(L)   #[10, 20, 30, 40, 'A']

# print(L.pop("A"))    #TypeError: 'str' object cannot be interpreted as an integer

# print(L.pop(15))     #IndexError: pop index out of range

print(L)    #[10, 20, 30, 40, 'A']
print(L.pop(-1))   #A

# print(L.pop(-10))    #IndexError: pop index out of range
print(L)     #[10, 20, 30, 40]


#---------------------- Remove() -----------------------------------
#remove() function removes the first occurrence of the specified element.
#          it does not return any value.

L = [10,20,30,40,"MSR","A","B"]

# print(L.remove())   #TypeError: list.remove() takes exactly one argument (0 given)

# print(L.remove(2))    #ValueError: list.remove(x): x not in list

print(L.remove("MSR"))   #None
print(L)     #[10, 20, 30, 40, 'A', 'B']

print(L.remove(20))     #None
print(L)    #[10, 30, 40, 'A', 'B']

# print(L.remove(30,40))    #TypeError: list.remove() takes exactly one argument (2 given)

# print(L.remove([30,40]))   #ValueError: list.remove(x): x not in list

l = [10,20,30,20,20,40,"MSR","A","B"]

l.remove(20)
print(l)         #[10, 30, 20, 20, 40, 'MSR', 'A', 'B']

l.remove(20)
print(l)         #[10, 30, 20, 40, 'MSR', 'A', 'B']