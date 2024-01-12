##------------------- Frozenset ------------------------

#frozenset is immutable.
# we cant add or remeve elements.
# duuplicates are not allowed.
# heterogenious type.
#no indexing.
# no slicing.
# insertion order not preserved.

s ={10,20,30,40}
# print(type(s))

f = frozenset(s)   #<class 'set'>
# print(type(f))    #<class 'frozenset'>
# print(f)    #frozenset({40, 10, 20, 30})

# for i in f:
#     print(i, end = " ")    #40 10 20 30 

print(f.add(35))    #AttributeError: 'frozenset' object has no attribute 'add'