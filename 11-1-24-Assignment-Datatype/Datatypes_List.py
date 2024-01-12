#----------- List Datatype-----------------------------
 
# List Represent a group of values as single entity.
# List is mutable datatype. 
# Mutable means we can add,update,delete elements after list created.
# Duplicates are allowed in list.
# Insertion order is preserved.
# Indexing allowed.
# Slicing Allowed.
# List is Heterogeneous (Diff datatype values applicable.).
# List Should be enclosed within Square Brackets [].

# #Taking Empty List
# l = []

# #Printing datatype of list.
# print(type(l))    #<class 'list'>

# #appending elements in existing list.
# l.append(30)
# l.append(40)
# l.append(20)
# l.append(10)

# #printing list values
# print(l)           # [30, 40, 20, 10]

# # #list can be add different datatype values
# l.append("Rohit")
# l.append(45)
# l.append(True)
# l.append(200.3)

## print a list
# print(l)       # [30, 40, 20, 10, 'Rohit', 45, True, 200.3]

## arthimetic operations in list
# print("l+l =",l+l)    #l+l = [30, 40, 20, 10, 'Rohit', 45, True, 200.3, 30, 40, 20, 10, 'Rohit', 45, True, 200.3]

# print(l*l)   #TypeError: can't multiply sequence by non-int of type 'list'

lst = [10,20,"rohit",45.5]
# print(lst*3)
# #o/p:- [10, 20, 'rohit', 45.5, 10, 20, 'rohit', 45.5, 10, 20, 'rohit', 45.5]

# print(lst+lst)    #[10, 20, 'rohit', 45.5, 10, 20, 'rohit', 45.5]

# print(lst*lst)   #TypeError: can't multiply sequence by non-int of type 'list'

# print(lst-lst)   #TypeError: unsupported operand type(s) for -: 'list' and 'list'

# print(lst%lst)    #TypeError: unsupported operand type(s) for %: 'list' and 'list'

# print(lst/lst)     #TypeError: unsupported operand type(s) for /: 'list' and 'list'

# print(lst<=lst)   # True

# print(lst<lst)     #False

## Indexing
# print(lst[0])      # 10
# print(lst[-1])     # 45.5
# print(lst[2])      # rohit

## slicing
# print(lst[::])        #[10, 20, 'rohit', 45.5]
# print(lst[::-1])      #[45.5, 'rohit', 20, 10]